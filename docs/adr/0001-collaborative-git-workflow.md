# ADR 0001 — Collaborative Git Workflow with CI-Gated Merges

- **Status:** Accepted
- **Date:** 2026-09-11
- **Deciders:** Pilot (Joseph Clay), Agent (Kiro)

## Context

The authoritative *Ultimate Cell-by-Cell Master Blueprint* mandates atomic commits (C2), CI as
Layer 5 objective proof (§3.3), and ADRs for non-obvious decisions. The *Zero-Defect ML Architecture*
deck reinforces that **"a local pass is subjective; a repository pass is objective"** and notes that
**"CI is advisory until Branch Protection is locked."**

The blueprint does not, by itself, prescribe a *branching strategy*. The Pilot has directed that the
professional collaborative Git workflow be merged into the process without deviation:

1. `main` is treated as **Production/Locked** — never coded on directly.
2. Work happens on an **isolated feature branch**.
3. Changes reach `main` only through a **Pull Request**.
4. **GitHub Actions CI** runs on the PR; a failing CI **blocks the merge**.
5. After merge, collaborators **sync** `main` locally.

This makes the repository — not any single laptop — the objective source of truth, which is the
core epistemic claim of Layer 5.

## Decision

Adopt the collaborative Git workflow as a permanent part of the build process:

- Development occurs on the working branch **`build/lab03-josephclay`**. Direct commits to `main`
  are prohibited.
- Every functional unit is an **atomic commit (C2)** on the working branch.
- Integration into `main` is performed exclusively via **Pull Request**.
- A **GitHub Actions** workflow (`.github/workflows/ci.yml`) runs on push/PR against a clean Ubuntu
  runner: it installs declared dependencies, runs the **Layer 1 Setup Gate**, runs **Layer 3 contract
  tests**, and executes the notebook headlessly (`nbconvert --execute`) as reproducibility proof.
- **Branch Protection** on `main` (require PR + require CI to pass) is the target end-state; until it
  is enabled in GitHub settings, CI is *advisory* and the Pilot enforces the rule manually.
- The Agent never pushes to `main` and never merges without Pilot authorization.

## Consequences

**Positive**
- Objective, machine-independent proof of reproducibility (Layer 5).
- `main` stays releasable; broken work is quarantined on the feature branch.
- Clean, reviewable history via atomic commits and PR diffs.
- Aligns the process with the deck's "Branch Protection" guidance.

**Negative / Costs**
- Slightly more ceremony (branch, PR, CI wait) than committing straight to `main`.
- Branch Protection must be configured in GitHub's web settings (outside this repo's files); until
  then the guarantee is procedural, not enforced.
- CI must install a working scientific-Python stack on Ubuntu; the local `.venv` is Python 3.14.6
  while the notebook historically declared 3.8.5 — the CI Python version will be pinned explicitly
  (tracked as a Setup-Gate finding and, if changed, a future ADR).
