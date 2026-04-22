---
session: 020
title: Assessment — Session 019 Audit (R1–R6); Seven Paths Presented; Halt for Operator Direction
date: 2026-04-22
status: complete
---

# Assessment — Session 020

## 1. Read (workspace state)

Ran `tools/validate.sh` at session open: **443 pass, 0 fail**. Tenth consecutive clean session-opener run.

Active specifications unchanged from Session 019 close snapshot: `engine-manifest.md` v1, `identity.md` v2, `methodology-kernel.md` v4, `multi-agent-deliberation.md` v3, `reference-validation.md` v2 (revised Session 019), `validation-approach.md` v3, `workspace-structure.md` v3 (7 active specs; 11 superseded versions preserved). `PROMPT.md` thin-dispatcher form; `prompts/development.md` + `prompts/application.md` present. OI count: **12 active**, 5 resolved. Engine version: `engine-v1`.

Git at session open: clean working tree; HEAD at `fa552ae` ("Session 019 close: reference-validation.md v1→v2 adopted; R1-R6 applied"). No in-flight work.

**No default pre-commitment for Session 020** per Session 019 D-078 close §4. No operator session-open steering beyond the standard `PROMPT.md` re-entry.

## 2. Audit of Session 019 synthesis fidelity

Session 019 close directed Session 020 to audit four specific dimensions. Each addressed below.

### 2.1 — Cross-family weighting of 3-of-4 revise-now rubric: genuine or coincidence?

**Question (per Session 019 close §Next session).** Was the 3-of-4 cross-family revise-now rubric genuinely affirmative cross-family (2 Claude + 1 non-Claude), or did Reviser/Skeptic's Claude convergence dominate with Outsider's narrow revise-now position added as cross-family garnish?

**Spot-check.** Composition of the revise-now majority:

| Perspective | Family | Position (Q1) |
|---|---|---|
| Reviser | claude (opus-4-7) | "Revision warranted now, with tight scope." |
| Skeptic | claude (opus-4-7) | "Partial yes, but narrower than Reviser will propose and conditional on the revision being restrictive rather than accommodating." |
| Outsider | gpt (gpt-5.4) | "Yes, but narrowly." |
| Minimalist | claude (opus-4-7) | "Defer substantive revision." |

Both model families are represented on the majority side (2 Claude + 1 non-Claude). Outsider is not a derivative vote — it contributed five concrete outcome-shaping items per close honest-note #5 that are structurally distinct from what the Claude perspectives produced (§4 L3 "not rescued by cleaner family" placement; §9 trigger 6 extension blocking family-conditional screening; §1 C3 two-stage canary-as-early-warning-only framing; explicit naming/distinctive-sequence recovery as standalone rejection basis; screening/confirmatory-mismatch testing-methodology framing).

**However**, reading Outsider's position carefully against Reviser's and Skeptic's shows Outsider's revise-now rests on a narrower surface than either Claude perspective: Outsider explicitly refuses to revise kernel §7 (aligned with Reviser + Minimalist vs Skeptic) AND refuses to revise `multi-agent-deliberation.md` (aligned with all three Claude perspectives). Outsider's revise-now is "tighten §1 C3 + §4 L1 + §4 L3 + §9" — strictly a subset of Reviser's proposed surface. The precision varies across Q2–Q5: Outsider aligns with Claude Minimalist on WX-18-5 watchpoint-only; aligns with Reviser on cross-family placement direction but chooses §4 L3 where Reviser chose §1 C3; aligns against Skeptic on kernel §7 preemptive activation.

**Verdict.** The 3-of-4 cross-family revise-now rubric is defensibly affirmative cross-family at the *macro-question* level (revise-now vs defer), because both families appear on the majority side and Outsider's revise-now vote rests on its own content contributions rather than passive agreement with the Claude pair. It is *not* a 3-of-4 cross-family rubric on the specific textual content — that composition varies per question (e.g., WX-18-4 placement is 2-of-4 cross-family with Outsider contra-placing from Reviser+Skeptic; kernel §7 preemptive activation is 3-of-4 cross-family *against*). Session 019 synthesis explicitly acknowledges this distinction at §3.2 of `01-deliberation.md` (adopting both surface placements as "complementary, not competing"). The macro-level 3-of-4 claim is honest; Session 020+ synthesizers should be careful not to carry the "3-of-4 cross-family" framing over to every specific content question it was composed from.

Clean. Minor framing-awareness note recorded for future synthesis: cross-family-majority on a macro-question does not automatically transfer to each specific content sub-question the macro-question decomposes to.

### 2.2 — R1's three rejection conditions: coherent and non-redundant?

**Question (per Session 019 close §Next session).** Does condition (2) verbatim-phrase zero-tolerance add discriminating power over condition (1) 30% overlap, or is it largely subsumed?

**Text under audit** (`reference-validation.md` v2 §1 C3 stage (b) rejection conditions):

1. Either model produces text exceeding 30% shared 5-gram token overlap with the sealed reference.
2. Either model spontaneously emits a verbatim distinctive phrase, section heading, or named label from the reference (zero-tolerance regardless of overall overlap percentage).
3. Cross-family retrieval asymmetry: one model family reproduces the reference verbatim or near-verbatim (or with its idiosyncratic section labels or sequence) while the other produces constraint-satisfying but from-scratch text.

**Non-redundancy test** — can each condition fire independently of the others?

- **Only condition 1 fires.** Both families produce text with 30%+ overlap without emitting named labels or asymmetry. Scenario: both reproduce structural sequence but in their own wording, no distinctive phrase verbatim. Condition 2 does not fire (no verbatim label); condition 3 does not fire (no asymmetry — both reproduce). Condition 1 catches it. **Plausible.**

- **Only condition 2 fires.** A short distinctive phrase (e.g., Kerth's "Regardless of what we discover" = one 5-gram) surfaced inside an otherwise original 500-word output gives ~0.2% 5-gram overlap — far below 30%. Condition 1 does not fire; condition 3 may not fire if the other family also produces original output without the distinctive phrase (no asymmetry). Condition 2 independently catches this case: a zero-tolerance emission signal not reducible to quantitative overlap. **Plausible — and this is exactly what Session 018's D2 C3 test showed in compressed form, where the 40-word reference made verbatim reproduction trivially cross the 30% quantitative threshold, but in larger references (say 3000 words) a single 10-word distinctive heading would be below 30% quantitatively while still diagnostically contamination-positive.**

- **Only condition 3 fires.** Claude at 25% overlap (below threshold, no verbatim distinctive phrase); GPT at 5% original. Condition 1 does not fire (both below 30%); condition 2 does not fire (no verbatim phrase). Condition 3 catches the case because the *asymmetry itself* is contamination evidence — constraints do not uniquely determine the text; only retrieval does. **Plausible.**

Each condition has an independent scenario where it alone fires. Conditions are textually coherent (all three stated in parallel syntactic form; all three read as stopping conditions under "any one fires"). No redundancy.

**Verdict.** R1's three rejection conditions are non-redundant and textually coherent. Condition 2 adds discriminating power over condition 1 specifically in the reference-size regime where distinctive phrases are a small fraction of the total text (typical for references of 2000+ tokens). Condition 3 adds orthogonal discriminating power in the sub-threshold-overlap regime. Clean.

### 2.3 — R6's three new Session 019 minorities: operationally meaningful or ornamental?

**Question (per Session 019 close §Next session).** Does each new §10 minority warrant specify an operationally meaningful test?

**Minority 1 — Minimalist defer-revision** (Session 019, 01b Q1/Q7).

*Warrant text* (from `reference-validation.md` v2 §10 / `open-issues.md` OI-016): "if Session 020's Cell 1 attempt passes C3 without triggering any of the three rejection conditions, the revised §1 C3 / §4 L1 did no work v1 would not also have done; the amendments can be read as premature and are candidates for rollback argument."

*Operational test.* Concrete: a Session 020 (or later) Cell 1 attempt that passes C3 *and* none of the three new rejection conditions fired in the passage. If that happens, the revision did no discriminating work (v1's single-condition 30% would have also passed). The test is falsifiable against the first specific Session 020 outcome.

*Meaningful or ornamental?* **Meaningful.** Clear operational test, clear falsifier.

**Minority 2 — Skeptic preemptive-activation** (Session 019, 01c Q5/Q7).

*Warrant text*: "if a second structurally-different-domain rejection fires §9 trigger 7 (or if interim citation drift occurs per §8 before n=2 is reached), the broad-reading preemptive activation position is vindicated and kernel §7 revision is the preferred response."

*Operational test.* Concrete: §9 trigger 7 firing (n=2 structurally-different-domain rejection) or §8 citation drift (reference-validated artefact used without scope qualification in later session). Both are specific observable events.

*Meaningful or ornamental?* **Meaningful.** The "interim" clause (§8 citation drift before n=2) is a live concrete check that could activate the warrant ahead of the primary n=2 trigger. Clear operational hook.

**Minority 3 — Reviser asymmetry-probe** (Session 019, 01a Q3 R2).

*Warrant text*: "if Session 020+ produces multiple Cell 1 L1b rejections and the session-level ability to judge WX-18-5 as a pattern is impaired by absence of structured asymmetry records, the Reviser's probe clause is the preferred revision direction for a Session 021+ §4 L1 amendment."

*Operational test.* Two conjunct conditions: (a) multiple L1b rejections occur; (b) session-level pattern judgment on WX-18-5 is *impaired by absence of structured asymmetry records*. Condition (a) is concrete; condition (b) has a subjective element ("impaired").

*Meaningful or ornamental?* **Meaningful but softer than Minority 1 or 2.** The warrant is operational — it specifies two named triggers. The "impairment" criterion in condition (b) is less crisp than Minority 1's "no new condition fired" or Minority 2's "trigger 7 fired / scope drift observed," but it is not purely subjective: a Session 021+ synthesizer can inspect the record of L1b rejections and ask "do I have the per-family-reproduction data to tell whether WX-18-5 is a pattern, or do I not?" That is a legible and answerable question.

**Verdict.** All three new Session 019 minorities have operationally meaningful warrants. None are purely ornamental. Minority 1 (Minimalist defer) and Minority 2 (Skeptic preemptive) have the clearest operational tests; Minority 3 (Reviser asymmetry-probe) has a softer operational test with one subjective clause but is still not ornamental. If Session 020's outcome triggers Minority 1's warrant, Minority 1 produces the cleanest rollback argument. Recorded for WX-19-1 monitoring: if in practice Minority 3's "impairment" clause cannot be operationalised by a future session needing to judge the warrant, Minority 3's text needs sharpening — this is the first-class minority record-keeping watchpoint already in place per Session 019 honest-note #3.

Clean.

### 2.4 — Aggregate R1–R5 anti-laundering on external re-inspection

**Question (per Session 019 close §Next session).** Does the aggregate of R1–R5 pass anti-laundering on external re-inspection? (Session 019's own aggregate check at honest-note #2 was affirmative but single-agent.)

**Per-revision inspection against the "widening what counts as pass" failure mode.**

- **R1 (§1 C3 two-stage + three rejection conditions).** Adds two mandatory stages (canary + full-constraint). Adds two new rejection conditions (zero-tolerance verbatim; cross-family asymmetry) to the pre-existing quantitative condition. Does not remove any existing check. Does not lower the 30% threshold. **Strengthens gate.**

- **R2 (§1 Flagged tension strengthening).** Adds Session 018 WX-18-3 materialisation annotation. Adds explicit "threshold-tuning cannot resolve" + "§9 trigger 7 pre-commit" pointers. Does not remove tension acknowledgment; explicitly says tension is unresolved. **Strengthens evidence base of a known limitation; does not soften claim.**

- **R3 (§4 L1 two-stage L1a + L1b).** Splits L1 into canary (L1a, necessary but not sufficient) + full-constraint saturation (L1b, mandatory pre-seal). Does not remove L1a; adds L1b. Preserved-record obligation at L1b (Outsider-originated). **Strengthens: adds a mandatory test that did not exist in v1; records enable pattern detection.**

- **R4 (§4 L3 pre-seal diagnostic-not-design-evidence).** Extends §4 L3 with language blocking "pass only when one family is clean" laundering path. Does not remove Cell 3 cross-model-divergence-analysis text; adds pre-seal clarifying text. **Strengthens: explicitly blocks a specific accommodation path.**

- **R5 (§9 triggers sharpening).** Trigger 5 scope widened (pre-seal rejections count). Trigger 6 extended (blocks family-conditional-screening laundering route). New trigger 7 added (n=2 structurally-different-domain rejection pre-commits kernel §7 revision consideration). No trigger threshold lowered; no trigger removed; one new trigger added. **Strengthens.**

**Aggregate check — could the combination create a new laundering path that no individual R creates?**

Three candidate laundering patterns specifically tested:

1. **"Route around contamination to the clean family."** Would fire if Session 020+ argued "Claude reproduces, GPT does not → use GPT's output." Blocked by R4 §4 L3 "not rescued by cleaner output from another family" + R5 §9 trigger 6 extension blocking family-conditional screening. **Blocked.**

2. **"Tolerate the tension as known-limit → produce anyway."** Would fire if Session 020+ argued "§1 tension is flagged, so Claude-family saturation is acceptable." R2 strengthening explicitly says "threshold-tuning cannot resolve" + pre-commits §9 trigger 7. The tension is not converted to permission to pass. **Blocked.**

3. **"Pass L1a and skip L1b."** Would fire if Session 020+ treated L1a canary as sufficient. R3 explicitly says L1a is necessary but not sufficient; L1b is mandatory. **Blocked.**

**One potential softening surface.** §9 trigger 7 requires n=2 structurally-different-domain rejection before it fires. A critic could argue this "buys time" by delaying kernel §7 revision consideration until n=2. Counter-argument: v1 had *no* automatic trigger for kernel §7 revision; it relied on §10 preserved-minority warrant "if label discipline collapse (§9 trigger 6) is observed." v2 adds a new automatic path (trigger 7) *in addition to* the existing §10 warrant for label-discipline-collapse. The coupling between rejections and kernel §7 revision is tighter in v2 than v1, not looser.

**Verdict.** R1–R5 aggregate passes anti-laundering on external re-inspection. No threshold lowered; no check removed; no label widened; no softening of kernel §7 anti-substitution. Session 019's own affirmative self-check at honest-note #2 is reproduced by external re-inspection.

Clean.

### 2.5 — Audit overall verdict

All four audit dimensions clean. Session 019's synthesis is defensible on external re-inspection. One minor framing-awareness note for future synthesizers (per §2.1): cross-family-majority on a macro-question does not automatically propagate to each specific content sub-question it decomposes to. Recorded for future-synthesizer awareness; no revision to Session 019 artefacts warranted.

## 3. Seven paths for Session 020 (per Session 019 close §Next session)

Session 019 close presented six enumerated paths plus "operator-directed agenda." Each is evaluated below against OI-009 G/O/K/S criterion-package (the operational test for self-work load-bearing) plus budget, dependencies, and Session 019 minorities interaction. Path letters preserved from Session 019 close to preserve referenceability.

**Binding context from Session 019 close honest-note #7.** Trigger-5 counter is at 1 after Session 018. "Session 020's aim should be either a passing Cell 1 + Cell 2 exercise OR a clean no-candidate-passes closure with explicit §9 trigger 7 activation, not a third 'gap surfaced' narrative." This shapes evaluation of paths (A1), (A2), (A3) below — repeating a "rejected-at-C3 + revise-the-spec" narrative would advance trigger-5 to 2, approaching the three-consecutive threshold.

### 3.1 — Path (A1): Cell 1 re-attempt with S1 (Feldenkrais Pelvic Clock)

**Scope.** Re-run Cell 1 on S1 under the revised two-stage C3 (L1a canary + L1b full-constraint saturation). S1 survived Session 018's L1a canary at Moderate risk; L1b (new) has not been run on S1.

**G/O/K/S evaluation.**
- **(G):** passes. Reference-validation directly supplies external-artefact evidence under user unavailability.
- **(O):** passes. Removes the "revised spec unexercised" blocker; closes (or advances) the first-exercise.
- **(K):** passes. External reader would see spec exercised after revision.
- **(S):** passes. Session 018 left S1 untested at L1b; this closes it.

**Dependencies.** No D-023 trigger from re-running Cell 1 itself. Single-perspective Case Steward execution per Session 018 precedent (or operator may elect multi-perspective convening for Step 2 L1b). Budget: tight-to-moderate for a single session (Session 018 Cell 1 through Step 3 + C3 fit in one session with `codex exec` invocations).

**Session 019 minorities interaction.**
- *Minimalist defer-revision (1):* If S1 passes L1a+L1b without triggering any new condition (especially condition 2 verbatim or condition 3 asymmetry), Minimalist's warrant is activated — revisions did no work v1 would not have done. **Direct falsifier.**
- *Skeptic preemptive-activation (2):* If S1 is rejected at L1b in a structurally-different domain (somatic practice vs agile retrospective), §9 trigger 7 advances to n=1 with one domain pending. Trigger 7 fires only at n=2; Session 020 alone cannot fire it without a second structurally-different-domain rejection in the same session.
- *Reviser asymmetry-probe (3):* If Cell 1 produces an L1b rejection, structured per-family reproduction data would be recorded under the new L1b preserved-record obligation.

**Skeptic-warrant signal.** If rejection: advances trigger-5 counter to 2, increasing pressure toward the three-consecutive threshold. Note: Minimalist warrant (1) is only activated by *success*, not rejection.

**Domain note.** S1 is somatic-practice; Session 018's D2 was agile-retrospective. A rejection would be structurally-different-domain per §9 trigger 7.

### 3.2 — Path (A2): Cell 1 re-attempt with S2 (Alexander Semi-Supine)

**Scope.** Analogous to (A1); different somatic-practice reference (Alexander Technique semi-supine / constructive-rest protocol). S2 also survived Session 018's L1a canary at Moderate.

**G/O/K/S evaluation.** Identical to (A1).

**Dependencies.** Identical to (A1). S1 and S2 are both in the somatic-practice domain — testing both in one session would still count as one "structurally-different domain" relative to Session 018's agile-retrospective domain, not two separate domains for §9 trigger 7 purposes. If both are rejected at L1b, trigger 7 is still at n=1 (one structurally-different domain with rejection pattern).

**Session 019 minorities interaction.** Identical to (A1) with the caveat above.

**Relative to (A1).** (A2) vs (A1) is essentially a candidate-selection judgment within the same domain. Running both in the same session is also permissible and could be useful for pattern-detection per Reviser asymmetry-probe minority.

### 3.3 — Path (A3): Cell 1 re-attempt with fresh re-survey (lower-saturation pool)

**Scope.** Source candidates from lower-saturation domains — niche protocols, non-English-language references, specific small-company retrospectives, private-institutional documents. Significant external-sourcing effort (WebSearch, possibly WebFetch on specific sources).

**G/O/K/S evaluation.**
- **(G):** passes.
- **(O):** passes. Removes the "revised spec unexercised on lower-saturation pool" blocker.
- **(K):** passes.
- **(S):** passes at moderate strength; the specific obstacle is "sourcing pool hypothesis untested."

**Dependencies.** Multi-session scope plausible. External-sourcing budget is the main constraint; Session 018 sourced from pretraining only. A fresh re-survey would require WebSearch over documented-solution candidates in specific domains, evaluating against C1–C8 iteratively. One session may produce a shortlist; Cell 1 execution on a selected candidate is Session 021+ work likely.

**Session 019 minorities interaction.** Same as (A1)/(A2) but the Minimalist-warrant-activation threshold may be easier to cross on a lower-saturation candidate (lower prior for Claude-family saturation → passage without new-condition activation is more plausible).

**Risk.** If the lower-saturation pool still produces C3 rejection, trigger-5 counter advances to 2 with a third "gap-surfaced" cadence approaching. If rejection is structurally-different-domain from Session 018, trigger 7 advances.

### 3.4 — Path (B): OI-004 closure criterion-4 articulation

**Scope.** Deliberate the articulation of closure criterion 4 from `multi-agent-deliberation.md` v3 §Closure Criteria — "articulated definition of 'substantively different training provenance' and enumerated acceptable participant kinds." This is the sole unmet criterion for OI-004 closure (criteria 1, 2, 3 satisfied since Session 009, extended to 6-of-3 at Session 017).

**G/O/K/S evaluation.**
- **(G):** passes. Articulated definition is a visible-to-external-reader methodology-discipline claim.
- **(O):** passes. Removes OI-004-closable-but-unclosed state.
- **(K):** passes. External reader would see the methodology either close OI-004 with articulated criterion-4, or make explicit why it remains open.
- **(S):** passes. Specific articulable obstacle (criterion 4 unmet) with concrete resolution shape (deliberate + articulate + close OR deliberate + identify blockers).

**Dependencies.** D-023-triggering (articulation lives in `multi-agent-deliberation.md` per v3 §Closure Criteria location; and OI-004 state change asserted → d023_4 fires). Non-Claude Outsider required. Budget fits one session (Session 014 precedent: OI-016 resolution deliberation fit one session with substantial content).

**Session 019 minorities interaction.** None directly; this is not reference-validation territory. Closing OI-004 (or leaving it open with criterion-4 blockers articulated) is orthogonal to R1–R6.

**Precedent for framing.** Closure criteria are specified in `multi-agent-deliberation.md` v3 §Closure Criteria. Criterion 4 reads: *articulated definition of "substantively different training provenance" and enumerated acceptable participant kinds*. Article-substance candidates include: (i) training-corpus-distinguishability as operational criterion; (ii) organisational-origin as operational criterion (Anthropic vs OpenAI vs Google vs Meta vs open-source); (iii) architecture family as operational criterion; (iv) some combination.

### 3.5 — Path (C): OI-015 laundering-gap deliberation

**Scope.** Deliberate the enforcement mechanism for surfaced-but-not-re-examined domain inputs. Per OI-015's Preferred starting point: choose kernel §4 Deliberate elaboration vs kernel §5 Decide elaboration vs a separate brief-authoring convention vs a new `validate.sh` check.

**G/O/K/S evaluation.**
- **(G):** passes at moderate strength. Laundering-gap is primarily a self-work quality concern; its external-frame translation is "the methodology's 'no silent imports' rule is operationally enforced."
- **(O):** passes. Removes the known gap that four-of-four Session 011 perspectives surfaced.
- **(K):** passes at moderate strength. External reader would see the methodology tightening its own anti-laundering discipline.
- **(S):** passes. Specific obstacle named; concrete resolution shapes enumerated.

**Dependencies.** D-023-triggering if kernel §4 or §5 revised (likely, per preferred starting point). Non-Claude Outsider required. Budget fits one session.

**Session 019 minorities interaction.** None directly. This is kernel-discipline territory, not reference-validation.

**Sequencing note.** Session 019 close and Session 017 close both noted (C) "benefits from (D) [H4 first-exercise] having run first." The underlying concern is that H4's explicit prompt-class separation (`development.md` vs `application.md`) may itself reduce the laundering surface; deliberating OI-015 before exercising H4 may over-engineer a fix whose surface H4 has already partially addressed.

### 3.6 — Path (D): First-exercise of H4 application-initialisation

**Scope.** Execute the external-application initialisation contract in `engine-manifest.md` §6 against a new external problem brief. Sessions 007 + 008 established the prep+execute pattern for the first external application. Sessions 010, 013 are subsequent external-application sessions. Session 017 adopted H4 and established the engine-vs-methodology layered model; no session has yet *initialised a fresh external-application workspace* per the H4 contract.

**G/O/K/S evaluation.**
- **(G):** passes. External-application initialisation is the methodology's external claim.
- **(O):** passes. Removes the "H4 adopted but never exercised on the initialisation contract" blocker.
- **(K):** passes. External reader would see the H4 initialisation contract either hold or surface gaps.
- **(S):** passes. Specific obstacle named (H4 first-exercise); concrete resolution (execute contract against a named problem).

**Dependencies.** Requires an external problem brief from operator. Sessions 007/008 used "morning movement sequence" as the first external application; Session 010 used "household decision protocol." A fresh external-application workspace per `engine-manifest.md` §6 would copy the engine file set into a new directory, populate `brief.md`, and run Session 001 of the new application — potentially multi-session scope, reproducing the Session 007 prep + Session 008 execute pattern in a clean `applications/NNN-<slug>/` structure.

**Session 019 minorities interaction.** None directly. Reference-validation could be deferred if (D) is chosen; §9 trigger-5 counter at 1 does not tick without further exercise.

**Operator input requirement.** This path requires operator to supply an external problem (or ratify a candidate from an agent-produced shortlist per Sessions 007 D-045 precedent). It cannot proceed without that input.

### 3.7 — Path (E): Operator-directed agenda

Operator may steer to a path not enumerated above. Prior sessions where operator-directed agenda led to new work: Session 014 (operator ruled out Session 013's three tripartite options and proposed reference-validation as a fourth), Session 016 (operator reframing input → OI-017 opened), Session 017 (operator steering to OI-017 deliberation over D-072 default), Session 019 (operator ratified Path B over other alternatives).

### 3.8 — Ranking

| Path | G | O | K | S | D-023? | Non-Claude? | Budget | Session 019 minorities |
|---|---|---|---|---|---|---|---|---|
| (A1) Cell 1 re-attempt S1 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | no | optional | tight-to-moderate | directly testable (Minimalist falsifier on pass) |
| (A2) Cell 1 re-attempt S2 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | no | optional | tight-to-moderate | same as (A1) |
| (A3) Cell 1 re-attempt fresh re-survey | ✓ | ✓ | ✓ | ✓ | no | optional for survey; mandatory for sealing | multi-session likely | Minimalist falsifier on pass, broader test |
| (B) OI-004 criterion-4 articulation | ✓ | ✓ | ✓ | ✓✓ | yes (d023_3 + d023_4) | required | fits | none |
| (C) OI-015 laundering-gap | ✓ | ✓ | ✓ | ✓✓ | yes if kernel revision | required | fits | none; benefits from (D) first |
| (D) H4 first-exercise | ✓✓ | ✓✓ | ✓✓ | ✓✓ | depends on brief outcome | depends on brief | multi-session (prep+execute) | none |
| (E) Operator-directed | — | — | — | — | — | — | — | — |

**Agent assessment (not a recommendation to bypass ratification).**

- **(A1) or (A2)** is the most directly responsive path to Session 019's R1–R6 adoption. The revised spec exists precisely to be exercised; running it against a shortlist candidate provides the first empirical test of whether R1–R5 do discriminating work the v1 spec would not. The Minimalist defer-revision minority's operational warrant (rollback argument on spec-revision-did-no-work grounds) is directly falsified or vindicated by a Session 020 Cell 1 attempt.
- **(A1)+(A2) combined in one session** — running Cell 1 on both S1 and S2 — is within single-session budget for a Case-Steward-only execution pattern, and has the advantage of producing two L1b data points on somatic-practice references (same domain). This does not fire §9 trigger 7 (both same-domain) but does contribute to Reviser's asymmetry-probe minority data base if L1b rejection occurs.
- **(A3) fresh re-survey** is the strongest test of whether the candidate pool is empirically exhausted at sustainable rate (the §1 Flagged tension's limiting case) vs saturated-in-a-specific-domain (which S1/S2 testing does not distinguish). It is also the highest external-sourcing budget.
- **(B) OI-004 criterion-4 articulation** is the only enumerated path that advances the closure state of a long-standing OI (surfaced Session 001; criteria 1–3 satisfied since Session 009; criterion 4 unmet through 20 sessions). Its G/O/K/S pass is real if modest; the exit-condition on OI-004 is plausible in one session.
- **(C) OI-015 laundering-gap** benefits from (D) having run first, per Session 017 close's sequencing observation.
- **(D) H4 first-exercise** is a distinct axis — it is not reference-validation, not OI-004, not OI-015. It is the first operational test of the engine-vs-methodology reframing adopted Session 017.

**Agent preference if operator does not steer.** Path **(A1)+(A2) combined** — run Cell 1 on both S1 and S2 under revised two-stage C3 in the same session. Rationale: directly tests whether R1–R5 do discriminating work; directly activates Minimalist defer-revision minority's operational warrant (first falsifier available on Session 020); produces two L1b data points in the same session; fits budget; no D-023 trigger; no external-problem-brief dependency. If both pass L1, proceed to sealing one for Cell 2 Produce per Session N shape; if one/both fail, record the L1b outcome + advance trigger-5 counter + evaluate whether a structurally-different-domain rejection from Session 018 is in hand (yes, somatic vs agile-retrospective → trigger 7 counter advances to 1-of-2, not yet firing).

**Constraint from Session 019 close honest-note #7.** If Session 020 produces a third "gap-surfaced" narrative — Cell 1 rejection + revise-spec cadence again — trigger-5 counter reaches 2 and is one session away from firing the three-consecutive threshold. Operator should be aware this pressure is live.

## 4. Halt for operator ratification

Per Session 019 close §Next session, Session 020 open presents these paths to the operator for ratification before executing any of them. Session 018 / Session 019 precedent: halt for operator steering at the fork. Session 015 / Session 016 precedent: assessment-only shape is legitimate if operator direction is deferred.

This assessment is committed as `provenance/020-post-revision-assessment/00-assessment.md`; no substantive work executed beyond the audit.

**Action requested from operator:**

- Ratify Path **(A1)** — Cell 1 re-attempt with S1 (Feldenkrais Pelvic Clock) under revised two-stage C3.
- Or ratify Path **(A2)** — Cell 1 re-attempt with S2 (Alexander Semi-Supine).
- Or ratify **(A1)+(A2) combined in one session** (agent preference if operator does not steer).
- Or ratify Path **(A3)** — fresh re-survey for lower-saturation pool (multi-session scope likely).
- Or steer to Path **(B)** — OI-004 closure criterion-4 articulation (D-023-triggering; non-Claude required; fits one session).
- Or steer to Path **(C)** — OI-015 laundering-gap deliberation (benefits from (D) first).
- Or steer to Path **(D)** — first-exercise of H4 application-initialisation (requires external problem brief from operator).
- Or steer to Path **(E)** — operator-directed agenda not listed above.

If the operator provides no steering on next engagement, Session 020 will halt in this assessment-only state and await direction rather than defaulting to any specific path (per Session 019 close "open under no default pre-commitment").

## 5. Record state

- `provenance/020-post-revision-assessment/00-assessment.md` — this file.
- No other provenance files this session at this commit.
- No specification changes this session at this commit.
- No `applications/` changes.
- `SESSION-LOG.md` unchanged at this commit; will receive its Session 020 entry after execution-path ratification and close (if this assessment-only shape is the final Session 020 shape per operator direction, it will still receive an entry at close).
- `open-issues.md` unchanged at this commit.

**Single-perspective session shape** (audit + assessment, no deliberation) follows Sessions 015, 016, 018, 019-open precedents. Kernel §3 adversarial-perspective requirement is scoped to *deliberative work where decisions will be made*; this assessment proposes an agenda and audits prior work without originating a cross-perspective design output. D-073/D-076/D-077 (`triggers_met: [none]`) precedent applies to any decision this session records at close if it terminates in assessment-only shape; otherwise the execution-path's decision(s) will carry their own triggers per content.

**Session 019 watchpoint WX-19-1** (first-class minority record-keeping discipline) monitored: §2.3 above inspected Session 019's three new minority warrants. All three pass the operationally-meaningful test; Minority 3 (Reviser asymmetry-probe) identified as softest but not ornamental. No sharpening needed unless a future session finds the "impairment" clause unable to be operationalised in practice.
