# Context establishment contract

Use this contract when establishing reusable PMM understanding, sending research
handoffs, returning findings, or preparing context proposals. It complements
`evidence-gaps.md` and `ssot-consumption.md`; it does not grant approval.
`product-marketing-context` integrates the workspace. Specialists own their
methods and domain artifacts. Only `ssot-context-loop` governs canon.

## Envelope and identity

Use lightweight Markdown tables or named fields with this frontmatter:

```yaml
---
contract: pmm-context-v1
artifact: context-workspace
project: example-company
product_scope: example-product
id: CTX-001
version: 1
updated: YYYY-MM-DD
owner: product-marketing-context
goal: Evaluate a new enterprise segment
return_to: product-marketing-context
---
```

Artifact types: `context-workspace`, `research-handoff`, `research-return`,
`readiness-assessment`, `context-proposal`. Omit inapplicable envelope fields.
Use stable project-scoped IDs: SRC (source), FND (finding), GAP, HND (handoff),
CTR (contradiction), PRP (proposal). Reuse existing IDs; never renumber on refresh.
Map specialist IDs to these IDs rather than losing lineage or double-counting.
Keep unknown metadata explicit. A generated version identifies the artifact,
not an invented source version. References may point to existing domain stores.

## Source/material inventory

One row per source or meaningfully distinct dataset. Record:

| Field | Required handling |
|---|---|
| ID, location, locator | Source ID; file/link/pasted statement; section, slide, timestamp, sheet or record. |
| Type, author/reporter, source role | Interview, CRM, deck, product doc, report, etc.; customer, seller, product owner, analyst or company collateral. |
| Dates and version | Event/collection date, source version and ingestion date separately. |
| Scope and coverage | Project/product, segment, role, region, stage, period; questions/topics covered. |
| Access/review state | Inventoried, inspected, analyzed, inaccessible, unreadable or partially inspected; identify inspected portions. |
| Lineage/duplicates | Original and derivative source IDs; multiple documents citing one interview are one underlying signal. |
| Limitations | Missing data, selection bias, access/use restrictions and unverified approval claims. |

Inventory before synthesis. Inspect goal-relevant material and disclose remaining
coverage. Do not claim a folder was fully analyzed when only selected files were.
Do not rewrite raw inputs. Reuse existing captured sources; SSOT owns capture
into its immutable `comms/` store. Do not discard unavailable materials silently.

## Evidence and findings

Each reusable finding records ID, statement, kind, evidence label, source IDs and
precise locators, supporting/opposing finding IDs, scope, method/derivation,
sample/denominator where meaningful, confidence with rationale, approval reference
when real, limitations, and expiry/review trigger. Unknown fields remain explicit.

| Kind | Meaning |
|---|---|
| Evidence | Observed data or a source report; identify which. A seller's report is not buyer truth. |
| Interpretation | Coded pattern or inference with derivation and limits. |
| Assumption | Unconfirmed premise, with reasoning and what would validate it. |
| Historical decision | A past choice; retain its scope, approval and supersession history. |
| Current approved decision | Explicit approval reference, applicable scope/effective date and no unresolved supersession. File existence is insufficient. |
| Unknown | No supported answer; link a Gap rather than filling it. |

Contradiction is a relationship between findings, recorded below, not a fourth
evidence tag. Use Sourced / Assumed / Gap (SSOT: [C] / [A] / [G]). A supported
interpretation may be Sourced with its derivation; unsupported extrapolation is
Assumed. Never introduce a top-level Derived label. A citation establishes what
the source says, not automatically that its claim is verified or approved.
Exact quotes require exact source wording. Reuse and approval never upgrade an
assumption into evidence. Confidence concerns this finding within this scope,
not the source platform in general or how often a draft repeated it.

## Contradictions and reconciliation

Record CTR ID, linked findings, scope, type, affected decisions, severity, owner,
proposed disposition, status and resolution evidence. Classify before resolving:

| Type | Treatment |
|---|---|
| Scope difference | Separate segment, role, stage or region; do not average away differences. |
| Time/product-version difference | Establish effective dates and applicability; retain historical truth. |
| Definition/measurement difference | Reconcile definitions, period and denominator with the data owner. |
| Reporter difference | Preserve buyer/seller reports; win-loss-intelligence owns outcome interpretation. |
| Evidence versus interpretation | Separate observation from the strategic conclusion. |
| Decision conflict | Verify approval scope and explicit supersession; escalate unresolved authority to SSOT. |
| Substantive factual conflict | Seek authoritative verification; hold dependent claims if consequential. |
| Evidence against approved canon | Preserve canon; route domain review and SSOT Gate 1, then Gate 2. |

PMC may explain an apparent conflict using demonstrated scope/time/definition
differences. It cannot pick a winner by recency, frequency or persuasive wording.
Keep competing explanations and the smallest discriminating test when unresolved.
A single material contradiction can warrant review; do not dismiss it as noise
merely because it is one-off or outside the current ICP.

## Decision-specific context readiness

Assess the goal and intended action, not document completeness. Identify the
context requirements and what changes if each plausible answer differs.

| Dimension | Values |
|---|---|
| Support | Evidence, interpretation, assumption, unknown |
| Authority | Approved, proposed, unapproved, approval unknown |
| Health | Current, stale, conflicting, superseded, missing |

These dimensions complement existing SSOT section statuses, not replace them.
Use a table: Requirement | Why needed | Source/version | Support | Authority |
Health | Gap ID | Evidence readiness | Permitted next action | Approval dependency.

| Evidence readiness | Meaning |
|---|---|
| **PROCEED** | Evidence is sufficient. |
| **PROCEED PROVISIONALLY** | Evidence is incomplete, but the risk is understood. |
| **HOLD THIS DECISION** | A consequential evidence gap needs to be resolved first. |

For provisional work, state the assumption, understood risk, permitted scope and
validation trigger. For a hold, name the affected decision, gap, owner and closure
criteria. Continue independent work. Missing approval is a separate dependency,
not an evidence hold; PROCEED never grants approval or bypasses a gate.
Research needs a useful question/scope, not an approved persona. Strategy proposals
need enough understanding to compare choices or explicit bounded hypotheses.
Drafts need a defensible brief and disclosed limitations. Approved execution also
needs the existing decision/claim/launch approvals. Reassess when inputs change.

## Research gaps and routing

Each GAP records: question; affected goal/decision; existing finding IDs;
counterfactual (what changes if wrong); priority; type; primary owner/contributors;
suggested method/retrieval; completion criteria; status; dependencies; return_to.
Statuses: open, assigned, in-progress, partially answered, resolved, deferred.
Reopen with a reason when new evidence invalidates closure. A report alone does
not resolve a gap. Approval gaps route to governance, not another study.

Types: missing material, insufficient evidence, unresolved contradiction, stale
validation, missing specialist interpretation, missing approval.
Priorities: blocking (hold affected decision), consequential (research or bounded
provisional route), non-blocking (defer or permitted assumption). Rank decision
impact, uncertainty, urgency and resolution effort, without arbitrary scores.
Retrieve existing information → analyze unprocessed evidence → clarify scope or
definitions → request internal facts → collect new research.

| Question | Primary owner |
|---|---|
| Customer jobs/pains/triggers/behavior/language; general study methods | customer-research |
| Closed-opportunity drivers and buyer/seller reason disagreement | win-loss-intelligence |
| Recurring objections and their contexts | objection-intelligence; sales-enablement owns final responses |
| Competitive landscape, competitor capabilities/offers/claims/pricing observations and competitive changes | competitor-profiling; customer-research supports customer review synthesis |
| ICP/persona attributes and buying committee | icp-and-buyer-personas |
| External market structure, category conditions and emerging-opportunity research | market-intelligence |
| Company-specific sizing, candidate fit/entry evaluation and where/whether to enter | market-entry-brief (exploration before decision mode) |
| Willingness to pay, value metric, packaging and pricing methods | pricing-strategy |
| Positioning choice/differentiation | positioning-strategy (strategy proposal) |
| Messaging architecture/translation | messaging-framework (uses upstream strategy/personas) |
| Sales process or CRM definitions | revops and internal sales/data owners |
| Product availability/limits/roadmap or internal business goals | Relevant human/system-of-record owner, coordinated by PMC |
| Measurement or tests of assumptions | analytics-tracking / marketing-experimentation as applicable |
| Canon approval/conflicting approved decisions | ssot-context-loop |

One question has one primary owner. Contributors reuse source IDs rather than
duplicate studies. PMC does not adopt these owners' methodologies or make their
strategic choices. A handoff is not permission for outreach, spending or access.
From scratch: explore problem/customer/category → buyer/segment hypotheses →
evidence → market-selection proposal → personas in that scope → strategy.
Exploration does not require an accepted market or approved candidate persona.

## Research handoff and return

HND fields: linked GAP IDs; exact question/affected decision; source/finding
references; approved context/version; hypotheses/opposing evidence; scope,
constraints/exclusions/dependencies; requested return/completion criteria;
primary owner/contributors; return_to. Request only the analysis needed.

The receiving owner preserves IDs, narrows its domain work, and returns:
questions/GAP IDs addressed; provenance-bearing findings; method/sample/denominator
and limitations; supporting/opposing evidence; confidence; unanswered questions;
completion-criteria assessment; domain artifact link; unapproved context implications
and suggested destinations. Status: answered, partially answered, inconclusive,
unable to complete. Return to PMC when it originated the handoff; standalone
domain artifacts remain valid and may attach this return without a new store.

PMC checks scope, source lineage and completion criteria, integrates supported
findings without upgrading labels/approval, retains disagreements, updates gap
status, and reassesses readiness. Preserve old findings with supersession links.
An incomplete return leads to targeted follow-up or an explicit hold/provisional
route, never an endless automatic research loop.

## Context proposals and canonical destinations

PRP fields: exact wording/structured context; project/product scope; existing
wording/reference; findings/sources; interpretation/assumptions/conflicts;
domain owner; proposed destination; authority (proposed) and section status;
pending validation/permitted uses; affected readers/decisions/assets;
explicit human decision required. Propose supported portions without requiring
every gap to close. A held decision stays unresolved; approval cannot prove it.

Use the existing SSOT core/living destinations for their domains. Goals, approved
market/segment choices, pricing/packaging, sales motion, journey decisions and GTM
direction can use scoped SSOT-owned decision records or versioned approved
references under the SSOT spec. Evidence stays in its appropriate living home.
PMC never writes canonical files, decisions, manifests or reconciler state.
No SSOT: /setup proposal → Gate 2. Existing SSOT: /scan → Gate 1 → /propose → Gate 2.
Saving/correcting the workspace or a specialist report never grants canon approval.
