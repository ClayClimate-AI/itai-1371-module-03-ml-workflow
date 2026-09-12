# Cell 5 — Part 3: Load the Wine Dataset (+ L4 Integrity Assertion)

> **Retroactive record.** Written 2026-09-11 per ADR 0005 Amendment 2, after the code was already
> committed and Pilot-verified. Normal C1 order is P-I-O-F *before* code — this file reconstructs
> that plan from what was actually built, so the enrichment chain (Sequence Mapping, Journal
> Point) has a real starting point instead of beginning at Cell 6.

- **C1 approved:** 2026-09-11 10:57 (original, pre-ADR-0005 approval — Purpose/Inputs/Outputs/Flow
  only; this file adds the six ADR 0005 fields retroactively)
- **C2 commit:** `bc48cb3` (code); execution proof re-saved in `265c779`

## Purpose

Load the raw Wine dataset, shape it into a DataFrame usable by the rest of the notebook, and
prove — before any downstream cell touches it — that it actually is the dataset the whole project
is built around (178 samples, 13 features, 3 classes, no nulls).

## Inputs

- `load_wine` and `pd` — bound in Cell 3. If Cell 3 hasn't run, this cell raises `NameError` (the
  exact failure this project already hit once — `progress.md` 05:27).

## Outputs

- `wine_data` — the raw `sklearn.utils.Bunch` returned by `load_wine()`.
- `df` — a 178×15 DataFrame: the 13 chemical feature columns plus `wine_class` (integer 0/1/2) and
  `wine_class_name` (string label).
- A printed integrity-check confirmation, dataset shape/feature/class summary, and `df.head()`.

## Flow

1. Call `load_wine()` to get the raw Bunch.
2. Build `df` from `wine_data.data` with `wine_data.feature_names` as columns.
3. Add two label columns: `wine_class` (raw integer target) and `wine_class_name` (mapped via
   `wine_data.target_names`).
4. L4 assertions, in order: raw data shape is exactly `(178, 13)`; there are exactly 3 target
   classes; the 13 feature columns of `df` contain zero nulls.
5. Print the integrity-check confirmation, then shape/feature-count/class-name summary and
   `df.head()`.

## Expected Result

`✅ Data integrity check passed — 178×13, 3 classes, 0 nulls.` printed, followed by
`Shape: (178, 15)` (13 features + 2 label columns), `Features: 13`, `Classes: ['class_0' 'class_1'
'class_2']`, and a 5-row preview table ending in `proline`, `wine_class`, `wine_class_name` — all
visible in the actual output at `execution_count: 4`.

## Concept & Jargon

**Data integrity assertion (Layer 4)**: verifying a freshly-loaded dataset matches its documented
shape/label-count/completeness *before* any transformation is applied to it, so a corrupted or
unexpectedly-different data source fails immediately and loudly rather than producing silently
wrong results three cells later.

- **Bunch**: scikit-learn's dict-like container for toy datasets (`.data`, `.target`,
  `.feature_names`, `.target_names`).
- **Target vs. feature**: `wine_class`/`wine_class_name` are the label to predict; the 13 chemical
  measurements are the features used to predict it.
- **Null check**: `df[...].isnull().sum().sum() == 0` — confirms no missing values snuck in during
  the Bunch-to-DataFrame conversion.

## Visual Sanity Check

Two independent things must both be true, not just plausible-looking: (1) the printed shape line
says `Shape: (178, 15)` — 13 features + 2 label columns, not 13 (a common off-by-two mistake if
someone later forgets the label columns were added); (2) `df.head()`'s `wine_class`/
`wine_class_name` pairs are internally consistent (e.g., every row showing `wine_class: 0` also
shows `wine_class_name: class_0`) — proving the `target_names` mapping in the list comprehension
lined up correctly rather than silently mis-indexing.

## Journal Point

*Pre-written insight for the final report:* "Adding the integrity assertions here felt like
overkill for a clean, well-known toy dataset — `load_wine` isn't going to return corrupted data.
But the value isn't really about this dataset; it's about building the habit of asserting shape
and nullity right after every load, so the same code pattern catches a real problem the day the
data source isn't a trusted scikit-learn toy dataset anymore."

## Simplified Takeaway

This cell pulls in the wine data, turns it into a table we can actually work with, and checks the
table looks the way we expect (right number of wines, right number of measurements, no blanks)
before we do anything else with it.

## Sequence Mapping

- **Where we were:** Cell 3 imported every library and verified they bound correctly, including
  `load_wine` itself.
- **Where we are:** The Wine dataset is loaded, shaped into `df`, and proven to match its expected
  178×13/3-class/0-null profile.
- **Where we are going:** Cell 6 explores `df`'s structure in more depth — sample/feature/class
  counts and distribution — building directly on `df` as constructed here.
