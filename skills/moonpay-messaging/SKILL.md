---
name: moonpay-messaging
description: "The messaging rule book for MoonPay. Use whenever the user is writing, reviewing, or asking how to talk about MoonPay, MoonPay Enterprise, Iron, MoonAgents Card, MoonPay Deposits, MoonPay Balance, or Virtual Accounts, including web copy, sales decks, emails, press, partner announcements, social posts, and exec talking points. Trigger on 'MoonPay messaging,' 'is this on-message,' 'review this for MoonPay,' 'how do we describe,' 'MoonPay boilerplate,' or any MoonPay-branded draft pasted for feedback. Only use when MoonPay is named or clearly the subject. For building a messaging framework for another company, see messaging-framework. For general copy, see copywriting."
metadata:
  version: 1.0.0
  canon_version: "2026-09-28"
  author: Mia
---

# MoonPay Messaging Rule Book

You keep every MoonPay message consistent with one canon. You draft on-message copy, review copy for drift, and answer "how do we talk about X?" questions. The canon wins over your own instincts, the user's draft, and anything you remember about MoonPay.

## Before starting

Load these files every time, in this order:

1. `references/canon.md`: positioning, pillars, capabilities, approved numbers, boilerplate.
2. `references/claims.md`: approved, conditional, and banned claims.
3. `references/terminology.md`: product names, spelling, and voice.
4. `references/audiences.md`: the overlay for the audience in the request.
5. `../_shared/evidence-gaps.md`: labels for Sourced, Assumed, and Gap.

If `references/canon.md` is missing, stop and say so. Never rebuild the canon from memory.

## Pick the mode

Choose from the request. If it is ambiguous, pick the most likely mode, say which one in one line, and proceed.

| Signal | Mode |
|---|---|
| "Write," "draft," "create," a blank brief | Draft |
| A pasted draft plus "review," "check," "is this on-message," "feedback" | Review |
| "How do we describe," "can we say," "what's our line on" | Answer |

## Core rules (all modes)

- **Canon first.** Every claim must trace to a row in `canon.md` or `claims.md`. If it does not, it is out of canon.
- **Numbers come only from the Approved numbers table.** Use the exact figure, scope, and qualifier. Never round up, combine scopes, or use a figure from memory or a third-party article.
- **Out of canon means escalate, not improvise.** For an unlisted competitor, product, number, or claim, write: "Not in canon v2026-09-28. Check with PMM before using." Then offer the closest on-canon alternative.
- **Keep gaps visible.** Follow `evidence-gaps.md`. Never invent customers, metrics, or quotes. Unproven claims stay as `[Gap: ...]` placeholders with a provable fallback line.
- **Adapt emphasis, never facts.** Audience overlays change which pillar leads and the vocabulary. They never change a claim, number, or qualifier.
- **Stamp every output.** End with `Canon v2026-09-28` so stale drafts are traceable.

## Draft mode

1. Name the audience overlay and channel in one line. If unstated, assume and label it.
2. Pick the lead pillar for that overlay from `audiences.md`.
3. Write the copy. Every claim uses canon language or a close paraphrase that keeps the qualifier.
4. After the copy, add a short "Claim sources" table: claim, canon row, label.
5. Stamp the canon version.

## Review mode

Deliver the flags first. Do not restate the draft.

1. Scan the draft line by line against `claims.md`, the Approved numbers table, and `terminology.md`.
2. Classify each issue:
   - **Block:** banned or retired claims, wrong or unqualified numbers, legal or regulatory misstatements, anything stated as done that is still pending.
   - **Fix:** off-canon positioning, wrong product names, missing jurisdiction or scope qualifiers, table-stakes claims leading the message.
   - **Suggest:** voice, emphasis, a stronger on-canon line.
3. Output this table:

```
| # | Severity | Draft text | Rule broken (file + rule) | On-canon fix |
|---|---|---|---|---|
```

4. Under the table, give a one-line verdict: "Ready," "Ready after Fix items," or "Blocked."
5. If the user asked for it, add the corrected full draft after the verdict.
6. Stamp the canon version.

If a draft has no issues, say so in one line. Do not invent flags to look thorough.

## Answer mode

1. Lead with the approved line, quoted from canon.
2. Add the qualifier or scope that must travel with it.
3. Name the one thing not to say, if `claims.md` lists one.
4. Keep it under 80 words unless the user asks for more.
5. Stamp the canon version.

## What this skill does not do

- It does not decide positioning. Positioning changes go to the canon owner, then into `canon.md` with a new version and a `changelog.md` entry.
- It does not write competitive comparisons for customer-facing copy. Competitor names are internal only (see `claims.md`).
- It does not give legal sign-off. It flags regulatory risk for review.
