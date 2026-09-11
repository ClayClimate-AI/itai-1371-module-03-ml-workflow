<!--
  README — LIVING DOCUMENT.
  Updated incrementally at every checkpoint alongside progress.md and checkpoints.md.
  Merged into the build process per Pilot directive; do not deviate.
  Badges + Build Progress + Checkpoint Ledger reflect the CURRENT state of the build.
-->

# Module 3 — Machine Learning Workflow & Types of Learning

<p>
  <img alt="Course" src="https://img.shields.io/badge/Course-ITAI%201371-0A66C2">
  <img alt="Module" src="https://img.shields.io/badge/Module-03-1F6FEB">
  <img alt="Subject" src="https://img.shields.io/badge/Subject-Wine%20Classification-8E44AD">
  <img alt="Points" src="https://img.shields.io/badge/Points-100-success">
  <img alt="Due" src="https://img.shields.io/badge/Due-Thu%2011%3A59pm-important">
  <img alt="Setup Gate" src="https://img.shields.io/badge/Setup%20Gate-PASS-brightgreen">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.14.6-3776AB?logo=python&logoColor=white">
</p>

**Build status.** The notebook (25 cells: 12 code / 13 markdown) is executed under a spec-driven,
gate-based protocol — the *Cell-by-Cell Master Blueprint* reinforced by the *Zero-Defect* architecture,
with a decision trail in ADRs 0001–0004. Work happens on `build/lab03-josephclay` (never on `main`,
which is Production/Locked) and integrates via PR → CI → merge. Currently past the C0 contract gate:
Cell 3 (imports) is verified and committed, and the local pre-commit gate plus CI are active.

> **This README is a living document.** It updates incrementally as the build advances, in lockstep
> with [`progress.md`](progress.md) and [`checkpoints.md`](checkpoints.md). Together these three files
> form a step-by-step, professor-visible trail of exactly what was done, plus clean resume points.

---

## Overview

This project executes the Module 3 lab notebook (`Module_03_Lab_Exercise.ipynb` — Wine dataset
classification) under a disciplined, gate-driven engineering protocol rather than ad-hoc cell running.
The **System** (immutable process: guardrails, builder loop, human checkpoints) is decoupled from the
**Subject** (the Lab 03 ML payload). The guiding principle: *a green checkmark is not proof; a contract is proof.*

- **Authoritative protocol:** Ultimate Cell-by-Cell Master Blueprint for ML Execution
- **Reinforcement:** Zero-Defect ML Architecture deck (adds the C5 Export Gate)
- **Pilot (sole execution/reflection authority):** Joseph Clay
- **Agent (proposes, pre-fills, implements to contract):** Kiro

---

## Deliverables

| # | Deliverable | Status | Naming convention |
| --- | --- | --- | --- |
| 1 | Executed notebook exported as PDF (all cells + outputs) | ⏳ Not started | `L03_SingleEpoch_ITAI1371.pdf` |
| 2 | Reflective journal (1–2 pages) | ⏳ Not started | `L03Journal_R_SingleEpoch_ITAI1371.pdf` |
| 3 | Contribution journal (1–2 pages) | ⏳ Not started | `L03Journal_C_SingleEpoch_ITAI1371.pdf` |

---

## Build Progress

```
[██████████░░░░░░░░░░░░░░]  Phase 1: Pre-Flight Setup   (in progress)
[░░░░░░░░░░░░░░░░░░░░░░░░]  Phase 2: Builder Loop        (locked until C0)
[░░░░░░░░░░░░░░░░░░░░░░░░]  Phase 3: Delivery + C5 Export (locked)
```

### Setup checklist (through C0)
- [x] Context pass over all source documents (blueprint, deck, notebook, instructions)
- [x] Bubble created — `docs/adr`, `specs`, `src`, `tests`, `.venv`
- [x] Living State initialized — `progress.md`, `checkpoints.md`, and this README
- [x] Collaborative Git workflow merged — branch `build/lab03-josephclay`, ADR 0001, CI workflow
- [x] Specs drafted — `Product_Spec.md`, `Tech_Spec.md` (group name `SingleEpoch` locked)
- [x] Step 0 — P-I-O-F + Definition of Done + Scope/Constraints (`docs/STEP0_Initial_Contract.md`)
- [x] Layer 1 Setup Gate — ✅ PASS (deps present, diff clean, `load_wine` OK)
- [ ] **C0 Human Gate** — Pilot sign-off (WAIT; no construction before this)

---

## Guardrail Ladder

| Layer | Gate | Meaning |
| --- | --- | --- |
| L0 | Bubble | Isolated project-level virtual environment (`.venv`) |
| L1 | Setup Gate | Validates 100% dependency presence before execution |
| L2 | P-I-O-F (C1) | Execution sequence planned & approved before code |
| L3 | Tests (TDD) | Known-bad inputs forced to fail |
| L4 | Asserts | Live integrity checks bounding every transform |
| L5 | CI + Hooks | Re-execution on a clean, objective machine state (CI) **and** a local pre-commit gate (L1+L3) that runs before every commit — see ADR 0003 |

## Checkpoint Ledger (summary)

| Gate | Name | Status |
| --- | --- | --- |
| C0 | Initial Contract | 🟡 PENDING |
| C1 | P-I-O-F (per unit) | ⚪ Not reached |
| C2 | Atomic Commit | ⚪ Not reached |
| C3 | Debugging / ADR | ⚪ Not reached |
| C4 | Reflection Interview | ⚪ Not reached |
| C5 | Export Gate | ⚪ Not reached |

_Full definitions and the authoritative ledger live in [`checkpoints.md`](checkpoints.md)._

---

## Collaborative Git Workflow (Layer 5 — Objective Proof)

> *A local pass is subjective; a repository pass is objective.* `main` is **Production/Locked** —
> we never code on it directly. Recorded in [`docs/adr/0001-collaborative-git-workflow.md`](docs/adr/0001-collaborative-git-workflow.md).

```
  feature branch            Pull Request            GitHub Actions CI            main
  build/lab03-josephclay  ───────────────►  clean Ubuntu runner  ──(green)──►  Production/Locked
   (atomic C2 commits)                       install • L1 • L3 • L5            (sync after merge)
                                             (red CI blocks the merge)
```

1. **Branch** — `git checkout -b build/lab03-josephclay` (isolated safe zone; done).
2. **Edit & commit** — SDD + TDD + Builder Loop; one unit = one atomic commit (C2).
3. **Pull Request** — push the branch and open a PR into `main`.
4. **CI** — GitHub Actions re-runs the gates on a blank machine; a failure **blocks the merge**.
5. **Sync** — after approval + merge, pull the updated `main` locally.

**Branch Protection** on `main` (require PR + require CI green) is the target end-state; it must be
enabled in the GitHub repository settings. Until then, CI is *advisory* and the Pilot enforces the rule.

**Local pre-commit hook (one-time per clone).** The hook body is version-controlled in `.githooks/`,
but Git activates it only when pointed there. After cloning, run once:

```bash
git config core.hooksPath .githooks
```

Thereafter every `git commit` first runs the **L1 Setup Gate** and, once tests exist, the **L3 contract
tests** — a non-zero result aborts the commit. This is the fast, local half of Layer 5; CI is the
objective backstop. `--no-verify` bypasses the hook (discouraged; log any bypass in `progress.md`). See
[`docs/adr/0003-local-precommit-hooks.md`](docs/adr/0003-local-precommit-hooks.md).

**Commit message convention (from 2026-09-11 onward).** Dual format — Conventional Commits prefix plus
the protocol checkpoint tag:

```
<type>(<scope>): <subject>  [C<gate>, verified [<n>]]
```

e.g. `feat(cell5): load Wine into DataFrame + L4 integrity check  [C2, verified [3]]`. Existing history
is left intact. See [`docs/adr/0004-dual-format-commit-convention.md`](docs/adr/0004-dual-format-commit-convention.md).

---

## Repository Layout

```
.
├── .github/workflows/ci.yml   # L5: clean Ubuntu runner → install → L1 → L3 → L5 (notebook execute)
├── .githooks/pre-commit   # L5 (local): runs L1 setup gate + L3 tests before every commit — see ADR 0003
├── .venv/                 # L0: isolated environment (Python 3.14.6)
├── docs/adr/
│   ├── 0001-collaborative-git-workflow.md
│   ├── 0002-python-version-strategy.md
│   ├── 0003-local-precommit-hooks.md
│   └── 0004-dual-format-commit-convention.md
├── specs/
│   ├── Product_Spec.md    # Why/What (precedence: HIGH)
│   └── Tech_Spec.md       # How (precedence: LOW)
├── src/                   # implementation logic
├── tests/                 # L3: contract tests
├── Module_03_Lab_Exercise.ipynb   # the Subject (payload)
├── progress.md            # living state: snapshot & logs
├── checkpoints.md         # gate reference & resume protocol
└── README.md              # this living, badged overview
```

---

## Core Mandates

- Never batch. **Never proceed on assumed consent.**
- The Agent is forbidden from self-verifying code — **only the Pilot runs cells.**
- TDD ordering (write the failing assertion first) is non-negotiable.
- Every non-obvious technical decision gets a numbered ADR in `docs/adr/`.

<!-- LAST-UPDATED: 2026-09-11 04:16 CT — Specs + Step 0 written; Layer 1 Setup Gate PASS; C0 package READY (awaiting Pilot sign-off). -->
