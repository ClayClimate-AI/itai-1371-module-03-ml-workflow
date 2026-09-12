# Cell 12 — Part 5, Step 3: Model Training

- **C1 approved:** 2026-09-11 (Pilot approved the P-I-O-F, including three added L4 assertions, before code was prepared)
- **C2 commit:** pending — awaiting Pilot run + save

## Purpose

Standardize features — fit only on training data, to prevent leakage — then train two classifiers
(Logistic Regression, Decision Tree) on the training set. First cell that actually produces a
trained model.

## Inputs

`X_train`/`X_test` (142×4 / 36×4), `y_train` (142,) — from Cell 11, stratification already proven.

## Outputs

`scaler` (fitted `StandardScaler`), `X_train_scaled`/`X_test_scaled`, `trained_models` dict holding
both fitted classifiers.

## Flow

1. `scaler.fit_transform(X_train)` — mean/std computed from train only.
2. `scaler.transform(X_test)` — same transform applied, **not** refit; this is the single line
   where leakage would happen if it were `fit_transform` instead.
3. **L4 assertions** (added at C1): `abs(X_train_scaled.mean()) < 0.01` (training data actually
   centered); `np.isfinite(...).all()` on both scaled arrays (no non-finite values introduced).
4. Loop over both models, `.fit()` each on scaled training data.
5. **L4 assertion** (added at C1): `len(trained_models) == len(models) == 2` — both models
   actually trained, not silently skipped.
6. Print the "what happened during training" rationale already in the template.

## Expected Result

`Training Logistic Regression...` / `✅ Logistic Regression training completed!`, then the same for
Decision Tree, then the 4-line explanation — no exceptions, at whatever `execution_count` follows
`[8]`.

## Concept & Jargon

**`fit` vs. `transform`** — `fit` learns parameters (mean/std) from data, `transform` applies
already-learned parameters; calling `fit_transform` on test data is exactly how leakage happens,
and this cell is the concrete enforcement point for the boundary Cell 11 set up. **Decision Tree
`max_depth=3`** — a manual regularization limit capping tree complexity; one of the two knobs
(along with the train/test split) the Learning-Curve cell will later show the effect of.

## Visual Sanity Check

`X_train_scaled.mean()` must be ~0 (proven by assertion, not eyeballed); the `X_test` scaling line
must read `.transform(`, never `.fit_transform(` — that single-word difference is correct vs. leaky.

## Journal Point

*Pre-written insight for the final report:* "This is the cell where 'no data leakage' stops being
a rule I stated in Cell 11 and becomes something enforced in code — the scaler literally cannot
see the test set's own statistics, only apply what it learned from training. It's also the first
cell whose output (two trained models) the Learning-Curve check will actually evaluate."

## Simplified Takeaway

This cell rescales all the measurements onto the same footing, using only what we learned from
the study set, then teaches two different models to guess wine type from that data.

## Sequence Mapping

- **Where we were:** Cell 11 produced a stratified train/test split.
- **Where we are:** Features scaled leak-free, two models trained on the training set.
- **Where we are going:** Cell 13 evaluates both models on the untouched test set.
