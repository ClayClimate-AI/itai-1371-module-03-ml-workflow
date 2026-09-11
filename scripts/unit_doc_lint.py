#!/usr/bin/env python3
"""Invariant #2 — Per-Unit Documentation Gate (ADR 0005, amended).

Every per-unit record under docs/units/*.md must carry all ten required sections
(the original P-I-O-F four, plus the six ADR 0005 enrichment sections), each with real
content. A record missing a section, or with a header but nothing under it, fails the
gate.

Only checks files that exist -- nothing is retroactive. Cells committed before ADR 0005
(Cells 3 and 5) are grandfathered per that ADR and have no docs/units/ file.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UNITS_DIR = ROOT / "docs" / "units"
SKIP_NAMES = {"README.md", "TEMPLATE.md"}

REQUIRED_SECTIONS = [
    "Purpose",
    "Inputs",
    "Outputs",
    "Flow",
    "Expected Result",
    "Concept & Jargon",
    "Visual Sanity Check",
    "Journal Point",
    "Simplified Takeaway",
    "Sequence Mapping",
]


def section_bodies(text: str) -> dict[str, str]:
    """Map each '## Heading' to the text before the next '## ' heading."""
    parts = re.split(r"(?m)^##\s+", text)
    bodies: dict[str, str] = {}
    for part in parts[1:]:
        heading, _, body = part.partition("\n")
        bodies[heading.strip()] = body.strip()
    return bodies


def main() -> int:
    print("=" * 60)
    print("PER-UNIT DOCUMENTATION GATE (ADR 0005, invariant #2)")
    print("=" * 60)

    if not UNITS_DIR.exists():
        print("[unit-doc] docs/units/ not present; skipping (no enriched units yet).")
        return 0

    files = sorted(p for p in UNITS_DIR.glob("*.md") if p.name not in SKIP_NAMES)
    if not files:
        print("[unit-doc] no unit records in docs/units/ yet; skipping.")
        return 0

    failures: list[str] = []
    for f in files:
        bodies = section_bodies(f.read_text())
        for section in REQUIRED_SECTIONS:
            body = bodies.get(section)
            if body is None:
                failures.append(f"{f.relative_to(ROOT)}: missing '## {section}' section.")
            elif len(body) < 3:
                failures.append(f"{f.relative_to(ROOT)}: '## {section}' section is empty.")

    print(f"[unit-doc] checked {len(files)} unit record(s) in docs/units/")
    if failures:
        print("PER-UNIT DOCUMENTATION GATE: ❌ FAIL")
        for x in failures:
            print(f"  - {x}")
        return 1

    print("PER-UNIT DOCUMENTATION GATE: ✅ PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
