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
2. **C1 P-I-O-F records gain four required fields**, captured per-unit in `docs/units/*.md`
   alongside the original four: **Expected Result**, **Concept & Jargon**, **Journal Point**,
   **Sequence Mapping**. These are documentation, not new Pilot sign-off gates — they ride on the
   existing C1 approval. `docs/units/TEMPLATE.md` is the required skeleton for each new unit going
   forward; Cells 3 and 5 (pre-dating this ADR) are grandfathered and not retroactively required to
   have one.
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
   | 2 | **Per-Unit Documentation Gate** — every `docs/units/*.md` record must contain all eight required sections, none empty. | `scripts/unit_doc_lint.py` | L2 |
   | 3 | **Failure-Classification Gate** — every entry under `progress.md`'s Failure & Amendment Logs must lead with `**Code Failure**` or `**Spec Failure**`. | `scripts/failure_log_lint.py` | C3 |
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
- More files to maintain per unit (`docs/units/<NN>-<slug>.md`). Mitigated by `TEMPLATE.md` and by
  the gate only enforcing files that exist — nothing retroactive.
- Invariant 4 depends on the local remote-tracking ref being current; a stale `origin/*` (no
  `git fetch` since the last push by someone else) could pass or fail incorrectly. Mitigated by
  documenting `git fetch` as a Resume Protocol step.
- Four more checks on every commit (~sub-second each, stdlib-only, no new dependencies).
