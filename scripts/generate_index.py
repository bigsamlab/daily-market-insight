from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
BRIEFS = ROOT / "briefs"

# 获取所有日报（按文件名倒序）
reports = sorted(BRIEFS.glob("*.html"), reverse=True)

if not reports:
    raise SystemExit("No reports found.")

latest = reports[0]

# ========= Hero 按钮 =========
html = INDEX.read_text(encoding="utf-8")

html = re.sub(
    r'(<a class="btn" id="today-report-btn" href=")[^"]*(">)',
    rf'\1briefs/{latest.name}\2',
    html,
)

# ========= 最新日报 =========
latest_block = f"""
<!-- AUTO_LATEST_REPORT_START -->
<div class="card report-card" id="latest-report">

<h3>{latest.stem} 日报</h3>

<p>
点击查看最新生成的 AI 与网络通信市场情报日报。
</p>

<a class="read-btn" href="briefs/{latest.name}">
阅读全文 →
</a>

</div>
<!-- AUTO_LATEST_REPORT_END -->
"""

html = re.sub(
    r'<!-- AUTO_LATEST_REPORT_START -->.*?<!-- AUTO_LATEST_REPORT_END -->',
    latest_block,
    html,
    flags=re.S
)

# ========= 最近日报 =========

recent = '<!-- AUTO_RECENT_REPORTS_START -->\n<div id="recent-reports">\n'

for report in reports[:10]:
    recent += f'<a href="briefs/{report.name}">{report.stem}</a>\n'

recent += "</div>\n<!-- AUTO_RECENT_REPORTS_END -->"

html = re.sub(
    r'<!-- AUTO_RECENT_REPORTS_START -->.*?<!-- AUTO_RECENT_REPORTS_END -->',
    recent,
    html,
    flags=re.S
)

INDEX.write_text(html, encoding="utf-8")

print(f"Homepage updated: {latest.stem}")
