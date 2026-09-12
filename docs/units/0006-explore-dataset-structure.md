# Cell 6 — Part 3: Explore Dataset Structure

- **C1 approved:** 2026-09-11 (Pilot approved the P-I-O-F, including the added L4 assertion, before code was prepared)
- **C2 commit:** pending — awaiting Pilot run + save

## Purpose

Characterize `df`'s structure — sample count, feature count, class labels, class balance, and
missing-value status — as the first exploratory pass before any transformation happens.

## Inputs

`df` (built in Cell 5: 178×15, 3 classes, integrity-checked).

## Outputs

Printed summary (sample/feature counts, unique classes, class distribution, missing-value count).
No new variables — this is read-only exploration.

## Flow

1. Print total samples (`len(df)`) and feature count (`len(df.columns) - 2`, excluding the two
   label columns).
2. Print unique class names and their value counts (`value_counts()`), to check for class
   imbalance.
3. **L4 assertion** (added at C1, not in the original template): `assert
   df.isnull().sum().sum() == 0` — proves the "no missing values" claim instead of just printing
   it, the same gap ADR 0005 was created to close.
4. Print total missing-value count and the confirmation line.

## Expected Result

Printed block ending in `Missing values: 0` / `✅ No missing values - this is a clean dataset!`,
now backed by an assertion rather than just printed, at whatever `execution_count` follows `[4]`.

## Concept & Jargon

**Class balance** — whether the 3 wine classes have roughly equal counts (imbalance affects which
metrics matter later, e.g. accuracy vs. per-class recall). **Class distribution** — the count per
label, here via `value_counts()`.

## Visual Sanity Check

The three `value_counts()` numbers must sum to 178 (matches Cell 5's shape check) — a mismatch
would mean the `wine_class_name` mapping broke somewhere between Cell 5 and here.

## Journal Point

*Pre-written insight for the final report:* "This cell is where 'no missing values' stopped being
something I just read off a print statement and became something the code actually proves before
claiming it — the same fix this project made to its own audit trail, applied to the notebook
itself."

## Simplified Takeaway

This cell counts how many wines we have, how many measurements per wine, how many of each type,
and actually proves nothing is missing — not just states it — before we do any real math on the
data.

## Sequence Mapping

- **Where we were:** Cell 5 loaded and integrity-checked `df` (178×13/3-class/0-null).
- **Where we are:** Structural/class overview of `df`, now with a proven missing-value check.
- **Where we are going:** Part 4 EDA (Cell 8) — visualizing the class distribution and feature
  correlations.
