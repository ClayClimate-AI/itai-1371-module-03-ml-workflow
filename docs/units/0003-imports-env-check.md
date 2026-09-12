# Cell 3 — Part 2: Environment Setup (Imports + L4 Assertion)

> **Retroactive record.** Written 2026-09-11 per ADR 0005 Amendment 2, after the code was already
> committed and Pilot-verified. Normal C1 order is P-I-O-F *before* code — this file reconstructs
> that plan from what was actually built, so the enrichment chain (Sequence Mapping, Journal
> Point) has a real starting point instead of beginning at Cell 6.

- **C1 approved:** 2026-09-11 05:20 (original, pre-ADR-0005 approval — Purpose/Inputs/Outputs/Flow
  only; this file adds the six ADR 0005 fields retroactively)
- **C2 commit:** `31eac15` (code); execution proof re-saved in `265c779`

## Purpose

Stand up the working environment for the whole notebook in one place: import every library the
downstream cells need, and fail loudly — before any data touches the pipeline — if the core
tools didn't bind correctly.

## Inputs

None from prior cells (this is the first code cell). Inputs are the `.venv` environment itself
(Layer 0) and the declared dependencies in `requirements.txt`.

## Outputs

- Bound names in the notebook's namespace: `pd`, `np`, `plt`, `sns`, `load_wine`,
  `train_test_split`, `LogisticRegression`, `DecisionTreeClassifier`, `accuracy_score`,
  `classification_report`, `confusion_matrix`, `StandardScaler`.
- Plot style set (`plt.style.use('default')`, `sns.set_palette("husl")`).
- Two printed confirmation lines.

## Flow

1. Import each library needed anywhere in the notebook (not just this cell) — front-loading avoids
   a `NameError` mid-pipeline later.
2. L4 assertion: `pandas` and `numpy` are not `None`, and `load_wine` is callable — a minimal
   "did the import actually work" check, not a full test suite.
3. Set matplotlib/seaborn styling defaults for later plots.
4. Print two success lines as a human-readable signal the cell completed.

## Expected Result

Two green-checkmark print lines (`✅ L4 environment check passed...`, `✅ All libraries imported
successfully!`) and a rocket-emoji line, with no exception — visible in the actual output at
`execution_count: 3`.

## Concept & Jargon

**Fail-fast environment validation**: rather than letting a broken import surface as a confusing
error three cells later (e.g., `NameError: load_wine` — which is exactly what happened once in
this project's own history, see `progress.md` 05:27 entry), assert the environment is sound at
the point of import, where the failure is unambiguous.

- **L4 assertion**: a pre/post integrity check on a transformation or setup step, per the
  blueprint's Layer 4 (distinct from Layer 3 `tests/` contract tests).
- **Binding**: a name in Python pointing at an imported module/object; "failed to bind" means the
  import silently produced `None` or an unusable object rather than raising.

## Visual Sanity Check

Confirm the assertion actually exercises real objects, not tautologies: `assert _mod is not None`
would trivially pass even on a broken import if `_mod` were reassigned after a failed import
attempt raised and got swallowed elsewhere. The correct proof is that the cell's *own* import
statements at the top ran with no exception — the assertions are a second, explicit check on top
of that, not a substitute for it. A "known-bad" version of this cell (e.g., misspelling
`load_wine`) throws an `ImportError` at the import line itself, before the assertions ever run —
confirming the assertions aren't the only thing standing between a broken environment and
downstream cells.

## Journal Point

*Pre-written insight for the final report:* "The first real lesson in this build wasn't about the
Wine dataset — it was about sequencing. Running Cell 5 before Cell 3 produced a `NameError`
because `load_wine` wasn't bound yet. That's not a code bug; it's why Layer 4's fail-fast checks
matter even for something as 'boring' as an imports cell — the checks catch the class of mistake
a human makes by running cells out of order, not just mistakes in the code itself."

## Simplified Takeaway

This cell just turns on all the tools we'll need later — pandas for tables, matplotlib for
charts, scikit-learn for the actual machine learning — and double-checks they turned on correctly
before we build anything on top of them.

## Sequence Mapping

- **Where we were:** Nothing yet — this is the first executable cell in the notebook.
- **Where we are:** All libraries imported and verified bound; plotting style set.
- **Where we are going:** Cell 5 loads the actual Wine dataset, using `load_wine` bound here.
