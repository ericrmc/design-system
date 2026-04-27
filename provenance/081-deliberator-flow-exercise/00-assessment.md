---
session: 081
title: First real deliberator-N flow — OI-079-001 disposition
date: 2026-04-27
engine_version_at_open: engine-v17
mode: self-development
substrate_session_no: 2
---

# Assessment

## Where the workspace is at open

S080 closed engine-v17 with the deliberator-N CLI surface complete and pytest green at 27 passed + 2 strict xfails (the xfails pin OI-080-001). The substrate at HEAD carries one closed session (`session_no=1`, slug `cli-deliberator-extension`), one sealed smoke deliberation, two smoke perspectives, one smoke synthesis_point, and five S080 decisions.

S080 close named three candidate workstreams for S081:
1. First real deliberator-N flow exercise (likely on the OI-079-001 disposition).
2. First human reviewer-subtractor cadence read (cadence trigger firmly hot at S081 per 078 D-6).
3. `selvedge migrate` runner + migration 002 (closes OI-080-001).

Operator selected **(1)**. The cadence read in (2) is operator-gated and was not picked up. (3) is deferred — OI-080-001 remains open with its xfail tests as structural memory.

## Scope this session is committed to

Run the first agent-on-substrate deliberator-N flow against a load-bearing question: the disposition of the 17-table breach raised by 079 D-2 / D-10 and OI-079-001.

Concretely:

1. Open substrate session 2 (`session-open`, narrative S081 → substrate session_no=2 per T-10 contiguity).
2. Open a deliberation in the substrate via `selvedge submit deliberation-open` with topic naming the OI-079-001 disposition.
3. Gather three blind perspectives (each writes its position to a file before any sees another):
   - **P-claude** — orchestrator (Claude Opus 4.7), Anthropic family, neutrally framed.
   - **P-codex** — `codex` CLI, OpenAI family, cross-family per `CLAUDE.md` `## Multi-agent work` and per `methodology.md` §When to convene multiple agents ("at least one perspective should come from a different model family").
   - **P-adversarial** — Claude general-purpose subagent, Anthropic family, briefed to challenge whatever the most plausible default disposition turns out to be and to surface unstated assumptions.
4. Submit the three perspectives to the substrate (`perspective` x3), seal the deliberation, write `synthesis-point` rows (≥1 convergence with ≥2 source perspectives per T-14, plus any divergence/minority points).
5. Record the disposition as a `decision` row of kind `'calibration'` if it ratifies an existing breach-with-cause clause, or `'substantive'` if it reshapes the schema/manifest. Record rejected alternatives per T-02.
6. Apply any spec-text edits the decision warrants (e.g., to `engine-manifest.md` §Substrate enumeration) — these would be small prose corrections, not active-spec content additions.
7. Validate, close, commit.

## The substantive question

OI-079-001 was raised in 079 02-decisions as: "D-10's table budget of 16 vs. the actual 17. Either ratify 17 as the new budget or subtract `synthesis_points` (which would require absorbing T-14 elsewhere). Reviewer decision."

S080's `00-assessment.md` §Discrepancy noted at open refined the framing: the schema has **17 tables** (`agent_runs, commitments, decision_alternatives, decisions, deliberations, engine_feedback, objects, perspectives, read_log, refs, role_write_capabilities, schema_migrations, sessions, spec_versions, subtraction_log, synthesis_points, work_items`); `engine-manifest.md` enumerates **15** (the 16 from 078 D-10 minus one — the manifest's prose lists 15, not 16). The two unenumerated tables are `objects` and `synthesis_points`.

The candidate dispositions, as the workspace currently sees them:

- **A — Ratify 17.** Update D-10's budget to 17 (or to "16 + synthesis_points"). Update `engine-manifest.md` enumeration to list all 17 tables. Record as `calibration` per the existing "breachable with cause" clause in 078 D-10. Cheapest. No schema change.
- **B — Subtract `synthesis_points`.** Absorb T-14's convergence-needs-≥2-sources constraint elsewhere (probably into `deliberations.synthesis_md` as JSON, or into a `kind` column on a generalised `notes`-style table). Requires migration 002 + the `selvedge migrate` runner, which doesn't exist (per OI-080-001 / EF-079-002). **Currently blocked.**
- **C — Enumerate `objects` as substrate-infrastructure exempt from the 16-table budget.** Treat `objects` as plumbing for T-01 ref resolution rather than a domain table; raise the budget to 17 only for the legitimate `synthesis_points` addition. Update the manifest's enumeration to call this out. Closer to (A) than (B).

The deliberation's job is to choose among A/B/C (or surface a fourth option) and to record the reasoning that carried it.

## Hard limits in force at open

- **078 D-5 release gate.** No methodology-expanding self-development between S079 and the close of the first 30-session external-problem trial. Calibration decisions that ratify existing-clause-permitted breaches are admitted; new active-spec content additions to `methodology.md` or peers are forbidden.
- **No close-time reviewer per kernel.** Per 078 D-7 step 1, the close-time-review pattern is archived. The reviewer-agent loop pattern S080 used for in-session orchestration may or may not be invoked here at orchestrator discretion; S081's emphasis is the deliberator-N flow itself, not in-session review.
- **No migration runner.** Per OI-080-001 / EF-079-002. Disposition B is blocked at the schema-change layer.
- **No methodology-revision text written to `methodology.md` etc.** Confirmed at open.

## Workspace inconsistency noted at open (carried forward, not fixed in this session)

OI-079-001 is named in `provenance/079-substrate-vertical-slice/02-decisions.md`, in S080 `00-assessment.md`, and in S080 `03-close.md`, but it does not exist as a file in `open-issues/` and is not listed in `open-issues/index.md`. The numbering convention text in the index says "OI-001 was first, OI-002 second, etc." — strict append-only — but OI-080-001 (the existing latest) uses a session-prefixed scheme. The workspace shifted convention without updating the convention text.

S081's deliberation can stand on its own — the question is well-posed in the prose record — but the bookkeeping inconsistency should be surfaced in the close so a future session can resolve it (either backfill `open-issues/OI-079-001.md` and update the convention text, or normalise the citations to the actual existing numbering scheme).

## Substrate session-no mapping

Substrate `sessions.session_no=2` corresponds to narrative S081. The mapping is carried by slug (`deliberator-flow-exercise`), this provenance directory, and the close. T-10 contiguity is satisfied by opening session_no=2 immediately after session_no=1 closed in S080.
