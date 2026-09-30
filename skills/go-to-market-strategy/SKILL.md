---
name: go-to-market-strategy
description: "Determine how to serve and win an accepted market over time. Use for GTM model, sales-led versus product-led versus partner-led or hybrid, route to market, motion priorities, responsibilities, validation and GTM strategy review. Market selection, prices, launches and final assets retain separate owners."
metadata:
  version: 2.0.0
---

# Go-to-Market Strategy

## Approved context and evidence

Read `../_shared/evidence-gaps.md` and `../_shared/ssot-consumption.md`.
Load only relevant approved manifest context and record sources in Inputs and assumptions.
Read `../_shared/segment-selection.md` when an audience decision is needed; inherit accepted segments and ICP.
Separate sources, interpretation, and proposals. Missing evidence remains Assumed or Gap.
Do not edit SSOT. Route proposed canon changes to `ssot-context-loop` for human review and approval.

## Inputs and entry gate

Inventory accepted market decision (`market-entry-brief`), ICP/personas (`icp-and-buyer-personas`), positioning (`positioning-strategy`), messaging (`messaging-framework`), pricing/packaging (`pricing-strategy`) and relevant approved SSOT.
Consume applicable `customer-research`/VoC, `competitor-profiling`, `win-loss-intelligence` and `objection-intelligence` findings with provenance, sample limits and confidence. Intelligence owners collect and synthesize; this skill decides proposed commercial implications.
When an accepted input is absent, name the upstream owner and gap. A provisional option comparison is allowed with labeled assumptions; no invented accepted strategy or automatic canon replacement.

## Workflow

1. **Frame the commercial decision.** State horizon, accepted market and buyer, buying committee, purchase complexity, value realization, contract/economic context and company constraints. Preserve accepted inputs verbatim in an inheritance register.
2. **Compare viable GTM models.** Evaluate sales-led, product-led, partner-led and hybrid against buyer buying behavior, product time-to-value, adoption friction, service/support needs, deal economics, sales capacity, partner value and evidence. Separate observed facts from modeled assumptions. Hybrid needs explicit segment/stage responsibilities, not a list of every channel.
3. **Propose route and priorities.** Explain the chosen model and rejected alternatives. Define direct/indirect route, motion/channel priorities, eligibility, commercial constraints and where each motion hands off. Pricing remains with `pricing-strategy`; market selection stays with `market-entry-brief`.
4. **Sequence and assign.** Stage motions by evidence, dependencies and capacity. Specify PMM, Sales, Product, CS, Partners, Marketing, RevOps and Finance responsibilities, decision rights and owners. Do not equate a launch date with the ongoing GTM model.
5. **Validate and revisit.** Define testable commercial assumptions, baseline/gaps, decision thresholds with rationale, guardrails, owners and milestones. Set a strategy review cadence and triggers such as buying-behavior change, economics deterioration, activation barriers, partner dependency or evidence contradicting canon. Avoid invented certainty and benchmarks.
6. **Route briefs.** Hand objectives, accepted audience, approved message/proof, motion role, dependencies, budget assumptions, success measures and learning needs to execution owners. Produce no final channel assets here.

## Handoffs

- Release-specific execution: `launch-strategy`; accepted new-market orchestration: `market-entry-orchestration`.
- Account, event, partner, post-sale or product narrative programs: `account-based-marketing`, `events`, `partner-marketing`, `customer-marketing`, `product-communications`.
- Seller, content and paid programs: `sales-enablement`, `content-strategy`, `paid-ads`.
- Activation and free/trial-to-paid: `product-activation`, `upgrade-conversion`.
- Measurement and commercial handoffs: `analytics-tracking`, `revops`; commercial assumptions/prices: `pricing-strategy`.

## Conflict and approval

If evidence challenges accepted market, ICP, positioning, messaging, pricing or GTM strategy, show the exact conflict, impact and source limitations. Propose review through `ssot-context-loop` and the upstream decision owner. Do not choose newer evidence silently, change canonical files, set prices independently or produce execution against an unapproved strategic change.
An accepted strategy may continue while review is pending only within its existing approvals and restrictions; flag affected plans and decision dependencies. Human approval is required before canonical strategic changes.

## Required output

Inputs and assumptions; accepted-input inheritance register; decision/horizon; evidence and gaps; model/options comparison; recommended route and prioritized motions; commercial assumptions/constraints; sequencing; cross-functional responsibilities; validation plan; review cadence/reconsideration triggers; execution briefs/handoffs; canon conflicts/proposed reviews; ranked Evidence gaps.
`output-quality-check` checks this decision artifact against these requirements. Market-facing assets undergo `messaging-consistency-audit`; launch readiness remains independent.

## Optional ideation

Only after objective, accepted audience, strategy and constraints are established, consult `../_shared/tactic-library/guidance.md` for candidate tactics. The owning motion skill evaluates each candidate.

## Related skills

`market-entry-brief`, `icp-and-buyer-personas`, `positioning-strategy`, `messaging-framework`, `pricing-strategy`, `customer-research`, `competitor-profiling`, `win-loss-intelligence`, `objection-intelligence`, `launch-strategy`, `market-entry-orchestration`, `account-based-marketing`, `events`, `partner-marketing`, `customer-marketing`, `product-communications`, `sales-enablement`, `content-strategy`, `paid-ads`, `product-activation`, `upgrade-conversion`, `analytics-tracking`, `revops`, `ssot-context-loop`.
