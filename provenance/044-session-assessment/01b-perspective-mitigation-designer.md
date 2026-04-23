---
session: 044
title: Perspective 2 (Mitigation Designer) raw output — Claude subagent; top-ranked mitigation M2 Convene-checklist amendment (spec-level candidate, minor-convention-first with 3-session verification); defer M3 stance-level MUST-be-non-Claude to S047+; reject M4 multi-family-panel-as-default; add M5+M6 prompt-level drafting + ratification discipline as minor conventions; keep separate from OI-019 via M7 cross-link annotation
date: 2026-04-24
status: perspective-raw-output
perspective: Mitigation Designer
perspective_index: 2
lineage: claude
---

# Perspective 2: Mitigation Designer

## Reading performed

- `provenance/044-session-assessment/01-brief-shared.md` — §1, §2, §3, §4, §5b, §6, §7, §8 (per role instruction; §5a, §5c, §5d not read during independent phase).
- `provenance/044-session-assessment/00-assessment.md` — §2 operator agenda verbatim; §3 factual checks including 21-for-21 historical Outsider-non-Claude pattern; §5 proposed shape; §7 D-129 first exercise.
- `provenance/043-session-assessment/00-assessment.md` — §5 object-of-analysis (§5a item 4 "established Outsider pattern … Claude subagent").
- `provenance/043-session-assessment/01-deliberation.md` — S043 synthesis (§5.12 preservation, Q1–Q7 convergence map).
- `provenance/043-session-assessment/participants.yaml`.
- `provenance/043-session-assessment/manifests/outsider.manifest.yaml` — the committed artefact: Claude subagent as Outsider.
- `provenance/043-session-assessment/manifests/non-claude.manifest.yaml` — Gemini as separate P5.
- `specifications/multi-agent-deliberation.md` v4 — §When Multi-Agent Deliberation Is Required, §When Non-Claude Participation Is Required, §Perspectives, §Heterogeneous-Participant Recording Schema, §Limitations, §Closure Procedure for OI-004.
- `specifications/methodology-kernel.md` v6 §3 Convene (the one-paragraph text that governs perspective assembly).
- `specifications/engine-manifest.md` §5 bump-trigger criteria.
- `specifications/read-contract.md` v4 §1 default-read enumeration.
- `open-issues/OI-019.md` — problem statement and sub-questions (a)–(f).

## Q1 — Why did the S043 role/lineage split happen?

My mitigation-design lens treats Q1 causally only enough to target fixes. Four of the operator's five seeds look load-bearing; one is weaker than it appears; and one additional cause is missing that matters for mitigation choice.

- **Cause 1 — MAD v4 silent on Outsider lineage: load-bearing.** Verified by §3c of this session's assessment. No normative clause exists. A mitigation must either add one or build a procedural substitute.
- **Cause 2 — Convene has no lineage-check: load-bearing.** Kernel §3 Convene is one paragraph and names neither lineage nor a role roster. A mitigation targeted here is cheap and does not require spec-revision.
- **Cause 3 — S043 §5 did not name the split as substantive: load-bearing, AND this is where the Case Steward role is structurally implicated.** §5a item 4 cited "established Outsider pattern (Sessions 017/022/028/036/041)" — the cited pattern's defining feature was lineage, not role, but the assessment author fused them. A mitigation that only targets MAD-text misses the drafting-level lapse.
- **Cause 4 — default-token ratification did not surface the implication: load-bearing but partially derivative of cause 3.** If §5 had flagged the split, "Proceed" would have ratified a disclosed change; because §5 did not, "Proceed" ratified an invisible one. Mitigation at the §5-drafting layer also substantially addresses this cause.
- **Cause 5 — §5.6 literal-discharge on participant-presence not Outsider-specifically: partially load-bearing but epiphenomenal to this specific lapse.** §5.6's warrant text never mentioned the Outsider role; it was written against a 21-for-21 empirical backdrop that made the Outsider's lineage a silent assumption. This is a general cause (warrants can be written against unstated structural presumptions); it did not itself cause S043. A mitigation here belongs in OI-019 (sub-question (d)-adjacent), not in this session's decisions.
- **Additional cause 6 — historical pattern invisible at session-open (default-read ellipsis).** The 21-for-21 pattern is knowable only by manifest inspection. No default-read file surfaces it. A Case Steward writing §5 in-session with §2c-window closes (most recent six) in default-read has to proactively archive-inspect to see the precedent; if they don't, the pattern does not enter framing. This matters for mitigation #1 design.

## Q2 — Is the operator's declared position correctly scoped?

Mitigation-design answer: **treat the declared position as strict-within-MAD-v4-triggered-deliberations and leave the unconstrained case as a convention, not as spec.** If MAD v4 codifies "Outsider MUST be non-Claude when non-Claude participation is required," that captures ~100% of the operator's concrete risk without enlarging scope to every low-stakes deliberation. Broader unconditional scope ("Outsider MUST be non-Claude in all multi-perspective deliberations") has worse cost/benefit: it forces cross-family convening on sessions where it is not otherwise warranted and opens a new laundering surface (sessions may be re-classified as non-deliberation to avoid the rule). This scope judgement shapes the mitigation set below.

## Q3 — What mitigations are warranted?

I evaluate the four operator-named mitigations plus three I am adding (5, 6, 7). Each is rated for mechanism, laundering risk, codification level, engine-v bump class, OI-019 interaction.

### M1 — Enlarge default-read surface so Outsider-lineage pattern is visible at session-open

**Mechanism (concrete):** do NOT add any new file to `read-contract.md` v4 §1. Instead, add one clause to `prompts/development.md` §Assess directing the Case Steward, when any multi-perspective deliberation is being shape-proposed, to cite the Outsider-lineage precedent count explicitly (e.g., "Outsider is non-Claude in NN of NN prior exercises; if this assessment proposes otherwise, §5 must name the departure as substantive"). Concrete text-level edit: a single bullet in `prompts/development.md` near the existing §2c close-rotation guidance. No change to read-contract.md.

**Anti-laundering risks:** medium. Adding the OI-019 "distribution-property observations at session-open" class is exactly the pattern OI-019 §5.12 reopen warrant (b) flags: mechanism created because a lapse occurred. Mitigating factor: the prompt clause is narrow (Outsider-role-specific, not a general distribution-audit), and it is a drafting-aid not a forcing convention. Retrofit-risk: low if scoped to Outsider, high if generalised. Keep it narrow.

**Codification level:** minor convention. Session-decision-record adoption with a 3-session verification window paralleling D-129. No spec amendment.

**Engine-v bump class:** none. `prompts/development.md` is not an engine-definition file for bump purposes when revised at the guidance level (see engine-manifest §5 — bumps trigger on substantive revision; a single directive bullet analogous to the existing §2c-window guidance does not meet that threshold).

**OI-019 interaction:** neutral. Addresses a specific Outsider-role observation class, not the general extended-baseline-visibility question in OI-019 (f). Does not advance OI-019's resolution; does not constrain it.

### M2 — Convene checklist that names lineage per perspective and blocks Claude-as-Outsider absent explicit override

**Mechanism (concrete):** amend `specifications/methodology-kernel.md` §3 Convene to add a two-sentence requirement: *"When a deliberation convenes named perspectives, each perspective's lineage MUST be recorded at convening time (Claude / non-Claude / specific non-Claude family). If the Outsider role is assigned to a Claude participant, the assessment MUST state this as a departure and name the reason."* Parallel amendment to `specifications/multi-agent-deliberation.md` §Perspectives adding a sub-bullet: *"Outsider-role lineage. If a deliberation names an Outsider perspective, its lineage is recorded at convening time; a Claude-lineage Outsider is a declared departure, not a default."* Validator support optional (check could parse assessment §5 for "Outsider" adjacency to "Claude subagent" without accompanying "departure" marker; P4 is best placed to evaluate whether this is worth building).

**Anti-laundering risks:** low-to-medium. The checklist is procedural, not stance-level — it forces disclosure, not a specific answer. The retrofit-risk per OI-019 §5.12 (b) is present but mitigated by the declared-departure escape hatch (the procedure does not assert Claude-as-Outsider is always wrong; it requires it be named). Stronger than M3 on this dimension: M3 is stance-level and forecloses; M2 is procedural and discloses.

**Codification level:** substantive spec amendment (both kernel and MAD v4). Two files touched.

**Engine-v bump class:** engine-v7 → engine-v8. Both kernel and MAD v4 are engine-definition files. Per engine-manifest §5: "existing engine-definition file receives a substantive revision" fires. Would be the seventh bump.

**OI-019 interaction:** advances (e) "D-129 spec-codification shape post-verification" indirectly — this is a similar disclosure-discipline pattern (record the thing you did, with reason). Does not conflict with (a)–(d) or (f).

### M3 — MAD v4 normative addition: Outsider MUST be non-Claude when non-Claude participation is required

**Mechanism (concrete):** add a normative clause to `specifications/multi-agent-deliberation.md` in §When Non-Claude Participation Is Required or §Perspectives: *"Outsider-role lineage constraint. When non-Claude participation is required per the triggers above, the Outsider role (if named in the deliberation) MUST be assigned to a non-Claude participant. A deliberation that assigns the Outsider role to a Claude participant in a required-trigger context is a specification violation. A non-required-trigger deliberation that names an Outsider role SHOULD assign non-Claude lineage; exceptions are recorded at convening time with reason."* Validator: add a check parsing manifest files — if any `outsider.manifest.yaml` in a required-trigger session has `participant_kind: claude-subagent`, fail.

**Anti-laundering risks:** medium-high. This is the retrofit-shaped mitigation per OI-019 §5.12 (b): S043 surfaced the problem; if this session adds the clause, the clause is in the class "spec change made in the same session that surfaced the motivating lapse." The MAD v4 §Limitations warning applies and the brief §7 names this explicitly. The clause is what the operator has declared correct; so reaching it is substantively justifiable. The risk is about *discipline integrity*, not substantive correctness — retrofitting even a substantively-right rule teaches the engine the wrong lesson about when to change specs.

**Codification level:** substantive spec amendment (MAD v4 only).

**Engine-v bump class:** engine-v7 → engine-v8. Per engine-manifest §5. Seventh bump overall.

**OI-019 interaction:** conflicts with OI-019 §5.12 reopen warrant (b) if adopted this session without a verification window — the Path-Selection Defender position exists to preserve the anti-laundering bar, and rapid spec change on an OI-adjacent question is exactly what §5.12 warns against. Recommended path: M3 is correctly-scoped as a future adoption *after* M2's disclosure-procedure has been exercised for at least 3 sessions.

**Recommendation:** DEFER M3 to a post-verification-window session (S047+). Adopt M2 now; M3 after M2 produces operational evidence.

### M4 — Multi-family panel discipline as default for substantive deliberations

Per brief note: "multi-family panel" means two-family panel with Codex given Gemini's weaker reasoning. Reformulating:

**Mechanism (concrete):** amend MAD v4 §When Non-Claude Participation Is Required to state: *"Substantive deliberations (triggers 1–3) SHOULD convene at least one Codex/GPT perspective in addition to any Gemini or other non-Claude participation. A deliberation with only Gemini non-Claude participation is an acceptable but not preferred shape for substantive triggers; the rationale must be recorded."*

**Anti-laundering risks:** high. This mitigation (i) concentrates the non-Claude record on GPT-family, exactly the concern §5.6 flagged; (ii) hardcodes a temporary operational weakness (Gemini's reasoning capability at this date) into spec; (iii) creates a perverse incentive to not exercise Gemini when stronger reasoning would help. The operator's operational-constraint disclosure is session-specific, not spec-invariant.

**Codification level:** spec-level if adopted; but I am **recommending REJECTION**.

**Engine-v bump class:** would be engine-v7 → engine-v8 if adopted. Not recommended.

**OI-019 interaction:** conflicts with §5.6 reopen warrant (i) (external-review-cites-narrow-record) and with OI-019's general concern for warrant-surface diversity.

**Recommendation:** REJECT. Record the operator's operational preference as a session-time consideration, not a spec-level rule. If Gemini's capability improves, the reason to hardcode disappears; if Codex's does not, the reason to hardcode risks overcorrection. This is best held at Case-Steward-discretion level informed by §5.6 monitoring, not at spec level.

### M5 (new) — Assessment §5 substantive-departure naming discipline

**Mechanism (concrete):** amend `prompts/development.md` §Assess to require: *"When a session-open assessment §5 shape proposal departs from a historical convention with ≥5 prior exercises, the assessment MUST name the departure as substantive in §5 itself (not in §6 Rejected alternatives), state the count of prior exercises, and propose explicit ratification rather than default-token ratification."* Analogous forcing function to the existing "substantive-revision candidate" framing but one level more granular — targeting §5-drafting specifically.

**Anti-laundering risks:** low. The mechanism is author-discipline at the drafting layer, not a new normative clause. Retrofit-risk is low because the convention is general (any ≥5-exercise convention, not just Outsider-lineage) and addresses the structural cause 3 directly. It protects future sessions from analogous invisible-departure lapses without locking any specific stance.

**Codification level:** minor convention. 3-session verification window (S045/S046/S047).

**Engine-v bump class:** none. Prompt-level guidance revision, similar to M1 classification.

**OI-019 interaction:** neutral-to-advancing. Complements OI-019 (d)'s operator-frame-observation input class by building a symmetric inward-facing discipline: the Case Steward catches substantive departures in its own drafting, not just in operator-surfaced observations.

**Recommendation:** ADOPT as minor convention this session. Complements M2 at the drafting layer.

### M6 (new) — Operator ratification discipline for substantive-departure shapes

**Mechanism (concrete):** amend `prompts/development.md` §Convene to require: *"When a session-open assessment §5 includes a substantive-departure shape per the M5 discipline, the session MUST halt for explicit operator ratification; default-token ratification is insufficient. The §5 text must surface the specific ratification decision sought (not the whole shape) so the operator can consent or dissent on the specific departure."* This addresses cause 4 (default-token ratification) at the forcing-function layer.

**Anti-laundering risks:** low. Increases operator overhead marginally; does not foreclose any direction. Retrofit-risk low.

**Codification level:** minor convention.

**Engine-v bump class:** none.

**OI-019 interaction:** neutral.

**Recommendation:** ADOPT as minor convention paired with M5.

### M7 (new) — OI-019 cross-linkage annotation

**Mechanism (concrete):** OI-019 §Cross-linkage gains a new entry recording Session 044's role/lineage question as a related-not-merged concern; Session 044 opens a distinct new OI (call it OI-020) for the Outsider-role-lineage question if M2/M3 are deferred past this session.

**Anti-laundering risks:** low. Keeps issues separate per OI-019 opening rationale. Does not bundle.

**Codification level:** OI-level annotation + possible new OI.

**Engine-v bump class:** none.

**OI-019 interaction:** explicitly non-merging; preserves OI-019 scope.

**Recommendation:** if M2 and M3 are both deferred past this session, open OI-020; if M2 is adopted this session, the OI is not needed.

## Q4 — Should MAD v4 gain a normative clause on Outsider lineage?

Candidates ranked by my mitigation-design preference:

- **(c) Convene-procedural disclosure** (= my M2): **preferred this session.** It names the load-bearing procedural gap (cause 2) without foreclosing edge-cases and without retrofitting a stance-level rule.
- **(a) Scope-conditional normative** (= my M3): **preferred post-verification** (S047+). Substantively correct; timing is the issue.
- **(b) Unconditional**: rejected as overbroad per Q2 above.
- **(d) Other**: M5+M6 above are "other" — author-discipline and ratification-discipline at the prompt layer rather than at MAD v4 itself.

## Q6 — Combined treatment with OI-019?

**Keep separate.** OI-019 concerns work-channel / warrant-surface diversity — a diffuse multi-mechanism question with no 3-of-5 convergence at S043. The Outsider-role-lineage question is concrete, load-bearing, and has a specific operator constraint. Bundling would dilute both. Cross-linkage annotation is appropriate (M7).

## Q7 — Is any part of the operator's framing wrong?

Not in a way warranting partial rejection. The "error" characterisation is apt (cause 3 is a drafting-level lapse, which is the thing an engine-discipline framing labels "error"). The five candidate causes are substantially load-bearing (my Q1 rates four as such; one as partially-so-and-best-placed-in-OI-019). The four candidate mitigations are partially addressing root causes — but M4 is targeting a non-load-bearing framing (§5.6-family-concentration is a separate concern from the role/lineage question). I have argued above for M4 rejection with that reason.

## Independent claim

The mitigation package that best addresses the S043 lapse is a **two-layer disclosure discipline** (M2 spec-level + M5/M6 prompt-level), deferring stance-level codification (M3) to post-verification — this sequences the anti-laundering bar correctly (disclosure this session; stance-level spec change after M2's procedural discipline has produced operational evidence across S045–S047). Mitigations M4 (multi-family-panel-as-default) and any rapid M3 adoption should be rejected as carrying laundering surface that exceeds the problem they address.

## Confidence and limits

**Confident:**
- M2 is the tightest-fitting minimum-viable mitigation and is correctly scoped as spec-level.
- M4 should be rejected on laundering-surface grounds regardless of the Gemini-capability caveat.
- M3 is substantively correct but should be sequenced post-verification, not adopted this session.

**Not confident:**
- Whether M2 qualifies as "substantive" enough to bump engine-v7 → engine-v8, or whether it is a minor spec elaboration within OI-002 heuristic (the amendment is small text-wise; the principle it codifies is not new — it makes explicit what was implicit). The Path-Selection Defender precedent (WX-35-1 pattern: minor convention → verification → spec codification) suggests M2 could plausibly be a minor amendment this session, avoiding the bump. I defer to synthesis on this classification.
- Whether M5 + M6 are genuinely additive or whether M2 alone captures their work. If M2 is adopted strongly, M5/M6 may be over-engineering.
- Whether P4 (Cross-Family Reviewer) will challenge M2 as retrofit-shaped despite my sequencing argument — my distinction between "procedural disclosure" and "stance-level prohibition" carries load and deserves adversarial testing.

**Unresolved:**
- Whether a separate OI-020 is warranted if M2 is deferred. My recommendation assumes M2 adopts this session; if synthesis defers it, OI-020 becomes the right path rather than leaving the concern unrecorded.
- Claude-family priors: I am designing mitigations as a Claude subagent. The non-Claude perspectives (P3 Outsider Codex, P4 Cross-Family Reviewer Codex) should scrutinise whether my bias toward procedural-over-stance-level reflects genuine anti-laundering reasoning or reflects Claude-family reluctance to codify a rule that forecloses Claude participation in a specific role. I have tried to reason through this explicitly but cannot fully self-audit.
