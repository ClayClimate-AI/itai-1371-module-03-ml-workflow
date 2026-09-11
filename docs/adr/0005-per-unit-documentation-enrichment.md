# ADR 0005 — Per-Unit Documentation Enrichment & Four New Invariants

- **Status:** Accepted
- **Date:** 2026-09-11
- **Deciders:** Pilot (Joseph Clay), Agent (Kiro)

## Context

The Pilot supplied an expanded per-cell checklist (11 items: P-I-O-F, Assertions/Test, Expected
Result, Human Test & Verification, Concept & Methodology, Visual Sanity Check, Jargon, Journal
Point, 10th-grade Conclusion, Sequence Mapping, Atomic Commit) plus three claimed "professional
gaps." An audit against the source *Ultimate Cell-by-Cell Master Blueprint* PDF and this repo's
implementation found:

- Two of the three claimed gaps are **not** gaps: the Failure Gate + ADRs (§2.4) and objective
  CI/CD verification (§3.3, Layer 5) are already normative in the blueprint and already
  implemented here (`docs/adr/000{1,2,3}-*.md`, `.github/workflows/ci.yml`, `.githooks/pre-commit`).
- One item is a genuine sharpening: explicitly classifying a failure as **Code Failure** (plan was
  right, implementation was wrong) vs. **Spec Failure** (implementation matched the plan, the plan
  was wrong) before acting, which the blueprint's Amendment Rule (§2.2) implies but never forces.
- Several items (Expected Result, Concept/Jargon, Journal Point, Sequence Mapping) are useful
  pedagogical/reporting scaffolding with no equivalent in the source blueprint.
- The pasted checklist also silently **dropped** the Amendment Rule (§2.2), the Layer 3
  (`tests/`) vs. Layer 4 (inline asserts) distinction, and C4's verbatim-transcript requirement —
  and it misdescribes the local pre-commit hook as scanning for "sensitive data leakage," which is
  not what ADR 0003 implements (L1 Setup Gate + L3 pytest only).
- A separate audit of the live repo found the underlying reason enrichment is needed in the first
  place: `progress.md` recorded Cells 3 and 5 as "Pilot-verified ✅ ran as `[2]`" while the
  *committed* notebook shows `execution_count: null` and empty `outputs` for both — a real proof
  gap the blueprint's own mandate ("a green checkmark is not proof; a contract is proof") exists to
  prevent.

## Decision

1. **The PDF blueprint remains the sole normative contract.** Gates C0–C5, Layers L0–L5, the
   Amendment Rule, spec precedence, and the L3/L4 distinction are unchanged. Nothing here
   supersedes them.
2. **C1 P-I-O-F records gain six required fields** *(amended 2026-09-11, see Amendment below)*,
   captured per-unit in `docs/units/*.md` alongside the original four: **Expected Result**,
   **Concept & Jargon**, **Visual Sanity Check**, **Journal Point**, **Simplified Takeaway**,
   **Sequence Mapping**. These are documentation, not new Pilot sign-off gates — they ride on the
   existing C1 approval. `docs/units/TEMPLATE.md` is the required skeleton for each new unit going
   forward. Cells 3 and 5 are **backfilled**, not grandfathered *(amended 2026-09-11, see second
   Amendment below)* — Sequence Mapping and the Journal Point trail are inherently chained, so
   starting the enrichment layer at Cell 6 would leave a hole at the beginning of the chain rather
   than a clean start.
3. **C3 failure entries must open with an explicit classification** — `**Code Failure**` or
   `**Spec Failure**` — before any resolution or ADR reference, per the Amendment Rule's existing
   "a missing rule is a contract failure, not a code failure" language.
4. **Correction for the record:** the local pre-commit hook (ADR 0003) does not scan for sensitive
   data; it runs L1 Setup Gate + L3 pytest only. Any future hook change to add secret-scanning is a
   separate ADR, not implied by this one.
5. **Four invariants are added to the guardrail ladder**, enforced in `.githooks/pre-commit` and
   (where applicable) CI, to make the proof gap structurally impossible going forward:

   | # | Invariant | Script | Layer |
   | - | --- | --- | --- |
   | 1 | **Execution-Proof Gate** — a notebook cell referenced as "Pilot-verified" in `progress.md`'s Unit Log must have a non-null `execution_count` and non-empty `outputs` in the committed notebook. | `scripts/execution_proof_gate.py` | L4 |
   | 2 | **Per-Unit Documentation Gate** — every `docs/units/*.md` record must contain all ten required sections, none empty. | `scripts/unit_doc_lint.py` | L2 |
   | 3 | **Failure-Classification Gate** — every entry under `progress.md`'s Failure & Amendment Logs must lead with `**Code Failure**`, `**Spec Failure**`, or `**Contract Drift**` (amended 2026-09-11: the original version only accepted the first two, which would have wrongly rejected a legitimate Contract Drift entry). | `scripts/failure_log_lint.py` | C3 |
   | 4 | **Push-Before-Verified Gate** — any commit hash `progress.md` marks Pilot-verified/Committed(C2) must be an ancestor of `origin/<branch>`. | `scripts/push_verified_gate.py` | L5 |

   Invariants 1–3 also run in CI (`.github/workflows/ci.yml`) as an objective backstop. Invariant 4
   is local-only by nature (it checks against the local remote-tracking ref; it is meaningless
   inside the CI runner that just checked out the pushed commit).

## Consequences

**Positive**
- The exact failure mode found in this audit (claiming verification the artifact doesn't show)
  now fails the commit instead of silently entering the trail.
- Per-unit records (`docs/units/`) become richer inputs to the final report and to C4, without
  adding a new human gate or contradicting the existing C1/C2/C3 vocabulary.
- The two mislabeled "gaps" are corrected in the written record so future sessions don't re-treat
  already-implemented controls as missing.

**Negative / Risks**
- More files to maintain per unit (`docs/units/<NN>-<slug>.md`). Mitigated by `TEMPLATE.md`.
- Backfilling Cells 3/5 means their P-I-O-F is written *after* the code, inverting the normal
  C1-before-code order — flagged explicitly in each backfilled file rather than presented as if it
  were written in advance.
- Invariant 4 depends on the local remote-tracking ref being current; a stale `origin/*` (no
  `git fetch` since the last push by someone else) could pass or fail incorrectly. Mitigated by
  documenting `git fetch` as a Resume Protocol step.
- Four more checks on every commit (~sub-second each, stdlib-only, no new dependencies).

## Amendment (2026-09-11)

A re-check against the Pilot's original pasted checklist found two more sections that had been
dropped rather than deliberately excluded:

- **Visual Sanity Check** — a specific, checkable correctness claim distinct from Expected Result
  (e.g., "the scaler was fit only on `X_train`, never `.fit_transform()`'d on `X_test`") — the
  thing that catches a subtle mistake a merely-plausible-looking output would not.
- **Simplified Takeaway** (the Pilot's naming; the source checklist called this the "10th-Grade
  Takeaway" — renamed here since "simplified" describes the content without a specific grade-level
  claim) — a plain-language, no-jargon summary of the unit.

Both are added as required `docs/units/*.md` sections (now ten total) and to
`scripts/unit_doc_lint.py`'s `REQUIRED_SECTIONS`. `docs/units/TEMPLATE.md` updated accordingly.
No other part of this ADR changes; Decision item 2 above reflects the amended field count.

## Amendment 2 (2026-09-11) — Backfill instead of grandfather

Pilot observed that Sequence Mapping and the Journal Point trail are cumulative: Cell 6's "Where
we were" has nothing to point at if Cell 5 has no record, and a Journal Point trail feeding C4
that starts at Cell 6 has a hole at the beginning rather than a clean start. Grandfathering Cells
3 and 5 (original Decision item 2) would have started the enrichment layer in the middle of the
sequence instead of at its actual beginning.

**Revised decision:** `docs/units/0003-imports-env-check.md` and `docs/units/0005-load-explore-wine.md`
are backfilled — written from the already-committed code and captured outputs, after the fact,
and explicitly labeled retroactive in each file's header (since normal C1 order is P-I-O-F
*before* code, not after). Both require Pilot review/approval before Cell 6 work begins, the same
standing the original C1 approval would have had. No other units are backfilled beyond these two;
this is a one-time catch-up to reach a real starting point, not a general retroactive-documentation
policy.
