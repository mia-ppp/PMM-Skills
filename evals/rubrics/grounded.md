# Grounded

**Question:** Does the output stay true to the provided context and avoid inventing facts?

## Great (2)
- Uses specific details from the prompt or input files.
- States assumptions openly when information is missing, or asks for it.
- Every number, customer, or claim traces to the input or is labeled as an estimate.

## OK (1)
- Uses the context, but parts of the advice would fit any company.
- Fills gaps with reasonable defaults without flagging them as assumptions.

## Bad (0)
- Invents stats, benchmarks, customers, quotes, or case studies and presents them as fact.
- Ignores or contradicts key details the user gave.
- Answers as if it read a URL or file it could not access.

## Edge cases
- Unsourced benchmark stated as fact ("average SaaS conversion is 2.35%"): Bad.
- Clearly marked placeholders ("[customer name]", "[X]% lift"): fine.
- A clarifying question plus a provisional answer: can still be Great.

## Anchors
_Fill after hand-grading._

| Tier | Sample ID | Skill | Excerpt | Why |
|---|---|---|---|---|
| Great | | | | |
| OK | | | | |
| Bad | | | | |
