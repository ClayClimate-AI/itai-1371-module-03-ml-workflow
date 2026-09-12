# Checkpoints — Gate Reference & Resume Protocol

> **Purpose of this file.** A durable reference for every human gate (C0–C5) and the exact
> procedure to resume the build after any stop ("Cold Start"). Maintained per the *Ultimate
> Cell-by-Cell Master Blueprint* (§3.1) and the *Zero-Defect ML Architecture* deck (which adds
> the C5 Export Gate). This file, together with `progress.md` and the badged `README.md`, forms the
> professor-visible, step-by-step trail of what was done and why. All three update at every checkpoint.

---

## Checkpoint Definitions

| Gate | Name | What it requires | Who signs off |
| --- | --- | --- | --- |
| **C0** | Initial Contract | Step 0 P-I-O-F + DoD + Scope/Constraints pre-filled; Layer 1 Setup Gate run and reported. **No construction until Pilot confirms.** | Pilot |
| **C1** | P-I-O-F (per unit) | Each cell/unit has an approved Purpose-Inputs-Outputs-Flow **before** any code is written. | Pilot |
| **C2** | Atomic Commit | One functional unit = one commit. Record unit name, testing performed, Pilot validation. | Pilot |
| **C3** | Debugging / ADR | On failure, log exact symptom & decision state **before** applying a fix. Non-obvious fixes get a numbered ADR. | Pilot |
| **C4** | Reflection Interview | Dynamic verbatim Q&A generated from this project's own failure logs, ADRs, and commit trail. | Pilot |
| **C5** | Export Gate | Kernel restart → run-all with counters `[1..N]` and zero gaps → visual audit (no clipping, margins fit) → headless PDF export. Any failure ⇒ fix and restart from Step 1. | Pilot |

---

## Guardrail Ladder (reference)

- **L0 Bubble** — strictly isolated project-level virtual environment (`.venv`).
- **L1 Setup Gate** — validates 100% dependency presence before execution (exit 0 only if clean).
- **L2 P-I-O-F (C1)** — execution sequence planned and approved prior to code.
- **L3 Tests (TDD)** — known-bad inputs mathematically forced to fail (a test that cannot fail is not a gate).
- **L4 Asserts** — live integrity checks bounding every data transformation (`check_alignment`, `check_scale`, `check_integrity`, `check_broadcasting`).
- **L5 CI + Hooks** — re-execution on a clean, objective machine state. *A local pass is subjective;
  a repository pass is objective.* Implemented as the **collaborative Git workflow**: `main` is
  Production/Locked; work occurs on branch `build/lab03-josephclay`; integration is PR-only; GitHub
  Actions (`.github/workflows/ci.yml`) re-runs L1/L3/L5 on a clean Ubuntu runner and a red run blocks
  the merge. Branch Protection on `main` is the target end-state (advisory until enabled). See
  `docs/adr/0001-collaborative-git-workflow.md`. A **local pre-commit hook** (`.githooks/pre-commit`,
  activated per clone via `git config core.hooksPath .githooks`) runs the fast subset — L1 Setup Gate +
  L3 tests — before every commit, aborting on failure; CI remains the objective backstop. See
  `docs/adr/0003-local-precommit-hooks.md`. Commit messages follow the dual format
  (`<type>(<scope>): <subject>  [C<gate>, verified [<n>]]`) per `docs/adr/0004-dual-format-commit-convention.md`.

### ADR 0005 Invariants (enforced in the hook, and in CI except #4)

| # | Invariant | Script | Catches |
| - | --- | --- | --- |
| 1 | Execution-Proof Gate | `scripts/execution_proof_gate.py` | A cell logged "Pilot-verified" in `progress.md` whose committed notebook shows `execution_count: null` / empty outputs. |
| 2 | Per-Unit Documentation Gate | `scripts/unit_doc_lint.py` | A `docs/units/*.md` record missing one of the 8 required sections (see ADR 0005). |
| 3 | Failure-Classification Gate | `scripts/failure_log_lint.py` | A Failure & Amendment Logs entry that doesn't open with `**Code Failure**` / `**Spec Failure**`. |
| 4 | Push-Before-Verified Gate | `scripts/push_verified_gate.py` | `progress.md` marking a commit Pilot-verified before it exists on `origin/<branch>`. Local-only — not run in CI. |

See `docs/adr/0005-per-unit-documentation-enrichment.md` for full rationale.

---

## Core Mandates (non-negotiable)

- A green checkmark is not proof; a **contract** is proof.
- **Never batch. Never proceed on assumed consent.**
- Agent is forbidden from self-verifying code — only the Pilot runs cells.
- TDD ordering (write the failing assertion first) is non-negotiable.
- Generate only renderable Markdown — no graphs, mermaid, or images in Agent output.

### Pilot-Locked Constraints (2026-09-11)

1. **Execution authority (STRICT):** The Agent NEVER runs notebook cells — not even to "validate
   locally on the Pilot's behalf." The Agent prepares/proposes cells and contracts; the **Pilot is
   the sole executor**. Local objective proof comes from the Bubble's L1/L3 gates and CI, not from
   the Agent executing the payload notebook.
2. **Delivery scope:** The **local Bubble** provides objective proof (L1 setup gate, L3 contract
   tests, L5 CI notebook execution on a clean runner). **Amended 2026-09-12 (ADR 0006):** the C5
   PDF export uses local `jupyter nbconvert --to webpdf` (Playwright/Chromium) instead of the
   originally-locked Colab path — rendering already-saved outputs, never re-executing. CI's
   `nbconvert --to notebook --execute` step remains the objective "runs clean" proof; this change
   only affects how the final PDF artifact is produced.

---

## Checkpoint Ledger (updated as gates are reached)

| Gate | Status | Date/Time (CT) | Pilot Sign-off | Notes |
| --- | --- | --- | --- | --- |
| C0 | **APPROVED** | 2026-09-11 05:07 | Joseph Clay ("Commence") | Step 0 + Setup Gate PASS accepted; risks resolved: ADR 0002 (py-version), solo member Joseph Clay, due Sept 10→11 (Canvas discrepancy). Construction authorized. |
| C5 | **PASSED** | 2026-09-12 11:35 | Joseph Clay (confirmed visual audit) | Kernel restart → Run All: counters `[1]`–`[13]`, zero gaps, zero errors, all key results reproduced exactly (deterministic, `random_state=42`). Export via ADR 0006 (amended): first `--to webpdf` attempt clipped long code lines — caught by reading the actual rendered pages, not just checking exit code — refined to `--to html` + a wrap-CSS patch + Playwright render. Re-verified page by page: no clipping, both EDA charts, the confusion matrix, and the learning-curve chart all render fully. `L03_SingleEpoch_ITAI1371.pdf`, 23 pages. |
| C4 | **PASSED (short form)** | 2026-09-12 | Joseph Clay | Dynamic interview per §3.4, 4 of 5 blueprint dimensions (territory novelty omitted at Pilot's discretion — noted, not silently dropped). Verbatim transcript in `reflections.md`, unedited. Questions drawn from this project's own trail: L3-vs-L4 distinction (CI vs. the scaling-order assertion), the 4 pre-run bugs caught by reading vs. running, the Learning-Curve contract-drift amendment, and the Cell 3/5 false-verification failure. |

---

## Resume Protocol (Cold Start)

If work stops and later resumes, the Agent shall, in order:

1. **Read `progress.md`** — take the Snapshot (Current Stage, Last Checkpoint, Next Single Action).
2. **Read this `checkpoints.md`** — confirm the last gate reached in the Checkpoint Ledger.
3. **Cross-check git history** — confirm the active branch is `build/lab03-josephclay` (never resume
   on `main`), and verify the last atomic commit (C2) matches the Unit Log.
4. **Run the Layer 1 Setup Gate** — confirm the environment is still valid (deps present, `.venv` active).
5. **State the next single action** and **request Pilot input** before proceeding. Never resume construction on assumed consent.
