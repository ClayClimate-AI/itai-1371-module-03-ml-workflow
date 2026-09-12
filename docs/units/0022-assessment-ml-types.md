# Cell 22 — Part 8: Assessment — Identify the ML Type

- **C1 approved:** 2026-09-11 (Pilot approved the P-I-O-F, including two added L4 assertions, before code was prepared)
- **C2 commit:** pending — awaiting Pilot run + save

## Purpose

Self-check comprehension of supervised/unsupervised/reinforcement learning by classifying 5
real-world scenarios, scored automatically against known-correct answers.

## Inputs

None from prior cells — self-contained scenario/answer lists (already correctly filled in the
template; no TODO here, unlike Cell 20).

## Outputs

Printed per-scenario correctness (✅/❌ + your answer vs. correct), a final `Score: X/5 (Y%)` line.

## Flow

1. Define `scenarios` (5 real-world descriptions).
2. Define `your_answers` and `correct_answers` (5 classifications each).
3. **L4 assertion** (added at C1): `len(scenarios) == len(your_answers) == len(correct_answers)
   == 5` — input counts align.
4. Loop, compare, tally `score`, print status per scenario.
5. **L4 assertion** (added at C1): `score == 5` — directly formalizes `docs/STEP0_Initial_Contract.md`
   DoD item 6 ("Assessment answers 5/5") as something the code proves, not just eyeballs.
6. Print final score.

## Expected Result

Five ✅ lines (each showing matching "Your answer" / "Correct" text), ending in `Score: 5/5 (100%)`
— no exceptions, at whatever `execution_count` follows `[14]`.

## Concept & Jargon

Reinforces the three learning-type definitions from Part 1 (start of the notebook) by testing
recognition against concrete scenarios, rather than just restating definitions.

## Visual Sanity Check

All 5 lines must show `✅`, none `❌`; the final line must read exactly `5/5 (100%)` — the DoD
assertion above makes this provable, not just visible.

## Journal Point

*Pre-written insight for the final report:* "This cell is where the project's own Definition of
Done — 'Assessment answers 5/5' — stopped being something I'd verify by reading a printed score
and became something the code asserts outright. Same principle as every other L4 check in this
build: a claim only counts once it's provable."

## Simplified Takeaway

This is a mini quiz checking whether we can tell apart the three types of machine learning from
real examples, and it grades itself automatically.

## Sequence Mapping

- **Where we were:** Cell 20 tested whether smarter feature choice matches the main model.
- **Where we are:** Confirm understanding of the three ML learning types via a scored quiz.
- **Where we are going:** Cell 25 — your written reflection, including the "Questions for further
  exploration" field flagged from Attempt 1's feedback.
