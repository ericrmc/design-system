---
session: 047
title: Path OS — Design plan artefact for external application (selvedge-disaster-response 4-5 session arc); four-perspective two-family MAD (2 Claude + 2 Codex/GPT-5.5) optimised for engine-feedback yield not disaster-response verisimilitude; D-133 M2 second-of-3 verification window exercise (populated at §5c); feedback-maximization is the primary optimisation target per operator framing; engine-v7 preservation window count 11 candidate (extends new longest further)
date: 2026-04-24
status: open
---

# Assessment — Session 047

## §1 State of the methodology at S047 open

- **Engine version loaded**: `engine-v7` (preservation window count at S047 open: 10 from S046 close). If this session preserves, count advances to 11.
- **Active specifications**: methodology-kernel v6, MAD v4, VA v5, workspace-structure v5, identity v2, reference-validation v3, read-contract v4, engine-manifest. All unchanged from S046.
- **Between-session check**: `engine-feedback/inbox/` empty; `engine-feedback/triage/` empty. External workspace `selvedge-disaster-response/` has no `provenance/` directories (Session 001 not yet run) and its `applications/001-disaster-response/brief.md` still carries `<<slot>>` placeholders (operator has not populated). Operator directly proceeds with S047 rather than the S046-anticipated external-workspace Session 001.
- **OI state**: 13 active OIs; OI-004 closed (S041 D-125); OI-019 live (S043 opened; S046 cross-linkage added).
- **First-class minorities**: 31 preserved engine-wide at S046 close.
- **Verification windows**: D-129 graduated to standing discipline at S046 (third-of-3 vindication-side); D-133 M2 at **first-of-3** vindication-side (S045 was first; S046 was single-orchestrator so M2 did not fire). **S047 is the second-of-3 M2 verification window exercise** (this session convenes MAD, so M2 matrix must be populated — see §5c).
- **Close-retention window**: most-recent-6 covers S041–S046. At S047 close, S041 rotates OUT and S047 enters (seventeenth close-rotation).
- **Cumulative post-S042 WX-24-1 MAD no-growth streak**: 19 sessions stable at 6,637 words (new-record streak tied with S045; S046 was single-orchestrator so MAD text was not edited).

## §2 Operator agenda verbatim

> Follow PROMPT.md and start the next session.
> The objective is to design a new artefact: a plan the operator can use to execute the new external application. In it will contain the stubs and evolving scenario/constraints for each of multiple sessions. Use MAD in this session to design the external application runs to get the most valuable feedback for this system's self-development.

**Operator-directed session shape**: MAD required (not single-orchestrator Path A or Path OS single-orchestrator as in S046). Target output: **a plan artefact** for operator use across multiple external-application sessions, containing per-session stubs + evolving scenario/constraints.

**Operator-declared optimisation target**: **"the most valuable feedback for this system's self-development"**. Not disaster-response verisimilitude; not plan-quality-as-artefact; not scenario realism. The plan is a vehicle for exercising and stress-testing the engine; the quality metric is engine-feedback yield.

## §3 Case Steward factual checks on operator framing

### §3a "Design the external application runs" — scope check

The operator's phrasing "design the external application runs" is plural and spans multiple sessions. The S046 brief.md as populated per the disaster-response scope described there would be one session's-worth of input. This session's artefact is at a different level: a **plan across sessions**, with per-session stubs each of which becomes a session's scope when that session runs. This is a design-meta artefact, not a session-scope artefact.

Confirmed via S046 close §6 "Halt 2 is between-sessions handoff — operator populates brief.md on own time before opening Claude Code in selvedge-disaster-response/ for its Session 001". Operator has chosen instead to delegate the brief-population to this session's design work. **That changes the handoff**: instead of operator populating the brief from their own scenario content, this session produces the plan (including scenario content + per-session stubs), and the operator uses the plan to drive the external workspace's Session 001+ (either by copying content into brief.md or by the external sessions reading the plan directly).

### §3b Feedback-yield as primary optimisation target

The operator's framing "get the most valuable feedback for this system's self-development" elevates **engine-feedback yield** above disaster-response-artefact quality. This is load-bearing: a plan designed for narrative realism may produce weak feedback (the engine chugs through competently); a plan designed to stress-test the engine's weak surfaces will produce stronger feedback.

This inverts the natural framing of an external-application brief. It means the MAD's design questions should be phrased in terms of "what design choice produces more feedback" rather than "what design choice produces a better disaster-response plan". The two may align but also may diverge; when they diverge, feedback-yield wins.

Candidate weak surfaces (to be refined by the perspectives):
- **Reference-validation void**: the scenario is fictional and self-contained, so kernel §7 Reference-validation's three-cell protocol cannot run. Does the engine gracefully default to qualitative multi-agent validation, or does kernel §7 produce friction?
- **Retroactive invalidation**: changing constraints invalidate prior assumptions. D-017 immutability says closed-session provenance is never edited. How does the engine record retroactive invalidation of assumptions without violating D-017 or silently compressing?
- **Cross-session OI lifecycle**: OIs opened in Session 001 of the external workspace may become irrelevant by Session 004 as constraints shift. Does the OI machinery (open/resolved/deferred) handle constraint-invalidation cleanly, or does it require new state-transitions?
- **Read-contract pressure**: 4-5 sessions of substantive content + per-session artefacts may pressure the §2c retention window or §2b aggregate budget in the external workspace. First-time exercise of close-rotation in a fresh workspace with no pre-Session-002 backlog.
- **Minority-preservation across constraint invalidation**: if a minority is preserved at Session 002 on assumption X, and assumption X is invalidated at Session 003, what happens to the minority? Discharge? Vindicate in reverse? Preserve orphaned? The spec does not address this.
- **Engine-feedback outbox practice**: first-ever real use of the outbox pathway. Does the schema work? Is the ergonomics of writing feedback mid-session natural or awkward?

### §3c "Plan" as artefact — placement question

The plan artefact lives in the **external workspace**, not self-dev. Rationale: the plan is operational input for the external-application executor; it belongs with the application's scope content. Self-dev's S047 provenance records the design process, not the plan itself.

Proposed placement: `applications/001-disaster-response/arc-plan.md` in the external workspace, with cross-reference from (or replacement of) the existing `applications/001-disaster-response/brief.md` Session-arc section.

Alternative: populate `brief.md` directly with the plan content, retiring the slot-template. This consolidates scope into one file but conflates static scope (problem statement, constraints-at-T0) with dynamic session-by-session content. Defer this choice to the MAD.

## §4 Path classification

**Path OS (Operator-Surfaced)**, **sixth instance** of the operator-surfaced-agenda super-class (S036 PD / S043 PSD / S044 OC / S045 OS / S046 OS-build / S047 OS-MAD-design).

Sub-class distinction from S046: S046 was operator-surfaced build-work on already-spec'd pathways (single-orchestrator; no MAD). S047 is operator-surfaced design-work with explicit operator MAD directive (multi-agent; deliberative). The taxonomic pattern flagged in S046 §4 (Path OS-D deliberative vs. Path OS-B build) is reinforced by this session's deliberative shape; still not proposing formal sub-class codification.

Frequency note: six of the last twelve sessions are Path OS (50% vs. 0% pre-S036). Tracking as forward observation at OI-019 relevance without adopting as a warrant.

## §5 Proposed work shape

**Four-perspective two-family MAD** (2 Claude subagents + 2 Codex/GPT-5.5 via `codex exec`), matching S044/S045 precedent and operator S044 R2 standing preference (Gemini operationally weaker; Codex preferred for non-Claude seats). Three-family shape rejected per R2; four-perspective chosen over three-perspective to cover four distinct concerns (plan design / scenario evolution / feedback-yield reframe / laundering-audit) without role-fusion.

**MAD triggers**: v4 §When Multi-Agent Deliberation Is Required trigger 3 ("reasonable practitioners could genuinely disagree") and trigger 4 ("load-bearing for any other reason — the plan drives an entire 4-5 session external-application arc; design choices have multi-session downstream consequences and shape the engine-feedback signal the arc produces"). Non-Claude participation: **recommended**, not required (decision does not modify kernel, MAD, VA, or OI-004 state). We convene two non-Claude perspectives anyway per Outsider 21-for-21 convention + §5.6 spirit-level sustained-exercise question + operator explicit MAD directive.

### §5a Work plan

1. **Write this assessment**; commit to establish brief-immutability anchor per MAD v4 §Brief Immutability.
2. **Halt 1** — operator ratifies: (a) shape (4-perspective two-family; 2 Claude + 2 Codex) — or proposes alternative; (b) question set Q1-Q5 below; (c) artefact output placement per §3c; (d) any scope constraints on the plan content (maximum session count? minimum feedback surfaces? operator-populated-at-T0 vs. Case-Steward-designed-at-T0?).
3. **Write shared brief** (`01-brief-shared.md`); commit before launching any perspective.
4. **Convene perspectives**:
   - P1 Plan Designer (Claude subagent via Agent tool)
   - P2 Scenario Evolver (Claude subagent via Agent tool)
   - P3 Outsider / Feedback-Yield Reviewer (Codex/GPT-5.5 via `codex exec --sandbox read-only`)
   - P4 Cross-Family Reviewer / Realist (Codex/GPT-5.5 via `codex exec --sandbox read-only`)
5. **Commit raw outputs** verbatim per MAD v4 §Non-Claude Participation Mechanism Shape A. Write manifests per Layer 2 schema.
6. **Synthesise** in `01-deliberation.md` per MAD v4 §Synthesis; preserve dissent per §Preserve Dissent.
7. **Decisions** in `02-decisions.md`. Expected shape (content TBD by deliberation):
   - D-147: adopt plan design from synthesis (triggers per deliberation outcome)
   - D-148: write plan artefact to external workspace at ratified path
   - D-149: preserve any first-class minority (if produced)
   - D-150: OI-019 cross-linkage (first real design-of-external-application as sub-question (f) data point)
   - D-151: housekeeping
8. **Write plan artefact** to the ratified location in the external workspace.
9. **Close**: `03-close.md`, SESSION-LOG.md row, `validate.sh`, commit + push. Seventeenth close-rotation.

### §5b Non-Path-A alternatives considered (D-129 standing discipline)

Per D-129 (now standing discipline after S046 third-of-3 vindication-side graduation):

1. **Path A-pure (Watch)** — rejected; operator surfaced substantive agenda with explicit MAD directive.
2. **Path OS single-orchestrator** (like S046) — rejected; operator explicitly said "Use MAD in this session". Single-orchestrator would violate operator directive and miss the adversarial-coverage MAD v4 requires for load-bearing design work.
3. **Path OS three-perspective two-family** (2 Claude + 1 Codex) — considered for budget-economy; rejected because four concerns (design / scenario / feedback-yield / laundering-audit) each warrant independent representation, and folding any two into one risks role-function under-articulation per S044 D-133 M2 synonym-drift guard.
4. **Path OS five-perspective three-family** (3 Claude + 1 Gemini + 1 Codex per S043 precedent) — rejected per operator S044 R2 standing preference (Gemini operationally weaker; Codex preferred for non-Claude seats); §5.6 spirit-level question addressed via Codex-only non-Claude participation on worst-case-side per recent sessions' pattern.

### §5c D-133 M2 Convene-time role/lineage matrix (second-of-3 verification window exercise)

Per D-133 S044, all seven columns populated before perspectives launch:

| # | Role | Function | Participant-kind | Provider / Model-family | MAD-v4-trigger | Lineage-constraint | Function-audit |
|---|------|----------|------------------|--------------------------|----------------|---------------------|-----------------|
| P1 | Plan Designer | Propose overall arc shape (session count, per-session objective + stubs, artefact progression, validation approach) targeted at feedback-yield | claude-subagent | anthropic / claude-opus-4-7 (Agent tool) | trigger 3 + 4 | none | must produce full-plan proposal that names specific engine surfaces the arc exercises (not just narrative plan content) |
| P2 | Scenario Evolver | Design the constraint-evolution mechanic — what specifically changes session-to-session (infrastructure / demand / coordination / communications per operator S046 scope answer 3); how changes are delivered (scheduled, operator-injected, emergent); how changes invalidate prior assumptions | claude-subagent | anthropic / claude-opus-4-7 (Agent tool) | trigger 3 + 4 | none | must produce evolution-mechanic design with explicit **retroactive-invalidation handling** proposal (D-017-compliant); duplicate coverage with P1 is guard — Scenario Evolver deepens the per-session-transitions that P1's arc structure contains |
| P3 | Outsider / Feedback-Yield Reviewer | Independent frame-completion / reframe on whether the proposed design is actually optimised for feedback-yield; identify gaps between P1+P2 design and actual engine weak-surfaces; suggest alternative feedback-maximising designs if warranted | non-anthropic-model | openai / gpt-5.5 via `codex exec --sandbox read-only` | trigger 3 + 4 | **lineage-constrained: Outsider role requires non-Claude per 21-for-21 convention**; Codex per operator R2 | must produce independent reframe not paraphrase of P1+P2; must cite specific engine surfaces (kernel §7, MAD v4, OI lifecycle, read-contract, reference-validation) and whether the design exercises them |
| P4 | Cross-Family Reviewer / Realist | Adversarial laundering-audit + feasibility; what shortcuts the executing sessions (external-workspace Session 001-005) might take that would compromise feedback yield; anti-laundering guards that prevent the arc from becoming ceremony | non-anthropic-model | openai / gpt-5.5 via `codex exec --sandbox read-only` | trigger 3 + 4 | none | function distinct from P3 Outsider (laundering-audit + executing-session-shortcut-risk + measurable anti-laundering guards vs. independent-reframe + feedback-yield-optimisation gaps); **synonym-drift guard per D-133 M2** — if P4 output paraphrases P3, synonym-drift observation fires |

**Lineage-constraint compliance**: Outsider seat filled by non-Claude per 21-for-21 convention (P3 Codex); S047 is 23rd post-operator-correction Outsider exercise with non-Claude in the seat. **Synonym-drift guard**: P3 vs P4 function divergence enforced by distinct role-specific stances in the briefs (P3 frame-completion + feedback-yield-reframe; P4 laundering-audit + feasibility).

**Departure discipline**: if any participant cannot be invoked as specified (e.g., Codex CLI unavailable mid-session), halt-for-explicit-operator-ratification before re-configuring.

**WX-44-2 model-version-drift discipline**: P3 + P4 manifest `model_id` values will be verified from Codex CLI startup metadata (raw-output log line 5) at commit time, not pattern-copied from prior sessions.

### §5d Question set (five questions)

Proposed for operator ratification at Halt 1:

- **Q1. Scenario at T0 + arc structure.** What is the fictional self-contained disaster-response scenario at Session 001's T0? What is the arc (session count, per-session broad objective)? Each perspective gives a concrete proposal; consolidation happens at synthesis.
- **Q2. Constraint-evolution mechanic.** What changes between sessions? How is the change delivered (operator injects new facts at session-open? changes are scheduled per session-N reveals-constraint-X? emergent from prior session's outputs?)? How is retroactive invalidation of prior assumptions recorded without violating D-017 immutability?
- **Q3. Artefact progression.** What artefact set does each session produce (system model / explicit assumptions / response plan / risks and failure points / decision trees per operator S046 scope answer 2)? Which artefacts are new per session vs. revised vs. superseded?
- **Q4. Validation approach per session.** Qualitative multi-agent per operator scope answer 4 — what specifically? Same 4-perspective shape as self-dev? Different shape per session? Reference-validation is explicitly N/A (fictional); domain-validation has no domain-actor; what fills kernel §7's three-senses void?
- **Q5. Feedback-yield optimisation (primary target).** What design choices across Q1-Q4 maximise engine-feedback yield? Which engine surfaces does the arc deliberately exercise, and which does it deliberately avoid (to keep scope bounded)? Name at least three concrete feedback surfaces the arc targets.

Cross-cutting concerns each perspective should surface in their §Honest Limits:
- Anti-laundering guards (what prevents the arc from becoming ceremony)
- Halts / operator-mediation points across the arc
- Assumptions about external-workspace executor fidelity (i.e., what the arc assumes Session 001-005 orchestrators will do that they might not)

## §6 Alternative session shapes considered and rejected

1. **Design the plan in self-dev as a specification-like artefact** (new file `specifications/external-application-plan-template.md` with per-session schema) — rejected because a single scenario-specific plan is not a reusable template; adding such a spec prematurely before the first external application arc runs would be specifying-ahead-of-evidence (mirrors §10.4-M2 concern).
2. **Write the plan as a populated `brief.md` in one pass this session** — rejected because the plan's per-session scope content is substantive design work warranting MAD (operator directive confirms); a single-file output may result from the deliberation but should emerge from synthesis, not precede it.
3. **Defer plan design to external-workspace Session 001** (i.e., external Session 001 itself designs the arc) — rejected because (a) operator explicitly directed THIS session to do the design, (b) external Session 001 would then be meta-designing its own successor sessions, which is structurally awkward and laundering-vulnerable, (c) the plan needs to exist before Session 001 to guide it.
4. **Design the plan to maximise disaster-response-plan quality, letting feedback-yield be incidental** — rejected; operator explicitly set feedback-yield as the primary optimisation target (§3b). This is the framing shift the MAD must carry through in every answer.

## §7 Honest limits at open

- **Synthesis bias risk**: Case Steward (Claude) will synthesise P1+P2+P3+P4. MAD v4 §Limitations notes synthesis is pattern's highest-risk single-agent re-entry point. Mitigation: positions tabulated per-perspective; any Claude synthesis move that contradicts Codex-prevailing convergence explicitly flagged; preserve dissent per MAD v4 §Preserve Dissent.
- **Feedback-yield is a novel optimisation target** for this engine. No prior session has explicitly optimised an external-application design for feedback yield. The MAD may produce a design that is unrealistic as a disaster-response plan (too many forced-stressed transitions; scenario incoherence) — that's acceptable per operator framing but should be declared honestly at synthesis.
- **Perspective concern overlap risk**: P1 Plan Designer + P2 Scenario Evolver both operate on "the plan"; risk of under-differentiation. Guard: P1 owns arc-level shape; P2 owns session-to-session transitions. Synonym-drift check at synthesis.
- **Non-Claude both-Codex**: §5.6 GPT-family-concentration worst-case-side data point continues (zero non-GPT non-Claude per operator R2 standing preference). Recorded transparently.
- **Plan artefact will not be validated by running it this session**. The first external-workspace session runs separately after this session closes. If the plan has gaps, they surface only at execution time and route back via engine-feedback/outbox.
- **Operator has not pre-populated brief.md**. This session effectively substitutes for brief-population: the plan artefact becomes the authoritative external-workspace scope document. If the operator still wants to override scenario specifics before Session 001 runs, that's a between-sessions operator edit — acceptable because the external workspace is outside self-dev's git control.
- **The arc may not run.** Operator may review the plan and defer / cancel / redesign. The S047 provenance records the design; execution is independent.
- **Four-question set Q1-Q5** may be insufficient if the perspectives uncover significant sub-questions. MAD v4 §Briefs allows expansion at synthesis; raw outputs may exceed the question set if needed.

## §8 Halts for operator ratification (R1-R5)

**R1. Path class and MAD shape.** Path OS with four-perspective two-family (2 Claude + 2 Codex) per §5 and §5c matrix. Accept / modify / reject?

**R2. Question set.** Q1-Q5 per §5d. Accept / drop-any / add-any?

**R3. Plan artefact placement.** Target output location in external workspace. Options: (a) `applications/001-disaster-response/arc-plan.md` alongside populated `brief.md`; (b) fully populate `brief.md` and retire slot-template with Session-arc section carrying per-session stubs; (c) `applications/001-disaster-response/arc-plan.md` + per-session-stub files at `applications/001-disaster-response/session-stubs/session-N-stub.md`. Default recommendation: (a). Ratify default / choose alternative?

**R4. Scope constraints on plan content.** Operator preference on: maximum session count (default recommendation: operator S046 scope "4-5 sessions")? Should the plan pre-script all constraint changes or leave some emergent? Should the plan designate specific engine surfaces to target for feedback, or let the perspectives choose? Defaults OK / specify?

**R5. Proceed.** On R1-R4 acceptance, convene perspectives and produce the plan artefact this session. Acknowledge proceed / halt for further clarification.

Operator single-token acceptance ("Proceed" / "Accept" / "All defaults") is sufficient; partial modifications can be listed inline.
