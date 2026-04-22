---
session: 016
title: Decisions — Operator Reframing Input Assessment; OI-017 Opened; D-072 Preserved
date: 2026-04-22
status: complete
---

# Decisions — Session 016

**Notice.** Per D-037/D-038/D-039 (adopted Session 006), every decision in a post-adoption session (≥006) carries `**Triggers met:**` and `**Triggers rationale:**` inline. Session 016 is a post-adoption session; the decision below follows the schema.

Session 016 contains **one decision**: D-073.

---

## D-073: Operator reframing input surveyed and hypothesised; OI-017 opened; D-072 precommitment preserved with Cell-1-or-deliberate fork

**Triggers met:** [none]

**Triggers rationale:** This decision is a planning-record implementing the PROMPT.md anti-silent-import rule (explicit surveying/hypothesising step on operator input) and opening a new open issue. It does not modify the kernel (no d023_1), does not create or revise a specification (no d023_2, d023_3), does not change OI-004 state (no d023_4), and is not the output of a multi-perspective deliberation (no d016_1 substantive kernel, d016_2 new spec; the surveying/hypothesising step is single-perspective orchestrator work presenting options competing under §3 of `00-assessment.md`, not an originated design output requiring cross-perspective reasoning). Opening OI-017 is itself not d016_3 / d023_4: D-023.4 is scoped to OI-004 state changes; OI-017 is a new OI. The subsequent deliberation of OI-017 will be d023-triggering and will require non-Claude participation. Single-perspective decision is scope-appropriate and mirrors D-072's precedent from Session 015 (also a planning-record on user-steered agenda).

**Decision:** Session 016 ratifies **Option α** (assessment-only; defer Cell 1; open OI-017) per the `00-assessment.md` §8 recommendation, contingent on user ratification at session close. The decision's four components:

1. **Operator input surfaced through an explicit surveying/hypothesising step** per PROMPT.md anti-silent-import rule and per OI-015 laundering-enforcement concern. The step is `00-assessment.md` §3 (surveying — six related framings and their fit with the current workspace) and §4 (three competing hypotheses: H1 no reframing, H2 full reframing, H3 partial reframing). The input is not absorbed silently; three alternatives compete and remain open for subsequent deliberation.

2. **OI-017 opened** ("engine-vs-methodology reframing: separability of engine-definition from development-provenance; distinct execution prompt for external applications"). Surfaced by Session 016 operator input; activation trigger: first session electing to deliberate OI-017; preferred starting point: the three-hypothesis frame (H1 / H2 / H3) surveyed in `00-assessment.md` §4, with the explicit understanding that additional hypotheses are permissible if argued. OI-007 count increments from 12 to 13.

3. **D-072 precommitment preserved with re-disposition.** Session 015 D-072 precommitted Session 016 to execute Option A (Cell 1 of reference-validation). Session 016's ratified agenda is Option α (assessment-only), which defers Cell 1 execution to Session 017 or later. D-072 is not revoked; its execution is rescheduled. Session 017 default is to execute Cell 1 per D-072 unless the user elects to deliberate OI-017 first; either disposition preserves the precommitment in the continuity-rule sense of not abandoning it silently.

4. **Tooling status recorded.** The operator's session-open note authorised `uv tool` installations where the engine determines a tool is needed; operator ratification may be requested where required. Session 016's work-shape (assessment + OI opening) requires no new tool installation. The existing `gemini` CLI and `codex` CLI (per CLAUDE.md) are sufficient for a subsequent OI-017 deliberation's non-Claude participation; no tool-request is filed this session.

**Why:** The operator input (preserved verbatim in `00-operator-input.md`) proposes a structural reframing that names a real distinction already latent in the specifications — between *methodology-as-abstract-approach* and *methodology-as-concrete-implementation* (per `00-assessment.md` §3.1). The reframing is substantive (per §3.4), would affect PROMPT.md and plausibly `methodology-kernel.md` and `identity.md` under full adoption, and is therefore D-023-triggering under at least clause 1 (kernel revision) if H2 or certain H3 variants are adopted. Per the methodology's continuity-and-discipline rules, such revisions require multi-agent deliberation with non-Claude participation; single-perspective adoption is a specification violation. The operator explicitly stated that resolution is not required this session. The minimum-discipline response is therefore: (a) surface the input through the required surveying/hypothesising step; (b) open the OI that will host the subsequent deliberation; (c) preserve D-072 with an explicit re-disposition rather than silently defer it. This is what Option α produces.

The recommendation against Option β (execute Cell 1 and also surface the input in this session) rests on session-budget reasoning per Session 015 D-072's own judgment: "Cell 1 case sourcing includes C3 saturation-gate runs (two constraints-only produce tests per candidate) and L1 contamination-canary runs (thin prompts to ≥2 model families per candidate), which have non-trivial cost per candidate and are better executed in a dedicated session." Compounding the reframing assessment with Cell 1 in a single session would weaken both. The recommendation against Option γ (full deliberation this session) honours the operator's explicit stance that resolution is not required and avoids a premature decision on a question framed as exploratory. The recommendation against Option δ (null-response) is specification-compliance: silent deferral of the input would violate the PROMPT.md anti-silent-import rule.

### Rejected alternatives (preserved)

**Rejected: Option β (execute Cell 1 and surface input in the same session).** Compounds scope; risks rushed Cell 1 or superficial assessment. If the user wishes to proceed with Cell 1 in parallel with the reframing discussion, Session 017 can sequence them: deliberate OI-017 → execute Cell 1 OR execute Cell 1 → deliberate OI-017. Either sequence is cleaner than bundling both into one session.

**Rejected: Option γ (full multi-agent deliberation on OI-017 this session).** Overrides operator's stated stance of resolution-not-required; forces premature decision on an exploratory proposal. The operator's "Any file may be modified" authorisation permits but does not mandate an immediate deliberation; the minimum-discipline response is to surface-and-open-OI, not to decide in the same session the input was received.

**Rejected: Option δ (null-response — proceed with Cell 1 as if input had not been received).** Violates PROMPT.md anti-silent-import rule. The input, treated this way, would be silently absorbed by subsequent sessions' reads rather than explicitly surfaced as a choice. This is the exact laundering failure mode OI-015 warns against.

**Rejected: renaming `methodology-kernel.md` to `engine-kernel.md` in this session.** Premature; would pre-commit to H2 before deliberation. File remains `methodology-kernel.md` through at least the next deliberation session.

**Rejected: modifying PROMPT.md in this session** (beyond appending the operator's session-open note, which the operator placed directly). Per workspace-structure.md §PROMPT.md: "It may be revised, but any revision should be treated as a significant event and recorded in provenance." A PROMPT.md revision prior to OI-017 deliberation would be a significant-event decision made single-perspective, which is a d016_1 / d016_4 trigger that would require multi-agent. Defer to OI-017's deliberation.

**Rejected: opening a minor `engine-manifest.md` specification in this session.** Would be a new specification (d016_2); requires multi-agent deliberation. Defer.

**Rejected: immediately revising `identity.md` to say "Selvedge names the engine."** Minor-looking but substantive — changes the scope of identity.md and would constitute a specification revision (d016_2). Defer.

### What remains open

- **OI-017 (engine-vs-methodology reframing).** To be deliberated in a subsequent session electing to address it. Preferred starting point: the H1 / H2 / H3 hypothesis frame in `00-assessment.md` §4. Deliberation will be D-023-triggering (kernel revision is possible under H2/H3; PROMPT.md revision is at minimum significant-event per workspace-structure.md); non-Claude participation required.
- **D-072 execution.** Cell 1 of reference-validation remains scheduled; default is Session 017 execution unless user elects to deliberate OI-017 first.
- **Session 015 audit findings.** Preserved in this session's `00-assessment.md` §2; no new revision-triggering actions required from the audit.

### OI state after this decision

- **OI-017 opened.** New open issue. Surfaced in Session 016 via operator input. Activation trigger: first session electing to deliberate OI-017 (may be Session 017 or later).
- **OI-007 count: 12 → 13** (OI-017 added).
- **OI-016 unchanged.** Remains Resolved — provisionally addressed pending first-exercise. The six automatic re-opening triggers remain in force.
- **OI-004 unchanged.** Tally 5 of 3; Closable pending criterion-4 articulation; voluntary:required ratio 5:5.
- **OI-002 unchanged.** No revision or creation this session; no new data point.
- **All other OIs unchanged.**

### Pre-commitment

- If Session 017 proceeds with Cell 1 per D-072: the six OI-016 re-opening triggers remain in force for the Cell 1 / Cell 2 exercise. OI-017 remains open as carried-forward work.
- If Session 017 deliberates OI-017 first: Cell 1 is deferred to a subsequent session; D-072 remains in effect; any kernel or PROMPT.md revision arising from OI-017 deliberation is D-023-triggering and requires non-Claude participation.
- Either disposition honours D-072 and D-073 jointly. Which is chosen is for the user to ratify at Session 017 open or for the Session 017 orchestrator to determine if user direction is not forthcoming.
