# Editorial direction: research and proposal

Research date: 5 November 2026.

Status: editorial direction with a local implementation draft. The Writing index and article template are implemented, with three unpublished general-analysis essays available only in development. They are not approved voice references or historical publications. Confirmed brand and user preferences are recorded separately in [brand.md](brand.md).

## Recommendation

Use **Writing** in navigation and **Field notes** as the editorial section title. Build a small library of thoughtful pieces about architectural decisions, operational consequences and engineering leadership. Use a readable essay with a decision record's reasoning behind it.

A candidate introduction: "Practical notes on architecture, operations and the decisions that teams live with."

The audience is engineering leaders and senior engineers assessing Adam's judgement, with hiring managers and recruiters able to understand the central point quickly. The purpose is to support architecture contracts and consulting, not to run a high-volume news publication.

## Research scope and limits

Reviewed primary publisher sites, their editorial structure and representative public pieces. Selection spans established authors, commercial engineering publications and modern practitioner-led writing. These are benchmarks, not a verified ranking of market success. Comparable audited traffic, subscriber engagement and consulting conversion figures were not available across all sources.

The Pragmatic Engineer and ByteByteGo each report more than one million readers on their own about pages. Those are publisher-reported reach signals, not verified consulting leads, paid subscriber counts or comparable audited measurements. Reach alone is not the goal for this site.

### Benchmarks

| Publication / author                                                                                                              | Observed approach                                                                                     | Useful adaptation for Adam                                                                   | Boundary                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [LeadDev](https://leaddev.com/)                                                                                                   | Role-focused engineering leadership coverage, practical problems, talks and reports.                  | Start with a situation a hiring engineering leader recognises.                               | A personal site should not mimic a large multi-author news/events operation.                                               |
| [Robert C. Martin / Clean Coder](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)                    | A clear architectural position explained with a recognisable diagram and explicit rules.              | Give each article a central argument and a visual that clarifies it.                         | Use Adam's measured voice, contextual limits and original diagrams. Do not copy rhetoric, claims or the signature diagram. |
| [Martin Fowler](https://martinfowler.com/bliki/StranglerFigApplication.html)                                                      | Named concepts and reference material, with clear explanations of applicability.                      | Write pieces people can return to when facing a decision.                                    | Established patterns need attribution; explaining a pattern alone is not a novel angle.                                    |
| [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/about)                                                          | Reported engineering stories, practitioner input, practical resources and independent analysis.       | Separate firsthand evidence, reporting and interpretation; provide useful takeaways.         | Its access, research capacity, business model and frequency do not transfer to a contractor's site.                        |
| [Will Larson / StaffEng](https://staffeng.com/guides/manage-technical-quality/) and [Irrational Exuberance](https://lethain.com/) | Frameworks and worked reasoning about engineering quality, strategy and leadership.                   | Offer usable decision aids with limitations; be fair to earlier decisions and their context. | Avoid process frameworks that exceed the problem or imply there is one universal model.                                    |
| [Gregor Hohpe / The Architect Elevator](https://architectelevator.com/architecture/famous-architects-sketch/)                     | Sketches and metaphors connect technical reasoning with organisational and business context.          | Explain why a design matters outside the architecture meeting.                               | Keep metaphors subordinate to technical accuracy; original line diagrams should match the site.                            |
| [Charity Majors](https://charity.wtf/p/in-praise-of-normal-engineers)                                                             | Strong practitioner argument about team ownership, delivery and operating software.                   | Show what teams need to sustain a system and how ownership affects architecture.             | Borrow the team focus, not the author's personal experiences or confrontational voice.                                     |
| [Julia Evans](https://jvns.ca/blog/2022/07/09/monitoring-small-web-services/)                                                     | Narrow practical questions, concrete examples and explicit operating constraints.                     | Make a small difficult idea understandable and useful; state the workload's limits.          | Her example concerns small, low-stakes services; it is not a reliability prescription for critical SaaS.                   |
| [Hillel Wayne](https://www.hillelwayne.com/post/hoc/)                                                                             | An explained model tested against concrete examples, with caveats and references.                     | Test the recommendation against counterexamples and show where it breaks down.               | Distinguish a model, an interpretation and demonstrated evidence.                                                          |
| [Simon Willison](https://simonwillison.net/) and [his guides](https://simonwillison.net/guides/)                                  | Separate longer reference material from smaller entries, links and experiments.                       | Keep polished durable articles easy to find; identify experiments as experiments.            | The volume and fast-moving AI news cycle are not this site's model.                                                        |
| [ByteByteGo](https://blog.bytebytego.com/about)                                                                                   | Accessible system-design education; its public API article uses a visual overview and bounded topics. | Let one clear diagram or compact comparison do useful explanatory work.                      | Do not become an interview-preparation site or repeat generic system-design summaries.                                     |

### Specific references worth revisiting

- [LeadDev: performance when part of the stack is outside your control](https://leaddev.com/technical-direction/planning-next-moves-improving-performance-when-half-your-stack-is-someone-elses-problem): a concrete leadership problem as the entry point. This is a conference-talk page, not a directly comparable essay.
- [Fowler: rewriting Strangler Fig](https://martinfowler.com/articles/2024-strangler-fig-rewrite.html): explains the revision of a long-lived reference article. The reported page-view figure is historical to that post, not a current market ranking.
- [StaffEng: manage technical quality](https://staffeng.com/guides/manage-technical-quality/): practical approaches selected for context, including respect for earlier decisions.
- [Hohpe: famous architects sketch](https://architectelevator.com/architecture/famous-architects-sketch/): abstraction and context rather than increasingly elaborate diagrams.
- [Majors: In Praise of Normal Engineers](https://charity.wtf/p/in-praise-of-normal-engineers): team ownership as a unit of sustainable delivery.
- [Evans: monitoring tiny web services](https://jvns.ca/blog/2022/07/09/monitoring-small-web-services/): scope, concrete behaviour and operational compromise made explicit.
- [Wayne: hierarchy of controls](https://www.hillelwayne.com/post/hoc/): an applied model with openly stated limits.
- [Nygard: documenting architecture decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions): compact context, decision and consequences. This informs reasoning structure, not a proposed public ADR register.

## Where this site can stand out

Architecture patterns, cloud savings and engineering ownership already have extensive coverage. This research does not establish that an unserved topic has no competing articles.

The stronger opportunity is a specific combination: established SaaS, .NET/Azure, hybrid modernisation, identity and tenant isolation, cloud economics, service recovery and internationally distributed teams. Focus on what a choice costs to implement and operate, what was deliberately left alone, and what the team needs after the architect leaves.

The distinguishing questions are:

1. What made the apparently obvious solution unsuitable here?
2. What did the choice make easier, and what burden did it add?
3. Who owns the consequences in production?
4. What lets the next team change the system confidently?
5. What evidence would make us choose differently?

These are proposed editorial angles. The CV supports the broad experience areas, not every detailed incident, comparison or retrospective outcome that an article might need.

## Writing voice and repeatability

Use the repository's [writing skill](../skills/adam-riddick-writing/SKILL.md), [working voice profile](../skills/adam-riddick-writing/references/voice.md) and [article workflow](../skills/adam-riddick-writing/references/workflow.md). Adam has asked for agent-generated articles in his prose and wants the profile to grow through edits rather than collecting samples now. The initial profile records confirmed preferences separately from proposed prose choices.

Reference authors influence the editorial reasoning and presentation, not the imitation of their voices. The [article brief](../skills/adam-riddick-writing/assets/article-brief.md) helps connect a piece to its actual evidence.

## Article format

Recommended main length: approximately 1,000–1,600 words, with shorter pieces when the subject warrants them. Readers should be able to understand the central decision in the first minute.

A flexible structure:

1. **The situation** — a concrete problem, the stakes and relevant constraints.
2. **The decision in brief** — a short, visually distinct summary near the top.
3. **The options** — what was considered, with a small comparison where useful.
4. **The trade-off** — the cost, compromise or responsibility accepted.
5. **What followed** — supported outcomes and the team's part in them. For a general analysis, use assessment criteria instead of implying a real deployment.
6. **When I would choose differently** — boundaries and signals for revisiting the choice.

Use these as prompts, not mandatory headings in every article. An essay should still have a natural argument. Forcing identical sections into every piece would feel mechanical.

Optional practical ending: a short set of questions to take into a design review. Each main piece should include at least one useful concrete aid: an original diagram, a decision comparison, a checklist or a worked example. Do not add a diagram merely as decoration.

Keep formal ADR identifiers, acceptance statuses and governance fields out of the main reading experience. Public writing is not necessarily an approved record of an employer's production decisions.

## Presentation

Use the existing theme as defined in [brand.md](brand.md).

- Typography-led index with one featured piece and a compact list of selected articles.
- Article title, short decision-oriented description, topic and month/year. Reading time can be added if calculated honestly.
- Three initial topic groups: Architecture; Operations & FinOps; Technical leadership.
- Wide desktop space for a small annotated sketch; keep body text approximately 65–75 characters wide.
- A quiet green summary panel near the opening; fine rules and mono captions for comparisons and figures.
- Diagrams in the same green, paper and muted palette, with labels readable on mobile.
- Optional short linked contents for longer pieces, not a dashboard of article metadata.
- No comments, reaction counts, social counters, pop-ups or subscription wall.
- A restrained contact link and related articles after the conclusion. Keep the reading experience primary.
- Keep URLs independent of publication dates, so an update does not require a URL change.
- RSS can be added as a low-maintenance way to follow the writing. A newsletter is a separate future decision.

## Candidate articles

These are working titles and research angles, not claims about Adam's historical decisions or completed drafts.

| Working title                                                      | Specific question                                                                              | Useful supporting artifact                          | Needed before first-person publication                                                       |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| A cloud saving is only a saving if you can still recover           | How do backup, retention and resource changes affect recovery obligations?                     | Cost/recovery comparison with explicit assumptions. | Adam's actual choices, validation and any disclosable operational evidence.                  |
| When the application becomes multi-tenant before the database does | Which boundaries protect isolation while old and new models coexist?                           | Conceptual trust and data-boundary diagram.         | Confirm the architecture details that can be shared; independently check technical claims.   |
| The handover is part of the architecture                           | What must the team be able to decide, operate and change without the original architect?       | A practical handover and ownership checklist.       | Specific examples and an honest distinction between observed results and principles.         |
| The cost of leaving the old system running                         | What operational and organisational costs remain during hybrid modernisation?                  | A coexistence-cost map.                             | Workload examples and the actual alternatives considered.                                    |
| Who owns the shared service when it fails?                         | How do shared identity, reporting or integration services acquire usable production ownership? | Ownership boundaries and an incident decision flow. | Confirmed, anonymised examples; no invented incidents.                                       |
| The recovery time hidden inside your identity architecture         | Which authentication dependencies affect recovery and degraded operation?                      | A conceptual dependency and failure-path sketch.    | Technical research and actual experience if framed as a personal case.                       |
| Faster provisioning changes who can make decisions                 | What changes in access, approvals and ownership when environments take hours instead of days?  | Before/after workflow, with masked metrics.         | Verify the process changes rather than extrapolating them from the CV's provisioning result. |
| A standard teams can use without asking its author                 | What makes engineering guidance reusable rather than a new bottleneck?                         | An annotated decision/example pairing.              | Examples of the standards and how the teams used them.                                       |

Suggested launch selection: the cloud saving/recovery piece, the multi-tenancy piece, the handover piece and the reusable-standard piece. This covers operations, architecture and leadership while remaining connected to the site's positioning. Final selection depends on available evidence and Adam's interest.

## Cadence and retrospective collection

No fixed public schedule. Quarterly is a useful planning ceiling for substantial retrospective pieces, not a requirement to fill every quarter.

Start with three or four strong articles. Build towards roughly eight to twelve selected pieces across recent experience, only as worthwhile source material becomes available. There is no need to manufacture a full calendar or produce a large archive at launch.

For a proposed retrospective collection covering 2023–2025, one candidate per quarter would provide up to twelve slots. Those years are a planning example, not an established chronology. Choose the actual periods after reviewing Adam's notes, existing writing and recollection. Leave quarters empty when there is no strong subject.

### Publication and experience dates

Display publication as month and year, for example `November 2026`.

- An article newly written now about a 2023 decision is published now. It can carry a secondary note such as `Retrospective: 2023` once that experience period is confirmed.
- Existing older writing can retain its original publication month when Adam supplies the original or a reliable record. Identify a substantial later revision separately.
- Never assign earlier publication dates simply to make the archive appear established.
- Keep experience period, original publication and subsequent revision separate in content records. A future implementation should store only known date precision and not fabricate a day to satisfy a field or search metadata.
- Month-level dates should be consistent across the UI, feeds and metadata. Do not use a concealed day-level date to imply false precision; exact timestamps should be added only when genuinely known or when publishing actually occurs.
- Write retrospective analysis with the constraints and knowledge available at the time clearly distinguished from what became apparent afterwards.

The archive can therefore be browsed by the period discussed while retaining an accurate publication month. A curated topics-first index will also avoid suggesting a busy chronological publishing history that does not exist.

## Editorial quality gate

Before a piece becomes public:

- It helps a specific reader with a real decision.
- The central argument is clear and its limits are stated.
- First-person experience and outcomes have a factual basis.
- Team contribution and Adam's responsibility are distinguishable.
- Sensitive details and the existing masking preferences are preserved.
- Sources are linked; invented or illustrative examples are identified.
- Technical advice has been checked against appropriate primary sources.
- Publication and experience dates are accurate.
- Its composition follows the established theme and works on mobile.

## Next step

Review the local `/writing/` page and the handover essay first. Use Adam's actual edits to refine the layout, argument and voice profile. Gather project-specific evidence only where an article is deliberately being developed into a personal case study. The implementation does not expose drafts in production builds.
