# Cell 10 — Part 5, Step 1: Data Preparation (Select X and y)

- **C1 approved:** 2026-09-11 (Pilot approved the P-I-O-F, including three added L4 assertions, before code was prepared)
- **C2 commit:** pending — awaiting Pilot run + save

## Purpose

Split `df` into the feature matrix `X` (the inputs a model will learn from) and target vector `y`
(the answer key) — the first cell in the actual ML workflow section; everything before this was
loading/exploring.

## Inputs

`df` (Cells 5/6/8 — loaded, integrity-checked, explored: 178×15).

## Outputs

`X` — a 178×4 DataFrame (`alcohol`, `malic_acid`, `ash`, `alcalinity_of_ash` — the template
deliberately uses 4 of the 13 features "for simplicity"). `y` — a 178-length Series (`wine_class`,
integer labels). Printed shapes and a 5-row preview of `X`.

## Flow

1. Define `feature_names` (the 4 chosen columns).
2. `X = df[feature_names]`, `y = df['wine_class']`.
3. **L4 assertions** (added at C1): `X.shape == (178, 4)`; `y.shape == (178,)`;
   `list(X.index) == list(y.index)` — a `check_alignment` assertion (per the guardrail-ladder
   naming in `checkpoints.md`) proving `X` and `y` stay in the same row order before anything
   downstream uses them.
4. Print the feature list and both shapes.
5. Print `X.head()`.

## Expected Result

Printed feature list, `Feature matrix shape: (178, 4)`, `Target vector shape: (178,)`, and a 5-row
table of the 4 selected columns — no exception, at whatever `execution_count` follows `[6]`.

## Concept & Jargon

**Feature matrix (X) vs. target vector (y)** — the fundamental input/output split for supervised
learning. **Feature selection** — choosing a subset of available columns as model inputs; here, 4
of the dataset's 13 features, trading signal for simplicity/interpretability.

## Visual Sanity Check

The printed `X.head()` column headers must exactly match `feature_names`, and `X`/`y` must come
from the same `df` in the same row order — confirmed by the alignment assertion above, not just
assumed.

## Journal Point

*Pre-written insight for the final report:* "Using only 4 of the 13 available features was a
deliberate simplicity trade-off in the template, not something I chose — worth noting as a
limitation, since the correlation heatmap in Cell 8 already showed these 4 aren't the most
differentiated set available."

## Simplified Takeaway

This cell pulls out the four measurements we'll actually use to guess a wine's type, and
separates them from the "answer key" (the true wine type) — that split is what every model
training step from here on builds on.

## Sequence Mapping

- **Where we were:** Cell 8 visualized class balance and feature correlations.
- **Where we are:** `df` officially split into inputs `X` and answer `y`, alignment proven.
- **Where we are going:** Cell 11 splits `X`/`y` into train/test sets.
