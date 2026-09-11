# Cell 8 — Part 4: EDA — Class Distribution + Correlation Heatmap

- **C1 approved:** 2026-09-11 (Pilot approved the P-I-O-F, including three added L4 assertions, before code was prepared)
- **C2 commit:** pending — awaiting Pilot run + save

## Purpose

Visually confirm class balance and inter-feature relationships via two plots — the first cell in
the notebook whose real output is an image, not text.

## Inputs

`df` (Cells 5/6 — loaded, integrity-checked, structure-checked: 178×15, 71/59/48 class split).

## Outputs

A rendered 2-panel matplotlib figure (class-count bar chart + 6-feature correlation heatmap), plus
three interpretive print lines. `class_counts`/`correlation_matrix` are local to the plot, not
persisted for later cells.

## Flow

1. Build a 12×4 figure with two subplots.
2. Left: bar chart of `df['wine_class_name'].value_counts()`.
3. **L4 assertion** (added at C1): `class_counts.sum() == len(df)` — class counts must account
   for every sample.
4. Right: annotated heatmap of the first 6 features' correlation matrix (`coolwarm`, centered at 0).
5. **L4 assertions** (added at C1): correlation matrix shape is exactly `(6, 6)`; its diagonal is
   all `1.0` (a feature always perfectly correlates with itself — if this breaks, the correlation
   computation or the `.iloc[:, :6]` slice is broken).
6. Render (`plt.show()`), then print the three interpretive bullets already in the template.

## Expected Result

A visible figure beneath the cell — left panel: 3 bars (red/green/blue) at roughly 71/59/48; right
panel: a 6×6 annotated heatmap whose diagonal reads `1.00` in every cell. Followed by the three
`📊 EDA helps us understand...` print lines, at whatever `execution_count` follows `[5]`.

## Concept & Jargon

**Correlation matrix** — pairwise linear relationship strength between features, ranging -1 to 1.
**Diverging colormap centered at 0** — zero correlation renders as neutral/white, so strong
positive/negative relationships visually stand out. A correlation matrix's diagonal is always 1.0
by definition (a feature perfectly correlates with itself); that fact doubles as a free
correctness check on the computation.

## Visual Sanity Check

Every diagonal cell in the heatmap must read `1.00` — if it doesn't, the correlation computation
or the 6-feature slice is broken. Bar heights should visually match Cell 6's printed counts
(class_1: 71, class_0: 59, class_2: 48).

## Journal Point

*Pre-written insight for the final report:* "This was the first cell where 'the output looks
right' meant actually looking at an image instead of reading a printed number — which is exactly
why the Visual Sanity Check has to be a specific, checkable claim (the diagonal is 1.0) rather
than a vague 'the chart looks fine.'"

## Simplified Takeaway

This cell turns the class counts and feature relationships we already know as numbers into two
pictures — a bar chart and a color-coded grid — so patterns are easier to spot at a glance.

## Sequence Mapping

- **Where we were:** Cell 6 confirmed class counts and zero missing values numerically.
- **Where we are:** The same facts, seen visually, plus feature correlations for the first time.
- **Where we are going:** Cell 10 starts the actual ML workflow — feature selection.
