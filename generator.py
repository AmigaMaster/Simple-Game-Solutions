import json
from pathlib import Path

# Path to your solutions
SOLUTIONS_DIR = Path("solutions")
OUTPUT_JSON = Path("structure.json")


def scan_directory(path: Path) -> dict:
  """Recursive function to build the directory structure as a dictionary."""
  tree = {"name": path.name, "type": "directory", "children": []}

  # Sort for consistent order
  items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))

  for item in items:
    if item.name.startswith("."):
      continue  # Ignore hidden files/folders
    if item.is_dir():
      tree["children"].append(scan_directory(item))
    elif item.is_file():
      tree["children"].append({
          "name": item.name,
          "type": "file",
          "path": str(item.relative_to(SOLUTIONS_DIR)).replace(  # Relative path for web access
              "\\", "/"
          ),
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