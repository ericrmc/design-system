---
title: Validation Approach
version: 9
status: active
created: 2026-04-17
last-updated: 2026-04-26
updated-by-session: 075
supersedes: validation-approach-v8.md
---

# Validation Approach

## Purpose

This specification defines how the methodology validates itself: what is checked, how checks are organized, and what the checks can and cannot assure. It serves the methodology's self-hosting principle — a methodology that cannot verify its own specifications cannot evolve reliably.

**Scope notes (Session 009 D-056 + Session 017 D-074).** This specification covers **Workspace validation** as defined in `methodology-kernel.md` v6 §7. Domain validation is performed by domain-actors outside this specification's scope. The Tier 1 / Tier 2 / Tier 2.5 discipline applies equally to self-development and external-problem applications of the Selvedge engine.

**Version history.** v9 (Session 075 per D-294) is a substantive revision implementing the (γ-6) phase-3.1 deliverables per S073 D-275 + S073 D-282 pre-ratification recovered per S074 D-286 operator-directive supersession-then-resumption. v9 (a) **codifies the SCD-3 harness-telemetry-digest schema** in §(z6) (replacing the v7+v8 DEFERRED-pointer language) with capture-adapter metadata + per-section field-level authority rules per §10.4-M34 P4 z-laundering-1 reframe; (b) **extends §Tier 2.5 audit shape** with reviewer-prompt-template v3 minimum-viable extension per S073 D-282 + (z7) lock-in-after-n=2 (digest-aware reviewer instructions; producer_kind/authority_level distinction; quarantine-semantics application; capture-adapter metadata check); (c) **closes the Codex-S074 audit Finding F4 mechanism gap** by extending check 27 enforcement to require all §1-§8 sections + tripartite §3a/§3b/§3c sub-sections (previously only §2+§7+scope-coverage were enforced); (d) records the new tooling: `tools/digest_emitter.py` (CM1 Claude Code PostToolUse hook capture-adapter; harness-measured authority; PreToolUse intentionally NOT configured per S075 D-296 to avoid duplicate records since PostToolUse event has tool_response field for status determination) + `tools/digest_reconstructor.py` (CM3 post-hoc bridge/comparator; post-hoc-reconstructed authority); (e) names the new check 26 substrate-aware branch (CHKD-2 evidence-consuming per S073 D-280 + §10.4-M33 P3 z9 reframe). v8 preserved as `validation-approach-v8.md` `status: superseded`.

v8 (Session 074 per D-288) was a substantive revision per operator-direct directive at S074 open per §10.4-M10 written-warrant clause (c) operator-surfacing channel cumulative count n=10 → n=11. v8 (a) REMOVED the v7 §Tier 2.5 reviewer-family family-distinctness requirement; reviewer family MAY now overlap with orchestrator/perspectives' family at the organisation level, with mandatory `reviewer_overlap_with_recent_mad_perspectives:` field disclosure + counterweighting check (existing v7 discipline preserved); and (b) ADDED an explicit provider-exclusion clause: the `google` provider is permanently excluded from reviewer roles per operator-directive at S074. Empirical basis recorded at `engine-feedback/inbox/EF-073-gemini-excluded-and-reviewer-family-rule-relaxation.md`: sustained findings_count=0 pattern across S063+S067+S071+S073 Gemini reviewer audits (n=4) + S073 codex cross-check on identical input produced findings_count=2 with substantive findings. v8 preserved as `validation-approach-v8.md` `status: superseded`.

v7 (Session 064 per D-233) was a substantive revision adopting operator audit findings from S063 resolving close + cross-family MAD synthesis at S064. v7 revised the §Tier 2.5 reviewer-family rule (relaxed from "no perspective in audited MAD" to "not orchestrator/close-author/primary-implementer/accountable-doer + cross-family at family + audit-scope-conditional family exclusion when self-validating own load-bearing claim"); revised the audit shape to require minimum-evidence-packet (retention-window closes + (z5) lifecycle ledger + active watchpoints + engine-feedback inbox + open-issues); added §7 Next-session-shape critique with P3's 5-condition affirmative-no-action-justification test; revised §(z5) Validation-Debt Lifecycle to make ledger **authoritative-not-witness**; added tripartite audit distinction (close correctness / mechanism adequacy / trajectory discipline); added Layer 6.5 bootstrap-limited-confidence labelling; added (z7) reviewer-prompt-template versioning + lock-in-after-n=2 discipline. Five new first-class minorities preserved §10.4-M21 through M25 (engine-wide 45 → 50). v6 (Session 063 per D-228) added §Tier 2.5 + §(z5) + §Bootstrap-Paradox + §Principled Asymmetry + checks 26+27+28 + Q10. v5-v1 history preserved per workspace-structure.md spec-versioning.

## Specification

### Multi-Tier Model

Validation has three tiers.

**Tier 1: Structural Checks** are automated checks run by `tools/validate.sh`. Verify form, not meaning.

**Tier 2: Guided Assessment** are questions printed by the validation tool for the agent or human conducting the session.

**Tier 2.5: Reviewer Discipline** is a triggered review at session close per the layered structural mechanism of S062 D-221, revised at S064 D-233 per operator audit findings + revised at S074 D-288 per operator-directive (family-distinctness REMOVED; google provider EXCLUDED from reviewer roles) + extended at S075 D-294 per (γ-6) phase-3.1 implementation (reviewer-prompt-template v3 minimum-viable extension; harness-telemetry-digest reading; producer_kind/authority_level distinction; quarantine-semantics application; capture-adapter metadata check; full §1-§8 audit-shape enforcement closing Codex-S074-F4). At v9: the reviewer MAY be from a family overlapping with orchestrator/perspectives (with mandatory disclosure + counterweighting check per §Tier 2.5 reviewer-family rule clause-by-clause below); the reviewer MUST NOT be from the `google` provider per clause (d); the reviewer MUST inspect `provenance/<NNN-session>/harness-telemetry-digest.yaml` when present and apply per-record producer_kind/authority_level distinctions per §10.4-M34. Produces `provenance/<NNN-session>/04-tier-2-audit.md`; gated on the trigger set in §Tier 2.5 below. Tier 2.5 supplements Tier 2; does not replace it.

### Principled Asymmetry (per S062 D-221 §2.2 + §10.4-M17 + S064 D-233)

The methodology exhibits a principled asymmetry between MAD-level deliberation and session-close validation:

- **Routine workspace checks may remain self-assessed** (Tier 2 Q1-Q9). The aliasing risk for these is bounded by Tier 1 + next-session Read + operator-discretionary audit.
- **Claims about unresolved validation debt, substantive progress, engine-definition change, and repeated warnings require stateful or distinct review.** These surfaces exhibit noticing-failure (writer misses pattern in own writing — operationally falsified at S051-S058 honest-limit chain) which compounds across sessions in a way that aliasing-failure (synthesizer collapses divergent perspectives) does not. Stateful review = cross-session pattern detection (Layer 1 check 26); distinct review = cross-family reviewer (Tier 2.5).

The MAD §Synthesis prohibition is alias-prevention; Tier 2.5 is noticing-failure-mitigation. Both serve cross-perspective integrity but address different failure modes.

**Tier 2.5 framing (per S064 §10.4-M23 P3 substrate-led reviewer-judged frame, adopted)**: Tier 2.5 is not "get a cross-family reviewer"; it is "force an independent-enough agent to inspect the right substrate surfaces against known failure modes." A different family reading a thin packet can still rubber-stamp; a same-family but temporally separated reviewer with a strong evidence checklist can sometimes catch more. The mechanism's load-bearing structure is **substrate-led, reviewer-judged**.

### Tier 1: Structural Checks

| # | Check | Source | Severity | Gate |
|---|-------|--------|----------|------|
| 1 | Required top-level files exist | workspace-structure | Fail | unconditional |
| 2 | Required directories exist | workspace-structure | Fail | unconditional |
| 3 | Each spec has YAML frontmatter | workspace-structure | Fail | unconditional |
| 4 | Each spec has Purpose/Specification/Validation sections | workspace-structure | Fail | unconditional |
| 5 | Provenance dirs follow NNN-title naming | workspace-structure | Fail | unconditional |
| 6 | Session log entry exists for each provenance dir | workspace-structure | Fail | unconditional |
| 7 | Each provenance dir has ≥1 .md file | methodology-kernel | Fail | unconditional |
| 8 | Provenance files have required frontmatter | workspace-structure | Fail | unconditional |
| 9 | Decision records include rejected alternatives | methodology-kernel | Warning | unconditional |
| 10 | No uncommitted changes to provenance files | workspace-structure | Warning | unconditional |
| 11 | Multi-agent ≥3 raw-output floor | MAD v2 #3 | Fail | session has ≥1 perspective file |
| 12 | Heterogeneous-participant schema well-formedness | MAD v2 #8 | Fail | session has manifests/ |
| 13 | Cross-model-claim honesty | MAD v2 #9 | Fail | cross_model: true AND check 12 PASS |
| 14 | Multi-agent trigger coverage (`d016_*` ↔ artefacts) | MAD v3 #1 | Fail | session ≥ 006 |
| 15 | Non-Claude trigger coverage (`d023_*` ↔ manifest) | MAD v3 #2 | Fail | session ≥ 006 AND check 12 PASS |
| 16 | Independent-claim evidence-pointer presence | MAD v4 schema | Fail | session ≥ 021 |
| 17 | Claude-output-in-training disclosure | MAD v4 schema | Fail | session ≥ 021 |
| 18 | OI-004 closure-retrospective well-formedness | MAD v4 closure | Fail | retrospective.md present |
| 19 | Non-Anthropic participant_organisation membership | MAD v4 closed-set | Fail | session ≥ 021 |
| 20 | Default-read per-file budget (8K hard / 6K soft) | read-contract §2 | Fail/Warn | session ≥ 022 |
| 21 | Archive-pack manifest integrity | read-contract §7 | Fail | archive/ present |
| 22 | Archive-pack citation consistency | read-contract §6 | Fail | archive/ present |
| 23 | MODE.md presence with recognised mode | workspace-structure §MODE.md | Fail | unconditional (engine-v7+) |
| 25 | Records-substrate integrity | records-contract §3 | Fail | session ≥ 058 |
| 26 | Honest-limit text repetition cluster detection (substrate-aware branch CHKD-2 evidence-consuming added v9 per S073 D-280 + §10.4-M33: digest-when-present consumed as evidence; grep-fallback when both digest and 00-assessment substrate-evidence absent per §Graceful Degradation). WARN at ≥3-cluster; FAIL at ≥6-cluster. | this spec §Tier 2.5 + §(z6) + S062 D-221 Layer 1 + S073 D-280 | Fail/Warn | session ≥ 063 |
| 27 | Cross-family reviewer audit. When Layer 2 trigger fires, verify `provenance/<NNN-session>/04-tier-2-audit.md` exists; verify required sections per §Tier 2.5 audit shape: frontmatter scope-coverage table; §1 trigger basis; §2 (α)-flag coverage; §3 substantive evidence with tripartite §3a/§3b/§3c distinction; §4 disposition table; §5 stale-item escalation; §6 reviewer metrics; §7 next-session-shape critique; §8 reviewer-cost note; verify bootstrap-limited-confidence label per Layer 6.5 when applicable; verify `reviewer_provider:` not `google` per v8 clause (d). **At v9 (Codex-S074-F4 close)**: full §1-§8 + tripartite §3a/§3b/§3c presence enforced (pre-v9 only §2+§7+scope-coverage+bootstrap-label were enforced; F4 was acknowledged as a continuing mechanism-adequacy gap deferred to S075+ per S074 close §7). | this spec §Tier 2.5 + S062 D-221 Layer 3 + S064 D-233 + S075 (γ-6) | Fail | session ≥ 063 AND Layer 2 trigger met |
| 28 | (z5) Validation-debt lifecycle integrity. Required fields, status enum, well-formed review_by_session, no stale-without-rationale rows. **At v7 (S064)**: ledger is authoritative-not-witness per §(z5) revised semantics; check 28 additionally verifies frontmatter `authoritative: true` declaration when ledger is read by Tier 2.5 reviewer. | this spec §(z5) Validation-Debt Lifecycle + S062 D-221 Layer 4 + S064 D-233 §10.4-M24 | Fail | session ≥ 063 AND ledger exists |
| 29 | Substrate-use evidence-probe (added engine-v13 Session 071 per D-264 (β)-phase). Inspects current session's `00-assessment.md` for `substrate_session_open: exercised \| unavailable \| skipped` + `substrate_evidence:` field presence (or prose declaration of substrate exercise/non-availability/skip); cross-checks `03-close.md` for mirror declaration when close-file present. WARN-only initially per S058 D-204 mechanism-rollout discipline. Per measurement-authority separation reframe (S071 §10.4-M28), structured declaration is `producer_kind: agent-declared` until backed by harness telemetry per (γ) phase-3 (z6) digest arc. | this spec §Tier 2.5 + S071 D-263 + S071 D-264 | Warn | session ≥ 071 AND current-session 00-assessment.md exists |

(Check 24 reserved-not-active per engine-v9 deferral.)

### Gating Conventions

**Presence-gating** (checks 11, 12, 13, 18, 21, 22, 27 sub-clause, 28 sub-clause): the check fires only when the relevant artefact exists.

**Session-number gating** with explicit constants in `validate.sh`:
- `TRIGGERS_MET_ADOPTION_SESSION=6` — checks 14, 15.
- `CRITERION4_ARTICULATION_SESSION=21` — checks 16, 17, 19.
- `READ_CONTRACT_ADOPTION_SESSION=22` — check 20.
- `RECORDS_CONTRACT_ADOPTION_SESSION=58` — check 25.
- `REVIEWER_AUDIT_ADOPTION_SESSION=63` — checks 26, 27, 28.
- `CHECK_29_ADOPTION_SESSION=71` — check 29.

**Substrate-aware fallback (check 26)**: `mcp__selvedge-retrieval__search` preferred when available per `retrieval-contract.md` v1; grep-based n-gram fallback otherwise. Per `multi-agent-deliberation.md` v4 §Graceful Degradation.

### Sequencing

Check 13 BLOCKED if check 12 fails. Check 14 BLOCKED if check 11 fails. Check 15 BLOCKED if check 12 fails. Check 27 BLOCKED if check 26 unavailable (substrate AND grep-fallback both unavailable); artefact-presence sub-clause runs independently.

### Honest Limits (mandatory inline documentation)

Each Tier 1 check with known-laundering surface carries an honest-limit comment block in `validate.sh` + inline NOTE in failure message + corresponding subsection in this specification. Divergence between any two of these three locations is a specification violation.

**Check 13 honest limit**: "This check verifies the session's claim is internally consistent with its manifests. It does not and cannot verify that the manifests' lineage claims are themselves true. Manifest truth relies on operator integrity and the `participant_selected_by` field's accountability." Tier 2 Q6 is the designed counter-pressure.

**Check 14 honest limit**: "This check verifies consistency between a decision's self-declared `triggers_met:` and the session's multi-agent artefacts. It does not and cannot verify that the `triggers_met:` declaration is itself a truthful classification of the decision against D-016. The declaration's truth relies on operator integrity and the `triggers_rationale:` field's adversarial visibility to Tier 2 review." Tier 2 Q7.

**Check 15 honest limit**: "This check verifies consistency between a decision's self-declared `d023_*` triggers and the session's non-Claude participant manifests. It does not verify that a manifest labeled non-Claude in fact represents a non-Claude participant nor that the substantive adequacy of any skip reason is genuine. The declaration's truth relies on operator integrity."

**Check 26 honest limit**: "This check verifies textual repetition of honest-limit content across the §2c retention-window's `03-close.md` files. It does not and cannot judge whether the repetition reflects genuine operational recurrence (legitimate) or ceremonial drift (the laundering surface that EF-058-tier-2-validation surfaces). The Tier 2.5 cross-family reviewer is the methodology's designed counter-pressure for the genuine-vs-ceremonial distinction."

**Check 27 honest limit**: "This check verifies that when the Layer 2 (γ) reviewer mechanism triggers, the session committed a `provenance/<NNN-session>/04-tier-2-audit.md` artefact AND its content satisfies the required-sections discipline per §Tier 2.5 audit shape. It does not and cannot verify that the audit's substantive findings are correct, that the disposition table accurately reflects the audit's reasoning, that the reviewer's family is genuinely non-Claude, or that the bootstrap-limited-confidence label (when present) is being honestly applied. The substrate-aware audit-quality assessment is Tier 2.5's reviewer-prompt + operator audit at resolving close (Layer 6) + Layer 6.5 bootstrap discipline."

**Check 28 honest limit**: "This check verifies that `validation-debt/index.md` table rows have required fields, valid status enum, well-formed review_by_session, frontmatter `authoritative: true` declaration when the ledger is in (z5) authoritative-not-witness mode (per v7), and no stale-without-rationale rows. It does not and cannot verify that items genuinely represent unresolved debt, that next_action descriptions are substantive, or that escalation_disposition rationales are non-formulaic. The Tier 2.5 reviewer + operator audit are the counter-pressures for substantive adequacy."

**Check 29 honest limit (added engine-v13 Session 071 per D-264)**: "This check verifies the session declares structured substrate-use evidence in 00-assessment.md + 03-close.md per the (ε) hybrid β-phase discipline adopted at S071 D-263. It does not and cannot verify that the declared substrate exercise actually occurred — `producer_kind: agent-declared` per the measurement-authority separation reframe (§10.4-M28). Until the (γ) phase-3 digest arc lands at S072+ with harness-measured fields per VD-003 gating conditions, structured declaration is self-report and check 29 is WARN-only. The (γ) digest is the methodology's designed counter-pressure for actual substrate-use verification."

### Tier 2: Guided Assessment

The validator prints these questions:

1. **Provenance continuity**: Did Read use prior provenance to understand past decisions? Were any past decisions re-proposed without acknowledgment?
2. **Specification consistency**: Are current specifications semantically consistent? Any contradictions or conflicting assumptions?
3. **Adversarial quality**: In deliberative work, did the adversarial perspective provide genuine challenge?
4. **Meaningful progress**: Is the methodology producing meaningful progress, or accumulating ceremony?
5. **Specification-reality alignment**: Are there specifications describing things that no longer exist, or things that exist without being specified?
6. **Cross-model-honesty evidence (paired with check 13)**.
7. **Trigger-coverage plausibility (paired with checks 14, 15)**.
8. **OI-004 closure-retrospective adequacy (paired with check 18)**.
9. **Read-contract adherence (paired with check 22)**.
10. **Layered-mechanism engagement (paired with checks 26, 27, 28)**: Verify (a) §8 honest-limits sections were authored deliberately, distinguishing genuine new gaps from recurrences; for recurrences, was the (z5) lifecycle ledger row updated rather than the close re-recording? (b) if Layer 2 (γ) triggered, did the reviewer's audit substantively engage with the session's claims (decisions + close + (α)-flagged items + tripartite distinction), or was the audit ceremonial? (c) if a (z5) lifecycle item was closed/deferred, was disposition substantive (concrete next action or escalation rationale) or formulaic? Flag instances where the structural mechanism passed Tier 1 mechanically but the underlying discipline is not engaged.

### Tier 2.5: Cross-Family Reviewer Discipline (revised v7 per S064 D-233; revised v8 per S074 D-288; extended v9 per S075 (γ-6))

**Trigger set.** Tier 2.5 triggers when ANY of the following conditions is met at session close:

- (a) **Engine-definition-touching** per OI-002 substantive-revision scope.
- (b) **Substantive-arc-class** per S048+ precedent.
- (c) **Layer 1 (α) WARN/FAIL emission** at close.
- (d) **Layer 4 (z5) lifecycle event**: any session that closes/defers a `validation-debt/index.md` item; or any session past which a lifecycle item's `review_by_session` lapses without re-disposition.
- (e) **Operator-discretionary**.

If none fires, Tier 2.5 is out-of-scope; orchestrator answers Tier 2 normally; no `04-tier-2-audit.md` artefact.

**Reviewer-family rule (revised v8 per S074 D-288 operator-directive; family-distinctness requirement REMOVED; google provider EXCLUDED)**:

The reviewer at session N-close MUST NOT be:
- (a) the session-N orchestrator (the agent that performed Read + Assess + Convene + Deliberate + Decide + Produce + Record + close-narrative-write activities); or
- (b) the close-author or primary implementer of the work being audited; or
- (c) the accountable doer for any decision being audited; or
- (d) **(NEW v8 per S074 D-288)** a member of the `google` provider family. The `google` provider is permanently excluded from reviewer roles per operator-directive at S074. Existing S063+S067+S071+S073 Gemini audit records remain valid as historical artefacts; no future reviewer-role invocation of google is permitted. Acceptable reviewer providers: any in `tools/validate.sh` PARTICIPANT_ORGANISATION_CLOSED_SET except `google` (operationally: `{anthropic, openai, local, other-named}` plus future-named providers).

**Family-distinctness requirement REMOVED at v8 per S074 D-288 operator-directive** (was v7: "The reviewer's family MUST differ from the orchestrator's family at the organisation level"). Reviewer family MAY now overlap with orchestrator/perspectives' family at the organisation level. Empirical basis: sustained Gemini findings_count=0 pattern across S063+S067+S071+S073 (n=4) + S073 codex cross-check on identical evidence packet produced findings_count=2 with substantive findings (see `engine-feedback/inbox/EF-073-gemini-excluded-and-reviewer-family-rule-relaxation.md` + `provenance/073-session/04-tier-2-audit-codex-cross-check.md`). Operator-directive: Claude and codex are operationally preferred reviewers despite family-overlap; family-overlap is permitted with mandatory `reviewer_overlap_with_recent_mad_perspectives:` field disclosure + counterweighting check (existing v7 disclosure discipline preserved verbatim below).

**Reviewer-overlap disclosure (preserved from v7; sole counter-pressure to family-overlap at v8)**: any reviewer-perspective overlap with recent MAD load-bearing claims, OR any orchestrator-reviewer family-overlap (orchestrator anthropic + reviewer anthropic; orchestrator openai + reviewer openai), MUST be disclosed in the `reviewer_overlap_with_recent_mad_perspectives:` field with explicit scope-handling: either (i) the overlapping load-bearing claim is excluded from audit scope, or (ii) the overlapping claim is counterweighted by an additional non-overlapping check (e.g., second reviewer from a different family; operator audit; substrate-mediated alternative validation). The `reviewer_provider:` field MUST NOT be `google` per (d) above.

**Prior MAD-perspective participation** is not by itself disqualifying (unchanged from v7). Same disclosure + counterweighting requirement applies per the v7 wording preserved verbatim above.

**Gaming modes the relaxed rule may open** (preserved per §10.4-M21):
- (i) Perspective-laundering at distance: labeling a favored reviewer as "only a perspective" then letting it validate its own synthesis-shaping contribution. Mitigation: load-bearing-claim disclosure required.
- (ii) Cross-family theater: satisfying family-level independence while keeping reviewer prompt-packet narrow. Mitigation: minimum-evidence-packet per audit shape below.
- (iii) Split-accountability evasion: orchestrator adopts another model's recommendation, then reviewer from same family certifies adoption as independent. Mitigation: accountable-doer clause (c) above.
- (iv) Multi-agent orchestration ambiguity: when multiple agents shared orchestration (e.g., TeamCreate). Mitigation at v7 was "reviewer-family must differ from any declared orchestrator-family"; at v8 per S074 D-288 family-distinctness is REMOVED, so mitigation is now "any orchestrator-reviewer family-overlap MUST be disclosed in `reviewer_overlap_with_recent_mad_perspectives:` field with counterweighting check per the v7 disclosure discipline preserved verbatim at v8". The `reviewer_provider:` field MUST NOT be `google` per clause (d) above.

**Fallback discipline**. When no acceptable provider is operationally available, the session MAY skip Tier 2.5 with explicit honest-limit recording per `multi-agent-deliberation.md` v4 §Graceful Degradation. Skip MUST record: substantive `reason:` + `retry_in_session:`.

**Reviewer audit shape (revised v7 per S064 D-233)**:

The reviewer produces `provenance/<NNN-session>/04-tier-2-audit.md` with the following frontmatter (additions to v6 marked **NEW**):

```yaml
---
session: <NNN>
title: Tier 2.5 Cross-Family Reviewer Audit — Session <NNN>
date: <YYYY-MM-DD>
status: complete
reviewer: <name/family>
reviewer_provider: <organisation per PARTICIPANT_ORGANISATION_CLOSED_SET>
reviewer_kind: <non-anthropic-model | human>
reviewer_overlap_with_recent_mad_perspectives: <none | <list of perspective-files this reviewer was a perspective in; if non-empty, scope-handling disclosed in §1>>
trigger_condition: <a | b | c | d | e | multiple>
session_under_review_subjects:
  - retention-window-closes: <list of 6 retention-window 03-close.md paths> # NEW v7: minimum-evidence-packet
  - validation-debt-ledger: validation-debt/index.md   # NEW v7
  - active-watchpoints: <list of active watchpoints from close §X>  # NEW v7
  - engine-feedback-inbox: engine-feedback/INDEX.md + inbox/  # NEW v7
  - open-issues: open-issues/index.md  # NEW v7
  - <other artefacts as required by trigger condition>
scope_coverage_table:  # NEW v7 per §10.4-M22 P1 audit-shape requirement
  retention-window-closes: <exercised | skipped + rationale>
  validation-debt-ledger: <exercised | skipped + rationale>
  active-watchpoints: <exercised | skipped + rationale>
  engine-feedback-inbox: <exercised | skipped + rationale>
  open-issues: <exercised | skipped + rationale>
findings_count: <integer>
findings_dispositioned: <integer>
duration_minutes: <integer>
reviewer_prompt_template_version: <integer; v1 at S063; v2 at S064 (locked in at S067 per (z7) n=2); v3 candidate at S075 per (γ-6) minimum-viable extension; lock-in-after-n=2 counter resets at v3>  # extended v9
harness_telemetry_digest_available: <true | false>  # NEW v9 per (γ-6) reviewer-prompt-template v3 minimum-viable extension
bootstrap_status: <none | limited-confidence>  # NEW v7 per Layer 6.5
---
```

Required sections (revised v7):

- **§1 Scope and trigger basis**. Which trigger fired; what artefacts read; if `reviewer_overlap_with_recent_mad_perspectives` is non-empty, scope-handling disclosed (excluded items OR counterweighting check).
- **§2 (α)-flag coverage**. If check 26 emitted no flags, "vacuous-by-scope".
- **§3 Substantive evidence (tripartite distinction per §10.4-M24)**. Three sub-evaluations:
  - **§3a Close correctness**: did the close narrative accurately record decisions, artefacts, and state? Citations to close §<N>, decisions, validator output.
  - **§3b Mechanism adequacy**: did the engine's mechanisms (Tier 2.5 + (z5) ledger + watchpoints + engine-feedback inbox + open-issues) function as designed at this session? Citations to specific mechanism instances.
  - **§3c Trajectory discipline**: is the engine's multi-session trajectory engaging with accumulated state, or accumulating ceremony? Citations to retention-window patterns; lifecycle ledger ledger-vs-narrative consistency.
- **§4 Disposition table**: per flagged item: source citation, disposition `accepted | disputed | deferred | resolved`, rationale.
- **§5 Stale-item escalation**: lifecycle items past review_by_session; reviewer confirms or escalates. **Per §10.4-M24 (z11) (z5) authoritative-not-witness**: any ledger-vs-narrative mismatch is a finding unless close explains why ledger is stale or superseded.
- **§6 Reviewer metrics**: overlap; findings_count (0 with substantive §3 acceptable per evidence-floor); findings_dispositioned; duration_minutes; harness-telemetry digest availability; reviewer_prompt_template_version.
- **§7 Next-session-shape critique (NEW v7 per S064 §10.4-M23 + P3's 5-condition test)**. The reviewer reads close's §7 next-session-recommendation and evaluates against 5 conditions:
  1. Open issues unprogressed across retention window.
  2. Engine-feedback inbox untriaged or repeatedly deferred items.
  3. Watchpoints stale, underspecified, or repeatedly carried forward without decision.
  4. Validation debt exists and next-session-recommendation does not explain why it can wait.
  5. Recent closes repeatedly recommend "watch" without operator agenda.
  
  If any of (1)-(5) is present, "Path A (Watch)" or equivalent default fires the reviewer's **disputed** disposition unless the close-narrative provides affirmative no-action justification (concrete reasoning why the active surface can wait + named re-evaluation trigger or session). If no condition fires, "Path A" is valid. Recorded in §4 disposition table.
- **§8 Reviewer cost note**: tokens or wall-clock minutes; comparison to prior triggered sessions if available; per WX-62-1 5-field recording.

**Evidence floor (not finding floor)** preserved per S062 D-221 §1.4 + P3 [`01c`, Q4] + P4 [`01d`, Q4]: reviewer audit with `findings_count: 0` AND substantive §3 (with tripartite distinction) IS passing. With empty/formulaic §3 IS NOT passing; check 27 fails.

**Reviewer self-report honest-limit (added v7 minor amendment per S071 D-264 + EF-067 Direction C from cross-family weighted convergence per S071 D-263 §2.6 of synthesis; extended at v7 minor amendment per S073 D-279 with REVD-2 quarantine semantics adoption)**. The audit-shape frontmatter fields `duration_minutes` + `reviewer_cost` (recorded per WX-62-1 5-field discipline at Layer 6.3) are **reviewer self-reports**, not harness-measured ground truth. Per EF-067 evidence chain at design-space §3.2 (S063 + S064 + S067 reviewer self-report propagation chain via reviewer-prompt-template baseline supplied to subsequent reviewers): self-reports anchor to the prior reviewer's self-report; no harness-measured ground truth ever enters the chain. **§10.4-M25 P1 audit-cost-budget threshold arithmetic on self-reported values is suspended** at S071 close per D-264 pending harness-measurement availability per the (γ) phase-3 (z6) digest arc per VD-003 lifecycle row + S072+ phase-3 design-space (Direction B subsumption per EF-067 cross-linkage with EF-059 (z6) extended scope; per measurement-authority separation reframe substantively adopted at S071 D-263 §5.1 of synthesis: Direction B fields will carry `producer_kind: harness-measured` distinguished from current `producer_kind: agent-declared` semantics). The cost-observation surface remains preserved with explicit caveat for cross-session pattern observation only (e.g., reviewer-cost trajectory may surface cadence-of-passivity signal even with imprecise absolute values; the §10.4-M25 P1 reopen-warrant text remains preserved as forward-observation discipline; the threshold arithmetic ("reviewer-cost growth >2× over S063 baseline") is suspended at S071 D-264 with this amendment).

**REVD-2 quarantine semantics extension (added v7 minor amendment per S073 D-279 + §10.4-M34 P4 z-laundering-1 reframe substantive adoption per `provenance/073-session/01-deliberation.md` §3.4)**. The (γ-6) staged hybrid adopted at S073 D-275 carries explicit quarantine semantics for the EF-067 reviewer self-report fields during the γ phase-3 implementation arc (S074-S076). Quarantine semantics: (a) self-report fields (`duration_minutes`, `reviewer_cost`) MUST be annotated with `producer_kind: agent-declared` + `authority_level: tertiary`; (b) self-report fields are explicitly excluded from §10.4-M25 P1 audit-cost-budget threshold arithmetic during quarantine; (c) harness-measured fields (`reviewer_invocation_wall_clock_seconds`, `reviewer_invocation_token_count`) are added in parallel via the (z6) digest schema at S074 phase-3.1 close; (d) reviewers may compare self-report-vs-harness-measured during quarantine for cross-session pattern observation, but threshold arithmetic operates only on harness-measured trajectory. REVD-3 retrospective re-baseline activates post-S076 VD-003 review when harness-measured baseline is established (n≥2 stable harness-measured observations at S074-S075); at REVD-3 the §10.4-M25 P1 threshold arithmetic re-activates against the harness-measured baseline; the current S063 self-report baseline (25 wall-clock minutes / ~45,000 tokens) is retired.

**(z7) Reviewer-prompt-template versioning + lock-in-after-n=2 (NEW v7 per S064 §10.4-M21+M22+M24 convergent reframe; extended v9 per S075 (γ-6) phase-3.1)**: reviewer-prompt-templates are workspace-adjacent operational instruments subject to iteration. The first triggered application at S063 used template v1 (ad-hoc per /tmp/s063-reviewer-prompt.md); S064 close used template v2 (revised per S064 D-233 audit shape); v2 locked in at S067 per (z7) n=2 (S064 + S067 successful applications). **v3 candidate** applies at S075 close per the minimum-viable extension above (digest-aware reviewer instructions + per-record producer_kind/authority_level distinction + REVD-2 quarantine semantics + capture-adapter metadata check). The lock-in counter resets at v3; v3 needs n≥2 successful applications before next revision (forecast S076-S077). Templates lock-in after n=2 successful applications; subsequent revision requires explicit deliberation surface (Path PD or Path AS-MAD-execution depending on scope) per the (z7) discipline.

### §(z5) Validation-Debt Lifecycle (authoritative-not-witness; revised v7 per S064 D-233 §10.4-M24)

**Location**. `validation-debt/index.md` at workspace root. Engine-adjacent.

**Authoritative semantics (NEW v7)**: the ledger is the **source-of-truth** for validation-debt lifecycle state. Frontmatter declares `authoritative: true`. Reviewer audits ledger as authoritative; close-narrative claims about debt MUST be checkable against ledger; ledger-vs-narrative mismatch is a Tier 2.5 finding unless close explains why ledger is stale or superseded with substantive rationale.

This is the (z11) reframe per P3 [`01c`, Q4]: "If the ledger is merely 'also read,' it becomes another record-not-engaged artefact." Per S058 records-substrate Substrate-N3.5 framing applied to (z5).

**Format**. Single markdown file with frontmatter + table of lifecycle items. Frontmatter:

```yaml
---
title: Validation-Debt Lifecycle Ledger
authoritative: true  # NEW v7
last-updated: <YYYY-MM-DD>
updated-by-session: <NNN>
---
```

Required fields per row (unchanged from v6): `id`, `introduced_session`, `owner_or_surface`, `next_action`, `review_by_session`, `status`, `escalation_disposition`. Status enum: `open | in-progress | resolved | deferred-with-rationale | escalated`.

**Lifecycle operations** unchanged from v6.

**Records-family promotion** deferred per S062 §10.4-M18.

### §(z6) Harness-Telemetry Digest (SCD-3 schema codified at v9 per S075 (γ-6) phase-3.1 implementation)

The (γ) reviewer's audit packet specification names the harness-telemetry-digest section as required input when telemetry is available. The digest is produced by a **capture-adapter** that observes substrate calls + tool calls + reviewer invocations during the session and writes a structured record consumable by `tools/validate.sh` check 26 (substrate-aware branch) + the Tier 2.5 reviewer.

**Location.** `provenance/<NNN-session>/harness-telemetry-digest.yaml`. Engine-adjacent (not part of `engine-manifest.md` §3 file set per `engine-manifest.md` §3 boundary rule for per-session provenance). Default-read by exclusion (not enumerated in `read-contract.md` v6 §1); read at session-scope by Tier 2.5 reviewer + check 26 + future digest consumers.

**Capture mechanisms (per S073 D-276 + S075 (γ-6) phase-3.1 implementation):**

- **CM1 — `tools/digest_emitter.py`** (Claude Code hooks PostToolUse). First capture-adapter; harness-measured authority. Configured in `.claude/settings.json` `hooks.PostToolUse`. Captures tool_name + truncated input_summary + status + ISO-8601 timestamp for every tool call; routes substrate calls (`mcp__selvedge-retrieval__*`) to the `substrate_calls:` section, other tools to `tool_calls:`. Each emitted record carries `producer_kind: harness-measured` + `authority_level: primary`.
- **CM3 — `tools/digest_reconstructor.py`** (post-hoc bridge/comparator). Secondary authority. Reads `00-assessment.md` frontmatter (`substrate_session_open`, `substrate_evidence`) + scans 00-assessment / 02-decisions / 03-close prose for substrate-tool mentions. Each reconstructed record carries `producer_kind: post-hoc-reconstructed` + `authority_level: secondary`. When the CM1 digest already exists, the reconstructor writes the comparator at `harness-telemetry-digest-cm3.yaml` (sibling) for cross-validation; otherwise writes the primary digest path.
- **CM2 — external telemetry wrapper.** Named portability end-state. Deferred to post-S076 review per VD-003 gating; activates when cross-harness-tool deployment becomes load-bearing.
- **CM4 — in-session agent-declared.** Explicitly excluded per §10.4-M28 + §10.4-M34. Schema field-level authority rules (below) prevent agent-declared records from being promoted to harness-measured solely through digest shape.

**SCD-3 schema (per S073 D-277 + §10.4-M34 P4 z-laundering-1 reframe substantive adoption).**

Frontmatter declares the **adapter's** capabilities; it does NOT declare authority for individual records. Per-record annotations are load-bearing.

```yaml
---
session: <NNN>
title: Harness-Telemetry Digest
schema_version: SCD-3
generated_at: <ISO-8601 UTC>
capture_adapter: <claude-code-hook | post-hoc-reconstruction | external-wrapper>
capture_adapter_version: <semantic version e.g. v1>
capture_capabilities:    # what this adapter observes
  - <field_name>
unobserved_fields:       # what this adapter cannot observe (portability disclosure)
  - <field_name>
# File-level frontmatter declares ADAPTER capabilities only. Each record below
# carries its own producer_kind + authority_level annotation; file-level header
# does NOT promote agent-declared records to harness-measured via shape alone.
---

substrate_session_open_declaration:    # mirrors 00-assessment.md frontmatter; carries the agent-declared shape explicitly
  declared_state: <exercised | unavailable | skipped | absent>
  evidence_summary: <prose ≤ 500 chars>
  producer_kind: agent-declared
  authority_level: tertiary

substrate_calls:    # invocations of mcp__selvedge-retrieval__* tools
  - tool_name: <e.g. mcp__selvedge-retrieval__forward_references>
    input_summary: <truncated; ≤ 240 chars>
    status: <success | error | unknown>
    timestamp_iso8601: <ISO-8601 UTC>
    producer_kind: <harness-measured | post-hoc-reconstructed | agent-declared>
    authority_level: <primary | secondary | tertiary>

tool_calls:         # non-substrate tool invocations
  - tool_name: <e.g. Edit, Bash, Write>
    input_summary: <truncated>
    status: <success | error | unknown>
    timestamp_iso8601: <ISO-8601 UTC>
    producer_kind: <harness-measured | post-hoc-reconstructed | agent-declared>
    authority_level: <primary | secondary | tertiary>

reviewer_invocations:  # (γ) Tier 2.5 reviewer launches at session close
  - reviewer_provider: <openai | anthropic | local | ...>   # NOT google per v8 clause (d)
    reviewer_kind: <codex | claude | other>
    timestamp_start: <ISO-8601 UTC>
    timestamp_end: <ISO-8601 UTC>
    wall_clock_seconds: <integer>           # producer_kind controls authority
    token_count: <integer or null>
    producer_kind: <harness-measured | post-hoc-reconstructed | agent-declared>
    authority_level: <primary | secondary | tertiary>
```

**Per-record authority semantics.** Per §10.4-M34 P4 z-laundering-1 reframe: a record's `producer_kind` is the load-bearing authority claim. Reviewer audits + check 26 + future digest consumers MUST consume `authority_level` per record (not infer from file-level frontmatter). Explicit non-promotion rule: `agent-declared` records CANNOT be promoted to `harness-measured` solely through digest shape (e.g., placing an agent-declared record under a CM1 file-level `capture_adapter: claude-code-hook` header does NOT promote it to primary authority).

**Reviewer availability (RAD-3 bridged transition per S073 D-278).** D2.1 (always-available-always-read) named end-state; D2.2 (available-at-best-effort) is the v9 default during (γ) rollout S075-S076. D2.1 hard-precondition activation gated to S076 VD-003 review if capture has demonstrated durability (n≥2 stable digest-bearing reviewer audits at S075-S076).

**Reviewer self-report quarantine (REVD-2 per S073 D-279 + §10.4-M34 P4 z-laundering-1 reframe).** During the (γ) phase-3 rollout window (S075-S076 inclusive), self-report fields (`duration_minutes`, `reviewer_cost` from the audit frontmatter) carry `producer_kind: agent-declared` + `authority_level: tertiary`. They are explicitly excluded from §10.4-M25 P1 audit-cost-budget threshold arithmetic during quarantine. Harness-measured fields (`reviewer_invocation_wall_clock_seconds`, `reviewer_invocation_token_count`) appear in the digest's `reviewer_invocations:` section in parallel — when an out-of-band capture wrapper is available; CM1 hooks do NOT capture these (the hook fires per tool-use, not per reviewer-launch). REVD-3 retrospective re-baseline activates post-S076 review when harness-measured reviewer-cost baseline established (n≥2 stable harness-measured observations); at REVD-3 the §10.4-M25 P1 threshold arithmetic re-activates against the harness-measured baseline and the S063 self-report baseline is retired.

**Check 26 substrate-aware branch (CHKD-2 evidence-consuming per S073 D-280 + §10.4-M33 P3 z9 reframe).** When `provenance/<current-session>/harness-telemetry-digest.yaml` exists, `tools/validate.sh` check 26 consumes it (counts `substrate_calls:` records; logs digest-presence) and proceeds with in-memory grep-based cluster detection over the §2c retention-window's `03-close.md` `§8` honest-limit lines. When digest absent, the grep fallback runs unchanged per `multi-agent-deliberation.md` v4 §Graceful Degradation. The validator does NOT call MCP at runtime per §10.4-M33; it consumes evidence produced at session-open by the orchestrator.

**Reviewer-prompt-template v3 minimum-viable extension (per S073 D-282 + (z7) lock-in-after-n=2; counter resets at v3 — v3 needs n≥2 successful applications before next revision).** Reviewers at v9 close MUST:

1. Inspect `provenance/<NNN-session>/harness-telemetry-digest.yaml` when present; record digest presence in §6 frontmatter `harness_telemetry_digest_available:` field (or §6 prose if frontmatter not extended).
2. When digest absent, name the absence as an honest-limit in §8 (or §X bootstrap section) — do not silently proceed.
3. Distinguish per-record `producer_kind` + `authority_level` when citing digest evidence in §3a/§3b/§3c. Treat `agent-declared` records as tertiary; treat `harness-measured` records as primary; treat `post-hoc-reconstructed` records as secondary cross-validation.
4. Apply REVD-2 quarantine semantics: do NOT cite reviewer self-report `duration_minutes` against §10.4-M25 P1 audit-cost-budget threshold arithmetic during the S075-S076 quarantine window. The §8 reviewer-cost note remains for cross-session pattern observation only.
5. Verify capture-adapter metadata coherence: when the digest's `capture_adapter:` claims `claude-code-hook` (CM1), the `unobserved_fields:` enumeration MUST include the fields the adapter cannot capture (e.g., `wall_clock_token_count`, `reviewer_invocation_wall_clock_seconds`); cross-check that no `harness-measured` records claim authority for unobserved fields.

Engine-v cadence summary (per S073 D-281 + S074 D-291 + S075 (γ-6) phase-3.1): S073 close = minor amendment to v7 codifying direction (engine-v13 preserved). S074 close = substantive v7 → v8 reviewer-family-rule revision per operator-directive (engine-v13 → engine-v14). **S075 close = substantive v8 → v9 codifying SCD-3 schema + audit-shape extension + check 27 §1-§8 + tripartite §3 enforcement + new tools/digest_emitter.py + tools/digest_reconstructor.py + check 26 substrate-aware branch (engine-v14 → engine-v15 ratified per S075 D-298).** S076 close = phase-3.2 minor extensions + VD-003 full review per VD-003 lifecycle row.

### §Bootstrap-Paradox Layered Handling (extended v7 with Layer 6.5)

Per S062 D-221 §2.1 Layer 6 + S064 D-233.

**Layer 6.1 — One-time operator audit at adoption sessions**. Per S062 + S063 + S064 closes.

**Layer 6.2 — Standing operator-audit cadence**. Every substantive-arc resolving close + every engine-version bump + operator-discretionary at any close. Recorded as honest-limit annotation at audited close OR same-day session-open annotation.

**Layer 6.3 — 3-session post-S063 observation window (WX-62-1)**. 5-field recording per session per S062 D-224.

**Layer 6.4 — Validator warning for unaudited validation-discipline changes**. Per check 27 sub-clause.

**Layer 6.5 — Bootstrap-limited-confidence labelling (NEW v7 per S064 D-233 + §10.4-M27 incorporated direction)**. When a session adopts revisions to the §Tier 2.5 mechanism itself, the (γ) reviewer audit at that session's close MUST carry an explicit `bootstrap_status: limited-confidence` field in its frontmatter + a §X "Bootstrap status" section disclosing:
- (a) the rules being audited under (i.e., the about-to-be-adopted vs the currently-active spec at session-open);
- (b) the conflict-disclosure status of reviewer (perspective overlap with this session's MAD if any);
- (c) a clear statement that the audit MUST NOT be cited as clean validation of the revised mechanism.

Layer 6.5 applies prospectively to any session that revises Tier 2.5 mechanism specs.

### Tool Location and Behavior

`tools/validate.sh` is read-only; produces structured pass/fail/warning report; prints Tier 2 questions; detects (γ) reviewer audit artefact at `provenance/<NNN-session>/04-tier-2-audit.md` per check 27; verifies required-sections per audit-shape; verifies bootstrap-limited-confidence label per Layer 6.5 when applicable; exits code 0/1 per Tier 1 failure presence.

### When to Run

- At session **start** during/after Read.
- After **Produce**.
- Before **Close**.
- **Before launching the (γ) reviewer at session close**: validator's check 26 output is reviewer's input for (α)-flag-coverage per check 27.

### Limitations

Automated structural checks verify form, not meaning. Passing all structural checks does not mean specifications are correct, provenance captures actual reasoning, decisions were well-considered, or the methodology is serving its purpose. See per-check honest limits above for specific gaming surfaces.

**Tier 2 self-assessment by the orchestrator** is the methodology's discipline for routine workspace claims per §Principled Asymmetry above. The pre-v6 limitation language ("known limitation, mitigated by making the questions explicit") was empirically falsified for claims about unresolved validation debt + substantive progress + engine-definition change + repeated warnings by the S051-S058 honest-limit chain; v6 replaced naming-as-mitigation with the structural mechanism.

**Tier 2.5 self-assessment by the cross-family reviewer** is bounded by reviewer-prompt design + evidence-floor + Layer 6 operator audit + Layer 6.5 bootstrap-limited-confidence labelling. The S063 first-instance produced operator audit findings disputing first-instance shape; v7 revises per those findings (rule scope; audit shape; tripartite distinction; Path-A challenge). Reviewer ability to launder remains; counter-pressures: check 27 + Q10 + Layer 6 + Layer 6.5.

**Operator-audit cadence drift** is the engine's outermost laundering surface per S062 §10.4-M16 reopen warrant (c).

**Substrate-led discipline (§10.4-M23) requires substrate-tooling** per `retrieval-contract.md` v1; advanced state-surface queries (e.g., automated "all watchpoints stale at session N" alerts) require additional tooling not in v7 scope. Mitigation: v7 encodes "substrate-aware retrieval when available" per §Graceful Degradation; advanced tooling deferred to follow-on arcs.

### §10 First-Class Minorities (Cross-Reference)

Five new minorities at S064 D-234, mirrored in `specifications/workspace-structure.md` v9 §10.4-M21 through §10.4-M25:

- **§10.4-M21 — P2 prompt-template-first / defer-spec-revision-to-S067+**. Position: minimum-viable response is reviewer-prompt-template extension at S064 + observation across WX-62-1 window. Substantive spec revision at S064 is precipitate against §10.4-M16 reopen warrant (b) sustained-pattern threshold (n≥3). Status at S064: rejected; preserved as standing reopen-warrant. Reopen warrants per §10.4-M21: (a) sustained-pattern threshold; (b) compact engine-v12 entry laundering; (c) bootstrap recurrence; (d) (z10-trigger) differential-trigger-set vindication.

- **§10.4-M22 — P1 two-session arc preferred**. Position: same-session adoption at S064 violates perspective-independence preservation per S062 deliberation §1.7 + S062+S063 reified two-session arc. S064 = MAD; S065 = phase-3 implementation. Status at S064: rejected per cross-family weighted convergence; preserved as standing reopen-warrant. Reopen warrants per §10.4-M22: (a) spec-text drift; (b) synthesizer-framing absorption; (c) phase-3 implementation flaw at S065+.

- **§10.4-M23 — P3 substrate-led reviewer-judged frame**. Position: Tier 2.5 is not "get a cross-family reviewer"; it is "force an independent-enough agent to inspect the right substrate surfaces against known failure modes." Status at S064: **substantively adopted** as v7 audit-shape direction. Preserved against future-arc rollback or narrowing into "use retrieval" framing. Reopen warrants per §10.4-M23: (a) reviewer-judges-without-substrate-input; (b) substrate-tooling gap blocks discipline; (c) reviewer-identity-magic recurrence.

- **§10.4-M24 — P3 (z11) (z5) authoritative-not-witness + (z12) explicit-Path-justification**. Position: (z5) ledger should be authoritative not witness; (z12) explicit Path-justification at every close. Status at S064: **adopted** in v7 (z11 incorporated into §(z5) authoritative semantics; z12 incorporated into prompts/development.md). Reopen warrants per §10.4-M24: (a) ledger-as-witness drift; (b) records-family promotion blocked by ledger maturity; (c) Path-justification omitted.

- **§10.4-M25 — P2 cadence-depth + P1 audit-cost-budget co-preservation**. Position (cadence-depth): engine-v11 → v12 at adjacent sessions (S063 + S064) with engine-v11 preservation depth 0 is first-of-record, approaching §5.4 cadence-runaway threshold. Position (audit-cost-budget): revised audit shape significantly increases reviewer cost; quality-laundering by budget-pressure is structural risk. Status at S064: **preserved as forward-observation discipline**. Reopen warrants per §10.4-M25: (a) engine-v13 at S065 fully activates §5.4 (status update at S071: engine-v13 ratified at S071 close per S071 D-265, NOT at S065; reopen warrant (a) does NOT fire); (b) reviewer-cost growth >2× over S063 baseline (status update at S071: per S071 D-264 the threshold arithmetic on self-reported values is suspended pending harness-measurement availability per (γ) phase-3 (z6) digest arc); (c) quality-laundering by budget-pressure observed in S065+ audits.

Six new minorities at S073 D-283 (engine-wide minority count: 54 → 60 at S073 close); full text mirrored in `specifications/workspace-structure.md` v9 §10.4-M30 through §10.4-M35:

- **§10.4-M30 — P1 (γ-1)/(γ-2) maximalist position dissent (S073)**. Maximal-scope γ phase-3 as structurally honest response to §10.4-M28 + §10.4-M29; rejected per cross-family weighted convergence on (γ-6); preserved as standing reopen-warrant.
- **§10.4-M31 — P2 (γ-3) minimum-viable position dissent (S073)**. Smallest-scope γ phase-3 discharging VD-003 gates; rejected per cross-family weighted convergence on (γ-6); preserved.
- **§10.4-M32 — P3 z8 portable-capture-adapter-contract reframe (S073; substantively adopted)**. Capture-adapter contract over CM1/CM2/CM3 implementations; CM2 named portability end-state. **Cross-family-originated-and-adopted-at-MAD-execution reframe-architecture pattern reified at n=5** (S058+S062+S064+S071+S073).
- **§10.4-M33 — P3 z9 validator-as-evidence-consumer reframe (S073; substantively adopted)**. validate.sh validates declared evidence; does NOT require live MCP substrate access at runtime.
- **§10.4-M34 — P4 z-laundering-1 measurement-authority-not-inherited-from-YAML-container reframe (S073; substantively adopted)**. Authority attaches per record/section, not file-level; agent-declared cannot be promoted to harness-measured via digest shape alone.
- **§10.4-M35 — P3 z10 + P4 z-laundering-2 staging-must-be-per-direction reframe (S073; consolidated; P3+P4 dual-originated; substantively adopted)**. Staged rollout requires per-direction disposition discipline; reopen-warrant-activation is not implementation-bundling.

Four new minorities at S071 D-266, mirrored in `specifications/workspace-structure.md` v9 §10.4-M26 through §10.4-M29:

- **§10.4-M26 — P1 full-(γ)-immediate position (Session 071)**. Position: full (γ) digest implementation as structural-correctness response; multi-session phase-3 arc per S062 D-220; engine-v13 at S072+ phase-3 close. Hybrid (ε) defers γ commitment; design-space §3.1 + §3.2 evidence chains operationally sufficient for γ commitment now. Status at S071: rejected per cross-family weighted convergence; preserved as standing reopen-warrant. Reopen warrants per §10.4-M26: (a) sustained substrate non-use post-β; (b) reviewer-cost-trajectory laundering recurrence; (c) operational tractability shift.

- **§10.4-M27 — P2 (γ)-deferral-criteria position (Session 071; partly absorbed)**. Position: (γ) scope precipitate per S062 §10.4-M16 P2 reopen warrant criteria; (z6)-specific surfaces lack n≥3 evidence; records-substrate phase-2/3 stabilisation pacing constraint. Status at S071: **partly absorbed** by (ε) hybrid synthesis; preserves threshold-for-phase-3-γ-activation question. Reopen warrants per §10.4-M27: (a) operator-audit cadence drops below 80% across 10-session window post-(γ); (b) (γ) capture mechanism portability friction blocks external-application engine load; (c) (z6) digest produces n≥3 sessions of measured behavior that diverges from spec-side expectation in ways β would have caught; (d) records-substrate phase-2/3 stalled because (γ) absorbed substantive-arc capacity.

- **§10.4-M28 — P3 measurement-authority-separation-as-load-bearing position (Session 071; substantively adopted; P4 endorsed)**. Position: digest records MUST distinguish `producer_kind: harness-measured | post-hoc-reconstructed | agent-declared` + `authority_level`. Without distinction, future sessions launder CM4 into γ via YAML shape alone. Status at S071: **substantively adopted** as phase-3 (γ) digest schema requirement per VD-003 lifecycle row gating. Preserved against future-arc rollback. Reopen warrants per §10.4-M28: (a) phase-3 (γ) digest spec adopted without producer_kind/authority_level fields; (b) CM4 entries treated as harness-measured-equivalent in any session's audit; (c) future MAD on related arc surfaces measurement-authority concern independently.

- **§10.4-M29 — P4 bundling-by-laundering audit position (Session 071; substantively adopted)**. Position: separate dispositions per direction prevents bundling-by-laundering; (γ) bundle risks combined cost looking inevitable because each part points at "harness measurement". Synthesis should preserve separate disposition for each: substrate habit correction (β-phase), immediate reviewer-cost caveat (Direction C now), separately scoped digest implementation (γ phase-3 arc). Status at S071: **substantively adopted** as (ε) hybrid composition. Preserved against future-arc bundling pressure. Reopen warrants per §10.4-M29: (a) phase-3 (γ) implementation adopts bundled-direction shape; (b) future MAD bundles related arcs without explicit per-direction cost analysis; (c) operator-audit at phase-3 close surfaces bundling-by-laundering finding.

Full minority text in `specifications/workspace-structure.md` v9 §10.4-M21 through §10.4-M29 (inclusive).

## Validation

To validate this specification:

1. Run `tools/validate.sh` and verify it performs the structural checks listed (1-23, 25, 26-28).
2. Verify the tool prints the ten guided questions.
3. Compare actual checks against the table; they should match.
4. Verify the tool is read-only and exits code 0/1 per Tier 1 failure presence.
5. Verify each check honest-limit subsection (13, 14, 15, 26, 27, 28) language matches the validate.sh comment block + failure message.
6. Verify check 13 BLOCKED for sessions where check 12 failed; check 14 BLOCKED if check 11 failed; check 15 BLOCKED if check 12 failed; check 27 BLOCKED if check 26 unavailable.
7. Verify session-number gating per constants.
8. Verify presence-gating per artefact for relevant checks.
9. Verify (γ) reviewer audit shape per §Tier 2.5 audit shape (frontmatter scope-coverage table + tripartite §3 + §7 next-session-shape critique + bootstrap-limited-confidence label when applicable) enforced by check 27.
10. Verify §Principled Asymmetry language is present.
11. Verify (z5) ledger frontmatter `authoritative: true` declaration is present per §(z5) authoritative-not-witness; check 28 verifies.
12. Verify Layer 6.5 language is present per §Bootstrap-Paradox Layered Handling.
13. Verify (z7) reviewer-prompt-template versioning + lock-in-after-n=2 discipline is present per §Tier 2.5.
