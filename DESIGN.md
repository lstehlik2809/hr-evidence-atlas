# Design contract

## Audience and reading task

Researchers, people analysts and practitioners asking which HR practices have credible causal evidence on business outcomes. Analytical exploration at reading pace, not operational monitoring.

Journey: orient to scope → distinguish outcome types → inspect contrasting treatments/results → question identification → find a relevant paper → inspect finding, setting and limitations → open original paper/abstract.

The default index shows workplace output because that most directly answers the original business-performance question. Employment, rated/proximal and adjacent evidence require an explicit scope change. No pooled effect size, success rate, evidence quality score, causal mediation claim or ROI estimate is inferred.

## Metric contract

- **Retained papers:** unique DOI records with `status === "Included"`; 68 in this snapshot. Denominator for composition. One unresolved-date record excluded.
- **Outcome counts:** retained records by normalized scope; 31 workplace output, 9 employment, 10 proximal, 18 adjacent. Metadata scopes describe measurement, not sign or strength.
- **Matching papers:** retained records matching every active scope, practice, design and search term. CSV uses exactly the same selection, regardless of the first 10/20 displayed rows.
- **Year/order:** verified first-online date when available; otherwise available online/issue year. Ordering within incomplete-date years is provisional. The date basis is available in each study note.
- **Reported effect:** source-extracted point estimate, with original outcome, estimand and qualifications. Missing values are not zeros; no cross-paper magnitude scale is displayed.
- **Review coverage:** 49 selected journals, 9,600 metadata records retrieved, 107 unique candidates individually assessed. Retrieval and human assessment are distinct.

## Panel and interaction plan

1. Editorial opening: review scope and outcome composition, with exact counts and denominator caveat.
2. Scroll narrative: sticky context panel tied to five readable notes; numbered controls offer a direct route; reduced motion disables smooth scrolling.
3. Index: text search and native selects share one state. Count, rows and CSV remain synchronized. Reset restores workplace output, all practices/designs and newest first.
4. Study note: actual finding, measured outcome, setting/sample, identification, reported estimate, risks, source-check depth and timing. Source link is available from both row and detail.
5. Methods: journal coverage, screening log and uncertainty, without expanding the main index into a metadata dump.

Shareable URLs retain filter parameters and selected study. Load-more preserves the full match count; keyboard focus moves to the first newly revealed title. The modal restores focus on close. An empty state distinguishes absence from this filtered inventory from absence of evidence in the literature. Static data have no asynchronous response races. A data-load error has an explicit message and download route.

## Visual roles

Warm white background, dark green ink, muted grey-green context; terracotta for qualifications. Georgia for editorial headings; Arial for reading/UI; Courier only for short metadata labels. Strong title hierarchy, thin rules, generous but purposeful space. Colors never substitute for outcome or direction labels. Percentage estimates are not plotted on a shared scale.

Desktop uses a side-by-side sticky panel and narrative. Narrow screens use a compact sticky panel above the notes; the study index reflows to a single reading column. No external font dependency.

## Acceptance tasks

- Identify window, scope and completeness caveat from the opening.
- Scroll or use numbered controls to reach mentoring, ranking and IV caveats.
- Find the mentoring paper; identify mandatory-versus-voluntary contrast and single-firm limit; open its DOI.
- Find observational HR-bundle papers and inspect their identifying assumptions.
- Filter to all retained papers and verify 68; default workplace output gives 31; employment gives 9.
- Search for an absent term; use reset; export only the selected records with limitations.
- Open/close a detail with keyboard; follow a study URL; inspect narrow reflow and enlarged text if browser tooling permits.

## Ten recurring failure-mode checks

1. Journey: five notes lead to paper-level investigation.
2. Hierarchy: editorial title and findings dominate; caveats use restrained emphasis.
3. Hero plot: outcome composition answers scope; no decorative large chart.
4. Data dump: curated findings/limitations in rows; full metadata in detail/download.
5. Labels: actual outcome, treatment, sample and estimator remain explicit.
6. Buried estimates: estimates stay with their units; heterogeneous quantities are not visually ranked.
7. Duplication: introductory stories illustrate selected papers; the index is the canonical complete inventory.
8. Color: stable semantic roles; meaning remains in words.
9. Typography: local fonts, readable hierarchy, no external asset dependency.
10. Spacing/scales: shared tokens and consistent rows; no shared effect-size scale.

Verification status is recorded separately in `VERIFICATION.md`; these design intentions are not claims that every browser check passed.
