# Tech Spec — How

> **Precedence: LOW.** Amended to match `Product_Spec.md` on any conflict. Defines the guardrail
> implementation, library choices, environment, and naming conventions for the build. Derived from
> the *Ultimate Cell-by-Cell Master Blueprint* and the *Zero-Defect ML Architecture* deck.

## 1. Environment (L0 Bubble)

- Isolated `.venv` at project root. Local dev Python: **3.14.6**.
- **CI Python pinned to 3.12** (`.github/workflows/ci.yml`) for a stable scientific stack on Ubuntu.
- Version mismatch vs. the notebook's declared `3.8.5` kernel is a **Setup-Gate finding**; if a
  specific version must be enforced, it will be recorded in a future ADR.

## 2. Dependencies (declared)

The Subject notebook imports: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`.
Tooling for gates: `pytest` (L3), `jupyter` + `nbconvert` (L5 execution), `pyyaml` (CI lint helper).

- **`requirements.txt`** will pin these (produced at/with the Setup Gate). The L1 gate performs a
  **dependency diff** (actual-imports vs. declared) and exits non-zero on any gap.

## 3. Guardrail Implementation

| Layer | Implementation |
| --- | --- |
| L0 Bubble | `.venv` (this project) |
| L1 Setup Gate | `scripts/setup_gate.py` — exit 0 only if all declared deps import + env facts (Python, data availability) validate; performs actual-vs-declared dependency diff |
| L2 P-I-O-F (C1) | Each notebook cell/unit documented with Purpose-Inputs-Outputs-Flow and Pilot-approved before code |
| L3 Tests (TDD) | `tests/` with `pytest`; each validator gets a known-bad input proving the test can fail |
| L4 Asserts | In-notebook validators bounding each transform: `check_alignment()`, `check_scale()` (features ∈ [0,1] or standardized), `check_integrity()` (no NaN/Inf), `check_broadcasting()` — each emits a vocal `PASS`; raises `AssertionError` (not `ValueError`) with an actionable message |
| L5 CI + Hooks | `.github/workflows/ci.yml` on clean Ubuntu: install → L1 → L3 → L5 (`nbconvert --execute`) |

## 4. ML Subject — technical choices (from the notebook)

- Dataset: `sklearn.datasets.load_wine` (178×13, 3 classes).
- Split: `train_test_split(test_size=0.2, random_state=42, stratify=y)`.
- Scaling: `StandardScaler` **fit on train only**, applied to train+test (no leakage).
- Models: `LogisticRegression(random_state=42)`, `DecisionTreeClassifier(random_state=42, max_depth=3)`.
- Metrics: `accuracy_score`, `classification_report`, `confusion_matrix`.
- Determinism: fixed `random_state=42` everywhere for reproducibility.

## 5. Conventions

- **Branching:** `main` = Production/Locked; work on `build/lab03-josephclay`; PR-only merges (ADR 0001).
- **Commits (C2):** one unit = one commit; message states unit + testing + Pilot validation status.
- **ADRs:** `docs/adr/NNNN-title.md`, format Status / Context / Decision / Consequences.
- **Living state:** `progress.md`, `checkpoints.md`, `README.md` updated at every checkpoint.
- **Deliverable naming:** group name `SingleEpoch` (see Product Spec §0).
- **Execution:** Agent NEVER runs cells (Pilot-locked). Colab used ONLY for the C5 final PDF export.
- **Agent output:** renderable Markdown only — no images/graphs/mermaid.
