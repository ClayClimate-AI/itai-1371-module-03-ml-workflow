# Product Spec — Why / What

> **Precedence: HIGH.** On any conflict with `Tech_Spec.md`, this document wins; the Tech Spec is
> amended to match. Defines intent, deliverables, metrics, and acceptance criteria for the Module 3
> ML Workflow lab. Source: assignment instructions (L03 Lab ITAI 1371) + the authoritative blueprint.

## 0. Canonical Identifiers (Pilot-locked — do not deviate)

- **Group name (`<GroupName>`):** `SingleEpoch` (one word, no spaces).
- **Group members:** Joseph Clay (solo).
- **Course:** ITAI 1371 · **Module:** 03 · **Lab:** L03.
- **Due:** originally Sept 10, 11:59 pm; completing Sept 11 (Canvas submission discrepancy).

## 1. Intent (the Why)

Demonstrate genuine understanding of the end-to-end machine-learning workflow and the three learning
types by executing the Wine-classification lab (`Module_03_Lab_Exercise.ipynb`) under a disciplined,
gate-driven process. The grade rewards *understanding and reproducibility*, not merely a notebook that
runs. Learning — not completion — is the goal.

## 2. User Stories

- As a **student (Pilot)**, I can run every notebook cell top-to-bottom with no gaps and see correct
  outputs, so I can export a clean PDF that proves full workflow comprehension.
- As a **professor**, I can open `progress.md`, `checkpoints.md`, and `README.md` and see exactly
  what was done, in what order, and why — a step-by-step, verifiable trail.
- As a **reviewer**, I can trust a green CI run as objective proof the work reproduces on a clean
  machine, not just "on the student's laptop."

## 3. Deliverables (What)

| # | Deliverable | Format | Naming |
| --- | --- | --- | --- |
| 1 | Executed notebook — all cells run, outputs visible | PDF | `L03_SingleEpoch_ITAI1371.pdf` |
| 2 | Reflective journal — genuine reflection on learning process (1–2 pp) | PDF | `L03Journal_R_SingleEpoch_ITAI1371.pdf` |
| 3 | Contribution journal — each member's contribution in own words (1–2 pp) | PDF | `L03Journal_C_SingleEpoch_ITAI1371.pdf` |

## 4. Success Metrics / Acceptance Criteria

**Notebook (Deliverable 1)**
- [ ] All 25 cells execute sequentially with counters `[1]..[N]`, **zero gaps** (C5 requirement).
- [ ] Wine dataset loads: 178 samples, 13 features, 3 classes, 0 missing values.
- [ ] EDA renders (class distribution + correlation heatmap).
- [ ] Both models train (Logistic Regression + Decision Tree) on **scaled** features (scaler fit on
      train only — no leakage).
- [ ] Evaluation prints accuracy + classification report; best model selected; confusion matrix renders.
- [ ] Data-type section, assessment (5/5 learning-type answers), and reflection cells complete.
- [ ] PDF captures all code + outputs legibly, no clipping, standard margins (C5 visual audit).

**Reflective journal (Deliverable 2)**
- [ ] Deep analysis of the learning process, not surface description; connects concepts (e.g., why the
      "answer key" distinguishes supervised from unsupervised; overfitting insight).

**Contribution journal (Deliverable 3)**
- [ ] Specific, own-words contribution for the sole member of `SingleEpoch` — Joseph Clay. (Missing individual contribution = −20 pts.)

**Process (System-level, from blueprint/deck)**
- [ ] Every unit passed C1 (P-I-O-F approved) before code.
- [ ] Atomic commits (C2) — one unit per commit — on branch `build/lab03-josephclay`.
- [ ] Green CI on the PR (objective L5 proof) before merge to `main`.
- [ ] C4 verbatim reflection interview transcript captured.

## 5. Grading Rubric (from instructions)

| Component | Points |
| --- | --- |
| Project (working program 60 + documentation 10) | 70 |
| Reflection | 10 |
| Individual contribution | 20 (missing = −20) |
| **Total** | **100** |

## 6. Constraints / Non-Goals

- **Non-goal:** changing the lab's pedagogical content or model choices beyond what the notebook asks.
- **Constraint:** deliverables must follow the exact naming convention with `SingleEpoch` as the group name.
- **Constraint:** work is the group's own; consultation of docs is allowed, but analysis/reflection
  must be original.
- **Due:** originally **Sept 10, 11:59 pm**; being completed **Sept 11** due to a Canvas submission discrepancy.
