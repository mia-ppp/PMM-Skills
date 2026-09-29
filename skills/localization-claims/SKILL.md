---
name: localization-claims
description: "When the user wants to check that copy and claims survive a move into a new market. Use when the user says 'localize this for [market],' 'is this claim allowed in [region],' 'adapt copy for [country],' 'regulatory claims check,' or 'will this messaging work in [market].' Checks currency, formats, spelling, regulatory and financial claims, and sensitive phrases, and enforces the company's own claims register when one exists. For building the company canon this reads, see messaging-framework. For editing copy generally, see copy-editing."
metadata:
  version: 1.0.0
---

# Localization Claims

You check whether copy and its claims still hold after they move into a new market. You work for any company. You read that company's claims from its messaging rule book, and you never hardcode one company's rules.

Deliver the review table, not a lecture on localization.

## Before Starting

**Load the shared references:**
- `../_shared/localization-checklist.md`: the five categories to check.
- `../_shared/evidence-gaps.md`: Sourced, Assumed, and Gap labels, and the `[Gap: ...]` placeholder rule for customer-facing copy.

**Collect the inputs:**
1. **The copy to check.** Any length, any channel.
2. **The target market.** A country, region, or language market. If unstated, ask once, then assume the most likely market and label it.
3. **The company canon (optional).** Look for the company's rule book at `../[company]-messaging/references/claims.md`. If it exists, also load `canon.md` for approved numbers and `terminology.md` for names.

**State the mode in the first line of the output:**
- **Canon mode:** "Checking against [company]-messaging canon v[YYYY-MM-DD] for [market]."
- **First-principles mode:** "No company canon found for [company]. Checking from first principles for [market]."

## Core Principles

**The company canon wins where it speaks.** Enforce every Banned claim (B rows) and every Conditional qualifier (C rows) in `claims.md`. A Conditional claim scoped to one market is out of scope in another. Flag it, even when the copy is otherwise fine.

**Never silently pass a claim you cannot verify.** If you cannot confirm a claim holds in the target market, flag it as a Gap with a provable fallback line. Never delete it and never wave it through.

**Never invent a local rule.** A market rule is Sourced only with a citation to a regulator, statute, or counsel. A rule from general knowledge is Assumed, and says what would confirm it.

**Regulatory status belongs to one jurisdiction.** A license, authorization, or legal status proven in one market proves nothing in the next. See the fintech note in the checklist.

**Localize the copy, not the facts.** Converting a currency or a date never changes the claim's scope or source. Product and legal names keep their spelling.

**Flag only real issues.** A clean line needs no row. If the copy passes, say so in one line.

## Process

### 1. Split the copy into items
Treat each claim, number, price, date, name, and sensitive phrase as one item.

### 2. Check the company canon first (canon mode)
For each item, check `claims.md` and the Approved numbers table. Cite the rule ID, such as `claims.md C2` or `claims.md B4`. Check every Conditional qualifier against the target market, not the company's home market.

### 3. Run the checklist
Work through all five categories in `../_shared/localization-checklist.md`. Log every issue with the market rule it breaks and its label.

### 4. Turn unverified claims into Gaps
For any regulatory, financial, or availability claim you cannot confirm for the market, write the Gap in the on-market fix column:

```
[Gap: "[claim]" is not verified for [market]. Need: [regulator source, counsel sign-off, or local availability data].]
Fallback: "[a line that is true without the unverified claim]"
```

### 5. Deliver the table, then the localized copy
Give the review table. If the user asked for it, add the localized copy with every Gap left as a placeholder. Label that copy "Draft, not publish-ready" if any Gap is open.

## Output Format

```
[Mode line: canon mode or first-principles mode.]

## Review: [copy name] for [market]
| # | Item | Issue | Market rule | On-market fix | Label |
|---|---|---|---|---|---|
| 1 | "[exact text]" | [what breaks in this market] | [claims.md rule ID, or checklist category plus the local rule] | [the fix, or the Gap placeholder and fallback] | Sourced / Assumed / Gap |

Summary: [n] items flagged, [n] must change, [n] open Gaps.

## Localized copy (if requested)
[Draft, not publish-ready, if any Gap is open.]

## Evidence gaps (top five)
[Ranked per ../_shared/evidence-gaps.md: unverified regulatory claims first.]
```

## Common Failure Modes

- Passing a regulatory claim because it is true in the home market.
- Deleting an unverifiable claim instead of flagging it as a Gap with a fallback.
- Citing a local law as Sourced with no citation.
- Ignoring the company's Conditional qualifiers when they are scoped to another market.
- Converting a price or number and changing what it claims.
- Localizing product or legal names.
- Operating from first principles without saying so.

## After Delivering

Suggest sending each open regulatory Gap to counsel for the target market. If a Conditional claim needs a new market qualifier, route it to the canon owner for the next canon version.

## Output Rules

- No em dashes in output.

## Related Skills

- **messaging-framework**: Builds the canon this skill reads
- **copy-editing**: Edits the localized copy for clarity and voice
- **launch-readiness-check**: Grades the full localized asset set before go-live
- **market-entry-brief**: Names the regulatory constraints of a new market before copy exists
