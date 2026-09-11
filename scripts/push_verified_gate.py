#!/usr/bin/env python3
"""Invariant #4 — Push-Before-Verified Gate (ADR 0005).

progress.md may not mark a unit's commit as Pilot-verified / Committed (C2) until that
commit actually exists on origin -- otherwise the "verified" claim only has local,
subjective standing and CI (the objective L5 backstop) has never run against it.

Checks every commit hash referenced in a "Pilot-verified" / "Committed (C2)" line of
progress.md against origin/<current-branch>, using the local remote-tracking ref. This is
local-only by nature: run `git fetch` first for an up-to-date answer, and it is
meaningless to run inside CI (which just checked out the pushed commit itself).
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROGRESS = ROOT / "progress.md"

HASH_RE = re.compile(r"`([0-9a-f]{7,40})`")


def run(cmd: list[str]) -> tuple[int, str]:
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()


def current_branch() -> str | None:
    rc, out = run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    return out if rc == 0 else None


def main() -> int:
    print("=" * 60)
    print("PUSH-BEFORE-VERIFIED GATE (ADR 0005, invariant #4)")
    print("=" * 60)

    if not PROGRESS.exists():
        print("[push-verified] progress.md not found; skipping.")
        return 0

    branch = current_branch()
    if not branch:
        print("[push-verified] could not resolve current branch; skipping.")
        return 0

    remote_ref = f"origin/{branch}"
    rc, _ = run(["git", "rev-parse", "--verify", remote_ref])
    if rc != 0:
        print(
            f"[push-verified] {remote_ref} does not exist locally (branch never pushed) "
            f"-- skipping. Push before recording any unit as Pilot-verified."
        )
        return 0

    failures: list[str] = []
    checked: set[str] = set()
    for line in PROGRESS.read_text().splitlines():
        low = line.lower()
        if "pilot-verified" not in low and "committed (c2)" not in low:
            continue
        for h in HASH_RE.findall(line):
            if h in checked:
                continue
            checked.add(h)
            rc, _ = run(["git", "rev-parse", "--verify", h])
            if rc != 0:
                continue  # not a resolvable commit in this repo; skip silently
            rc, _ = run(["git", "merge-base", "--is-ancestor", h, remote_ref])
            if rc != 0:
                failures.append(h)

    print(f"[push-verified] checked {len(checked)} referenced commit(s) against {remote_ref}")
    if failures:
        print("PUSH-BEFORE-VERIFIED GATE: ❌ FAIL")
        for h in failures:
            print(f"  - Commit {h} is logged as verified/committed but is not on {remote_ref}.")
        print("\nFix: git push, then re-stage progress.md before committing this claim.")
        return 1

    print("PUSH-BEFORE-VERIFIED GATE: ✅ PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
