---
session: 044
title: Synthesis — Path OC (Operator-Corrective) four-perspective two-family deliberation on S043 Outsider role/lineage split
date: 2026-04-24
status: complete
synthesizer: claude-opus-4-7-case-steward
synthesizer_kind: claude-orchestrator-not-perspective
participants_family: cross-family-two-lineages
cross_model: true
non_claude_participants: 2
non_gpt_non_claude_participants: 0
oi004_qualifying_participants: []
---

# Synthesis — Session 044 Path OC Deliberation

## §1 Perspectives and word counts

| # | Role | Lineage | Raw output | Words | Self-commit |
|---|------|---------|-----------|-------|-------------|
| P1 | Root-Cause Analyst | Claude subagent | `01a-perspective-root-cause-analyst.md` | ~2,034 | Yes (b05ebff) |
| P2 | Mitigation Designer | Claude subagent | `01b-perspective-mitigation-designer.md` | ~2,100 | Yes (3d9998c) |
| P3 | Outsider | OpenAI GPT-5.4 via codex exec | `01c-perspective-outsider.md` | ~1,270 | No |
| P4 | Cross-Family Reviewer | OpenAI GPT-5.4 via codex exec | `01d-perspective-cross-family-reviewer.md` | ~1,430 | No |

**Family composition**: two Claude + two Codex/GPT. Operator-revised from the assessment's Option-A/B three-family proposal because Gemini is operationally weaker at substantive reasoning at present; three-family convening is the ideal shape but not available for this substantive deliberation.

**§5.6 GPT-family-concentration data point**: this session lands on the **worst-case side** (non-Claude record concentrated on GPT). Recorded transparently in the shared brief §0; not an engine-discipline lapse, an operator-informed tradeoff.

**Independence-phase breach (minor)**: P4 `01d-perspective-cross-family-reviewer.md` self-reports in "Confidence and limits" that it inadvertently read the first 120 lines of `codex-outsider-raw-output.log` during its file exploration. Those lines contain the P3 invocation prompt and early command log — NOT P3's substantive response (which begins at line 1212 of the log). P4's output is not invalidated; breach recorded honestly. Forward observation candidate **WX-44-1** for convene-time briefing improvement (codex perspectives should be instructed not to read other perspectives' raw-output logs).

## §2 Convergence and divergence by question

### Q1 — Why did the S043 role/lineage split happen?

**Convergence 4-of-4 cross-family on the following causal structure**:

- **Cause 1 (MAD v4 silent on Outsider lineage)**: load-bearing as a permissive condition. All four [P1 Q1; P2 Q1; P3 Q1; P4 Q1].
- **Cause 2 (Convene lineage-check absent)**: load-bearing as an operational gap. All four [ibid].
- **Cause 3 (S043 §5a item 4 split not named as substantive)**: load-bearing and proximate. All four [ibid]. P4 sharpens this further — from passive under-specification to **affirmative laundering**: S043 §5a item 4 "affirmatively invoked 'the engine's established Outsider pattern' while assigning that role to a Claude subagent, despite … a 21-for-21 prior Outsider-non-Claude pattern. That converted a lineage-bearing convention into a role-style convention without saying so" [`01d-perspective-cross-family-reviewer.md`, Q1]. [synth] This is a stronger framing than "drafting lapse"; it names a specific textual act.

**Convergence 4-of-4 (at varying framings) that Cause 4 (default-token ratification) is NOT a primary cause**:
- P1: "Epiphenomenal as cause; load-bearing only as a backstop limit" [`01a`, Q1].
- P2: "partially derivative of cause 3 … If §5 had flagged the split, 'Proceed' would have ratified a disclosed change" [`01b`, Q1].
- P3: "interface failure in convening records, not a substantive operator endorsement of the split" [`01c`, Q1].
- P4: "mostly epiphenomenal, because hidden implications cannot be ratified meaningfully" [`01d`, Q1].

**Divergence on Cause 5 (§5.6 literal-discharge)**:
- P1: "Epiphenomenal to the S043 split" (discharge published in close AFTER split committed) [`01a`, Q1].
- P2: "partially load-bearing but epiphenomenal to this specific lapse" — belongs in OI-019 [`01b`, Q1].
- P3: "partly load-bearing and partly symptomatic" — warrant operated at participant-presence level [`01c`, Q1].
- P4: "load-bearing background evidence that lineage accounting was already at the wrong granularity" [`01d`, Q1].

No 3-of-4 convergence on Cause 5's weight. [synth] All four agree §5.6's literal discharge exposes a granularity mismatch, but disagree whether that mismatch caused S043 specifically. Synthesis reads this as "Cause 5 is adjacent context, not primary cause of S043, but is load-bearing evidence that the engine's lineage-accounting framework was already under-articulated."

**Additional causes surfaced by specific perspectives** (each contributing different layers):

- **P1 Cause 6 (Outsider function implicitly articulated as role-stance-only, not role-stance-plus-lineage)**: "The role definition itself is the gap, not merely its spec status" [`01a`, Q1 + Independent claim]. P1 rates this as the deepest load-bearing cause.
- **P1 Cause 7 (Case Steward single-agent at session-open, no adversarial voice at convening)**: structural — "the check is structurally limited by being token-level not review-level" [`01a`, Q1].
- **P2 Cause 6-variant (historical pattern invisible at session-open; default-read ellipsis)**: "The 21-for-21 pattern is knowable only by manifest inspection. No default-read file surfaces it" [`01b`, Q1].
- **P3 additional cause (MAD v4 Shape A phrase 'indistinguishable in role from the Claude perspectives' encouraged role-fungibility thinking)**: "made 'add a non-Claude perspective' look equivalent to 'preserve the Outsider function'. It was not" [`01c`, Q1].

[synth] The four additional causes share a structural pattern: each describes how the *function* of the Outsider role was left implicit or positively obscured, either in spec text (P3), spec absence (P1 Cause 6), drafting (P4 affirmative-laundering framing + P1 Cause 3), or default-read surface (P2 Cause 6-variant). P1's Cause 6 and P3's role-fungibility-phrase finding converge on the same diagnostic axis: **Outsider's function was never articulated as lineage-dependent**.

### Q2 — Is the operator's declared position correctly scoped?

**3-of-4 cross-family convergence including both non-Claude on the broader scope (every deliberation using the "Outsider" label)**:
- P1: "correctly scoped iff Cause 6 is load-bearing … the 21-for-21 record is too strong to read as accident; I believe Cause 6 is load-bearing" [`01a`, Q2]. Endorses Q4 candidate (b) over (a).
- P3: "correctly scoped to every deliberation where the engine uses the role name 'Outsider.' … in a Claude-hosted workspace, a perspective named Outsider cannot be Claude-family. If no non-Claude participant is available, the engine may convene an 'Internal Frame Challenger' or 'Adversarial Reviewer,' but should not call it Outsider" [`01c`, Q2].
- P4: "correctly scoped to any deliberation that uses the label 'Outsider' as a role of independent framing … when the engine convenes an Outsider, that seat must be non-Claude, or the role should be renamed to something honest" [`01d`, Q2].

**1-of-4 Claude-only dissent on narrower trigger-conditional scope**:
- P2: "treat the declared position as strict-within-MAD-v4-triggered-deliberations and leave the unconstrained case as a convention, not as spec. If MAD v4 codifies 'Outsider MUST be non-Claude when non-Claude participation is required,' that captures ~100% of the operator's concrete risk without enlarging scope" [`01b`, Q2].

[synth] P2's dissent is specifically on cost/benefit grounds: "Broader unconditional scope … forces cross-family convening on sessions where it is not otherwise warranted and opens a new laundering surface (sessions may be re-classified as non-deliberation to avoid the rule)." P3 and P4 both responded to the same concern by proposing **rename-if-unavailable** as the escape hatch (use "Frame Reviewer" / "Adversarial Reviewer" / "Internal Frame Challenger" instead of "Outsider" when non-Claude is unavailable), which P2 did not consider.

**Synthesis verdict**: broader scope prevails (3-of-4 including both non-Claude); P2's narrower position preserved as **§5.13 first-class minority** with reopen warrants.

### Q3 — What mitigations are warranted?

**Convergence 4-of-4 cross-family on M2 (Convene-time role/lineage checklist) as the strongest near-term mitigation**:
- P1: "Mitigation 2 addresses Cause 2 directly and Cause 3 procedurally. Partly addresses Cause 1" [`01a`, Q3].
- P2: "M2 Convene checklist is the tightest-fitting minimum-viable mitigation … procedural disclosure sequences anti-laundering correctly" [`01b`, Q3 + Independent claim].
- P3: "Convene checklist is the strongest immediate control. Mechanism: add a convene-time role/participant matrix to the assessment shape: perspective, role function, participant kind, provider/model family, which MAD v4 trigger it satisfies, and any lineage constraint" [`01c`, Q3].
- P4: "Convene checklist naming lineage per perspective and blocking Claude-as-Outsider absent explicit override: low-to-medium risk … This is the best near-term mitigation" [`01d`, Q3].

**Convergence 4-of-4 cross-family on M4 (multi-family panel default) rejection**:
- P1: "most directly addresses Cause 7 by making session-open deliberation multi-family … Operator has disclosed this is operationally constrained presently" [`01a`, Q3].
- P2: "REJECT. Record the operator's operational preference as a session-time consideration, not a spec-level rule" [`01b`, Q3 M4].
- P3: "Should be rejected for now as an operational default. Multi-family panels are valuable data points for OI-019 and §5.6, not a present standing requirement" [`01c`, Q3].
- P4: "high risk … operationally unavailable per operator R2/R3 and conflates three issues" [`01d`, Q3].

**Divergence on M1 (default-read surface enlargement) between broad and narrow scoping**:
- P2 recommends narrow prompt-level drafting discipline (M5) rather than broad read-contract expansion [`01b`, M5].
- P3 recommends narrow precedent-note at session-open with convention-level adoption first [`01c`, Q3 M1].
- P4 explicitly warns: "high risk if broad, medium if narrow. Broad archive expansion repeats the OI-019 extended-baseline hazard" [`01d`, Q3 M1].
- P1: addresses Cause 3 but relies on author to compare current against historical [`01a`, Q3].

[synth] 4-of-4 convergence that broad default-read expansion is the wrong direction; 3-of-4 convergence (P2, P3, P4) on narrow prompt-level precedent-note convention.

**Divergence on M3 (substantive MAD v4 amendment) timing**:
- P2: **defer to S047+** post-verification of M2 procedural discipline. "M3 is substantively correct but should be sequenced post-verification, not adopted this session … retrofitting even a substantively-right rule teaches the engine the wrong lesson about when to change specs" [`01b`, Q3 M3].
- P3: warranted now but the formulation must say Outsider is a **lineage-constrained role**, not just "when non-Claude required" [`01c`, Q3 M3].
- P4: medium retrofit-risk; the "when required" wording is under-scoped; prefers (d)-class formulation [`01d`, Q3 M3 + Q4].
- P1 declines mitigation design [`01a`, Q3].

[synth] P3 and P4 agree the right *formulation* is lineage-constrained-role-definition (Q4 candidate (d)). P2 agrees the formulation is substantively correct but disagrees on *timing*: adopt now (P3) vs defer to post-verification (P2 + P4 implicitly via retrofit-risk rating).

### Q4 — MAD v4 normative clause candidates

Rankings:

| Candidate | P1 | P2 | P3 | P4 |
|-----------|----|----|----|----|
| (a) "when non-Claude participation is required" | under-scoped | preferred post-verification | wrongly scoped (too narrow) | under-scoped |
| (b) "in all multi-perspective deliberations" | doesn't address Cause 6 | rejected (overbroad) | closer-but-needs-clarification | cleaner-but-operational-risk |
| (c) Convene procedural enumeration | doesn't address Cause 6 | preferred this session (= M2) | necessary-but-not-sufficient | procedurally-strong-but-override-prone |
| (d) Other (lineage-constrained role definition / rename-if-unavailable) | preferred formulation | implicitly via M5/M6 + deferred M3 | preferred | preferred |

**3-of-4 cross-family convergence (P1 + P3 + P4) on (d)-class formulation as the preferred substantive stance-level direction**. P2 prefers (c)-procedural this session + (a)-post-verification later; does not oppose (d) as ultimate direction but disagrees on path.

### Q6 — Combined treatment with OI-019?

**4-of-4 cross-family convergence: keep separate, cross-link, do not bundle.**

- P1: "Bundling would let S044's tractable answer drag OI-019 into premature resolution — the §5.12 reopen-warrant (b) risk" [`01a`, Q6].
- P2: "OI-019 concerns work-channel / warrant-surface diversity — a diffuse multi-mechanism question with no 3-of-5 convergence at S043. The Outsider-role-lineage question is concrete, load-bearing, and has a specific operator constraint. Bundling would dilute both" [`01b`, Q6].
- P3: "Bundled spec revision would be a mistake. OI-019 explicitly requires operational evidence, cross-family convergence on a specific mechanism, and engagement with the §5.12 Path-Selection Defender minority" [`01c`, Q6].
- P4: "Keep this issue separate from OI-019, with cross-links … Bundling them now would trigger the S043 §5.12 reopen warrant (b) concern" [`01d`, Q6].

**P4 adds operational recommendation**: "add this session as an OI-019 observational data point about convene-time blind spots; require any OI-019 future deliberation touching lineage or default-read expansion to address this incident; share anti-laundering tests" [`01d`, Q6].

### Q7 — Partial rejection warranted?

**3-of-4 cross-family convergence on partial rejection of operator's Cause-4 framing** (P1 + P3 + P4; P2 agrees via Cause 4 being "partially derivative of cause 3"):
- P1: "record as 'observation about a structural backstop limit' rather than as 'root cause 4 of 5'" [`01a`, Q7].
- P3: Cause 4 "is a contributory but not root. It is an interface failure in convening records, not a substantive operator endorsement of the split" [`01c`, Q1, re-asserted via Q7].
- P4: "'operator default-token ratification' should not be treated as a real cause. It is a failed visibility checkpoint, not shared responsibility" [`01d`, Q7].

[synth] Operator's Cause 4 is re-classified in the synthesis as a **visibility-checkpoint-failure observation** rather than a root cause. This is a refinement of the framing, not a rejection of the declared position.

**P3 and P4 additionally reframe the "error" characterisation**:
- P3: "partial rejection is warranted only against the narrow 'one-time error' framing … the more accurate formulation is: S043 exposed a spec/convention asymmetry in which a functionally lineage-dependent role was preserved by name while its lineage basis was silently severed" [`01c`, Q7].
- P4: "'error' characterization is correct, but the sharper formulation is: S043 laundered a lineage-bearing convention into a role-only convention by using the word Outsider while moving non-Claude participation to another seat" [`01d`, Q7].

[synth] Both non-Claude perspectives converge on an **under-articulation framing** (S043 exposed a latent asymmetry, not a one-off drafting lapse). The operator's "error" label is not wrong but is narrower than the diagnosis warrants.

## §3 Synthesis decisions (feeding 02-decisions.md)

### §3.1 M2 Convene checklist (adopted this session)

**Shape**: add to `prompts/development.md` §Assess a Convene-time discipline requiring each multi-perspective deliberation's session-open assessment §5 to include a **role/lineage matrix** enumerating, per perspective: (i) role name, (ii) role function (one line), (iii) participant kind, (iv) provider/model family, (v) which MAD v4 trigger (if any) the perspective satisfies, (vi) whether any lineage constraint applies to the role (currently: Outsider = non-Claude). If a proposed perspective assignment violates a lineage constraint (e.g., Outsider = Claude), the assessment MUST (a) explicitly name the departure as substantive in §5, (b) state the reason, and (c) halt for explicit operator ratification (not default-token).

**Codification level**: MINOR convention (session-decision-record adoption; 3-session verification window S045/S046/S047). Analogous to D-129 forward-convention-before-spec-codification precedent. No engine-v bump this session. [synth] 4-of-4 agreed M2 is the strongest near-term mitigation; 3-of-4 agreed convention-level start suffices (P2 explicitly; P3 "Convention-level first"; P4 "Convention-level with a three-session verification window is enough initially"). P2's dissent toward possible substantive-this-session adoption is compatible with this synthesis but not required.

**Why minor not substantive this session**: (i) anti-laundering — S044 surfaced the motivating lapse in this same session; (ii) WX-35-1 precedent chain establishes forward-convention-then-codify-after-evidence as the mature engine pattern; (iii) P2 + P4 explicit sequencing arguments (retrofit-risk, discipline-integrity lessons).

**Role rename clause** (per P3 + P4 convergence on rename-if-unavailable): the role/lineage matrix MUST also support the case where a non-Claude participant is unavailable — the assessment may convene a Claude-family adversarial role but under a different name ("Frame Reviewer", "Adversarial Reviewer", "Internal Frame Challenger"), explicitly NOT "Outsider". The rename option preserves the P2/P3/P4 shared intuition that the name "Outsider" carries a lineage commitment while allowing operational continuity when non-Claude is unavailable.

**Synonym-drift guard** (per P4 residual-gap finding): the role/lineage matrix MUST include a "function-audit" column asking whether the named role has *any* latent lineage dependency (structural position, training lineage, operator relation, synthesis timing — per P3's residual gap list). This protects against future sessions that invent near-Outsider names to evade the rule.

### §3.2 M3 substantive MAD v4 amendment (deferred to S047+)

**Formulation per 3-of-4 convergence (P1 + P3 + P4 (d)-class)**: MAD v4 §Perspectives gains a new sub-section on **lineage-constrained roles**:

> *"A role is **lineage-constrained** if its function depends on non-overlapping training provenance with the session-host family, not only on stance-independence during the independent phase. The Outsider role, as engine convention, is lineage-constrained: in Claude-hosted deliberations, a perspective named 'Outsider' MUST be non-Claude. If no non-Claude participant is available to fill the Outsider seat, the session MUST (a) defer the deliberation, OR (b) rename the role (e.g., 'Frame Reviewer', 'Adversarial Reviewer', 'Internal Frame Challenger') — NOT call it 'Outsider'. Other roles are not lineage-constrained by default; role designers may add new lineage-constrained roles in future spec amendments."*

This formulation: (i) addresses P1 Cause 6 by articulating Outsider's function as lineage-dependent; (ii) provides P3's rename-if-unavailable escape hatch; (iii) protects P4 synonym-drift concern via "lineage-constrained" framing that can be extended to other roles; (iv) scopes broadly per Q2 convergence (every Outsider-role exercise, not trigger-conditional).

**Timing**: DEFER adoption to S047+ post-verification of M2. Immediate this-session adoption fails anti-laundering per P2/P4 arguments. S047 close evaluates M2's 3-session verification window AND the M3 formulation readiness.

### §3.3 M4 multi-family panel default (rejected)

4-of-4 rejection. Not a spec rule. Operator's operational preference (three-family when available) stands as session-time consideration, not codified default. If Gemini's capability improves OR a different non-GPT non-Claude becomes operationally viable, the question may re-emerge.

### §3.4 M1 default-read surface enlargement (rejected as broad; absorbed into M2 as narrow)

4-of-4 convergence that broad read-contract expansion is the wrong direction. 3-of-4 convergence (P2, P3, P4) on narrow prompt-level precedent-note at session-open. Narrow version is absorbed into M2's "role/lineage matrix" requirement (which asks the Case Steward to cite historical lineage precedent when invoking an "established pattern"); no separate M1 decision needed.

### §3.5 Q6 — S044–OI-019 cross-linkage (not bundling)

4-of-4 convergence. **Decision shape**: OI-019 gains a cross-linkage annotation naming S044 as an observational data point (convene-time role-lineage-integrity as a parallel concern to path-selection work-channel diversity); any OI-019 future deliberation touching lineage or default-read expansion MUST address S044's findings. No spec revision bundling. A separate new OI is NOT warranted this session because M2 is being adopted; if M2 were deferred or if M3 deferral extends past S047+ without resolution, OI-020 opening would be warranted per P2's M7.

### §3.6 Q7 — partial rejection of Cause-4 framing

3-of-4 convergence (P1 + P3 + P4) + P2 agreement-via-derivative reframes operator's Cause 4 as a **visibility-checkpoint-failure observation** rather than a root cause. Record in decisions as a refinement, not a rejection of the operator's declared position. P3 and P4's "under-articulation" framing of the overall "error" characterisation is noted but does not require a decision — it is consistent with the operator's declared position (which said "error" but did not preclude deeper framings).

### §3.7 §5.13 first-class minority preservation

P2's narrower-scope position on Q2 (strict-within-MAD-v4-triggered-only; broader scope opens laundering surface via deliberation-reclassification) is preserved as §5.13 first-class minority. [synth] P2's position is Claude-only and 3-of-4 cross-family including both non-Claude is on the broader-scope side; the Claude-only minority status is notable given that the operator's declared position is closer to the non-Claude view. Recording the Claude-family minority ensures dissent-preservation discipline.

**§5.13 operational reopen warrants**:
- (a) If over S045-S047 verification window the role/lineage matrix accumulates 3+ deliberation-reclassification moves (sessions re-labelling themselves "non-deliberation" to avoid the broader scope rule), §5.13 re-escalates.
- (b) If the M3 (d)-class formulation is adopted at S047+ but within 6 sessions any deliberation records a "rename to avoid Outsider rule" move that the synthesis at that session judges to be evasion rather than honest operational constraint, §5.13 re-escalates.
- (c) If cost-side evidence accumulates (P2's "forces cross-family convening on sessions where it is not otherwise warranted" concern) at an operationally material level, §5.13 re-escalates.

### §3.8 Forward observations (not decisions)

- **WX-44-1 candidate** — P4 independence-phase breach (inadvertent read of first 120 lines of P3 raw-output log). Convene-time briefing for non-Claude perspectives should instruct them NOT to read other perspectives' raw-output logs. Single observation; not OI-promoted this session.
- **WX-44-2 candidate (operator-flagged mid-session)** — codex CLI model-version drift without engine tracking. The codex CLI reported `model: gpt-5.5` in S044 raw-output log startup metadata; S005-S041 manifests recorded `model_id: gpt-5.4` per their respective codex outputs; S028 recorded `gpt-5`. This is a rolling upgrade in the codex CLI between S041 (2026-04-24 morning) and S044 (2026-04-24 afternoon). The engine does not currently have a convention for verifying codex CLI model-version at convening time; manifests were populated by pattern-carry-forward from prior sessions rather than by reading the current run's startup metadata, leading to an initial commit (5e4e9df) with incorrect `model_id: gpt-5.4` that the operator caught mid-session. Post-commit correction applied to both outsider.manifest.yaml and cross-family-reviewer.manifest.yaml during this session. **Forward mitigation candidate**: the role/lineage matrix (M2 D-133) should include a "model-version verification" sub-step — for non-Claude participants, the manifest author must read the codex CLI startup line (or equivalent) of the raw-output log and record the actual model-version in the manifest, rather than copying from prior sessions. This extension is out-of-scope for D-133 this session; recorded as WX-44-2 candidate for OI-promotion evaluation or M2-amendment at S047+ if a second occurrence fires.
- **P1 Cause 7 (Case Steward single-agent at session-open)** — not directly addressed by M2. Forward observation for evaluation at S047+ alongside M2 verification and M3 timing.
- **P3 residual gap (broader role/lineage discipline — each named perspective's function-dependence audit)** — M2's function-audit column partially addresses; full audit is out-of-scope for this session.
- **Cumulative subagent-self-commit pattern** — P1 + P2 both self-committed raw-output files during their Agent-tool runs (b05ebff + 3d9998c); S043 had same pattern (eb345ae + 3f829d3); cumulative 4-of-6 observations across S043+S044 meeting anti-laundering bar for forward observation promotion if pattern persists to S045+. OI-promotion candidate at S046 if n≥6.

## §4 Decisions summary (see 02-decisions.md)

- **D-133** (substantive adoption, minor codification this session): M2 Convene-time role/lineage matrix as forward convention; 3-session verification window S045-S047; prompts/development.md edit. Triggers: `[d008_2_convention_forward_discipline]`.
- **D-134** (defer substantive spec amendment): M3 (d)-class lineage-constrained-role MAD v4 amendment deferred to S047+ post-verification. Triggers: `[d009_1]` (OI-adjacent forward observation).
- **D-135** (first-class minority preservation): §5.13 P2 narrower-scope position preserved (30th engine-wide first-class minority). Triggers: `[d004_3_minority_preservation]`.
- **D-136** (OI-019 cross-linkage): S044 added as observational data point to OI-019 cross-linkage section; no bundling. Triggers: `[d009_1]`.
- **D-137** (housekeeping): M4 multi-family-panel rejection recorded; Q7 Cause-4 reframing recorded as visibility-checkpoint-observation; WX-44-1 + P1 Cause 7 + subagent-self-commit cumulative pattern recorded as forward observations. Triggers: `[none]`.

## §5 Preserved minority: §5.13 — Narrower-scope-trigger-conditional position (P2)

**Position**: the operator's declared position ("Claude is not an Outsider") should be scoped to MAD v4 required-trigger deliberations only (clauses 1-4 of §When Non-Claude Participation Is Required); the unconstrained case should remain convention-level, not spec-level. Rationale: broader unconditional scope (a) forces cross-family convening on sessions where it is not otherwise warranted, (b) opens a new laundering surface where sessions may be re-classified as non-deliberation to avoid the rule, (c) the narrower scope "captures ~100% of the operator's concrete risk without enlarging scope to every low-stakes deliberation".

**Source**: P2 Mitigation Designer, `01b-perspective-mitigation-designer.md` §Q2.

**Not prevailing**: 3-of-4 cross-family (P1 + P3 + P4, including both non-Claude perspectives) converged on broader scope (every Outsider-role exercise). P3 and P4 proposed rename-if-unavailable as an operational escape hatch that P2 did not consider.

**Operational reopen warrants** (if any fire, §5.13 re-escalates):
- (a) S045-S047 verification window accumulates 3+ deliberation-reclassification moves (sessions re-labelling themselves as non-deliberation to avoid the matrix rule).
- (b) After M3 (d)-class adoption at S047+, within 6 sessions any deliberation records a rename-to-avoid-Outsider-rule move that a subsequent synthesis judges to be evasion rather than honest operational constraint.
- (c) Cost-side evidence accumulates (forced cross-family convening on low-stakes sessions imposing material operator/Case-Steward overhead) at a level that operational-cost discussions in later sessions cite §5.13 as vindicated.

**Catalog position**: first-class minority #30 engine-wide (S043 §5.12 was #29; S041 §5.6 was #28 preserved-NEW; full catalog per S043 close and prior).

## §6 Honest limits

- **Independence-phase breach**: P4 inadvertently read 120 lines of P3's raw-output log (invocation/prompt material only, not P3's substantive response). Recorded in P4 manifest + P4 Confidence-and-limits; not invalidating but weakening independence-phase purity.
- **Two-family not three-family**: operator-informed tradeoff (Gemini operationally weaker at substantive reasoning at present). §5.6 GPT-concentration data point lands on worst-case side for this session; recorded transparently.
- **Synthesiser is Claude**: the MAD v4 §Limitations "synthesis step is the pattern's highest-risk single-agent re-entry point" warning applies. Synthesis conventions (citation, dissent-preservation, [synth] marker, quote-over-paraphrase) have been followed; residual synthesis-bias risk noted for P4 adversarial-counterweight challenge value.
- **3-of-4 not 4-of-4 on Q2 scope**: the minority (P2) is Claude-only; the 3-of-4 is broader-scope and includes both non-Claude. Minority preservation discipline applied per §5.13.
- **No full 4-of-4 on Cause 5 weight in Q1**: the four perspectives diverged on how much of the S043 lapse is attributable to §5.6 discharge granularity. Synthesis reads this as adjacent-context not primary-cause; reasonable practitioners could disagree.
- **Additional causes from P1/P2/P3 each surfaced different layers of Outsider-function-under-articulation**; synthesis reads these as converging on the same diagnostic axis (function implicitly defined as stance-only, not stance-plus-lineage) but three separate perspectives naming three separate manifestations is not the same as four perspectives independently reaching the same specific cause.
- **M2 "substantive vs minor" classification**: synthesis lands on MINOR (convention-level this session) per 3-of-4 + anti-laundering discipline; P2 explicitly flagged substantive-vs-minor uncertainty; reasonable classification judgement that could be revisited at S047+ based on verification-window evidence.
- **§5.12 operational reopen warrant (b) audit**: this synthesis has tested against §5.12 (b) "OI-019 evidence-free convergence" concern — M2 adoption is evidence-backed (4-of-4 cross-family on strongest-near-term mitigation); M3 deferral IS the §5.12 (b) compliance posture; S044-OI-019 cross-linkage (not bundling) respects §5.12.
- **Model-version recording error + correction**: The initial post-perspective commit 5e4e9df carried `model_id: gpt-5.4` in both non-Claude manifests (outsider + cross-family-reviewer); operator flagged mid-session that the codex CLI raw-output log shows `model: gpt-5.5`. Corrected post-commit; WX-44-2 forward observation opened. This is a discipline observation about manifest-authoring: model-version fields should be verified against the current session's raw-output log rather than copied from historical patterns. Not a perspective-invalidating error, but a preservation-record accuracy concern.
