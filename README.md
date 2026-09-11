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
</p>

<p>
  <img alt="Protocol" src="https://img.shields.io/badge/Protocol-Cell--by--Cell%20Master%20Blueprint-2C3E50">
  <img alt="Architecture" src="https://img.shields.io/badge/Architecture-Zero--Defect-2C3E50">
  <img alt="Methodology" src="https://img.shields.io/badge/Methodology-Spec--Driven%20Gates-2C3E50">
</p>

<p>
  <img alt="Stage" src="https://img.shields.io/badge/Stage-Pre--Flight%20Setup-yellow">
  <img alt="Checkpoint" src="https://img.shields.io/badge/Checkpoint-C0%20READY%20(awaiting%20sign--off)-orange">
  <img alt="Progress" src="https://img.shields.io/badge/setup-6%2F7%20tasks%20(Setup%20Gate%20PASS)-brightgreen">
  <img alt="Python" src="https://img.shields.io/badge/.venv-Python%203.14.6-3776AB?logo=python&logoColor=white">
  <img alt="Cells" src="https://img.shields.io/badge/Notebook-25%20cells%20(12%20code%20%2F%2013%20md)-informational">
</p>

<p>
  <img alt="Branch" src="https://img.shields.io/badge/branch-build%2Flab03--josephclay-6f42c1?logo=git&logoColor=white">
  <img alt="Main" src="https://img.shields.io/badge/main-Production%2FLocked-critical">
  <img alt="Workflow" src="https://img.shields.io/badge/workflow-PR%20%E2%86%92%20CI%20%E2%86%92%20merge-0A66C2">
  <img alt="CI" src="https://img.shields.io/badge/CI-GitHub%20Actions%20(advisory)-yellow?logo=githubactions&logoColor=white">
  <img alt="ADR" src="https://img.shields.io/badge/ADR-0001%2C%200002%20accepted-2C3E50">
</p>

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
| L5 | CI + Hooks | Re-execution on a clean, objective machine state |

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

---

## Repository Layout

```
.
├── .github/workflows/ci.yml   # L5: clean Ubuntu runner → install → L1 → L3 → L5 (notebook execute)
├── .venv/                 # L0: isolated environment (Python 3.14.6)
├── docs/adr/
│   └── 0001-collaborative-git-workflow.md
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
