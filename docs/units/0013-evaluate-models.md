# Cell 13 — Part 5, Step 4: Model Evaluation

- **C1 approved:** 2026-09-11 (Pilot approved the P-I-O-F, including the train/test gap check and three added L4 assertions, before code was prepared)
- **C2 commit:** pending — awaiting Pilot run + save

## Purpose

Evaluate both trained models on the held-out test set (accuracy, classification report), select
the best performer, and compute each model's train accuracy to flag a large train/test gap — a
lightweight overfitting check ahead of the full Learning-Curve chart later.

## Inputs

`trained_models` (Cell 12), `X_train_scaled`/`y_train` (Cell 12/11, for the new train-accuracy
check), `X_test_scaled`/`y_test` (Cell 11/12).

## Outputs

`results` (test accuracy per model), `train_results` (train accuracy per model, new), `best_model`
(string), printed classification reports, model comparison, and a new gap-check line per model.

## Flow

1. For each trained model: predict on `X_test_scaled` → `accuracy_score` → `results[name]`.
2. **L4 assertions** (added at C1): `len(y_pred) == len(y_test)`; test accuracy in `[0.0, 1.0]`.
3. Print accuracy + `classification_report`.
4. **New:** predict on `X_train_scaled` → train accuracy → `train_results[name]`; assert it's also
   in `[0.0, 1.0]`.
5. **New:** print `Train: X | Test: X | Gap: X -- <flag>`, where the flag is `⚠️ possible
   overfitting` if `gap > 0.10`, else `✅ train/test gap small`.
6. **L4 assertion** (added at C1, after the loop): `set(results) == set(train_results) ==
   set(trained_models)` — nothing silently dropped.
7. Compare models, pick `best_model = max(results, key=results.get)`, print it.

## Expected Result

Per-model accuracy + classification report, a `Train: 0.XXX | Test: 0.XXX | Gap: 0.0XX -- <flag>`
line per model, the comparison table, and the best-model announcement — no exceptions, at whatever
`execution_count` follows `[9]`.

## Concept & Jargon

**Train accuracy vs. test accuracy** — the single-point version of the overfitting question the
full Learning-Curve chart answers with a whole curve; a large gap here is the same signal, just
without the sweep across training-set sizes. **Classification report** — per-class
precision/recall/F1, not just one accuracy number.

## Visual Sanity Check

**Corrected after running the cell:** the code's `gap > 0.10` check is intentionally
one-directional — it targets overfitting specifically (train accuracy *much higher* than test),
not any train/test difference. A negative gap (test scoring higher, as Logistic Regression did
here: Train 0.866 / Test 0.917) isn't the failure mode this check watches for; with only 36 test
samples, a model can land on an easier-than-average subset by chance, and that's not something to
flag. If a model *does* flag `⚠️`, that's the specific signal worth a note in the reflection.

## Journal Point

*Pre-written insight for the final report:* "Adding the train/test gap check here, before the full
learning curve, meant I already knew roughly what to expect from that chart — the single-point
comparison and the full curve should tell the same story, just at different resolutions."

*Updated after running the cell:* Logistic Regression actually scored *higher* on test (0.917)
than train (0.866) — a negative gap. That's not a bug and not the textbook "train ≥ test" pattern
assumed above; with only 36 test samples, a model can land on an easier subset by chance. Worth
stating plainly in the reflection rather than glossing over it: a small gap in either direction is
the reassuring signal, not specifically train-higher-than-test. Decision Tree's gap (+0.047) is
the more typical direction, and both are comfortably under the 0.10 flag threshold.

## Simplified Takeaway

This cell grades both models on the final exam (test set) they've never seen, and also checks
their practice-test score (train set) — a model that aced practice but bombed the real exam is a
red flag caught right here, before even drawing the full chart.

## Sequence Mapping

- **Where we were:** Cell 12 trained two models, leak-free.
- **Where we are:** Both evaluated on held-out data, with an early overfitting signal computed.
- **Where we are going:** Cell 14 interprets the best model's confusion matrix, then the new
  Learning-Curve cell provides the full picture.
