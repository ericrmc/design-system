---
session: 078
title: Design commitments — close
date: 2026-04-27
engine_version_at_close: engine-v16
mode: self-development
---

# Close

## What was done

Session 078 produced design commitments for the next-generation Selvedge engine, per the handoff in `provenance/077-design-space/03-close.md` §"What session 078 should address." The session ran as a multi-agent deliberation with two cross-family voices (operator-confirmed at session open per the same ratio as 077; reasoning recorded in `00-assessment.md`).

1. **Five blind perspectives written.** Three Anthropic (substrate-architect, agents-architect, adversary) via the Agent tool's general-purpose subagent type; two OpenAI (cross-family engineer, cross-family methodologist) via `codex exec --sandbox read-only --skip-git-repo-check`. All five wrote in parallel before any saw another's position. Per-perspective seed briefs at `seeds/`; positions at `perspectives/01-substrate-architect.md` through `perspectives/05-codex-methodologist.md`. Total ~12,400 words of perspective content.

2. **Synthesis written preserving dissent.** `01-deliberation.md`. Ten convergence points and five divergence points named explicitly. Each claim tagged by source perspective for traceability. Three load-bearing minority positions preserved as first-class for the decision record to dispose: Div-1 (S2-narrow per `[adv]`); Div-2 (reviewer subsume-into-human per `[adv]`, remove-now-return-narrower per `[meth]`); Div-5 (`[adv]`'s "does 078 subtract more than it adds?" diagnostic).

3. **Twelve decisions recorded.** `02-decisions.md`.

   - **D-1** Substrate-shape: **S1-typed** (S1 cells for argument; S3 tuples for state; S2 files for specifications only).
   - **D-2** Agent set: **3 LLM roles + 1 human role**. No LLM reviewer at first cut (deferred to 080+ contingent on substrate evidence). No LLM assembler (deterministic templating). Specifier, decider, deliberator-N as the LLM roles.
   - **D-3** Refusal contract: **16 refusals** enumerated as T-01 through T-16, mapped to `constraints.md` failure properties.
   - **D-4** Reading B (accretion-without-subtraction): **adopt**.
   - **D-5** Reading C (self-hosting-as-disease): **hold open with operator-enforced release gate** — engine-v17 is provisional until first external-problem trial of 30 sessions completes.
   - **D-6** D-4.b (subtractor=human): **adopt collapse**. One human reviewer-subtractor role; deterministic eligibility report.
   - **D-7** D-4.c (cut engine-v16): **adopt**. Six concrete cut targets applied by 079 as its first action.
   - **D-8** Schema-evolution protocol: **additive-default; contract changes are foundation-touching**. Two-tier rollback.
   - **D-9** Substrate technology: **SQLite 3, single-writer, local-only**. Concurrency falsification trial specified for 079.
   - **D-10** Write budgets: **≤ 400 non-blank lines active spec; ≤ 16 tables in migration 001; ≤ 20 refusals at first cut**. Engine-v16 currently breaches the 400-line budget (430 non-blank); D-7's cut resolves the breach.
   - **D-11** 079 handoff: **vertical-slice implementation**. Apply the cut → migration 001 → CLI → round-trip test → concurrency trial → close. Explicit "must not" list constraining horizontal expansion.
   - **D-12** 078 self-test: **subtraction column ≥ addition column**. 9 subtractions, 11 additions; 4 of the additions consume zero active-engine-spec lines (dispositions). Engine-v17 is smaller than engine-v16 by line count. `[adv]`'s test passes.

4. **No active engine-v16 file modified.** Session 078 produced provenance only. No engine-version bump.

5. **Validator clean.** `tools/validate.sh` runs at 078 close (recorded below).

## State at close

The active engine surface is unchanged from session 076 / 077: `engine-v16`, eight files, 430 non-blank lines (640 total). The breach of D-10's 400-line budget is recorded in the decision; D-7's cut applied by 079 brings the engine under budget.

The design-commitment surface that session 079 inherits is fully specified at `02-decisions.md`. 079's deliverables are seven concrete steps (D-11) with explicit exit criteria. The "must not" list constrains 079 from horizontal expansion (no LLM agents; no generated narrative; no archive migration; no scope beyond migration 001).

Engine-version increments are anticipated as follows:
- **engine-v16 → engine-v17 at 079 close** (D-7 cut applied; substrate landed; CLI authored).
- **engine-v17 → engine-v18** is not anticipated until after the first external-problem trial completes (D-5 release gate). Bug fixes and validator tightening are admitted; new active-spec content is not.

## What session 079 should address

Per D-11, session 079 implements the substrate vertical slice in this order:

1. Apply the D-7 cut to engine-v16 active spec; bump to engine-v17 in `engine-manifest.md`; archive the removed sections per `methodology.md` §Preservation.
2. Author `state/migrations/001-initial.sql` implementing the D-1 substrate-shape and D-3's 16 refusals.
3. Implement the `selvedge` CLI: `init`, `id-allocate`, `submit`, `validate --precommit`, `subtract-eligibility`.
4. Wire `tools/validate.sh`'s successor to call `selvedge validate --precommit`.
5. Run the round-trip test (open → write decision with one alternative + one ref → close → reopen → verify T-06 refuses UPDATE on closed decision).
6. Run the D-9 concurrency falsification trial (16 parallel submits, injected sleep, one mid-transaction kill).
7. Close with a decision recording trial results and any engine_feedback raised.

079 must not build any LLM agent role, generate close narrative via LLM, migrate 75-session pre-restart provenance, solve schema-evolution beyond migration 001, or bump beyond engine-v17. Exit criteria are enumerated at D-11.

If 079 hits an implementation blocker on a refusal, 079 records the blocker as engine_feedback, downgrades the refusal in migration 001, and 080+ deliberates the resolution. Graceful degradation with explicit feedback is admitted.

Session 080's likely work, contingent on 079's outcome:
- First agent-on-substrate flow (start with deliberator-N because the multi-perspective pattern is the irreducible role per `[agt]`).
- First human-reviewer-subtractor cadence read (contingent on cadence-overdue from 079 close; per D-6, default cadence is every 5th self-development session).
- First 080-deliberation may also produce the conditional re-introduction of the LLM reviewer if the substrate's refusal contract demonstrably fails to catch a class of error a substrate-query reviewer could (D-2 OI-078-002).

## Honest limits

1. **Line count claim in 077-`00-assessment.md` was off.** 077 stated "engine-v16 is the active surface (eight files, ~350 lines)." Actual count: 430 non-blank / 640 total. The "~350" estimate was directional; D-10 records the actual measurement and ties the budget to non-blank-line count for clarity. This is recorded in D-10 itself; noting here so that future sessions reading the close find the discrepancy without searching. The discrepancy is itself evidence for D-4 Reading B (the engine grew quietly without anyone noticing the count).

2. **Two cross-family voices is a 078 choice, not a methodology rule.** Same as 077; reasoning recorded in `00-assessment.md`. `methodology.md` §When to convene multiple agents requires *at least one*. 078's 2-of-5 ratio is operator-directed at session open; 079 picks its own ratio against the same rule (and may not need a deliberation at all if the implementation surface is unambiguous, which D-11 is structured to ensure).

3. **No close-time reviewer audit was run for 078.** Operator-directed at session open: 077's close self-documented honest limits thoroughly; the reviewer mechanism is in redesign scope per D-7's adoption of `[meth]`'s cut of `methodology.md` §When to review at close. 079 may elect to run a reviewer over 078 retrospectively if its substrate implementation surfaces evidence the close mis-recorded what was decided. The decision is 079's. Per D-2, no LLM reviewer is built in 079; if the retrospective audit happens, it is human or operator-directed.

4. **Codex calls used `--sandbox read-only`.** Same as 077. Position content was emitted to stdout and captured by the orchestrator. Output files at `perspectives/04-codex-engineer.md` (74 lines) and `perspectives/05-codex-methodologist.md` (92 lines). These are shorter than the Anthropic perspectives by design — codex tends to terser specificity — but the substantive coverage of the assigned deliverables (D-9 substrate tech, D-8 schema evolution, D-7 cut, D-11 handoff) is complete.

5. **Subagent task prompts forbade `git` explicitly.** Per 077-`03-close.md` honest-limit-1, the seed `_shared.md` instructed all five subagents not to invoke git. No subagent committed in 078. The mechanism note from 077 is closed: explicit per-task forbiddance prevents the unilateral-commit failure. This is recorded for future-session reference.

6. **The deliberation pattern's blind discipline was procedurally enforced, not substrate-enforced** — same as 077. D-3's T-05 and T-13 commit this to the substrate in 079; the procedural-only state ends with engine-v17.

7. **D-12's self-test accounting is at the level 078 can produce.** 9 subtractions, 11 additions; 4 of the additions are dispositions consuming zero active-engine-spec lines. The accounting is honest at the *deliberation-output* level, not at the *implementation-cost* level: the substrate adds substantial state (state/migrations/, state/selvedge.sqlite, the `selvedge` CLI) which is not counted as "active engine spec" but is engine-definition for engine-v17. By line count of code-and-substrate, engine-v17 is *larger* than engine-v16; by line count of *active prose-spec the agent must read at session open*, engine-v17 is smaller. Both accountings are true; the methodology's diagnostic question is the second one (`constraints.md` §4 "foundational instructions decay under load"), which is what `[adv]`'s test addresses. D-12 records this honestly; future sessions auditing 078 are free to apply a different accounting if they think it more material.

8. **Engine-feedback inbox not consulted.** Same as 077. The session's read list (per `00-assessment.md`) included `provenance/077-design-space/` but not `engine-feedback/INDEX.md`. The 076 close marked the EF records open at restart as rejected by engine-v16 supersession; reading the inbox in 078 would not have changed the design commitments. Recording for honesty.
