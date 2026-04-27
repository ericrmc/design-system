---
session: 081
title: First real deliberator-N flow exercise — close
date: 2026-04-27
engine_version_at_close: engine-v17
mode: self-development
substrate_session_no: 2
---

# Close

## What was done

S081 ran the first agent-on-substrate deliberator-N flow on a load-bearing question (OI-079-001 disposition: 17-table-vs-D-10's-≤16-vs-manifest's-15 discrepancy) and recorded the resulting calibration plus two bookkeeping dispositions in the substrate.

### Concretely

1. **Substrate session 2 opened.** `selvedge submit session-open` — narrative S081 → substrate `sessions.session_no=2`. T-10 contiguity satisfied (S080 was session_no=1).
2. **Deliberation 2 opened in substrate.** `selvedge submit deliberation-open` — `deliberations.deliberation_id=2`, topic naming the OI-079-001 disposition with the three named candidates.
3. **Three blind perspectives gathered.** P-2-claude (anthropic, orchestrator's own analysis, written before reading any other), P-2-codex (openai, via `codex exec --sandbox read-only` with a self-contained prompt that forbade tool use), P-2-adversarial (anthropic, Claude general-purpose subagent in separate context, briefed adversarially with file-read permission but instruction-barred from the other perspective files). Blind condition preserved across all three. Files at `provenance/081-deliberator-flow-exercise/perspectives/` (P-claude.md, P-codex.md, P-adversarial.md).
4. **Perspectives submitted to substrate.** `perspectives.perspective_id` 3 (alias `P-2-claude`), 4 (`P-2-codex`), 5 (`P-2-adversarial`).
5. **Deliberation sealed.** `sealed_at = 2026-04-27T06:14:18.722Z` with synthesis_md (1651 bytes) recording convergence/divergence/minority structure. T-13 now refuses sealed_at→NULL on this row (and the OI-080-001-known hole admits sealed_at→other-non-NULL — not exploitable through the CLI).
6. **Four synthesis_points written.** Two convergence (reject-B; manifest-must-align), one divergence (A-vs-C-vs-D), one minority (budget-is-derived-quantity). T-14 satisfied for both convergence rows (≥2 source_perspectives).
7. **Three decisions recorded** in substrate (`D-S002-1` calibration with 3 alternatives; `D-S002-2` and `D-S002-3` dispositions with 0 alternatives) and in `02-decisions.md`. D-1's body_md cited [P-2-claude], [P-2-codex], [P-2-adversarial], producing 3 substrate `refs` rows; D-3 cited [P-2-adversarial] producing 1 ref; D-2 wrote no refs.
8. **`engine-manifest.md` enumeration corrected** from 15 to 17 substrate tables (added `objects` and `synthesis_points` to the prose enumeration; annotated `objects` as the citable_alias indirection table powering T-01). Frontmatter `updated-by-session` 079 → 081. Engine version unchanged (correction-of-omission, not substantive content addition; per the manifest's own §Versioning).
9. **OI-079-001 backfilled** at `open-issues/OI-079-001.md` with status: Resolved (provisionally — minority forward as OI-081-001). Index updated in both active and resolved tables (hybrid-state for OI-081-001 follow-up linkage).
10. **OI-081-001 opened** at `open-issues/OI-081-001.md` carrying the P-2-adversarial minority position forward for post-release-gate review. Index active count 14 → 15.

## State at close

- **Active engine version:** `engine-v17` (provisional per 078 D-5; unchanged this session — calibration + bookkeeping; no engine-version bump).
- **Substrate at close:** sessions 2, deliberations 2, perspectives 5, synthesis_points 5, decisions 8, decision_alternatives 12, refs 4. Migration sha256 unchanged from S079 close.
- **Validator:** `tools/validate.sh` passes at 16 ok / 0 fail (counting the 03-close.md row that reaches "ok" at the same commit that lands this file; pre-close run showed 15 ok / 0 fail with one warn for the missing close).
- **Tests:** `pytest state/tests/` 27 passed, 2 xfailed (the strict xfails are still pinning OI-080-001 — unchanged from S080 close).
- **Open issues:** active count 14 → 15 (OI-081-001 added). OI-079-001 backfilled and resolved (hybrid-state, in both active and resolved tables of the index).
- **Engine-feedback:** unchanged from S080 close — no new EF rows from S081.

## Refusal coverage at close

S081 exercised the following refusals against real (not test) substrate writes for the first time:

| Refusal | S081 evidence |
|---|---|
| T-10 | session_no=2 (contiguous from session_no=1; would refuse session_no=3 at S081 open) |
| T-05 | not directly exercised (no post-seal perspective insert attempted); the seal at 2026-04-27T06:14:18.722Z is what would now refuse such an attempt |
| T-13 | seal at 2026-04-27T06:14:18.722Z would now refuse sealed_at→NULL on deliberation 2; the known-hole on sealed_at→other-non-NULL (OI-080-001) is not exploitable via the CLI |
| T-14 | both convergence synthesis_points (rows 2, 3) submitted with 2 source_perspectives — CHECK satisfied; would refuse a 1-source convergence write |
| T-01 | citable_alias parsing on D-1 body_md resolved [P-2-claude], [P-2-codex], [P-2-adversarial] to perspective object_ids 13/14/15; would refuse an unresolved alias |
| T-02 | session-close (run after this file lands) refuses if any substantive S081 decision lacks alternatives — no substantive decisions in S081 (all calibration/disposition); not exercised |
| T-08 | three rejection_reason_md fields written for D-1 alternatives, all > 16 chars; not refused |
| T-12 | all writes via `__cli__` role; would refuse non-`__cli__`; not exercised this session |

The pytest pinned-coverage from S080 still holds; OI-080-001 xfails still pinning (will flip when migration 002 lands).

## What S082 should address

Three candidates, in priority order:

1. **Human reviewer-subtractor cadence read.** Per 078 D-6, default cadence is every 5th self-development session; S076–S081 are six self-dev sessions, so the cadence trigger has been firmly hot for two sessions running. S080 close named it; S081 did not take it (operator selected the deliberator-flow exercise instead). Operator decides whether S082 takes it. Dossier inputs now larger than at S080 close: `bin/selvedge subtract-eligibility` (now has substantive substrate content from S081 — 5 perspectives, 5 synthesis_points, 8 decisions, 12 alternatives, 4 refs), the four EF rows in `engine-feedback/inbox/` (unchanged), OI-080-001 (still HIGH), OI-081-001 (newly opened — explicitly *for* the subtractor's eventual attention, post-gate). The cadence read is the natural complement to having just exercised the deliberator-N flow on a real question; the subtractor has fresh evidence to read.

2. **`selvedge migrate` runner + migration 002.** Closes OI-080-001 structurally. S080 close described what this entails (two-tier rollback per 078 D-8, idempotency against existing rows, sha256 verification, validator integration). Load-bearing piece. Releases the strict xfails in `state/tests/test_deliberation_kinds.py`. Independent of (1); could run in either order, but choosing (1) first lets the subtractor weigh in on whether the runner's design needs adjusting in light of OI-081-001's post-gate reconsideration of the budget mechanism (the runner's T-15 enforcement is what would replace the prose-budget if OI-081-001 lands that direction).

3. **Numbering-convention text resolution.** S081 D-2 deferred this. The resolution is small (one paragraph in `open-issues/index.md` Conventions section) but it touches workspace-discipline prose. Could be done as a 5-minute side-action of either (1) or (2), or held until a session that has slack.

**Hard limit on S082:** the 078 D-5 release gate remains in force. Calibrations under existing breach clauses, disposition decisions, mechanism-implementing-existing-methodology (the migrate runner), and human-subtractor reads are admitted. New active-spec content in `methodology.md` or peers is forbidden. S081 itself produced no methodology-text expansion.

## Honest limits

1. **Disposition C was rejected partly on a reading discovered after the seal.** P-2-claude's perspective explicitly named "I don't know whether 078's D-10 author intended `objects` to count as one of the 16" as the load-bearing uncertainty. The deliberation answered the question after the seal (during decision-write), and the answer made C structurally weaker (substantive D-10 revision rather than recategorisation within it). The blind deliberation surfaced the right uncertainty, but the answer landed in the decision record rather than in the synthesis. A future deliberation pattern might require resolving named uncertainties before sealing — but that is methodology-revision, gate-blocked.

2. **The minority position is preserved but not acted on.** P-2-adversarial argued the budget mechanism itself is the failure surface. The decision adopted A; OI-081-001 carries the dissent forward. This is the kernel's preservation discipline working as designed (`methodology.md` §When to convene multiple agents: "Synthesis preserves dissent: a minority position is recorded as a minority, not erased") but it is also a deferred bet: if the post-gate session that picks up OI-081-001 lands D, then S081's D-1 will look like ceremony defending ceremony, exactly the failure mode P-2-adversarial named. The bet is that the release gate's admit-only-existing-clauses discipline is the right discipline to hold during a release-stabilisation window even when a perspective makes a defensible case against the clause being held.

3. **No close-time review of S081 itself.** Per 078 D-7 step 1, the kernel's close-time-review section was removed at engine-v17. The deliberator-N flow this session ran *is* the methodology's mechanism for cross-checking on substantive decisions; it was applied to the OI-079-001 disposition. It was *not* applied to the bookkeeping decisions D-2 and D-3 (single-author, no cross-family, no adversarial perspective) — the kernel does not require it for dispositions.

4. **The three perspectives were of different lengths and depths** (P-2-claude ~5400 chars, P-2-codex ~3800 chars, P-2-adversarial ~4700 chars). The codex perspective was the shortest; this is partly the effect of the self-contained prompt-only context (no file access) versus the adversarial subagent's permitted reads. Whether this affects the deliberation quality is an open question for OI-019 (path-selection work-channel and warrant-surface diversity), which already exists for related concerns.

5. **The numbering-convention inconsistency in `open-issues/index.md` is unresolved this session** (S081 D-2 explicitly deferred). The session-prefixed scheme (OI-079-001, OI-080-001, OI-081-001) does not match the index's "strictly append-only" convention text. Recorded for S082+ rather than silently corrected.

6. **`engine-manifest.md` was edited without a spec_version row in the substrate.** The substrate's `spec_versions` table is currently empty (no rows tracking the active engine-definition specs); the manifest edit was a correction-of-omission per the manifest's own §Versioning rule and did not bump the engine version. A future session that introduces spec-version tracking for the active engine specs in the substrate inherits this provenance gap (no row records the S081 manifest touch); it can be backfilled then.

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
  ok    provenance/081-deliberator-flow-exercise/00-assessment.md
  ok    provenance/081-deliberator-flow-exercise/03-close.md (closed)

Summary: 16 ok / 0 fail
```

(The 03-close.md row reaches "ok" at the same commit that lands this file.)
