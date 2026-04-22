---
session: 014
title: Decisions — OI-016 Resolution
date: 2026-04-22
status: complete
---

# Decisions — Session 014

## D-069: Adopt reference-validation mechanism; revise kernel §7; create new specification

**Triggers met:** [d016_1, d016_2, d016_3, d016_4, d023_1, d023_2]

**Triggers rationale:** The decision modifies `methodology-kernel.md` (d016_1, d023_1) with a substantive §7 revision (v3 → v4 per OI-002's five-point heuristic — new named validation sense, new normative content, new anti-substitution clause, new label discipline). The decision also creates `specifications/reference-validation.md` as a new v1 specification with `supersedes: none` (d016_2, d023_2) — the Session 012 D-063 precedent for single-purpose-spec creation. Reasonable practitioners disagreed (d016_3) across multiple axes: 3-1 cross-model split on Q3 validation shape (Architect within-session vs Operationalist+Skeptic+Outsider hand-off hybrids); 3-1 split on Q5 framing (third-sense-with-anti-substitution vs Skeptic's provisional-substitute); variance on Q2 iteration count (1 to 3); 2-2 split on Q6 pass-threshold strictness crossing the model-family axis (Skeptic+Outsider strict vs Architect+Operationalist middle-to-loose). Operator-marked load-bearing (d016_4) because this is the session's primary work-product and the mechanism's adoption gates all future external-artefact work. d023_1 fires: non-Claude participation mandatory; Outsider (OpenAI GPT-5 via `codex exec`, session id `019db2bf-92cb-7771-b828-7eb85da11efe`, reasoning effort xhigh, 30,685 tokens) present in deliberation with full D-024 manifest; six concrete Outsider-sourced contributions materially shaped adopted content — see Key arguments below. d023_2 fires on spec creation; non-Claude participation present. d023_3 not triggered (multi-agent-deliberation.md not revised). d023_4 not triggered in this decision (OI-004 state change is D-071's work per Session 011 D-062 precedent).

**Decision.** Revise `methodology-kernel.md` v3 → v4, replacing §7 Validate. Preserve v3 as `methodology-kernel-v3.md` (status: superseded). Create new specification `specifications/reference-validation.md` v1 containing the mechanism detail per the synthesis Q1–Q7 content.

### Kernel §7 v4 replacement text

```markdown
#### 7. Validate

Validate the session's output at each level on which it makes claims. Three senses apply.

**Workspace validation** applies to every session. Check that:
- New specifications don't contradict existing ones
- Specifications describe the workspace as it actually is
- Provenance records are complete and well-formed
- Open issues reflect the actual state of uncertainty

**Domain validation** applies when a session produces or revises an artefact intended for use outside the workspace and a domain-actor is available. Obtain evidence from the domain-actor who holds the problem the artefact addresses — the user of a sequence, the reader of a specification, the participant in a process, or an equivalent — that the artefact functioned for its intended use. Record who performed the validation, what was tried, what happened, and whether modifications were requested. Domain validation may complete out-of-session; when it does, the receiving session records the report and decides whether it triggers revision.

**Reference validation** applies when a session produces an external-intent artefact and no domain-actor is available. A reference-validation exercise pairs the methodology's Produce step (run blind against a staged constraint tranche set whose emergent constraints surface during the run) with comparison against a pre-selected documented proven solution the Produce agents do not see. The exercise runs across a small number of sessions in a sealed three-cell protocol (Curation, Produce, Validation) specified in `specifications/reference-validation.md`. The exercise records constraint-satisfaction, structural correspondence, cross-model divergence, and a contamination audit.

**Reference validation supplies evidence about the methodology's capacity to derive artefacts under stated constraints. It does not establish that the artefact functioned in its intended use. It does not substitute for Domain validation when a domain-actor is available.** Artefacts passing reference-validation carry the label `validation: reference-validated` in frontmatter and retain that scoping in any later citation.

If any validation reveals problems, they are either fixed in this session (return to Produce) or recorded as open issues for subsequent sessions.
```

### New specification file

Create `specifications/reference-validation.md` v1 with the mechanism's full operational detail. Content outline:
- Purpose and scope (what reference-validation is for, what it does not establish).
- The eight selection criteria (C1–C8 per synthesis Q1).
- The five-stage comparison procedure (Q2 synthesis).
- The sealed three-cell protocol (Curation / Produce / Validation) with role definitions (Q3 synthesis).
- The seven-layer contamination defence stack (L1–L7 per synthesis Q4).
- Pass criteria at artefact and methodology levels (Q6 synthesis).
- Mechanism-failure vs methodology-gap distinction (three-core-properties test per Outsider Q6(c)).
- Label discipline (`validation: reference-validated` frontmatter tag).
- Required per-exercise artefacts (`brief-gatekeeper.md`, `contamination-audit.md`, `comparison-verdict.md`).
- Preserved first-class minorities: Skeptic "provisional substitute" framing; Architect pure-within-session shape; Skeptic+Outsider narrower-claim joint dissent.

### Key arguments carried

**3-of-4 cross-model convergence on hand-off-containing hybrid** [01b Q3 + 01c Q3 + 01d Q3]. Only Architect argued pure within-session. The hand-off majority includes the non-Claude Outsider. Adopted shape: Outsider-originated **sealed three-cell protocol** (Curation + Produce + Validation) with internal iteration budget in Produce Cell. *Architect's pure-within-session preserved as first-class minority with reopening trigger (Cell-2-to-Cell-3 information loss).*

**3-of-4 cross-model convergence on third-named-sense framing with anti-substitution** [01a Q5 + 01b Q5 + 01d Q5]. Skeptic alone argued "provisional substitute, not pillar." Adopted kernel text names reference-validation as third sense AND incorporates the load-bearing Skeptic-dissent content (explicit "does not establish intended-use functioning" clause). *Skeptic's "provisional substitute" framing dissent preserved as first-class minority with reopening trigger (label discipline collapse).*

**2-2 cross-model+adversarial convergence on narrower-claim Q7 framing** [01c Q7 + 01d Q7]. Skeptic + Outsider argue the mechanism validates a narrower claim than the original domain-validation loop. Architect + Operationalist argue close-with-minority. Synthesis adopts Skeptic+Outsider stronger framing: OI-016 moves to "Resolved — provisionally addressed pending first-exercise" rather than plain closed (D-070 formalises this).

**2-2 cross-model+adversarial convergence on stricter pass-thresholds** [01c Q6 + 01d Q6]. Skeptic + Outsider converge on N=5, 80% pass, 3 domains, ≥1 low-saturation. Architect proposed N=4, 75%, 2 domains; Operationalist proposed N=5, 60%. Adopted the stricter Skeptic+Outsider bar per cross-model adversarial convergence weight.

**Outsider-originated sealed three-cell protocol** [01d Q3] becomes the adopted validation shape. No Claude perspective produced the curation/produce/validation separation-of-duties framing at this level. Adopted with internal iteration budget per Operationalist and Skeptic hand-off proposals.

**Outsider-originated contamination canary** [01d Q4]: pre-case-adoption thin-prompt probe across model families adopted as L1 refinement.

**Outsider-originated distinctive-marker audit** [01d Q4]: rare-marker enumeration + reproduction-check adopted as L7.

**Outsider-originated three-core-properties test** [01d Q6(c)]: Blindness + Stageability + Discriminability as the primary mechanism-failure test. If any 2 of 3 fail in Session 015, mechanism is falsified.

**Outsider-originated "benchmark theater"** [01d Q7]: the strongest-failure-mode characterisation as a genre-of-performance rather than a local mechanism-violation. Shapes the synthesis's union of falsifiability conditions.

**Outsider-originated narrower-claim preservation** [01d Q7]: *"even if this mechanism works, it validates a narrower claim than the old loop did."* Shapes the adopted OI-016 disposition (D-070).

### Rejected alternatives (preserved)

**Rejected: pure within-session validation shape (Architect minority).** 3-of-4 cross-model against, including non-Claude Outsider. Architect's concern (hand-off loses design-intent information) is real and preserved as Q3 reopening trigger WX-14-2.

**Rejected: "provisional substitute, not pillar" framing in kernel text (Skeptic minority).** 3-of-4 cross-model against. Skeptic's dissent preserved in the kernel text's load-bearing clauses (does not establish intended-use functioning; does not substitute for domain validation) AND as a reopening trigger for WX-14-3 (label discipline collapse). The word "provisional" is not adopted; the content of the provisional framing is adopted.

**Rejected: looser pass-thresholds (Architect N=4, 75%, 2 domains; Operationalist N=5, 60%).** 2-2 cross-model+adversarial for stricter bar (N=5, 80%, 3 domains). Synthesis adopts stricter bar. Operationalist's methodology-version reset rule and partial-credit rule retained from the looser proposals.

**Rejected: closing OI-016 plainly (Architect+Operationalist position).** 2-2 with Skeptic+Outsider on stronger state-change. D-070 implements the stronger state-change.

## D-070: OI-016 resolution — Resolved pending first-exercise with automatic re-opening triggers

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** Reasonable practitioners disagreed (d016_3) on OI-016 disposition — 2-2 split with Architect+Operationalist for close-with-minority and Skeptic+Outsider for the stronger framing that the mechanism does not close the issue at the level Session 009's insight set. The cross-model (Outsider) aligned with the adversarial (Skeptic) on this question, which shifts the weight toward the stronger state-change per the convergence-crossing-model-family-axis pattern established in Sessions 008/010/011/013. Operator-marked load-bearing (d016_4) — the OI-016 disposition is the session's second-most-significant outcome after mechanism adoption (D-069) and determines what Session 015+ reads as the methodology's position on reference-validation's adequacy. d016_1 not triggered (no kernel change in this specific decision — that's D-069). d016_2 not triggered (no spec creation/revision in this decision). d023_1/2/3 not triggered (no kernel, spec, or multi-agent-deliberation modification in this decision). d023_4 not triggered because D-023.4 per established Session 007/008/010/012 interpretation covers OI-004 state changes, not other OI state changes; OI-016 is not OI-004.

**Decision.** Update OI-016 in `open-issues.md` as follows.

### OI-016 new text (replaces current Open-status text)

```markdown
### OI-016: Domain-validation pathway under user unavailability
**Surfaced:** Session 013 (per D-067)
**Status:** **Resolved — provisionally addressed pending first-exercise** (per D-069/D-070, Session 014)

Session 013's user Validate receipt for the Session 010 external artefact included a standing constraint: *"I'm no longer available to manually validate any artefacts you produce due to availability constraints."* Session 014 resolved OI-016 by designing and adopting a reference-validation mechanism (per D-069) — a sealed three-cell protocol (Curation / Produce / Validation) that compares methodology-produced artefacts to pre-selected documented proven solutions under staged constraint release and a seven-layer contamination defence stack. Kernel §7 v3 → v4 substantive revision adds Reference validation as a third named validation sense alongside Workspace and Domain. New specification `specifications/reference-validation.md` v1 contains mechanism detail.

**The resolution is provisional pending first-exercise (Session 015) per the following.**

The Skeptic+Outsider joint position (Session 014 Q7, 2-2 split vs Architect+Operationalist) holds that the mechanism validates a **narrower claim** than the original domain-validation loop. Reference validation supports the claim "the methodology can derive artefacts that resemble proven solutions under blinded staged constraints"; it does not establish "the methodology's new external artefacts function in live domain use." The kernel §7 v4 text includes this scope-statement explicitly, but the joint position remains as the standing warrant for the OI's re-opening.

**Automatic re-opening triggers.** OI-016 re-opens if any of the following is observed in first-exercise or accumulates across exercises:

1. **Outsider's three-core-properties test failure** (per Session 014 Q6c / D-069 spec): failure of any 2 of Blindness / Stageability / Discriminability in Session 015 or any subsequent reference-validation exercise.
2. **Counterfactual-probe inversion** (Skeptic Q7): counterfactual-probe results show methodology producing artefact tracking original reference rather than modified constraint.
3. **"Too fast" pattern** (Architect Q7): single Produce iteration arriving at ≥80% structural alignment across multiple cases despite passing contamination tests.
4. **Noise-floor inversion** (Operationalist Q6c): reference-validation pass-rate within 15 percentage points of no-methodology constraint-only baseline.
5. **Three-consecutive-"gap-surfaced"-non-passes** (Skeptic Q7 anti-laundering): three consecutive exercises each "surface a gap" each "addressed in subsequent session" with none producing a passing result. Pattern is not gap-surfacing; it is methodology-failure serially relabelled.
6. **Label discipline collapse** (Architect Q7 + Outsider Q7): `validation: reference-validated` artefacts used externally without the label qualification; reference-validation referred to as "validated" simpliciter; kernel §7's anti-substitution clause softened or removed without concurrent strengthening elsewhere.

**Preserved first-class minorities** inside this OI:

- **Skeptic "provisional substitute" framing minority** (Session 014, 01c Q5): the kernel should name reference-validation as explicitly provisional, not as equal-but-distinct third sense. Operational warrant: if label discipline collapse (trigger 6) is observed, the Skeptic's stricter framing is the preferred revision direction for kernel §7.
- **Architect pure-within-session shape minority** (Session 014, 01a Q3): validation should be a single-session loop, not a hand-off. Operational warrant: if Cell-2-to-Cell-3 hand-off consistently loses design-intent information that continuous-loop would have preserved (per WX-14-2), the Architect's proposal is the preferred revision direction for Q3.
- **Skeptic+Outsider joint narrower-claim minority** (Session 014, 01c+01d Q7): even if the mechanism works as designed, it validates a narrower claim than domain-validation. Operational warrant: this minority is the standing warrant behind the six re-opening triggers above; any movement to soften the kernel text's scope-statement activates the minority.
- **Session 013 Skeptic original strong-pause position** (Session 013, 01c Q6 carried forward): not superseded by D-069's adoption; preserved as the structural backdrop against which reference-validation is measured.

**Fallback-to-pause circumstances** (if any re-opening trigger fires and the methodology chooses pause over re-design): no new external artefacts produced; reference-validation mechanism suspended; OI-016 returns to Open with a new activation-trigger for design of a replacement mechanism.

**Scope boundary** (unchanged from Session 013 framing): OI-016 addresses the pathway question for domain validation. It does not address revision of existing Validate receipts for Session 008 and Session 010 artefacts (both in hand, both complete).
```

### Move OI-016 to Resolved Issues table

Add row: `OI-016: Domain-validation pathway under user unavailability | 2026-04-22 | 014 | Session 013 opened the OI. Session 014 resolved via reference-validation mechanism adoption (D-069) with kernel §7 v3 → v4 substantive revision and new specification/reference-validation.md v1. Resolution is **provisional pending first-exercise** — six automatic re-opening triggers specified (three-core-properties test; counterfactual-probe inversion; "too fast" pattern; noise-floor inversion; three-consecutive-gap-surfaced pattern; label discipline collapse). Three first-class minorities preserved within the resolution. See D-069, D-070, and OI-016 full text above.`

### Key arguments carried

**Cross-model+adversarial convergence on stronger state-change** [01c Q7 + 01d Q7]. The Skeptic's explicit "OI-016 should remain open" position and the Outsider's "narrower claim" framing combine to reject the Architect+Operationalist plain-close-with-minority disposition. Adopted: Resolved-provisional with automatic re-opening.

**Anti-laundering rule** [01c Q7]: *"Three consecutive reference-validation exercises each of which 'surfaced a gap,' each of which was 'addressed in a subsequent session,' and none of which produced a passing result"* — Skeptic names this specific pattern as procedural self-deception. Adopted as re-opening trigger 5.

**Label discipline as structural safeguard** [01a Q7 + 01d Q7]: the distinction between reference-validated and domain-validated artefacts is load-bearing for the mechanism's honesty. If the distinction collapses in use, the mechanism has failed at the level procedural self-deception operates. Adopted as re-opening trigger 6.

### Rejected alternatives (preserved)

**Rejected: plain "Resolved" status** (Architect+Operationalist close-with-minority position). 2-2 against; Skeptic+Outsider cross-model+adversarial convergence shifted the weight toward Resolved-provisional.

**Rejected: keeping OI-016 "Open" indefinitely** (Skeptic's strongest position in Q7). Skeptic's stronger preference ("OI-016 should remain open") is softened by the adoption of Resolved-provisional — but the six automatic re-opening triggers and the preserved minorities together capture the structural content of Skeptic's concern. If the triggers fire, the Skeptic's preferred state is restored automatically.

**Rejected: no re-opening triggers** (would be the light-touch resolution; not seriously proposed by any perspective). All four perspectives propose falsifiability conditions; adopting without encoding them would lose their substance.

## D-071: OI state housekeeping — Session 014 watchpoints, OI-004 tally advance

**Triggers met:** [d016_4, d023_4]

**Triggers rationale:** Operator-marked load-bearing (d016_4) for session-housekeeping per Session 005 D-033 / 006 D-043 / 007 D-049 / 008 D-052 / 009 D-056 / 010 D-059 / 011 D-062 / 012 D-065 / 013 D-068 precedent. d023_4 fires because this decision asserts an OI-004 state change: the sustained-practice criterion-2 tally advances from 4-of-3 to **5-of-3** (criterion already satisfied; Session 014 is the fifth required-trigger deliberation with non-Claude participation after Sessions 005, 006, 009, 011). D-023 literal reading: any OI-004 state change triggers, and the tally advance is a state change per the ledger (per Session 011 D-062 precedent). Non-Claude participation is required per d023_4 and is present (Outsider with full D-024 manifest). d016_1 / d016_2 / d016_3 not triggered: no kernel change in this decision; no spec change; the bookkeeping updates themselves are not disputed. d023_1 / d023_2 / d023_3 not triggered in this decision (D-069 carries those).

**Decision.** Update `open-issues.md` OI tracking as follows.

### OI-004 update

**Session 014 tally (per D-071):** Session 014 is the **fifth required-trigger deliberation** with non-Claude participation. D-069 modifies `methodology-kernel.md` and creates a new specification (d023_1 and d023_2 both fire); D-071 itself asserts an OI-004 state change (d023_4 fires — tally extends further beyond satisfied threshold). The Outsider (OpenAI GPT-5 via `codex exec`, session id `019db2bf-92cb-7771-b828-7eb85da11efe`, reasoning effort xhigh, 30,685 tokens) participated with a full D-024 manifest. **Six concrete Outsider-sourced contributions materially shaped adopted Session 014 content:**

1. Sealed three-cell protocol (Curation + Produce + Validation) as the Q3 adopted validation shape [01d Q3] — no Claude perspective produced this three-cell separation-of-duties framing at this level.
2. Contamination canary refinement to L1 selection gate [01d Q4] — thin prompts derived from tranche-0 fired at multiple model families to detect spontaneous reproduction of reference's idiosyncratic structure.
3. Distinctive-marker audit as L7 [01d Q4] — rare-marker enumeration + reproduction-check as distinct operational defence.
4. Three core properties test (Blindness + Stageability + Discriminability) as primary mechanism-failure test [01d Q6(c)] — no Claude perspective produced this three-property integrity formulation.
5. "Benchmark theater" framing for strongest failure mode [01d Q7] — distinct genre-of-performance characterisation.
6. Narrower-claim Q7 framing [01d Q7] — shapes the adopted OI-016 disposition (Resolved-provisional rather than plain-close).

Tally advances from 4-of-3 to **5-of-3** (fifth required-trigger deliberation with non-Claude participation). Criterion-3 cumulative data points across Sessions 005–014: **forty** (thirty-four through Session 013; six added in Session 014). Criterion 4 remains unmet. **Voluntary-to-required ratio is now 5:5** — first session where required-trigger count catches up with the voluntary count (previously 5:4 after Session 013). This rebalancing is informative for any future criterion-4-articulation or closure deliberation: the cross-model discipline is sustained equally across required and voluntary contexts.

### OI-002 observation

Session 014 creates `specifications/reference-validation.md` as a new v1 specification (`supersedes: none`). This is the **third creation** of a narrow single-purpose spec in the workspace (after Session 012's `identity.md`). Per the Session 012 D-063 precedent, creation of a narrow single-purpose spec is outside OI-002's existing substantive-vs-minor-revision binary. Observation recorded: the pattern of creating narrow single-purpose specs is now n=2 (identity.md and reference-validation.md); a future heuristic update could formalise creation as a third category distinct from substantive revision and minor revision. No formal OI-002 update this session; monitor.

Session 014 also revises `methodology-kernel.md` v3 → v4. The revision is **substantive** per the OI-002 five-point heuristic: new normative content (Reference validation as third named sense, anti-substitution clause, label discipline, scope-statement). File-level versioning applied; v3 preserved as `methodology-kernel-v3.md`.

### OI-007 update

**Count decrements 13 → 12** after OI-016 resolution. This is the second downward direction reversal after Session 012's count decrement (13 → 12 after OI-001 closure), itself the first since Session 009. Count is now at the lowest it has been since Session 011 (before OI-015 was opened). Monitor; the downward reversal does not yet reverse the overall upward trend from the methodology's first 11 sessions.

### OI-005 annotation

Session 014 does not touch OI-005. The reference-validation mechanism applies to the methodology as a whole; it does not elaborate sub-activities of any specific kernel activity. OI-005 remains available for future deliberation.

### OI-008 annotation

Session 014's reference-validation mechanism introduces `contamination-audit.md` as a required per-exercise artefact (per D-069's new specification). This is one form of validation-output-persistence but is scoped to reference-validation exercises specifically, not to `tools/validate.sh` output. OI-008's original question (should `tools/validate.sh` output be persisted as part of session provenance) is unchanged by Session 014. Annotation recorded for traceability; no OI-008 state change.

### OI-012 annotation

Session 014 does not touch `validate.sh`. The hard-coded `02-decisions.md` path issue remains per Session 009 D-055. Reference-validation exercise artefacts (per D-069) introduce new file patterns (`brief-gatekeeper.md`, `contamination-audit.md`, `comparison-verdict.md`) that future exercises will commit into session provenance directories; these may or may not interact with the OI-012 collision surface depending on how they are numbered. The Reviser/Outsider pattern-match proposal preserved in D-055 remains the preferred starting point for a future fix. Monitor.

### OI-013 annotation

Session 014 does not produce a non-file external artefact. OI-013's activation trigger does not fire.

### OI-014 annotation

Session 014 resolves OI-016 (which was interdependent with OI-014 per Session 013 D-068). The interdependence is dissolved: OI-016's option-(a) "recruit alternate validators" was ruled out by user steering, so the automatic OI-014 activation through an OI-016 option-(a) election does not occur. OI-014 remains independently open; its original activation trigger (first external application whose domain-validation receipt shape materially differs from Session 008's single-user-self-report pattern) is structurally moot under the user's standing unavailability constraint — no domain validation of any shape is obtainable from the user going forward. If Session 015+ reference-validation first-exercise surfaces a receipt-shape question that OI-014 anticipated, the OI activates on that trigger.

### OI-015 annotation

Session 014 does not address the laundering enforcement gap. OI-015 remains available for future deliberation.

### Session 014 watchpoints (WX-14-1 through WX-14-6)

Per Session 010 D-058 / Session 012 D-065 / Session 013 D-068 precedent, watchpoints are recorded in the decision record (this D-071) rather than as formal OIs unless they name novel methodology mechanisms.

- **WX-14-1: Contamination canary efficacy.** Does L1 saturation-test (pre-adoption thin-prompt probe across model families) meaningfully reduce the candidate pool? If not, the defence is ornamental; if too aggressively, the pool is empty (per Q6c operational trigger for mechanism failure). Monitor in Session 015 first-exercise.
- **WX-14-2: Three-cell hand-off information loss.** Does the Cell 2 → Cell 3 session boundary lose design-intent information that a continuous within-session loop would preserve? This is the Architect's minority-reopening trigger for Q3. If Cell 3 repeatedly needs to reconstruct context that Cell 2's iteration budget had handled continuously, the Architect's pure-within-session proposal becomes the warranted revision direction.
- **WX-14-3: Label discipline preservation.** Do `validation: reference-validated` artefacts retain their scoping in external citation, or does the label drift to plain "validated"? This is the Skeptic's minority-reopening trigger for kernel §7. Collapse of the distinction activates the Skeptic's "provisional substitute" framing as the warranted revision direction.
- **WX-14-4: Gatekeeper-brief edit frequency.** Session 015+ should commit `brief-gatekeeper.md` at exercise start and never edit it during the Produce Cell. Git-log audit of the file for post-Produce-Cell-open commits surfaces experimenter-demand-characteristics contamination (Operationalist procedural-self-deception observable). Zero edits is the target; >0 edits triggers audit.
- **WX-14-5: Pass-rate distribution presence/absence of `fail-methodology-gap` verdicts.** Healthy mechanism produces a mix of pass, partial-match-iterate, and fail-methodology-gap verdicts. All-pass is suspicious (per Operationalist Q7). Across the first 3 exercises, observe whether any exercise produces `fail-methodology-gap`; if not, examine case-selection for bias toward easy passes.
- **WX-14-6: Cross-model convergence pattern in Cell 3.** Is cross-model divergence yielding useful contamination signal? Specifically: do Claude and non-Claude validators in Cell 3 disagree on contamination calls in informative ways (different rare-markers flagged; different structural-match assessments), or do they converge in ways that suggest shared-pretraining artefacts? First 3 exercises provide the signal.

### Key arguments carried

OI-004 tally advance per D-023.4 literal reading (Session 011 D-062 precedent). Criterion-3 six-contribution count continues the Sessions 011 (5) / 012 (5) / 013 (5) pattern at +1 (6). Voluntary-to-required ratio rebalancing (5:5) recorded as watchable pattern for future criterion-4 articulation.

### Rejected alternatives (preserved)

**Rejected: no OI-002 observation** (would skip the pattern-recognition on narrow single-purpose spec creation). Session 012 D-065 precedent is to record observations even absent formal heuristic update.

**Rejected: immediate OI-012 fix** (Session 009 D-055 precedent is to defer; no new collision pressure observed in Session 014).

**Rejected: immediate OI-008 revision** (scope of Session 014 is OI-016 resolution; OI-008 is distinct).

**Rejected: raising watchpoints to formal OIs** (Session 010 D-058 / 012 D-065 / 013 D-068 precedent is to record watchpoints in decision records; elevation to formal OI requires a subsequent session observing pattern across multiple data points).
