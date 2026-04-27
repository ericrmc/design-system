---
session: 079
title: Substrate vertical slice — assessment
date: 2026-04-27
engine_version_at_open: engine-v16
mode: self-development
---

# Assessment

## State at open

Engine-v16 active. 078 closed yesterday with twelve design commitments; D-11 hands 079 a vertical-slice implementation plan with seven concrete deliverables and an explicit "must NOT" list. The engine surface is 430 non-blank lines (breaching D-10's 400-line budget by 30); D-7's cut is 079's first action and is what brings the surface back under budget at engine-v17.

The substrate (`state/`), the `selvedge` CLI, and `state/migrations/001-initial.sql` do not yet exist. `tools/validate.sh` is the engine-v16 minimal file-presence checker; D-11 step 4 wires its successor to call `selvedge validate --precommit`.

Available tooling on the operator machine: SQLite 3.51.0, Python 3.14.4, jq. The CLI will be Python (3.14) calling the `sqlite3` stdlib module — no external dependencies, matches the boring-substrate spirit of D-9.

## Read

For 079 (per `prompts/development.md` §Read and the D-11 handoff):
- `provenance/078-design-commitments/02-decisions.md` and `03-close.md` — the binding contract for 079.
- `specifications/methodology.md`, `specifications/workspace.md`, `specifications/engine-manifest.md` — the targets of the D-7 cut.
- `tools/validate.sh` — the wrapper to be re-pointed.
- Engine-v16 active spec for the line-count baseline (430 non-blank).

Not read (consciously, per `development.md` §Read "you do not need to read the full provenance back-catalogue"):
- Pre-restart provenance under `archive/pre-restart/` and the per-OI files under `open-issues/`. None bear on the substrate vertical slice. The OI index was scanned to confirm no engine-v16-blocking item is open; OI-016 hybrid-resolved state and OI-019's deliberation pattern issue are both at active-monitor cadence and do not constrain 079.
- 077 perspectives or deliberation. 078's decisions consolidate them.
- `engine-feedback/INDEX.md`. Per 078 honest-limit-8, the 076 close marked all open EF records rejected by engine-v16 supersession; 079's narrow scope does not need this surface.

## Agenda

The seven D-11 deliverables in order, with explicit checkpoints:

1. **Apply D-7 cut.** Six surgical edits to `methodology.md`, `workspace.md`, `engine-manifest.md`. Archive removed sections to `archive/specifications/`. Bump `engine-manifest.md` to engine-v17. Re-count non-blank lines and confirm under 400.
2. **Author `state/migrations/001-initial.sql`.** Implement D-1's three-mode storage (S1 cells / S3 tuples / S2 files) across the 16-table schema named in D-10's calibration. Encode T-01..T-16 as triggers, CHECK constraints, UNIQUE indexes, or application-layer parses (recording in the migration which mechanism each refusal uses).
3. **Implement `selvedge` CLI.** Python 3 single file at `selvedge/cli.py` with shim `bin/selvedge`. Subcommands: `init`, `id-allocate`, `submit`, `validate --precommit`, `subtract-eligibility`, `recover`. Single-writer (`BEGIN IMMEDIATE`); structured errors (`E_WRITE_BUSY`, `E_REFUSAL_T<NN>`, `E_STALE_SCHEMA`, `E_SCHEMA_MIGRATING`); idempotency keys per D-9.
4. **Wire `tools/validate.sh`.** Append a final stage that, when `state/selvedge.sqlite` exists, invokes `bin/selvedge validate --precommit` and exits non-zero on its failure.
5. **Round-trip test.** Script at `state/tests/round_trip.sh`. Open S079 → write decision (1 alt + 1 ref) → close → reopen → expect T-06 refusal on UPDATE.
6. **Concurrency falsification trial.** Script at `state/tests/concurrency.sh`. 16 parallel submits with injected sleep, one killed at SIGKILL mid-transaction. Expected outcomes per D-9; record actual outcomes in close.
7. **Close.** Write `02-decisions.md` recording trial results, calibration parameters chosen, any engine_feedback raised. Write `03-close.md`. Commit + push.

## Multi-agent deliberation

**None.** Per 078 honest-limit-2: "079 picks its own ratio against the same rule (and may not need a deliberation at all if the implementation surface is unambiguous, which D-11 is structured to ensure)." D-11 is unambiguous. The work is implementation-against-contract, not design. If implementation reveals a contract ambiguity (a refusal that cannot be implemented as specified per D-3 §Open), 079 records it as engine_feedback and 080+ deliberates the resolution; this is graceful-degradation per D-11 §Open.

The session will record decisions for the calibration parameters that D-9 §Open and other "Open" sections defer to 079: `busy_timeout`, retry budget, lease-expiry interval, idempotency-key composition, exact-trigger-vs-CHECK-vs-application-parse choice per refusal.

## Close-time review

**Not run as a separate-agent audit.** Per 078 §Honest limits §3, the reviewer mechanism is in redesign scope per D-7's cut of `methodology.md` §When to review at close. 079 elects not to retrospectively audit 078 because the substrate work itself is the audit: if 078's decisions are implementable, the substrate lands; if they are not, the engine_feedback rows produced are the audit's findings.

The post-cut engine-v17 will not contain the close-time-review specification at all (D-7 step 1). The transitional sentence "Close-time review is superseded until the substrate distinguishes prevention from audit; D-2 conditional re-introduction governs" replaces the section.

## Validation

Workspace validation runs at close: `tools/validate.sh` (file presence), the new `selvedge validate --precommit` (substrate integrity + ref resolution + spec hashes), the round-trip test, and the concurrency trial. Domain validation does not apply (this is self-development; no external artefact). Provisional-reference-substitute is being archived in 079's first action, so it does not apply.

## Risks specific to 079

1. **Refusal infeasibility at trigger level.** T-01 (ref resolution from `body_md`) is application-layer per D-3; if the parse is fragile, T-01 effectively shifts to "best effort at write time, validated again at close." Acceptable per D-3 §Open with engine_feedback.
2. **Concurrency trial result ambiguity.** A single-writer SQLite design may produce frequent `E_WRITE_BUSY` under 16-parallel load even with retry. The trial's purpose is to surface the calibration, not to demand zero contention; D-9 §Open admits this.
3. **D-7 cut breaking spec navigation.** Removing the workspace.md layout tree may make a fresh reader's first session harder. Per D-7 §Open: if surfaced, raise engine_feedback for 080+ revisit.
4. **Scope creep into 080 territory.** The "must NOT" list in D-11 is the constraint; the assembler-as-LLM, reviewer dashboard, and agent-on-substrate flows are explicitly off-limits in 079. The `selvedge` CLI is the substrate's only writer in 079; an agent-driven write path is 080+.

## Exit criteria (from D-11)

- Fresh workspace: `selvedge init` applies migration 001 cleanly.
- Round-trip test passes from clean state.
- Concurrency trial produces the D-9 expected results, or surfaces a documented calibration.
- Closed-session structured rows are immutable except via later corrective rows (T-06).
- `selvedge validate --precommit` reports clean against the post-079 workspace.
- A documented command path exists that 080 can use to hand one agent output to the substrate.

End-of-session deliverable: engine-v17 lands, substrate operational, provenance recorded.
