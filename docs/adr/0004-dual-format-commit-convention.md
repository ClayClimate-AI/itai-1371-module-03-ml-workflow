# ADR 0004 — Dual-Format Commit Convention (Conventional Commits + C-Gate Tag)

- **Status:** Accepted
- **Date:** 2026-09-11
- **Deciders:** Pilot (Joseph Clay), Agent (Kiro)

## Context

The build uses the blueprint's checkpoint vocabulary (C0–C5), and early commits were tagged with that
vocabulary alone:

- `e5b1a4d` — `C2: Pre-flight setup through C0 (contract, specs, gates, CI, living state)`
- `31eac15` — `C2: Cell 3 (Part 2 imports + L4 env assertion) — Pilot-verified [2]`

This checkpoint tag is valuable — it maps each commit to a gate in the protocol and to the Unit Log.
However it is **not** a [Conventional Commits](https://www.conventionalcommits.org) message: that spec
requires a leading `type(scope): description`, where `type` is drawn from a fixed set (`feat`, `fix`,
`docs`, `chore`, `test`, `refactor`, `ci`, `build`, …). A Conventional-Commits linter (e.g. commitlint)
would reject a message beginning with `C2:`.

We want both properties at once: the machine-parseable Conventional prefix (tooling, changelog,
semantic intent) **and** the human/process-facing checkpoint tag (which gate, which verified counter).

## Decision

1. **Adopt a dual-format commit message going forward:**

   ```
   <type>(<scope>): <subject>  [C<gate>, verified [<n>]]
   ```

   - `<type>` — a Conventional Commits type: `feat`, `fix`, `docs`, `test`, `chore`, `ci`, `build`,
     `refactor`, `perf`, `style`.
   - `<scope>` — the unit under change (e.g. `cell5`, `hooks`, `adr`, `ci`).
   - `<subject>` — imperative, concise.
   - `[C<gate>, verified [<n>]]` — the protocol checkpoint tag: which gate this commit satisfies and,
     for a Pilot-verified notebook unit, the execution counter `[n]`. The `verified [n]` part is
     included only when a cell was actually run by the Pilot; process/tooling commits use just `[C<gate>]`.

   **Examples**
   - `feat(cell5): load Wine into DataFrame + L4 integrity check  [C2, verified [3]]`
   - `chore(hooks): add repo-tracked pre-commit running L1+L3  [C2]`
   - `docs(adr): ADR 0003/0004 — hooks + commit convention  [C2]`

2. **Existing history is left intact.** Commits `e5b1a4d` and `31eac15` keep their `C2:`-style
   messages; rewording would rewrite history (hash changes, force-push) for no functional gain. The
   convention applies **from the next commit onward**.

3. **Not machine-enforced (yet).** No commitlint gate is added now; the convention is a documented
   discipline. If desired later, a `commit-msg` hook can enforce it (a natural companion to ADR 0003).

## Consequences

**Positive**
- Messages are simultaneously Conventional-Commits-valid *and* carry the protocol checkpoint/verified
  metadata — no information lost, tooling-compatible.
- Scope makes the affected unit explicit; grep/changelog tooling works.
- History remains immutable and honest (no retroactive rewriting).

**Negative / Risks**
- Two conventions in one line is slightly more verbose. Accepted: the extra signal is worth it.
- Mixed history (old `C2:` style + new dual format) until enough new commits accumulate. Documented
  here so the transition point is auditable.
- Not enforced by a hook yet, so a malformed message is possible. Mitigation: Agent authors commit
  messages to this format; optional `commit-msg` hook can be added if drift appears.
