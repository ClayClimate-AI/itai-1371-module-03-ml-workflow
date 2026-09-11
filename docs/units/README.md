# Per-Unit Records

Per ADR 0005, every notebook unit built **after** 2026-09-11 gets one record here:
`docs/units/<NN>-<slug>.md`, where `<NN>` is the notebook cell index (matching the
"Cell N" naming used in `progress.md`'s Unit Log).

Copy `TEMPLATE.md`, fill in all ten sections before requesting C1 approval, and keep
the file even after the unit is committed — it is durable documentation, not a scratch
pad. `scripts/unit_doc_lint.py` (wired into the pre-commit hook and CI) fails the commit
if any section is missing or empty.

Cells 3 and 5 pre-date this ADR and are grandfathered — they have no file here, and the
lint does not require one for them.
