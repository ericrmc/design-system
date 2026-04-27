---
session: 083
title: Coding review loop — close
date: 2026-04-27
engine_version_at_close: engine-v19
mode: self-development
---

# Close

## What was done

S083 added a structural reviewer mechanism to the engine kernel: any session that produces, modifies, or deletes executable logic must invoke a reviewer subagent and continue invoking it until the reviewer reports no medium-or-higher findings remain. The change is operator-directed and is a deliberate exception to the 078 D-5 release gate. The pre-existing engine-definition close review is retained as a single-pass mechanism; both are now documented in `specifications/methodology.md` §When to review and wired into both prompts.

### Concretely

1. **`specifications/methodology.md` v2 → v3.** Replaces the superseded §When to review at close with §When to review, comprising §Coding review loop and §Engine-definition close review. The loop's scope ("executable logic"), severity taxonomy (critical/high/medium/low), adjudication bar (substantive enough that a future independent reviewer could judge soundness), termination condition (no medium-or-higher findings remain unresolved), and four-iteration deadlock pathway are all specified.
2. **`prompts/development.md` updated.** Operating instructions now invoke both reviewer mechanisms.
3. **`prompts/application.md` updated.** New §Review section mirrors the development prompt for external-problem sessions; structural-validation-check trigger added per F5.
4. **`specifications/workspace.md` v2 → v3.** `04-review.md` description expanded to cover loop iterations and the per-iteration record naming convention (`04-review-iter-N.md`).
5. **`specifications/engine-manifest.md` v18 → v19.** Engine bumped v18 → v19. §Current engine version rewritten; §Engine-version history appended.
6. **`tools/validate.sh` banner updated to engine-v19.**
7. **Coding review loop applied to this session's changeset** as a self-hosting demonstration. Two iterations: iteration 1 found 2 critical/high + 3 medium + 2 low findings; all medium-or-higher were fixed; iteration 2 returned clean. Recorded in `provenance/083-coding-review-loop/04-review.md`.
8. **Two open issues opened.** `OI-083-001-coding-review-substrate-enforcement.md` (substrate gate for the loop, MEDIUM, deferred). `OI-083-002-coding-review-severity-taxonomy.md` (worked rubric for the severity taxonomy, LOW, needs empirical signal first).
9. **`open-issues/index.md` updated.** Active count 14 → 16 (two new entries).

## State at close

- **Active engine version:** `engine-v19` (provisional in the same sense v18 was; further methodology-expanding changes remain gated by 078 D-5 except where operator-directed).
- **Methodology:** v3. The kernel now has a structural reviewer mechanism distinct from validation, with a defined termination condition.
- **Substrate at close:** unchanged from S082 (no migration). sessions=3, deliberations=2, perspectives=5, synthesis_points=5, decisions=11, decision_alternatives=15, refs=7, migrations=2.
- **Validator:** `tools/validate.sh` 16 ok / 0 fail at this commit (17 ok at the same commit landing this file).
- **Open issues:** active count 14 → 16; two new entries (OI-083-001 substrate enforcement, OI-083-002 severity taxonomy).
- **Engine-feedback inbox:** unchanged (EF-079-001 T-12 still awaiting writer-role activation; EF-079-002 already triaged at S082).

## Refusal coverage at close

Unchanged from S082. The new reviewer mechanism is *prevention via process*, not a substrate refusal; it does not extend T-01..T-16. OI-083-001 tracks the eventual substrate enforcement.

## Override of the 078 D-5 release gate

Recorded explicitly. The gate's clause forbidding methodology-expanding self-development sessions from modifying active spec content between Session 079 and the close of the first external-problem trial of 30 sessions is overridden for this revision by operator directive. The decision record (S083 D-2) names the override with reason; the manifest's §Current engine version re-cites it. No multi-agent deliberation was convened (the decision is operator-directed; cross-family review of the loop's design details is deferred to a future session once the mechanism has been exercised against real code-producing sessions).

## What S084 should address

Three candidates, in priority order:

1. **Human reviewer-subtractor cadence read** — still hot from S080, S081, S082 (now four sessions), and the workspace continues to accumulate. The S082 close named this as #1 priority for S083; it remained deferred. The dossier inputs are now richer still: substantive substrate content from S081 + S082, the unchanged inbox EFs, OI-081-001, OI-083-001, OI-083-002, all active OIs.
2. **Run the new coding review loop on a real code-producing session.** The S082 candidate (3) — pytest coverage extension to T-03/T-07a/b/T-09/T-16 — is the natural choice. It produces empirical signal for OI-083-002's severity taxonomy and confirms the loop's workability on a non-trivial change.
3. **Numbering-convention text resolution** (carried forward from S081 D-2 / S082 close).

The release gate continues to apply at v19. Calibrations, dispositions, mechanism-tests-implementing, mechanism-implementing-existing-methodology, human-subtractor reads, and operator-directed exceptions remain admitted; new active-spec content not so authorised remains forbidden.

## Validator at close

```
== Selvedge validator (engine-v19) ==

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
  ok    state/migrations/002-tighten-deliberation-immutability.sql
  ok    selvedge/cli.py
  ok    bin/selvedge

Workspace identity:
  ok    MODE.md

Workspace directories:
  ok    provenance

Substrate (selvedge validate --precommit):
validate --precommit: ok

Latest session check:
  ok    provenance/083-coding-review-loop/00-assessment.md
  ok    provenance/083-coding-review-loop/03-close.md (closed)

Summary: 17 ok / 0 fail
```

(The 03-close.md row reaches "ok" at the same commit that lands this file.)
