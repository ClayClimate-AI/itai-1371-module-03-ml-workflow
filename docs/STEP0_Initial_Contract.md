# Step 0 — Initial Contract (P-I-O-F · DoD · Scope) — for Checkpoint C0

> Per blueprint §1.3: a pre-construction comprehension pass, pre-filled from source context. The
> Agent is **forbidden from advancing past C0 without Pilot confirmation.** This is the whole-project
> contract; each individual cell later gets its own P-I-O-F at C1.

- **Project:** ITAI 1371 · Module 03 · Lab L03 — ML Workflow & Types of Learning
- **Group:** `SingleEpoch` · **Pilot:** Joseph Clay · **Agent:** Kiro
- **Subject:** `Module_03_Lab_Exercise.ipynb` (Wine classification, 25 cells)

---

## P — Purpose (the Why)

Execute the Wine-classification lab end-to-end under the gate-driven protocol so it (a) runs cleanly
top-to-bottom, (b) demonstrably teaches the ML workflow and the three learning types, and (c) produces
three graded PDF deliverables — while leaving a professor-visible, reproducible audit trail.

## I — Inputs

- **Data:** `sklearn.datasets.load_wine` (178 samples × 13 features, 3 classes, no missing values).
- **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn.
- **Starter code:** the 25-cell notebook (12 code / 13 markdown), already scaffolded with the workflow.
- **Governing specs:** `Product_Spec.md` (HIGH), `Tech_Spec.md` (LOW).

## O — Outputs

- **Deliverable 1:** `L03_SingleEpoch_ITAI1371.pdf` — fully executed notebook, all outputs visible.
- **Deliverable 2:** `L03Journal_R_SingleEpoch_ITAI1371.pdf` — reflective journal (1–2 pp).
- **Deliverable 3:** `L03Journal_C_SingleEpoch_ITAI1371.pdf` — contribution journal (1–2 pp).
- **Process artifacts:** green CI run, atomic commit trail, ADRs, C4 verbatim transcript.

## F — Flow (high-level architecture)

```
load_wine → DataFrame → EDA (dist + corr) → feature select → split (stratified 80/20)
   → StandardScaler (fit train only) → train {LogReg, DecisionTree} → evaluate (acc, report, CM)
   → interpret best model → data-types + assessment + reflection → C5 export (Colab) → PDFs
```
Each arrow is a **Unit**: gets its own C1 P-I-O-F, an L4 assertion pair (`check_integrity` in/out),
an L3 test where applicable, and a C2 atomic commit — before the Pilot runs the cell.

---

## Definition of Done (DoD)

1. All 25 cells execute sequentially, counters `[1]..[N]`, **zero gaps**.
2. Dataset assertions hold: shape (178,13), 3 classes, 0 nulls.
3. No data leakage: scaler fit on **train only**.
4. Both models trained; evaluation + best-model selection + confusion matrix rendered.
5. Assessment answers 5/5; reflection markdown completed by Pilot.
6. L4 validators emit `PASS` (vocal success) and are proven to catch known-bad input (L3).
7. CI green on the PR (clean-runner objective proof) before merge to `main`.
8. Three PDFs exported per C5 gate, named exactly per Product Spec §3.
9. C4 verbatim reflection interview transcript captured.
10. `progress.md` / `checkpoints.md` / `README.md` reflect final state.

---

## Scope & Constraints

**In scope**
- Executing/validating the existing lab notebook; adding L4 in-notebook validators; contract tests;
  CI; the three deliverables.

**Out of scope (anti-over-engineering)**
- No new models/datasets beyond what the notebook specifies; no hyperparameter tuning beyond the
  given `max_depth=3`; no deployment; no changes to pedagogical intent.

**Hard constraints**
- Agent NEVER runs cells (Pilot-locked). Colab used ONLY for the C5 PDF export.
- Deliverable naming uses group `SingleEpoch`, exactly.
- `main` is Production/Locked; work on `build/lab03-josephclay`; PR + green CI to merge.
- Renderable Markdown only in Agent output.

**Known risks / open items — RESOLVED at C0 (2026-09-11)**
- **Python version:** ✅ Resolved via **ADR 0002** — Bubble 3.14.6 (Setup Gate passed), CI pinned
  3.12 as the reproducible reference/Colab proxy, notebook's declared 3.8.5 treated as non-binding.
- **Group members:** ✅ **Joseph Clay (solo)** — contribution journal covers the single member.
- **Due date:** ✅ Originally **due Sept 10, 11:59 pm**; being completed **Sept 11** due to a Canvas
  submission discrepancy. Treat as time-critical — prioritize the critical path to the three PDFs.
