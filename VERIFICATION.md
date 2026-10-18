# Verification status

## Passed

- JavaScript syntax checks for the application, data and shared selection logic.
- 68 retained unique papers; one unresolved-date paper is excluded from retained counts.
- Outcome counts reproduced: 31 workplace output, 9 employment, 10 rated/proximal, 18 adjacent.
- Original-source link, finding, measurement, setting, verification depth and limitations present for every study.
- Public JSON and embedded data are identical.
- Shared selection logic checked against exact expected mentoring and HR-systems paper sets, intersecting filters, all four scope counts, case-insensitive multiword search, empty results and newest/alphabetical ordering.
- Reported effect ranges, hazard interpretation, subgroup qualifications and customer-versus-profit distinction retained.
- Local linked files exist; HTML IDs are unique; referenced static DOM targets exist.
- Key text/surface contrast pairs checked numerically; a muted-text contrast failure on the qualification surface was corrected.
- Source archive integrity and required GitHub Pages files checked during packaging.

## Live desktop browser checks passed

The public GitHub Pages deployment was opened and visually inspected at a 1,363 CSS-pixel desktop viewport on 18 October 2026. The initial page, scrollytelling mentoring scene and study-detail dialog were inspected as rendered screenshots.

- GitHub's initial Pages deployment completed successfully for commit `bb968f53150fb50660350977a12a14d265de8841`.
- Scrolling from the mentoring note to the ranking note changed the sticky evidence panel correctly. Numbered note navigation also reached the intended scene after its smooth-scroll transition.
- The ranking detail showed the correct title, limitation and DOI link.
- Escape closed the dialog and returned focus to its opening button.
- Outcome scopes displayed the expected 68 total and 9 employment records; the default showed 31 workplace-output records.
- HR systems plus observational identification returned exactly the Pay and Train and High Involvement Management papers.
- No-results, pointer/keyboard reset and mentoring search were exercised.
- Load-more revealed 20 rows while retaining the full 31-paper matching count.
- A mentoring study deep link opened the correct dialog and preserved the one-paper selection in a fresh tab.
- Citation copying returned the success message; a filtered one-paper CSV download completed in the browser. Downloaded-file byte inspection was unavailable through the synchronized filesystem, so export contents were checked through shared source/selection logic rather than reading the downloaded file.
- The displayed paper/abstract link targeted the expected DOI. Every external source was not individually opened during browser QA.

## Remaining verification limits

The managed preview supervisor is unavailable in this workspace (`sites-previewd mailbox ... No such file or directory`). The documented status check confirmed the same infrastructure failure. No substitute server or browser runtime was used.

The unavailable local preview was superseded by the live desktop check above. Narrow-screen, enlarged-text and real-phone rendering remain unverified: the available browser controls did not provide a confirmed viewport/zoom change. Reduced-motion behavior was checked in source, not with an emulated browser preference. This is not representative-user validation or a full accessibility audit.

## Publishing

Repository: https://github.com/lstehlik2809/hr-evidence-atlas

Published page: https://lstehlik2809.github.io/hr-evidence-atlas/

GitHub's Pages settings reported the site live, and the public page was opened and verified. The repository's default branch is the publishing source, with HTTPS enforced.
