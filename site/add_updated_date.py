import os
import datetime
import re
from pathlib import Path

def update_frontmatter(file_path: Path):
    """Add or update 'updated:' in YAML frontmatter of a Markdown file."""
    # Get file modification time
    mtime = datetime.datetime.fromtimestamp(file_path.stat().st_mtime)
    updated_str = mtime.strftime("%B %-d, %Y")  # e.g., October 7, 2025

    text = file_path.read_text(encoding="utf-8")

    # Regex to detect YAML frontmatter
    frontmatter_pattern = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
    match = frontmatter_pattern.match(text)

    if match:
        frontmatter = match.group(1)
        if re.search(r"^updated:", frontmatter, re.MULTILINE):
            # Replace existing updated field
            frontmatter = re.sub(
                r"^updated:.*$",
                f"updated: {updated_str}",
                frontmatter,
                flags=re.MULTILINE,
            )
        else:
            # Append updated field
            frontmatter += f"\nupdated: {updated_str}"
        new_text = f"---\n{frontmatter}\n---" + text[match.end():]
    else:
        # No frontmatter: create one at the top
        new_text = f"---\nupdated: {updated_str}\n---\n\n{text}"

    file_path.write_text(new_text, encoding="utf-8")
    print(f"✅ Updated: {file_path}")

def update_all_markdown(root_dir="."):
    """Recursively process all .md files in the given directory."""
    for path in Path(root_dir).rglob("*.md"):
        # Skip hidden or build directories
        if any(part.startswith("_") for part in path.parts):
            continue
        update_frontmatter(path)

if __name__ == "__main__":
    root = Path(".")
    update_all_markdown(root)
