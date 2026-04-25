---
title: Validation Approach
version: 7
status: active
created: 2026-04-17
last-updated: 2026-04-26
updated-by-session: 064
supersedes: validation-approach-v6.md
---

# Validation Approach

## Purpose

This specification defines how the methodology validates itself: what is checked, how checks are organized, and what the checks can and cannot assure. It serves the methodology's self-hosting principle — a methodology that cannot verify its own specifications cannot evolve reliably.

**Scope notes (Session 009 D-056 + Session 017 D-074).** This specification covers **Workspace validation** as defined in `methodology-kernel.md` v6 §7. Domain validation is performed by domain-actors outside this specification's scope. The Tier 1 / Tier 2 / Tier 2.5 discipline applies equally to self-development and external-problem applications of the Selvedge engine.

**Version history.** v7 (Session 064 per D-233) is a substantive revision adopting operator audit findings from S063 resolving close + cross-family MAD synthesis at S064. v7 revises the §Tier 2.5 reviewer-family rule (relaxed from "no perspective in audited MAD" to "not orchestrator/close-author/primary-implementer/accountable-doer + cross-family at family + audit-scope-conditional family exclusion when self-validating own load-bearing claim"); revises the audit shape to require minimum-evidence-packet (retention-window closes + (z5) lifecycle ledger + active watchpoints + engine-feedback inbox + open-issues); adds §7 Next-session-shape critique with P3's 5-condition affirmative-no-action-justification test; revises §(z5) Validation-Debt Lifecycle to make ledger **authoritative-not-witness**; adds tripartite audit distinction (close correctness / mechanism adequacy / trajectory discipline); adds Layer 6.5 bootstrap-limited-confidence labelling; adds (z7) reviewer-prompt-template versioning + lock-in-after-n=2 discipline. Five new first-class minorities preserved §10.4-M21 through M25 (engine-wide 45 → 50). v6 supersedes per immutability discipline. v6 (Session 063 per D-228) added §Tier 2.5 + §(z5) + §Bootstrap-Paradox + §Principled Asymmetry + checks 26+27+28 + Q10. v5-v1 history preserved per workspace-structure.md spec-versioning.

## Specification

### Multi-Tier Model

Validation has three tiers.

**Tier 1: Structural Checks** are automated checks run by `tools/validate.sh`. Verify form, not meaning.

**Tier 2: Guided Assessment** are questions printed by the validation tool for the agent or human conducting the session.

**Tier 2.5: Cross-Family Reviewer Discipline** is a triggered cross-family review at session close per the layered structural mechanism of S062 D-221, revised at S064 D-233 per operator audit findings. The reviewer is non-Claude family; produces `provenance/<NNN-session>/04-tier-2-audit.md`; gated on the trigger set in §Tier 2.5 below. Tier 2.5 supplements Tier 2; does not replace it.

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
| 26 | Honest-limit text repetition cluster detection (substrate-aware preferred / grep-fallback). WARN at ≥3-cluster; FAIL at ≥6-cluster. | this spec §Tier 2.5 + S062 D-221 Layer 1 | Fail/Warn | session ≥ 063 |
| 27 | Cross-family reviewer audit. When Layer 2 trigger fires, verify `provenance/<NNN-session>/04-tier-2-audit.md` exists; verify required sections per §Tier 2.5 audit shape (frontmatter scope-coverage table; §1 trigger basis; §2 (α)-flag coverage; §3 substantive evidence with tripartite distinction; §4 disposition table; §5 stale-item escalation; §6 reviewer metrics; §7 next-session-shape critique; §8 reviewer-cost note); verify bootstrap-limited-confidence label per Layer 6.5 when applicable. (Sub-clauses revised v7.) | this spec §Tier 2.5 + S062 D-221 Layer 3 + S064 D-233 | Fail | session ≥ 063 AND Layer 2 trigger met |
| 28 | (z5) Validation-debt lifecycle integrity. Required fields, status enum, well-formed review_by_session, no stale-without-rationale rows. **At v7 (S064)**: ledger is authoritative-not-witness per §(z5) revised semantics; check 28 additionally verifies frontmatter `authoritative: true` declaration when ledger is read by Tier 2.5 reviewer. | this spec §(z5) Validation-Debt Lifecycle + S062 D-221 Layer 4 + S064 D-233 §10.4-M24 | Fail | session ≥ 063 AND ledger exists |

(Check 24 reserved-not-active per engine-v9 deferral.)

### Gating Conventions

**Presence-gating** (checks 11, 12, 13, 18, 21, 22, 27 sub-clause, 28 sub-clause): the check fires only when the relevant artefact exists.

**Session-number gating** with explicit constants in `validate.sh`:
- `TRIGGERS_MET_ADOPTION_SESSION=6` — checks 14, 15.
- `CRITERION4_ARTICULATION_SESSION=21` — checks 16, 17, 19.
- `READ_CONTRACT_ADOPTION_SESSION=22` — check 20.
- `RECORDS_CONTRACT_ADOPTION_SESSION=58` — check 25.
- `REVIEWER_AUDIT_ADOPTION_SESSION=63` — checks 26, 27, 28.

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

### Tier 2.5: Cross-Family Reviewer Discipline (revised v7 per S064 D-233)

**Trigger set.** Tier 2.5 triggers when ANY of the following conditions is met at session close:

- (a) **Engine-definition-touching** per OI-002 substantive-revision scope.
- (b) **Substantive-arc-class** per S048+ precedent.
- (c) **Layer 1 (α) WARN/FAIL emission** at close.
- (d) **Layer 4 (z5) lifecycle event**: any session that closes/defers a `validation-debt/index.md` item; or any session past which a lifecycle item's `review_by_session` lapses without re-disposition.
- (e) **Operator-discretionary**.

If none fires, Tier 2.5 is out-of-scope; orchestrator answers Tier 2 normally; no `04-tier-2-audit.md` artefact.

**Reviewer-family rule (revised v7 per S064 D-233 + §10.4-M21 P2 gaming-warnings preserved)**:

The reviewer at session N-close MUST NOT be:
- (a) the session-N orchestrator (the agent that performed Read + Assess + Convene + Deliberate + Decide + Produce + Record + close-narrative-write activities); or
- (b) the close-author or primary implementer of the work being audited; or
- (c) the accountable doer for any decision being audited.

The reviewer's family MUST differ from the orchestrator's family at the organisation level per `tools/validate.sh` PARTICIPANT_ORGANISATION_CLOSED_SET (orchestrator anthropic → reviewer organisation outside `{anthropic}`; orchestrator openai → reviewer outside `{openai}`).

**Prior MAD-perspective participation** is not by itself disqualifying. It becomes disqualifying when the reviewer is asked to independently validate its own load-bearing claim from that prior MAD, in which case the overlap MUST be disclosed in the reviewer audit's `reviewer_overlap_with_recent_mad_perspectives:` field with explicit scope-handling: either (i) the load-bearing claim is excluded from audit scope, or (ii) the load-bearing claim is counterweighted by an additional non-overlapping check (e.g., second reviewer; operator audit; substrate-mediated alternative validation).

**Gaming modes the relaxed rule may open** (preserved per §10.4-M21):
- (i) Perspective-laundering at distance: labeling a favored reviewer as "only a perspective" then letting it validate its own synthesis-shaping contribution. Mitigation: load-bearing-claim disclosure required.
- (ii) Cross-family theater: satisfying family-level independence while keeping reviewer prompt-packet narrow. Mitigation: minimum-evidence-packet per audit shape below.
- (iii) Split-accountability evasion: orchestrator adopts another model's recommendation, then reviewer from same family certifies adoption as independent. Mitigation: accountable-doer clause (c) above.
- (iv) Multi-agent orchestration ambiguity: when multiple agents shared orchestration (e.g., TeamCreate). Mitigation: orchestrator-family declared at session-open; reviewer-family must differ from any declared orchestrator-family.

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
reviewer_prompt_template_version: <integer; v1 at S063; v2 at S064; lock-in-after-n=2 per (z7)>  # NEW v7
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

**(z7) Reviewer-prompt-template versioning + lock-in-after-n=2 (NEW v7 per S064 §10.4-M21+M22+M24 convergent reframe)**: reviewer-prompt-templates are workspace-adjacent operational instruments subject to iteration. The first triggered application at S063 used template v1 (ad-hoc per /tmp/s063-reviewer-prompt.md); S064 close uses template v2 (revised per S064 D-233 audit shape). Templates lock-in after n=2 successful applications; subsequent revision requires explicit deliberation surface (Path PD or Path AS-MAD-execution depending on scope).

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

### §(z6) Harness-Telemetry Digest (specified-deferred, unchanged from v6)

The (γ) reviewer's audit packet specification names the harness-telemetry-digest section as required input when telemetry is available. Implementation deferred per S062 D-225 EF-059 with named activation preconditions.

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

- **§10.4-M25 — P2 cadence-depth + P1 audit-cost-budget co-preservation**. Position (cadence-depth): engine-v11 → v12 at adjacent sessions (S063 + S064) with engine-v11 preservation depth 0 is first-of-record, approaching §5.4 cadence-runaway threshold. Position (audit-cost-budget): revised audit shape significantly increases reviewer cost; quality-laundering by budget-pressure is structural risk. Status at S064: **preserved as forward-observation discipline**. Reopen warrants per §10.4-M25: (a) engine-v13 at S065 fully activates §5.4; (b) reviewer-cost growth >2× over S063 baseline; (c) quality-laundering by budget-pressure observed in S065+ audits.

Full minority text in `specifications/workspace-structure.md` v9 §10.4-M21 through §10.4-M25.

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
