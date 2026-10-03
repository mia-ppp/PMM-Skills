# SSOT consumption contract

This contract applies to every skill that creates, edits, plans, or approves
customer-facing or go-to-market content. It works with `ssot-context-loop`; it
does not replace its file model, commands, evidence tags, or approval gates.

## Find and load the active canon

1. Identify the active client or project from the user's request and supplied
   assets. Do not combine two clients' SSOTs.
2. Look for the project-root `manifest.yaml`, then inspect its `agents` entry for
   this skill's `name`. Paths are relative to `ssot/<client-slug>/` as defined by
   `ssot-context-loop/references/ssot-spec.md`.
3. Read every mapped file that exists. Check `state.md` for stale or contested
   sections and follow relevant `anti-patterns`, evidence tags, and pending
   validations. Treat missing mapped files as gaps. Do not invent replacements.
4. When the skill has no manifest entry, load the smallest relevant set from the
   real schema below. Note this fallback in Inputs and assumptions. Do not load
   unrelated SSOT files.
5. If no applicable SSOT exists, use `.agents/product-marketing-context.md` (or
   its legacy `.claude/` location) as provisional bootstrap context when present.
   It is not governed canon. Label uncertainty under the existing evidence-gap
   rules, and ask for missing task-critical facts as the skill normally would.

An SSOT is authoritative for claims it covers. Where a company rule book or
claims register also exists, follow the stricter applicable factual or legal
restriction and flag a conflict for review instead of choosing silently.

## Select only relevant SSOT files

| Needed context | SSOT files to read |
|---|---|
| Category and product definition | `core/00-what-it-is.md` |
| Positioning, value proposition, messaging pillars, differentiators, deprecated frames | `core/01-how-you-position-it.md` |
| Capabilities, integrations, shipped/not shipped, allowed roadmap claims | `core/02-product.md` |
| ICP, personas, buying committee, persona priorities and messaging | `core/03-who-it-is-for.md`, plus `living/04-icp-signals.md` when field fit matters |
| Use cases and customer-described outcomes | `living/05-use-cases.md` |
| Evidence, proof, metrics, testimonials, approved claims | `living/07-evidence.md` |
| Objections and supported responses | `living/08-objection-handling.md` |
| Competitive context | `living/06-competitive.md` only when the task needs it |
| Approved strategic changes or impacted assets | relevant `decisions/*.md`; use `09-iteration.md` for recorded drift lessons when relevant |
| Goals, accepted market/segment choice, pricing/packaging, sales motion, journey decisions, ongoing GTM | applicable scoped approved `decisions/*.md` records or exact-version references governed by SSOT |

Common selections: outbound needs positioning, the target persona, problem/use
case, proof, and objections. Website and campaign copy needs category,
positioning, product truth, proof, and relevant personas. Social content needs
positioning, relevant persona context, evidence, and approved claims. Sales
collateral needs positioning, product truth, persona context, proof, and
objections. The manifest entry wins when it is more specific.

## Context readiness before consequential decisions

Read `../_shared/context-establishment.md` when context is being established or
task-critical intelligence is incomplete, stale or conflicting. Reuse the PMC
workspace readiness/handoff when present, checking goal, scope and source version.
For each relevant requirement preserve support, authority and health separately.
Do not infer approval from existence, citations, freshness or evidence sufficiency.

Use PROCEED, PROCEED PROVISIONALLY or HOLD THIS DECISION with the shared meanings.
Record provisional assumptions, understood risks, permitted scope and validation
triggers. A hold names the affected decision, GAP, owner and closure criteria;
continue independent work. Missing approval remains a separate dependency.
Research/exploratory hypotheses do not require approved personas or markets.
Existing execution and launch approval gates remain mandatory.

Covered canon stays authoritative even when stale or challenged; do not invent a
replacement or state a suspect claim as freshly validated. Flag the review and
hold the affected unsupported claim where necessary. Bootstrap findings can fill
uncovered provisional context, never override covered canon or become approved
through reuse. Route establishment/integration to product-marketing-context and
domain gaps to its existing owner table; execution owners do not rebuild context.

For approved decision references, verify topic, product/segment/region scope,
effective date, approval, explicit supersession and the exact approved source
version. A mutable external link or the newest decision filename is insufficient.
If a manifest omits task-critical context, load the relevant approved record and
report the mapping gap. State summaries are indexes, not an alternative canon.
Handoffs preserve source/finding IDs, labels, authority, health and unresolved
gaps; the receiver narrows context without upgrading or reinterpreting it silently.

## Persona intelligence consumption and reuse

Apply this contract when audience intelligence materially affects strategy,
GTM, execution or review. Pure technical, statistical, instrumentation,
configuration, hygiene, formatting and other non-audience work is exempt.
No persona lookup or audience brief is needed merely to satisfy this contract.

### Reuse the full source, select relevant intelligence

Prefer the relevant approved full persona in `core/03-who-it-is-for.md` or
an explicitly approved project reference. Load omitted task-critical context
and report a manifest mapping gap. Suitable provisional profiles may support
bounded work under the existing readiness rules, without overriding covered canon.
Downstream owners may load the source directly; no persona-skill rerun is needed.

Keep access to the full attribute profile, committee model and relevant evidence.
A role summary or message map alone is insufficient when material detail is lost.
A concise task selection may reference the full source; it never replaces it.
Preserve source/section, available version or review date, actual approval status,
attribute evidence labels, confidence, limitations and material uncertainty.
Record missing metadata without inventing it. Missing nonessential metadata alone
is not a reason to hold work; unavailable essential provenance remains explicit.

Select the relevant role, job, pains, stakes, current behavior, criteria,
objections, proof requirements, language and other supported intelligence.
Include stage, trigger, situation or account facts only when the task needs them.
Do not infer a specific prospect's situation from a general persona pattern.
Separate required buyer proof from evidence the company actually has.

Reuse an originating brief when suitable, checking scope and source status.
Use existing artifacts, annotations or short notes; no fixed table, separate
brief or exhaustive attribute coverage is required. Do not ask questions already
answered by the persona or regenerate/rescore it for a downstream task.

### Apply intelligence within existing ownership

`icp-and-buyer-personas` owns reusable profiles and proposed revisions.
Research/intelligence owners supply evidence; `product-marketing-context` integrates
cross-domain findings, gaps and readiness. `ssot-context-loop` owns approval
and canonical persistence. Downstream strategy, GTM and execution owners make
or propose their own decisions and produce their own outputs.

Use relevant intelligence to determine material choices, such as argument,
value emphasis, proof, objections, detail, CTA, motion or channel. Channel defaults
are candidates, not substitutes for buyer understanding. Link interpretations
and proposals to their supporting intelligence; they are not new persona facts.
Reuse does not freeze future strategy, move decisions to the persona skill,
or authorize changes to approved canon.

### Preserve uncertainty and handle conflicts

- **Reuse without promotion:** provisional profiles keep their actual evidence
  and approval status. Repeated reuse never upgrades an assumption or grants approval.
- **Preserve covered canon:** supplement only uncovered context where permitted.
  Contradictory evidence is a review item for the domain owner and SSOT;
  never silently replace an approved persona or choose a competing profile.
- **Assess missing intelligence:** ask only unresolved questions that materially
  change the task. Proceed provisionally with assumption, risk, scope and validation
  trigger when defensible; otherwise hold only the affected choice.
- **Separate approval:** absent persona approval is a dependency only where the
  intended action or an existing gate requires it. Exploration does not require
  approved personas. Provisional drafting never grants launch clearance.
- **Route generation and revisions:** necessary reusable profile work belongs to
  `icp-and-buyer-personas`, with evidence from research owners. Execution owners
  do not invent missing persona facts, quotes or approvals, or write canon.

### Handoffs and meaningful application review

Carry the full-source reference, actual evidence/approval status, task-relevant
intelligence and material gaps through audience-dependent handoffs. Preserve
available versions and source/finding IDs. The receiver may narrow the selection
but must retain access to the rich source and must not silently alter its meaning.
Orchestration owners pass context; asset owners produce assets.

Make material choices traceable to supported or explicitly assumed intelligence
in the existing artifact or concise internal review notes. No prescribed table
or attribute count is required. Keep notes separate from customer-facing copy.

`output-quality-check` inspects meaningful application against the originating
skill and this applicable contract. Title/tone changes alone do not establish
application when material buyer needs differ. Shared treatment is valid when
relevant evidence supports shared needs; do not manufacture persona differences.
Do not fail an output merely for omitting irrelevant attributes, an optional
brief/table, or nonessential metadata. Unavailable essential evidence is
UNVERIFIABLE, not a claimed pass. Route actual failures to the originating owner.
`messaging-consistency-audit` separately evaluates alignment with approved canon.

## Keep strategy and expression separate

- **Canonical message** is the approved strategic meaning in the SSOT.
- **Approved/contextual variation** changes wording, emphasis, detail, or format
  for a channel, persona, funnel stage, or audience while preserving that meaning.
- **Messaging drift** changes, weakens, genericizes, or materially reframes an
  approved SSOT element. A difference in wording alone is not drift.

The SSOT owns what the company says. The channel skill owns how to express it.
No downstream skill may independently redefine category, positioning, ICP,
persona priorities, core problem, value proposition, messaging pillars,
differentiators, product capabilities, approved proof, objections, or approved
strategic decisions. If source materials conflict or suggest canon is outdated,
surface the conflict as a review item. Do not settle it by choosing the newest,
most repeated, or most persuasive wording.

Claims must remain traceable to the SSOT and approved evidence. Preserve `[C]`,
`[A]`, and `[G]` meaning. A gap stays a gap with the fallback required by
`../_shared/evidence-gaps.md`; do not upgrade it because a draft sounds confident.

## Write, route, and approve safely

Skills may adapt a message and propose asset corrections. They must not write to
canonical SSOT files, decisions, or `state.md`. Only `ssot-context-loop` manages
those through its signal, evidence, and human approval gates. Human approval
remains mandatory for any change to canonical positioning or messaging.

When outputting an asset, record the SSOT files used in Inputs and assumptions.
If an asset appears inconsistent with canon, explain the mismatch and offer a
channel-appropriate correction. Route suspected canon problems to
`ssot-context-loop` for review, not direct editing.
