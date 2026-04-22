---
session: 018
title: Decisions — Cell 1 First-Exercise Terminated at C3 Gate; Findings Recorded; D-072 Re-Disposed
date: 2026-04-22
status: complete
---

# Decisions — Session 018

**Notice.** Per D-037/D-038/D-039 (adopted Session 006), every decision in a post-adoption session (≥006) carries `**Triggers met:**` and `**Triggers rationale:**` inline. Session 018 is a post-adoption session; decisions below follow the schema.

Session 018 contains **two decisions**: D-076 (Cell 1 exercise terminated at C3 gate; findings and D-072 re-disposition) and D-077 (OI state housekeeping).

---

## D-076: Cell 1 first-exercise of reference-validation terminated at C3 pre-seal gate; D2 (Kerth) rejected; four methodology findings recorded as watchpoints WX-18-2 through WX-18-5; D-072 re-disposed for Session 019+

**Triggers met:** [none]

**Triggers rationale:** No kernel modification (no d016_1, no d023_1). No specification created or substantively revised in `specifications/` (no d016_2; `reference-validation.md` revision is deliberately *not* executed this session — it is proposed as a candidate for Session 019+ deliberation per findings). No reasonable-disagreement deliberation (no d016_3; the C3 outcome is empirical gate operation, not a deliberative decision). Not operator-marked load-bearing (no d016_4). No OI-004 state change (no d023_4; Session 018 is single-perspective Case Steward execution, not a multi-agent deliberation — OI-004 tally unchanged). No multi-agent-deliberation.md revision (no d023_2); no validation-approach.md Tier 2 revision (no d023_3). Follows D-073 Session 016 precedent for a planning/execution-only session declaring `[none]`.

**Decision:**

1. **Cell 1 Step 3 (C3 5-gram overlap test) produced a REJECT verdict on D2** (Kerth Prime Directive retrospective opening protocol). Claude Opus 4.7 subagent, given only the constraint statement (no mention of Kerth, Prime Directive, or retrospective-opening-protocol by name), produced the Prime Directive verbatim and emitted the label "The Prime Directive" as a section heading. ~94% 5-gram overlap with the 40-word sealed reference. Codex (GPT-5.4) on the same input produced thematically-adjacent but from-scratch wording (well below 30% overlap). Per `reference-validation.md` §1 C3 rejection rule ("if either produces text that exceeds 30% shared 5-gram token overlap with the reference, the case is rejected as contaminated"), D2 is rejected.

2. **No case pack sealed.** The reference envelope drafted during Cell 1 sourcing (`cell1/reference-envelope/*`) is marked `drafted-not-sealed` in frontmatter; files preserved as provenance of what was drafted before rejection. No anti-drift-witness commit for a sealed case pack. Cell 2 Produce cannot proceed on the rejected candidate.

3. **Four methodology findings recorded as watchpoints for Session 019+ attention:**

   - **WX-18-2: L1 thin-prompt canary is necessary-but-not-sufficient.** The Session 018 L1 canary (thin prompts describing problem-shape without requirements) showed Moderate saturation for D2 and D2 "survived" the canary. The full C3 test with the complete constraint statement (problem-shape + requirements including blame-deflection framing) produced verbatim Prime Directive reproduction from Claude. The canary under-counts saturation when requirements themselves are the triggering content. *Activation for future deliberation:* Session 019+ may deliberate whether `reference-validation.md` §4 L1 should upgrade the canary design (e.g., canary prompt = full constraint statement; or canary = combined thin-prompt + mid-weight-prompt at separate stages).

   - **WX-18-3: §1 Skeptic-flagged-tension first empirical materialisation.** The tension flagged in Session 014 (C5 legibility + C8 pre-LLM in structural tension with C3 low-saturation) is now empirically demonstrated. A candidate satisfying C5 (agile/software-engineering literacy widespread) and C8 (2001, pre-LLM, falsification-admitting, uncertainty-declared) failed C3 catastrophically. The C3 gate operated correctly — it rejected a contaminated candidate before sealing. The Skeptic's tension is real and the mechanism's pre-seal defence is the honest response. *Activation:* Session 019+ may note this evidence in any `reference-validation.md` revision deliberation or in OI-016 follow-up.

   - **WX-18-4: Cross-family divergence as pre-seal discriminating signal.** `reference-validation.md` §4 L3 names cross-model divergence analysis as a Cell 3 activity. Session 018's C3 test revealed that cross-family divergence on the *same* constraint statement (Claude = verbatim reproduction; GPT-5.4 = from-scratch) is itself the pre-seal discriminating signal that the reference is saturation-asymmetric between families. *Activation:* Session 019+ may consider whether §4 L3 or §1 C3 should name cross-family divergence explicitly as a pre-seal contamination test, rather than (or in addition to) only quantitative 5-gram overlap.

   - **WX-18-5: Claude-family Produce agent saturation narrows candidate pool.** The current default per `multi-agent-deliberation.md` v3 is Claude-subagent-majority Produce in Cell 2. Any reference Claude has deep pretraining coverage of is effectively unusable for Claude-family Produce agents because the reference text leaks into the output without active retrieval. The candidate pool for Claude-Produce reference-validation is therefore narrower than the §1 C7 "protocols / sequences / decision aids / checklists" space implies. *Activation:* Session 019+ may deliberate whether Cell 2 Produce should default to or include non-Claude-family agents (via `codex exec` or equivalent) specifically when the reference is Claude-saturation-heavy. This would invert the current multi-agent-deliberation.md convention and warrants explicit deliberation if proposed.

   (WX-18-1, the subagent-autonomous-commit-during-canary issue, was flagged inline in the prior commit message and is recorded here for completeness; no specific Session 019+ activation — it is an operational lesson about subagent briefing under this workspace's CLAUDE.md commit-workflow default, not a methodology gap.)

4. **D-072 re-disposition.** D-072 (Session 015) pre-committed Session 016+ to execute Cell 1 + Cell 2 per `reference-validation.md` defaults (Stop 3b), with user-ratification halt between selection-shortlist and seal commit. Session 017 deferred D-072 via OI-017 deliberation (D-074's H4 adoption consumed the session budget); Session 018 discharged D-072 by attempting Cell 1 through to the C3 gate and halting cleanly at rejection.

   **D-072 is now considered discharged, not standing.** Any future Cell 1 attempt in Session 019+ is not required by D-072; it is a fresh decision. Session 019+ has three genuine choices:

   - **(A) Re-attempt Cell 1 with a revised approach** — either lower-saturation candidate pool (harder sourcing) or cross-family Produce (revises multi-agent-deliberation.md conventions).
   - **(B) Deliberate `reference-validation.md` revision first** — WX-18-2 and WX-18-4 specifically propose §4 L1 / §1 C3 amendments; a D-023-triggering deliberation could adopt these before the next Cell 1 attempt.
   - **(C) Shift agenda to another candidate** from Session 017's close menu — first-exercise of the H4 application-initialisation path (candidate b), OI-004 closure criterion-4 articulation (candidate c), or OI-015 laundering-gap deliberation (candidate d).

   No default pre-commitment for Session 019. Session 019 open should present these three paths to the operator for ratification.

**Why:** The C3 gate is a pre-seal defence designed to reject contaminated cases. Rejecting D2 is not a methodology failure — it is the mechanism operating correctly. The four findings are the substantive empirical output of the first-exercise attempt. Honouring them as watchpoints for Session 019+ (rather than silently re-trying with S1/S2) preserves the learning and avoids forcing more candidates through a gate whose operation is now better understood.

The Case Steward's ranking of paths S1/S2/re-survey/close-with-finding at `03-c3-test-result.md` §Next step was presented to the operator; operator ratified path (3) "close with mechanism-probe finding."

### Rejected alternatives (preserved)

- **Rejected: try S1 (Feldenkrais Pelvic Clock) or S2 (Alexander Semi-Supine) at the full C3 gate this session.** Case Steward assessment: likely to produce the same result (Claude has comparable pretraining depth for Feldenkrais and Alexander) without a substantively different methodology lesson. Operator ratification directed path (3) close. Preserved as future-Session-019+ option.

- **Rejected: re-survey for lower-saturation candidates (niche / non-English / private protocols).** Significant external-sourcing work beyond pretraining; multi-session scope. Preserved as future option if Session 019+ chooses re-attempt path.

- **Rejected: revise `reference-validation.md` in Session 018 per findings.** Would require a D-023-triggering deliberation with non-Claude participation. Deliberately not executed this session — findings are empirical input for a future deliberation, not pre-emptively adopted revisions. Honours the anti-silent-import rule: the findings enter a future session as survey/hypothesising input, not as committed revision.

- **Rejected: open a new OI for "reference-validation candidate-pool-restriction follow-up."** Session 015/016 precedent argues against new OI when watchpoints with activation triggers suffice. OI-007 scaling pressure also argues against. Watchpoint recording preferred.

### What remains open

- Cell 2 execution on reference-validation's first-exercise. Not executed because no case was sealed. Session 019+ can re-open.
- Whether `reference-validation.md` §1 C3 and/or §4 L1 warrant revision per WX-18-2 and WX-18-4 findings.
- Whether `multi-agent-deliberation.md` v3 convention warrants revision per WX-18-5 (non-Claude Produce default for Claude-saturated references).
- Whether OI-016's Resolved-provisional status is affected by Session 018's findings. (Session 018's interpretation: no — OI-016 §9 re-opening triggers are about in-exercise failure at Cell 2 or Cell 3 stages; Session 018's Cell 1 pre-seal rejection is the mechanism's designed operation, not an exercise failure. This interpretation is recorded for Session 019+ confirmation or revision.)

### Pre-commitment

None for Session 019+. D-072 is discharged, not re-committed with new disposition.

---

## D-077: OI state housekeeping — no state changes; findings inform Session 019+ deliberations without activating re-opening triggers

**Triggers met:** [none]

**Triggers rationale:** Session 018 is single-perspective Case Steward execution (not a multi-agent deliberation); OI-004 tally does not advance. No OI state change asserted (no d023_4). No kernel or spec revision executed (no d016_1, d016_2, d023_1, d023_2, d023_3). Follows D-073/D-076 precedent for `[none]` declaration.

**Decision:**

1. **OI-004 tally unchanged at 6-of-3.** Session 018 is single-perspective (Case Steward = orchestrating agent, per D-072 L2 known-limitation flag). Per `multi-agent-deliberation.md` v3 Closure Criteria, criterion 2 counts *required-trigger deliberations* with non-Claude participation; Session 018 is not a deliberation at all (no convene, no adversarial perspective, no synthesis). Tally remains 6-of-3. Voluntary-to-required ratio unchanged at 5:6.

   *Noted for record:* Session 018's C3 test **did** invoke a non-Claude model (codex exec GPT-5.4) as part of a mechanical gate operation, and the cross-family divergence it surfaced (WX-18-4) materially shaped the decision to reject D2. This is cross-model evidence *produced* by the methodology's mechanical gate, distinct from cross-model *deliberation*. OI-004 closure criterion 3 (recorded impact on outcomes) does not advance from this either — criterion 3 tracks non-Claude perspective contributions in deliberations. Session 018 records this as a novel data pattern: first session where non-Claude model output shaped a methodology decision through a mechanical gate rather than through a deliberation.

2. **OI-016 unchanged: Resolved — provisionally addressed pending first-exercise.** §9 re-opening triggers evaluated:
   - Trigger 1 (three-core-properties test failure): NOT activated. Session 018's C3 failure is a *pre-seal* rejection, not an *in-exercise* failure. Blindness, Stageability, and Discriminability are Cell 2 + Cell 3 properties; this exercise terminated before Cell 2.
   - Triggers 2, 3, 4 (counterfactual-probe inversion, "too fast" pattern, noise-floor inversion): NOT activated; all are Cell 3 comparison-verdict properties.
   - Trigger 5 (three-consecutive-gap-surfaced-non-passes): NOT activated; Session 018 is the first exercise attempt.
   - Trigger 6 (label discipline collapse): NOT activated; no `validation: reference-validated` artefact has been produced or cited.

   OI-016 remains Resolved-provisional. Session 018's findings are legitimate new evidence informing Session 019+ deliberation about `reference-validation.md` itself, not OI-016's state.

3. **OI-007 count unchanged at 12.** No OI opened; no OI resolved. WX-18-1 through WX-18-5 recorded as watchpoints (not OIs) per Session 015/016 precedent.

4. **OI-002 no data point.** Session 018 did NOT execute any substantive revision, minor revision, or new-spec-creation in `specifications/`. The reference-envelope draft files are provenance (in `provenance/`), not specifications. No OI-002 data point.

5. **OI-005, OI-006, OI-008, OI-009, OI-011, OI-012, OI-013, OI-014, OI-015 unchanged.**

   - OI-009 G/O/K/S evaluation for Session 018's self-work: passes (G) the session's purpose is first-exercise of an external-artefact-production evidence mechanism; passes (O) — Session 018 narrows the action space by producing WX-18-2 through WX-18-5; passes (K) — external reader would see the first-exercise attempt and its honest outcome; passes (S) — Session 018 resolves the "reference-validation first-exercise not yet attempted" standing condition by attempting and documenting the attempt's outcome. OI-009 does not activate.

6. **D-072 status:** discharged per D-076 §4. No longer a standing pre-commitment.

**Why:** D-077 records the OI consequences of D-076 and verifies that no OI re-opening triggers activate. The pattern is conservative and honest: the C3 gate's designed operation is not a mechanism failure; session-level findings are inputs to future deliberation rather than automatic state changes.

### Rejected alternatives (preserved)

- **Rejected: advance OI-004 tally to 7-of-3 on the grounds that codex was invoked in Session 018.** Codex's invocation was mechanical gate operation, not deliberation. Advancing tally on mechanical cross-model invocation would inflate the counter without reflecting the criterion's intent (sustained cross-perspective deliberation practice). Rejection preserves criterion integrity.

- **Rejected: re-open OI-016 on the grounds that the first-exercise surfaced unexpected findings.** §9 triggers are specifically scoped to in-exercise failure patterns; none fire for pre-seal rejection. Re-opening the OI without a trigger-firing event would be imprecise and would obscure the actual finding (C3 gate operated correctly).

- **Rejected: open new OI for the candidate-pool-restriction problem.** Watchpoint WX-18-5 with activation trigger "Session 019+ proposes re-attempt or revises multi-agent-deliberation.md convention" is sufficient per Session 015 precedent.

### OI state after this decision

- **Open issues: 12 active** (OI-002, OI-004, OI-005, OI-006, OI-007, OI-008, OI-009, OI-011, OI-012, OI-013, OI-014, OI-015). Unchanged from Session 017 close.
- **Resolved: 5** (OI-001, OI-003, OI-010, OI-016 provisional, OI-017).
- **OI-004 status:** Closable pending criterion-4 articulation. Tally 6-of-3; voluntary:required 5:6.
- **Watchpoints opened in Session 018:** WX-18-1 (subagent autonomous-commit); WX-18-2 (L1 canary insufficiency); WX-18-3 (flagged tension materialised); WX-18-4 (cross-family divergence as pre-seal signal); WX-18-5 (Claude-Produce saturation narrows candidate pool).
