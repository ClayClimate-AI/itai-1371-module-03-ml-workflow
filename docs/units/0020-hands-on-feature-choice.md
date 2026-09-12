# Cell 20 — Part 7: Hands-On Practice (Build Your Own Model)

- **C1 approved:** 2026-09-11 (Pilot approved the P-I-O-F, including feature choice and two added L4 assertions, before code was prepared)
- **C2 commit:** pending — awaiting Pilot run + save

## Purpose

Complete the hands-on task by building a second Logistic Regression model using `flavanoids`,
`color_intensity`, `proline` — features classically known to separate wine cultivars well — and
compare its accuracy against the main model's 4-feature default. Direct follow-up to Cell 10's
Journal Point, which flagged that the main model's features weren't the most differentiated per
Cell 8's correlation heatmap.

## Inputs

`df`, `y` (Cell 5/10), `results['Logistic Regression']` (Cell 13, `0.917`, for comparison),
`wine_data.feature_names` (for the printed list).

## Outputs

`your_features` (the 3 chosen columns, replacing the template's `['alcohol', 'color_intensity',
'proline']` default), `X_your`, `your_model` (a second, separately-trained Logistic Regression),
`your_accuracy`, printed comparison.

## Flow

1. Print the 13 available features.
2. `your_features = ['flavanoids', 'color_intensity', 'proline']` — Pilot's chosen replacement for
   the template's TODO default.
3. `X_your = df[your_features]`; stratified 80/20 split (same pattern as Cell 11).
4. **L4 assertions** (added at C1): `X_your.shape == (178, 3)`; split accounting
   (`len(X_train_your) + len(X_test_your) == len(X_your)`).
5. Scale fit-on-train-only (same pattern as Cell 12).
6. Train Logistic Regression, predict, compute accuracy.
7. **L4 assertion** (added at C1): accuracy in `[0.0, 1.0]`.
8. Print comparison against `results['Logistic Regression']` (0.917).

## Expected Result

The 13-feature list, `Your model features: ['flavanoids', 'color_intensity', 'proline']`, an
accuracy line, `Original model accuracy: 0.917`, and — likely, given these are stronger features
— the `🎉 Great job!` message, at whatever `execution_count` follows `[13]`.

## Concept & Jargon

This cell is an empirical test of Cell 10's limitation note: does a domain-informed feature choice
actually beat the simpler default? Not assumed — measured directly against the same test
methodology (stratified split, train-only scaling) as the main model.

## Visual Sanity Check

`X_your.shape` must be exactly `(178, 3)`; printed features must read `['flavanoids',
'color_intensity', 'proline']`, not the old template default.

**Corrected after running the cell:** the actual result was an exact tie — `0.917` vs. `0.917`.
The template's `if your_accuracy > results['Logistic Regression']` treats a tie as "not improved,"
so it printed `🤔 Try different features...` even though the 3-feature model matched the 4-feature
model's accuracy exactly, using one fewer input. That's not a failure to flag as a bug — it's a
real result worth stating honestly rather than letting the template's binary message imply the
attempt did worse.

## Journal Point

*Pre-written insight for the final report:* "Cell 10 flagged that the main model's 4 features
weren't the most differentiated ones available, per the correlation heatmap. This cell tests that
directly — using three features known to separate wine cultivars well and measuring whether
accuracy actually improves, rather than leaving that as a stated-but-unverified limitation."

*Updated with the actual result:* the 3-feature model tied the 4-feature model exactly at 0.917 —
matching accuracy with one fewer input, which is itself a meaningful result (fewer features doing
equally well suggests `alcohol`/`ash`/`alcalinity_of_ash` in the original set weren't adding much
signal). The template's message logic doesn't have a category for "tied," which is a small but
real gap between the code's binary framing and what actually happened.

## Simplified Takeaway

We build a second, smaller model using three specifically chosen measurements instead of the
original four, and check head-to-head whether picking better inputs actually makes the model
smarter.

## Sequence Mapping

- **Where we were:** Cell 18 covered general data-types concepts.
- **Where we are:** Test whether smarter feature choice beats the main model.
- **Where we are going:** Cell 22 — assessment quiz on ML types.
