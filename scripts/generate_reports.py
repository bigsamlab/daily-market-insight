from pathlib import Path
import json
briefs=sorted(Path("briefs").glob("*.html"), reverse=True)
data=[{"date":p.stem,"url":f"briefs/{p.name}"} for p in briefs]
Path("data").mkdir(exist_ok=True)
Path("data/reports.json").write_text(json.dumps(data,indent=2),encoding="utf-8")
print("Generated",len(data),"reports")
