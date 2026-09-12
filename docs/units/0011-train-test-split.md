# Cell 11 — Part 5, Step 2: Data Splitting

- **C1 approved:** 2026-09-11 (Pilot approved the P-I-O-F, including three added L4 assertions, before code was prepared)
- **C2 commit:** pending — awaiting Pilot run + save

## Purpose

Split `X`/`y` into a stratified 80/20 train/test set, so evaluation later happens on genuinely
unseen data — the split this whole project's overfitting question depends on.

## Inputs

`X` (178×4), `y` (178,) — from Cell 10, alignment already proven.

## Outputs

`X_train` (~142×4), `X_test` (~36×4), `y_train` (~142,), `y_test` (~36,). Printed sample counts
and per-class breakdowns for both splits.

## Flow

1. `train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)`.
2. **L4 assertions** (added at C1): `len(X_train) + len(X_test) == len(X)` (split accounting);
   `len(X_train) == len(y_train) and len(X_test) == len(y_test)` (alignment); `set(y_train.unique())
   == set(y_test.unique()) == set(y.unique())` (stratification actually held — no class vanished
   from either split).
3. Print train/test sample counts.
4. Print per-class counts (`np.bincount`) for both splits.
5. Print the "why split data" rationale already in the template.

## Expected Result

`Training set: 142 samples`, `Testing set: 36 samples`, per-class counts in both splits roughly
proportional to the original 71/59/48 split, all three assertions passing silently, at whatever
`execution_count` follows `[7]`.

## Concept & Jargon

**Stratification** — preserving each class's proportion across both splits, so the test set isn't
accidentally missing or overloaded with one wine type. **`random_state`** — fixes the split so
it's reproducible run to run. This is the template's first explicit mention of "prevents
overfitting" — the exact concept the Learning-Curve cell later proves visually.

## Visual Sanity Check

Train + test counts must sum to 178; every one of the 3 classes must appear in *both* splits
(stratify actually worked, nothing vanished); the split proportions should visually track the
original 71/59/48 ratio, just scaled by 0.8/0.2.

## Journal Point

*Pre-written insight for the final report:* "This is the cell where 'no data leakage' stops being
an abstract worry and becomes a concrete boundary — everything trained after this point only ever
sees `X_train`/`y_train`; `X_test`/`y_test` stay untouched until evaluation. The Learning-Curve
check later in this notebook is really just a rigorous way of proving that boundary held."

## Simplified Takeaway

This cell splits the wine data into a "study set" (80%) the model learns from and a "final exam
set" (20%) it never sees until we grade it — keeping the two separate is what makes the later
evaluation actually mean something.

## Sequence Mapping

- **Where we were:** Cell 10 split `df` into `X`/`y`.
- **Where we are:** `X`/`y` split into stratified train/test sets, accounting and stratification proven.
- **Where we are going:** Cell 12 scales features (fit on train only) and trains both models.
