---
name: events
description: "When the user wants to decide, plan, activate, or measure an event as a product marketing or GTM motion. Covers owned events, sponsorships and exhibits, speaking, attendance for meetings, webinars, executive dinners, roundtables, conferences, trade shows, and customer or community events. Use for event strategy, event ROI decisions, event follow-up, or event marketing. For channel assets, route to their owning skill; for launch sequencing, see launch-strategy."
metadata:
  version: 1.0.0
---

# Events

Plan events as a GTM motion. Own the event decision, strategy, narrative brief,
activation map, follow-up logic, and measurement plan. Do not become an event
production or logistics planner. Catering, AV, venue sourcing, travel, and booth
shipping are out of scope unless an operational constraint changes the GTM plan.

## Before planning

- Read `../_shared/evidence-gaps.md` and `../_shared/ssot-consumption.md`.
- Read `../_shared/segment-selection.md` when selecting or prioritizing audiences.
- Check `.agents/product-marketing-context.md` (or legacy `.claude/`) when no
  applicable SSOT covers the needed context.
- Identify the event, date or planning window, role, business goal, target
  audience, resources or budget constraints, and decision owner. Do not stop
  for missing facts. Mark them Assumed or Gap and state what would resolve them.
- When an SSOT exists, use the project manifest and relevant canon files. Record
  the SSOT version or files used. Never alter canonical files.

## Workflow

### 1. Decide whether the event merits investment

State the event role: hosting, sponsoring or exhibiting, speaking, attending
for meetings, webinar or virtual event, executive dinner or roundtable,
conference or trade show, or customer or community event. Mixed roles are
allowed; describe each motion distinctly.

Choose one primary objective and any secondary objectives from pipeline
generation, pipeline acceleration, customer expansion, category or brand
building, product education, community, and customer advocacy. Explain why this
event merits investment now, how it supports the broader GTM strategy, and what
alternative or opportunity cost is relevant when known. Do not manufacture ROI,
attendance, pipeline, or conversion estimates. Mark unsupported estimates as
Assumed or Gap and identify the evidence needed.

### 2. Set the event strategy

Define the target segment, personas and accounts, event objective, theme or
thesis, audience offer, CTA, desired buyer action, sales involvement, success
criteria, and pre-event, during-event, and post-event motions. Explain the
audience problem the event addresses and why this event should exist beyond
general awareness.

Select metrics that test the stated objective. Set a target only when the user
or a source provides a basis. Separate leading indicators from business
outcomes. Treat attributed or influenced pipeline as influence unless causal
incrementality has been demonstrated.

### 3. Build the event narrative from canon

Use the approved SSOT as authority for category, positioning, ICP, persona
priorities, core problem, value proposition, pillars, differentiators, product
truth, and approved claims. Adapt emphasis and wording for event format,
persona, theme, and funnel stage while preserving canonical meaning.

Capture the event theme, central audience problem, core message, supporting
messages, approved proof, CTA, and relevant session, booth/demo, or executive
talking points. Do not invent new product claims or independently redefine
strategy. If the event requires a material narrative that conflicts with canon,
flag the conflict and route evidence through `ssot-context-loop`. Do not silently
change canon. A missing or stale SSOT element remains a gap, not permission to
guess.

### 4. Orchestrate activation through asset owners

The event strategy owns the brief, audience, timing, purpose, dependencies, and
handoff. The downstream skill owns the actual channel artifact. Route only the
assets the plan needs:

| Need | Owning skill |
|---|---|
| Event landing or registration page | `marketing-copy` |
| Invitations, reminders, registration nurture, no-show or attendee nurture | `email-sequence` |
| Named-account or executive outreach | `cold-email` |
| Event promotion, live coverage, clips, recap posts | `social-content` |
| AE/SDR talk tracks, meeting preparation, demo or follow-up guidance | `sales-enablement` |
| Launch is the primary motion and the event is one launch channel | `launch-strategy` |
| Tracking requirements or event measurement instrumentation | `analytics-tracking` |

Keep traceability where the project can support it:
`EVENT STRATEGY ID → SSOT VERSION → DOWNSTREAM SKILL → ASSET`. Do not rewrite
downstream channel artifacts inside this skill.

### 5. Plan segmented follow-up

Specify owner, timing, purpose, and next step for relevant groups: attended and
engaged, attended with low engagement, registered but absent, target account
met or not met, existing customer, open opportunity, and speaker, VIP, or
partner. Combine groups when their next action is genuinely the same. Route
message drafting to the channel skill that owns it. Include consent, suppression,
and sales handoff constraints supplied by the user or project.

### 6. Measure, learn, and hand off

Choose only metrics relevant to the objective. Possible leading indicators
include target accounts invited, registrations, target-account attendance,
meetings booked or completed, engagement, and qualified follow-ups. Possible
outcomes include opportunities created or accelerated, influenced pipeline,
expansion, post-event conversion, reusable content, and customer or market
learning. Define data source, owner, measurement window, and baseline/target only
where known. Separate observed outcomes from attribution claims. Record learning
and evidence that could inform future event decisions; route any proposed canon
change through the SSOT process.

## Required output: event strategy

Every plan contains these sections. Mark a section Not applicable with a reason
when the event type does not need it. Missing evidence is never a reason to omit
a section.

1. **Inputs and assumptions**: Sources and context used, with Sourced, Assumed,
   or Gap labels per `../_shared/evidence-gaps.md`.
2. **Event decision**: Why this event and why now, role, objective, audience,
   broader GTM role, expected outcomes, and major assumptions/evidence gaps.
3. **Event strategy**: Type, audience, objective, theme, offer, CTA, desired
   buyer action, sales role, and success definition.
4. **Canonical messaging inputs**: SSOT/client, canon version or mapped files,
   relevant approved elements, and any missing, stale, or conflicting inputs.
5. **Event narrative**: Core message, supporting messages, proof, CTA, and
   applicable speaker/session, booth/demo, or executive angles.
6. **Activation plan**:

   | Phase | Asset / motion | Audience | Purpose | Owning skill | Timing | Status |
   |---|---|---|---|---|---|---|

7. **Sales motion**: Before, during, and after event.
8. **Follow-up segmentation**: Segment, treatment/next action, owner, timing,
   and rationale.
9. **Measurement plan**: Leading indicators and business outcomes, with source,
   owner, window, and targets only where supported.
10. **Evidence gaps**: Ranked Assumed and Gap items using the shared format.

## Final checks

- The chosen event role and objective are explicit, and the audience is defined.
- The event thesis, offer, CTA, desired buyer action, and success criteria align.
- Narrative preserves canonical meaning; conflicts are routed to SSOT review.
- Activation and follow-up name the downstream asset owner and handoff.
- Metrics fit the objective, distinguish leading indicators from outcomes, and
  do not state influence as causal revenue.
- Claims, estimates, and audience choices carry evidence labels. No unsupported
  ROI or pipeline estimate is presented as fact.
- Every required output section is present or marked Not applicable with reason.

## Boundaries and routing

- `messaging-consistency-audit` checks event narratives and assets vertically
  against SSOT and horizontally against other market-facing assets. Route event
  strategy-level narrative conflict to `events`; route each asset correction to
  its owning channel skill.
- `output-quality-check` checks whether this event strategy meets the requirements in
  this skill. It does not check company-message alignment.
- `ssot-context-loop` owns canon review and approval. Repeated narrative conflict
  or evidence of stale canon is a review request, never an automatic edit.
- Detailed event production and logistics are outside this skill's core scope.

## Related skills

- `launch-strategy`: event as one component of a product or feature launch.
- `marketing-copy`, `email-sequence`, `cold-email`, `social-content`,
  `sales-enablement`: channel artifacts and sales execution.
- `analytics-tracking`: tracking implementation and instrumentation.
- `messaging-consistency-audit`: SSOT alignment and cross-asset narrative checks.
- `output-quality-check`: independent check against this skill's declared quality bar.
- `ssot-context-loop`: governed canon review and approval.
