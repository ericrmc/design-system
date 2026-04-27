---
session: 080
title: CLI deliberator extension — assessment
date: 2026-04-27
engine_version_at_open: engine-v17
mode: self-development
substrate_session_no: 1
---

# Assessment

## Where the workspace was at open

Engine `engine-v17` (provisional per 078 D-5). Substrate at HEAD held only the post-init schema — 17 tables, migration 001 applied, sha256 verified clean against the file. Validator green at 16 ok / 0 fail. Two engine-feedback rows in `engine-feedback/inbox/` from S079: EF-079-001 (T-12 application-layer downgrade pending non-`__cli__` writer), EF-079-002 (T-15 deferred until `selvedge migrate` exists).

S079 close named two candidate workstreams for S080:
1. **Primary** — first agent-on-substrate deliberator-N flow (≥2 perspectives, ≥1 cross-family, sealing, synthesis_points).
2. **Contingent** — first human reviewer-subtractor cadence read (4 self-development sessions since restart; cadence triggers at 080 or 081 per operator).

## What this session committed to address

The orchestrator surfaced a structural blocker before opening: **`bin/selvedge submit` accepts only four `kind` values** (`session-open`, `session-close`, `decision`, `spec-version`). The schema and triggers for `deliberations`, `perspectives`, `synthesis_points` are present and refusal-bearing (T-05, T-13, T-14, T-06), but no CLI write path exists for them. The deliberator-N flow named as S080's primary work was therefore not executable.

Three options were surfaced to the operator:
- **A**: extend the CLI **and** run the deliberation in S080.
- **B**: run the deliberation in degraded form (Markdown-only, no substrate rows).
- **C**: extend the CLI only; defer the deliberation + cadence read to S081.

Operator selected **C**, with explicit direction to (i) reduce orchestrator load, (ii) include pytest-based tests for the new submit kinds, (iii) invoke a reviewer-agent audit loop and continue until priority issues resolve.

## Scope this session is committed to

1. Extend `selvedge submit` with four new kinds: `deliberation-open`, `perspective`, `deliberation-seal`, `synthesis-point` — `__cli__`-role only, T-12 application-layer.
2. Adopt pytest as the substrate test harness alongside the existing bash tests; add `pyproject.toml`, `state/tests/conftest.py`, and test files covering the four new kinds plus parallel coverage for the four pre-existing kinds.
3. Run a reviewer-agent audit loop (separate-context Claude subagent) over the work; address findings until clean.
4. Defer the deliberator-N flow exercise itself, the OI-079-001 17-table-breach disposition, the human reviewer-subtractor cadence read, and any methodology revision to S081 or later.

## Hard limits in force at open

- **078 D-5 release gate.** No methodology-expanding self-development between S079 and the close of the first 30-session external-problem trial. CLI completion of write paths the schema already encodes is mechanism-implementing-existing-methodology; admitted. Adding new active-spec content to `methodology.md` or peer specifications would be expansion; refused.
- **No close-time reviewer per kernel.** The kernel's §"When to review at close" was archived per 078 D-7 step 1 ("substrate distinguishes prevention from audit"). The reviewer-agent loop this session uses is in-session orchestration — a Claude subagent invoked via the harness — not a methodology-level mechanism. It does not re-introduce the archived close-time-review pattern at the spec layer.
- **No migration runner.** Per EF-079-002, `selvedge migrate` is deferred. Any substrate-schema fix that requires editing migration 001 in place violates the workspace's preservation rule and the substrate's own integrity model (sha256 stored in `schema_migrations`). Schema holes surfaced this session must be **documented** as open issues, not silently patched.

## Discrepancy noted at open

Counted manually, the schema has **17 tables**: `agent_runs, commitments, decision_alternatives, decisions, deliberations, engine_feedback, objects, perspectives, read_log, refs, role_write_capabilities, schema_migrations, sessions, spec_versions, subtraction_log, synthesis_points, work_items`. The 079 D-2 breach record reads "16 from D-10 + synthesis_points = 17", and `engine-manifest.md` §Substrate enumerates 15 named tables. The unenumerated table is `objects` — load-bearing infrastructure for T-01 ref resolution. The discrepancy is between the manifest's prose enumeration and the actual schema, not between the breach record's count and reality. Recorded here so the next reviewer-subtractor cadence read can decide whether to enumerate `objects` in the manifest or treat it as substrate-infrastructure exempt from the 16-table budget.

## Substrate session-no mapping

Substrate `sessions.session_no=1` corresponds to narrative session 080. T-10 requires contiguity-from-1; the substrate is its own counter starting at the first session that exists in it. Pre-080 sessions are not migrated into the substrate (per 078 D-11 must-not). The mapping is carried only by the slug (`cli-deliberator-extension`) and these provenance files; future sessions querying the substrate for "narrative S080" must know to look up `session_no=1`. A future session that wants to make this discoverable from substrate inspection alone has the option to add a `narrative_session_no` column via migration 002+.
