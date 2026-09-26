# Rubrics

Four dimensions grade every skill output. Each is scored Great (2), OK (1), or Bad (0).

| Dimension | Question it answers |
|---|---|
| [Grounded](grounded.md) | Does it stay true to the input and avoid inventing facts? |
| [Decisive](decisive.md) | Does it make a call, or hand the decision back? |
| [Usable](usable.md) | Could a senior PMM act on it with light edits? |
| [Sharp](sharp.md) | Does it say something general best practice would not? |

## Grading rules

- **Score each dimension on its own.** A grounded answer can still be indecisive.
- **When torn between two tiers, pick the lower one.** This keeps scores conservative and repeatable.
- **Write a one-line reason for every score.** Quote the output where possible.
- **Length is not quality.** Do not reward long answers for covering more ground.
- **Grade the output, not the prompt.** A vague prompt does not excuse a vague answer.

## Anchors

Each rubric file ends with empty anchor slots. Fill them after hand-grading, using outputs from the first 20 calibration samples only. Pull anchors from different skills where possible.
