# Evidence gaps

Every skill loads this file and follows it. This is the single source for the rule. `AGENTS.md` only points here.

Every content-producing skill also follows `../_shared/ssot-consumption.md`. It defines
how an existing company SSOT takes precedence, which canonical files to load, and
how to preserve channel adaptation without changing strategy.

Evidence decides how an item is labeled, never whether it is included.

- **Keep every segment, claim, and opportunity that lacks proof, and label it.** Never drop one because proof is missing.
- **Never invent proof to close a gap.** No made-up stats, customers, quotes, win rates, or market sizes.
- **Turn thin proof into a validation task, not a deletion.** Name the test that would settle it.
- **Never stop for missing facts.** Proceed, state the assumption in the deliverable, and label it.

## Labels

Every claim, segment, and number carries one of three labels.

| Label | Use when | What to write |
|---|---|---|
| **Sourced** | You have a citable source: user material, research, internal data, a public source | Cite it inline |
| **Assumed** | You reasoned it from context but nothing confirms it | State the assumption and what would confirm it |
| **Gap** | No proof and no basis to assume | Name the missing proof and how to get it: beta test, interview, internal data, survey |

Examples:
- Sourced: "Chargebacks cost [segment] [x]% of GMV (source: Q3 internal chargeback report)."
- Assumed: "Marketplaces feel this pain more than SaaS, assuming higher card-not-present volume. Confirm with 5 marketplace interviews."
- Gap: "No proof that healthcare buyers switch for this. Get it from a 10-account beta."

Confidence ratings (High, Medium, Low) rate how strong a finding is, not where it came from. Keep them next to the label. A Sourced finding from one interview is Sourced, Low confidence.

## Inputs and assumptions

Every deliverable comes with a short "Inputs and assumptions" note. It records what the work rests on. Where it goes depends on who reads the deliverable.

- **Internal deliverables open with it.** Examples: GTM plans, positioning, messaging frameworks, personas, and research.
- **Customer-facing outputs get it as a separate note after the copy.** Examples: emails, landing pages, ads, and sales copy. Never put it inside the copy.

- **List the files and sources used.** Label them Sourced.
- **List each missing fact and what was assumed in its place.** Label the assumption Assumed, or Gap if nothing could stand in.
- **Keep it to one line per item.** Detail belongs in the body and the Evidence gaps section.

```
## Inputs and assumptions
| Item | What was used, missing, or assumed | Label |
|---|---|---|
| [file or source] | Used: [what it provided] | Sourced |
| [missing fact] | Missing. Assumed [assumption] in its place. | Assumed |
| [missing fact] | Missing. Nothing could stand in. [How to get it.] | Gap |
```

## Relevance cuts are not evidence cuts

- **Cut an item only for relevance, never for missing proof.** Example: a claim no buyer would care about.
- **List every relevance cut.** Put it under "Cut claims" with a one-line reason. Never delete silently.

## Customer-facing copy

- **Keep Gap claims as `[Gap: ...]` placeholders in drafts.** Never state them as fact.
- **Give every hero, headline, or key claim that depends on a Gap a provable fallback line.** Write it directly under the placeholder.
- **Label any draft with open Gaps "Draft, not publish-ready" at the top.** Never delete `[Gap: ...]` items to make a draft look finished.

```
[Gap: "Cuts fraud losses [x]% for marketplaces." Need: marketplace beta results]
Fallback: "Screens every payment before authorization."
```

## The Evidence gaps section

List every Assumed and Gap item, with no cap. Rank them so the reader sees what matters first.

- **Rank by impact on the plan's main number or lead claim.** The main number is the headline figure, such as year-one ARR or market size. The lead claim is the one the plan rests on, such as why the lead segment goes first.
- **Put the top five in the body, with why each matters.** Name what moves if the item proves wrong, such as "year-one ARR falls by about a third."
- **Put the rest in an appendix,** in the same ranked order. Together the two lists cover every Assumed and Gap item.
- **Fill Owner and Resolve by for every row.** If unknown, suggest a role and a milestone, marked `(suggested)`. A suggested owner is a stated assumption.

```
## Evidence gaps (top five)
| Rank | Item | Label | Why it matters | How to resolve | Owner | Resolve by |
|---|---|---|---|---|---|---|
| 1 | [segment, claim, or number] | Assumed / Gap | [what moves in the main number or lead claim if it is wrong] | [beta test, interview, internal data] | [role] | [date or milestone] |

## Appendix: Remaining evidence gaps
| Rank | Item | Label | Assumption or missing proof | How to resolve | Owner | Resolve by |
|---|---|---|---|---|---|---|
| 6 | ... | | | | | |
```

- **Keep the short "what most changes the answer" summary separate.** A skill's 5-bullet cap applies to that summary, never to the Evidence gaps lists.
