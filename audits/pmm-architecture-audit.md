**The repository has a credible foundation for a PMM operating system, but it is not yet complete end-to-end.** It is strongest once usable context and strategic decisions already exist. Its largest weakness is turning heterogeneous company material, or unanswered research questions, into that reusable context before producing strategy and deliverables.

A senior PMM could use it today as a governed workbench, supplying the research judgment and coordination themselves. They could not yet reliably hand it a company folder or broad goal and expect the system to establish the necessary understanding, resolve dependencies, and maintain the full learning cycle.

I reviewed README, all **44 SKILL.md files**, the shared architecture, and relevant research, strategy, governance, competitor, pricing, and measurement references/templates. This assesses the **current working tree**, including pre-existing uncommitted changes. I made no changes, created no files, and ran no behavioral evaluations. “Strong” below means a complete documented workflow within its stated scope, not independently demonstrated runtime reliability.

**1. Architecture inferred from the current repository**

The actual architecture has two context paths:

```text
Company notes / codebase / conversations
    → product-marketing-context
    → provisional bootstrap document

Customer evidence / competitor URLs / opportunity evidence
    → specialized research and intelligence skills
    → separate findings, profiles and language banks
    → SSOT setup or scan
    → human review and approval
    → governed core + living intelligence

Approved context + accepted decisions
    → positioning / messaging / pricing / ongoing GTM
    → motion and channel skills
    → output-quality review
    → messaging consistency review
    → launch readiness, where applicable

Results / field evidence
    → domain analysis
    → SSOT scan → confirmation → proposals → approval
```

Three architectural strengths deserve preservation:

- **Shared context consumption is explicit.** Skills load manifest-mapped SSOT, preserve covered canon, and use bootstrap context only provisionally.
- **Persona reuse is unusually well specified.** Downstream skills select relevant intelligence into an audience brief rather than create another persona.
- **Review responsibilities are separated.** Output compliance, messaging alignment, and launch clearance answer different questions.

The [SSOT consumption contract](/Users/mrignaynipandey/PMM-Skills/skills/_shared/ssot-consumption.md) is the strongest connective tissue in the repository.

However, the first and last connections are incomplete:

- There is no general workflow for **company-material intake → cross-domain synthesis → reviewed context baseline**.
- There is no consistent workflow for **measurement result → reusable finding → affected assumption/decision → context-update proposal**.

The launch orchestrator fills a narrower role. It conducts an accepted new-market entry, rather than orchestrating the whole PMM operating system.

**2. Audit of the three starting states**

| Starting state | Classification | What works | What prevents end-to-end use |
|---|---|---|---|
| **Has research** | **Partial** | Customer research analyzes transcripts, surveys, tickets and reviews. Win/loss and objections preserve source distinctions. SSOT setup accepts positioning docs, persona research, competitive notes and decks. | No common source inventory, heterogeneous ingestion contract, cross-domain reconciliation method, or baseline completeness review. The PMM must decide how to distribute material and combine findings. |
| **Partial research** | **Partial** | Evidence labels, confidence, ranked gaps, validation tasks and owners are widely required. Persona hypotheses and provisional strategy are supported. | Gaps remain attached to individual deliverables. No consolidated research backlog, coordinated study design, collection progress, or explicit criteria for when evidence is sufficient for the next decision. |
| **Starting from scratch** | **Partial, weakest** | Digital research, competitor profiling, provisional personas, market sizing and pricing research provide useful components. | No guided discovery sequence spanning company, product, market, category, customer, sales and economics. Several skills expect inputs that scratch research is supposed to establish. |

**Has research**

The repo can extract substantial signal from supplied customer evidence. It also explicitly preserves contradictions and separates customer language, interpretation, and proposed marketing language.

But “ingest a company folder” requires more than these individual analyses. For example:

> A deck says enterprise buyers value control; interviews favor simplicity; CRM wins cluster in mid-market; product docs show the enterprise capability is still beta.

Individual owners can analyze each source. The repo does not prescribe how to establish whether this is a segment difference, a product-version difference, unsupported positioning, or a genuine contradiction requiring a decision.

[SSOT `/setup`](/Users/mrignaynipandey/PMM-Skills/skills/ssot-context-loop/references/ssot-spec.md:182) extracts claims and maps them into files. It does not provide the full synthesis and reconciliation process needed before those claims become a baseline.

**Partial research**

The evidence-gap contract is a strong starting point. It asks what would change if an assumption proves wrong and assigns resolution work.

Its unit of operation is nevertheless **the deliverable**, not the company’s learning agenda. Several skills can independently generate overlapping interview, proof, segment and pricing tasks. There is no owner responsible for combining those into the smallest useful research program.

**Starting from scratch**

[Customer research](/Users/mrignaynipandey/PMM-Skills/skills/customer-research/SKILL.md) claims ownership of research design, sampling and interview methodology, but its detailed guidance emphasizes extraction and online research. Recruiting, screeners, interview guides, study sequencing and synthesis acceptance criteria are much thinner.

There is also a dependency tension:

- Market-entry asks for candidate-buyer understanding and routes missing persona research to the persona owner.
- Persona work expects an accepted market and routes market selection back to market-entry.
- Provisional hypotheses are allowed, but no overarching workflow explains how exploratory buyer research precedes accepted market selection.

An experienced PMM can resolve this. The system should make that sequence explicit.

**3. Capability matrix**

These classifications consider both establishing the context and maintaining it for reuse.

| Capability | Classification | Assessment |
|---|---|---|
| Company/product overview | **Partial** | Bootstrap and SSOT product files exist; organizational context, portfolio relationships and business constraints are thinner. |
| Business goals | **Partial** | Bootstrap captures goals; GTM uses them. No explicit governed home for objectives, horizons, constraints and baseline performance. |
| Market/category | **Partial** | Market-entry and positioning cover sizing and framing; ongoing category and market understanding lacks a dedicated synthesis workflow. |
| ICP and segmentation | **Partial** | Detailed shared scoring and decision inheritance; exploratory segmentation and canonical storage of the full segment model remain unclear. |
| Personas/buying committee | **Strong** | Evidence/hypothesis/reuse modes, attribute provenance, confidence, committee roles, exclusions and downstream reuse are explicit. |
| Pains, jobs and use cases | **Strong** | Research extraction, persona attributes, switching dynamics and living use cases connect effectively. |
| Customer evidence/VoC | **Strong** | Quotes, interpretations, context, contradictions, denominators and limitations have a clear owner and reusable output. |
| Product capabilities | **Partial** | SSOT distinguishes shipped, unshipped and roadmap claims; product-document/demo validation workflow is underdeveloped. |
| Competitors and alternatives | **Partial** | Detailed profiles and buyer alternatives exist; URL/SEO emphasis and competing stores weaken reuse. |
| Differentiation | **Strong** | Positioning owns it, traces capabilities to buyer value, and performs competitive/proof stress tests. |
| Positioning | **Strong** | Defined owner, evidence trace, trade-offs, inherited segment and approval routing. |
| Messaging | **Partial** | Strong capability/proof/persona translation; reusable architecture is narrower than enterprise messaging needs and persistence is not fully specified. |
| Objections | **Strong** | Discovery/library owner and response/collateral owner are separated; provenance and refresh are explicit. |
| Proof/evidence | **Partial** | Living evidence and claim restrictions exist; reusable proof status, scope, permissions and expiry are not consistently modeled. |
| Pricing/packaging | **Partial** | Methods and strategy owner exist; approved pricing, entitlements and commercial-policy context lack an explicit SSOT destination. |
| Sales motion | **Partial** | GTM and RevOps define it; persistent approved model and reader mapping remain underspecified. |
| Customer journey | **Partial** | Website, acquisition, activation, upgrade and post-sale workflows exist; no unified researched journey model across them. |
| Historical decisions | **Partial** | Core changes receive records; broader strategic, research and “retain current strategy” decisions are not consistently recorded. |
| Assumptions versus evidence | **Strong** | Shared labels, confidence distinctions and gap preservation are pervasive. |
| Confidence/source provenance | **Partial** | Rich domain-level fields; no common source/finding identity and lineage contract across the system. |
| Mixed-material intake | **Missing** | No general folder inventory, extraction coverage, source classification and reconciliation workflow. |
| Cross-domain synthesis | **Partial** | Customer synthesis and SSOT drift comparison exist; initial company-wide reconciliation is missing. |
| Coordinated research planning | **Partial** | Many local validation tasks; no consolidated program and progress loop. |
| Goal-based routing | **Partial** | Natural-language triggers and domain handoffs; no general entrypoint that diagnoses context readiness. |
| SSOT approval/governance | **Strong** | Baseline and subsequent changes have explicit human gates and auditable proposals. |
| Measurement/field-learning closure | **Partial** | Domain metrics and field intelligence exist; standardized context-update handoff is absent. |
| Segment selection ownership | **Duplicate/overlapping** | Market-entry owns selection, but persona, positioning and comparison-page fallbacks can also select. |
| Competitive knowledge storage | **Duplicate/overlapping** | Profiles, comparison-page data and SSOT competition have no complete projection/ownership contract. |
| Output/consistency/readiness reviews | **Strong** | Legitimate complementary responsibilities; these should not be merged. |

**4. Context/SSOT gaps**

The current SSOT is principally **product truth, positioning, buyer context and field intelligence**. It is not yet a complete PMM context model.

The [fixed file layout](/Users/mrignaynipandey/PMM-Skills/skills/ssot-context-loop/references/ssot-spec.md:35) has no explicit canonical home for:

- Business objectives, strategic constraints and success horizons.
- Market structure, category dynamics and the accepted segmentation model.
- Approved pricing, packaging, entitlements and commercial policies.
- Ongoing GTM model, sales motion and cross-functional decision rights.
- The researched customer journey and measurement baseline.

These can be mentioned in existing files or decision records, but that is not equivalent to a defined current-state home that downstream skills know to load.

Other material gaps:

1. **Approval, evidence and validity need separate treatment.** A source can substantiate that a founder made a claim without substantiating the claim itself. Bootstrap labels user/file statements Sourced; readers need the underlying source type and verification status too.
2. **The bootstrap-to-SSOT transition is underspecified.** Authority precedence is clear, but coverage tracking, unresolved bootstrap proposals and references to their approved replacements are not.
3. **One claim per file needs cross-references.** Single ownership is useful; without stable claim references, the same buyer pain or capability can be repeated differently across positioning, personas, use cases and evidence.
4. **Canon versioning is inconsistent.** Launch contracts require a date-based canon version. SSOT uses section validation dates and decision records, without a single explicit release/version model.
5. **Manifest schemas conflict.** `/manifest` shows `agents` as a list of named entries; the later GTM example shows a keyed mapping. Readers should have one contract. See [manifest schema](/Users/mrignaynipandey/PMM-Skills/skills/ssot-context-loop/references/ssot-spec.md:297) and [migration example](/Users/mrignaynipandey/PMM-Skills/skills/ssot-context-loop/references/ssot-spec.md:362).
6. **Enterprise scope is thin.** Multiple products, regions, segments and business units need explicit inheritance and exception rules, beyond separation by client.
7. **Persistence assumes GitHub.** Mandatory commit/push is not configurable for companies whose approved knowledge system is elsewhere. This is an adoption constraint, not a reason to remove durable persistence.

**5. Research and synthesis gaps**

The missing capability is broader than “more customer research.”

**Intake and coverage**

No shared process establishes which files were found, which were readable, which were actually analyzed, which duplicate earlier sources, and which remain excluded or unavailable. PDF reports, decks, spreadsheets and transcripts have no common extraction/coverage contract.

Tool guides help access systems; they do not supply this methodology.

**Reconciliation**

Customer research preserves conflicting customer evidence, and SSOT scan compares signals with existing canon. Neither fully handles **conflicting inputs before canon exists**.

A baseline needs to distinguish:

- Contradiction.
- Different segment, persona or stage.
- Different product version or time period.
- Seller interpretation versus buyer report.
- Approved historical decision versus current factual evidence.
- Unknown requiring validation.

**Research design**

The repo needs more operational detail within existing research ownership:

- Decision and competing hypotheses.
- Appropriate method and participant/cohort selection.
- Recruiting and screening.
- Interview/survey instruments.
- Analysis plan and bias controls.
- Evidence sufficiency and decision criteria.
- Findings-to-context handoff.

The current minimum-data-point rules are too coarse to serve as universal readiness criteria. Five community posts and five buyer interviews are not interchangeable evidence.

**Market, product and internal discovery**

Market-entry is a decision brief, not a general category-research program. Competitor-profiling is largely website, review and SEO intelligence. Product docs and stakeholder conversations lack a comparable research workflow.

**Confidence and contradictory signals**

Confidence standards vary across research, segment scoring and SSOT. These can remain method-specific, but need a shared explanation of their meaning and limits.

The SSOT also categorizes a one-off or outside-ICP signal as possible `noise`. That needs refinement: a credible single product contradiction or emerging adjacent-market signal may deserve investigation even before repetition. See [verdict definitions](/Users/mrignaynipandey/PMM-Skills/skills/ssot-context-loop/references/ssot-spec.md:168).

**6. Routing/orchestration gaps**

**Users can ask naturally, but dependable multi-step diagnosis is not yet specified.**

Existing routing covers:

- Skill discovery through descriptions.
- Local upstream/downstream handoffs.
- New-market launch gates.
- Asset remediation ownership.

It does not consistently cover:

> “Here is our company folder. Help us understand why growth has stalled.”

The system needs to infer the decision, inventory available context, identify missing evidence, select owners, and continue through dependencies. Today, that work falls to the host agent’s general judgment.

Specific limitations:

- `product-marketing-context` offers codebase auto-drafting or conversational collection, rather than company-material intake.
- `ssot-context-loop`, without a command, asks for scope and lists commands instead of diagnosing the workflow.
- `market-entry-orchestration` blocks at missing artifacts and names the next owner, but is explicitly limited to accepted market entry.
- `go-to-market-strategy` inventories upstream strategy, but should not become a generic research router.
- No common workflow state tracks research tasks, outstanding approvals, completed findings and readiness to proceed.

The historical routing result does not demonstrate this capability. [Eval documentation](/Users/mrignaynipandey/PMM-Skills/evals/README.md) says routing evaluates request text alone, and [measured results](/Users/mrignaynipandey/PMM-Skills/evals/RESULTS.md) concern an earlier skill catalog. That tests skill selection, not a sustained operating-system workflow.

**7. Downstream skills rebuilding context unnecessarily**

| Skill | Rebuilding/overlap risk | Recommended boundary |
|---|---|---|
| `competitor-alternatives` | Can score/select a lead segment when context is missing; independently conducts deep competitor research and creates competitor data files. | Route market selection upstream. Consume competitor profiles; create a presentation-specific projection only. |
| `content-strategy` | Independently mines calls, surveys, forums, sales and support for themes and language. | Use existing research first; retain incremental content-question research and return new findings to its research owner. |
| `launch-strategy` | Inherits accepted strategy but its required output still requests sizing and a scoring table. | Reference accepted sizing/selection; re-analysis only through an explicit upstream review. |
| `positioning-strategy` | Can select a best-fit segment when none is accepted. | Keep a provisional fit hypothesis, but route the market decision to its owner. |
| `icp-and-buyer-personas` | Ownership says accepted market; generation process can still score/select a lead segment. | Distinguish exploratory segmentation evidence from accepted market selection. |
| `messaging-framework` | Can infer provisional positioning and persona lines despite separate upstream owners. | Allow reaction drafts, but make the upstream dependency and return path explicit. |

The repeated “read context, ask only for missing facts” sections are mostly defensive repetition, not necessarily duplicate research.

Likewise, **task-specific audience briefs, account hypotheses and persona cards are legitimate adaptations** when they preserve source/version/status. The shared contract already protects that distinction.

**Deliverable/assignment bias**

Yes, the repo remains over-optimized for producing outputs relative to building understanding first.

Evidence includes:

- Bootstrap prefers codebase/marketing-copy extraction.
- Strategy skills repeatedly instruct agents to produce a provisional answer despite missing evidence.
- Messaging is organized heavily around capability tables and hero lines.
- Launch templates still pull in full market sizing and scoring.
- Shared gap prioritization centers on a deliverable’s “main number or lead claim.”
- Launch references explicitly describe assignment context.

Recent additions improve ongoing GTM, field intelligence and governance. The remaining imbalance is methodological: **there are more explicit standards for the finished artifact than for the investigation that makes it credible.**

**8–9. Prioritized changes, with existing-owner assessment**

**P0: Foundational**

| Change | Existing skill assessment first | Recommendation |
|---|---|---|
| **Company-material intake and context-readiness diagnosis** | `product-marketing-context` already owns context setup, but its two intake modes do not handle mixed evidence comprehensively. SSOT setup stores claims without full intake diagnosis. | Extend `product-marketing-context` with company-folder/material intake and goal-based diagnosis. No new skill. |
| **Cross-domain baseline synthesis** | `customer-research` can synthesize customer evidence; win/loss, objections and competitors own other domains. None owns their integrated baseline. | Let `product-marketing-context` assemble domain findings into a context proposal; let SSOT own reconciliation governance and approval. Keep domain analysis with existing owners. |
| **Complete context model and reader contract** | SSOT has the right authority, but its fixed layout omits important context and has schema/version inconsistencies. Adding another context skill would create competing authority. | Extend the SSOT specification with explicit homes or authoritative references for goals, market/segments, pricing, GTM, journey and measurement. Standardize manifest and version semantics. |
| **Guided research-plan and gap-closing workflow** | `customer-research` already claims research-design ownership, but does not fully operationalize it. Local evidence-gap lists cannot coordinate a program. | Strengthen research planning, collection, synthesis and follow-up modes. Consolidate domain gaps through context intake; preserve specialist research ownership. |
| **Evidence readiness before consequential strategy** | Labels prevent fabrication, but do not determine whether evidence is sufficient. Output-quality-check cannot supply an unstated domain standard. | Add decision-specific readiness criteria to existing research/strategy skills: proceed, proceed provisionally, or hold the affected choice. Preserve independent progress. |
| **Remove contradictory ownership instructions** | Shared boundaries are largely correct; fallback procedures and older templates undermine them. A router would inherit these contradictions. | Fix selection/research fallbacks in persona, positioning, comparison and launch workflows before expanding orchestration. |

The desired user-facing result should be:

> “Here is what we already know, what is interpretation, what conflicts, what evidence would change the decision, and the existing owners that will resolve it.”

**P1: Important**

| Change | Why existing support is insufficient | Recommendation |
|---|---|---|
| **Common source/finding lineage** | Each intelligence skill captures provenance differently; citations alone do not deduplicate or connect findings across handoffs. | Add a shared evidence-record contract with source/finding IDs, location, date, source type, scope, confidence rationale and dependencies. Reuse existing raw stores. |
| **Broader research methods** | Customer research favors online VoC; market-entry favors decision briefs; competitor profiling favors URLs/SEO; SSOT records product truth but does not validate it. | Add references/modes to these owners for primary research, category/market structure, internal stakeholder research and product validation. No separate market/product research skill yet. |
| **Measurement-to-context closure** | Analytics, RevOps, experimentation and motion skills measure locally; SSOT accepts supplied signals but receives no consistent learning packet. | Standardize the handoff: result, cohort/window, limitations, finding, challenged assumption, affected context, proposed review and owner. |
| **Unified researched journey** | Existing journey skills cover separate surfaces and lifecycle stages. | Extend personas/customer research to capture the reusable journey; execution skills consume it. Avoid a second journey authority. |
| **Reusable proof lifecycle** | Evidence files and claim checks lack a complete permission/scope/expiry model. | Extend living evidence and customer-marketing proof handoffs with claim scope, verification, approval, permitted use and review date. |
| **Configurable durable persistence and enterprise scope** | SSOT assumes GitHub and one client-shaped context hierarchy. | Preserve governance while supporting approved storage backends and product/region/business-unit scopes. |
| **Three complete workflow evaluations** | Current tests mostly assess individual outputs and routing; some expectations retain older boundaries. | Add mixed-material, partial-evidence and scratch scenarios that test context reuse, contradictions, research completion, approvals and learning closure across handoffs. |

**P2: Nice to have**

| Change | Why existing support is insufficient | Recommendation |
|---|---|---|
| **Context/research status summary** | `state.md` tracks SSOT status but not the complete research workflow. | Extend its reporting or link to the intake workflow’s task state; do not create a separate competing dashboard store. |
| **Selective downstream invalidation** | Manifest impact analysis exists, while launch contracts broadly stale every downstream artifact on a new canon version. | Track which decisions/claims changed and which assets actually depend on them. |
| **More representative walkthroughs** | README examples emphasize already-defined tasks and accepted decisions. | Add established-company examples starting with mixed research, incomplete knowledge and zero research. |
| **Optional local helpers** | Intake inventory and consistency checks currently rely on agent execution of prose. | Later add read-only inventory/schema checks, after the contracts stabilize. No infrastructure rewrite first. |

**New skills recommendation: none initially.**

The missing work can largely be addressed by strengthening and connecting `product-marketing-context`, `customer-research`, the specialist intelligence owners, and `ssot-context-loop`.

A separate general PMM orchestrator becomes justified only if the expanded context entrypoint cannot cleanly manage goal diagnosis and workflow state. Its scope would then be routing and dependency management, with no independent research, strategy or canonical knowledge ownership. I would not add it before fixing the existing contracts.
