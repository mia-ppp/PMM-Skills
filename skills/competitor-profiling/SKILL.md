---
name: competitor-profiling
description: "Use when the user wants competitor research, a named competitor profile or dossier, competitive landscape discovery, an alternative-universe comparison, or competitive signals/change investigation. Accept URLs, supplied research, and targeted verification requests. For external market/category conditions, see market-intelligence; for comparison pages, see competitor-alternatives; for battlecards, see sales-enablement; for closed-deal causes, see win-loss-intelligence."
metadata:
  version: 1.2.0
---

# Competitor Profiling

Establish sourced facts about alternatives, structure a comparable landscape,
and verify changes against dated baselines. Separate facts, reported claims,
interpretations, and implications. Research does not approve strategy.

## Before starting

- Resolve the active project/product scope. Keep other projects' evidence and
  approval references out of this return; IDs are project-scoped.
- Read `../_shared/evidence-gaps.md` and `../_shared/ssot-consumption.md`.
- Read `../_shared/context-establishment.md` when available. It owns Phase 1
  evidence, readiness, and handoff/return semantics. Otherwise use the compatible
  minimum in [references/templates.md](references/templates.md).
  Read that reference for domain checks and the return template on every run.
- Load relevant manifest-mapped approved context. Record version, authority,
  health, and gaps. Bootstrap context stays provisional.
- Preserve originating HND/GAP/SRC/FND IDs, exact question, completion criteria,
  scope, constraints, opposing evidence, and return destination.
- Inventory profiles, raw captures, supplied dossiers, customer findings, and
  dated snapshots before collecting more. Mark inspection coverage and unavailable material.
- Resolve job/problem or named entity, geography, period, intended use, and depth.
  Ask only for missing facts that materially change the work.
  Exploration requires useful scope, not approved personas or an accepted market.

## Choose the smallest useful mode

Read the selected section of [references/modes.md](references/modes.md).
Use only modes needed for the question.

| Mode | Exact job and triggers | Output |
|---|---|---|
| Competitive landscape | Identify and structure the relevant alternative universe. “Who competes for this job?” “Map our alternatives.” | Inclusion rationale, alternative register, supported comparison, coverage/freshness view. |
| Entity profiling | Establish sourced facts about a named alternative. “Profile this competitor.” “Verify whether this feature exists.” | Focused or full dossier with field-level provenance and verification. |
| Competitive signals | Identify and verify changes against a dated baseline. “What changed since our last profile?” “Investigate this launch.” | Event/delta register with verification, materiality, and affected references. |

Landscape discovery may commission focused profiles before comparison.
Signals refresh affected fields and comparisons without repeating full studies.
Named-entity requests need not start with landscape discovery.

## Research and evidence

Use existing evidence and the smallest useful verification. URLs are optional.
Methods include supplied-material analysis, documentation, published commercial
terms, release notes, original filings, permitted demos/trials, and customer findings.
Scraping and SEO are optional methods, not prerequisites. Read
[references/tool-reference.md](references/tool-reference.md) only when those tools
fit the question. Missing tools never justify invented data.

Keep these distinctions explicit:
- Competitor-authored claim versus documented behavior versus direct verification.
- Customer-reported experience versus general product fact.
- Unknown capability versus scoped evidence of absence in a tier/version.
- Announcement versus available, beta, limited access, or withdrawn capability.
- Observed change versus inference about intent, demand, or commercial impact.
- Search overlap versus evidence of commercial competition.

Record lineage and counterevidence. Copies of one announcement are one signal.
Ratings, traffic, and review counts do not verify revenue or customer totals.
Never infer absence from an omitted feature or inaccessible page. Compare equivalent
versions, tiers, currencies, billing periods, and regions. No universal source-count
threshold establishes confidence or readiness.

## Persistence and refresh

Preserve the existing project-relative competitor-profiles location when used:

```text
competitor-profiles/
  raw/<alternative-slug>/<YYYY-MM-DD>/<capture-id>/
    scrapes/
    seo/
    reviews/
    supplied/
  <alternative-slug>.md
  _summary.md
  _signals.md
```

Use only applicable subdirectories. Existing date-only raw folders remain valid.
A capture ID prevents overwriting same-day runs. Retain source IDs and precise
paths on refresh. Capture collected raw evidence before synthesis when saving is
part of the task. Reference supplied originals without rewriting them; respect
access/use restrictions. If capture is unavailable, disclose the limitation.
Never overwrite earlier raw captures. Preserve profile versions, change history,
and supersession links. _summary.md is a derived comparison, not another authority.
_signals.md is an optional noncanonical event view, not an installed monitor.

Save only in the user's project when requested or workflow-authorized.
Do not write into the skills repository during production runs.
Research or a cadence does not authorize outreach, account creation, spending,
installed monitoring, or sending alerts.

## Ownership and handoffs

| Need | Owner and boundary |
|---|---|
| Market conditions, category conventions, opportunity hypotheses | `market-intelligence`. Competitive gaps do not establish demand. |
| Customer experience themes and reusable language | `customer-research`. Reuse findings and attribute reported experience. |
| Closed-deal causes and buyer/seller disagreement | `win-loss-intelligence`. Competitor presence is not loss causality. |
| Objection library | `objection-intelligence`. Route evidence, not invented responses. |
| Where/whether to enter and company-specific sizing | `market-entry-brief`. Landscape relevance does not select a market. |
| Who to target and buying group | `icp-and-buyer-personas`. Their targeting claims do not select our ICP. |
| Our positioning, differentiation, and category/frame | `positioning-strategy`. Maps/whitespace are research, not strategic choices. |
| Messaging architecture | `messaging-framework`. Observed wording does not change our messages. |
| Pricing/packaging decisions | `pricing-strategy`. Record terms without recommending our price. |
| GTM or competitive response decisions | `go-to-market-strategy` and relevant decision owners. Surface review needs without committing actions. |
| Battlecards and comparison pages | `sales-enablement` and `competitor-alternatives`. Consume sourced views and approved company claims. |
| Integrated context and goal-relative readiness | `product-marketing-context`. Return findings without becoming an orchestrator. |
| Approved canon, drift verdicts, and persistence | `ssot-context-loop`. Explicit human approval is mandatory for canonical changes. |

Never write canonical files, decisions, manifests, or state.md.
Return to originating PMC or named requester using the packet in templates.md.
Suggest competitive context for living/06-competitive.md and supporting evidence
for living/07-evidence.md without duplicating claims. SSOT chooses destinations
and gates. Verified external changes are not SSOT drift verdicts and never
silently rewrite strategy or collateral.

## Output rules

- Open with Inputs and assumptions, selected mode, scope, and inspected coverage.
- Use Sourced / Assumed / Gap with kind, verification, confidence/rationale,
  limitations, approval status, and review trigger.
- Expose derivations and labeled inputs without adding a Derived evidence tag.
- Preserve unknowns, opposing evidence, and completion-criteria assessment.
- End with ranked Evidence gaps: top five in the body, all others in an appendix.
  Give owners and milestones, explicitly marking suggestions.
- Use no em dashes. Keep sentences short and bullets led by outcomes.
