from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
BRIEFS = ROOT / "briefs"
ARCHIVE = ROOT / "archive.html"

files = sorted(BRIEFS.glob("*.html"), reverse=True)

print(f"ROOT = {ROOT}")
print(f"BRIEFS = {BRIEFS}")
print(f"Found {len(files)} html files")

for f in files:
    print(f.name)

links = ""

for f in files:
    links += f'<a href="briefs/{f.name}">{f.stem}</a>\n'

html = ARCHIVE.read_text(encoding="utf-8")

html = re.sub(
    r'<!-- ARCHIVE_START -->.*?<!-- ARCHIVE_END -->',
    f'<!-- ARCHIVE_START -->\n{links}\n<!-- ARCHIVE_END -->',
    html,
    flags=re.S
)

ARCHIVE.write_text(html, encoding="utf-8")

print("Archive Updated")
