# Synthetic auditor smoke example

This fixture uses a synthetic SampleCo SSOT under `fixtures/ssot/`. It contains
deliberate channel variation, category/persona drift, generic value language,
incorrect capabilities, unsupported proof, and repeated drift. No company SSOT
or company asset is used.

## Executive summary

Assets scanned: 4 of 4 provided. Canon: synthetic SampleCo, reviewed 2026-09-01.
Aligned: 1. Approved variations: 1. Drift: 6. Contradictions: 2.
Unsupported claims: 1. SSOT review flags: 1. The category drift repeats in two
independent assets, which merits review but does not make it canonical.

## Prioritized remediation table

| Asset | Location | SSOT element | Current message | Classification | Severity | Why it matters | Canonical reference | Recommended action | Route to skill | Status |
|---|---|---|---|---|---|---|---|---|---|
| outbound.md | Email 1, paragraph 1 | Product capability | "automates every workflow" | CONTRADICTION | P0 / Critical | Claims execution that product truth explicitly excludes. | `core/02-product.md`, capabilities and anti-patterns | Replace with an accurate description of finding delays and showing traces. | `cold-email` | Open |
| outbound.md | Email 1, paragraph 1 | Proof | "saving teams 40% in operating costs" | UNSUPPORTED_CLAIM | P0 / Critical | No approved quantified result supports the percentage. | `living/07-evidence.md`, evidence | Remove the percentage or use approved evidence after verification. | `cold-email` | Open |
| outbound.md | Email 1, paragraph 1 | Category | "AI productivity platform for every business team" | DRIFT | P1 / High | Broadens the category and target beyond operations workflow analytics. | `core/00-what-it-is.md`, category; `core/03-who-it-is-for.md`, primary persona | Restore operations workflow context and audience. | `cold-email` | Open |
| outbound.md | Email 1, paragraph 1 | Persona | "every business team" | DRIFT | P1 / High | Expands the audience beyond the approved operations leader persona. | `core/03-who-it-is-for.md`, primary-persona | Restore the operations leader audience. | `cold-email` | Open |
| outbound.md | Email 1, paragraph 1 | Value proposition | "AI productivity platform" | DRIFT | P2 / Medium | Genericizes the workflow bottleneck and process-data value proposition. | `core/01-how-you-position-it.md`, position | State the specific job and outcome in channel language. | `cold-email` | Open |
| outbound.md | Email 1, paragraph 1 | Product outcome | "eliminates delays" | DRIFT | P2 / Medium | Overstates an insight and prioritization product as guaranteeing an outcome. | `core/01-how-you-position-it.md`, position; `core/02-product.md`, capabilities | State the product helps locate delays and prioritize fixes. | `cold-email` | Open |
| sales-deck.md | Slide 2, category frame | Category | "AI productivity platform for every business team" | DRIFT | P1 / High | Repeats the competing broad category frame in a second asset. | `core/00-what-it-is.md`, category | Correct the asset and add the repeated frame to SSOT review for validation. | `sales-enablement`; `ssot-context-loop` | SSOT review |
| Cross-asset | website.md Hero vs outbound.md Email 1 and sales-deck.md Slide 2 | Category / product definition | Website describes workflow bottlenecks and process traces. Email and deck call it an "AI productivity platform." | CONTRADICTION | P1 / High | The same buyer receives materially different product definitions across channels. | `core/00-what-it-is.md`, category; `core/01-how-you-position-it.md`, position | Align email and deck to the approved workflow analytics story; route each asset to its owning skill. | `cold-email`; `sales-enablement` | Open |
| Cross-asset | outbound.md Email 1; sales-deck.md Slide 2 | Category framing pattern | The same broad category appears in two independent assets. | SSOT_REVIEW_REQUIRED | P1 / High | The repetition may reflect a broader canon or enablement problem. It is not proof the current canon is wrong. | `core/00-what-it-is.md`, category | Review sources and current market evidence through the SSOT process; do not change canon automatically. | `ssot-context-loop` | SSOT review |
| website.md | Hero | Positioning | "find workflow bottlenecks before they affect service levels" | ALIGNED | None | Preserves approved problem and value. | `core/01-how-you-position-it.md`, position | No change. | `copywriting` | Verified |
| linkedin.md | Post body | Persona variation | "find the workflow delays... decide what to fix first" | APPROVED_VARIATION | None | Social phrasing emphasizes the same audience and strategic outcome. | `core/01-how-you-position-it.md`, position; `core/03-who-it-is-for.md`, primary persona | Keep. | `social-content` | Verified |

## Proposed corrections

For the outbound findings, route a proposed asset revision to `cold-email`.
Keep the operations leader persona, describe the trace and prioritization value,
and remove the unapproved 40% result. Do not change the SSOT.

## SSOT review queue

Review whether the repeated broad category frame in outbound and the sales deck
reflects stale enablement or a genuine change in market understanding. Treat this
as a review question only. Repetition does not update canon.

## Re-audit status

No corrected version supplied. All outbound findings remain Open. Website and
LinkedIn remain verified.

## Test coverage

- Aligned claim: website hero.
- Legitimate channel variation: LinkedIn post.
- Category drift and persona broadening: outbound email.
- Genericized and overstated value proposition: "eliminates delays."
- Contradictory capability: "automates every workflow."
- Unsupported proof: "saving teams 40%."
- Repeated cross-asset drift: surfaced as `SSOT_REVIEW_REQUIRED`, separated from
  asset-level fixes, with no automatic canon change.
