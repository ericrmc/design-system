med threshold.
    29	   - Differentiation: distinguish "major" (new spec files, kernel revisions, new required-fields) from "minor" substantive (budget-value tuning, constant updates, prose corrections with behavioral change).
    30	   - Cadence-aware bumping: raise the bar for adjacent-session bumps; require exceptional justification.
    31	
    32	2. **Whether engine-version portability metadata should be added.** Candidate: an engine-v-compatibility table in engine-manifest.md naming which engine-versions are backwards-compatible with which (for external applications loading an older engine-version). This would be a new normative section, itself substantive per OI-002.
    33	
    34	3. **Whether to revise engine-manifest §7 history-entry discipline.** Current history entries describe what was substantively different in each bump; Calibrator [01a Q5] recommended strengthening this annotation discipline for cadence-periods so external adopters can distinguish substantive-vs-ceremonial bumps from the history alone.
    35	
    36	**Session 024+ activation triggers.**
    37	
    38	This OI is open but deferred. The deliberation becomes active if any of:
    39	
    40	- **engine-v5 proposed before Session 026.** Any further engine-v-bump within three sessions of Session 023 would produce four bumps in five sessions (or equivalent). §5.4 minority elevates to substantive.
    41	- **External-application portability confusion observed.** An external-application workspace reports rule-drift between adjacent engine-versions (e.g., loaded engine-v2 but ran validator checks that assume engine-v4 rules). §5.4 minority elevates to substantive regardless of cadence pattern.
    42	- **Operator direction.** The operator may undertake OI-018 deliberation in any session as Path-E operator-directed agenda.
    43	
    44	**Until activation trigger fires.** Session 024+ sessions should:
    45	- Record in their close whether any engine-v-bump was proposed and, if so, explicit justification.
    46	- Note this OI-018 in the OI-monitoring list at close (similar to the OI-009 G/O/K/S criterion-package monitoring precedent).
    47	- Not undertake pre-emptive §5 revisions without the activation trigger firing (per same-session-causing-and-revising prohibition from Q5 unanimity).
    48	
    49	**Interaction with §5.4 Session 022 minority.** §5.4 is preserved verbatim in `provenance/022-workspace-scaling-trajectory/01-deliberation.md` per D-017 immutability. This OI does not edit that record; it provides the operational handle for the §5.4-triggered deliberation when the trigger fires. The §5.4 minority text is the binding source for the warrant; this OI is the procedural instrument.

 succeeded in 0ms:
   260	
   261	**Single-deliberation sessions** use flat numbered files at the session's provenance root, consistent with Sessions 001, 002, 003, and 004:
   262	
   263	```
   264	provenance/<NNN-title>/
   265	  00-assessment.md
   266	  01-brief-shared.md            # optional: shared brief preserved for auditability
   267	  01a-perspective-<role>.md
   268	  01b-perspective-<role>.md
   269	  ...
   270	  01-deliberation.md            # synthesis
   271	  manifests/
   272	    <role>.manifest.yaml        # one per participant
   273	  participants.yaml             # session-level index
   274	  human-review.md               # if a reviewer-shape participant was included
   275	  STATUS.md                     # if the session halted awaiting a non-Claude response
   276	  02-decisions.md
   277	  03-close.md
   278	```
   279	
   280	When all briefs in the deliberation share byte-identical non-role sections (the default), briefs need not be preserved as separate files — each raw-output file already contains the role-specific stance, and the shared sections are derivable from any brief. If briefs in a deliberation depart from this shape (e.g., differentiated context), the briefs must be preserved as separate files named `01*-brief-<role>.md`.
   281	
   282	**Multi-deliberation sessions** use a subdirectory layout:
   283	
   284	```
   285	provenance/<NNN-title>/
   286	  00-assessment.md
   287	  deliberations/
   288	    <decision-id>/
   289	      briefs/
   290	        00-shared-context.md
   291	        01-<role>.md
   292	      responses/
   293	        01-<role>.md
   294	        ...
   295	      manifests/
   296	        <role>.manifest.yaml
   297	      participants.yaml
   298	      human-review.md             # if a reviewer-shape participant was included
   299	      synthesis.md
   300	      manifest.json               # session-level metadata (model IDs, timestamps, commit)
   301	  02-decisions.md
   302	  03-close.md
   303	```
   304	
   305	`manifest.json` records deliberation-level metadata (commit hash at convening time, deliberation decision-id, start/end timestamps). Per-participant detail lives in the `manifests/` directory.
   306	
   307	### Graceful Degradation
   308	
   309	- **Minimum viable quorum.** If a perspective fails to return an output (error, refusal, malformed response), the deliberation may proceed with the remaining perspectives provided at least three returned valid outputs. The failure is recorded in the synthesis file's frontmatter or in `manifest.json`.
   310	- **Stance refusal.** A perspective that refuses the assigned stance, or that substantively disagrees with the brief itself, has its refusal preserved as provenance. Refusal is signal, not an error to coerce around.
   311	- **Fewer than three valid outputs.** The deliberation must be re-run or the question reformulated. A synthesis over one or two perspectives is not a multi-agent deliberation.
   312	- **Non-Claude participant non-response.** Per the halt-before-synthesis rule, synthesis does not proceed when a Shape-A non-Claude participant has not responded. Timeout policy (whether a session may eventually proceed after N days with a recorded opt-out) is not mandated by v2; the halt is in place until the awaited response is committed or the session formally records opt-out.
   313	
   314	### Limitations
   315	
   316	These statements are required content for every multi-agent deliberation's synthesis or decision record that relies on a Claude-only mechanism:
   317	
   318	- **All Claude-subagent perspectives share a model family.** The parallel-subagent implementation uses instances of the same Claude model family. Shared training produces shared blind spots: the same cultural priors, argumentative reflexes, refusal patterns, and aesthetic preferences.
   319	- **Intra-Claude-family size-mixing is not cross-model participation.** Mixing Opus, Sonnet, and Haiku does not narrow OI-004; it may surface capability-band differences but does not introduce independent training lineages. See OI-011 for separate tracking of intra-family mixing.
   320	- **Parallel isolation prevents conversational anchoring, not training-distribution anchoring.** Four instances of the same model, given briefs written in a shared vocabulary, will correlate in ways that look like agreement but are actually shared priors. Consensus across subagents is weak evidence, not strong.
   321	- **Brief-writing has no adversary.** The convening agent's framing choices propagate into all perspectives identically. Adding multi-agent to brief-writing creates infinite regress; the methodology does not pretend otherwise.
   322	- **The synthesis step is the pattern's highest-risk single-agent re-entry point.** Synthesis conventions (citation, dissent-preservation, `[synth]` marker, quote-over-paraphrase) reduce but do not eliminate this risk.
   323	- **Non-Claude participation depends on convener fidelity.** The transport guarantee is over the record, not the generation. The convener must commit the participant's response verbatim; there is no automated verification of faithfulness at v2. See Open Extensions below for future enforcement directions.
   324	- **A single non-Claude participant narrows OI-004 less than its presence suggests.** One human reviewer selected from the operator's social graph shares correlated priors with the operator; one non-Anthropic model accessed once may not reveal training differences that emerge only over many interactions. Closure of OI-004 requires sustained practice (see the Closure section).
   325	
   326	The specification's tone on limitations is deliberately uncompromising. Softening the language in future revisions is not a minor correction.
   327	
   328	### Closure Criteria for OI-004
   329	
   330	OI-004 may be considered for closure when all of the following hold:
   331	
   332	1. **Participant independence.** At least one participant in qualifying deliberations has `training_lineage_overlap_with_claude: independent-claim` (non-Anthropic model) or `participant_kind: human` with a `participant_selection_method` other than `self`.
   333	2. **Sustained practice.** Non-Claude participation has occurred in at least three required-trigger deliberations across different sessions, recorded correctly per the schema above.
   334	3. **Recorded impact.** The synthesis or decision records show that non-Claude input shaped at least one outcome — the cross-lineage-influence ratio (see Open Extensions) is non-zero.
   335	4. **Articulation.** A successor decision defines what "substantively different training provenance" means and enumerates acceptable participant kinds. Articulated Session 021 per D-082; see §Criterion-4 Articulation for OI-004 below.
   336	
   337	OI-004 is not automatically closed on meeting these criteria; a future session must deliberate and decide. "Closable" and "closed" are distinct states. The OI now has a four-state lifecycle (added v4); see §Closure Procedure for OI-004 below.
   338	
   339	### Criterion-4 Articulation for OI-004
   340	
   341	(Added v4 per D-082, Session 021.)
   342	
   343	Criterion 4 requires an **independence warrant** with two branches: model-provenance independence (for LLM participants) and selection independence (for human participants). The two-branch structure follows the Outsider's frame-completion contribution at Session 021 [01d, Q1] — "training provenance" is the right question for model participants but the wrong question for humans, where selection-process independence is the load-bearing dimension.
   344	
   345	**For model participants**, "substantively different training provenance" is established by ALL of the following:
   346	
   347	1. **Organisational origin distinct from Anthropic.** Recorded as `participant_organisation: <name>` in the Layer 2 manifest; the organisation MUST NOT be Anthropic, MUST NOT be a known Anthropic-derived entity, and MUST be a value in the closed set enumerated in `tools/validate.sh` PARTICIPANT_ORGANISATION_CLOSED_SET (initial set: openai, google, meta, xai, mistral, deepseek, cohere, local, other-named; extensible by named decision per `validation-approach.md` v4 §Closed-set extension discipline).
   348	
   349	2. **No documented Claude-derived training dependency.** No public documentation that the LLM was trained on Claude outputs (distillation, synthetic-data sourcing, or RLAIF using a Claude reward model). Recorded as `claude_output_in_training: known-no | known-yes | unknown` in the Layer 2 manifest. Where `known-yes`, the participant fails this prong. Where `unknown`, the participant is recorded as such; `unknown` is itself signal per the unknown-field rule and surfaces to Tier 2 Q8 review (see `validation-approach.md` v4).
   350	
   351	3. **Stable attributable identity at provider / model-family / model-id granularity.** Sufficient for audit: a future auditor must be able to identify *which specific model* participated. Recorded across the existing `provider`, `model_family`, `model_id`, `model_version` fields. A participant lacking any of these is `unknown` at that level and fails this prong.
   352	
   353	**For human participants**, the analogous requirement is **selection independence from the operator**:
   354	
   355	1. `participant_selection_method` MUST NOT be `self`.
   356	2. Selection method MUST be one of `solicited-externally`, `pre-registered`, or `solicited-from-graph` (the last conditionally; see §Acceptable Participant Kinds for OI-004 below).
   357	3. Selection-method context MUST be recorded in `selection_relationship_to_operator` (free-text or `n/a`).
   358	
   359	**Operational corroboration** (criterion 3, the existing acceptance test) is required to convert eligibility-under-this-articulation into actual narrowing. Criterion-4 articulation defines *who can count*; criterion 3 verifies *whether they did*. This bifurcation follows the 2-of-4 cross-family Session 021 split with cross-family weighting (Skeptic + Outsider) on placing operational corroboration in criterion 3 rather than in criterion-4 definition. The Articulator's [01a, Q1] D-Min ∩ O-Corr position and the Operationaliser's [01c, Q1] P4 position (operational corroboration as definitional prong) are preserved as joint first-class minority §5.5 in `provenance/021-oi004-criterion4-articulation/01-deliberation.md` with operational activation triggers.
   360	
   361	**Audit-time test.** For any deliberation `S` claiming OI-004-narrowing participation by `P`:
   362	
   363	1. Verify `P`'s manifest declares the v4 fields `participant_organisation` (if `non-anthropic-model`), `claude_output_in_training`, `training_lineage_evidence_pointer` (if `independent-claim`), `selection_relationship_to_operator` (if `human`), and `independence_basis`. Missing fields are validation failures (checks 16, 17, 19).
   364	2. Verify the model-branch or human-branch prongs above hold per declared values. If any prong fails, the criterion-4-narrowing claim for `P` is rejected.
   365	3. Verify criterion-3 evidence (recorded impact) for `P` exists in the deliberation's synthesis or decision record. If absent, the participant is eligible-on-trust for an introductory window of three required-trigger deliberations; thereafter, criterion-3 evidence is required.
   366	
   367	### Acceptable Participant Kinds for OI-004
   368	
   369	(Added v4 per D-082, Session 021.)
   370	
   371	The following participant categories are **acceptable** when their per-participant manifest satisfies the criterion-4 articulation prongs above.
   372	
   373	**Qualifying alone** (count toward OI-004 narrowing without combination):
   374	
   375	- **Non-Anthropic LLM via own provider's endpoint.** `participant_kind: non-anthropic-model`; `provider` in closed set; `aggregator_intermediary: n/a`. Examples: GPT-family via `codex exec`; Gemini via Google API; Llama via Meta endpoint.
   376	- **Non-Anthropic LLM via aggregator API.** Same as above but with the underlying provider/model/version recorded; `aggregator_intermediary: <name>` field required and non-empty. Operator MUST disclose if the aggregator is known to apply system-prompt modifications that could mask training-provenance signal.
   377	- **Locally hosted open-weight model.** `participant_kind: non-anthropic-model`; `provider: local`; weights lineage recorded in `transport_notes`; `claude_output_in_training: known-no` (open-weight models with public training-data cards typically support this) or `unknown` with explicit acknowledgement.
   378	- **Human reviewer recruited externally.** `participant_kind: human`; `participant_selection_method: solicited-externally`. Recruitment channel MUST be recorded in `selection_relationship_to_operator`; compensation, if any, MUST be disclosed in `transport_notes`.
   379	- **Human reviewer pre-registered.** `participant_kind: human`; `participant_selection_method: pre-registered`. Pre-registration date and basis MUST be recorded.
   380	
   381	**Qualifying only in combination** with another qualifying participant:
   382	
   383	- **Human reviewer from operator's social graph.** `participant_kind: human`; `participant_selection_method: solicited-from-graph`; `selection_relationship_to_operator:` annotation required and substantive. Per the existing Limitations note, this category alone does not substantiate cross-provenance independence; combination with at least one Qualifying-Alone participant is required.
   384	
   385	**Qualifying shapes**: both `participation_shape: perspective` and `participation_shape: reviewer` qualify if the independence-preserving procedure is documented per the existing Non-Claude Participation Mechanism section.
   386	
   387	**Recommended for high-stakes deliberations** (D-023-triggering; engine-version bumps; OI closures): panel of multiple non-Claude participants. Not required for criterion 4; recorded as a synthesis-frontmatter signal for future analyses.
   388	
   389	**Excluded**:
   390	
   391	- `participant_kind: claude-subagent` (per existing Claude-Only-Is-Not-Cross-Model rule).
   392	- `participant_kind: anthropic-other` — the affirmative complement to Claude-Only-Is-Not-Cross-Model: intra-Anthropic mixing does not satisfy OI-004 even with model-branding distinctions. (Per Operationaliser [01c, Q2] and Outsider [01d, Q2] convergence.)
   393	- `participant_kind: unknown`.
   394	- Any participant with `training_lineage_overlap_with_claude: known-overlap`.
   395	- `participant_kind: human` with `participant_selection_method: self`.
   396	
   397	**Mechanical cross-family invocation outside the perspective-deliberation frame** (the Session 018 pattern) is **NOT** a participant kind for OI-004 narrowing. It MAY be recorded as corroborating evidence for criterion 3 in the session-level participants index via the `mechanical_cross_family_invocation:` block (schema above). Mechanical invocation supplements but does not substitute for participant-perspective contribution. (4-of-4 cross-family convergence at Session 021.)
   398	
   399	The Skeptic's [01b, Q2] strict-enumeration position — enumerate only kinds the methodology has operationally exercised — is preserved as first-class minority §5.1 in `provenance/021-oi004-criterion4-articulation/01-deliberation.md` with operational activation triggers including unexercised-enumeration-cited-as-narrowing-basis.
   400	
   401	### Closure Procedure for OI-004
   402	
   403	(Added v4 per D-082, Session 021.)
   404	
   405	OI-004 has four ordered states:
   406	
   407	1. **Open.** Default until criteria 1–3 are satisfied.
   408	2. **Closable pending criterion-4 articulation.** Criteria 1–3 satisfied; criterion 4 not yet articulated. (Sessions 009–020 held this state.)
   409	3. **Articulated; awaiting closure-retrospective.** All four criteria articulated as auditable predicates per §Criterion-4 Articulation above. Closure requires a one-time `oi-004-retrospective.md` artefact applying the criteria to the cumulative record. (Sessions 021+ hold this state.)
   410	4. **Closed.** The retrospective artefact is committed, `validate.sh` check 18 passes for the artefact, Tier 2 Q8 has been answered substantively, and a successor session has decided on OI-004 closure with explicit citation to the retrospective.
   411	
   412	States are advanced by named decisions, not asserted by prose annotation. A state advance from Articulated (state 3) to Closed (state 4) requires ALL of the following:
   413	
   414	(i) **Closure-retrospective artefact** committed at `provenance/<NNN-closure-session>/oi-004-retrospective.md` containing the three required sections (`## Qualifying Deliberations Table`, `## Summary Tally`, `## P4 Assertion`) per check 18; plus `validate.sh` check 18 PASS; plus Tier 2 Q8 substantively answered.
   415	
   416	The retrospective's Qualifying Deliberations Table contains one row per Sessions-005-onwards qualifying deliberation with columns: session number; decision id(s); participant kinds; per-prong satisfaction (boolean per row) of criterion-4 articulation prongs; criterion-3 data points contributed; frame-replacement-or-novel-mechanism flag (boolean).
   417	
   418	The Summary Tally totals: total qualifying deliberations; total non-Claude participants; total criterion-3 data points; total frame-replacement-or-novel-mechanism instances.
   419	
   420	The P4 Assertion explicitly cites at least one cross-lineage divergence-from-Claude-consensus with `[provenance/<NNN>/<file>, §X]` citation. (Per Skeptic [01b, Q3] condition (i): a documented case where the non-Claude participant's position contradicted Claude-perspective consensus AND the synthesis adopted the non-Claude position.)
   421	
   422	(ii) **Successor-session adjudication.** The closure decision must be made by a session distinct from the session that articulated criterion 4 (Session 021 for the initial articulation). The successor session must be a multi-agent deliberation with non-Claude participation per §When Non-Claude Participation Is Required clause 4 (asserts a change in OI-004 state). The successor session's Outsider should not be the same instance as the articulating session's Outsider where feasible.
   423	
   424	(iii) **Cross-model contradiction-prevailing data point** identified in the retrospective per the P4 Assertion above. If absent in the existing record, OI-004 remains in state 3 until such a case occurs in a future deliberation.
   425	
   426	(iv) **Sustained-practice forward commitment**: voluntary:required ratio (counted across non-Claude participation history) remains ≥1.0 at successor-session adjudication time. Drift below would be evidence the discipline weakened post-articulation.
   427	
   428	The Articulator's [01a, Q6] and Outsider's [01d, Q6] sub-option-(a) "close-on-articulation" positions are preserved as first-class minorities §5.2 and §5.3 in `provenance/021-oi004-criterion4-articulation/01-deliberation.md` with operational activation triggers including the Outsider's "indefinitely movable finish line" warrant.
   429	
   430	### Interaction with Existing Decisions
   431	
   432	- **D-005** (perspectives are work-specific, not fixed) — reaffirmed.
   433	- **D-009** (acknowledgment of simulated disagreement) — remains in force. Its scope now includes the Claude-monoculture limitation of the Claude-subagent mechanism, not only the original same-context simulation case, and it extends further to the trust-boundary limitation of human-mediated non-Claude participation transport.
   434	- **D-014** (minor-correction heuristic) — reaffirmed.
   435	- **D-016** (multi-agent triggers) — reaffirmed; this specification's "When Non-Claude Participation Is Required" extends, rather than replaces, D-016's triggers.
   436	- **D-020** (treatment of v1 kernel pointer as minor) — reaffirmed.
   437	- **D-022** (Claude-only is not cross-model) — integrated as the Claude-Only-Is-Not-Cross-Model rule above; v4 extends this to anthropic-other per §Acceptable Participant Kinds for OI-004.
   438	- **D-025** (this session does not narrow OI-004 operationally) — the specification records OI-004 as state 3 ("Articulated; awaiting closure-retrospective") per v4 four-state lifecycle.
   439	- **D-082** (Session 021 — OI-004 criterion-4 articulation; engine-v1 → engine-v2 bump) — adopts the criterion-4 articulation, acceptable-participant-kinds enumeration, schema additions, and four-state lifecycle in v4.
   440	
   441	### Open Extensions
   442	
   443	These directions are noted as candidates for future revisions, not mandated. Each entry records its **activation precondition**: the concrete event or schema change that would make the extension worth revisiting (per D-035, Session 005; the pattern is "keep rule-history inside the artifact that enforces the rule" per the Archivist's Session 005 Q6 proposal).
   444	
   445	- **Differentiated context per perspective** (from Session 003's Futurist position) — each perspective receives only the workspace context its stance requires, declared by the brief. *Activation precondition: a session surfaces evidence that shared-brief uniform context distorted outputs (e.g., a brief-priming failure beyond the level observed in Session 004's "training-distribution theatre" phrase).*
   446	- **Cross-lineage-influence ratio** (from Session 004's Skeptic) — a measured ratio, across a rolling window of deliberations, of decisions where a non-Claude participant's position differed from the synthesized Claude consensus and the synthesis adopted the non-Claude position. Suggested floor: above 10% over a ten-deliberation window for non-Claude participation to be considered genuinely impactful. Not mandated; candidate for a validation-tool enhancement. *Activation precondition: OI-004 approaches closure (closure criterion 3 explicitly requires this metric or equivalent evidence-of-impact).*
   447	- **Pre-committed dissent log** (from Session 004's Skeptic) — after synthesis the operator writes what they expected the synthesis to conclude before reading it, committed as a separate hashed file. Measurement tool for operator-synthesis alignment. *Activation precondition: a session surfaces evidence of suspected operator-synthesis alignment (e.g., a synthesis that reads as confirmation of the operator's stated priors rather than of the raw outputs).*
   448	- **Integrity hashing, append-only raw files, convener attestation** (from Session 004's Archivist) — `raw_response_sha256` per raw output, enforced by `validate.sh`; raw files append-only from commit; a `convener_attestation` field in manifests. All deferred to a future tooling session. *Activation precondition: one instance of suspected post-hoc editing of a raw output, OR a future session decides check 13's gaming surface needs narrowing. These three items are paired; adopt together or not at all, since each alone is partial.*
   449	- **Structural validation cross-check for OI-004 honesty** (from Session 004's Skeptic) — `validate.sh` fails sessions that claim OI-004 narrowing in a decision record while recording all `participant_kind: claude-subagent` in their provenance. Requires extending the validator's parsing beyond structural checks. *Activation precondition (revised Session 006, D-042): `triggers_met:` is adopted prospectively (done Session 006 via D-037 through D-040) AND at least one post-adoption decision asserting an OI-004 state change exists, OR a separate non-mutating retrospective index has been produced for earlier cases per the D-039 retrospective-artefact pattern. Rationale for revision: Session 005's D-033 narrowing (the original first test case) predates `triggers_met:` adoption under D-039's session-number gating; a derivative check would have no in-scope test case until a post-adoption OI-004-state-change decision is made. Additionally, Session 006's D-043 is itself an OI-004 state change and implementing the check in Session 006 would have required grading Session 006's own claim (Skeptic, Session 006 Q6) — a conflict of interest on first firing.*
   450	- **Disagreement-density metric** (from Session 003) — count or rate disagreements across perspectives' outputs; flag suspiciously low values as likely training-induced correlation. *Activation precondition: a reporter-tool scope is defined distinct from `validate.sh` (which is scoped to structural checks, not measurements).*
   451	- **Pluggable synthesizer role** — different model, human reviewer, or panel synthesising. Requires designing synthesizer selection and accountability. *Activation precondition: a session surfaces a load-bearing synthesizer-framing failure that single-synthesizer conventions cannot correct.*
   452	- **Non-Claude synthesizer** — when synthesis is itself load-bearing and contested, the synthesizer may be a non-Claude participant (reducing the single-model re-entry risk). *Activation precondition: check 13 gaming becomes a live concern (recorded in provenance) AND a non-Claude synthesizer channel is available.*
   453	- **Multi-agent synthesis** — recursive application of this pattern to the synthesis step itself when contested. *Activation precondition: a session surfaces a synthesis quality gap unaddressed by single-synthesizer conventions (citation, dissent-preservation, `[synth]` markers, quote-over-paraphrase).*
   454	- **Non-Anthropic model participation via API** — direct path to OI-004 closure that becomes available when the workspace's permissions and secrets allow an outbound non-Anthropic API call. *Activation precondition: a concrete need for API-based transport that CLI wrappers (demonstrated usable in Session 005 via `codex exec`) cannot serve.*
   455	
   456	## Validation
   457	
   458	To validate this specification:
   459	
   460	1. For every session with provenance, identify each Decision the session recorded. Each Decision that meets any trigger in "When Multi-Agent Deliberation Is Required" must be backed by either (a) multi-agent deliberation artifacts (raw perspective files plus a synthesis) or (b) an explicit single-agent annotation naming the reason.

 succeeded in 0ms:
     1	---
     2	id: OI-015
     3	status: see-body
     4	surfaced-in-session: see-body
     5	---
     6	
     7	### OI-015: Laundering enforcement gap in domain reading
     8	**Surfaced:** Session 011 (per D-061; sourced from four-way convergent concern at Q4 across Reviser [01a, Q4], Minimalist [01b, Q4], Skeptic [01c, Q4], Outsider [01d, Q4])
     9	**Status:** Open — activation trigger specified
    10	The Session 011 kernel §1 Read revision (per D-060) names "domain reading" as a legitimate Read-activity sense and includes a reconciliation clause requiring that domain inputs be *surfaced* (named, recorded) rather than silently applied. The reconciliation honours PROMPT.md's anti-silent-import rule. But four-of-four Session 011 perspectives identified a residual enforcement gap: the reconciliation requires domain inputs be surfaced at Read; it does not require surfaced domain inputs be *re-examined as choices* at Deliberate or Decide. A future session could surface a pretrained intuition as "domain reading" and then have the deliberation treat it as given context rather than proposed option — a conclusion smuggled rather than surveyed. Verbatim failure-mode samples from the four perspectives:
    11	
    12	- [Reviser, 01a, Q4]: "A perspective... wants a workspace-level revision... They rationalise it as emerging from 'domain reading'... But what actually happened is the perspective imported a methodology idea from pretraining... Silent import, laundered through Read."
    13	- [Minimalist, 01b, Q4]: "The orchestrating agent has, from pretraining, a strong intuition about the answer. Rather than running an explicit surveying step that would force the intuition to compete with alternatives, the agent labels the intuition 'domain reading' and absorbs it as Read-activity context."
    14	- [Skeptic, 01c, Q4]: "The conclusion — 'use BATNA' — was smuggled in at Read, then validated by the subsequent steps treating it as environment rather than choice. This is the failure. It is not hypothetical; it is the natural shape of the failure mode once domain reading is legitimised."
    15	- [Outsider, 01d, Q4]: "The orchestrating agent knows, from pretraining, a standard movement or facilitation pattern. It writes a brief that already encodes that pattern, labels it 'domain reading,' and then lets perspectives deliberate over a pre-shaped solution."
    16	
    17	Enforcement would require one or more of: kernel §4 Deliberate elaboration requiring re-examination of domain inputs; kernel §5 Decide elaboration requiring domain-input-sourced claims to cite specific brief/survey language; a new `validate.sh` check; a brief-authoring convention distinguishing user-stated-constraints provenance from pretrained-input provenance. **Activation trigger:** first post-Session-011 external-artefact session where a laundering pattern (domain input accepted as given rather than surveyed) is observed and recorded, OR a session proposes kernel §4/§5 revision addressing the gap. Preferred starting point for future deliberation: whether the enforcement mechanism should live in kernel §4 Deliberate, kernel §5 Decide, or a separate brief-authoring convention. Such a deliberation would likely be D-023_1-triggering (kernel revision) and require non-Claude participation.
    18	
    19	**Session 013 annotation:** Session 013's Read activity included both workspace reading (full workspace state) and domain reading (user's verbatim Validate report as primary domain input). No laundering pattern occurred: the user's report was preserved verbatim in `00-validate-user-report.md` and re-examined explicitly in the deliberation's Q1–Q6 rather than absorbed silently as Read-activity context. OI-015 did not activate; Session 013 is a positive example of the reconciliation working as intended.
    20	
    21	

exec
/bin/zsh -lc ./tools/validate.sh in /Users/ericmccowan/Development/complex-systems-engine
codex
The validator is still streaming. I’m polling for the part that matters here: current check 20 output, aggregate count, and whether the live workspace matches the brief’s 6,403-word figure.
 exited 1 in 8622ms:
  ✓ methodology-kernel.md — all required fields present
  ✓ multi-agent-deliberation-v1.md — all required fields present
  ✓ multi-agent-deliberation-v2.md — all required fields present
  ✓ multi-agent-deliberation-v3.md — all required fields present
  ✓ multi-agent-deliberation.md — all required fields present
  ✓ read-contract-v1.md — all required fields present
  ✓ read-contract.md — all required fields present
  ✓ reference-validation-v1.md — all required fields present
  ✓ reference-validation.md — all required fields present
  ✓ validation-approach-v1.md — all required fields present
  ✓ validation-approach-v2.md — all required fields present
  ✓ validation-approach-v3.md — all required fields present
  ✓ validation-approach-v4.md — all required fields present
  ✓ validation-approach.md — all required fields present
  ✓ workspace-structure-v1.md — all required fields present
  ✓ workspace-structure-v2.md — all required fields present
  ✓ workspace-structure-v3.md — all required fields present
  ✓ workspace-structure.md — all required fields present

[4] Specification sections
  ✓ engine-manifest.md — all required sections present
  ✓ identity-v1.md — all required sections present
  ✓ identity.md — all required sections present
  ✓ methodology-kernel-v1.md — all required sections present
  ✓ methodology-kernel-v2.md — all required sections present
  ✓ methodology-kernel-v3.md — all required sections present
  ✓ methodology-kernel-v4.md — all required sections present
  ✓ methodology-kernel.md — all required sections present
  ✓ multi-agent-deliberation-v1.md — all required sections present
  ✓ multi-agent-deliberation-v2.md — all required sections present
  ✓ multi-agent-deliberation-v3.md — all required sections present
  ✓ multi-agent-deliberation.md — all required sections present
  ✓ read-contract-v1.md — all required sections present
  ✓ read-contract.md — all required sections present
  ✓ reference-validation-v1.md — all required sections present
  ✓ reference-validation.md — all required sections present
  ✓ validation-approach-v1.md — all required sections present
  ✓ validation-approach-v2.md — all required sections present
  ✓ validation-approach-v3.md — all required sections present
  ✓ validation-approach-v4.md — all required sections present
  ✓ validation-approach.md — all required sections present
  ✓ workspace-structure-v1.md — all required sections present
  ✓ workspace-structure-v2.md — all required sections present
  ✓ workspace-structure-v3.md — all required sections present
  ✓ workspace-structure.md — all required sections present

[5] Provenance directory naming
  ✓ 001-genesis
  ✓ 002-self-validation
  ✓ 003-multi-agent-deliberation
  ✓ 004-participation-mechanisms
  ✓ 005-schema-enforcement
  ✓ 006-triggers-met-schema
  ✓ 007-external-application-examination
  ✓ 008-first-external-application
  ✓ 009-external-validate-receipt
  ✓ 010-household-decision-protocol
  ✓ 011-w1-kernel-read-revision
  ✓ 012-methodology-naming
  ✓ 013-artefact-revision
  ✓ 014-oi016-resolution
  ✓ 015-session-assessment
  ✓ 016-operator-reframing-assessment
  ✓ 017-oi017-reframing-deliberation
  ✓ 018-reference-validation-exercise-1
  ✓ 019-reference-validation-revision
  ✓ 020-workspace-scaling-deliberation
  ✓ 021-oi004-criterion4-articulation
  ✓ 022-workspace-scaling-trajectory
  ✓ 023-session-assessment
  ✓ 024-session-assessment

[6] Session log completeness
  ✓ Session 001 in SESSION-LOG.md
  ✓ Session 002 in SESSION-LOG.md
  ✓ Session 003 in SESSION-LOG.md
  ✓ Session 004 in SESSION-LOG.md
  ✓ Session 005 in SESSION-LOG.md
  ✓ Session 006 in SESSION-LOG.md
  ✓ Session 007 in SESSION-LOG.md
  ✓ Session 008 in SESSION-LOG.md
  ✓ Session 009 in SESSION-LOG.md
  ✓ Session 010 in SESSION-LOG.md
  ✓ Session 011 in SESSION-LOG.md
  ✓ Session 012 in SESSION-LOG.md
  ✓ Session 013 in SESSION-LOG.md
  ✓ Session 014 in SESSION-LOG.md
  ✓ Session 015 in SESSION-LOG.md
  ✓ Session 016 in SESSION-LOG.md
  ✓ Session 017 in SESSION-LOG.md
  ✓ Session 018 in SESSION-LOG.md
  ✓ Session 019 in SESSION-LOG.md
  ✓ Session 020 in SESSION-LOG.md
  ✓ Session 021 in SESSION-LOG.md
  ✓ Session 022 in SESSION-LOG.md
  ✓ Session 023 in SESSION-LOG.md
  ✗ Session 024 missing from SESSION-LOG.md

[7] Provenance directory contents
  ✓ 001-genesis — 3 file(s)
  ✓ 002-self-validation — 4 file(s)
  ✓ 003-multi-agent-deliberation — 9 file(s)
  ✓ 004-participation-mechanisms — 8 file(s)
  ✓ 005-schema-enforcement — 9 file(s)
  ✓ 006-triggers-met-schema — 9 file(s)
  ✓ 007-external-application-examination — 9 file(s)
  ✓ 008-first-external-application — 10 file(s)
  ✓ 009-external-validate-receipt — 10 file(s)
  ✓ 010-household-decision-protocol — 9 file(s)
  ✓ 011-w1-kernel-read-revision — 9 file(s)
  ✓ 012-methodology-naming — 9 file(s)
  ✓ 013-artefact-revision — 10 file(s)
  ✓ 014-oi016-resolution — 9 file(s)
  ✓ 015-session-assessment — 3 file(s)
  ✓ 016-operator-reframing-assessment — 4 file(s)
  ✓ 017-oi017-reframing-deliberation — 10 file(s)
  ✓ 018-reference-validation-exercise-1 — 3 file(s)
  ✓ 019-reference-validation-revision — 9 file(s)
  ✓ 020-workspace-scaling-deliberation — 9 file(s)
  ✓ 021-oi004-criterion4-articulation — 9 file(s)
  ✓ 022-workspace-scaling-trajectory — 12 file(s)
  ✓ 023-session-assessment — 8 file(s)
  ✓ 024-session-assessment — 5 file(s)

[8] Provenance frontmatter
  ✓ 001-genesis/00-survey.md
  ✓ 001-genesis/01-deliberation.md
  ✓ 001-genesis/02-decisions.md
  ✓ 002-self-validation/00-assessment.md
  ✓ 002-self-validation/01-deliberation.md
  ✓ 002-self-validation/02-decisions.md
  ✓ 002-self-validation/03-close.md
  ✓ 003-multi-agent-deliberation/00-assessment.md
  ✓ 003-multi-agent-deliberation/01-deliberation.md
  ✓ 003-multi-agent-deliberation/01a-perspective-methodologist.md
  ✓ 003-multi-agent-deliberation/01b-perspective-pragmatist.md
  ✓ 003-multi-agent-deliberation/01c-perspective-skeptic.md
  ✓ 003-multi-agent-deliberation/01d-perspective-archivist.md
  ✓ 003-multi-agent-deliberation/01e-perspective-futurist.md
  ✓ 003-multi-agent-deliberation/02-decisions.md
  ✓ 003-multi-agent-deliberation/03-close.md
  ✓ 004-participation-mechanisms/00-assessment.md
  ✓ 004-participation-mechanisms/01-brief-shared.md
  ✓ 004-participation-mechanisms/01-deliberation.md
  ✓ 004-participation-mechanisms/01a-perspective-archivist.md
  ✓ 004-participation-mechanisms/01b-perspective-integrator.md
  ✓ 004-participation-mechanisms/01c-perspective-skeptic.md
  ✓ 004-participation-mechanisms/02-decisions.md
  ✓ 004-participation-mechanisms/03-close.md
  ✓ 005-schema-enforcement/00-assessment.md
  ✓ 005-schema-enforcement/01-brief-shared.md
  ✓ 005-schema-enforcement/01-deliberation.md
  ✓ 005-schema-enforcement/01a-perspective-archivist.md
  ✓ 005-schema-enforcement/01b-perspective-implementer.md
  ✓ 005-schema-enforcement/01c-perspective-skeptic.md
  ✓ 005-schema-enforcement/01d-perspective-outsider.md
  ✓ 005-schema-enforcement/02-decisions.md
  ✓ 005-schema-enforcement/03-close.md
  ✓ 006-triggers-met-schema/00-assessment.md
  ✓ 006-triggers-met-schema/01-brief-shared.md
  ✓ 006-triggers-met-schema/01-deliberation.md
  ✓ 006-triggers-met-schema/01a-perspective-archivist.md
  ✓ 006-triggers-met-schema/01b-perspective-implementer.md
  ✓ 006-triggers-met-schema/01c-perspective-skeptic.md
  ✓ 006-triggers-met-schema/01d-perspective-outsider.md
  ✓ 006-triggers-met-schema/02-decisions.md
  ✓ 006-triggers-met-schema/03-close.md
  ✓ 007-external-application-examination/00-assessment.md
  ✓ 007-external-application-examination/01-brief-shared.md
  ✓ 007-external-application-examination/01-deliberation.md
  ✓ 007-external-application-examination/01a-perspective-generalist.md
  ✓ 007-external-application-examination/01b-perspective-steward.md
  ✓ 007-external-application-examination/01c-perspective-skeptic.md
  ✓ 007-external-application-examination/01d-perspective-outsider.md
  ✓ 007-external-application-examination/02-decisions.md
  ✓ 007-external-application-examination/03-close.md
  ✓ 008-first-external-application/00-assessment.md
  ✓ 008-first-external-application/01-brief-shared.md
  ✓ 008-first-external-application/01-deliberation.md
  ✓ 008-first-external-application/01a-perspective-explorer.md
  ✓ 008-first-external-application/01b-perspective-pragmatist.md
  ✓ 008-first-external-application/01c-perspective-skeptic.md
  ✓ 008-first-external-application/01d-perspective-outsider.md
  ✓ 008-first-external-application/02-decisions.md
  ✓ 008-first-external-application/03-close.md
  ✓ 008-first-external-application/artefact-morning-unfurl.md
  ✓ 009-external-validate-receipt/00-assessment.md
  ✓ 009-external-validate-receipt/00-validate-user-report.md
  ✓ 009-external-validate-receipt/01-brief-shared.md
  ✓ 009-external-validate-receipt/01-deliberation.md
  ✓ 009-external-validate-receipt/01a-perspective-reviser.md
  ✓ 009-external-validate-receipt/01b-perspective-minimalist.md
  ✓ 009-external-validate-receipt/01c-perspective-skeptic.md
  ✓ 009-external-validate-receipt/01d-perspective-outsider.md
  ✓ 009-external-validate-receipt/02-decisions.md
  ✓ 009-external-validate-receipt/03-close.md
  ✓ 010-household-decision-protocol/00-assessment.md
  ✓ 010-household-decision-protocol/01-brief-shared.md
  ✓ 010-household-decision-protocol/01-deliberation.md
  ✓ 010-household-decision-protocol/01a-perspective-drafter.md
  ✓ 010-household-decision-protocol/01b-perspective-mediator.md
  ✓ 010-household-decision-protocol/01c-perspective-outsider.md
  ✓ 010-household-decision-protocol/01d-perspective-skeptic.md
  ✓ 010-household-decision-protocol/02-decisions.md
  ✓ 010-household-decision-protocol/03-close.md
  ✓ 011-w1-kernel-read-revision/00-assessment.md
  ✓ 011-w1-kernel-read-revision/01-brief-shared.md
  ✓ 011-w1-kernel-read-revision/01-deliberation.md
  ✓ 011-w1-kernel-read-revision/01a-perspective-reviser.md
  ✓ 011-w1-kernel-read-revision/01b-perspective-minimalist.md
  ✓ 011-w1-kernel-read-revision/01c-perspective-skeptic.md
  ✓ 011-w1-kernel-read-revision/01d-perspective-outsider.md
  ✓ 011-w1-kernel-read-revision/02-decisions.md
  ✓ 011-w1-kernel-read-revision/03-close.md
  ✓ 012-methodology-naming/00-assessment.md
  ✓ 012-methodology-naming/01-brief-shared.md
  ✓ 012-methodology-naming/01-deliberation.md
  ✓ 012-methodology-naming/01a-perspective-namer.md
  ✓ 012-methodology-naming/01b-perspective-steward.md
  ✓ 012-methodology-naming/01c-perspective-skeptic.md
  ✓ 012-methodology-naming/01d-perspective-outsider.md
  ✓ 012-methodology-naming/02-decisions.md
  ✓ 012-methodology-naming/03-close.md
  ✓ 013-artefact-revision/00-assessment.md
  ✓ 013-artefact-revision/00-validate-user-report.md
  ✓ 013-artefact-revision/01-brief-shared.md
  ✓ 013-artefact-revision/01-deliberation.md
  ✓ 013-artefact-revision/01a-perspective-reviser.md
  ✓ 013-artefact-revision/01b-perspective-householder.md
  ✓ 013-artefact-revision/01c-perspective-skeptic.md
  ✓ 013-artefact-revision/01d-perspective-outsider.md
  ✓ 013-artefact-revision/02-decisions.md
  ✓ 013-artefact-revision/03-close.md
  ✓ 014-oi016-resolution/00-assessment.md
  ✓ 014-oi016-resolution/01-brief-shared.md
  ✓ 014-oi016-resolution/01-deliberation.md
  ✓ 014-oi016-resolution/01a-perspective-architect.md
  ✓ 014-oi016-resolution/01b-perspective-operationalist.md
  ✓ 014-oi016-resolution/01c-perspective-skeptic.md
  ✓ 014-oi016-resolution/01d-perspective-outsider.md
  ✓ 014-oi016-resolution/02-decisions.md
  ✓ 014-oi016-resolution/03-close.md
  ✓ 015-session-assessment/00-assessment.md
  ✓ 015-session-assessment/02-decisions.md
  ✓ 015-session-assessment/03-close.md
  ✓ 016-operator-reframing-assessment/00-assessment.md
  ✓ 016-operator-reframing-assessment/00-operator-input.md
  ✓ 016-operator-reframing-assessment/02-decisions.md
  ✓ 016-operator-reframing-assessment/03-close.md
  ✓ 017-oi017-reframing-deliberation/00-assessment.md
  ✓ 017-oi017-reframing-deliberation/00-operator-steering.md
  ✓ 017-oi017-reframing-deliberation/01-brief-shared.md
  ✓ 017-oi017-reframing-deliberation/01-deliberation.md
  ✓ 017-oi017-reframing-deliberation/01a-perspective-architect.md
  ✓ 017-oi017-reframing-deliberation/01b-perspective-operationalist.md
  ✓ 017-oi017-reframing-deliberation/01c-perspective-skeptic.md
  ✓ 017-oi017-reframing-deliberation/01d-perspective-outsider.md
  ✓ 017-oi017-reframing-deliberation/02-decisions.md
  ✓ 017-oi017-reframing-deliberation/03-close.md
  ✓ 018-reference-validation-exercise-1/00-assessment.md
  ✓ 018-reference-validation-exercise-1/02-decisions.md
  ✓ 018-reference-validation-exercise-1/03-close.md
  ✓ 019-reference-validation-revision/00-assessment.md
  ✓ 019-reference-validation-revision/01-brief-shared.md
  ✓ 019-reference-validation-revision/01-deliberation.md
  ✓ 019-reference-validation-revision/01a-perspective-reviser.md
  ✓ 019-reference-validation-revision/01b-perspective-minimalist.md
  ✓ 019-reference-validation-revision/01c-perspective-skeptic.md
  ✓ 019-reference-validation-revision/01d-perspective-outsider.md
  ✓ 019-reference-validation-revision/02-decisions.md
  ✓ 019-reference-validation-revision/03-close.md
  ✓ 020-workspace-scaling-deliberation/00-assessment.md
  ✓ 020-workspace-scaling-deliberation/01-brief-shared.md
  ✓ 020-workspace-scaling-deliberation/01-deliberation.md
  ✓ 020-workspace-scaling-deliberation/01a-perspective-splitter.md
  ✓ 020-workspace-scaling-deliberation/01b-perspective-tooler.md
  ✓ 020-workspace-scaling-deliberation/01c-perspective-skeptic.md
  ✓ 020-workspace-scaling-deliberation/01d-perspective-outsider.md
  ✓ 020-workspace-scaling-deliberation/02-decisions.md
  ✓ 020-workspace-scaling-deliberation/03-close.md
  ✓ 021-oi004-criterion4-articulation/00-assessment.md
  ✓ 021-oi004-criterion4-articulation/01-brief-shared.md
  ✓ 021-oi004-criterion4-articulation/01-deliberation.md
  ✓ 021-oi004-criterion4-articulation/01a-perspective-articulator.md
  ✓ 021-oi004-criterion4-articulation/01b-perspective-skeptic.md
  ✓ 021-oi004-criterion4-articulation/01c-perspective-operationaliser.md
  ✓ 021-oi004-criterion4-articulation/01d-perspective-outsider.md
  ✓ 021-oi004-criterion4-articulation/02-decisions.md
  ✓ 021-oi004-criterion4-articulation/03-close.md
  ✓ 022-workspace-scaling-trajectory/00-assessment.md
  ✓ 022-workspace-scaling-trajectory/01-brief-shared.md
  ✓ 022-workspace-scaling-trajectory/01-deliberation.md
  ✓ 022-workspace-scaling-trajectory/01a-perspective-architect.md
  ✓ 022-workspace-scaling-trajectory/01a-stance-architect.md
  ✓ 022-workspace-scaling-trajectory/01b-perspective-conservator.md
  ✓ 022-workspace-scaling-trajectory/01b-stance-conservator.md
  ✓ 022-workspace-scaling-trajectory/01c-perspective-skeptic.md
  ✓ 022-workspace-scaling-trajectory/01c-stance-skeptic.md
  ✓ 022-workspace-scaling-trajectory/01d-stance-outsider.md
  ✓ 022-workspace-scaling-trajectory/02-decisions.md
  ✓ 022-workspace-scaling-trajectory/03-close.md
  ✓ 023-session-assessment/00-assessment.md
  ✓ 023-session-assessment/01-brief-shared.md
  ✓ 023-session-assessment/01-deliberation.md
  ✓ 023-session-assessment/01a-perspective-calibrator.md
  ✓ 023-session-assessment/01b-perspective-pacer.md
  ✓ 023-session-assessment/01c-perspective-skeptic.md
  ✓ 023-session-assessment/02-decisions.md
  ✓ 023-session-assessment/03-close.md
  ✓ 024-session-assessment/00-assessment.md
  ✓ 024-session-assessment/01-brief-shared.md
  ✓ 024-session-assessment/01a-perspective-splitter.md
  ✓ 024-session-assessment/01b-perspective-archivist.md
  ✓ 024-session-assessment/01c-perspective-skeptic.md

[9] Decision record quality
  ✓ 001-genesis/02-decisions.md — includes rejected alternatives
  ✓ 001-genesis/02-decisions.md — includes rejected alternatives
  ✓ 002-self-validation/02-decisions.md — includes rejected alternatives
  ✓ 002-self-validation/02-decisions.md — includes rejected alternatives
  ✓ 003-multi-agent-deliberation/02-decisions.md — includes rejected alternatives
  ✓ 003-multi-agent-deliberation/02-decisions.md — includ