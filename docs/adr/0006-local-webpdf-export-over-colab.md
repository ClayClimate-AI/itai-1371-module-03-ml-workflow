# ADR 0006 — Local `nbconvert --to webpdf` Export Instead of Colab (C5)

- **Status:** Accepted
- **Date:** 2026-09-12
- **Deciders:** Pilot (Joseph Clay), Agent (Kiro)

## Context

`checkpoints.md`'s Pilot-Locked Constraints (2026-09-11) and `docs/STEP0_Initial_Contract.md`'s
resolved risks both locked the C5 Export Gate to Google Colab specifically: kernel restart →
run-all `[1..N]` → visual audit → headless PDF export, with Colab explicitly "not part of the
build/verify loop" otherwise. When the Pilot asked to convert the notebook to PDF and push it to
GitHub, they chose local `nbconvert` over that locked path.

Neither of `nbconvert`'s two PDF backends was available locally: no LaTeX (`pdflatex`/`xelatex`,
no `pandoc`) and no Playwright/Chromium (the modern `--to webpdf` backend). A LaTeX install is
heavy (a full TeX distribution); Playwright + a headless Chromium download is far lighter
(~270MB) and is `nbconvert`'s own recommended non-LaTeX path.

## Decision

1. **Local export replaces Colab for C5**, per the Pilot's explicit choice. This is a genuine
   contract change (checkpoints.md's Constraint 2), not a silent substitution — logged here and as
   a Contract Drift in `progress.md`.
2. **Toolchain:** `playwright` installed into `.venv` (`pip install playwright`), Chromium fetched
   via `playwright install chromium`. Export command: `jupyter nbconvert --to webpdf
   Module_03_Lab_Exercise.ipynb` — **no `--execute` flag**. This renders the notebook's
   *already-saved* cell outputs (from the Pilot's own prior runs) to PDF; it does not re-run any
   cell, so it doesn't touch the "Agent never runs the payload notebook" rule.
3. **What's lost vs. Colab:** the original rationale for Colab was an independent, objective
   re-execution environment (parallel to CI). Local `webpdf` export does not re-verify the
   notebook runs top-to-bottom on a clean environment — that guarantee still comes from CI's
   `nbconvert --to notebook --execute` step (`.github/workflows/ci.yml`), which is unaffected by
   this ADR and remains the objective re-run proof. This ADR only changes *how the final PDF
   artifact is produced*, not how "does it run clean" is proven.
4. **Visual audit still applies**: before the PDF is pushed, the Pilot reviews the rendered output
   for clipping/margin issues per the C5 checklist — the Agent generates the file, the Pilot signs
   off on it looking right.

## Consequences

**Positive**
- No manual Colab upload/download round-trip; the export happens in the same environment that's
  been running the whole build.
- Lightweight toolchain (~270MB Chromium vs. a multi-GB LaTeX distribution).
- Dry-run confirmed working before any real export was attempted: a clean 768KB PDF from the
  in-progress notebook, no errors.

**Negative / Risks**
- Loses Colab's "different environment" cross-check for the final artifact specifically (CI still
  covers "does it run clean," just not "does it export clean on another platform").
- `--to webpdf`'s image-alt-text warnings (3 images, expected — the matplotlib figures have no alt
  text) are cosmetic and don't block export; not an accessibility requirement this project scoped.
