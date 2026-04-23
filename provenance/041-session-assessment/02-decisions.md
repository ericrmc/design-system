---
session: 041
title: Decisions — OI-004 closure (state 3→4); minor spec documentary update; housekeeping
date: 2026-04-24
status: complete
---

# Decisions — Session 041

## D-125: Advance OI-004 from state 3 (Articulated; awaiting closure-retrospective) to state 4 (Closed)

**Triggers met:** [d023_4]

**Triggers rationale:** D-125 asserts a state change for OI-004 from state 3 to state 4 per `multi-agent-deliberation.md` v4 §Closure Procedure. This is the literal firing of d023_4 ("Asserts a change in the state of OI-004"). The decision was backed by multi-agent deliberation with non-Claude participation (three Claude subagents + OpenAI GPT-5.4 via `codex exec`) per the required-trigger deliberation clause 4 of §When Non-Claude Participation Is Required.

**Decision:**

OI-004 advances from state 3 to state 4 (Closed) at Session 041 close. All four closure conditions per `multi-agent-deliberation.md` v4 §Closure Procedure for OI-004 are met:

- (i) Closure-retrospective artefact committed at `provenance/041-session-assessment/oi-004-retrospective.md` with the three required sections (`## Qualifying Deliberations Table`, `## Summary Tally`, `## P4 Assertion`); check 18 expected PASS at validator run; Tier 2 Q8 substantively answered in `03-close.md` §3b Q8.
- (ii) Successor-session adjudication: Session 041 ≠ Session 021 (articulating session). Session 041 is a multi-agent deliberation with non-Claude participation per clause 4.
- (iii) Cross-model contradiction-prevailing data point identified in the retrospective's P4 Assertion: **Session 017 H4 layered model** as the anchor case (Outsider rejected the Claude-framed H1/H2/H3 option-set and proposed H4 as a fourth hypothesis; synthesis adopted H4). **Session 014 three-cell protocol** as a corroborating case. Both cases are verified against source synthesis self-characterisations per `provenance/041-session-assessment/01-deliberation.md` §R2 source-text-primacy reading.
- (iv) Voluntary:required ratio at closure decision time: 12:10 = 1.20 ≥ 1.0.

**Rationale:**

Per `provenance/041-session-assessment/01-deliberation.md` §4 R1 + §2 (Convergences) + §3 (Divergences):

- 3-of-4 cross-family convergence for closure (Closure-advocate + Retrospective-auditor + Outsider; Closure-skeptic dissents) meets the workspace's 3-of-4 cross-family threshold for substantive moves. The non-Claude vote (Outsider) is on the closure side.
- Condition (iii) is satisfied by **Session 017 H4 layered model** as the anchor P4 case and **Session 014 three-cell protocol** as a corroborating case. The Outsider's [01D, Q2] strict reading (only S017 qualifies cleanly; S014 borderline; S021 and S036 do not qualify per source-synthesis self-characterisations) is adopted on source-text-primacy grounds. The Retrospective-auditor's [01C] broader grading (all four candidates at grade 3) is preserved as §5.8 first-class minority. The Closure-skeptic's [01B] deferral position is preserved as §5.7 first-class minority.
- Conditions (ii) and (iv) are uncontested (4-of-4).
- Condition (i) is satisfied by the committed retrospective artefact; check 18 verifies structural well-formedness; Tier 2 Q8 substantive review in `03-close.md` addresses the substantive-adequacy question.

The §5.2 Articulator close-on-articulation minority and §5.3 Outsider "indefinitely movable finish line" minority preserved at Session 021 are **discharged as vindicated-and-discharged** per R4 of the deliberation. Neither is preserved as a live operational minority after closure. §5.3 is strongly vindicated (Session 041 is exactly the indefinitely-deferrable pattern §5.3 warned against); §5.2 is partially vindicated (the articulator was correct that articulation without a near-term retrospective invites drift; twenty successor sessions confirmed this) but not vindicated in the strong same-session-closure sense.

**Non-Claude participation:** not skipped. Outsider: OpenAI GPT-5.4 via `codex exec`, session id `019dbc04-102e-73f3-ae02-d784ef73bd98`, manifest at `manifests/outsider.manifest.yaml`, raw response at `01D-perspective-outsider.md`. Criterion-4 prongs per `multi-agent-deliberation.md` v4 §Criterion-4 Articulation: C4-1 ✓ (OpenAI in closed set); C4-2 `unknown` (signal per §Unknown-field rule; surfaces to Tier 2 Q8); C4-3 ✓ (`provider: openai` + `model_family: gpt-5` + `model_id: gpt-5.4` all recorded).

**Rejected alternatives:**

1. **Retain at state 3 (Skeptic position)**: the Closure-skeptic argued deferral pending non-GPT non-Claude participation. Rejected because (a) the Session 021 Skeptic's strict-enumeration minority §5.1 already preserved the concern about enumeration-beyond-exercise; (b) continued state-3 retention has itself become the indefinitely-deferrable pattern §5.3 warned against; (c) the GPT-family concentration is preserved as new §5.6 minority with reopen warrants (R3), not absorbed silently into the closed state. The Skeptic's concern is addressed structurally via §5.6 preservation rather than via closure deferral.

2. **Close with broad P4 grading (Auditor position)**: the Retrospective-auditor graded all four candidate cases at 3 (strong). Rejected in favour of Outsider's strict reading because the source synthesis texts (S021 §3.5 + §7; S036 §3c) explicitly self-characterise the Outsider contributions as frame-completion or augmentation rather than contradiction-prevailing. Adopting the broader grading would have contradicted the source-text evidence.

3. **Close without preserving new minority**: absorbing the GPT-family concern into the closed-state Limitations note alone (no first-class minority). Rejected because §5.6 requires operational activation warrants for defeasibility; a Limitations-note-only approach lacks the reopen-trigger specificity Session 015/019/020/021 precedent established.

4. **Bundle closure with a substantive spec revision**: adopt closed-state d023_4 semantics as substantive revision to `multi-agent-deliberation.md` §When Non-Claude Participation Is Required clause 4, bumping engine-v7→engine-v8. Rejected in favour of treating the closed-state semantics as clarification-not-revision per the 4-of-4 convergence on the substantive reading (§2.6 of synthesis). The minor documentary update per D-126 is sufficient.

5. **Produce retrospective without closing** (the Session 040 close §6 "Path OI-004 retrospective draft" framing): produce the retrospective artefact this session and defer the state-3→4 decision to a future successor session. Rejected because (a) the Outsider activation-warrant §5.3 has already been operationally reached (indefinitely-movable finish line after 20 successor sessions); producing the retrospective without closing extends the same pattern by another session; (b) 3-of-4 cross-family met the threshold for closure in this session, not in a hypothetical future one; (c) the Session 040 close's "draft" framing was default-agent pre-assessment language, not an operator constraint — operator's ratification of Path OI-004 without qualification permits this session to decide closure if the evidence supports it.

## D-126: OI housekeeping + minority preservation + minor documentary spec update (closed-state OI-004)

**Triggers met:** [d016_3]

**Triggers rationale:** D-126 effects a minor documentary update to `multi-agent-deliberation.md` §Closure Criteria + §Closure Procedure to record the closed-state OI-004 status and the closed-state semantics of d023_4 + clause 4 — this is a revision to a specification in `specifications/`, firing d016_3. Per the OI-002 substantive-vs-minor heuristic (Session 001+), documentary status-change + clarification-of-existing-semantics is minor (not substantive), so this spec change does not fire d023_2 (substantive revision of `multi-agent-deliberation.md`) and does not bump engine-v7.

**Decision:**

Documentary update to `specifications/multi-agent-deliberation.md`:

- §Closure Criteria for OI-004: update status-note "OI-004 may be considered for closure" framing to reflect state 4 (Closed) reached at Session 041 per D-125.
- §Closure Procedure for OI-004: update state 4 description to "Closed (reached Session 041 per D-125)" with pointer to `open-issues/resolved/OI-004.md`.
- No normative text change. No new content. No schema change. No validator change.

Additionally:

- **Move `open-issues/OI-004.md` to `open-issues/resolved/OI-004.md`** per `open-issues/index.md` §Conventions resolution protocol. Update frontmatter: `status: resolved`; add `resolved-in-session: 041`; add `resolved-on: 2026-04-24`. Append Session 041 closure note preserving the catch-up-history from the prior record.
- **Update `open-issues/index.md`**: remove OI-004 row from Active issues table; add OI-004 row to Resolved issues table with resolved-on 2026-04-24, resolved-session 041. Update active count from 13 to 12.
- **Preserve §5.6 (GPT-family-concentration joint minority)** in the resolved-OI-004 record + cross-reference from `multi-agent-deliberation.md` minority-preservation context.
- **Preserve §5.7 (Skeptic deferral) and §5.8 (Auditor broader-grading)** in the closure-retrospective provenance. These are not added to the active preserved-minority ledger; they are historical artifacts of Session 041's closure deliberation.
- **Discharge §5.2 and §5.3** Session 021 minorities per D-125 rationale. Record as vindicated-and-discharged in closed-state record.

**OI metric updates at Session 041 close:**

- OI-004: state 4 (Closed). Resolved-in-session 041. Criterion-2 final tally: 9-of-3. Voluntary:required final ratio: 12:10 = 1.20. Criterion-3 cumulative final: 79.
- OI-016 (Resolved-provisionally-v2): unchanged. §9 trigger 5 at 2-of-3; trigger 7 re-fire counter at 0-of-3. Session 041 is not a reference-validation exercise.
- OI-002: **16th data point** — D-126 minor-classification of closed-state documentary update. Heuristic continues to hold stable.
- OI-005, OI-006, OI-007, OI-008, OI-009, OI-011, OI-012, OI-013, OI-014, OI-015, OI-018: unchanged.
- **Active OI count: 13 → 12** (OI-004 moves to resolved).

**First-class minorities at Session 041 close:**

- Total preserved across engine: 27 → **28** (§5.6 added; §5.2 + §5.3 discharged; net +1 with disposition recorded).
- Resolved / discharged (13): §5.2 S027 (vindicated S027); §5.3 S028 (converted S028); §5.6 S031 (vindicated S031); §5.7 S033 (vindicated S033); §5.8 S031 (vindicated S031); §5.9 S034 (vindicated S034); §5.10 S034 (vindicated S034); §10.2-Skeptic-preemptive S032 (vindicated S032); §10.1 S032→S033 (activated-and-adopted); §10.1-Skeptic+Outsider joint S032 (vindicated-direction); §10.2 Reviser S032 (partial-vindicated); **§5.2 S021 (Articulator close-on-articulation) discharged at S041**; **§5.3 S021 (Outsider "indefinitely movable finish line") discharged at S041**.
- Continued preservation (15): §5.1 S023; §5.4 S022 (activated-not-escalated); §5.5 S023; Session 024 A.4 group (5); Session 027 §A/§B/§C (3); §5.11; §10.3 three (Skeptic-preserver minimal-revision; Outsider naming; Reviser separate-OI); §10.4-M1 through §10.4-M6 (6).
- **New** (1): **§5.6 Skeptic + Outsider GPT-family-concentration concern** (joint; cross-family 2-of-4 finding-of-fact convergence; operational warrants per `provenance/041-session-assessment/01-deliberation.md` §5.6 + `open-issues/resolved/OI-004.md`).
- §5.7 and §5.8 are not added to the active ledger — they are historical-deliberation minorities preserved in the retrospective provenance only.

**Watchpoint updates:**

- **WX-22-1** witness-dumping: no new data.
- **WX-24-1** MAD growth: MAD at 6,386 words unchanged; **20-session no-growth streak** achieved — new longest; first 20-session-depth data point in watchpoint history.
- **WX-24-2** budget-literal drift: no exercise Session 041. Forward-discipline carry-forward (now seventh-session).
- **WX-24-3** n=7 stable (Session 041 adds one Outsider invocation per standard pattern; n advances to **8** — first non-"n=7 stable" data point since Session 034).
- **WX-27-1** archive-token citation: no re-firing at structural level; no author-side variants.
- **WX-28-1** close-rotation-exception-frequency: forward observation continues; thirteenth rotation at Session 041 close produces zero retention-exceptions (sustains vindicated pattern at three additional post-cumulative data points).
- **WX-33-2** reference-validation.md v3 per-file 7,160-word soft-warn: stable.
- **WX-34-1** SESSION-LOG.md row-verbosity: standing forward discipline against ~2,002-word base (post-Session-040 remediation); Session 041 row construction appropriate to substantive session.
- **WX-35-1** OI-004.md state-history gap: **standing discipline applied with explicit edit — OI-004.md is actually moved to resolved this session, not just claimed.** Fifth post-vindication operational application.
- **WX-21-2** (Session 021): RESOLVED. Session 041 closure-retrospective identified the contradiction-prevailing case (S017 H4) that WX-21-2 flagged as unverified at articulation time. Watchpoint discharged.
- **WX-21-3** (Session 021): RESOLVED. Session 041 synthesis explicitly tested and adopted the Outsider's strict reading over the Claude Auditor's broader reading on source-text-primacy grounds — the most non-orchestrator-deferring move in the synthesis. The "convergence-by-mechanism" reasoning from Session 021 R4 is partially vindicated (it justified one deferral; did not justify twenty) per Outsider [01D, Q5]. Watchpoint discharged with nuance recorded.

**Trigger counters:**

- §9 trigger 5: 2-of-3 unchanged.
- §9 trigger 7 post-v3 re-fire counter: 0-of-3 unchanged.

**Twenty-third consecutive housekeeping `[none]` record broken**: D-077 through D-124 were all `[none]`-classified (22 consecutive sessions); D-125 declares `[d023_4]` (OI-004 state change fires trigger). D-126 declares `[d016_3]` (minor spec revision). The `[none]` streak from D-077 ends at Session 041 per the operator-selected substantive Path OI-004 work.

**Engine-v7 preserved (preservation window count advances to 5; matches engine-v4 five-session preservation depth Sessions 024/025/026/027 exactly — with Session 041 being a substantive content session, not a Path-A-shape preservation session).** The engine-v cadence concern (§5.4 Session 022 minority) does not re-escalate: D-125/D-126 do not revise any engine-definition file substantively; engine-v7 is preserved through a substantive OI-closure session at the preservation-window depth matching engine-v4 exactly.

**Rejected alternatives for D-126:**

1. **No spec update at all** — leave `multi-agent-deliberation.md` §Closure Criteria and §Closure Procedure unchanged, relying solely on `open-issues/resolved/OI-004.md` to record closure. Rejected because readers of the active spec should see that OI-004 closure has been reached; the documentary update is factual correction that maintains spec-reality alignment per Tier 2 Q5.

2. **Substantive update (engine-v-bump)** — treat the closed-state d023_4 semantics as new normative content requiring engine-v8. Rejected per D-125 Rejected alternative 4: 4-of-4 convergence on substantive reading indicates the semantics were implicit in the existing text; no revision to text logic, only to status.

3. **Bundle with WX-27-1 / WX-24-2 cleanups** (Path-L-style bundle). Rejected per anti-laundering (Session 031 close §4b precedent): those cleanups were not independently warranted this session and bundling would muddy the D-125/D-126 scope.

4. **Preserve §5.7 and §5.8 in active ledger** — treat the deliberation's own dissent (Skeptic deferral; Auditor broad-grading) as live preserved minorities. Rejected because these are about Session 041's own closure decision, not about the closed-state OI-004 going forward; they are historical artefacts best preserved in the retrospective provenance, not in the active-engine minority ledger.

5. **Open a new OI for GPT-family concentration** instead of preserving §5.6. Rejected because §5.6 is properly a preserved minority with reopen-warrants on the closed issue, not a new issue in its own right — it concerns the strength of the evidence base for closure, not a distinct methodological question.

6. **Update `open-issues/index.md` active-count framing** to remove OI-016 from active count (currently hybrid-state). Rejected because OI-016's hybrid-state continues unchanged; no trigger for its reclassification this session.
