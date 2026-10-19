# Design contract

## Audience and question

HR leaders, people analysts and researchers who want a quick, honest overview of what recent causal studies say about HR practices and business performance, and who may then check individual papers. Reading pace, not monitoring. Light theme, plain language.

**Primary question:** when HR practices were tested with credible designs since 2025, did business output improve?
**Follow-ups:** for which practices? How solid is the evidence? Could my organization do this? Where is the paper?

Journey: answer (hero) → walkthrough on one evidence map → filtered list → study note → original paper.

## Measures

| Measure | Definition |
|---|---|
| Retained studies | `status === "Included"`; 68. One unconfirmed-date candidate is excluded from all counts. |
| Outcome group | `scope`: business output 31, turnover/absence/hiring 9, rated/self-reported 10, related settings 18. |
| Result | `direction_code` per [CODEBOOK.md](CODEBOOK.md). A count of studies (vote count), not an effect size. Business output: 16 improved, 7 mixed, 7 worsened, 1 no detectable effect. |
| Who decides | `lever`: employer 50, law/policy 8, technology 8, manager characteristic 2. |
| Checking depth | `depth_level`: methods 16, abstract only 52. |
| Design | `design_group`: randomized 26, natural/quasi 20, experiment with randomization not confirmed 19, observational with adjustment 3. Only 6 of 31 business-output studies are randomized. |

All numbers in the hero and walkthrough are computed from the data at load time. No pooled effect, percentage of "HR that works", quality score or ROI is shown, because the studies estimate different quantities in different settings.

## Layout and encoding

- **Hero:** the answer as a unit chart (one mark per business-output study, grouped by result) with the one-sentence summary and the single canonical caveat, linked to "How to read this".
- **Walkthrough:** seven steps; one persistent evidence map (rows = 7 practice groups ordered by count, columns = 4 outcome groups). Each mark is one study and opens its note. Steps change the highlighting only, so readers keep their place. On phones the map sticks to the top (about 45% of an 844px screen) and the text scrolls beneath it.
- **Result encoding:** shape *and* color: ▲ improved (green), ◆ mixed (ochre), ▼ worsened (brick), ○ no detectable effect (grey ring), dashed ring unclear. Legible without color. Other steps use filled vs hollow circles in neutral ink.
- **Text alternative:** "Show the map as a table" gives the same counts with result breakdowns. Each count links to the filtered list. Map marks are not keyboard tab stops; keyboard users reach every study through the table and list.
- **List:** a compact row: result | title, journal, date, setting, finding, main limitation | design, checking depth, lever (if not employer), links. Default: business output, newest first, 10 rows.
- **Caveats:** stated once in "How to read this", plus the main limitation on each study. Not repeated elsewhere.

## Visual system

One system sans-serif for reading and UI; Georgia only for page and section headings, never italic. No monospace, no decorative labels, no gradients. Minimum text 12px; body 16–17px. Color tokens are on `:root`. Direction colors are reserved for results only. Caveats use neutral ink and grey rules, so "limitation" never reads as "worsened". Text contrast ≥ 5:1 on all surfaces; marks and input borders ≥ 3:1.

## Interaction

Filters: search, outcome group (default business output), practice, result, design, who decides. Count, rows and CSV share one selection function. Reset restores the defaults. The URL keeps filters and the open study; invalid parameters fall back to defaults. "Show more" moves focus to the first new row. The dialog returns focus on close. The empty state explains that no match does not mean no research exists.

## Ten failure-mode checks

1. Journey: answer → map walkthrough → list → note → paper.
2. Hierarchy: the hero answer dominates; caveats are restrained.
3. Hero plot: the unit chart is the answer itself, and the map's size serves the walkthrough.
4. Data dump: curated row fields; full metadata in the note and CSV.
5. Labels: plain outcome, practice and result names on screen; no internal codes.
6. Buried estimates: the result is the primary encoding; no effect sizes are ranked across incomparable studies.
7. Duplication: one canonical caveat block.
8. Color: semantic, reserved for result; shape redundancy.
9. Typography: system sans plus one serif for headings.
10. Spacing and scales: shared tokens; the map uses one mark per study throughout.
