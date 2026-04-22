---
session: 014
title: Assessment — OI-016 Resolution with User-Steered Reference-Validation Frame
date: 2026-04-22
status: complete
---

# Assessment — Session 014

## 1. Read (workspace state)

Ran `tools/validate.sh` at session open: **323 pass, 0 fail, 0 warnings**.

Active specifications (5):

- `methodology-kernel.md` v3 (last-updated Session 011, D-060)
- `workspace-structure.md` v2 (last-updated Session 009, D-054)
- `multi-agent-deliberation.md` v3 (last-updated Session 006, D-041)
- `validation-approach.md` v3 (last-updated Session 006, D-041)
- `identity.md` v1 (created Session 012, D-063)

Superseded files preserved (7): `methodology-kernel-v1.md`, `methodology-kernel-v2.md`, `workspace-structure-v1.md`, `multi-agent-deliberation-v1.md`, `multi-agent-deliberation-v2.md`, `validation-approach-v1.md`, `validation-approach-v2.md`.

External artefacts (2 canonical, 1 superseded):

- `applications/008-morning-unfurl/morning-unfurl.md` (Session 008; Validate receipt in `provenance/009-external-validate-receipt/00-validate-user-report.md`).
- `applications/010-household-decision-protocol/house-decision-five-moves.md` v2 (Session 013 revision; Validate receipt for v1 in `provenance/013-artefact-revision/00-validate-user-report.md`; revision **not domain-validated** per user standing constraint).
- `applications/010-household-decision-protocol/house-decision-five-moves-v1.md` (superseded, preserved).

Open issues: 13 active (OI-002, OI-004, OI-005, OI-006, OI-007, OI-008, OI-009, OI-011, OI-012, OI-013, OI-014, OI-015, OI-016). 3 resolved (OI-001, OI-003, OI-010).

Most-recent session context: Session 013 revised the Session 010 artefact per the user's Validate receipt and opened OI-016 in response to the user's standing constraint on domain-validation availability.

## 2. Audit of Session 013 synthesis fidelity

The Session 013 close asked Session 014 to audit four specific questions. Findings:

**2.1 3-1 Move 5 shape split — genuine or synthesizer-reaching?** **Genuine.** The Householder's structural argument (separating two functionally distinct moments; breaking the caring-more-equals-owning-execution inheritance from Move 4) is preserved as first-class minority with an operational failure-mode falsifiability condition (WX-13-1). The adopted Move 5 text includes a deliberate structural protection targeting the Householder's primary concern — *"you both own the decision, but one of you is carrying the next steps."* The 3-of-4 majority includes the Outsider, so the convergence crosses the model-family axis legitimately. Not synthesizer-reaching for cross-model consensus; the Householder's position is operationalised as reopening warrant rather than merely recorded in dissent register.

**2.2 C4 3-1 placement split — Skeptic minority honoured with falsifiability condition?** **Partially.** The minority (single-sentence framing acknowledgment rather than body-text) is preserved with a falsifiability condition: *"if a future domain-actor reports that the conditional note reads as domain-specific scaffold rather than useful prompt … the Skeptic's single-sentence-acknowledgment alternative is the explicit warrant for moving the conditional out of Move 5 into a framing mention."* **Weakness:** the condition depends on *future domain-actor* feedback — exactly the pathway OI-016 flags as unavailable going forward. The falsifiability test is nominal-not-operable under the current domain-validation constraint. Session 014 should note this when designing a new validation pathway, because any viable reference-validation mechanism must be capable of exercising falsifiability conditions of this kind — otherwise Skeptic-preserved minorities become undemonstrable without explicit bound.

**2.3 Revised artefact text satisfies C1–C4 in the user's terms without being compressible?** **Yes.**
- C1 (Move 1 too robotic, too many constraints up front): addressed by removing the declarative example and adopting three question-openers including the user's own "Should we talk about the lounge?" phrase; explicit constraint-loosening sentence present once.
- C2 (Move 1 example line reads corporate): addressed by removing the offending line entirely.
- C3 (Move 5 must name person responsible for follow-up): addressed by Move 5 title rewrite to "Close it, and name the follow-through" and two-speaker split example.
- C4 (handling replaced items — reuse, donate, dispose): addressed via conditional note inside Move 5 using the user's own vocabulary.

One subtle concern flagged: *"you both own the decision"* uses "own" **verbally** — close to but not identical to the Outsider-flagged nominal "owner." The verbal usage is load-bearing for addressing Householder's caring-more-inheritance concern, so eliminating it would weaken the clarification. The trade-off is visible, not hidden.

**2.4 Register-drift watchlist — caught anything or ornamental?** Applied as designed. Grep of v2 for all five watchlist phrases ("surface the decision," "surface tensions," "align on," "check in on," "align on what matters") plus "owner" and "governance" returned zero matches. **Effect indeterminate:** zero-hits is consistent with either clean drafts from the start or caught-near-misses revised before commit. The "owner"-specific flag *did* demonstrably shape content — the adopted title uses "follow-through" (Outsider's preferred term) over "following up" (used by three Claude perspectives). Intent genuine; broader watchlist effect unverifiable without access to preliminary drafts.

**Overall audit verdict:** Session 013's synthesis fidelity is mostly clean, with one clearly-noted weakness (C4 falsifiability depends on unavailable pathway) and one subtle trade-off ("own" verbal usage in Move 5 clarification). The weakness in 2.2 is directly actionable by Session 014's agenda.

## 3. Agenda options considered

Per Session 013's close recommendation (D-068):

- **A.** OI-016 resolution (three-policy-choice deliberation per Session 013 Outsider framing).
- **B.** OI-004 closure — criterion-4 articulation.
- **C.** OI-015 laundering-gap deliberation.
- **D.** OI-005 broader sub-activities.
- **E.** Third external application (would trigger OI-016 activation as prerequisite, effectively forcing A first).

## 4. User ratification — specific steering

The user ratified **Option A** with the following verbatim guidance at Session 014 open:

> Option A (OI-016 resolution). No external human recruitment is possible. Artefacts will need validation to prove the methodology. You are encouraged to use additional tooling and data sources to complete the validation. For example, pick a use case that already has a proven solution documented, and see if your methodology would have produced the same artefacts knowing the same constraints, understanding this may be an iterative process, and more multi-agent use may be required in the validation step for this reason.

### 4.1 What the steering rules out

From the Session 013 Outsider tripartite frame:

- **Option (a)** "recruit alternate domain validators" — **ruled out** by "No external human recruitment is possible."
- **Option (b)** "label outputs as unvalidated" — **ruled out** implicitly by "Artefacts will need validation to prove the methodology."
- **Option (c)** "pause external-artefact production" — **ruled out** by the same reason.

### 4.2 What the steering names positively

The user has proposed a **fourth option (d): reference-validation**, with these properties:

- **Mechanism:** pick a use case with a documented proven solution; give the methodology the stated constraints; compare the methodology's produced artefact to the reference.
- **Tooling and data sources** are explicitly permitted in the validation step.
- **Iterative** — the comparison may not pass first time; iteration is expected shape.
- **Multi-agent use in validation** is **a suggestion, not a prescription.** Alternative shapes (iteration within a single session; hand-off to a subsequent session; single-agent validation; something else) are permitted. The deliberation chooses.

A follow-up steer received during brief drafting added two substantive constraints:

> For question 3, I would add that multi-agent validation was a suggestion that might not fit your methodology; it's possible a validation step might require revisiting previous steps, or rely on another session to deliberate further, it can be solved multiple ways, this is up to you. Ideally your use case simulations imply you do not have all the constraints up front, and your methodology should be able to adapt, follow the process, and continue designing the best system; at the same time you are designing the methodology itself.

Translated to design requirements:

- **Validation-step shape is open** (ruled into Q3 as a selection question rather than a prescription).
- **Reference cases should imply constraints that do not arrive all at once.** The exercise tests the methodology's capacity to absorb emergent constraints mid-run, not just to reproduce a solution from a fully-specified brief. This is a selection criterion (Q1) and a comparison-procedure requirement (Q2).
- **Co-design principle.** The methodology is being designed *at the same time it is designing*. A first-exercise that surfaces a methodology gap is a legitimate output, not mechanism failure. The pass criteria (Q6) must distinguish mechanism-failure from methodology-gap-discovery.

This is consistent with the fourth-option provision flagged in Session 013's OI-016 text: *"a fourth option (proxy validation, panel review, observational pilot, self-validation with explicit limitations) is permissible if argued."* The user has argued it — and sharpened the scope of the argument with the emergent-constraints and co-design steers.

### 4.3 Scope implication

Session 014 engages OI-016 **voluntarily** — no new external artefact is being proposed in Session 014 itself. Session 014's work-product is the **mechanism specification**. The first exercise of the mechanism is deferred to Session 015 or later, depending on what the deliberation produces. This keeps Session 014's scope bounded to design rather than also requiring proof-of-mechanism within the same session.

### 4.4 Carry-forward from Session 013

The Session 013 Skeptic's **strong-pause minority** is preserved and must be engaged by this deliberation. Its core claim ("Session 014+ should not produce new external artefacts until the validation-source question is resolved") is not refuted by the user ratifying Option (d) — it becomes a falsifiability condition for Option (d)'s adequacy. The Skeptic in Session 014 must carry it forward with new lines of attack specific to reference-validation (circularity / pretraining-contamination being the most obvious).

## 5. Selected agenda

**Session 014 agenda:** Resolve OI-016 by designing a reference-validation mechanism within the user's specified constraints.

Expected outputs:

1. Concrete mechanism specification: selection criteria for reference cases; the comparison procedure; the multi-agent validation step (if adopted); pass/partial/fail criteria; iteration shape.
2. Likely kernel §7 revision (naming a new validation sense alongside Workspace / Domain; or extending Domain; form to be deliberated). Substantive revision; file-level versioning per D-004.
3. Possible `workspace-structure.md` revision if the mechanism introduces new file-location conventions (e.g., references / fixtures / comparison records).
4. OI-016 resolution: move from **open** to **resolved** (with Skeptic's strong-pause preserved as first-class minority inside the resolution record) OR narrowed to **closable pending first-exercise** if the deliberation ends up specifying the mechanism but deferring validation of the mechanism's adequacy to first use.
5. Session 013 Skeptic strong-pause carry-forward engaged substantively, not merely noted.
6. WX-14-N watchpoints for Session 015+ first-exercise monitoring.
7. Possible minor update to `multi-agent-deliberation.md` v3 if the validation-step multi-agent shape warrants explicit recognition (likely a pointer in Open Extensions rather than substantive revision).

Expected **not** to be produced in Session 014:

- Actual execution of a reference-validation on a live case (deferred to Session 015+).
- Any external artefact in `applications/` (the mechanism specification is self-infrastructure, not external artefact).

## 6. Trigger implications (per D-023)

- **D-023_1** fires (kernel §7 modification — substantive). → Non-Claude participation **mandatory**.
- **D-023_2** likely fires (possibly `workspace-structure.md` revision, possibly `validation-approach.md` revision). → Non-Claude participation already required by D-023_1.
- **D-023_3** possibly fires (minor `multi-agent-deliberation.md` update). Non-Claude participation already required.
- **D-023_4** fires (OI-016 state change — resolution; also OI-004 criterion-3 data points extension). Non-Claude participation already required.

Therefore Session 014 is a **required-trigger deliberation**. Non-Claude participation is mandatory per `multi-agent-deliberation.md` v3. If resolution carries D-023_1 (kernel revision), OI-004 sustained-practice tally advances from 4-of-3 to **5-of-3** (fifth required-trigger deliberation with non-Claude participation — extending beyond satisfied threshold).

## 7. Perspectives selected

Four perspectives for parallel deliberation, following the Shape A pattern (D-021) used in Sessions 005, 006, 007, 008, 009, 010, 011, 012, 013:

- **01a Architect** (Claude Opus 4.7 subagent). Charged with proposing the concrete mechanism design: selection criteria, comparison procedure, multi-agent validation shape, pass/partial/fail criteria, iteration structure, kernel §7 revision wording.

- **01b Operationalist** (Claude Opus 4.7 subagent). Charged with operational viability: session-level cost (tokens, wall-clock, tool calls); reference sourcing (where proven solutions come from — academic literature, open-source, historical records, canonical examples); failure handling; tooling integration (web search, fetch, file analysis); sustainability across N sessions.

- **01c Skeptic** (Claude Opus 4.7 subagent, adversarial). Carries forward the Session 013 strong-pause minority. Primary attack line for Session 014: the circularity / pretraining-contamination concern — does reference-validation actually validate anything if LLM pretraining includes the reference? Secondary lines: reference-gaming, selection bias, reference-solution-quality variance, undemonstrable-falsifiability concerns from audit §2.2.

- **01d Outsider** (OpenAI GPT-5 via `codex exec`, Shape A per D-021). Cross-model perspective. **Load-bearing because the pretraining-contamination concern is itself a cross-model question.** If Claude and GPT-5 both reproduce a reference through retrieval rather than design, that is weaker evidence than if they independently arrive at converging outputs through methodology-driven work. The Outsider's distinct pretraining is literally a control against Claude-specific reproduction. Additionally: the Outsider contributes its own angle on candidate references and selection criteria.

Perspective choice coverage: design (Architect), operation (Operationalist), adversarial (Skeptic), cross-model (Outsider). Deliberately avoids a Historian or Surveyor role because the immediate work is mechanism design rather than candidate-case sourcing; candidate sourcing is a downstream question Session 015+ engages when first-exercising the mechanism.

## 8. Handoff

Shared brief drafted at `01-brief-shared.md`. Anchor commit hash to be recorded after commit. Non-Claude brief will be assembled from the shared brief plus the standard D-024 framing before `codex exec` invocation.
