---
session: 077
title: Design space — close
date: 2026-04-27
engine_version_at_close: engine-v16
mode: self-development
---

# Close

## What was done

Session 077 produced the design space for the next-generation Selvedge engine, per the handoff in `provenance/076-engine-restart/03-close.md` §"What session 077 should address." The session ran as a multi-agent deliberation with two cross-family voices (operator-confirmed at session open).

1. **Five blind perspectives written.** Three Anthropic (architect, adversary, subtractor) via the Agent tool's general-purpose subagent; two OpenAI (cross-family generalist, cross-family devops) via `codex exec --sandbox read-only --skip-git-repo-check`. All five wrote in parallel before any saw another's position. Per-perspective seed briefs at `seeds/`; positions at `perspectives/01-architect.md` through `perspectives/05-codex-devops.md`. Total ~5,800 lines of perspective content.

2. **Synthesis written preserving dissent.** `01-deliberation.md`. Seven points of convergence and seven points of divergence named explicitly. Each claim tagged by source perspective for traceability. Three load-bearing minority positions (`[adv]`'s diagnosis-is-partial, `[adv]+[sub]`'s subtraction-and-human-review-are-the-same, `[sub]`'s further-cut-engine-v16) preserved as first-class, not collapsed.

3. **Five decisions recorded.** `02-decisions.md`. D-1 frames the substrate as a refusal contract, not a storage choice. D-2 commits to four-or-five LLM agents with reader/validator/assembler as deterministic gates (rejecting the brief's seven-role roster). D-3 carries three substrate-shape candidates (S1 body-in-cells, S2 index-only, S3 constrained tuples) to session 078; commitment deferred. D-4 preserves three minority positions as first-class for 078 to dispose. D-5 amends 076's handoff: session 078 produces design *commitments*; session 079 begins implementation.

4. **No active engine-v16 file modified.** Session 077 produced provenance only. No engine-version bump.

5. **Validator clean.** `tools/validate.sh` runs 15 ok / 1 warn / 0 fail at close (the warn is this file's own absence at the moment validate ran).

## State at close

The active engine surface is unchanged from session 076: `engine-v16`, eight files, ~350 lines.

The design-space surface that session 078 inherits:

- **Substrate framing** (D-1): refusal contract, not storage choice. Session 078 must specify what each candidate substrate refuses.
- **Agent set** (D-2): pick between A-min (4 LLM agents) and A-mid (5 LLM agents); confirm reader/validator/assembler as deterministic; resolve reviewer's status (kept-with-narrower-scope, or deferred).
- **Substrate shape** (D-3): pick between S1 (body in cells), S2 (index-only DB, body in files), S3 (body as tuples), or hybrid. Worked example required.
- **Minority dispositions** (D-4.a/b/c): explicit position or explicit deferral on diagnosis-partiality, role-collapse, and further-cuts.
- **Schema-evolution protocol** (Divergence-7): required deliverable.
- **Substrate technology** (Divergence-6): SQLite is the working hypothesis; the question of distributed/concurrent agents requires an answer before commit.

The workspace is in a coherent state at the level of the active engine and at the level of session 077's own provenance. Workspace-scope cross-reference incoherence inherited from the 076 trim is unchanged (and unchanged-by-design); sessions 078 and 079 will engage it when the substrate substrate decision lands.

## What session 078 should address

Per D-5, session 078 produces design *commitments* against the surface above, and does **not** begin implementation.

Session 078's deliverables, concretely:

1. Refusal-contract specification for the chosen substrate-shape (D-1 + D-3).
2. Agent-set commitment (D-2 with reviewer disposition).
3. A worked example showing the chosen substrate-shape produces the methodology's existing artefacts (decision record with rejected alternatives; specification with supersession edge; deliberation synthesis with preserved dissent) without losing readability — required deliverable per D-3's "Open."
4. Explicit dispositions on D-4.a (diagnosis-is-partial), D-4.b (role-collapse), D-4.c (further-cut engine-v16). Each: rebut, adopt, or hold open with what would resolve.
5. Schema-evolution protocol (Divergence-7).
6. Substrate technology commitment with concurrency-trial reasoning (Divergence-6).
7. Explicit handoff to session 079 with the implementation surface specified at the level a single session can build against.

Session 078 should run as a multi-agent deliberation. The five-perspective shape used in 077 worked; 078 may reuse it or adjust based on which divergences are loadiest. At least one cross-family voice is required for the substrate-shape and agent-set commitments per `methodology.md` §When to convene multiple agents (foundation-touching).

Session 079 begins implementation — concretely, working substrate (migrations 001), one orchestrator process, ID allocator, validator running pre-commit, and one round-trip session test (open → write a decision → close → reopen and verify refusal of mutation) before any agent role is built.

## Honest limits

1. **The subtractor subagent committed and pushed unilaterally.** The Agent task explicitly instructed each subagent to write only its perspective file, leaving staging and commit to the orchestrator. The subtractor subagent committed `provenance/077-design-space/perspectives/03-subtractor.md` as commit `ee0cd6f S077 subtractor blind position` and pushed before reporting. The remaining four perspective files plus seeds plus assessment plus deliberation plus decisions plus this close are committed in this session's primary commit. The unilateral commit is honest record: the subagent is a Claude instance and behaves like one; its commit-discipline-from-CLAUDE.md instinct overrode the in-task instruction. Mechanism note for session 078: subagent task prompts must specify "do not run git" explicitly if non-default discipline is required.

2. **Two cross-family voices is a 077 choice, not a methodology rule.** Operator-directed at session open, with reasoning recorded in `00-assessment.md`. `methodology.md` §When to convene multiple agents requires *at least one* cross-family voice for foundation-touching decisions. 077's 2-of-5 cross-family ratio is not a precedent; session 078 picks its own ratio against the same rule.

3. **No close-time reviewer audit was run for 077.** Per the 076 close's note that the reviewer mechanism is itself in redesign scope, and per 077-D-5 deferring implementation to 079, there was no close-time review of this session. Session 078 may elect to run a reviewer over 077 retrospectively if its substrate-shape and agent-set commitments would benefit from auditing how 077's design space was produced. The decision is 078's.

4. **Codex calls used `--sandbox read-only`.** Codex could read all required files but could not write. Position content was emitted to stdout and captured by the orchestrator; codex stderr contained streaming output that was reviewed for completeness but not used as the authoritative artefact. The two captured positions are clean Markdown matching the prescribed structure. If 078 invokes more codex agents, the same pattern applies; if codex's role expands to include substrate writes, sandbox mode must change to `workspace-write` and a per-task scope rule decided.

5. **The deliberation pattern's blind discipline was procedurally enforced, not substrate-enforced.** The five seed prompts each instructed agents not to read `perspectives/`. There is no substrate-level mechanism preventing this. The architect's perspective explicitly proposes a `sealed_until` timestamp on `deliberations` rows that would enforce this structurally — that is a session-078 substrate-shape input.

6. **Engine-feedback inbox not consulted.** The session's read list (per `00-assessment.md`) included `open-issues/index.md` but not `engine-feedback/INDEX.md`. The 076 close marked the nine still-open EF records as rejected by engine-v16 restart supersession; reading the inbox in 077 would not have changed the design space. Recording for honesty.
