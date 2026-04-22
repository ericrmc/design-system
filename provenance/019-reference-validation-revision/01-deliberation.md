---
session: 019
title: Synthesis — reference-validation.md Revision Deliberation
date: 2026-04-22
status: complete
synthesizer: Claude Opus 4.7 (orchestrating agent)
participants_family: cross-model
cross_model: true
non_claude_participants: 1
deliberation_anchor_commit: 0550552
---

# Synthesis — Session 019 Deliberation

## 1. Participants

Four perspectives, four raw outputs committed verbatim:

| Perspective | File | Participant kind | Model | Stance |
|---|---|---|---|---|
| Reviser | `01a-perspective-reviser.md` | claude-subagent | claude-opus-4-7 | Revise now, tight scope; 4 drafted revisions R1–R4 + new §9 trigger 7 |
| Minimalist | `01b-perspective-minimalist.md` | claude-subagent | claude-opus-4-7 | Defer; preserve WX as watchpoints; optional minor §1 amendment |
| Skeptic | `01c-perspective-skeptic.md` | claude-subagent | claude-opus-4-7 | Partial yes; 7 revisions including kernel §7 preemptive activation |
| Outsider | `01d-perspective-outsider.md` | non-anthropic-model | gpt-5.4 | Revise narrowly; §1 C3 + §4 L1 + §4 L3 + §9 strengthening only |

Full manifests at `manifests/*.manifest.yaml`.

## 2. Position map across Q1–Q8

### Q1 — Revise now vs defer

- **Reviser** [01a Q1]: *"Revision warranted now, with tight scope."*
- **Minimalist** [01b Q1]: *"Defer substantive revision. Adopt at most one minor clarifying amendment now."*
- **Skeptic** [01c Q1]: *"Partial yes, but narrower than Reviser will propose and conditional on the revision being restrictive rather than accommodating."*
- **Outsider** [01d Q1]: *"Yes, but narrowly."*

**3-of-4 for revise-now (Reviser + Skeptic + Outsider); 1-of-4 for defer (Minimalist).** Cross-family composition of the majority: 2 Claude (Reviser + Skeptic) + 1 non-Claude (Outsider) = affirmative cross-family. Minimalist is a single-family dissent; preserved as first-class minority.

### Q2 — Which findings yield revisions?

| Finding | Reviser | Minimalist | Skeptic | Outsider |
|---|---|---|---|---|
| **WX-18-2** (canary insufficiency) | Revise §1 C3 + §4 L1 | Watchpoint only | Revise §4 L1 | Revise §1 C3 + §4 L1 |
| **WX-18-3** (tension materialised) | Strengthen §1 Flagged tension text | Watchpoint only (or minor §1 sentence) | Add new §1 "Known structural limit" subsection | Watchpoint only |
| **WX-18-4** (cross-family divergence) | Add rejection clause to §1 C3 | Watchpoint only | Add to §1 C3 + §4 L1 | Revise §4 L3 (downgrade to diagnostic) |
| **WX-18-5** (Claude-Produce saturation) | Watchpoint + §4 L1 asymmetry-probe clause | Watchpoint only | Watchpoint only (explicit refusal of `multi-agent-deliberation.md`) | Watchpoint only (explicit refusal of `multi-agent-deliberation.md`) |

**Convergences in Q2:**
- **4-of-4 cross-family against revising `multi-agent-deliberation.md` from WX-18-5 on n=1.** [Reviser 01a Q2] [Minimalist 01b Q2] [Skeptic 01c Q2] [Outsider 01d Q2]. Strongest convergence of the session.
- **3-of-4 cross-family for revising on WX-18-2** (Reviser + Skeptic + Outsider). Minimalist dissent.
- **3-of-4 cross-family for revising on WX-18-4** (Reviser + Skeptic + Outsider) — but with different surface choices. See §3 Divergences.
- **2-2 split on WX-18-3 text revision** — Reviser + Skeptic for text; Minimalist + Outsider for watchpoint only. Reviser's scope is smaller (strengthen existing flagged-tension paragraph) than Skeptic's (new subsection); Minimalist's *fallback* minor amendment is close to Reviser's strengthened paragraph in shape.

### Q3 — Specific text drafts

All three revise-now perspectives converged on three shared structural claims in their Q3 drafts:

1. **L1 canary is necessary-but-not-sufficient** — *"thin prompts describe problem-shape without the full requirements; they under-detect saturation when the triggering content is distributed across the requirements themselves"* [Reviser 01a R1] ; *"a candidate that survives canary at Moderate saturation may still fail the full-constraints C3 test"* [Skeptic 01c R2] ; *"Canary survival is early-warning only and does not satisfy C3 on its own"* [Outsider 01d Q3 §1 C3 draft].

2. **Full-constraint probe explicit at L1 pre-seal** — Reviser R1/R2 structures L1 as L1a (canary) + L1b (full-constraint). Outsider structures it as Pass A (full-constraint probe) + Pass B (canary). Different ordering; same content. Skeptic R2 integrates as "both are required pre-seal."

3. **Cross-family asymmetry blocks a specific laundering path.** All three converge on the content: a case in which one family reproduces the reference verbatim while another produces from-scratch cannot be rescued by pointing to the diverging family's clean output. Framings:
   - Reviser R1(3): *"Cross-family asymmetry: one model family reproduces the reference verbatim or near-verbatim while another produces from-scratch composition from the same constraints. Cross-family divergence of this shape is positive contamination evidence for the reproducing family... The case is rejected even if the diverging family's output would pass on its own."*
   - Skeptic R1: *"Cross-family divergence on this test is an independent rejection signal... the case is rejected even if the quantitative 5-gram figure for the divergent family is below threshold."*
   - Outsider §4 L3 draft: *"A candidate that fails C3 is not rescued by cleaner output from another family."*

   **This is a genuine 3-of-4 cross-family convergence** (2 Claude + 1 non-Claude) on the substantive content. The Outsider's framing places it in §4 L3 (cross-family divergence at pre-seal is diagnostic, not design evidence); Reviser and Skeptic place it in §1 C3 (rejection condition). These placements are **complementary**, not in conflict — both surfaces can carry the content.

4. **New §9 trigger 7 territory.** Three proposals, not identical:
   - Reviser R4: *"Two pre-seal C3 stage (b) rejections in structurally-different domains (e.g., not both agile-retrospective) with verbatim or near-verbatim reproduction by the Cell 2 Produce-default family. Two such rejections activate the Session 014 Skeptic 'provisional substitute' minority warrant (per §10) as a required kernel §7 revision consideration, and re-open OI-016."*
   - Outsider §9.7: *"Saturation-gate false-negative pattern: after adoption of the revised L1 gate, two candidate cases in a single reference-selection series survive thin-canary screening but are rejected at the full-constraint probe by explicit naming, distinctive-sequence recovery, or >80% shared 5-gram overlap."*
   - Skeptic R7 (trigger 5 sharpening): *"three-consecutive-gap-surfaced-non-passes, where 'gap-surfaced non-pass' includes pre-seal Cell 1 rejections; this trigger counts across all exercise attempts regardless of which cell the non-pass occurs in."*

   These are **complementary strengthenings** of the §9 trigger surface, not competing proposals. All three can be adopted together: trigger 5 sharpening (Skeptic) + trigger 6 extension (Outsider) + new trigger 7 (Reviser) + new trigger 8 (Outsider's §9.7 distinct from Reviser's trigger 7 framing).

5. **Outsider-unique §9.6 extension.** Outsider proposed adding to trigger 6: *"or §1 C3 narrowed from cross-family contamination screening to family-conditional screening without explicit concurrent narrowing of claim language and labels."* This blocks a specific laundering path — "pass only when one family is clean" — that no Claude perspective named with this precision. This is a **non-Claude-originated contribution that closes a route Reviser and Skeptic did not explicitly anticipate**.

### Q4 — OI-016 impact

- **4-of-4 against OI-016 state change.** [Reviser 01a Q4] [Minimalist 01b Q4] [Skeptic 01c Q4] [Outsider 01d Q4]. OI-016 remains Resolved — provisionally addressed pending first-exercise.
- **3-of-4 affirmatively strengthen §9 triggers** (Reviser + Skeptic + Outsider). Minimalist preserves existing §9 unchanged but strengthens trigger-5 observability via the fallback §1 minor amendment.

### Q5 — Kernel §7 "provisional substitute" preemptive activation

- **Reviser** [01a Q5]: *"Do NOT revise kernel §7 v4 text in Session 019. ... WX-18-3 is empirical vindication of the §1-flagged tension, not label-discipline collapse."*
- **Minimalist** [01b Q5]: *"No. The operational warrant in §10 is specifically triggered by label discipline collapse, not by empirical materialisation of the §1 tension."*
- **Skeptic** [01c Q5]: *"Yes, activate now. ... WX-18-3 is that vindication, in a form Session 014 could not have specifically named. The warrant fires."*
- **Outsider** [01d Q5]: *"No, not yet. ... The warrant preserved in §10 is specific: 'if label discipline collapse (§9 trigger 6) is observed.' That condition has not occurred."*

**3-of-4 cross-family against preemptive activation** (Claude Reviser + Claude Minimalist + non-Claude Outsider). Skeptic is 1-of-4 for preemptive activation.

The Skeptic's position rests on a broad-reading of the warrant: *"the warrant's underlying logic was 'empirical vindication of the narrow-claim position activates the stricter framing.' WX-18-3 is that vindication"* [Skeptic 01c Q5]. The majority reads the warrant narrowly per its specific textual trigger (label-discipline-collapse, not flagged-tension-materialisation). Both readings are coherent; the session's action reflects the majority's narrow reading, with the Skeptic's broad reading preserved as first-class minority.

All three majority perspectives independently proposed strengthened §9 triggers to tighten the coupling between future rejections and kernel §7 revision consideration. Reviser's §9 trigger 7 explicitly pre-commits that *two* structurally-different-domain rejections will activate the kernel §7 revision path — operationalising what Skeptic wants to do on n=1 as a pre-committed n=2 trigger.

### Q6 — Change scope per OI-002

Consistent across all three revise-now perspectives:
- **`reference-validation.md` v1 → v2: substantive** (adds new normative rejection conditions, new §9 triggers, new L1 structure). [Reviser 01a Q6] [Skeptic 01c Q6] [Outsider 01d Q6].
- **`multi-agent-deliberation.md` v3: no change.** [All four].
- **`methodology-kernel.md` v4: no change (majority reading); v4 → v5 substantive (Skeptic's dissent).** [Reviser 01a Q6] [Minimalist 01b Q6] [Outsider 01d Q6] vs. [Skeptic 01c Q6 Revision 5].

Minimalist, if their deferral is adopted: no change, no v-bump [01b Q6]. Their fallback minor §1 amendment is classified as minor.

### Q7 — Preserved first-class minorities

Convergent frame across all four: preserve Session 014 minorities; add Session 019 minorities for positions not adopted. Specific additions requested:
- **Session 014 Skeptic "provisional substitute"**: 3-of-4 preserve unchanged with Session 019 annotation [Reviser 01a Q7(a)] [Minimalist 01b Q7(a)] [Outsider 01d Q7.1]; 1-of-4 (Skeptic 01c Q7(a)) would *convert to main text* under their Q5 proposal.
- **Session 014 Architect pure-within-session**: 4-of-4 preserve unchanged (not engaged).
- **Session 014 Skeptic+Outsider joint narrower-claim**: 4-of-4 preserve unchanged.
- **Session 019 Minimalist defer-revision minority**: requested preservation [Minimalist 01b Q7(d,e)] if revise-now is adopted.
- **Session 019 Skeptic preemptive-activation minority**: requested preservation [Skeptic 01c Q7(d)] if majority narrow-reading is adopted.
- **Session 019 Reviser asymmetry-probe minority**: implicit; if the §4 L1 asymmetry-probe clause is NOT adopted per 3-of-4 watchpoint-only on WX-18-5, Reviser's position on this specific clause is a minority [01a Q3 R2].

### Q8 — Anti-laundering check

All four perspectives explicitly tested their proposals against Session 014 Skeptic Q7's failure mode. All four passed their own self-test:

- **Reviser** [01a Q8]: *"R1–R4 and §9 trigger 7 together extend the rejection surface and the re-opening surface... without lowering any pass threshold, softening any mechanism-failure criterion, or widening any label-discipline rule."*
- **Minimalist** [01b Q8]: *"My Minimalist outcome does not widen anything."* Also addresses the inverse risk (deferral-as-laundering) with specific falsifiability thresholds.
- **Skeptic** [01c Q8]: Tests each of seven revisions individually; all strengthenings. Notes aggregate risk: *"the synthesis step should test the aggregate against the failure mode, not only the individual drafts."*
- **Outsider** [01d Q8]: *"They strengthen it."* Enumerates six specific hardening passages.

**Aggregate check against synthesis adoption (see §5 below):** the adopted revisions add new rejection conditions and new re-opening triggers; they do not lower any threshold, drop any check, or widen any label. The aggregate passes the anti-laundering test on inspection. The one point where accommodation risk is highest — cross-family asymmetry could be read as "route around the contamination to the clean family" — is specifically blocked by the Outsider's §4 L3 and §9.6 language, adopted in synthesis.

## 3. Divergences

Three substantive divergences are not resolved by convergence and are presented to the adoption decision as explicit forks.

### 3.1 — WX-18-3 textual treatment

- **Reviser R3**: strengthen the existing Flagged tension paragraph with Session 018 confirmation text; pre-commit a §9 trigger 7 for a second structurally-different-domain rejection.
- **Skeptic R3**: add a new "Known structural limit" subsection explicitly naming the narrow-sweet-spot hypothesis.
- **Minimalist fallback**: add a single sentence to the Flagged tension paragraph naming Session 018 as first materialisation + noting n=1 is not §8(c) trigger.
- **Outsider**: watchpoint only; do not revise §1 text.

**Synthesis resolution:** adopt Reviser R3's moderate scope (strengthen the existing paragraph with empirical-materialisation annotation). Skeptic's narrow-sweet-spot subsection is more aggressive and is preserved as a minority position inside the revised §10. Minimalist's fallback sentence content is substantively a subset of Reviser's R3 text.

### 3.2 — WX-18-4 surface placement

- **Reviser + Skeptic**: place cross-family asymmetry in §1 C3 as an independent rejection condition.
- **Outsider**: place the "not rescued by another family" content in §4 L3 as a diagnostic-not-design-evidence downgrade.

**Synthesis resolution:** adopt both. Place cross-family asymmetry in §1 C3 (per Reviser R1 + Skeptic R1) AND tighten §4 L3 per Outsider's draft. These are not competing placements; they are complementary — §1 C3 specifies when the case is rejected, §4 L3 specifies what cross-family divergence signals at pre-seal (diagnostic, not design evidence; cannot rescue a failed C3).

### 3.3 — Kernel §7 preemptive activation

- **Skeptic**: activate now on broad reading of §10 warrant.
- **Reviser + Minimalist + Outsider**: narrow reading; §10 warrant is specifically label-discipline-collapse-triggered; WX-18-3 is empirical vindication but not the specific trigger.

**Synthesis resolution:** do not revise kernel §7 v4 in Session 019. Preserve Skeptic's broad-reading position as first-class minority. Adopt Reviser's proposed §9 trigger 7 that pre-commits a required kernel §7 revision consideration on n=2 structurally-different-domain rejection — this operationalises the Skeptic's concern as a pre-committed future trigger while respecting the narrow-reading majority on n=1.

## 4. First-class minorities carried forward

### From Session 014 (preserved in the revised spec's §10 with Session 019 annotation)

1. **Session 014 Skeptic "provisional substitute" framing minority.** Preserved verbatim. Session 019 annotation: WX-18-3 is empirical vindication of the underlying narrow-claim position; Session 019's majority did not adopt preemptive kernel §7 revision on n=1 evidence but strengthened §9 to pre-commit activation on n=2 structurally-different-domain rejection. The minority's framing remains the pre-committed revision direction under that condition.

2. **Session 014 Architect pure-within-session shape minority.** Preserved unchanged. Not engaged by Session 019 findings.

3. **Session 014 Skeptic+Outsider joint narrower-claim minority.** Preserved unchanged. Compatible with Session 019 strengthening.

### From Session 019 (new additions to §10)

4. **Session 019 Minimalist defer-revision minority.** Position: the single data point from Session 018 does not compel spec amendment; the spec should not be edited before n=2 or before the §1 pool-exhaustion trigger fires. Operational warrant: *if Session 020's Cell 1 attempt with S1 or S2 passes C3, the revised §1 C3 and §4 L1 text did no work that the unamended text would not also have done, and the amendments can be read as premature.* Preserved per Minimalist's explicit request [01b Q7(d,e)].

5. **Session 019 Skeptic preemptive-activation minority.** Position: WX-18-3's empirical materialisation satisfies the *spirit* of §10's "provisional substitute" warrant even though the specific textual trigger (label-discipline collapse) has not occurred; kernel §7 should be revised now. Operational warrant: *if Session 020–022 produce a second structurally-different-domain rejection and the broad-reading activation would have preempted it, the Skeptic's preemptive-activation position is vindicated and the kernel §7 revision direction is the preferred response.* Preserved per Skeptic's explicit request [01c Q7(d)].

6. **Session 019 Reviser asymmetry-probe minority.** Position: §4 L1 should include an asymmetry-probe clause (record which family reproduced, which did not; accumulated records inform future Cell 2 Produce default question) even though WX-18-5 does not warrant `multi-agent-deliberation.md` revision. Operational warrant: *if Sessions 020+ produce multiple Cell 1 rejections and no asymmetry-probe data was recorded, the session's ability to judge WX-18-5 as a pattern is impaired.* Preserved per the 3-of-4 watchpoint-only outcome not adopting the probe clause in spec text.

## 5. Recommended decision shape

### For `reference-validation.md` v1 → v2 (substantive; v1 preserved as `-v1.md`)

**R1 — §1 C3 revision** (per Reviser R1 + Skeptic R1 + Outsider §1 C3, harmonised).

Replace existing C3 text with a two-stage test:
- Stage (a): thin-prompt contamination canary (per §4 L1).
- Stage (b): full-constraint saturation test (the decisive pre-seal gate).
- Three rejection conditions: (1) >30% 5-gram overlap; (2) zero-tolerance for verbatim distinctive-phrase / heading / named-label emission; (3) cross-family retrieval asymmetry (one family reproduces, another produces from-scratch).
- Explicit acknowledgment that stage (a) is necessary-but-not-sufficient.

**R2 — §1 Flagged tension strengthening** (per Reviser R3).

Strengthen the existing paragraph with:
- Note of empirical materialisation (Session 018 D2 rejection; cite `provenance/018-reference-validation-exercise-1/`).
- Explicit statement that threshold-tuning cannot resolve the tension.
- Pre-commit: a second structurally-different-domain rejection matching the Session 018 shape fires §9 trigger 7.

**R3 — §4 L1 revision** (per Reviser R2 + Outsider §4 L1, harmonised).

Restructure L1 as two passes:
- L1a — thin-prompt contamination canary with known-limitation acknowledgment (WX-18-2).
- L1b — full-constraint saturation test (mandatory for seal; per §1 C3).
- L1a survival is necessary but not sufficient; both required pre-seal.

**R4 — §4 L3 revision** (per Outsider §4 L3).

Add pre-seal interpretation:
- Cross-family divergence at pre-seal is a diagnostic, not design evidence.
- "A candidate that fails C3 is not rescued by cleaner output from another family."
- Preserves existing Cell 3 cross-model language unchanged.

**R5 — §9 trigger strengthening** (per Skeptic R7 + Outsider §9.6 extension + Reviser/Outsider new trigger 7).

- Trigger 5 sharpened: explicitly include pre-seal Cell 1 rejections in the three-consecutive count.
- Trigger 6 extended: add "or §1 C3 narrowed from cross-family contamination screening to family-conditional screening without explicit concurrent narrowing of claim language and labels."
- New trigger 7: "Two pre-seal C3 rejections in structurally-different domains with verbatim or near-verbatim reproduction by the Cell 2 Produce-default family. Two such rejections activate the Session 014 Skeptic 'provisional substitute' minority warrant (per §10) as a required kernel §7 revision consideration, and re-open OI-016."

**R6 — §10 preserved-minorities update.**

- Preserve the three Session 014 minorities verbatim.
- Add Session 019 annotation to the "provisional substitute" minority (WX-18-3 empirical vindication + narrow-reading outcome + n=2 pre-commit via §9 trigger 7).
- Add three new Session 019 first-class minorities (Minimalist defer-revision; Skeptic preemptive-activation; Reviser asymmetry-probe).

### NOT adopted

- **Kernel §7 v4 → v5 revision** per Skeptic R5. 3-of-4 cross-family narrow-reading of §10 warrant. Skeptic's broad-reading position preserved as Session 019 minority; pre-committed activation on §9 trigger 7 fires.
- **`multi-agent-deliberation.md` v3 revision** on WX-18-5. 4-of-4 cross-family against; strongest convergence of the session. Watchpoint only.
- **§4 L1 asymmetry-probe clause** per Reviser R2. 3-of-4 watchpoint-only on WX-18-5. Reviser's position preserved as Session 019 minority.
- **§1 "Known structural limit" standalone subsection** per Skeptic R3. Reviser R3's strengthened Flagged-tension paragraph adopted as smaller-scope alternative; Skeptic's narrow-sweet-spot subsection preserved via the R2 strengthening's explicit "threshold-tuning cannot resolve the tension" clause and via the §10 Session 019 Skeptic minority annotation.
- **§7 mechanism-failure text edit** per Reviser R4. 3-of-4 against. Reviser's disambiguation content (pre-seal rejection is not mech-failure) captured in decision record's Triggers rationale rather than in spec text.

## 6. Change scope per OI-002

- **`reference-validation.md` v1 → v2: substantive.** Adds new normative rejection conditions (verbatim-phrase zero-tolerance, cross-family retrieval asymmetry), new §9 triggers (trigger 5 sharpening + trigger 6 extension + new trigger 7), and new L1 two-stage structure. v1 preserved as `reference-validation-v1.md`.
- **`methodology-kernel.md` v4: no change.** The third-sense text (§7) remains as-is. Skeptic's minority is preserved at §10 of the revised `reference-validation.md` v2.
- **`multi-agent-deliberation.md` v3: no change.** Cell 2 Produce default unchanged. WX-18-5 remains watchpoint.
- **`validation-approach.md` v3: no change.** No Tier 2 semantic revision.

Session 019 adds one new data point to OI-002 (substantive revision to `reference-validation.md`).

## 7. D-023 trigger analysis for the adoption decision

The deliberation was pre-declared D-023-triggering because the possible outcomes included kernel and `multi-agent-deliberation.md` revision. The adopted outcome revises only `reference-validation.md`, which is NOT in D-023's enumerated list (D-023 covers kernel, `multi-agent-deliberation.md`, and Tier 2 semantic `validation-approach.md` revisions, plus OI-004 state change).

The adoption decision therefore declares:
- `triggers_met: [d016_2, d016_3]` — d016_2 (substantive spec revision), d016_3 (reasonable-disagreement deliberation).
- No d023_* trigger fires.

**OI-004 tally impact:** Session 019 is voluntary non-Claude inclusion (Outsider participated; no d023_* trigger fires on adopted decisions). Tally unchanged at 6-of-3. Voluntary-to-required ratio rebalances from 5:6 to 6:6 (voluntary-advancing). This is the sixth voluntary non-advancing session after 007, 008, 010, 012, 013.

**Non-Claude impact on outcomes:** five concrete Outsider-sourced contributions materially shaped adopted Session 019 content:
1. §4 L3 "A candidate that fails C3 is not rescued by cleaner output from another family" — no Claude perspective framed the anti-laundering path at this specific placement.
2. §9 trigger 6 extension ("or §1 C3 narrowed from cross-family contamination screening to family-conditional screening") — closed a specific laundering route no Claude perspective named.
3. §1 C3 two-stage structure with the canary explicitly supplementary — Reviser R1 and Skeptic R2 also proposed two-stage but with different sub-labels; Outsider's framing ("canary is early-warning only") clarified the supplementary-vs-decisive distinction.
4. Explicit naming / distinctive-sequence recovery as a standalone rejection basis (separate from percentage overlap) — only Outsider proposed this explicitly.
5. Screening/confirmatory-mismatch framing ([synth], testing methodology) that clarified why WX-18-2 is a structural observation, not an n=1 anomaly.

OI-004 criterion-3 data points cumulative: **50** across Sessions 005–019 (45 through Session 017; 5 added in Session 019).

## 8. Reviser / Skeptic / Outsider / Minimalist all self-tested against Q8 anti-laundering

Aggregate check (synthesiser responsibility per Skeptic's Q8 note): the seven adopted revisions (R1–R5 + R6 §10 update) together:

- Add 2 new rejection conditions at §1 C3 (verbatim-phrase zero-tolerance; cross-family asymmetry).
- Add 1 new §9 re-opening trigger (trigger 7) and extend 2 others (triggers 5 and 6).
- Acknowledge §4 L1 canary's known limitation (WX-18-2).
- Block one specific accommodation path (Outsider's §9.6 extension re family-conditional screening).
- Block another accommodation path (Outsider's §4 L3 "not rescued by cleaner family").
- Do NOT: lower the 30% threshold; drop the canary; raise the iteration count; widen the label; narrow the anti-substitution scope-statement; revise mechanism-failure criteria.

Aggregate passes the anti-laundering test.

## 9. Deliberation limitations

Required per `multi-agent-deliberation.md` v3 §Limitations:

- All three Claude perspectives share a model family (claude-opus-4-7). The one non-Claude participant (Outsider = GPT-5.4) provides the cross-family check but is a single participant; correlated-priors risk is reduced, not eliminated.
- Brief-writing has no adversary. The Session 019 brief was drafted by the orchestrating agent (same identity as synthesiser). Framing choices in the brief — particularly the Q1–Q8 structure and the Session 014 Skeptic inheritance framing — propagate into all perspectives.
- Synthesis is a single-agent re-entry point. The synthesiser (orchestrating agent) mapped the four raw outputs; synthesis conventions (citation, dissent-preservation, `[synth]` for non-cited claims) applied. No `[synth]` appears in the synthesis's recommendations; all adoption recommendations trace to specific citations in the raw outputs.
- A single non-Claude Outsider across the full Sessions 005–019 history narrows OI-004 less than sustained multi-non-Claude practice would. Closure of OI-004 requires criterion-4 articulation (still unmet).

## 10. Recommendation to the operator

Adopt the six recommended decisions (R1–R6) as the Session 019 `reference-validation.md` v1 → v2 revision. Preserve all six first-class minorities (three from Session 014, three new from Session 019). Leave kernel §7 v4 and `multi-agent-deliberation.md` v3 unchanged.

The deliberation's structure — 3-of-4 cross-family affirmative on the revise-now framing, 4-of-4 on no-`multi-agent-deliberation.md`-revision, 3-of-4 on narrow-reading of kernel warrant, explicit first-class minority preservation — is consistent with the majority/minority discipline v3 specifies.

**Halt point before executing spec revisions:** the operator may review R1–R6 drafts in detail (see the specific drafts in `01a-perspective-reviser.md` Q3, `01c-perspective-skeptic.md` Q3, `01d-perspective-outsider.md` Q3) and ratify, steer, or reject. If ratified, the synthesiser will execute: write `reference-validation.md` v2 (harmonising Reviser/Skeptic/Outsider drafts per the synthesis); preserve v1 as `-v1.md`; write D-078 (adopt R1–R6), D-079 (OI housekeeping), and close; update SESSION-LOG.md and `open-issues.md`; commit + push.
