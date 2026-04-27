---
session: 080
title: CLI deliberator extension — close
date: 2026-04-27
engine_version_at_close: engine-v17
mode: self-development
substrate_session_no: 1
---

# Close

## What was done

S080 executed Option C per D-1: extend the `selvedge submit` CLI to cover the four deliberator-N flow kinds, write pytest coverage, run a reviewer-agent audit loop until clean, defer the deliberator-N exercise to S081.

### Concretely

1. **CLI extension.** `selvedge/cli.py` gained four handler functions (`_submit_deliberation_open`, `_submit_perspective`, `_submit_deliberation_seal`, `_submit_synthesis_point`) registered in `SUBMIT_HANDLERS`. All four write via the `__cli__` role with T-12 application-layer enforcement, attach `objects` rows correctly (object_kind = `'deliberation' | 'perspective' | 'synthesis_point'`; perspectives carry citable alias `P-{deliberation_id}-{label}`; deliberations and synthesis_points use NULL aliases per design), and propagate refs from body_md via the existing `_record_refs` parser.
2. **Smoke validation against live substrate.** Before pytest, the four new kinds were exercised end-to-end against the live S080 substrate: deliberation 1 ("smoke test") opened, perspectives 1–2 inserted (anthropic + openai families), seal applied at `2026-04-27T04:47:49.593Z`, synthesis_point 1 written (convergence kind, both perspectives as sources). These rows persist in the substrate at close as the first `objects` rows of kinds `'deliberation'`, `'perspective'`, `'synthesis_point'` ever written to the workspace.
3. **pytest harness.** Added `pyproject.toml` (declares pytest dev dep, `testpaths = state/tests`), `state/tests/conftest.py` (session-scoped `_snapshot_primary` autouse + per-test `clean_substrate`, `open_deliberation`, `selvedge_cli`, `db` fixtures), `state/tests/test_deliberation_kinds.py` (17 tests, 2 strict xfails), `state/tests/test_existing_kinds.py` (12 tests, parallel coverage for the four pre-existing kinds — `session-open`/`session-close`/`decision`/`spec-version` — including T-10/T-02/T-08/T-01/T-04/T-11/T-06 refusals).
4. **Reviewer-agent audit loop.** Two passes via Claude Explore subagent (separate context, in-process via the harness `Agent` tool). Pass 1 surfaced HIGH findings on T-06 deliberations UPDATE hole, T-14 divergence/minority test gap, T-13 timestamp-rewrite admission, plus an ADVISORY on pytest parallels for pre-existing kinds. Pass 2 verified all pass-1 findings either resolved or deferred-with-record; no new findings; verdict ADVISORY ONLY (close OK).
5. **OI-080-001 opened.** Documents the two substrate holes (T-06 missing on deliberations UPDATE, T-13 admits sealed_at re-timing). HIGH priority. Blocked on `selvedge migrate` runner per EF-079-002. Pinned by two strict xfail tests that will trip the suite when migration 002 lands.
6. **Five decisions recorded** in both `02-decisions.md` and the substrate (`decisions` rows 1–5; aliases `D-S001-1` through `D-S001-5`). Four substantive (D-1 through D-4, each with rejected-alternative rows per T-02), one disposition (D-5, no alternatives required).

## State at close

- **Active engine version:** `engine-v17` (provisional per 078 D-5; no engine-version bump this session — CLI extension is mechanism-implementing-existing-schema, not active-spec-content change).
- **Substrate:** `state/selvedge.sqlite` carries session 1 (open at this point in narrative; closes at the same commit that lands this file), 1 deliberation (sealed; smoke), 2 perspectives (smoke), 1 synthesis_point (smoke), 5 decisions (D-S001-1..5) with their alternatives, plus the migration record (sha256 unchanged from S079 close).
- **Validator:** `tools/validate.sh` passes at 16 ok / 0 fail.
- **Tests:** `state/tests/round_trip.sh` (9/9 from S079, unchanged) + `state/tests/concurrency.sh` (PASS from S079, unchanged) + `pytest state/tests/` **27 passed, 2 xfailed** (the two strict xfails are the OI-080-001 forcing functions).
- **Open issues:** active count 13 → 14 (added OI-080-001). Index updated.
- **Engine-feedback:** unchanged from S079 close. Two rows still in `engine-feedback/inbox/` (EF-079-001 T-12 application-layer; EF-079-002 T-15 deferred).

## Refusal coverage at close

The active substrate refusal table (per S079 close) is unchanged at the substrate level — S080 added no triggers. **Pytest coverage** for the substrate refusals as of S080:

| Refusal | S079 evidence | S080 pytest evidence |
|---------|---------------|----------------------|
| T-01 unresolved alias | round_trip.sh | `test_t01_unresolved_alias_refused` |
| T-02 substantive needs alternative | (implicit; S079 close) | `test_t02_substantive_decision_requires_alternative_at_close` |
| T-04 spec body sha mismatch | round_trip.sh (positive case) | `test_spec_version_hash_mismatch_refused` (negative) + `test_spec_version_hash_match_admitted` (positive) |
| T-05 perspective-after-seal | — (no exercise pre-S080) | `test_t05_perspective_after_seal_refused` |
| T-06 closed-session decision | round_trip.sh | `test_t06_closed_decision_immutable_via_sql` |
| T-06 closed-session perspective | — | `test_t06_closed_session_perspective_immutable` |
| T-06 closed-session synthesis_point | — | `test_t06_closed_session_synthesis_point_immutable` |
| T-06 closed-session **deliberation** | — | **`test_t06_deliberations_update_unprotected_xfail`** (strict xfail; OI-080-001) |
| T-08 short rejection_reason | — | `test_t08_short_rejection_reason_refused` |
| T-10 session contiguity | — | `test_t10_session_must_be_contiguous` |
| T-11 close-blocks-on-workitems | — | `test_session_close_after_unresolved_workitems_refused` |
| T-12 non-`__cli__` role | — | `test_t12_non_cli_role_refused` |
| T-13 sealed_at→NULL | — | (covered indirectly via xfail siblings) |
| T-13 sealed_at→other-non-NULL | — | **`test_t13_permits_resealing_to_other_timestamp_xfail`** (strict xfail; OI-080-001) |
| T-14 convergence ≥2 sources | — | `test_t14_convergence_with_one_source_refused` + `test_t14_convergence_with_zero_sources_refused` + `test_t14_divergence_with_one_source_admitted` + `test_t14_minority_with_one_source_admitted` |

Refusals **not yet exercised in pytest**: T-03 (one active spec_version per spec_id), T-07a/b (cite of superseded spec_version), T-09 (commitment state machine), T-15 (no DROP COLUMN/TABLE — deferred per EF-079-002), T-16 (lease-expired refused as 'leased'). Future sessions extending pytest coverage to these are admitted under the release gate (mechanism-test-implementing).

## What S081 should address

S081 was deferred from S080 with three explicit candidate workstreams:

1. **First real deliberator-N flow exercise.** Open a `deliberations` row in the substrate, insert ≥2 perspectives (≥1 from cross-family — `codex` CLI per `CLAUDE.md`), seal, write synthesis_points, decide. Likely topic: **OI-079-001 disposition** (the 17-table breach: ratify, absorb into the manifest's enumeration, or shrink the schema). The discrepancy noted in S080's `00-assessment.md` (the manifest enumerates 15 tables; the schema has 17 once `objects` and `synthesis_points` are counted) is the substantive question this deliberation can resolve.

2. **First human reviewer-subtractor cadence read.** Per 078 D-6, default cadence is every 5th self-development session; S076–S080 are five self-dev sessions, so the cadence trigger is **firmly hot at S081**. Operator decides whether S081 takes it. Dossier: `bin/selvedge subtract-eligibility` (currently empty against the post-init substrate; will have content after S081 writes substrate rows for the deliberation), the four EF rows in `engine-feedback/inbox/`, and now also OI-080-001 (which is itself a subtraction candidate in reverse — a hole the cadence-read may decide warrants pulling forward instead of letting accumulate).

3. **`selvedge migrate` runner + migration 002.** If S081 has slack after (1) and operator concurs, building the runner per EF-079-002 plus migration 002 closing OI-080-001 is the natural next mechanism step. If S081 does not have slack, this remains its own future session. Building the runner is a load-bearing piece — it must apply migrations idempotently against existing substrates with rows present, verify post-migration sha256, refuse partial application, integrate with the validator. Not a 30-minute job.

**Hard limit on S081:** the 078 D-5 release gate is in force (no methodology-expanding self-development until the first 30-session external-problem trial completes). All three workstreams above are mechanism-implementing-existing-methodology, not methodology-expansion. Adding new active-spec content to `methodology.md` or peer specifications would still be expansion and is forbidden until the gate lifts.

## Honest limits

1. **The deliberator-N flow is callable but not yet exercised on a real question.** S080's evidence is that the four new kinds **work** (smoke test against live substrate; pytest 27/27 happy + refusal paths); not that they **carry decisions** the workspace can stand on. S081 must do that.

2. **The smoke-test rows in the substrate are real S080 evidence, not test pollution.** Deliberation 1 ("smoke test"), perspectives 1–2, synthesis_point 1 are persistent in `state/selvedge.sqlite` at close. They are the first agent-on-substrate rows the workspace ever wrote. The provenance honestly records them as smoke validation; a future session that wants to query the substrate for "real" deliberations must filter or know the convention.

3. **OI-080-001 is open and HIGH.** Two substrate holes (T-06 missing on deliberations UPDATE; T-13 admits sealed_at re-timing) are documented but not fixed. The holes are exploitable only by direct sqlite3 access bypassing the CLI; today's only writer is `__cli__`, which exposes no path to mutate sealed deliberations. The strict xfail tests are the structural memory; the open issue is the structural assignment.

4. **Substrate session_no maps non-trivially to narrative session_no.** Substrate `sessions.session_no=1` corresponds to narrative S080. Future sessions querying the substrate for narrative S080 must look up `session_no=1`. The mapping is carried by slug + provenance directory + this file. A future migration could add `narrative_session_no` to the sessions table.

5. **The reviewer-agent loop pattern is in-session-only.** D-5 records it as a disposition-kind decision, not a methodology mechanism. Whether to specify it formally (with cross-family deliberation per the kernel) is deferred to post-release-gate. Until then: practice-at-orchestrator-discretion.

6. **No close-time review of S080 itself.** Per 078 D-7 step 1, the kernel's close-time-review section was removed at engine-v17. The reviewer-agent loop ran against work-in-progress, not against the close artefact. A future session that elects to retrospectively audit S080 reads `02-decisions.md` against the substrate's `decisions` rows + `decision_alternatives` + `objects` (aliases `D-S001-1..5`) — that audit is short and structural now.

7. **Manifest discrepancy unaddressed.** The 17-table-vs-15-enumerated mismatch noted in `00-assessment.md` was carried forward as input for S081's likely deliberation (the OI-079-001 disposition); S080 did not act on it.

## Validator at close

```
== Selvedge validator (engine-v17) ==

Active engine-definition files:
  ok    PROMPT.md
  ok    prompts/development.md
  ok    prompts/application.md
  ok    specifications/methodology.md
  ok    specifications/constraints.md
  ok    specifications/workspace.md
  ok    specifications/engine-manifest.md
  ok    tools/validate.sh
  ok    state/migrations/001-initial.sql
  ok    selvedge/cli.py
  ok    bin/selvedge

Workspace identity:
  ok    MODE.md

Workspace directories:
  ok    provenance

Substrate (selvedge validate --precommit):
validate --precommit: ok

Latest session check:
  ok    provenance/080-cli-deliberator-extension/00-assessment.md
  ok    provenance/080-cli-deliberator-extension/03-close.md (closed)

Summary: 16 ok / 0 fail
```

(The 03-close.md row reaches "ok" at the same commit that lands this file.)
