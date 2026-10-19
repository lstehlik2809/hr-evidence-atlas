# Codebook

How the result, lever and checking-depth codes in `studies.json` were assigned. **Status: first draft.** An AI assistant (Claude) assigned every `direction_code` and `lever` code on 19 October 2026, working only from each study's recorded finding (`finding`) and reported direction (`direction`). Both were extracted mostly from abstracts. No person has reviewed the codes yet; review the per-study table below, especially the rows with a coding note. The codes summarize what the authors report; they do not judge whether the result is credible. That judgment belongs to `identification_risk`, design and checking depth.

## Result direction (`direction_code`)

Code the direction of the study's **main business outcome**: the outcome that puts the study in its outcome group (for business-output studies: productivity, sales, quality, innovation, safety or time use).

| Code | Rule |
|---|---|
| `improved` | At least one tested version of the practice improved the main outcome, and no version, subgroup or setting worsened it. Null results for other arms do not change the code. |
| `mixed` | Gains and losses are both reported: across versions, subgroups or settings, or between two business outcomes (for example quantity up, quality down). |
| `worsened` | At least one tested version worsened the main outcome, and none improved it. |
| `no_effect` | No tested version changed the main outcome detectably. This is not evidence that the effect is zero. |
| `unclear` | The checked source does not report a direction for the main outcome. |

Effects on non-business outcomes (stress, well-being, redistribution between workers, political goals) do not change the code. They remain in the finding text.

Known limits: a single AI coder with no human review yet, no blinding, and abstract-level sources for most studies. Counts of codes are vote counts: they ignore effect size, precision and study quality, and published studies over-represent positive results. Do not read the share of `improved` codes as the probability that an HR practice works.

## Who decides (`lever`)

| Code | Meaning |
|---|---|
| `employer` | A practice an employer can choose to adopt. Includes practices tested by researchers inside an organization. |
| `mandate` | A law, regulation or government policy changed the practice (for example board-level worker representation, mandatory profit-sharing, pay-gap reporting, public training subsidies). Firms did not choose it. |
| `technology` | Adoption or design of AI or other workplace technology. |
| `attribute` | Firms or workers are compared by a manager characteristic (gender, promotion speed), not by a deliberate practice. |

## Checking depth (`depth_level`)

`methods` if `depth` records a check of anything beyond the abstract and publisher record: methods, design, randomization, identification, instruments, models, sample, analysis, limitations or an author manuscript. Otherwise `abstract`. The rule is applied mechanically to the `depth` text by a regular expression, and the original `depth` text is kept.

## Pre-registration (`prereg`)

`stated` if the recorded design says the study was preregistered; otherwise `not_checked`. No trial registry was searched, so `not_checked` does not mean "not registered".

## Other changes made with this coding

- S026 (*The Paradox of Inventors' Job Security*) moved from "Voice, inclusion & support" to "Staffing & careers": the treatment is employment protection against dismissal.

## Per-study codes

Read the source sentence (finding) in the page's study note or in `studies.json`.

| ID | Title | As reported | Result | Lever | Depth | Coding note |
|---|---|---|---|---|---|---|
| S001 | Voice at Work | Positive productivity; null voluntary exits | **Improved** | Law/policy | abstract | — |
| S002 | The Impact of Staff and Manager Training on Firm Productivity: Differential and Interaction Effects | Positive under model assumptions | **Improved** | Employer | methods | — |
| S003 | Pay and Train to Sustain: A Dynamic Human Capital Resources View of the Relationship Between HRM Practices and Organizational Performance Over Time | Positive; initial-stock dependent | **Improved** | Employer | methods | Coded improved: growth was larger where initial human-capital stocks were low, but no subgroup reported a decline. |
| S004 | Incentivizing Team Leaders: A Firm‐Level Experiment on Subjective Performance Evaluation of Leadership Skills | Positive | **Improved** | Employer | abstract | — |
| S005 | Effort Redirection Across Multiple Career Tracks: Salary-Cut Policy and State-Owned Enterprises in China | Efficiency-job creation trade-off | **Worsened** | Law/policy | abstract | Coded worsened: operational efficiency, the business-performance outcome, fell. The rise in politically rewarded job creation is not a business-performance gain. |
| S006 | Inventor Rewards, Specialization, and Innovation Performance | Mixed quantity-quality trade-off | **Mixed or depends** | Law/policy | abstract | — |
| S007 | Designing Teams for the Future: How a “Permeable Organizational Design” Intervention Enables Environmental Prognostication to Promote Turning Points in Team Trajectories | Positive | **Improved** | Employer | abstract | — |
| S008 | Human-Centered Artificial Intelligence: A Field Experiment | Positive tailored; negative untailored | **Mixed or depends** | Technology | abstract | — |
| S009 | No Gifts Returned: Surprise Bonuses Reduce Productivity in a Natural Field Experiment | Negative | **Worsened** | Employer | abstract | — |
| S010 | Performance Ranks, Conformity, and Cooperation: Evidence from a Sweater Factory | Negative public; null private | **Worsened** | Employer | abstract | Coded worsened: public ranks lowered productivity; private ranks had no average effect. No arm improved output. |
| S011 | Promotion Decisions and the Adoption of Explicit Potential Assessment | Negative | **Worsened** | Employer | methods | — |
| S012 | Should Human Capital Development Programs be Mandatory or Voluntary? Evidence from a Field Experiment on Mentorship | Positive mandatory; null voluntary | **Improved** | Employer | methods | Coded improved: the mandatory arm raised productivity; the voluntary arm showed no detected improvement. No arm worsened it. |
| S013 | The Performance Effects of Giving Front-Line Employees Direct Access to Performance Data and Thereby Limiting the Supervisor’s Feedback-Intermediation Role: Evidence from a Field Experiment | Improved time allocation; output gain unclear | **Improved** | Employer | methods | Coded improved on the measured outcome (less nonproductive time). The paper does not show that revenue rose. |
| S014 | The Selection Effects of Part-Time Work: Experimental Evidence from a Large-Scale Recruitment Drive | Negative selection on measured productivity | **Worsened** | Employer | abstract | — |
| S015 | The impact of on-the-job training subsidies on firm-level outcomes: evidence from Flemish SMEs | Positive; concentrated in smaller firms | **Improved** | Law/policy | methods | — |
| S016 | Pay transparency and productivity | Mixed; no average decline | **Mixed or depends** | Law/policy | methods | Coded mixed: no average decline, but overpaid employees raised effort while underpaid employees weakly reduced it. |
| S017 | Gender Pay Disclosure and Firm Performance: Quasi‐Experimental Evidence From the United Kingdom | Positive reported | **Improved** | Law/policy | methods | — |
| S018 | Promoting Women to Managerial Roles in the Bangladeshi Garment Sector | Initial performance cost; longer-run integration | **Worsened** | Employer | methods | Coded worsened: female supervisors initially performed worse amid bias; retained supervisors later performed similarly. No performance gain was reported. |
| S019 | Timing Matters: How Pay‐For‐Performance Payment Timing Motivates Lower‐Performing Employees in Pay‐For‐Performance Systems | Positive; subgroup and time dependent | **Improved** | Employer | abstract | — |
| S020 | Measuring the output reduction due to incentive ratcheting in the field | Less ratcheting increased sales | **Improved** | Employer | methods | — |
| S021 | The Productivity Effect of High Involvement Management: Causal Evidence From Germany | Positive; no detected synergy | **Improved** | Employer | methods | — |
| S022 | Collaboration, Workplace Practice Adoption, and Performance: Evidence from a Field Experiment | Positive safety | **Improved** | Employer | methods | — |
| S023 | The Trade-Offs of Letting Local Managers Make Hiring Decisions | Positive on average; heterogeneous | **Mixed or depends** | Employer | abstract | Coded mixed: mean productivity and sales rose, but some stores lost. |
| S024 | Roadmap or Compass? The Value of Prior Collaborative Experience in an Unfamiliar Task Environment | Context-dependent | **Mixed or depends** | Employer | abstract | — |
| S025 | Supervisory Support Shift: The Impact of Disability Inclusion on Coworker Productivity | Negative coworker spillover in setting | **Worsened** | Employer | abstract | — |
| S026 | The Paradox of Inventors’ Job Security | Mixed novelty-value trade-off | **Mixed or depends** | Law/policy | abstract | — |
| S027 | Making the Invisible Hand Visible: Managers and the Allocation of Workers to Jobs | Positive | **Improved** | Manager characteristic | methods | — |
| S028 | The Effects of Mandatory Profit-Sharing on Workers and Firms: Evidence from France | Null productivity; redistribution | **No detectable effect** | Law/policy | abstract | Coded no effect: productivity and investment effects were small to nonexistent; the main effect was redistribution. |
| S029 | The Power of Proximity to Coworkers | Learning gains; experienced-worker output trade-off | **Mixed or depends** | Employer | abstract | — |
| S030 | The female manager effect: evidence on firm strategy and performance from a Matching Difference-in-Differences design | Positive sales/productivity; null profits | **Improved** | Manager characteristic | abstract | Coded improved: productivity and sales rose; profit margins showed no significant change. |
| S031 | Social comparison and the value of performance trajectory information: A field experiment in the workplace | Positive; conditional | **Improved** | Employer | abstract | — |
| S032 | Sotto Voce: The Impacts of Technology to Enhance Worker Voice | Positive retention/attendance | **Improved** | Employer | methods | — |
| S033 | Reducing Job Demands Through a Participatory Work Redesign Intervention: A Quasi‐Experimental Study in Aged Care | Improved demands; uncertain employment effects | **Unclear** | Employer | abstract | Coded unclear: job demands fell, but the employment outcomes (turnover, leave) were described as unclear. |
| S034 | Cut to the Curve: Underrecognition and Talent Loss from Forced Ranking in a Multinational Firm | Negative retention | **Worsened** | Employer | methods | — |
| S035 | Flexible Pay and Labor Supply: Evidence from Uber’s Instant Pay | Higher labor supply | **Improved** | Employer | abstract | — |
| S036 | Vaccines at Work: Experimental Evidence from a Firm Campaign | Null absence benefit | **No detectable effect** | Employer | abstract | — |
| S037 | Conscientiousness in the Workplace: Evidence from a Field Experiment in West Africa | Positive employment outcomes | **Improved** | Employer | abstract | — |
| S038 | Filtering the labor pool: How digitalization redistributes hiring costs | Stage-dependent hiring trade-off | **Mixed or depends** | Technology | abstract | — |
| S039 | Clause and Effect: Theory and Field Experimental Evidence on Noncompete Clauses | More mobility/earnings; null leakage | **Mixed or depends** | Employer | abstract | Coded mixed: removing noncompetes increased worker mobility (a retention cost to the firm) with no detected leakage of secrets. |
| S040 | Return to Office and the Tenure Distribution | Loss of seniority/tenure | **Worsened** | Employer | abstract | — |
| S041 | Bridging the social class capital gap: A psychological intervention in the newcomer adjustment context. | Positive subgroup performance; null intention effect | **Improved** | Employer | abstract | — |
| S042 | Off to a hard start: How job rotation reshapes newcomers’ learning and adjustment process. | Learning-social integration trade-off | **Mixed or depends** | Employer | abstract | — |
| S043 | The relative effects of design thinking versus after-action review on team performance: An experiential/episodic team learning perspective. | Positive versus active comparator | **Improved** | Employer | abstract | — |
| S044 | The Relationship Between Organizational Authenticity Perceptions and Employees’ Work Performance: Evidence From a Field Experiment | Positive | **Improved** | Employer | abstract | — |
| S045 | Cognitive reappraisal emotion regulation interventions in the workplace and their impact on job performance: An ecological momentary intervention approach | Positive self-reported performance | **Improved** | Employer | abstract | — |
| S046 | Customer‐Oriented Boundary Spanning, Functional Diversity, and Customer Adoption | Positive; moderated | **Improved** | Employer | abstract | — |
| S047 | Harnessing the Potential of Workday Design: The Sequencing of Task Difficulty and Its Implications for Workday Well‐Being and Performance | Positive; moderated | **Improved** | Employer | abstract | — |
| S048 | The effects of food insecurity on work outcomes. | Positive work outcomes | **Improved** | Employer | abstract | — |
| S049 | Stimulating gender-diverse teams’ creativity through team diversity training: A field experiment | Partial/conditional; active-arm contrast null | **No detectable effect** | Employer | abstract | Coded no effect: the active-training contrast was not significant; only a conditional indirect pathway was supported. |
| S050 | Employee health and performance promotion through the off‐job crafting intervention: A randomized crossover trial | Null performance; better recovery | **No detectable effect** | Employer | abstract | — |
| S051 | Mission Motivation and Public Sector Performance: Experimental Evidence from Pakistan | Positive public-service output | **Improved** | Employer | abstract | — |
| S052 | Long-Term and Lasting Impacts of Personal Initiative Training on Entrepreneurial Success | Long-term positive effects reported | **Improved** | Employer | abstract | — |
| S053 | Promotions and Productivity: The Role of Meritocracy and Pay Progression in the Public Sector | Treatment-specific; no pooled estimate extracted | **Unclear** | Employer | abstract | Coded unclear: the abstract does not report the direction of the main treatment effects. |
| S054 | Do social comparisons motivate workers? A field experiment on relative earnings, labor supply and the inhibitory effect of pay inequality | Positive under equal piece rates; null with inequality | **Improved** | Employer | abstract | — |
| S055 | How and for whom using generative AI affects creativity: A field experiment. | Positive; moderated | **Improved** | Technology | abstract | — |
| S056 | The Allocation of Incentives in Multilayered Organizations: Evidence from a Community Health Program in Sierra Leone | Allocation-dependent | **Unclear** | Employer | abstract | Coded unclear: results depend on where incentives are placed; no single direction is reported. |
| S057 | The value of leadership: Evidence from a large-scale field experiment | Positive task performance | **Improved** | Employer | abstract | — |
| S058 | The Power of Disagreement: A Field Experiment to Investigate Human–Algorithm Collaboration in Loan Evaluations | Positive; design dependent | **Improved** | Technology | abstract | — |
| S059 | Does a Theory-of-Value Add Value? Evidence from a Randomized Control Trial with Tanzanian Entrepreneurs | Positive active-arm contrast | **Improved** | Employer | abstract | — |
| S060 | Generative AI at Work | Positive; heterogeneous | **Improved** | Technology | abstract | — |
| S061 | For good and for bad: The distinctive effects of successors’ leadership behavior on collective engagement and organizational performance. | Context-dependent; vision communication null | **Mixed or depends** | Employer | abstract | — |
| S062 | Incentive and Signaling Effects of Bonus Payments: An Experiment in a Company | Mechanism evidence | **Unclear** | Employer | abstract | Coded unclear: mechanism evidence from a stylized game; no business-output effect. |
| S063 | Training, Communications Patterns, and Spillovers inside Organizations | Positive; model-based spillovers | **Improved** | Employer | abstract | — |
| S064 | Leveraging Social Comparisons: The Role of Peer Assignment Policies for Productivity and Stress | Positive output; stress trade-off | **Improved** | Employer | abstract | Coded improved: self-chosen and targeted peers both motivated performance; the trade-off concerns stress, not output. |
| S065 | Peer Evaluation and Team Performance: An Experiment on Complex Problem Solving | Null performance | **No detectable effect** | Employer | abstract | — |
| S066 | The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers | Positive pooled; noisy individual trials | **Improved** | Technology | abstract | — |
| S067 | Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality | Task-dependent | **Mixed or depends** | Technology | abstract | — |
| S068 | The Cybernetic Teammate: A Field Experiment on Generative AI and Teamwork | Positive on professional tasks | **Improved** | Technology | abstract | — |
| S069 | How Do You Identify a Good Manager? | Manager-selection dependent | **Worsened** | Employer | methods | Coded worsened for the practice of letting managers self-select: they performed worse than randomly selected managers. |
