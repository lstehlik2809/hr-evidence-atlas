# Verification status

Redesign of 19 October 2026. Checks were run in headless Chromium (Playwright) against the local `index.html` at 1440×900 and 390×844.

## Passed

- `tools/build.py --check`: valid codes for all 69 records; unique IDs and DOIs; meta counts match; embedded data identical to `studies.json`; every study has a matching `CODEBOOK.md` row (a deliberately introduced mismatch was caught).
- Counts recomputed independently in Python and matched in the browser: default 31; all 68; worsened 10; law/policy in business output 8; randomized in business output 6; Pay & performance × business output 12 (via the table link); the mentoring search returns exactly S012.
- The hero sentence uses the same counts as the data (16 / 7 / 7 / 1 of 31).
- The CSV row count equals the on-screen count, and the CSV includes result code, coding note, main limitation, design, depth and paper URL.
- Reset, the empty state, invalid URL parameters, deep links to filters plus a study, "Show more" (10 → 20, focus to row 11), opening the dialog by keyboard, Escape closing it with focus returned and the URL cleaned, and map marks opening the matching study.
- Scroll steps 1–7 drive the map to the matching state at both viewport sizes.
- No JavaScript errors; no horizontal overflow at either size or at 200% text size (1280px wide); no rendered text below 12px.
- Contrast computed: text tokens 5.0–15.5:1 on all surfaces; result marks ≥ 5:1; "unclear" mark and input borders raised to ≥ 3:1.
- `tools/crossref_check.py` was tested against stubbed Crossref responses. It flagged a missing DOI, a changed title and an out-of-window date; it did not flag a year-only date; it skipped known DOIs and non-HR titles; and it de-duplicated candidates.

## Not verified

- **DOIs and dates against Crossref.** Crossref was unreachable from the build environment (network policy). The *Evidence check* workflow performs this check on GitHub's network; run it once by hand (Actions → Evidence check → Run workflow) and review the issue it opens.
- **Result and lever codes** were drafted by an AI assistant from abstract-level findings and have **not been reviewed by a person**. See `CODEBOOK.md`.
- **Pre-registration** was not checked in any registry: 3 studies state it in their design and the rest are "not checked".
- The workflows have not yet run on GitHub.
- Real phones, screen readers and representative users were not tested. Reduced motion was checked in the source only.
