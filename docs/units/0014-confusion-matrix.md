# Cell 14 — Part 5, Step 5: Model Interpretation (Confusion Matrix)

- **C1 approved:** 2026-09-11 (Pilot approved the P-I-O-F, including three added L4 assertions, before code was prepared)
- **C2 commit:** pending — awaiting Pilot run + save

## Purpose

Visualize exactly where the best model (Logistic Regression) succeeds and fails, per class —
which wine types get confused with which.

## Inputs

`best_model` (`"Logistic Regression"`), `trained_models`, `X_test_scaled`/`y_test`,
`wine_data.target_names`, and `results[best_model]` (0.917, from Cell 13 — used for a cross-check).

## Outputs

`cm` (3×3 confusion matrix array), a rendered annotated heatmap, printed interpretation bullets.

## Flow

1. `best_model_obj = trained_models[best_model]`; predict on `X_test_scaled`.
2. `cm = confusion_matrix(y_test, y_pred_best)`.
3. **L4 assertions** (added at C1): `cm.shape == (3, 3)`; `cm.sum() == len(y_test)` (all
   predictions accounted for); `np.trace(cm) / cm.sum()` is close to `results[best_model]` — a
   cross-cell consistency check, recomputing accuracy independently from the confusion matrix and
   proving it matches Cell 13's `accuracy_score` result.
4. Render the heatmap (annotated, `Blues`, labeled with class names).
5. Print the 3 interpretation bullets already in the template.

## Expected Result

A 3×3 blue heatmap, diagonal cells visibly darker/higher-valued than off-diagonal, whose diagonal
sum divided by 36 equals `0.917` (matching Cell 13, proven not assumed). Followed by the 3
`🔍 Interpreting...` print lines, at whatever `execution_count` follows `[10]`.

## Concept & Jargon

**Confusion matrix** — rows are true classes, columns are predicted classes; diagonal = correct,
off-diagonal = specific misclassifications (e.g., row `class_1`, column `class_2` = a true
class_1 wrongly predicted as class_2). This is the same "raw numbers → visual heatmap" upgrade
discussed for learning curves, applied here first.

## Visual Sanity Check

Diagonal sum ÷ total must equal `0.917` — proven by the third assertion, not eyeballed. Cell 13's
classification report already showed `class_2` recall at 0.70 (the weakest), so the heatmap's
`class_2` row should show at least one off-diagonal value.

## Journal Point

*Pre-written insight for the final report:* "The confusion matrix assertion that ties back to
Cell 13's accuracy number was the most valuable one so far — it's not just checking this cell's
own math, it's proving two independently-computed numbers from two different cells agree, which
is a stronger guarantee than either check alone."

## Simplified Takeaway

This chart shows exactly which wine types the model got right and which ones it mixed up — not
just one accuracy number, but the specific pattern of mistakes.

## Sequence Mapping

- **Where we were:** Cell 13 evaluated both models and picked Logistic Regression.
- **Where we are:** See exactly where the best model succeeds/fails, per class.
- **Where we are going:** The new Learning-Curve cell — the last piece, showing whether this
  performance generalizes across training-set sizes.
