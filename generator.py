import json
import datetime
import subprocess
from pathlib import Path

# Path to your solutions
SOLUTIONS_DIR = Path("solutions")
OUTPUT_JSON = Path("structure.json")

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


def scan_directory(path: Path) -> dict:
  """Recursive function to build the directory structure as a dictionary."""
  tree = {"name": path.name, "type": "directory", "children": []}

  # Sort for consistent order
  items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))

  for item in items:
    if item.name.startswith("."):
      continue  # Ignore hidden files/folders
    if item.is_dir():
      sub_tree = scan_directory(item)
      if sub_tree["children"]:
        tree["children"].append(sub_tree)
    elif item.is_file():
      if item.suffix.lower() in ALLOWED_EXTENSIONS:
        tree["children"].append({
            "name": item.stem,
            "type": "file",
            "path": str(item.relative_to(SOLUTIONS_DIR)).replace(
                "\\", "/"
            ),
            "last_modified": get_last_modified(item),
        })
  return tree


def main():
  if not SOLUTIONS_DIR.exists():
    print(
        f"Folder {SOLUTIONS_DIR} not found. Please create the directory"
        " structure."
    )
    return

  data = scan_directory(SOLUTIONS_DIR)

  with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

  print(f"Structure successfully written to {OUTPUT_JSON}.")


if __name__ == "__main__":
  main()