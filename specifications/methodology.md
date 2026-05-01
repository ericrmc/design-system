---
title: Methodology
version: 12
status: active
created: 2026-04-27
updated-by-session: 161
supersedes: methodology-v11 (engine-v46); per S161 DV-S161-1 (§Roles disambiguation paragraph clarifying agent and human in post-restart context)
---

# Methodology

This file defines what Selvedge does. It is the entire kernel: what the engine is, what a session does, when to convene multiple agents, when to review at close, and how preservation works. It replaces the prior split across `methodology-kernel.md`, `identity.md`, `multi-agent-deliberation.md`, and `validation-approach.md`.

## What Selvedge is

Three layers:

- **Selvedge** — the methodology. Diverse perspectives reasoning together, producing durable artefacts, preserving reasoning, and evolving the system by running the same mechanic on its own outputs.
- **Selvedge engine** — the current loadable implementation. The set of files enumerated in `specifications/engine-manifest.md` at a given commit.
- **Application of the engine** — a specific run against a problem. Two kinds: **self-development** (the engine evolves its own specifications) and **external-problem** (the engine runs against a non-self problem).

The methodology is domain-general. The engine is a concrete realisation. An application is a particular run.

The name *selvedge* — the self-finished edge of woven cloth — names three properties: self-hosting (the methodology evolves by running its own process on itself), multi-strand preservation (disagreement preserved as first-class, not melted into consensus), and durability by construction (versioned specs, recorded supersession, provenance as a first-class output).

## How a session works

A **session** is one application of the engine. Each session reads what it needs from the workspace, decides what to advance, does the work, and closes coherently.

A session may include any subset of the following activities. They are a vocabulary, not a strict sequence. They have a general flow (you cannot decide before you deliberate) but recursion is permitted.

1. **Read** — load only what the session's work requires. Record what was loaded.
2. **Assess** — state what this session will address and why. The agenda is explicit so the next session can read it.
3. **Convene** — name the perspectives the work needs. For deliberative work, at least one perspective is adversarial.
4. **Deliberate** — perspectives state positions independently before seeing one another, then synthesise. Disagreements are preserved.
5. **Decide** — record what was decided, the reasoning that carried it, what was rejected and why, what remains open.
6. **Produce** — create or revise the artefacts the decisions warrant.
7. **Validate** — check that what was produced is consistent with the workspace and meets its stated purpose. Two senses: workspace and domain. When no domain-actor is available, Domain validation is recorded as skipped; skipping is not a third sense.
8. **Record** — commit the session's provenance to `provenance/NNN-<slug>/`.
9. **Close** — leave the workspace coherent. Audit load-bearing interpretive choices the session relied on (lift each into the assumption_register or defer via self-review forward-reference; engine-application prompts carry the close-time interpretive-choice audit clause and the typed-observation→gate promotion trigger). Commit at git. State what the next session should address.

A session that does only validation may skip Convene and Deliberate. A session that proposes a kernel revision should perform all nine.

## When to convene multiple agents

Use multi-agent deliberation when:

- The decision changes how the methodology works (a kernel revision, a deliberation-pattern change, a validation-mechanism change, a workspace-structure change).
- The question has two or more genuinely plausible positions that the author can name before deliberation.
- The author marks the work load-bearing for reasons stated in the record.

### Number

Floor of 3 valid perspectives. Target 4 for methodology-changing decisions; 3 acceptable for narrower load-bearing questions. Below the floor is consultation, not deliberation. Justify any deviation at convening time. (Per S131 DV-S131-1; restores MAD-v4 quorum after the post-restart 25-deliberation 2-default drift.)

### Selection and naming

Perspectives are chosen for **expected disagreement on this problem**. No permanent roster. The convening agent names each perspective's expected-disagreement axis at convening time. Free-form labels — but use short stable names consistently across brief, raw output, synthesis, and decision record.

### Adversarial requirement

At least one perspective is adversarial — its job is to challenge the emerging consensus, identify unstated assumptions, and argue for alternatives. Brief-writing has no other built-in adversary; this is the cheapest structural insurance against consensus-as-shared-prior.

### Cross-family

When the decision touches the methodology itself, **at least one perspective MUST come from a different model family** (different organisation; e.g., not Anthropic). The cross-family perspective surfaces assumptions a single training-distribution shares. This was Selvedge's earliest substantive finding (Session 4, pre-restart) and the property that protected the methodology's foundation against single-family bias.

For other multi-agent deliberations, cross-family is the default and strongly recommended. Absence is recorded in the decision-record with reason. Use `codex` for non-Anthropic (OpenAI) and `gemini` for Google when a third family strengthens the deliberation.

### Stance briefs

Each perspective receives a brief whose non-role sections are **byte-identical** across all LLM perspectives in the deliberation: methodology context, problem statement, design questions, evidence base, response format, constraint on external imports. Only the role-specific stance varies (150–300 words, second person, naming the *load* the perspective carries — not the *conclusion* it should reach). Diffing two LLM perspective briefs from one deliberation must reveal only the role-specific stance.

For human or domain perspectives, the briefing must convey **equivalent content** (the same context, problem, questions, and external-imports constraint) but the form may differ (verbal, conversational, written-prose) per the perspective's mode of reasoning. Equivalence of content is the discipline; byte-identicality is the LLM-specific implementation.

### Brief immutability

Briefs are committed to the workspace under `deliberations/<wno>-<slug>/` (or equivalent record path) before any perspective is launched. Briefs are not edited during the deliberation. The on-disk write-and-no-subsequent-edits is the deliberation's anchor; the git commit at session-close materialises the record into history but does not redefine the anchor.

### Independence and quorum

Each perspective:

- States its position before seeing other perspectives' positions, to prevent anchoring.
- Cites the workspace material it relied on for load-bearing claims.
- Is willing to say "I don't know" rather than fabricate.

Fewer than 3 valid outputs is not a deliberation; re-run or reformulate. A refusal is provenance, not error — preserved as the perspective's body. Do not synthesise over 1–2 perspectives.

### Synthesis

The synthesizer must not have been one of the perspectives.

- **Citation.** Every claim attributing a position to a perspective cites the source (e.g. `[P-N, Q#]` or `[P-N, section]`). Unattributed perspective-specific language is a discipline failure.
- **`[synth]` markers.** Synthesizer-original claims (not directly sourced from any perspective) are tagged `[synth]`. This lets future readers compute the sourced-vs-synthesised ratio.
- **Convergence vs coverage.** Distinguish *convergence* (all perspectives independently reached a similar conclusion) from *coverage* (one perspective raised the point; others were silent). They are different epistemic states. Record only multi-source agreement as `synthesis_points.kind='convergence'`.
- **Dissent preservation.** Disagreements are recorded as `divergence` or `minority` synthesis_points with `source_perspectives` pointing at the dissenting perspective_ids. A minority position with a strong argument is preserved as-is, not diluted.

The synthesis of perspectives **is not itself a decision**. It feeds Decide.

At every sealed deliberation the synthesizer additionally authors a `seal-grade:` engine_feedback row naming single-frame counterfactuals — positions no perspective took that the synthesis admits as load-bearing alternative readings — before `deliberation-seal` returns. The operational clause, definition, exclusions, payload shape, and v2 promotion trigger live in `prompts/development.md` §Seal-time deliberation-grading per DV-S159-1; this is the deliberation-seal sibling of the §8.5 close-time interpretive-choice audit (DV-S155-1) and is operator/agent-policed at engine-v46.

### Skipping triggered deliberation

If a multi-agent deliberation would otherwise be triggered but is not performed (because the workspace lacks a non-Claude provider, because the decision is operator-directed, because the cost is unwarranted for this scope), the reason is recorded in the session's decision record.

### Reopen on new reading

A sealed deliberation may be reopened in a follow-up session when post-close operator dialogue or new reading surfaces a **load-bearing option neither perspective named**. The follow-up session re-enters Deliberate with the new option included as a candidate shape, treating the prior synthesis as one input rather than as final. The bar is *load-bearing option neither perspective named*: minor refinements or restatements of options already present in the prior frame are not grounds. Substrate-level supersession admits this without new machinery; this convention names when reopening is appropriate so that the social cost of doing so is not the limiting factor.

When a follow-up session reopens, it cites the prior decision and the new reading or dialogue that surfaced the missed option, and treats prior perspectives' reasoning as available context — not as binding. Reopening is normal, not failure.

## When to review

Two reviewer mechanisms apply, distinguished by what the session produced.

### Coding review loop

When a session produces, modifies, or deletes **executable logic** — Python under `selvedge/`, SQL under `state/migrations/`, shell logic under `bin/` or `tools/`, or any other artefact whose execution behaviour the change alters — a reviewer subagent audits the change before the session closes. The reviewer is a distinct agent (separate context, not the implementer, not the close author) invoked with the changed files and the relevant context.

Out of scope (does **not** trigger the loop, though may still trigger the engine-definition close review below): version strings and banner text, comments and docstrings, file headers, README-equivalent prose, and shell-script changes that touch only documentation lines. The test is whether the change can alter execution behaviour. A change that only renames a variable for clarity but preserves identical behaviour is in scope (the reviewer can confirm equivalence quickly); a change that updates a comment or a version banner is not.

The reviewer reports findings classified by severity: **critical**, **high**, **medium**, **low**. Critical and high findings indicate a defect that, if shipped, would break the engine or the substrate; medium findings indicate a correctness, safety, or coverage gap that a future session should not have to clean up; low findings are nits.

For every medium-or-higher finding the implementer either:

- **Fixes** the finding (preferred), or
- **Adjudicates** the finding explicitly: records the reason for not fixing in the session's `04-review.md`, with enough detail and specific argument that a future reviewer — not this one, not the implementer — could independently judge whether the call was sound. A bare assertion of disagreement is not adjudication; the reason must engage the finding's substance. Adjudications are subject to subsequent audit by the engine-definition close reviewer or by the next session that touches the same code.

The reviewer is then re-invoked against the updated changeset. The loop continues until the reviewer reports no medium-or-higher findings remain unresolved.

**Termination and deadlock.** The session does not close until the reviewer's final pass returns clean of medium-or-higher findings. If the loop reaches a fourth iteration without converging — the reviewer keeps surfacing new medium+ issues, or the implementer adjudicates findings the next reviewer pass re-raises — the implementer halts the loop, records the unresolved findings and the iteration history in `04-review.md`, opens `OI-<session>-<slug>-findings-unresolved.md` with the full transcript, and closes the session in a halted state. A halted session is not a normal close; the next session reopens the work as its first agenda item.

The mechanism is structural, not advisory: a coding session that closes without a clean reviewer pass (or an explicit halted-state record) is invalid and the next session must reopen the work. The substrate enforces this since engine-v31 (S104, closing OI-083-001): the operator declares `sessions.kind` at open (default `coding`, alternatives `spec_only` and `meta`; immutable post-open via T-29). The `review_passes` table records each reviewer iteration with outcome ∈ {clean, findings, nonconverged} and an operator-asserted `head_sha` for staleness audit. T-30 refuses close on a coding session unless the latest review_pass is outcome=clean, or outcome=nonconverged with `halt_issue_id NOT NULL` (the halt path). T-20 is narrowed: open medium+ findings still refuse normal close, but admit the halt path so unresolved findings are recorded honestly rather than force-adjudicated. Halted-as-status-value (a third value on `sessions.status`) is deferred to OI-S104-3 because admitting it would require a calibrated rebuild of the heavily-FK'd `sessions` table; halt is currently encoded by the review_pass row's outcome on a `status='closed'` session.

The severity taxonomy (critical / high / medium / low) admits classifier disagreement at its boundaries, especially between medium and low. A worked rubric is deferred until two or three code-producing sessions have exercised the loop and produced empirical examples to calibrate against; until then the implementer and reviewer note any classification disagreement in `04-review.md`, and the implementer treats genuinely-borderline findings as medium for the purpose of the loop's termination condition. The deferral is tracked under `OI-083-002-coding-review-severity-taxonomy.md`.

This responds to constraints §2 (models treat failure as cheap; prevention must be structural) and §5 (detection without a feedback loop into prevention does not correct anything). The loop is the structural feedback path: a finding that is not addressed before close has not been detected, only noted.

### Engine-definition close review

When a session changes any engine-definition file (per `engine-manifest.md`) — including spec text, prompts, or the manifest itself — a separate reviewer audits the close at `04-review.md`, regardless of whether the change involved code. This is a single-pass audit, not a loop; its scope is whether the engine remains coherent after the change.

A session that triggers both mechanisms records both: the coding review loop's iterations and the engine-definition close review.

## Validation senses

A session's Validate activity operates at two senses:

- **Workspace validation** — the session's artefacts are internally consistent, do not contradict active specifications, and accurately describe the workspace as it is. Workspace validation applies to every session.
- **Domain validation** — when a session produces an artefact intended for use outside the workspace, and a domain-actor is available, the domain-actor reports whether the artefact functioned for its intended use. The session records the report.

When no domain-actor is available, Domain validation is recorded as **skipped: no domain-actor**. Skipping is a first-class outcome, not a defect requiring backfill, and is not a third validation sense. Workspace validation still applies; if a session needs cross-workspace coherence checks (e.g. for an external-application stage product), those checks are recorded as Workspace validation by the validating workspace.

The substrate may admit experimental validation primitives at a workspace-experimental layer when an arc lacks a domain-actor by structural condition (fictional, future-facing, or otherwise inaccessible domains). Such primitives produce substrate evidence that may inform a future kernel revision but are not themselves additional senses. Kernel-promotion questions for these primitives are tracked as open issues with explicit re-evaluation triggers and per-arc dispositions. The disaster-response arc's `reference_harness` pilot was re-evaluated at arc close and resolved as scope-change (DV-S151-1): kept workspace-experimental with named ergonomic-fix scope (OI-S151-1), kernel-promotion deferred to a second structurally-gap arc whose re-evaluation gate requires a substrate-detectable structural-trigger predicate (OI-S151-4). Sub-types and closure-shapes that the pilot surfaced as harness output are not canonicalised as kernel primitives on harness evidence alone; the typed-conflict-primitive seam was deliberated at S152 D-20 and resolved as a typed-observation pathway permitted at the workspace-experimental layer only (DV-S152-1) — nullable opt-in `conflict_kind` and `closure_kind` atoms on the harness substrate kind with no closed enum, kernel methodology names no canonical values, the migration carries through OI-S152-1 alongside OI-S151-1's ergonomic-fix coding session, and OI-S152-2 specifies the graduation-review trigger when second-arc evidence accumulates. Reachability of deliberation atoms from the artefact-set is a separate seam (OI-S151-3) and not bundled into harness disposition.

## Preservation

- **Decisions record rejected alternatives**, not just chosen options. The reasoning that led to a rejection is the input to a future decision that may reconsider it.
- **Specifications evolve through new versions, not silent edits.** When a spec is revised, the prior version is preserved (in archive or under a versioned filename) and the new version takes its place at the canonical filename.
- **Provenance is immutable after close.** Closed-session records are not edited; if a closed session contained an error, a subsequent session corrects it explicitly with a record of the correction.
- **All session work is committed to git** at close. Git history is the workspace's tamper-evident substrate.

## Roles

Two actors interact with this engine and are named throughout this kernel and the executable prompts. Their roles have shifted since the engine was first authored, and the vocabulary should be read with that shift in mind.

- **The agent** is the language-model process that opens sessions, reads the substrate, drafts decisions, runs deliberations, ships specs, runs review loops, commits, and pushes. In the post-restart engine the agent is the only CLI-runner; every `bin/selvedge submit` call is authored by the agent. Multi-agent deliberation produces multiple agent-instances within a session (one per perspective; capture and reviewer subagents are also agent-instances), but they are all the agent.
- **The human** (also referred to in older kernel text as *the operator*) directs scope, surfaces course corrections, ratifies methodology-changing decisions, names friction patterns, decides what external problems to test the engine against, and acts as the structural reviewer-subtractor. Per S075 problem statement, this is "a human reviewer with a defined scope, scheduled at predictable intervals, with the authority to reframe rather than just ratify"; per provenance/078-design-commitments §D-2 the human is one of four roles in the active agent set, the only one with subtraction authority.

Where this kernel and the prompts say *operator-policed* (DV-S130-1 temporal-claim grounding, DV-S155-1 close-time interpretive-choice audit, DV-S159-1 seal-time deliberation-grading), the meaning is *agent-policed at execution with human-as-structural-reviewer recovery via calibration-EF*. The substrate refuses what neither catches. This split is the structural defense the methodology relies on; the §Engine-feedback-pathway is the surface that makes the human-as-reviewer role deliberate rather than accidental. (Cites DV-S161-1; D-24 P-2 cross-family + P-1 + P-3 caveat.)

## Engine-feedback pathway

**Engine-feedback** is the channel for surfacing concerns about the methodology itself during the execution of an application. The human or an agent-instance records observations as `engine_feedback` rows in the substrate (engine-v26+ via `bin/selvedge submit engine-feedback`); a future session may triage feedback and act on it as a methodology revision.

The engine-feedback pathway is what allowed the human's interventions across Selvedge's seventy-five self-development sessions to become structural rather than ephemeral. A successor system should not rely on a self-correcting agent (no LLM agent has shown sustained self-correction under load); it should expect that some of its limitations will be surfaced by humans and design the surfacing path deliberately.

## Self-hosting

The methodology evolves by applying its own process to itself. Changes to this kernel pass through the same Read → Assess → Convene → Deliberate → Decide → Produce → Validate → Record → Close as any other artefact. The kernel is revised when the process it describes no longer matches the process actually followed, or when a better process is discovered.

The self-hosting property has limits. A self-applied methodology with no problem outside itself loses the falsification signal that keeps work substantive. The methodology that survives contact with a real complex-systems-design problem will be different from the one that has only been applied to itself, and only the former is the methodology Selvedge originally set out to build. Self-development is the bootstrap, not the destination.
