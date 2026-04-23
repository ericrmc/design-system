---
session: 044
title: Decisions — D-133 adopt minor forward convention M2 Convene-time role/lineage matrix with 3-session verification window S045-S047; D-134 defer substantive MAD v4 (d)-class lineage-constrained-role amendment to S047+ post-verification; D-135 preserve §5.13 Claude-only narrower-scope position as first-class minority (#30); D-136 cross-link OI-019 ↔ S044 (not bundling); D-137 housekeeping (M4 rejection; Cause-4 framing reframed as visibility-checkpoint-observation; WX-44-1 + WX-44-2 + P1 Cause 7 + subagent-self-commit cumulative pattern recorded as forward observations)
date: 2026-04-24
status: decisions-complete
---

# Session 044 Decisions

Five decisions ratifying the §3 synthesis of `01-deliberation.md`. Numbering continues the engine-wide decision register (D-129 through D-132 were at S043; D-133 opens this session).

## D-133: Adopt minor forward convention — M2 Convene-time role/lineage matrix in session-open assessments

**Triggers met:** [d008_2_convention_forward_discipline]

**Triggers rationale:** This decision adopts a forward convention (analog of D-116 Session 036 WX-35-1 file-edit claim discipline; D-129 Session 043 non-Path-A alternatives discipline) at the session-decision-record level, without amending any specification file this session. Per OI-002 heuristic and WX-35-1 Session 036 precedent, this is a minor convention with a verification window preceding any substantive codification.

### Decision text

Starting Session 045, every multi-perspective deliberation's session-open assessment §5 (perspective shape proposal) MUST include a **role/lineage matrix** with one row per convened perspective and at minimum the following columns:

| Role name | Role function (one line) | Participant kind | Provider / model family | MAD v4 trigger satisfied (if any) | Lineage constraint | Function-audit |
|-----------|-------------------------|------------------|------------------------|----------------------------------|-------------------|-----------------|

**Column semantics**:
- **Role name**: the short role name used consistently throughout briefs, raw outputs, synthesis, and decisions (per MAD v4 §Perspectives naming discipline).
- **Role function**: a single sentence naming what the role is supposed to produce/challenge/represent. Forcing function: articulating the role's function at convening time, not only its stance.
- **Participant kind**: per MAD v4 Layer 2 manifest enumeration (claude-subagent / non-anthropic-model / human / anthropic-other / unknown).
- **Provider / model family**: anthropic / openai / google / other-named. For non-Claude participants, **the model_id MUST be verified against the current session's raw-output log or CLI startup metadata, NOT copied from prior-session manifests** (addresses WX-44-2 codex CLI model-version rolling-upgrade observation).
- **MAD v4 trigger satisfied**: which of §When Non-Claude Participation Is Required clauses (1/2/3/4) or §When Multi-Agent Deliberation Is Required clauses this perspective's inclusion satisfies. "n/a" if none.
- **Lineage constraint**: the role's lineage constraint, if any. Currently-established convention: `Outsider = non-Claude`. Other roles: `none` until a future decision adds a lineage-constrained role to the register.
- **Function-audit**: a one-line check of whether this role's function depends on any latent lineage-or-structural property (training lineage, operator relation, synthesis timing, structural position). Synonym-drift guard per P4 residual-gap finding: catches cases where a role not literally named "Outsider" would carry an unstated lineage dependency.

**Departure discipline**: if the proposed perspective shape violates a lineage constraint (e.g., Outsider = Claude), the session-open assessment MUST:
(i) explicitly name the departure as substantive in §5 itself (not in §6 Rejected alternatives);
(ii) state the reason for the proposed departure;
(iii) surface the operator-visible impact of the departure (e.g., "this session would be the first since S005 to assign Outsider to a Claude participant; the 21-for-21 prior non-Claude pattern would be broken; §5.6 implications are ...");
(iv) halt for explicit operator ratification of the departure — default-token ratification IS NOT sufficient for departure-shapes.

**Rename-if-unavailable clause** (per P3 + P4 convergence): if a lineage-constrained role cannot be filled per its constraint (e.g., no non-Claude participant available to serve as Outsider), the assessment MUST either (a) defer the deliberation to a session where the constraint can be satisfied, OR (b) rename the role to a non-constrained analog ("Frame Reviewer", "Adversarial Reviewer", "Internal Frame Challenger") and explicitly not call the role "Outsider". Renaming is recorded in §5 as a substantive shape choice and is subject to the departure discipline's halt-for-ratification clause.

This convention is **standing** (not windowed; once adopted it applies to every multi-perspective deliberation assessment) but it is **minor** per OI-002 — no specification file is amended this session. The convention lives in session decision records until such time as substantive spec-level codification is warranted (candidate: D-134 M3 at S047+ post-verification).

### 3-session verification window

Sessions 045 / 046 / 047 each exercise the convention. Evaluation at **Session 047 close**:

- **Vindication conditions**: (i) at least one session in the window surfaces a lineage-constraint departure or a rename-if-unavailable case and applies the departure discipline cleanly; OR (ii) all three sessions produce role/lineage matrices that add information to the reasoning trail (specifically: matrices that would have caught S043's §5a item 4 had it been applied then, verified by a retrospective check at S047); OR (iii) the convention produces no departures but the matrices are non-vacuous and record concrete per-perspective function articulation.
- **Non-vindication conditions**: (i) one or more sessions omit the matrix entirely without explicit rationale; OR (ii) the matrices become template-filled ceremony without substantive content; OR (iii) a departure occurs without halt-for-ratification discipline applied.

If vindicated at S047 close, the convention continues as standing discipline and D-134 M3 substantive spec amendment becomes priority-active for S047+ deliberation (candidate for engine-v8 bump via MAD v4 + kernel §Convene amendment).

If non-vindicated, the convention is withdrawn, §5.13 first-class minority (D-135) re-escalates, and the question returns to OI-status pending further evidence.

### Why minor not substantive this session (anti-laundering sequencing)

Per MAD v4 §Limitations + the shared brief §7 anti-laundering reminders + P2 + P4 explicit sequencing arguments: substantive spec amendment (MAD v4 + kernel) in the same session that surfaced the motivating lapse is exactly the retrofit pattern MAD warns against. The forward-convention-then-codify-after-evidence pattern (D-116 WX-35-1; D-129 non-Path-A alternatives) is the mature engine sequencing. Synthesis §3.1 argument applies: "disclose now; codify after evidence."

P2's substantive-vs-minor uncertainty is resolved in favor of minor per this sequencing + the 4-of-4 cross-family convergence that convention-level suffices to start (P3: "Convention-level first"; P4: "Convention-level with a three-session verification window is enough initially"; P2: explicitly preferred; P1: did not take a position on classification).

### Rejected alternatives

1. **Adopt M2 as substantive MAD v4 + kernel amendment this session** (engine-v7 → engine-v8 bump). Rejected per anti-laundering sequencing above. P3/P4 both flagged this risk; P2 explicitly recommended deferral.

2. **Lighter shape — only list participant_kind + provider per perspective, no role-function or function-audit columns.** Rejected: the role-function column is what addresses P1 Cause 6 (Outsider-function under-articulation) at the session-open layer, and the function-audit column addresses P4 synonym-drift residual gap. A lighter shape would leave Cause 6 unaddressed.

3. **Adopt only the departure-discipline clause without the full matrix** (narrower mechanism — just the halt-for-explicit-ratification when Claude-as-Outsider is proposed). Rejected: misses P3 and P4 concerns about synonym drift and leaves the role-function under-articulation gap unaddressed. The matrix is the integrated fix; a sub-clause would be partial.

4. **Defer the entire M2 adoption to S047 post-OI-019 progress.** Rejected: operator has declared a position requiring correction "should not recur"; deferring all action to a future session leaves the discipline gap unpatched through S045-S046. M2 convention adoption is the minimum-response to the operator's declared-position constraint.

5. **Codify M2 at the prompt layer (`prompts/development.md` §Convene) rather than as session-decision-record convention.** Rejected: prompt-layer edit is also a form of substantive change this session that fails the same anti-laundering test. The session-decision-record convention is the correct codification level until verification-window evidence accumulates.

## D-134: Defer substantive MAD v4 amendment — M3 (d)-class lineage-constrained-role formulation to S047+ post-verification

**Triggers met:** [d009_1]

**Triggers rationale:** This decision concerns a substantive MAD v4 amendment candidate; deferral is OI-adjacent (OI-019 §5.12 reopen-warrant (b) class of concern about rapid spec change in same session as motivating pattern). The trigger identifier `d009_1` matches OI-019's opening-decision trigger code and signals that this decision's disposition is forward-looking (not a same-session substantive change).

### Decision text

The substantive MAD v4 amendment proposed in `01-deliberation.md` §3.2 (the (d)-class lineage-constrained-role formulation preferred by 3-of-4 cross-family including both non-Claude perspectives) is **not adopted this session**. Adoption is **deferred to Session 047 or later**, pending D-133 M2 verification-window evidence.

**The deferred amendment shape** (per §3.2 of the synthesis, recorded here as the candidate for S047+ deliberation):

> *MAD v4 §Perspectives gains a new sub-section on lineage-constrained roles:*
>
> *"A role is **lineage-constrained** if its function depends on non-overlapping training provenance with the session-host family, not only on stance-independence during the independent phase. The Outsider role, as engine convention, is lineage-constrained: in Claude-hosted deliberations, a perspective named 'Outsider' MUST be non-Claude. If no non-Claude participant is available to fill the Outsider seat, the session MUST (a) defer the deliberation, OR (b) rename the role (e.g., 'Frame Reviewer', 'Adversarial Reviewer', 'Internal Frame Challenger') — NOT call it 'Outsider'. Other roles are not lineage-constrained by default; role designers may add new lineage-constrained roles in future spec amendments."*

This formulation addresses:
- **P1 Cause 6** (Outsider-function implicit articulation): articulates lineage-dependence in the function definition itself.
- **P3 + P4 rename-if-unavailable escape hatch**: preserves operational flexibility when non-Claude is unavailable.
- **P4 synonym-drift concern**: the "lineage-constrained" framing is extensible — new roles may be added to the list if their functions depend on training lineage, structural position, or similar.
- **3-of-4 Q2 broader-scope convergence**: binds the rule to every Outsider-role exercise, not trigger-conditional.

### S047 adoption conditions

At Session 047 close, M3 is eligible for substantive adoption (engine-v7 → engine-v8 bump candidate) if ALL of:
1. D-133 M2 convention is vindicated per its verification conditions.
2. No §5.13 reopen warrant (see D-135) has fired.
3. A deliberation with at least 3-of-4 cross-family convergence (including at least one non-Claude on the prevailing side) ratifies the specific text of the amendment. This would be a substantive-revision session (Path O-S047 or similar).
4. Anti-laundering audit confirms the amendment is evidence-backed (verification-window operational evidence cited) rather than pressure-driven.

If any condition fails at S047 close, adoption defers further or the formulation is revised per accumulated evidence.

### Rejected alternatives

1. **Adopt M3 (d)-class substantive amendment this session**. Rejected per anti-laundering sequencing (same reasoning as D-133 rejection #1). P3's preference for this-session adoption was noted but P2/P4 explicit deferral arguments + MAD v4 §Limitations standing warning prevail.

2. **Adopt M3 (a)-class narrower formulation** ("Outsider MUST be non-Claude when non-Claude participation is required"). Rejected: 3-of-4 cross-family (P1 + P3 + P4) rated this under-scoped; §5.13 preserves this formulation as minority (Q2 P2 position) while the deferred-for-S047+ candidate is the (d)-class.

3. **Adopt M3 (c)-class convene-procedural-only formulation** ("Convene MUST enumerate lineage per perspective and halt if Outsider = Claude without override") as spec-level this session. Rejected: same anti-laundering concern; D-133 M2 already captures the procedural mechanism at convention level.

4. **Skip forward-candidate recording and leave M3 entirely to a future session to re-derive.** Rejected: synthesis §3.2 3-of-4 convergence on the (d)-class formulation is a preservation-worthy artefact; a future session re-deriving risks drift away from this session's cross-family consensus. Recording the candidate here with explicit deferral is the appropriate middle path.

## D-135: Preserve §5.13 first-class minority — P2 narrower-scope trigger-conditional position

**Triggers met:** [d004_3_minority_preservation]

**Triggers rationale:** Per MAD v4 §Synthesis "Preserve dissent" + the engine-wide first-class-minority preservation convention (established across S004+, formalised at multiple subsequent sessions): a perspective that does not prevail and whose position has distinctive operational content is preserved as a first-class §5-series minority in this session's provenance with reopen warrants stated.

### Decision text

Preserve P2's Q2 position — that the operator's declared position ("Claude is not an Outsider") should be scoped to MAD v4 required-trigger deliberations only, not to every multi-perspective deliberation using the Outsider role name — as **§5.13 first-class minority** in this session's provenance.

**§5.13 full text**: see `01-deliberation.md` §5.

**Catalog position**: **30th engine-wide first-class minority** (S043 §5.12 was #29; this is the first minority preservation at S044). Running tally from S043 close: 28 continuing + 1 new (§5.12) = 29 at S043 close; S044 adds §5.13 → **30** at S044 close.

**Operational reopen warrants** (if any fire, §5.13 re-escalates):
- **(a) Deliberation-reclassification pattern**: if over S045-S047 verification window the role/lineage matrix accumulates 3+ deliberation-reclassification moves (sessions re-labelling themselves "non-deliberation" to avoid the broader scope rule), §5.13 re-escalates.
- **(b) Post-M3-adoption evasion**: if the M3 (d)-class formulation is adopted at S047+ but within 6 sessions any deliberation records a "rename to avoid Outsider rule" move that the synthesis at that session judges to be evasion rather than honest operational constraint, §5.13 re-escalates.
- **(c) Operational cost accumulation**: if cost-side evidence accumulates (P2's "forces cross-family convening on sessions where it is not otherwise warranted" concern) at an operationally material level that later sessions cite §5.13 as vindicated, §5.13 re-escalates.

§5.13 is Claude-only (P2 was the only perspective on the narrower-scope side; 3-of-4 cross-family including both non-Claude converged on broader scope). This intra-family minority is preserved specifically because the operator's declared position aligns with the broader-scope side and thus the Claude-family narrower-scope dissent is most at risk of being overlooked in future revisions.

### Rejected alternatives

1. **Do not preserve; record P2's position as absorbed into D-133/D-134 via rename-if-unavailable clause.** Rejected: the rename-if-unavailable clause addresses operational flexibility, not P2's cost-benefit scope argument. P2's concern about "deliberation-reclassification laundering surface" is a distinct operational hypothesis that the rename clause does not test. Preservation is warranted.

2. **Preserve as forward observation rather than first-class minority.** Rejected: P2's position has specific operational content (specific scope scoping; specific cost-benefit argument; specific laundering-surface hypothesis), not just a generic concern. MAD v4 §Synthesis preserves such positions as first-class minorities.

3. **Preserve the position but without operational reopen warrants.** Rejected: preserved minorities without reopen warrants become ceremonial (see §5.2 origin before Session 027 vindication). Operational reopen warrants are what make preservation load-bearing.

## D-136: Cross-link OI-019 ↔ Session 044 (observational data point added; no bundling)

**Triggers met:** [d009_1]

**Triggers rationale:** This decision records Session 044's role-lineage question as an OI-019 observational data point and modifies `open-issues/OI-019.md` §Cross-linkage accordingly. Per MAD v4 anti-laundering discipline + the 4-of-4 cross-family convergence on keep-separate-cross-link from Q6 of the deliberation.

### Decision text

1. **`open-issues/OI-019.md` §Cross-linkage section amended** to add:

> *Session 044 (Path OC, Operator-Corrective): the S043 Outsider role/lineage split that this session responded to is an instance of convene-time-discipline asymmetry adjacent to OI-019's (d) "spec-level enlargement of warrant surface with operator-frame-observation input class" sub-question. Session 044 adopted D-133 M2 Convene-time role/lineage matrix as minor forward convention with S045-S047 verification window, and deferred D-134 M3 substantive MAD v4 lineage-constrained-role amendment to S047+. Any future OI-019 deliberation touching lineage, default-read expansion, or convene-time-discipline MUST engage S044's findings, particularly the 3-of-4 cross-family Q2 broader-scope convergence vs the §5.13 Claude-only narrower-scope minority, and the P4-identified synonym-drift residual gap. This cross-linkage is observational, not bundling — OI-019 retains its independent closure criteria per its §Provisional closure criteria section.*

2. **OI-019 §Session 043+ activation triggers** gains a sub-bullet:

> *Session 044 D-133 M2 verification-window outcome at S047 close: if M2 is vindicated, OI-019 sub-question (d) "spec-level enlargement of warrant surface with operator-frame-observation input class" is closer to resolution (the role/lineage matrix is an operationalisation of convene-time observation); if non-vindicated, OI-019 (d) remains open and §5.12 + §5.13 minority positions both strengthen.*

3. **No new OI opened this session.** Per synthesis §3.5: "A separate new OI is NOT warranted this session because M2 is being adopted; if M2 were deferred or if M3 deferral extends past S047+ without resolution, OI-020 opening would be warranted per P2's M7." This session adopts M2 and defers M3 with a specific S047 evaluation point, so the OI-020-opening condition is not met.

### Rejected alternatives

1. **Open OI-020 "Convene-time role/lineage discipline" as a parallel OI to OI-019.** Rejected: M2 is being adopted this session, meaning the session does not leave the concern unrecorded; OI-020 would be redundant with D-133/D-134 machinery. P2's M7 explicitly scoped OI-020 to the case where M2 and M3 are both deferred past this session; M2 is not deferred, so OI-020 is not warranted.

2. **Bundle OI-019 and this session's question into one joint spec revision at S047+.** Rejected: 4-of-4 cross-family convergence against bundling in Q6; §5.12 reopen-warrant (b) risk explicitly flagged by P4; OI-019's diffuse multi-mechanism nature vs S044's concrete lineage question do not warrant coupling.

3. **Do nothing on OI-019 cross-linkage.** Rejected: 4-of-4 convergence on cross-link-without-bundling IS a positive disposition; leaving OI-019 unmodified would under-respond to the synthesis.

## D-137: Housekeeping — M4 rejection + Cause-4 reframing + forward observations

**Triggers met:** [none]

**Triggers rationale:** Housekeeping decision bundling (a) explicit rejection of operator-seeded M4 mitigation candidate; (b) reframing of operator-seeded Cause 4 as visibility-checkpoint-observation rather than root cause (per Q7 3-of-4 convergence); (c) four forward observations recorded for future-session evaluation without OI promotion this session. Individually each sub-item is non-substantive housekeeping; bundled here for session-close completeness.

### Decision text

**Sub-decision (a) — M4 Multi-family panel default: REJECTED.** Per 4-of-4 cross-family convergence at Q3 M4 rejection. Shape of the rejection: the operator's "multi-family panel discipline as the new default for substantive deliberations" proposal (operator-seeded Mitigation 4) is not adopted as spec-level rule. It stands as operational preference — the operator may request multi-family convening per session, and the Case Steward may propose it when operationally appropriate — but it is not codified as a standing default. Reasons (per 4-of-4 convergence):
- It hardcodes a temporary operational weakness (Gemini's substantive-reasoning capability at this date; per operator R2 disclosure);
- It concentrates non-Claude record on GPT-family (directly against §5.6 warrant (i));
- It conflates three separate issues (Outsider-role integrity; §5.6 GPT-concentration; OI-019 path-selection diversity).

**Sub-decision (b) — Cause 4 reframed.** The operator's session-open agenda named five candidate causes for the S043 role/lineage split. Cause 4 ("operator default-token ratification did not surface the implication") is reframed per 3-of-4 cross-family convergence (P1 + P3 + P4; P2 via "derivative of cause 3") as a **visibility-checkpoint-failure observation**, not as a root cause. This is a refinement of the operator's framing (Q7 partial rejection), not a rejection of the operator's declared position (which is out-of-scope per the brief). The refinement is recorded here so that future sessions' mitigation reasoning does not target the ratification mechanism (i.e., do not propose "make operator review non-token") when the load-bearing causes are upstream (P1 Cause 6; P1 Cause 7; P3 MAD v4 Shape A role-fungibility phrase; P4 affirmative-laundering framing of Cause 3).

**Sub-decision (c) — Forward observations recorded** (not OI-promoted this session):

- **WX-44-1**: P4 independence-phase breach — P4 inadvertently read 120 lines of P3 raw-output log during its file exploration; those lines contained P3 invocation/prompt material only, not P3's substantive response (which begins at log line 1212). Not output-invalidating; convene-time briefing improvement candidate. Forward mitigation: non-Claude perspective prompts should explicitly instruct against reading other perspectives' raw-output logs. Single-session observation; OI-promotion candidate if recurs at S045+.

- **WX-44-2**: codex CLI model-version drift — initial S044 post-perspective commit carried `model_id: gpt-5.4` (pattern-carried-forward from S005-S041 manifests); operator flagged mid-session that codex CLI raw-output log reports `model: gpt-5.5`; post-commit correction applied. Forward mitigation candidate: extend D-133 M2 role/lineage matrix with a "model-version verification" sub-step requiring manifest authors to read the codex CLI startup metadata line of the current session's raw-output log rather than copying from prior manifests. This extension is out-of-scope for D-133 as adopted this session; recorded as WX-44-2 candidate for OI-promotion or D-133-amendment at S047+ if a second occurrence fires.

- **P1 Cause 7 (Case Steward single-agent at session-open; no adversarial voice at convening)**: not directly addressed by D-133 M2 (M2 addresses Cause 6 via function-articulation; Case Steward structural feature remains). Forward observation for S047+ evaluation alongside M2 verification and M3 timing. A full address would require a structural change to how session-open assessments are authored (e.g., pre-assessment peer review, or requiring the assessment itself be multi-perspective in some way); such a change exceeds anything converged on this session.

- **Subagent self-commit cumulative pattern**: P1 (b05ebff) and P2 (3d9998c) both self-committed their raw-output files during their Agent-tool runs; S043 had same pattern in P1 (eb345ae) and P4 Outsider (3f829d3). Cumulative **4-of-6 observations** across S043 + S044 (S043 P2/P3/P5 did not; S044 P3/P4 Codex did not). Meets anti-laundering bar for forward observation promotion if pattern persists to S045+. OI-promotion candidate at S046 close if cumulative n ≥ 6. Mechanism hypothesis: general-purpose Agent tool subagents have autonomous git-commit-and-push capability per CLAUDE.md "commit workflow" instruction and are interpreting the instruction as applicable to their subagent scope; this is not necessarily incorrect but creates a consistency mismatch (Codex perspectives do not have write access so cannot self-commit; Claude subagents and Gemini-CLI behave differently). Not opened as OI this session per anti-laundering (single-pattern observation would be promotion-shaped retrofit after noticing).

### Rejected alternatives

1. **Open WX-44-2 as OI-020** this session. Rejected: single occurrence; anti-laundering bar for OI promotion not met. The M2 (D-133) machinery provides a natural venue for extending model-version verification in a future session; premature OI promotion would force the issue into formal resolution before evidence accumulates.

2. **Promote subagent-self-commit cumulative pattern to OI this session** (at n=4). Rejected: anti-laundering bar is typically met at n≥3 of N observations with N ≥ 6 (per WX-35-1 precedent); cumulative 4-of-6 is borderline but the mechanism is not engine-discipline-relevant (the subagent behavior does not violate engine discipline; it is just an observed behavioral pattern). OI-promotion candidate at n≥6 only if pattern demonstrates engine-impact (e.g., repeated commit-race conditions, or unrecorded edits across self-commits).

3. **Fold Cause-4 reframing into D-134 rather than housekeeping D-137.** Rejected: D-134 is a substantive deferral decision with specific forward semantics; mixing in a framing refinement muddies the D-134 record. Cause-4 reframing is appropriately housekeeping because it does not change any substantive engine state — it clarifies how the operator's framing is recorded without rejecting the declared position.

4. **Separate individual decisions for each of M4 rejection + Cause-4 reframing + four forward observations** (6 separate decisions total this session instead of bundled D-137). Rejected: bundling reduces decision-record noise without loss of auditability; each sub-item has its rationale and cross-linkage recorded within D-137. Precedent: S043 D-132 bundled multiple housekeeping sub-items similarly.

5. **Open WX-44-1 as formal watchpoint (opened-and-monitored) at this session.** Rejected: single-session observation with clear forward mitigation (prompt-layer instruction adjustment at next convening); WX-44-1 can be addressed informally in S045's convening without formal watchpoint machinery. If it recurs at S045 despite prompt adjustment, formal watchpoint opening becomes appropriate at S045 close.
