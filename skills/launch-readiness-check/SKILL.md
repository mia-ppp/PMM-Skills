---
name: launch-readiness-check
description: "When the user wants to grade a full set of launch assets against one company canon before go-live. Use when the user asks 'are we ready to launch' or mentions 'launch QA,' 'pre-launch audit,' 'check all our launch assets,' or 'launch readiness.' Runs the rule book's Block, Fix, and Suggest review on every asset, then returns a go/no-go scorecard with a Ready, Ready after fixes, or Not ready verdict. It is the Rung 4 gate of the launch chain. For reviewing a single piece of copy, see the company's *-messaging skill. For the launch sequence itself, see market-launch."
metadata:
  version: 1.0.0
---

# Launch Readiness Check

You are the last gate before go-live. You grade every launch asset against one company canon and return a go/no-go scorecard. One banned claim in one asset is enough to stop the launch.

Deliver the scorecard, not advice about how to review copy.

## Before Starting

**Load the shared references:**
- `../_shared/launch-stages.md`: Rung 4 entry criteria, the gate, and the handoff contract.
- `../_shared/evidence-gaps.md`: Sourced, Assumed, and Gap labels, and the rule for `[Gap: ...]` placeholders.

**Load the company canon.** Find the company's rule book at `../[company]-messaging/`. Load its `references/` in this order:
1. `canon.md`: the Approved numbers table and the canon version.
2. `claims.md`: Approved (A), Conditional (C), and Banned (B) claims, plus competitor rules.
3. `terminology.md`: product names, spelling, and voice.
4. `audiences.md`: the overlay each asset is written for.

Read the rule book's own `SKILL.md` review mode too. Its severity definitions win where they are stricter than the ones below.

**If no canon exists for the company, stop.** Write: "No canon for [company]. Build the company rule book first (Rung 2 of launch-stages.md)." Never grade against memory or a generic standard.

**Collect the asset set.** List every asset with its type (email, landing page, deck, battlecard, social, other) and its canon stamp. If the user says more assets exist than they pasted, grade what you have and list the rest as not reviewed.

## Core Principles

**One canon, every asset.** Grade every asset against the same canon version. Never mix versions in one scorecard.

**Every flag cites its rule.** Name the file and the rule ID, such as `claims.md B4` or `canon.md section 5, Customers row`. For terminology, name the file and the row, such as `terminology.md, Product names`. A flag with no rule is an opinion. Cut it.

**A Block anywhere means Not ready.** The launch verdict is only as good as the worst asset.

**Never invent flags.** A clean asset gets zero flags and the verdict Ready. Padding the table to look thorough erodes trust in the real Blocks.

**Grade the asset, not the brief.** A good reason for a claim does not make it on-canon.

## Severity

| Severity | Use for |
|---|---|
| **Block** | A Banned claim (B rows). A number that is wrong, unscoped, or not in the Approved numbers table. A Conditional claim (C rows) missing its qualifier. A regulatory or legal misstatement. Anything stated as done that is still pending. A named competitor in customer-facing copy. A `[Gap: ...]` placeholder with no fallback line. |
| **Fix** | Off-canon positioning or category. A wrong product name or spelling. Table stakes leading the message. A `[Gap: ...]` placeholder that still needs its fallback swapped in. A missing or stale canon stamp on the asset. |
| **Suggest** | Voice, emphasis, or a stronger on-canon line. |

## Process

### 1. Confirm the canon
Name the company, the rule book, and the canon version from `canon.md`. This version stamps the whole scorecard.

### 2. Review each asset
For each asset, check it line by line against `claims.md`, the Approved numbers table in `canon.md`, and `terminology.md`. Log every issue with its severity, the exact asset text, the rule broken (file and rule ID), and the on-canon fix.

Give each asset its own verdict:
- **Ready:** no Block and no Fix.
- **Ready after Fix items:** Fix items only.
- **Blocked:** one or more Block items.

### 3. Roll up
Count assets and flags by severity. Pick the top blocking issues: every Block, ordered by how many assets repeat it, then by customer exposure (web and email before internal decks).

### 4. Give the launch verdict
- **Ready:** every asset is Ready.
- **Ready after fixes:** no asset is Blocked, and at least one has Fix items. Launch once the Fix items close.
- **Not ready:** any asset is Blocked.

Write the verdict as one line and put it first.

## Output Format

The verdict comes first because the scorecard is a decision document. The "Inputs and assumptions" note follows the header, as in market-entry-brief.

```
**Verdict: [Ready / Ready after fixes / Not ready].** [One line: the count of Block and Fix items, and the deciding issue.]

Artifact: go/no-go scorecard
Rung: 4
Canon: v[YYYY-MM-DD]
Built from: [company]-messaging canon v[YYYY-MM-DD]; [n] launch assets

## Inputs and assumptions
| Item | What was used, missing, or assumed | Label |
|---|---|---|

## Rollup
| Total assets | Block | Fix | Suggest | Assets Ready | Ready after Fix items | Blocked |
|---|---|---|---|---|---|---|

## Top blocking issues
| # | Issue | Rule (file + ID) | Assets affected |
|---|---|---|---|

## Asset scorecard
| # | Asset | Type | Asset stamp | Block | Fix | Suggest | Asset verdict |
|---|---|---|---|---|---|---|---|

## Flags by asset
### [Asset name]
| # | Severity | Asset text | Rule broken (file + rule ID) | On-canon fix |
|---|---|---|---|---|
[Or one line: "No issues. Ready."]

## Not reviewed
[Assets named but not provided, or "None."]

## Evidence gaps (top five)
[Ranked per ../_shared/evidence-gaps.md: open Gap placeholders and out-of-canon claims first.]

Canon v[YYYY-MM-DD]
```

## Common Failure Modes

- A flag with no file or rule ID.
- Returning Ready after fixes when one asset has a Block.
- Grading against memory because the company canon was missing.
- Inventing Suggest flags on a clean asset.
- Restating each asset before flagging it.
- Mixing two canon versions in one scorecard.
- Leaving off the canon stamp.

## After Delivering

If the verdict is not Ready, offer to run the company rule book's review mode on the Blocked assets to draft corrected versions. Route any out-of-canon claim that should become canon to the canon owner for the next version.

## Output Rules

- No em dashes in output.

## Related Skills

- **market-launch**: Runs the launch chain this check gates
- **copy-editing**: Polishes assets after the Fix items are closed
- **sales-enablement**: Rebuilds decks and battlecards that come back Blocked
