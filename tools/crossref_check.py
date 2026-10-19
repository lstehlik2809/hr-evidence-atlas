"""Monthly evidence check against Crossref.

1. Verifies that every listed DOI resolves to the recorded title and an
   online date inside the review window.
2. Lists new articles in the journal roster published since the review
   window opened, not already in the inventory or screening log, whose
   titles suggest an HR practice tested with a causal design.

Nothing is added to the data automatically: the report is for manual review.

Usage: python3 tools/crossref_check.py [--out report.md] [--skip-verify] [--skip-discover]
Exit code 0 always; the report's first line says whether anything needs attention.
Set CROSSREF_MAILTO to identify the caller to Crossref's polite pool.
"""
import argparse
import difflib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://api.crossref.org"

HR_TERMS = re.compile(
    r"\b(employee|worker|workforce|workplace|human resource|\bhr\b|personnel|staff|pay|compensation|incentive|bonus|"
    r"wage|salary|training|mentor|onboarding|newcomer|hiring|recruit|selection|promotion|appraisal|feedback|"
    r"manager|managerial|supervisor|leadership|team|turnover|retention|quit|absence|absenteeism|remote work|"
    r"work from home|hybrid work|job design|work design|flexib|diversity|inclusion|well-being|wellbeing|"
    r"burnout|career|talent|performance management|ranking|recognition|noncompete|profit-sharing)", re.I)
CAUSAL_TERMS = re.compile(
    r"(experiment|randomi[sz]ed|\brct\b|quasi|natural experiment|difference-in-difference|"
    r"regression discontinuity|instrumental variable|causal|evidence from|field study|intervention|"
    r"staggered|event study|synthetic control)", re.I)


def get(path, params=None, retries=4):
    url = API + path + ("?" + urllib.parse.urlencode(params, safe=":,") if params else "")
    mailto = os.environ.get("CROSSREF_MAILTO")
    agent = "hr-evidence-atlas-check/1.0" + (f" (mailto:{mailto})" if mailto else "")
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": agent}), timeout=60) as r:
                return json.load(r)["message"]
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if attempt == retries - 1:
                raise
        except (urllib.error.URLError, TimeoutError):
            if attempt == retries - 1:
                raise
        time.sleep(2 ** (attempt + 1))


def norm(title):
    return re.sub(r"[^a-z0-9 ]", "", re.sub(r"<[^>]+>", "", title or "").lower()).strip()


def date_of(item, key):
    parts = (item.get(key) or {}).get("date-parts") or [[]]
    parts = [p for p in parts[0] if p is not None]
    return "-".join(f"{p:02d}" if i else str(p) for i, p in enumerate(parts)) or ""


def verify(data):
    problems = []
    for s in data["studies"]:
        try:
            item = get("/works/" + urllib.parse.quote(s["doi"]))
        except Exception as e:  # network failure is reported, not fatal
            problems.append(f"| {s['id']} | {s['doi']} | Request failed: {e} |")
            continue
        time.sleep(0.2)
        if item is None:
            problems.append(f"| {s['id']} | {s['doi']} | DOI not found in Crossref |")
            continue
        title = (item.get("title") or [""])[0]
        ratio = difflib.SequenceMatcher(None, norm(title), norm(s["title"])).ratio()
        if ratio < 0.85:
            problems.append(f"| {s['id']} | {s['doi']} | Title differs (similarity {ratio:.2f}): Crossref has “{title}” |")
        online = date_of(item, "published-online") or date_of(item, "issued")
        start = data["meta"]["from"]
        before = int(online) < int(start[:4]) if len(online) == 4 else online < start[:len(online)]
        if online and before and s["status"] == "Included":
            problems.append(f"| {s['id']} | {s['doi']} | Crossref online date {online} is before the window start {data['meta']['from']} |")
        if s.get("first_online") and online and len(online) >= 10 and online[:10] != s["first_online"][:10]:
            problems.append(f"| {s['id']} | {s['doi']} | Recorded first online {s['first_online']}, Crossref has {online} |")
    return problems


def discover(data):
    known = {s["doi"].lower() for s in data["studies"]} | {s["doi"].lower() for s in data["screening"]}
    since = data["meta"]["from"]
    candidates, hr_only, scanned, failures = [], [], 0, []
    for j in data["journals"]:
        cursor = "*"
        while cursor:
            try:
                msg = get(f"/journals/{j['issn']}/works", {
                    "filter": f"from-pub-date:{since},type:journal-article",
                    "select": "DOI,title,published-online,issued",
                    "rows": 1000, "cursor": cursor})
            except Exception as e:
                failures.append(f"{j['journal']}: {e}")
                break
            items = (msg or {}).get("items", [])
            scanned += len(items)
            for it in items:
                doi = it.get("DOI", "").lower()
                title = (it.get("title") or [""])[0]
                if doi in known or not HR_TERMS.search(title):
                    continue
                known.add(doi)
                row = (j["journal"], date_of(it, "published-online") or date_of(it, "issued"), title, doi)
                (candidates if CAUSAL_TERMS.search(title) else hr_only).append(row)
            cursor = msg.get("next-cursor") if items else None
            time.sleep(0.2)
    return candidates, hr_only, scanned, failures


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="evidence-check.md")
    ap.add_argument("--skip-verify", action="store_true")
    ap.add_argument("--skip-discover", action="store_true")
    args = ap.parse_args()
    data = json.loads((ROOT / "studies.json").read_text(encoding="utf-8"))

    problems = [] if args.skip_verify else verify(data)
    candidates, hr_only, scanned, failures = ([], [], 0, []) if args.skip_discover else discover(data)
    candidates.sort(key=lambda c: c[1], reverse=True)
    hr_only.sort(key=lambda c: c[1], reverse=True)

    attention = bool(problems or candidates or failures)
    lines = [f"Needs attention: {'yes' if attention else 'no'}", "",
             f"Inventory checked through {data['meta']['as_of']}; window opens {data['meta']['from']}.", ""]
    if not args.skip_verify:
        lines += ["## Listed studies checked against Crossref", ""]
        lines += (["| ID | DOI | Issue |", "|---|---|---|", *problems] if problems
                  else [f"All {len(data['studies'])} DOIs resolve with matching titles and in-window dates."])
        lines.append("")
    if not args.skip_discover:
        lines += ["## New candidates to screen", "",
                  f"Scanned {scanned:,} articles published since {data['meta']['from']} in {len(data['journals'])} journals "
                  "and not yet in the inventory or screening log. The table lists titles with both an HR term and a "
                  "causal-design term; each needs a manual check of design, outcome and first-online date.", ""]
        if candidates:
            lines += ["| First online | Journal | Title | DOI |", "|---|---|---|---|"]
            lines += [f"| {d} | {j} | {t.replace('|', '/')} | https://doi.org/{doi} |" for j, d, t, doi in candidates]
        else:
            lines.append("No new candidates.")
        if hr_only:
            lines += ["", f"<details><summary>{len(hr_only)} more HR titles without a design term in the title "
                      "(designs are often named only in the abstract)</summary>", "",
                      *[f"- {d} · {j} · {t} · https://doi.org/{doi}" for j, d, t, doi in hr_only[:400]],
                      *(["- …list truncated at 400"] if len(hr_only) > 400 else []), "", "</details>"]
        if failures:
            lines += ["", "Journals that could not be fetched:", *[f"- {f}" for f in failures]]
    Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(lines[0])


if __name__ == "__main__":
    sys.exit(main())
