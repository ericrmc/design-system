---
session: 159
title: oi-s154-5-deliberation-grading-seal-time — deliberation
generated_by: selvedge export
---

# Deliberation

## D-23 — Shape of seal-time deliberation-grading clause: single-frame counterfactual + sub-type verification (sibling to DV-S155-1 close-time audit)

sealed_at: 2026-05-01T21:27:18.731Z

### P-1 (anthropic)

**Position.** Split OI-S154-5 and ship only seal-time single-frame counterfactual now as a §4 operator-policed clause mirroring DV-S155-1, payload one engine_feedback seal-grade row; sub-type verification stays harness-scope per DV-S152-1.

**schema_sketch.**
- No new table at v1 — reuse engine_feedback with flag observation and structured headline prefix seal-grade: mirroring DV-S155-1 audit-step: pattern.
- No new submit kind at v1 — the structured-headline convention already carried close-time audit; reuse compounds.
- No new column on synthesis_points or perspective rows; counterfactuals not surfaced by any P-N stay outside the typed convergence/divergence/minority enum.
- Sub-type verification rides DV-S152-1 nullable conflict_kind/closure_kind atoms on reference_harness, not on this clause.
- A future graduation could add a typed synthesis_point.kind=counterfactual value, but only after recurrence pressure on substrate, mirroring DV-S152-1 stage-gate.
**cli_surface.**
- After bin/selvedge submit deliberation-seal, submit one engine_feedback row: flag observation, body prefixed seal-grade: enumerating counterfactuals named or none-with-exclusion-reason.
- Lifts of named counterfactuals into typed synthesis_points use existing bin/selvedge submit synthesis-point with kind=minority — already the closest typed slot for an unrepresented stance.
- No new flag on deliberation-seal; ordering is operator-prose-policed identical to §8.5 audit-step and temporal-claim grounding.
- Free-prose paragraph in synthesis_md alone is rejected because it loses queryability across the seal-grade corpus.
**migration_path.**
- Bump prompts/development.md from v14 to v15 inserting §4 sub-clause Seal-time single-frame counterfactual grading, mirroring §8.5 close-time audit phrasing for visible parity.
- Bump methodology v10 to v11 §Synthesis to name the seal-grade row as part of synthesis discipline and call out S154-5 two-clause split; sub-type verification points to DV-S152-1.
- Engine-manifest engine-v45 to engine-v46 because methodology Synthesis is load-bearing.
- Open a sibling OI for sub-type verification at typed-observation closure, scoped to harness arcs only, citing DV-S152-1 — not bundled into this seal clause.
- Close OI-S154-5 by-mechanism, citing the §4 clause and the new sibling OI for sub-type verification; preserve M-? minority-track for future typed counterfactual synthesis_point kind.
- No SQL migration ships in this session; spec_only boundary holds, identical to DV-S155-1.
**what_not.**
- Do NOT add a new typed synthesis_point kind counterfactual at v1; recurrence pressure on substrate is absent and DV-S152-1 stage-gate-discipline forbids kernel-elevation on single-instance evidence.
- Do NOT bundle sub-type verification into this clause — the actor (harness operator) and substrate (reference_harness columns) differ, mirroring why D-21 excluded S154-5 from the close-audit.
- Do NOT make seal a substrate gate at v1 — calibration-EF recovery pathway is the same pattern DV-S155-1 chose and that DV-S130-1 temporal-claim grounding has run on for sessions.
- Do NOT permit a free-prose synthesis_md paragraph as the audit artefact; the seal-grade row is the inventory and the queryable surface, identical to audit-step.
- Do NOT extend perspective-claim section_kind enum with a counterfactual kind; the audit names what no perspective took, so it cannot be a perspective-claim by construction.
- Do NOT scope-limit to methodology-changing deliberations only; every sealed deliberation gets graded, matching the close-time audit session-universal scope.
**open_question.**
- What is the right exclusion list for single-frame counterfactual — where does the line sit for stance-shape variations within an axis already deliberated?
- Should the seal-grade row cite synthesis_md byte-offsets or atom-ids for each counterfactual named, or is free-prose locator (section heading + bullet) enough at v1?
- I do not know whether the synthesizer-as-actor materially changes the policing pattern; recurrence evidence is absent so empirical answer is unavailable.
- Does a deliberation that produces no convergence (only divergence + minority) still need a seal-grade row, or do divergence rows already enumerate the stance-space?
- Should reopen-on-new-reading interact with seal-grade — does a follow-up session that surfaces a missed option fire a calibration-EF against the prior seal-grade row automatically?
**risk.**
- Synthesizer self-grading is a known failure mode: an LLM enumerating counterfactuals it did not name may converge on the same blind spots; calibration-EF recovery is the only honest mitigation at v1.
- Prose-only seal-grade may be skimmed identically to §8.5 audit-step; if next-deliberation arc shows no new counterfactuals surfaced, the gate-promotion question fires earlier than expected.
- Splitting leaves sub-type verification on a sibling OI; if that OI drifts atop already-stacked harness debt the bundled framing of OI-S154-5 is lost without compensating progress.
- The structured-headline convention is now load-bearing across three clauses (temporal-claim, audit-step, seal-grade); a fourth or fifth pushes substring-matching analytics past viability and forces typed graduation.
- Operator burden: every sealed deliberation now requires two extra submits (seal-grade row + any lifted minority synthesis_point); ceremony-compounding risk that P-2 named at D-21 applies again here.
**what_lost.**
- Lost vs typed synthesis_point.kind=counterfactual now: clean queryability across the seal-grade corpus and a kernel-recognised stance-space-completeness primitive.
- Lost vs bundling both clauses: the OI-S154-5 framing as one discipline is broken; future readers see two siblings and may miss the original intuition that named them together.
- Lost vs scope-limiting to methodology-changing deliberations: avoidance of seal-grade ceremony on lightweight deliberations whose stance-space was obvious at convening time.
- Lost vs immediate substrate gate: guaranteed prevention of seals without a counterfactual inventory, which P-1 in D-21 argued for and which is preserved as the M-1 promotion target here too.
- Lost vs free-prose synthesis_md paragraph: zero-additional-submit ergonomics and tighter coupling between counterfactual naming and the synthesis text it grades.

### P-2 (openai)

**Position.** Ship a narrow seal-time counterfactual clause now, split sub-type verification back to the harness typed-observation pathway, and keep v1 agent-policed because the actor is the synthesizer.

**schema_sketch.**
- Add no table, column, trigger, or synthesis_point kind in v1; use an engine_feedback observation row with headline prefix seal-grade:.
- Define the counterfactual as the strongest no-perspective-took option that would change the synthesis if adopted and is admitted by synthesis coverage gaps.
- Exclude restatements, already preserved divergence or minority positions, micro wording, ordering, naming, and options barred by recorded constraints.
- Keep conflict_kind and closure_kind verification on reference_harness, because DV-S152-1 made them nullable opt-in harness atoms.
- A later gate can check row presence only, not counterfactual quality, so v1 should stay substrate-light.
**cli_surface.**
- Before deliberation-seal, submit engine-feedback with flag=observation and a seal-grade: body tied to the deliberation alias.
- The body names one counterfactual, explains why it would matter, and states whether synthesis addressed it, opened an FR, or nilled it by exclusion.
- Allow seal-grade: 0 only when the row names the exclusion that removed every qualifying alternative.
- If the counterfactual warrants future work, submit the FR before seal and cite it in the seal-grade: row.
- Typed-observation closure verification should use the harness surface when OI-S152-1 lands, not the deliberation CLI.
**migration_path.**
- Amend methodology §Synthesis after convergence-vs-coverage to require seal-time counterfactual naming for every deliberation seal.
- Amend prompts/development §4 so seal-grade: is submitted before deliberation-seal or explicitly nilled.
- Bump engine-manifest for prompt and methodology text only; no SQL migration or enum change ships in v1.
- Close OI-S154-5 only with split rationale: counterfactual discipline resolved, sub-type verification rehomed to harness work.
- If no existing harness issue can own verification at typed-observation closure, open one before resolving OI-S154-5.
**what_not.**
- Do not treat the synthesizer self-check as an independent perspective; methodology independence applies to perspectives, not synthesis.
- Do not add counterfactual to synthesis_points.kind without redesigning source-perspective semantics in prompts/development §4.
- Do not fold sub-type verification into seal-grade:, because that turns harness-field correctness into deliberation-quality prose.
- Do not gate v1 at the substrate; presence enforcement would not solve a weak or anchored self-audit.
- Do not let seal-grade: become a list of micro-edits or aesthetic alternatives.
**open_question.**
- Should seal-grade: 0 be rare and reviewable, or is nil a normal result for tightly scoped deliberations?
- Who may reject a weak seal-grade: row when the synthesizer and operator disagree before seal?
- Does a later calibration miss with a present but bad row trigger a gate, a reviewer step, or just tighter clause text?
- Which exact harness issue owns sub-type verification if OI-S152-1 remains only the nullable-column migration?
- Should routine non-kernel deliberations carry the same row, or is the deliberation threshold already the scope limit?
**risk.**
- The same LLM that chose the synthesis frame may name a counterfactual that confirms rather than challenges that frame.
- seal-grade: 0 can become empty compliance unless exclusions are concrete and later calibration can call misses.
- Rehomed sub-type verification may drift if no harness closure owner is named.
- engine_feedback prefix rows are weaker for later query than a typed table.
- A future gate may reward formulaic row presence while missing the actual unvoiced alternative.
**what_lost.**
- We lose typed queryability over seal counterfactuals until later evidence justifies a table or synthesis-point redesign.
- We lose immediate prevention of ungraded seals because v1 is agent-policed.
- We lose the apparent neatness of one OI becoming one clause.
- We lose any chance to canonicalize conflict and closure sub-types here, preserving DV-S152-1 non-canonical stance.
- We lose retrospective comfort because a seal-time I-do-not-know may force reopening under methodology §Reopen on new reading.

### P-3 (anthropic)

**Position.** Ship nothing new this session: close OI-S154-5 as superseded-by-existing-mechanism with a one-paragraph discipline reminder in methodology §Synthesis pointing at canonical divergence/minority synthesis_points and §Reopen-on-new-reading.

**schema_sketch.**
- No new substrate kinds, no new synthesis_point.kind enum value, no new engine_feedback headline prefix this session.
- Existing synthesis_points.kind in {convergence, divergence, minority} already carries the dissent-preservation load the OI names; reuse it.
- If a future session needs counterfactual-as-typed-thing, propose it then with calibration-EF evidence, not now on theory.
- Sub-type verification stays where DV-S152-1 placed it: nullable opt-in atoms on the harness substrate kind at workspace-experimental layer, kernel-agnostic.
- Reopen-on-new-reading is the existing mechanism for surfacing a load-bearing option no perspective named.
**cli_surface.**
- No new submit kind, no new payload shape, no extension to bin/selvedge submit deliberation-seal.
- The synthesizer continues to submit synthesis-point rows with the existing three kinds; dissent goes in divergence or minority.
- A future reader who spots a missed counterfactual files an engine-feedback row with flag=calibration naming the sealed deliberation.
- A follow-up session reopens via the existing pathway: cite the prior decision plus the new reading, treat prior synthesis as one input.
- No seal-grade: prefix; no inventory enumeration at seal-time.
**migration_path.**
- This session: dispose OI-S154-5 as superseded-by-existing-mechanism citing methodology §Synthesis dissent preservation plus §Reopen on new reading.
- This session: add a one-paragraph reminder to methodology.md §Synthesis or prompt-development §4 naming the failure mode and pointing at the existing surface — no new clause.
- Deferred: any typed counterfactual primitive waits for second-arc evidence per OI-S152-2 graduation trigger.
- Deferred: any seal-time gate waits for calibration-EF evidence of the failure mode actually recurring.
- Sub-type verification stays with harness; no kernel migration this session.
**what_not.**
- No §8.6 close-time-style clause for deliberation-seal; the symmetry with §8.5 is aesthetic, not load-bearing.
- No new counterfactual synthesis_point kind on theory; an enum without recurrence evidence is the fold-and-unfold pattern DV-S152-1 explicitly warned against.
- No seal-grade: engine_feedback prefix; another prefix multiplies the audit-step inventory pattern across surfaces with no evidence the seal-time variant is actually missed.
- No fold of the sub-type-verification half into a kernel clause; that half belongs entirely at workspace-experimental per DV-S152-1.
- No mirroring of DV-S155-1 v1-policed→v2-gate boilerplate; reflexive pattern-application is the ceremony attractor adversary-stance is paid to flag.
**open_question.**
- Has any sealed Selvedge deliberation actually shipped a missed load-bearing counterfactual that the existing dissent slots could not have absorbed?
- If the failure mode is real but rare, is operator-prompt discipline at synthesis time cheaper than a clause?
- Does folding the reminder into methodology §Synthesis vs prompt-development §4 matter for adoption?
- What is the bar for counterfactual-as-distinct-from-divergence — and can it be stated without the existing dissent vocabulary?
- Does OI-S154-5 title itself reflect a triage-time over-specification we should now correct?
**risk.**
- If the failure mode is real and recurring, ship-nothing leaves the gap open until calibration-EF evidence accumulates — same risk DV-S155-1 accepted but here without HIGH peer-arc evidence.
- A discipline reminder absent a clause may be invisible to future synthesizers; ceremony has discoverability, prose does not.
- Closing OI-S154-5 as superseded may be reopened later if a second arc surfaces the gap, paying the close-and-reopen cost twice.
- Adversary-stance ship-nothing can read as obstruction; the position must be recorded with the reasoning that admits later reversal.
- If P-1/P-2/P-4 converge on a clause and this perspective is the lone minority, the synthesis must preserve it as minority, not dilute it.
**what_lost.**
- A symmetric §8.6 surface that future readers could grep for alongside §8.5 — symmetry has cognitive value even if not load-bearing.
- The opportunity to ship the v1-policed→v2-gate trajectory in advance of recurrence, paying migration cost once if recurrence was inevitable.
- A typed counterfactual synthesis_point that future analytics could query distinctly from divergence/minority.
- A unified self-audit surface across session-close and deliberation-seal that R-1.5 of DV-S155-1 explicitly considered and rejected on different grounds.
- The HIGH-leverage version of OI-S154-5 disposition: closing with a clause closes the issue more durably than closing with a reminder pointing at existing surface.

### P-4 (anthropic)

**Position.** Ship the single-frame counterfactual half this session as a §4 prompt addition mandating a seal-counterfactual: engine_feedback row at deliberation-seal; defer sub-type verification to OI-S151-4 second-arc harness re-evaluation.

**schema_sketch.**
- No new substrate table; reuse engine_feedback with flag=observation headline prefix seal-counterfactual: per DV-S155-1 precedent.
- No new synthesis_points.kind value; the counterfactual is meta-on-the-synthesis, not a synthesis_point of the deliberation itself.
- Body enumerates 0..N positions no perspective took that the synthesis admits but did not address; 0 is a valid output if the synthesizer attests the frame is exhausted.
- Sub-type verification atom (closure_kind/conflict_kind cross-check vs DV-S152-1) explicitly out-of-scope for this clause.
**cli_surface.**
- bin/selvedge submit engine-feedback with flag=observation and body_md prefixed seal-counterfactual: <count>... after deliberation-seal and before next submit.
- No new submit kind; no new flag value; no schema migration.
- Document in prompt-development §4 (Convene perspectives) adjacent to the deliberation-seal CLI block, not in §8.5 which is session-close territory.
**migration_path.**
- Ship: prompt-development §4 paragraph, methodology.md §Synthesis one-sentence pointer, no engine bump.
- Defer: sub-type verification — ride OI-S151-4 second-arc gate; that arc is where typed-observation closure already lives.
- Defer: substrate gate on seal-counterfactual presence — promotion-trigger mirrors DV-S155-1 (calibration-EF naming a sealed deliberation reopened for an unnamed counterfactual fires gate-promotion OI).
**what_not.**
- Reject new synthesis_points.kind=counterfactual enum branch; adds schema surface for a discipline that may never gate (no operator-policed clause has graduated yet).
- Reject free-prose-only-in-synthesis_md; loses the calibration-EF anchor needed for v2 promotion-trigger to fire.
- Reject bundling sub-type verification into this clause; mechanically lives at harness re-evaluation (OI-S151-4) and applies only to disaster-response arc per DV-S152-1 opt-in atoms.
- Reject methodology-spec-only language without payload; loses the structured headline that lets future audits query seal-counterfactual: rows.
**open_question.**
- Whether single-frame counterfactual is policeable; methodology §reopen-warrant load-bearing option neither perspective named is the closest existing phrasing — cite or restate?
- Whether scope-limit to methodology-changing or kernel-touching deliberations is needed, or whether seal-counterfactual: 0 for tactical seals is cheap enough that a uniform requirement pays.
- Whether the synthesizer-as-actor (LLM, not operator) changes the v2 graduation bar — calibration-EFs are operator-authored, so the recovery path is structurally identical to DV-S155-1.
- I do not know whether retrospective single-frame misses are frequent enough to justify even this minimum shape; one substrate datapoint (D-21 excluding S154-5) is suggestive but thin.
**risk.**
- Ceremony-without-payoff: substrate scan shows zero operator-policed disciplines have graduated to gates (DV-S104-5, DV-S116-3, DV-S155-1, temporal-claim grounding all still v1); this clause may join the unfired-trigger pile.
- Synthesizer-gaming: the LLM author of the synthesis is the same actor naming counterfactuals it did not see, which is the same blind-spot the clause is trying to police.
- Definition-creep: single-frame counterfactual risks expanding to cover any minor unspoken alternative, defeating the load-bearing filter; exclusion list (mirroring §8.5) is needed.
- Coupling-leak: shipping without sub-type verification leaves OI-S154-5 partially open, requiring careful closure language to avoid orphan-issue confusion.
**what_lost.**
- Loses the unified treatment a two-clause shape would give: sub-type verification stays on the OI-S151-4 critical path, not this session.
- Loses the schema-typing benefit of synthesis_points.kind=counterfactual; future structured queries must filter engine_feedback.body_md LIKE seal-counterfactual: instead of joining a typed kind.
- Loses the option to gate seal-counterfactual presence at deliberation-seal directly; v2 graduation must wait for an unfired-counterfactual calibration-EF, which may take many sessions or never.
- Loses the symmetry of close-time and seal-time disciplines living in adjacent §8.5 anchors; placing the seal-clause in §4 is structurally correct but makes the discipline pair harder to read together.

### Synthesis

**D-23 synthesis — seal-time deliberation-grading clause shape.**

**Convergences (independent multi-perspective agreement).**

**C-1 SPLIT.** P-1 [P-23-P-1, Position], P-2 [P-23-P-2, Position], and P-4 [P-23-P-4, Position] independently converge on splitting OI-S154-5: ship the seal-time single-frame counterfactual clause now; rehome sub-type verification to the harness substrate kind per DV-S152-1, owned by OI-S151-4's second-arc re-evaluation gate. P-3 dissents on grounds that ship-nothing-and-reminder suffices [P-23-P-3, Position]; preserved as M-1 below.

**C-2 NO NEW SUBSTRATE AT V1.** P-1, P-2, and P-4 converge on operator/agent-policed v1 with no new table, no new synthesis_point.kind value, no new submit kind [P-23-P-1, Schema sketch; P-23-P-2, Schema sketch; P-23-P-4, Schema sketch]. Reuse engine_feedback flag=observation with structured headline prefix; promotion-trigger to substrate gate mirrors DV-S155-1 (calibration-EF naming a sealed deliberation reopened for an unnamed counterfactual fires gate-promotion OI). P-3 also rejects new substrate but on stronger ship-nothing grounds [P-23-P-3, What not].

**C-3 PREFIX `seal-grade:`.** P-1 (anthropic) and P-2 (openai-codex, cross-family) independently propose the headline prefix `seal-grade:` mirroring DV-S155-1's `audit-step:` pattern [P-23-P-1, Schema sketch; P-23-P-2, Schema sketch]. Cross-family convergence on naming carries weight beyond a single-family agreement. P-4 alone proposes `seal-counterfactual:` [P-23-P-4, Schema sketch] (preserved as D-1 divergence below).

**C-4 UNIVERSAL SCOPE.** P-1 and P-2 converge on requiring the row at every sealed deliberation, with `seal-grade: 0` admitted when a named exclusion removes every qualifying alternative [P-23-P-1, What not; P-23-P-2, CLI surface]. Matches close-time audit's session-universal scope; no methodology-changing-only gate. P-4 leaves scope as open question [P-23-P-4, Open questions]; P-3 dissents on the universal mandate.

**Divergences and minority preserved.**

**D-1 NAMING.** P-4 proposes `seal-counterfactual:` over `seal-grade:` for content-specificity [P-23-P-4, Position]. Recorded as divergence, not adopted: the cross-family C-3 convergence on `seal-grade:` carries the symmetry-with-audit-step argument that two perspectives reached independently.

**M-1 SHIP-NOTHING.** P-3 holds that OI-S154-5 surfaces a usage gap, not a mechanism gap, and that existing divergence/minority synthesis_points plus methodology §Reopen-on-new-reading already carry the load [P-23-P-3, Position; P-23-P-3, Migration path]. P-3 proposes closing OI-S154-5 as superseded-by-existing-mechanism with a one-paragraph methodology §Synthesis reminder.

M-1 is preserved as minority. The synthesis does not adopt M-1 because: (a) `divergence` and `minority` synthesis_point kinds preserve dissent among perspectives that took positions, not stances no perspective took; (b) §Reopen-on-new-reading is post-hoc recovery, but OI-S154-5 explicitly names "name single-frame counterfactual at seal time, NOT at retrospective time" — the discipline asks for prevention, not recovery; (c) substrate-light operator-policed clause with calibration-EF promotion path is the cheapest experiment that produces evidence for or against the mechanism.

M-1's strongest insight — that operator-policed clauses risk joining an unfired-trigger pile (P-4 substrate evidence: zero promotions to gates yet [P-23-P-4, Risks]) — is folded into the migration_path: the v2 promotion trigger is named explicitly so future evidence either fires it or affirms M-1's prediction.

**[synth] residual.** The synthesizer notes that the §4-vs-§Synthesis placement question (P-1 in §4 with methodology pointer; P-3/P-2 lean methodology §Synthesis primary) is resolved by analogy with DV-S155-1: the operational clause with payload shape lives in prompt-development; methodology carries a one-sentence pointer naming the sibling discipline. Engine-version bump: the kernel-touching nature (methodology §Synthesis amendment is load-bearing per P-1's reasoning) warrants engine-v45 to engine-v46 mirroring DV-S155-1's bump cadence.

**Decision frame for DV-S159-1.**

Adopt: §4 seal-time deliberation-grading clause; engine_feedback prefix `seal-grade:`; universal scope; v1 operator/agent-policed; v2 promotion via calibration-EF. Methodology §Synthesis one-sentence pointer. Sub-type verification rehomed to a new sibling OI under OI-S151-4's gate. Close OI-S154-5 by-mechanism citing the clause and the new sibling OI. Bump prompt-development v14→v15, methodology v10→v11, engine-v45→v46.

Reject: M-1 ship-nothing (preserved as minority); P-4 prefix-naming `seal-counterfactual:` (preserved as divergence); typed `synthesis_point.kind='counterfactual'` (insufficient recurrence pressure); fold sub-type verification into the seal clause (mechanically distinct, harness-scope per DV-S152-1).

### Synthesis points

- **convergence C-1.** Split OI-S154-5: ship counterfactual clause now; rehome sub-type verification to harness per DV-S152-1 / OI-S151-4.
- **convergence C-2.** No new substrate at v1; reuse engine_feedback observation with structured headline prefix; v2 promotion via calibration-EF mirrors DV-S155-1.
- **convergence C-3.** Headline prefix `seal-grade:` mirroring `audit-step:` pattern; cross-family convergence (P-1 anthropic + P-2 openai-codex).
- **convergence C-4.** Universal scope: every sealed deliberation gets a seal-grade row; `seal-grade: 0` admitted with named exclusion.
- **divergence D-1.** Naming: P-4 proposed `seal-counterfactual:` for content-specificity over `seal-grade:` symmetry; not adopted.
- **minority M-1.** Ship nothing; close OI-S154-5 as superseded-by-existing-mechanism using divergence/minority synthesis_points and methodology §Reopen.
