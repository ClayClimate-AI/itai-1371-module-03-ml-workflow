# ADR 0002 — Python Version Strategy

- **Status:** Accepted
- **Date:** 2026-09-11
- **Deciders:** Pilot (Joseph Clay), Agent (Kiro)

## Context

Three different Python versions are in play:

| Surface | Version | Source |
| --- | --- | --- |
| Local Bubble `.venv` | **3.14.6** | System Python used to create the venv |
| CI runner | **3.12** (pinned) | `.github/workflows/ci.yml` |
| Notebook metadata | **3.8.5** (declared) | `Module_03_Lab_Exercise.ipynb` `language_info.version` |

The Layer 1 Setup Gate **passed** on 3.14.6: all declared dependencies
(`pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`) install and import, and `load_wine`
returns the expected 178×13 / 3-class dataset. The notebook's declared `3.8.5` is a historical
artifact of whatever kernel last saved the file; it is **not** a hard requirement of the lab.

The final graded artifact (Deliverable 1 PDF) will be produced from **Google Colab** at the C5 Export
Gate, whose runtime is currently Python 3.11/3.12-class — not 3.8.5 and not 3.14.

The risk of *not* deciding: silent version drift between local proof, CI proof, and the Colab export
could produce "works here, breaks there" behavior — exactly the silent failure the Zero-Defect
architecture exists to prevent.

## Decision

1. **Local Bubble stays on Python 3.14.6.** It passed the Setup Gate; no reason to downgrade.
2. **CI is pinned to Python 3.12** as the objective, reproducible reference environment. 3.12 is a
   stable, widely-supported scientific-Python baseline and is close to the Colab runtime.
3. **The notebook's declared `3.8.5` is treated as non-binding metadata**, not a constraint. We do
   not force the kernel to 3.8.5.
4. **Colab (C5) is the delivery runtime.** The notebook must execute cleanly on Colab's default
   Python; the CI 3.12 pin is chosen to approximate that so a green CI is a meaningful predictor of a
   clean Colab run.
5. The code uses only version-agnostic APIs of the declared libraries (no 3.14-only or 3.8-only
   syntax), so all three runtimes remain compatible.

## Consequences

**Positive**
- Setup Gate already green locally; no rework.
- CI 3.12 is a realistic proxy for the Colab delivery runtime → CI green ≈ Colab clean.
- Version assumptions are now explicit and auditable rather than silent.

**Negative / Risks**
- Three distinct versions still exist; if any library later exposes a version-specific behavior, it
  could pass locally/CI yet differ on Colab. Mitigation: the L5 CI step executes the full notebook
  headlessly, and the C5 gate re-runs it on Colab with a full kernel restart — two independent proofs.
- If a genuine incompatibility appears, revisit this ADR (supersede with a pinned single version).
