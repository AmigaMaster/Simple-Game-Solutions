import json
import datetime
import subprocess
from pathlib import Path
from urllib.parse import quote

# Path to your solutions
SOLUTIONS_DIR = Path("solutions")
OUTPUT_JSON = Path("structure.json")
OUTPUT_SITEMAP = Path("sitemap.xml")
BASE_URL = "https://amigamaster.github.io/Simple-Game-Solutions"

# Allowed text/documentation file extensions (images and binaries will be ignored)
ALLOWED_EXTENSIONS = {".md", ".txt"}


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


def scan_directory(path: Path, sitemap_entries: list) -> dict:
    """Recursive function to build the directory structure and collect sitemap entries."""
    tree = {"name": path.name, "type": "directory", "children": []}

    # Sort for consistent order
    items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))

    for item in items:
        if item.name.startswith("."):
            continue  # Ignore hidden files/folders
        if item.is_dir():
            sub_tree = scan_directory(item, sitemap_entries)
            if sub_tree["children"]:
                tree["children"].append(sub_tree)
        elif item.is_file():
            if item.suffix.lower() in ALLOWED_EXTENSIONS:
                rel_path = item.relative_to(SOLUTIONS_DIR).as_posix()
                # Map source extension to compiled .html extension
                html_rel_path = str(Path(rel_path).with_suffix(".html"))
                last_mod = get_last_modified(item)
                
                tree["children"].append({
                    "name": item.stem,
                    "type": "file",
                    "path": rel_path,
                    "last_modified": last_mod,
                })
                
                sitemap_entries.append({
                    "loc": f"{BASE_URL}/solutions/{html_rel_path}",
                    "lastmod": last_mod
                })
    return tree


def main():
    if not SOLUTIONS_DIR.exists():
        print(
            f"Folder {SOLUTIONS_DIR} not found. Please create the directory"
            " structure."
        )
        return

    sitemap_entries = []
    data = scan_directory(SOLUTIONS_DIR, sitemap_entries)

    # 1. Write structure.json
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
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
    root_lastmod = datetime.datetime.now(datetime.timezone.utc).isoformat()
    xml_lines.append("  <url>")
    xml_lines.append(f"    <loc>{quote(BASE_URL + '/', safe=':/%()')}</loc>")
    xml_lines.append(f"    <lastmod>{root_lastmod}</lastmod>")
    xml_lines.append("  </url>")

    # Sort entries alphabetically by URL location for clean output
    sitemap_entries = sorted(sitemap_entries, key=lambda x: x["loc"])

    for entry in sitemap_entries:
        # Properly percent-encode special characters (like %20 and %27) without escaping via &apos;
        encoded_loc = quote(entry["loc"], safe=":/%()")
        xml_lines.append("  <url>")
        xml_lines.append(f"    <loc>{encoded_loc}</loc>")
        xml_lines.append(f"    <lastmod>{entry['lastmod']}</lastmod>")
        xml_lines.append("  </url>")

    xml_lines.append("</urlset>")

    with open(OUTPUT_SITEMAP, "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines) + "\n")

    print(f"Sitemap successfully written to {OUTPUT_SITEMAP}.")


if __name__ == "__main__":
    main()