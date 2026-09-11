#!/usr/bin/env python3
"""Layer 1 — Setup Gate.

Blueprint contract: exit 0 ONLY if all real dependencies are present and the environment is sane.
Performs:
  1. Dependency diff  — packages imported by the notebook vs. those declared in requirements.txt.
  2. Presence check   — every declared dependency actually imports in this environment.
  3. Env integrity    — Python version + Subject data availability (load_wine).

This is SYSTEM tooling, not the Subject notebook; running it does not violate the
"Agent never runs cells" rule (which governs the payload notebook, executed only by the Pilot).
"""
from __future__ import annotations

import ast
import importlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK = ROOT / "Module_03_Lab_Exercise.ipynb"
REQS = ROOT / "requirements.txt"

# Map import name -> distribution name (where they differ)
IMPORT_TO_DIST = {
    "sklearn": "scikit-learn",
    "cv2": "opencv-python",
}
# Standard-library modules we should never flag as missing deps
STDLIB_ALLOW = {"os", "sys", "json", "math", "random", "time", "pathlib", "itertools", "collections"}


def notebook_imports(nb_path: Path) -> set[str]:
    """Extract top-level imported module names from all code cells."""
    if not nb_path.exists():
        return set()
    nb = json.loads(nb_path.read_text())
    names: set[str] = set()
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        src = "".join(cell.get("source", []))
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for n in node.names:
                    names.add(n.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom) and node.module:
                names.add(node.module.split(".")[0])
    return names


def declared_dists() -> set[str]:
    if not REQS.exists():
        return set()
    dists = set()
    for line in REQS.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        for sep in (">=", "==", "<=", "~=", ">", "<"):
            if sep in line:
                line = line.split(sep)[0]
                break
        dists.add(line.strip().lower())
    return dists


def main() -> int:
    failures: list[str] = []
    notes: list[str] = []

    print("=" * 60)
    print("LAYER 1 — SETUP GATE")
    print("=" * 60)

    # 3. Environment integrity — Python version
    py = sys.version_info
    print(f"[env] Python {py.major}.{py.minor}.{py.micro}")
    notes.append(f"Python {py.major}.{py.minor}.{py.micro}")

    # 1. Dependency diff
    imports = notebook_imports(NOTEBOOK)
    third_party = {m for m in imports if m not in STDLIB_ALLOW}
    declared = declared_dists()
    print(f"[diff] notebook third-party imports: {sorted(third_party)}")
    print(f"[diff] declared in requirements.txt : {sorted(declared)}")

    for mod in sorted(third_party):
        dist = IMPORT_TO_DIST.get(mod, mod).lower()
        if dist not in declared:
            failures.append(f"Imported '{mod}' not declared in requirements.txt (expected '{dist}')")

    # 2. Presence check — declared deps must import
    print("[deps] import check:")
    for mod in sorted(third_party):
        try:
            importlib.import_module(mod)
            print(f"       OK   {mod}")
        except Exception as exc:  # noqa: BLE001
            failures.append(f"Dependency '{mod}' failed to import: {exc}")
            print(f"       FAIL {mod} — {exc}")

    # 3b. Subject data availability
    try:
        from sklearn.datasets import load_wine

        d = load_wine()
        n, f = d.data.shape
        assert n == 178 and f == 13, f"unexpected wine shape ({n},{f})"
        print(f"[data] load_wine OK — {n} samples x {f} features, classes={list(d.target_names)}")
    except Exception as exc:  # noqa: BLE001
        failures.append(f"Subject data check failed: {exc}")
        print(f"[data] FAIL — {exc}")

    print("-" * 60)
    if failures:
        print("SETUP GATE: \u274c FAIL")
        for x in failures:
            print(f"  - {x}")
        return 1
    print("SETUP GATE: \u2705 PASS")
    print("  notes:", "; ".join(notes))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
