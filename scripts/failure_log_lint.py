#!/usr/bin/env python3
"""Invariant #3 — Failure-Classification Gate (ADR 0005, corrected).

The blueprint's own Living State format (§3.1) defines TWO valid shapes for this section,
not one:
    - [Failure Symptom] | [ADR Ref] | [Resolution]
    - [Contract Drift]  | [C0 Amendment Date]

Every entry must open with one of three tags: **Code Failure** or **Spec Failure** (for a
Failure Symptom entry -- the plan was right and the implementation was wrong, or vice
versa) or **Contract Drift** (for a scope/DoD amendment that isn't a failure at all, e.g.
the Pilot deliberately expanding scope). An earlier version of this script only accepted
the first two, which would have wrongly rejected a legitimate Contract Drift entry --
found and fixed when the Learning-Curve scope amendment needed logging.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROGRESS = ROOT / "progress.md"

SECTION_RE = re.compile(
    r"^##\s+Failure\s*&\s*Amendment Logs\s*$(.*?)(?=^##\s|\Z)",
    re.MULTILINE | re.DOTALL,
)
PLACEHOLDER_RE = re.compile(r"^\(none yet\)$", re.IGNORECASE)
TAG_RE = re.compile(r"^\*\*(Code Failure|Spec Failure|Contract Drift)\*\*", re.IGNORECASE)


def main() -> int:
    print("=" * 60)
    print("FAILURE-CLASSIFICATION GATE (ADR 0005, invariant #3)")
    print("=" * 60)

    if not PROGRESS.exists():
        print("[failure-log] progress.md not found; skipping.")
        return 0

    text = PROGRESS.read_text()
    m = SECTION_RE.search(text)
    if not m:
        print("[failure-log] no 'Failure & Amendment Logs' section found; skipping.")
        return 0

    body = m.group(1)
    entries = [
        ln.strip().lstrip("-").strip()
        for ln in body.splitlines()
        if ln.strip().startswith("-")
    ]
    entries = [e for e in entries if e and not PLACEHOLDER_RE.match(e)]

    print(f"[failure-log] {len(entries)} logged entr{'y' if len(entries) == 1 else 'ies'}")
    failures = [e for e in entries if not TAG_RE.match(e)]

    if failures:
        print("FAILURE-CLASSIFICATION GATE: ❌ FAIL")
        for e in failures:
            print(f"  - Missing leading **Code Failure**/**Spec Failure**/**Contract Drift** tag: {e[:80]}")
        return 1

    print("FAILURE-CLASSIFICATION GATE: ✅ PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
