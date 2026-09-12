# ADR 0003 — Local Pre-Commit Hooks (Layer 5, shifted left)

- **Status:** Accepted
- **Date:** 2026-09-11
- **Deciders:** Pilot (Joseph Clay), Agent (Kiro)

## Context

Layer 5 of the guardrail ladder is "CI + Hooks" — *a local pass is subjective; a repository pass is
objective.* Until now only the CI half existed (`.github/workflows/ci.yml` runs L1/L3/L5 on a clean
Ubuntu runner). Locally there were **no active hooks**: `core.hooksPath` was unset and `.git/hooks`
contained only Git's stock `*.sample` files. Consequently a broken environment or a failing test could
be committed locally and only be caught later on the PR — a slow feedback loop for a time-critical build.

We want the fast, subjective local check to run *before* each commit is created, so obvious breakage is
caught in seconds rather than on the CI round-trip. This must be:

1. **Version-controlled** — a hook living only in `.git/hooks` is invisible to the repo, unreviewable,
   and lost on fresh clones. It must be tracked and auditable like any other artifact.
2. **Consistent with CI** — the hook should run the *same* gate commands CI runs, so "green locally"
   predicts "green on CI".
3. **Non-blocking before its inputs exist** — `tests/` is currently empty; the hook must skip L3
   gracefully (mirroring CI's pre-C0 skip warnings) instead of failing when there is nothing to test.
4. **Non-destructive and overridable** — hooks must never mutate files or history; `--no-verify`
   remains available for genuine emergencies (discouraged, and such a commit should be flagged).

Git does not track `.git/hooks`, so the standard mechanism for a version-controlled hook is a
repo-tracked directory pointed at by `core.hooksPath`.

## Decision

1. **Repo-tracked `.githooks/` directory**, wired via `git config core.hooksPath .githooks`. The hook
   is therefore reviewable, diffable, and travels with the branch.
2. **`.githooks/pre-commit`** runs, in order, the two *fast* local gates and mirrors CI exactly:
   - **L1 Setup Gate:** `python scripts/setup_gate.py` (prefers `.venv/bin/python` when present).
   - **L3 Contract tests:** `pytest -q tests` **only if** `tests/*.py` exist; otherwise print a skip
     notice and pass (matches the CI `::warning::` behavior pre-C0).
   - The heavy **L5** notebook execution is **NOT** run in the hook (too slow for every commit); it
     stays in CI. The pre-commit hook is deliberately the *fast subset* of L5.
3. Any non-zero exit from a gate **aborts the commit** with a clear message.
4. **`core.hooksPath` is a local Git setting** (not committed). To make the hook effective on a fresh
   clone, a one-line bootstrap (`git config core.hooksPath .githooks`) is documented in the README and
   run once per clone. The hook *body* is version-controlled; only the activation pointer is local.
5. `--no-verify` is preserved for emergencies but is discouraged; a bypassed commit must be noted in
   `progress.md`.

## Consequences

**Positive**
- Broken deps / failing tests are caught in seconds, before the commit exists — fast feedback.
- The hook is version-controlled and reviewed, unlike an untracked `.git/hooks` script.
- Same commands as CI ⇒ local green is a meaningful predictor of CI green (defence in depth: hook →
  CI → C5 Colab).
- Graceful L3 skip means the hook is usable *now*, before any tests exist, and strengthens automatically
  once L3 units land.

**Negative / Risks**
- `core.hooksPath` must be set once per clone; if a collaborator forgets, their local hook is inactive
  (CI still catches them — the objective backstop). Mitigation: README bootstrap step.
- The hook runs the L1 gate on every commit (~sub-second); negligible but non-zero overhead.
- `--no-verify` can bypass the hook. Mitigation: discouraged by policy + logged; CI cannot be bypassed.
