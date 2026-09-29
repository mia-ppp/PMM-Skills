---
name: case-deck-builder
description: "Turn a finished PMM research document into a sparse, evidence-tagged presentation for a take-home assignment. Use when the user asks to build a case deck, take-home presentation, or research-to-slides deck. Requires the assignment prompt and source research document before starting."
metadata:
  version: 1.0.0
---

# Case Deck Builder

Turn finished research from PMM agents into a concise presentation that answers a specific take-home assignment. The assignment prompt controls the structure and requested main-slide count.

## Required Inputs

Before starting a deck run, confirm that you have both inputs:

1. **Assignment prompt:** required. It determines the requested slide count, company, and sections.
2. **Finished source document:** a Google Doc exported as Markdown or DOCX, or a Drive link when a Google Drive MCP is connected.

If either is missing, ask for the missing input and wait. If the user gives a Drive link but no Drive MCP is connected, ask them to export the document as Markdown or DOCX. Do not begin the outline without both inputs.

Read the entire source document, including tables, footnotes, and citations. Preserve its source relationships and labels. Never invent a fact, number, or source.

## Workflow

1. Parse the prompt. List every requested part, exact main-slide count if stated, and named sections such as approach, 30-60-90, or go-to-market.
2. Map every major part to one main slide. Follow the prompt's order. Merge related parts when needed. Never exceed the requested count.
3. If no count is stated, choose the fewest slides that answer every part and state the assumption in the outline.
4. Choose an anchor slide: approach, summary, or both, based on what the prompt asks.
5. For every slide, select one claim, the numbers that prove it, and the strongest proof point. Put remaining useful evidence in the appendix if it fits. Put all other source material in the cut log with a one-line reason.
6. Tag every factual claim and number as Cited, Assumed, or Gap using the Source Tagging rules below.
7. Build an appendix within its cap. The appendix does not count toward the requested main-slide count.
8. Write `output/<company>/deck-outline.md` and `cut-log.md`. Stop and wait for the user's approval or edits. Do not build a PowerPoint before approval.
9. After approval, convert the approved outline to the JSON input described below and run `scripts/build_deck.js`. Render the deck to images, inspect every slide for overflow and overlap, fix issues, and deliver the `.pptx` and cut log.

## Slide Rules

- Headlines state a claim, never a topic. For example: "Finance rebuilds what Sales already sold," not "Positioning."
- Give approach at most one slide, and only when the prompt asks how the candidate works.
- End every main slide with a one-line key insight that states the so-what.
- Use tables by default for dense information. Keep tables near five columns by six rows. Move overflow to the appendix.
- Highlight the recommended option in every comparison table.
- Keep hedges, postscript notes, URLs, and abbreviations off slides. Put them in the appendix or cut log. The abbreviations "imp," "comp," and "resp" are prohibited on slides.
- Give every slide an eyebrow in the format `NN  SECTION  ·  COMPANY`. For appendix slides use `A1  APPENDIX  ·  COMPANY`, incrementing the appendix number. Verify the company name against the assignment prompt.
- Never add speaker notes.
- Do not add generic process slides reused across assignments. Every slide must answer this assignment.
- Use no em dashes. Keep sentences to two lines at most.

## Source Tagging

Carry the agents' source structure into the slide content and appendix:

- **Cited:** numbered superscripts `¹`, `²`, `³`, mapped to rows in the Sources table.
- **Assumed:** `ᴬ` plus a number, such as `ᴬ¹`, mapped to the Assumptions table.
- **Gap:** `ᴳ` plus a number, such as `ᴳ¹`, mapped to the Gaps table.

Assign stable numbers within each tag type. A superscript on a slide must resolve to exactly one appendix row, and every appendix row must be cited on at least one slide. If a required claim has no support in the source, include it as a Gap and name what would close it. Do not drop assignment requirements because evidence is missing.

## Appendix Rules

- Cap appendix slides at half the main-slide count, rounded down. For example, eight main slides allow four appendix slides and four main slides allow two.
- Label appendix slides A1, A2, A3, and so on.
- Compress references into tables, never lists:
  - Sources: `# | Source | Claim it supports | Slide`
  - Assumptions: `# | Assumption | Reasoning | Slide`
  - Gaps: `# | Gap | What would close it | Slide`
- Supporting data such as segment math or full competitor tables may go in the appendix within its cap.

## Output Files

Save all files to `output/<company>/`:

- `deck-outline.md`: all main and appendix slides, each with eyebrow, claim headline, content, key insight, and source tags.
- `<company>-deck.pptx`: build only after the user approves the outline.
- `cut-log.md`: every source item not used on a slide or in the appendix, with one line explaining why. Do not include the cut log in the deck.

## Outline Format

Start the outline with the assignment mapping: every part of the ask, the exact requested main-slide count or the fewest-slide assumption, and its assigned slide. Then use this format for each slide:

```markdown
## Slide 1
- Eyebrow: 01  SECTION  ·  COMPANY
- Headline: [A claim that answers the assignment]
- Subline: [Optional, one line]
- Content: [Table, concise bullets, or a three-step visual, including source tags]
- Key insight: [One-line so-what]
- Tags: [All source tag references on this slide]
```

Repeat for each main slide. Outline appendix slides with the same fields and A-numbered eyebrows. Include the exact Sources, Assumptions, and Gaps tables in the appendix outline.

## Building the PowerPoint

Build only after the outline is approved. Use `scripts/build_deck.js`, which requires `pptxgenjs` to be available to Node.js. The script accepts a JSON file and an output `.pptx` path:

```bash
node scripts/build_deck.js deck-data.json output/<company>/<company>-deck.pptx
```

The JSON structure is:

```json
{
  "company": "Company",
  "requiredMainSlides": 1,
  "slides": [
    {
      "eyebrow": "01  SECTION  ·  COMPANY",
      "headline": "A claim headline",
      "subline": "Optional one-line context",
      "type": "table",
      "columns": ["Column one", "Column two"],
      "rows": [["Entry", "Evidence¹"]],
      "highlightRow": 0,
      "keyInsight": "The so-what in one line.",
      "appendix": false
    }
  ]
}
```

Use `type: "steps"` with a `steps` array for a three-step visual. Mark appendix slides with `appendix: true`; use A-numbered eyebrows. The deck builder does not author or infer content. It lays out the approved outline as supplied.

## QA Checklist

- Main-slide count matches the prompt exactly. Appendix is within its cap.
- Every assignment requirement maps to at least one main slide.
- Every superscript resolves to one appendix row, and every appendix row is referenced.
- No topic headlines, slide abbreviations, hedges, URLs, em dashes, or speaker notes appear.
- Company name is correct in every eyebrow.
- Render slides to images and inspect for text overflow and overlap.

## Related Skills

- **sales-enablement**: create sales decks and collateral for active sales conversations.
- **customer-research**: conduct or synthesize customer research before a source document is ready.
