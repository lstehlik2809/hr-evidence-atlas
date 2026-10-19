"""Validate studies.json and embed it into index.html.

Usage: python3 tools/build.py [--check]

--check only validates and confirms the embedded copy matches; it writes nothing.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "studies.json"
PAGE = ROOT / "index.html"
EMBED = re.compile(r"^window\.HR_EVIDENCE = .*;$", re.M)

ALLOWED = {
    "direction_code": {"improved", "mixed", "worsened", "no_effect", "unclear"},
    "lever": {"employer", "mandate", "technology", "attribute"},
    "depth_level": {"abstract", "methods"},
    "prereg": {"stated", "not_checked"},
    "scope": {"Workplace output", "Employment outcome", "Rated/proximal performance", "Adjacent evidence"},
    "design_group": {"Randomized experiment", "Quasi-experiment", "Observational identification",
                     "Other experiment / allocation unverified"},
}
RESULT_LABELS = {"improved": "Improved", "mixed": "Mixed or depends", "worsened": "Worsened",
                 "no_effect": "No detectable effect", "unclear": "Unclear"}
REQUIRED = ["id", "doi", "title", "authors", "journal", "finding", "identification_risk", "paper_url",
            "practice_group", "status", "year", *ALLOWED]


def validate(data):
    errors = []
    ids = [s["id"] for s in data["studies"]]
    if len(ids) != len(set(ids)):
        errors.append("duplicate study ids")
    dois = [s["doi"].lower() for s in data["studies"]]
    if len(dois) != len(set(dois)):
        errors.append("duplicate DOIs")
    for s in data["studies"]:
        for field in REQUIRED:
            if s.get(field) in (None, ""):
                errors.append(f"{s.get('id')}: missing {field}")
        for field, allowed in ALLOWED.items():
            if s.get(field) not in allowed:
                errors.append(f"{s['id']}: {field}={s.get(field)!r} not in {sorted(allowed)}")
        if not s.get("paper_url", "").startswith("https://"):
            errors.append(f"{s['id']}: paper_url is not https")
    retained = [s for s in data["studies"] if s["status"] == "Included"]
    meta = data["meta"]
    if meta["retained"] != len(retained):
        errors.append(f"meta.retained={meta['retained']} but {len(retained)} studies are Included")
    if meta["unresolved"] != len(data["studies"]) - len(retained):
        errors.append("meta.unresolved does not match non-Included studies")
    if meta["journals"] != len(data["journals"]):
        errors.append("meta.journals does not match journal roster")
    codebook = {line.split("|")[1].strip(): line for line in (ROOT / "CODEBOOK.md").read_text(encoding="utf-8").splitlines()
                if line.startswith("| S")}
    for s in data["studies"]:
        label = RESULT_LABELS.get(s.get("direction_code"))
        if label and f"**{label}**" not in codebook.get(s["id"], ""):
            errors.append(f"{s['id']}: CODEBOOK.md row missing or result differs from {label}")
    return errors, retained


def main():
    check_only = "--check" in sys.argv
    data = json.loads(DATA.read_text(encoding="utf-8"))
    errors, retained = validate(data)
    if errors:
        print("Validation failed:\n  " + "\n  ".join(errors))
        sys.exit(1)

    canonical = json.dumps(data, indent=2, ensure_ascii=False)
    # "</" would end the inline <script> early.
    embedded = "window.HR_EVIDENCE = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + ";"
    page = PAGE.read_text(encoding="utf-8")
    if len(EMBED.findall(page)) != 1:
        print("index.html must contain exactly one 'window.HR_EVIDENCE = ...;' line")
        sys.exit(1)

    if check_only:
        current = json.loads(EMBED.search(page).group(0)[len("window.HR_EVIDENCE = "):-1].replace("<\\/", "</"))
        if current != data:
            print("index.html embedded data differs from studies.json; run tools/build.py")
            sys.exit(1)
    else:
        DATA.write_text(canonical, encoding="utf-8")
        PAGE.write_text(EMBED.sub(lambda _: embedded, page), encoding="utf-8")

    scopes = Counter(s["scope"] for s in retained)
    directions = Counter(s["direction_code"] for s in retained if s["scope"] == "Workplace output")
    print(f"OK: {len(retained)} retained; scopes {dict(scopes)}; workplace-output directions {dict(directions)}")


if __name__ == "__main__":
    main()
