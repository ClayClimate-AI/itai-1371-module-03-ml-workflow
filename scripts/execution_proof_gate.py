#!/usr/bin/env python3
"""Invariant #1 — Execution-Proof Gate (ADR 0005).

A notebook cell may not be recorded as Pilot-verified in progress.md unless the
*committed* .ipynb actually carries proof it was run: a non-null execution_count and at
least one captured output. This closes the gap found in audit — progress.md claimed
Cells 3 and 5 were "Pilot-verified ran as [2]" while the committed notebook showed
execution_count: null and outputs: [] for both.

Scope: only checks cells referenced by a "Cell <N>" unit in progress.md's Unit Log whose
row contains "pilot-verified" (case-insensitive). Units not yet claimed as verified are
not checked here -- this gate catches false claims, not incomplete work.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROGRESS = ROOT / "progress.md"
NOTEBOOK = ROOT / "Module_03_Lab_Exercise.ipynb"

UNIT_ROW_RE = re.compile(r"Cell\s+(\d+)", re.IGNORECASE)


def verified_cell_indices() -> set[int]:
    if not PROGRESS.exists():
        return set()
    indices: set[int] = set()
    for line in PROGRESS.read_text().splitlines():
        if "|" not in line or "pilot-verified" not in line.lower():
            continue
        m = UNIT_ROW_RE.search(line)
        if m:
            indices.add(int(m.group(1)))
    return indices


def main() -> int:
    print("=" * 60)
    print("EXECUTION-PROOF GATE (ADR 0005, invariant #1)")
    print("=" * 60)

    if not NOTEBOOK.exists():
        print("[exec-proof] notebook not found; skipping.")
        return 0

    claimed = verified_cell_indices()
    if not claimed:
        print("[exec-proof] no 'Pilot-verified' Cell-N rows in progress.md; skipping.")
        return 0

    nb = json.loads(NOTEBOOK.read_text())
    cells = nb.get("cells", [])
    failures: list[str] = []

    print(f"[exec-proof] cells claimed Pilot-verified in progress.md: {sorted(claimed)}")
    for idx in sorted(claimed):
        if idx >= len(cells):
            failures.append(f"Cell {idx} referenced in progress.md but does not exist in the notebook.")
            continue
        cell = cells[idx]
        if cell.get("cell_type") != "code":
            failures.append(f"Cell {idx} is marked Pilot-verified but is not a code cell.")
            continue
        exec_count = cell.get("execution_count")
        outputs = cell.get("outputs") or []
        if exec_count is None:
            failures.append(
                f"Cell {idx}: logged Pilot-verified but execution_count is null "
                f"in the committed notebook -- no proof it ran."
            )
        if not outputs:
            failures.append(
                f"Cell {idx}: logged Pilot-verified but has no captured outputs "
                f"in the committed notebook."
            )

    if failures:
        print("EXECUTION-PROOF GATE: ❌ FAIL")
        for f in failures:
            print(f"  - {f}")
        print(
            "\nFix: re-run the affected cell(s) in your kernel, save the notebook WITH "
            "outputs, then re-stage before committing. Do not edit progress.md to claim "
            "verification the artifact itself doesn't show."
        )
        return 1

    print("EXECUTION-PROOF GATE: ✅ PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
