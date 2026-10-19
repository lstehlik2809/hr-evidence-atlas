# HR Causal Evidence Map, 2025–26

A single edition, not a living review. (The repository and its URL keep the earlier name, HR Evidence Atlas, so existing links keep working.)

What causal studies published from **1 January 2025 to 18 October 2026** found about HR practices and business performance: 68 experiments, quasi-experiments and observational studies with adjustment, each with its finding, main limitation and a link to the paper.

Published page: https://lstehlik2809.github.io/hr-evidence-atlas/

## What the page does

1. **Answers first.** The opening shows how many of the 31 business-output studies improved, worsened or had mixed results.
2. **Walks through the evidence.** Seven scroll steps share one evidence map (practice × outcome measured). Each step changes what the map highlights: where evidence is dense or thin, result direction, backfires, implementation dependence, design strength, and whether an employer can choose the practice.
3. **Lets readers check every study.** A filterable list (outcome, practice, result, design, who decides) with the finding, main limitation, design, checking depth and paper link. Each study note gives the coding rationale, sample, estimate and date basis. Filters and study notes have shareable URLs; the current selection downloads as CSV.

`index.html` is self-contained: HTML, CSS, JavaScript and data in one file, with no build step for readers, no external fonts and no analytics.

## Scope and limits

- 68 retained studies: 31 business output, 9 turnover/absence/hiring, 10 rated or self-reported performance, 18 related settings (AI tools, public sector, lab tasks). One further candidate with an unconfirmed publication date is excluded from counts.
- A broad scoping inventory from 49 selected journals, screened by a single reviewer; **not a systematic review**.
- Result codes are **vote counts drafted by an AI assistant and not yet reviewed by a person**. See [CODEBOOK.md](CODEBOOK.md). No pooled effect, quality score or HR ROI is estimated.
- 52 of 68 studies were checked at abstract level only; 16 against methods sections.

## Maintenance

- Edit `studies.json`, then run `python3 tools/build.py`. It validates the data and the codebook, and embeds the data into `index.html`. `python3 tools/build.py --check` (run by the *Validate data* workflow on every push) fails if the embedded copy is stale.
- New codes need a matching row in `CODEBOOK.md`.
- Keep study IDs stable: study links use them.
- Headline numbers on the page are computed from the data. The walkthrough's worked examples (steps 4–5) name specific studies and need a manual check if those studies' codes change.

## Checking the data against Crossref

The *Evidence check* workflow (`.github/workflows/evidence-check.yml`) runs only when started by hand from the Actions tab, since this is a single edition. It runs `tools/crossref_check.py`, which:

- checks every listed DOI against Crossref for title and date;
- lists articles in the 49 journals, not yet in the inventory or screening log, whose titles suggest an HR practice and a causal design. This catches studies missed inside the window, plus anything published since, which a single edition does not add.

It opens or comments on one issue for manual review and never edits the data. Optionally set a repository variable `CROSSREF_MAILTO` to use Crossref's polite pool.

`DESIGN.md` describes the information-design contract. `VERIFICATION.md` records what was checked and what was not.
