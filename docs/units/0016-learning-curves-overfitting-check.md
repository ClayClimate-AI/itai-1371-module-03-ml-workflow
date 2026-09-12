# Cell 16 — Step 6 (Amendment): Learning Curves — Overfitting Check

- **C1 approved:** 2026-09-11 (Pilot approved the P-I-O-F, including two added L4 assertions, before code was prepared)
- **C2 commit:** pending — awaiting Pilot run + save
- **Note:** this is a genuinely new cell, not an edit to the original template — added per the C0
  Amendment in `docs/STEP0_Initial_Contract.md` (DoD 25→27 cells). It's preceded by a new markdown
  header cell (index 15) explaining why it exists. Its insertion shifted every subsequent cell
  (old Cell 15 "Part 6..." onward) by +2.

## Purpose

For both trained models, plot learning curves (training vs. cross-validation accuracy across
increasing training-set sizes) to prove — visually and numerically — whether each model
generalized or overfit. This is the "big chart" from the Pilot's original request.

## Inputs

`trained_models` (Cell 12 — used as templates; `learning_curve` clones and refits internally, it
doesn't disturb the already-fitted models), `X_train_scaled`/`y_train` (Cell 11/12).

## Outputs

A rendered 2-panel figure (one learning curve per model), printed final-gap summary per model.

## Flow

1. `train_sizes = np.linspace(0.3, 1.0, 8)` — 8 points from 30% to 100% of the training set.
   **Corrected before running:** originally started at 10%, which with `cv=5` risked a
   `ValueError` — a class could have as few as 3-4 samples in a ~14-sample subset, below the
   5-per-class floor `StratifiedKFold(n_splits=5)` requires. Found by reading the code, not by
   running it (the Agent cannot execute the payload notebook); fixed before handing to the Pilot.
2. For each model: `learning_curve(model, X_train_scaled, y_train, train_sizes=train_sizes, cv=5,
   scoring='accuracy', random_state=42)` → sizes, train_scores, val_scores; mean across folds.
3. **L4 assertions:** output shapes align across `sizes`/`train_scores`/`val_scores`; both
   mean-accuracy arrays stay in `[0, 1]`.
4. Plot both lines (Training score / Validation score) per model, side by side.
5. Print each model's final-point gap with the same `⚠️`/`✅` flag pattern from Cell 13.
6. Print the interpretation block (overfitting/underfitting/healthy generalization).

## Expected Result

Two side-by-side line charts (Logistic Regression, Decision Tree), each with a training line and
a validation line across 8 points from 30%→100% of the training set; a final-gap summary line per
model; no exceptions.

## Concept & Jargon

**Learning curve** — training and cross-validation accuracy plotted against training-set size.
**Cross-validation (`cv=5`)** — a more robust estimate than one fixed test set, averaging over 5
different splits of the training data itself.

## Visual Sanity Check

Each model's final-point gap here should be roughly the same order of magnitude as Cell 13's
single-point gap (LogReg ≈ -0.05, Tree ≈ 0.047) — not identical (different methodology:
cross-validation on the training set vs. one fixed held-out test set), but not wildly different
either. A bug found and fixed pre-run: a second `{{flag}}` in an f-string would have rendered the
literal text `{flag}` instead of the actual value — caught by re-reading the generated code before
handing it off, corrected to `{flag}`.

## Journal Point

*Pre-written insight for the final report:* "To rigorously evaluate my models beyond a
surface-level test score, I analyzed the performance gap between training and cross-validation
accuracy across increasing training-set sizes — the principle behind Learning Curves. A large,
persistent gap would be visual and mathematical proof of overfitting; training and validation
accuracy tracking closely at a high level is proof of genuine generalization rather than
memorization."

*Updated with the actual result:* Both models showed exactly the healthy pattern — Logistic
Regression's training (0.873) and validation (0.838) accuracy converged to a 0.035 gap, Decision
Tree's to a 0.038 gap, both lines climbing together as training size increased from 33 to 113
samples rather than the training line staying flat/high while validation stagnates. That's the
visual and mathematical proof neither model memorized the training data — they generalized.

## Simplified Takeaway

We retrain each model many times on bigger and bigger practice sets and watch two lines — if they
end up close together and high, the model actually learned the pattern; if they stay far apart, it
memorized instead.

## Sequence Mapping

- **Where we were:** Cell 14's confusion matrix showed exactly where the best model gets confused.
- **Where we are:** Prove whether that performance holds up across a systematic sweep of
  training-set sizes, for both models.
- **Where we are going:** Part 6 (old Cell 15, now Cell 17) — the notebook's remaining conceptual
  sections (data types, hands-on practice, assessment).
