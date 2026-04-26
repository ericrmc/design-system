---
session: 074
title: Tier 2.5 Cross-Family Reviewer Audit — Session 074
date: 2026-04-26
status: complete
reviewer: codex (GPT-5.5)
reviewer_provider: openai
reviewer_kind: non-anthropic-model
reviewer_overlap_with_recent_mad_perspectives: "family-overlap with S058+S062+S064+S071+S073 codex P3+P4 perspectives; no scope-overlap with S074 audit subjects (S074 audits operator-directive amendment, not prior MAD outputs)"
trigger_condition: multiple
session_under_review_subjects:
  - retention-window-closes:
      - provenance/068-session/03-close.md
      - provenance/069-session/03-close.md
      - provenance/070-session/03-close.md
      - provenance/071-session/03-close.md
      - provenance/072-session/03-close.md
      - provenance/073-session/03-close.md
  - validation-debt-ledger: validation-debt/index.md
  - active-watchpoints: WX-28-1 + WX-24-1 + WX-43-1 + WX-50-1 + WX-58-1 + WX-62-1 (closed)
  - engine-feedback-inbox: engine-feedback/INDEX.md (EF-073 row added)
  - open-issues: open-issues/index.md
scope_coverage_table:
  retention-window-closes: exercised
  validation-debt-ledger: exercised
  active-watchpoints: exercised
  engine-feedback-inbox: exercised
  open-issues: exercised
findings_count: 4
findings_dispositioned: 4
duration_minutes: 72
reviewer_prompt_template_version: 2
bootstrap_status: limited-confidence
---

## §1 Scope and trigger basis

This audit covers S074 close-readiness at audit-time. `provenance/074-session/03-close.md` does not yet exist, so close correctness is evaluated against the in-progress S074 materials: `00-assessment.md`, `02-decisions.md`, EF-073 inbox/triage/index state, revised `validation-approach.md` v8, preserved `validation-approach-v7.md`, updated `tools/validate.sh`, `workspace-structure.md` v9, `engine-manifest.md` engine-v14 entry, `validation-debt/index.md`, `open-issues/index.md`, and retention-window closes S068-S073.

Tier 2.5 triggers fire correctly. Trigger (a) fires because S074 substantively revises the Tier 2.5 mechanism in `validation-approach.md` v7 → v8 and substantively updates `tools/validate.sh`; it also updates `engine-manifest.md` and makes a minor `workspace-structure.md` amendment. Trigger (e) fires because the S074 operator directive is itself a discretionary reviewer-policy intervention. Trigger (b) is partial: this is a substantive single-session operator-directed amendment, not a normal multi-session substantive arc. Trigger (d) does not fire because VD-003 remains in-progress, with no lifecycle close/defer/escalate event at S074.

Reviewer-overlap disclosure: I am OpenAI/codex family and have family-overlap with prior MAD P3/P4 perspectives in S058, S062, S064, S071, and S073. I do not have scope-overlap with S074’s load-bearing subject, which is the operator-directed reviewer-family policy amendment. Counterweighting check: the load-bearing authority surface here is the operator directive itself plus the S073 empirical cross-check record; I reduce independence weight on any claims about codex-perspective quality and focus on whether the resulting mechanism text, tooling, ledgers, and forward shape are coherent.

## §2 (α)-flag coverage

Check 26 was in scope over the retention-window closes and emitted no honest-limit repetition cluster in the current reviewer run. Because S074 has no close file at audit-time, there is no S074 close-local §8 honest-limit text for Check 26 to inspect. (α)-flag coverage is therefore clean for the S068-S073 window and vacuous-by-scope for S074 close text.

I do not treat the incomplete validator run as final S074 validation. It is mid-session: S074 has no `03-close.md`, no records row yet, and no audit file committed. However, the run did surface a close-readiness issue in the current decision file, dispositioned below as F1.

## §3 Substantive evidence

## §3a Close correctness

The S074 assessment and decisions correctly identify the operator-directive path. The EF-073 intake records the directive verbatim: Gemini/google is excluded from reviewer roles, family-distinctness is to be relaxed, and no further MAD is to deliberate retaining Gemini. D-286 maps that into Path-L per operator-directed substantive amendment, explicitly deferring S073 D-282 phase-3.1 implementation to S075+. D-287 records EF-073 as same-session resolved. D-288 and D-289 record the two load-bearing changes: `validation-approach.md` v8 removes family-distinctness and excludes google; `tools/validate.sh` adds `EXCLUDED_REVIEWER_PROVIDERS="google"` and the S074+ check 27 provider sub-clause. D-291 records engine-v14.

Finding F1: S074 `02-decisions.md` is not validator-clean as written. D-288, D-289, and D-291 each declare `[d016_2]`, but they only carry `Non-Claude participation: skipped per operator-directive (D-286 single-agent rationale carries forward)`. The current check 14 pattern accepts D-286 because it contains the exact `Single-agent reason:` annotation, but it fails D-288/D-289/D-291 because they declare d016 triggers without perspective files and without that exact annotation. This is form-level but close-blocking if left unchanged. The substantive reason is present by reference; the artefact shape is not.

Subject to F1, the close-state claims are otherwise coherent: EF-073 index row exists and is resolved, v7 is preserved as superseded, engine-v14 is recorded, and `validation-debt/index.md` remains unchanged with VD-003 in-progress.

## §3b Mechanism adequacy

The main operator-directed mechanism change is justified by the evidence packet. S073’s official Gemini audit produced `findings_count: 0`, while the codex cross-check on the same input produced two substantive findings. EF-073 correctly frames this as evidence against treating family-distinctness as the load-bearing property of audit quality. The v8 rule preserves the stronger remaining counter-pressure: mandatory overlap disclosure and either scope exclusion or counterweighting.

Finding F2: `validation-approach.md` v8 did not fully remove family-distinctness semantics. The main v8 rule at lines 144-154 says family-distinctness is removed and only google is excluded, but the earlier Tier 2.5 summary still says “The reviewer is non-Claude family” at line 33. More materially, the gaming-modes section at line 162 still says “reviewer-family must differ from any declared orchestrator-family.” That conflicts with the v8 rule permitting same-family reviewers with disclosure and counterweighting. This is not just wording: future sessions could cite the stale line to reject an otherwise allowed anthropic/openai reviewer.

Finding F3: `validation-approach.md` v8 preserves stale S073 phase-3 implementation text as if S074 phase-3.1 still landed. Lines 262-276 still say CM1/CM3, SCD-3, the check 26 substrate-aware branch, and the template v3 candidate occur at S074 phase-3.1, and line 276 says the “full `validation-approach.md` v7 → v8 substantive revision at S074 phase-3.1 close codifies the (z6) digest schema spec.” S074 D-286 explicitly defers that implementation to S075+, and the actual v8 revision is the reviewer-family/google amendment, not the full digest implementation. This creates a forward-commitment mismatch inside the active validation spec.

Finding F4: check 27 still does not structurally enforce the audit shape that v8 says is required. `validation-approach.md` requires frontmatter scope coverage, §1, §2, tripartite §3, §4, §5, §6, §7, §8, and bootstrap labelling when applicable. `tools/validate.sh` currently checks only §2, §7, a scope-coverage proxy, the bootstrap frontmatter label heuristic, and the new google-provider exclusion. D-289 explicitly says it preserves the existing v7 sub-clauses rather than adding full shape enforcement. The result is a mechanism gap: the spec relies on the reviewer prompt and operator audit for most required sections, while the validator’s advertised check 27 coverage is narrower than the spec table implies.

## §3c Trajectory discipline

Trajectory discipline is stronger than ceremonial here. The operator directive is not a spontaneous taste change; it is grounded in a concrete mismatch between four Gemini zero-finding audits and the S073 codex cross-check. S074 also correctly preserves historical Gemini audits rather than retroactively invalidating closed records.

The main trajectory risk is displacement. S073 D-282 pre-ratified a concrete S074 phase-3.1 implementation path for the γ digest arc. S074 properly supersedes it under operator authority, but the active v8 spec now mixes two trajectories: the actual S074 reviewer-policy amendment and the deferred γ implementation text still written as S074. S075 should recover the γ implementation arc with explicit cleanup, not proceed as if v8 already contains the full digest implementation.

Aggregate-budget pressure also persists. S071-S073 all record aggregate pressure above the 90K soft band, and S074 plans to rely on close-rotation S068 OUT as the aggregate-reducing action while leaving EF-068-read-write-rebalance unactivated. That discharges the letter of the read-contract obligation, but it does not resolve the trajectory. The repeated “close-rotation alone” posture should not become a substitute for the structural rebalance question.

## §4 Disposition table

| Item | Source | Disposition | Rationale |
|---|---|---|---|
| F1: D-288/D-289/D-291 declare d016 triggers without exact `Single-agent reason:` annotation | `provenance/074-session/02-decisions.md` D-288/D-289/D-291; validator check 14 behavior | accepted | The rationale exists by reference to D-286, but current validator form requires per-decision exact annotation or perspectives. Fix before final close. |
| F2: v8 leaves stale non-Claude/family-distinctness text | `specifications/validation-approach.md` lines 33 and 162 versus lines 144-154 | accepted | Conflicts with S074’s load-bearing rule change and can mislead future reviewer selection. |
| F3: v8 preserves stale S074 phase-3.1 γ implementation text | `specifications/validation-approach.md` lines 262-276; S074 D-286 defers S073 D-282 to S075+ | accepted | Active spec now describes deferred implementation as already scheduled at S074/v8. Needs cleanup in S075 recovery scope. |
| F4: check 27 enforcement narrower than required audit shape | `tools/validate.sh` check 27 block; `validation-approach.md` audit-shape requirements | accepted | Validator enforces only a subset of required audit shape; this is a continuing mechanism-adequacy gap, not a blocker for this audit because the prompt requires the full shape manually. |

## §5 Stale-item escalation

No validation-debt lifecycle item is stale. VD-001 and VD-002 are resolved. VD-003 is `in-progress`, `review_by_session: S076`, and its state is consistent with S074 D-292’s claim that the ledger is unchanged at S074. No ledger-vs-narrative mismatch requires escalation.

Engine-feedback has no new items after EF-073 is filed and resolved. Six triaged items remain visible, including non-γ long-deferred surfaces EF-068-read-write-rebalance, EF-058-claude-md-drift, and EF-047-brief-slot-template. These are not stale under the validation-debt ledger, but they should be named explicitly in future §7 next-session-shape tests rather than compressed into “inbox actively progressing.”

## §6 Reviewer metrics

Reviewer overlap: family-overlap with prior codex MAD perspectives, no scope-overlap with S074 audit subject. Findings count: 4. Findings dispositioned: 4. Duration: 72 minutes, producer_kind: agent-declared, authority_level: tertiary. Harness telemetry digest: unavailable; γ phase-3 digest implementation is deferred beyond S074 by the operator directive. Reviewer prompt template version: 2. Bootstrap status: limited-confidence.

## §7 Next-session-shape critique

Because S074 has no close file at audit-time, this test evaluates the recorded forward shape in S074 assessment/decisions: recover phase-3.1 implementation at S075+ while preserving VD-003 review at S076.

1. Open issues unprogressed: present. The index still has 13 active OIs. The no-action justification is acceptable for S074 because the operator directive was narrow and urgent. S075 should not use that same justification without naming the active γ implementation and deferred EF/OI surfaces.

2. Engine-feedback inbox untriaged or repeatedly deferred: partially present. EF-073 is resolved. The γ-surface records continue through VD-003. But EF-068-read-write-rebalance, EF-058-claude-md-drift, and EF-047-brief-slot-template remain long-deferred. Path-AS/Path-L recovery at S075 is acceptable only if the close names these non-γ rows as consciously deferred.

3. Watchpoints stale or underspecified: not fired as a stale-watchpoint issue. WX-28-1 and WX-24-1 are actively tracked; WX-50-1/WX-58-1/WX-62-1 are closed. The aggregate-budget watch surface remains substantively active.

4. Validation debt exists and next-session recommendation does not explain why it can wait: condition does not dispute the proposed S075 recovery. VD-003 is in-progress and S075+ phase-3.1 is the direct next action after S074 supersession. S075 should explicitly reconcile the S074 deferral with S076 review timing.

5. Recent closes repeatedly recommend watch without operator agenda: not fired. The S068-S073 window is Path T, Path T, Path-AS Shape-1, Path-AS MAD, Path-AS design-space, Path-AS MAD. No repeated Path A default pattern exists.

Disposition: Path-AS/Path-L γ implementation recovery at S075 is valid. Path A would be disputed unless the operator gives a new direction. S075 should first clear F1-F3 or explicitly carry them as known defects.

## §8 Reviewer cost note

Reviewer self-report: 72 minutes. Token count is not harness-measured. Under REVD-2 quarantine, this cost note is agent-declared/tertiary and excluded from §10.4-M25 audit-cost threshold arithmetic until harness telemetry is implemented and re-baselined. Compared with the S073 codex cross-check, this audit spent more time because it included the revised v8/v7 diff, tool inspection, and in-progress S074 validator behavior.

## §X Bootstrap status

This audit has `bootstrap_status: limited-confidence` because S074 revises the §Tier 2.5 mechanism being used to audit S074.

Rules being audited under: S074 opened under active `validation-approach.md` v7. The audit is being produced under the about-to-be-adopted v8 rule: family-distinctness removed, google excluded, overlap disclosure plus counterweighting retained. That bootstrap posture is exactly why the limited-confidence label applies.

Reviewer overlap status: codex/GPT-5.5 has family-overlap with prior S058+S062+S064+S071+S073 codex P3/P4 perspectives. There is no scope-overlap with S074’s load-bearing subject, which is the operator-directed reviewer-family amendment. The counterweighting check is the operator-policy authority surface plus the S073 empirical cross-check record.

This audit must not be cited as clean validation of the revised Tier 2.5 mechanism. It may be cited as a limited-confidence bootstrap audit that found four issues requiring cleanup or explicit carry-forward.
