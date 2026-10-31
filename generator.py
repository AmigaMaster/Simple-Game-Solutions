import json
import datetime
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote
from xml.sax.saxutils import escape as xml_escape

# Path to your solutions
SOLUTIONS_DIR = Path("solutions")
OUTPUT_JSON = Path("structure.json")
OUTPUT_SITEMAP = Path("sitemap.xml")
BASE_URL = "https://amigamaster.github.io/Simple-Game-Solutions"

# Allowed text/documentation file extensions (images and binaries will be ignored)
ALLOWED_EXTENSIONS = {".md", ".txt"}

# Files that are not walkthroughs (paths relative to SOLUTIONS_DIR, posix style)
EXCLUDED_FILES = {"Template-EN.md"}


def get_last_modified(file_path: Path) -> str:
    """Get the latest modified date from Git (if available), otherwise from file system."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cI", str(file_path)],
            capture_output=True,
            text=True,
            check=True
        )
        date_str = result.stdout.strip()
        if date_str:
            return date_str
    except Exception:
        pass
    
    mtime = file_path.stat().st_mtime
    return datetime.datetime.fromtimestamp(mtime, datetime.timezone.utc).isoformat()


def analyze_file(file_path: Path) -> tuple[int, int]:
    """Read file content and calculate number of words and actions (- )."""
    try:
        content = file_path.read_text(encoding="utf-8")
        words = len(content.split())
        actions = sum(1 for line in content.splitlines() if line.strip().startswith("- "))
        return words, actions
    except Exception as exc:
        # Do not hide unreadable files (e.g. wrong encoding): show a warning in the Actions log
        print(f"::warning file={file_path.as_posix()}::Could not analyze file: {exc}", file=sys.stderr)
        return 0, 0


def scan_directory(path: Path, sitemap_entries: list) -> tuple[dict, int, int, int]:
    """Recursive function to build the directory structure and collect sitemap entries."""
    tree = {"name": path.name, "type": "directory", "children": []}
    total_files = 0
    total_words = 0
    total_actions = 0

    # Sort for consistent order
    items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))

    for item in items:
        if item.name.startswith("."):
            continue  # Ignore hidden files/folders
            
        if item.is_dir():
            sub_tree, sub_files, sub_words, sub_actions = scan_directory(item, sitemap_entries)
            if sub_tree["children"]:
                tree["children"].append(sub_tree)
                total_files += sub_files
                total_words += sub_words
                total_actions += sub_actions
                
        elif item.is_file() and item.suffix.lower() in ALLOWED_EXTENSIONS:
            rel_path = item.relative_to(SOLUTIONS_DIR).as_posix()
            if rel_path in EXCLUDED_FILES:
                continue
            last_mod = get_last_modified(item)
            words, actions = analyze_file(item)
            
            tree["children"].append({
                "name": item.stem,
                "type": "file",
                "path": rel_path,
                "last_modified": last_mod,
                "words": words,
                "actions": actions,
            })
            
            # The web app opens solutions via ?file=<path> (same URL format as the app's share links).
            # There are no static .html pages, so the sitemap must not point to them.
            sitemap_entries.append({
                "loc": f"{BASE_URL}/?file={quote(rel_path, safe='')}",
                "lastmod": last_mod
            })
            total_files += 1
            total_words += words
            total_actions += actions
            
    return tree, total_files, total_words, total_actions


def newest_lastmod(entries: list) -> str:
    """Newest lastmod of all entries (deterministic, so sitemap.xml only changes when content changes)."""
    newest = None
    for entry in entries:
        try:
            dt = datetime.datetime.fromisoformat(entry["lastmod"])
        except ValueError:
            continue
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=datetime.timezone.utc)
        if newest is None or dt > newest[0]:
            newest = (dt, entry["lastmod"])
    if newest:
        return newest[1]
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def main():
    if not SOLUTIONS_DIR.exists():
        print(
            f"Folder {SOLUTIONS_DIR} not found. Please create the directory"
            " structure.",
            file=sys.stderr
        )
        sys.exit(1)  # fail the workflow instead of deploying an incomplete site

    sitemap_entries = []
    data, total_files, total_words, total_actions = scan_directory(SOLUTIONS_DIR, sitemap_entries)

    output_data = {
        "stats": {
            "total_files": total_files,
            "total_words": total_words,
            "total_actions": total_actions
        },
        "name": data["name"],
        "type": data["type"],
        "children": data["children"]
    }

    # 1. Write structure.json
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    print(f"Structure successfully written to {OUTPUT_JSON}.")

    # 2. Build sitemap.xml
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        'xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 '
        'http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd" '
        'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]

    # Add root index page entry
    xml_lines.append("  <url>")
    xml_lines.append(f"    <loc>{xml_escape(BASE_URL + '/')}</loc>")
    xml_lines.append(f"    <lastmod>{newest_lastmod(sitemap_entries)}</lastmod>")
    xml_lines.append("  </url>")

    # Sort entries alphabetically by URL location for clean output
    sitemap_entries = sorted(sitemap_entries, key=lambda x: x["loc"])

    for entry in sitemap_entries:
        xml_lines.append("  <url>")
        xml_lines.append(f"    <loc>{xml_escape(entry['loc'])}</loc>")
        xml_lines.append(f"    <lastmod>{entry['lastmod']}</lastmod>")
        xml_lines.append("  </url>")

    xml_lines.append("</urlset>")

    with open(OUTPUT_SITEMAP, "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines) + "\n")

    print(f"Sitemap successfully written to {OUTPUT_SITEMAP}.")


if __name__ == "__main__":
    main()
