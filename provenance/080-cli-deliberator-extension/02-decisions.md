---
session: 080
title: CLI deliberator extension — decisions
date: 2026-04-27
engine_version: engine-v17
substrate_session_no: 1
---

# Decisions

## D-1 (substantive) — Re-scope S080 from primary deliberator-N flow to CLI extension only (Option C)

**What.** S080 extends `selvedge submit` with the four substrate-write kinds the schema already encodes (`deliberation-open`, `perspective`, `deliberation-seal`, `synthesis-point`) and stops there. The first agent-on-substrate deliberator-N flow exercise, the OI-079-001 17-table-breach disposition, and the human reviewer-subtractor cadence read all defer to S081 or later.

**Why.** Discovered before opening: `bin/selvedge submit` accepts only four kinds; the schema and triggers for the deliberator-N flow are present and refusal-bearing but not callable. The S079 close named the deliberator-N flow as primary work without anticipating the missing CLI surface. The orchestrator surfaced three options to the operator (A: extend + deliberate same session; B: degraded Markdown-only deliberation; C: extend only, defer deliberation). Operator selected C explicitly to **reduce orchestrator load** (a distinct observation that single-session work crowding produces the constraint #4 + #6 compound failure described in `specifications/constraints.md`).

**Rejected alternatives.**

- **R-1.1 — Option A (extend CLI plus run deliberator-N flow in S080).** Rejected because combining mechanism-build with first-use-of-mechanism crowds a single session with two distinct workstreams. The constraints file warns against single-agent context saturation; opting to combine these would set up the next session's context even larger, and the orchestrator would be evaluating its own newly-built CLI on a substantive question simultaneously.
- **R-1.2 — Option B (Markdown-only deliberation, degraded form).** Rejected because the entire 078 D-1 substrate decision is that coordination flows through the substrate, not through prose. Running the first deliberation in degraded form would teach the workspace to route around the substrate when the substrate is inconvenient — exactly the failure mode 078 was designed to prevent.

**Open.** S081 must execute what S080 did not: open a real deliberation in the substrate (likely on the OI-079-001 disposition, with cross-family perspective via `codex` CLI per `CLAUDE.md`), seal it, write synthesis_points, and decide. Until S081 exercises the new kinds end-to-end against a real load-bearing question, the S080 evidence is only that the kinds **work**, not that they **carry decisions** the workspace can stand on.

---

## D-2 (substantive) — Adopt pytest as the substrate test harness, alongside (not replacing) the bash tests

**What.** Add `pyproject.toml` declaring pytest as a dev dependency; add `state/tests/conftest.py` with substrate snapshot/restore session-fixture and per-test `clean_substrate` / `open_deliberation` / `db` fixtures; add `state/tests/test_deliberation_kinds.py` covering the four new kinds; add `state/tests/test_existing_kinds.py` providing pytest parallels for the four pre-existing kinds (alongside, not replacing, `state/tests/round_trip.sh` and `state/tests/concurrency.sh`). Run via `uv run --with pytest pytest state/tests/`.

**Why.** Three drivers, in order: (1) **operator instruction** to use pytest for the new tests; (2) refusal-test ergonomics — pytest's `pytest.raises` and `--rx` xfail reporting express "expected refusal" more cleanly than bash `grep -q` patterns and produce structured output for the reviewer agent to consume; (3) speed — the full pytest suite (29 tests, two of them strict xfails) runs in 2–4 seconds against the snapshot/restore fixture, versus ~one second per bash test for snapshot+CLI startup. Bash tests are kept because `concurrency.sh` exercises the `bin/selvedge submit` process boundary including startup cost (D-9 calibration), which the pytest harness currently does via subprocess but does not parallelise.

**Rejected alternatives.**

- **R-2.1 — Stay with bash only.** Rejected because the new refusal cases are heterogeneous (T-05 trigger refusal, T-13 trigger refusal, T-14 CHECK refusal, T-12 application-layer refusal, plus state-machine guards `E_NOT_SEALED` and `E_ALREADY_SEALED`). Each would need its own bash block with grep patterns; the file would reach 500+ lines and become brittle. Pytest expresses these as 13 small functions sharing fixtures.
- **R-2.2 — Replace bash with pytest entirely.** Rejected because the `concurrency.sh` falsification trial from S079 D-9 calibrated against a specific contention pattern (16 parallel writers, in-transaction sleep, SIGKILL mid-tx) that depends on the actual `bin/selvedge submit` process startup behaviour. Re-implementing this in pytest would not reduce work; it would only move it.

**Open.** Future test-harness consolidation can convert `round_trip.sh` to pytest (the coverage is now a strict superset in `test_existing_kinds.py`) once a session has time to retire the bash file cleanly. Out of S080's scope.

---

## D-3 (substantive) — Defer OI-080-001 (T-06 missing on `deliberations` UPDATE; T-13 admits sealed_at re-timing) to a session that builds `selvedge migrate`

**What.** The reviewer-agent pass 1 surfaced two substrate holes: `t06` has no trigger family member protecting `deliberations` UPDATE/DELETE on a closed session, and `t13` only refuses non-NULL→NULL transitions on `sealed_at` (admitting non-NULL→other-non-NULL silently). Both are recorded as `open-issues/OI-080-001.md` (HIGH priority, blocked-on `selvedge migrate`). Two strict xfail tests pin the current behaviour and will trip the suite to red when migration 002 lands the missing triggers.

**Why.** Fixing in S080 would require either editing `state/migrations/001-initial.sql` in place (which invalidates the sha256 stored in `schema_migrations` and violates the workspace's preservation rule that specs evolve via new versions, not silent edits) **or** building the deferred `selvedge migrate` runner per EF-079-002 plus migration 002 plus the supporting validator tightening — a workstream of similar size to S080's whole CLI extension, attempted on top of it. Both options exceed the scope cap chosen in D-1. The hole is documented (open issue), bounded in threat (today's only writer is `__cli__`, which has no path to mutate sealed deliberations), and forced into future visibility (the strict xfail tests turn from green to red the moment a future session ships migration 002 without unmarking them, surfacing the issue at exactly the right point).

**Rejected alternatives.**

- **R-3.1 — Edit `001-initial.sql` in place to add the missing triggers.** Rejected because the substrate's own integrity model stores the sha256 of the migration in `schema_migrations`; an in-place edit would falsify that record and require either re-init (destroying S080's substrate state) or silent sha256 update (defeating the integrity check). Either path violates "specifications evolve through new versions, not silent edits" (workspace.md §Preservation).
- **R-3.2 — Build `selvedge migrate` plus migration 002 in S080.** Rejected because the runner is itself a load-bearing piece: it must apply migrations idempotently against existing substrates with rows already present; it must verify the post-migration sha256; it must refuse partial application; it must integrate with the validator. Bundling this with S080's CLI extension would re-create the same single-session crowding D-1 was chosen to avoid.
- **R-3.3 — Document the hole in 03-close.md only, no open issue, no xfail.** Rejected because relying on close-prose-as-record is exactly the failure mode constraints.md §1 names: prose drifts, tests do not. The xfail tests are the structural memory; the open issue is the structural assignment of responsibility.

**Open.** The session that builds `selvedge migrate` (probably the session immediately following the first external-problem trial pause, when methodology-touching work is again admitted under the release gate) inherits OI-080-001 as a precondition: the runner ships **with** migration 002 fixing both holes, not separately. The closing condition in OI-080-001 lists the four steps: runner exists; migration 002 lands the trigger fixes; the two xfail tests flip to xpassed; the round-trip + concurrency tests rerun green against the migrated substrate.

---

## D-4 (substantive) — Adopt strict xfail tests as the workspace pattern for documented substrate holes

**What.** When a hole in the substrate is identified and deferred, write a test that demonstrates the hole as it exists today; mark it `pytest.mark.xfail(strict=True, reason="OI-NNN-NNN: …")`. The test passes (as xfailed) while the hole is unfixed; it **fails** (as xpassed) the moment the substrate is fixed without unmarking the test. Two such tests added in S080 (`test_t06_deliberations_update_unprotected_xfail`, `test_t13_permits_resealing_to_other_timestamp_xfail`) now pin OI-080-001's two parts.

**Why.** Constraints.md §5 names the failure mode: "Detection without a structural feedback loop into prevention does not correct anything." A documented-but-untested hole relies on the future agent reading the open issue. A strict xfail test makes the substrate fix structurally visible at the test-suite level — the suite literally cannot return to all-green after a fix until the test is reckoned with. This is what "structural feedback loop into prevention" looks like at the test-discipline layer.

**Rejected alternatives.**

- **R-4.1 — `pytest.mark.skip(reason=…)`.** Rejected because a skipped test produces no signal when the substrate is fixed. The signal would have to come from the future agent re-reading the open issue and remembering to unskip; that's the same fragile mechanism constraints.md §5 indicts.
- **R-4.2 — Plain comment in the test file ("TODO: when migration 002 lands, add this test").** Rejected on the same grounds — comments do not enforce.

**Open.** None. The pattern is small enough to apply pointwise without specifying it as a methodology mechanism (which would be release-gate-violating). Future sessions that surface holes simply follow the precedent established here.

---

## D-5 (disposition) — Adopt in-session reviewer-agent loop as an orchestrator-side practice for S080

**What.** Per operator instruction received mid-session, S080 invoked a Claude subagent (Explore type, separate context, in-process via the harness `Agent` tool) as a reviewer over the work-in-progress. Pass 1 surfaced findings; the orchestrator addressed each (added tests, opened OI-080-001); pass 2 verified. Two passes; loop closed at "ADVISORY ONLY (close OK)".

**Why.** Operator-directed: "reduce load on the orchestrator agent (you)" plus "keep looping until all priority issues have been resolved". The pattern is mechanism-at-the-harness-level (a subagent invocation), not methodology-at-the-spec-level. It does not re-introduce the close-time-reviewer section archived per 078 D-7 step 1; it is in-session help for the orchestrator. Recorded under substrate `kind='disposition'` (not `substantive`) because no methodology spec changes; the practice is not specified for future sessions, only used in this one. Disposition kind requires no rejected-alternative rows per T-02.

**Rejected alternatives.** None deliberated; operator directive.

**Open.** Whether the in-session reviewer-agent practice should become a methodology mechanism (and therefore warrant a spec section, with cross-family deliberation) is an open question for after the release gate lifts. For now: practice-at-orchestrator-discretion.

---

## Substrate decision rows

The five decisions above are written into the substrate via `bin/selvedge submit decision` at the same commit as this file (D-1 through D-5 → substrate `decision_no` 1–5 against `session_id=1`). Each substantive decision (D-1 through D-4) carries ≥1 alternative row per T-02. D-5 (minor) does not require alternatives. Aliases: `D-S001-1` through `D-S001-5` (substrate-relative; the substrate's `session_no=1` corresponds to narrative S080 per the assessment file's mapping note).
