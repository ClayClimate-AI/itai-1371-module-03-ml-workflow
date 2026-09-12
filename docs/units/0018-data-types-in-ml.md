# Cell 18 — Part 6: Understanding Different Data Types in ML

- **C1 approved:** 2026-09-11 (Pilot approved the P-I-O-F, including two added L4 assertions, before code was prepared)
- **C2 commit:** pending — awaiting Pilot run + save

## Purpose

Illustrate six data types ML works with (numerical continuous/discrete, categorical
nominal/ordinal, text, boolean) with examples and matching use cases. Purely conceptual — first
cell since the imports that doesn't touch `df`, `X`, `y`, or the models.

## Inputs

None — self-contained literal data.

## Outputs

Printed block per data type (name, example values, matching use case), plus a closing
key-insight line.

## Flow

1. Define `data_examples` (6 categories, each with 5 example values).
2. **L4 assertions** (added at C1): every category name matches one of the known use-case tags
   (`Continuous`, `Discrete`, `Nominal`, `Ordinal`, `Text`, `Boolean`); exactly 6 categories exist.
3. For each category, print its name and examples, then print a matching use-case line via
   substring match (`'Continuous' in data_type`, etc.).
4. Print the closing insight line.

## Expected Result

Six printed blocks, each with a non-empty `Use case:` line, ending in the `💡 Key Insight` line —
no exceptions, at whatever `execution_count` follows `[12]`.

## Concept & Jargon

Different ML data types need different handling — categorical data needs encoding, text needs
vectorization, numerical data usually doesn't need either. This cell is the map of that landscape
before the notebook moves on.

## Visual Sanity Check

Every one of the 6 printed blocks must show a real use-case sentence, not a blank line after
"Use case:" — provable via the coverage assertion above rather than eyeballed.

## Journal Point

*Pre-written insight for the final report:* "Not every unit needs to touch real data — this one is
pure conceptual scaffolding. But even a static, illustrative cell benefits from an integrity
check: proving no category silently falls through the branching, rather than assuming six
hand-written examples are self-evidently complete."

## Simplified Takeaway

This cell just shows six different kinds of information a computer might work with — numbers,
categories, text, yes/no — and what kind of ML problem each one is normally used for.

## Sequence Mapping

- **Where we were:** The Learning-Curve cell proved neither model overfit.
- **Where we are:** Stepping back from the wine project to the general concept of data types.
- **Where we are going:** Cell 20 — hands-on practice, picking your own features.
