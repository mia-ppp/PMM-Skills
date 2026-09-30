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

Common selections: outbound needs positioning, the target persona, problem/use
case, proof, and objections. Website and campaign copy needs category,
positioning, product truth, proof, and relevant personas. Social content needs
positioning, relevant persona context, evidence, and approved claims. Sales
collateral needs positioning, product truth, persona context, proof, and
objections. The manifest entry wins when it is more specific.

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
