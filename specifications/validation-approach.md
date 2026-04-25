---
title: Validation Approach
version: 6
status: active
created: 2026-04-17
last-updated: 2026-04-26
updated-by-session: 063
supersedes: validation-approach-v5.md
---

# Validation Approach

## Purpose

This specification defines how the methodology validates itself: what is checked, how checks are organized, and what the checks can and cannot assure. It serves the methodology's self-hosting principle — a methodology that cannot verify its own specifications cannot evolve reliably.

**Scope notes (Session 009 D-056 + Session 017 D-074).** This specification covers **Workspace validation** as defined in `methodology-kernel.md` v6 §7. Domain validation (the second sense of §7) is performed by domain-actors outside this specification's scope. The Tier 1 / Tier 2 / Tier 2.5 (added v6) discipline applies equally to self-development and external-problem applications of the Selvedge engine.

**Version history.** v6 (Session 063 per D-228) is a substantive revision adopting the layered structural mechanism decided at S062 D-221 in resolution of `engine-feedback/inbox/EF-058-tier-2-validation-discipline-by-distinct-agent.md`. v6 adds three new Tier 1 checks (26, 27, 28), one new Tier 2 question (Q10), and three new sections: §Tier 2.5 Cross-Family Reviewer Discipline (Layer 2), §(z5) Validation-Debt Lifecycle (Layer 4), §Bootstrap-Paradox Layered Handling (Layer 6). The §Limitations naming-as-mitigation language for Tier 2 self-assessment is replaced with structural-mechanism reference + the principled-asymmetry articulation per S062 D-221 §2.2 + §10.4-M17. v6 supersedes v5 (`validation-approach-v5.md`). Earlier versions: v5 (S022 D-084) added checks 20-22 + Q9; v4 (S021 D-082) added checks 16-19 + Q8; v3 (S006) added checks 14-15 + Q7; v2 (S005) added checks 11-13 + Q6.

## Specification

### Multi-Tier Model (extended v6)

Validation has three tiers (extended from two at v5).

**Tier 1: Structural Checks** are automated checks run by `tools/validate.sh`. They verify that the workspace's files conform to the formats and conventions defined in other specifications. Necessary but not sufficient for methodology health.

**Tier 2: Guided Assessment** is a set of questions printed by the validation tool for the agent or human conducting the session to consider. These questions address properties that cannot be checked mechanically.

**Tier 2.5: Cross-Family Reviewer Discipline (added v6)** is a triggered cross-family review at session close per the layered structural mechanism of S062 D-221. Scope is constrained to claims requiring stateful or distinct judgement per the Principled Asymmetry below. The reviewer is non-Claude family per `multi-agent-deliberation.md` v4 §Heterogeneous-Participant Recording Schema; produces `provenance/<NNN-session>/04-tier-2-audit.md`; gated on the trigger set in §Tier 2.5 below. Tier 2.5 supplements Tier 2; does not replace it.

### Principled Asymmetry (added v6 per S062 D-221 §2.2 + §10.4-M17)

The methodology exhibits a principled asymmetry between MAD-level deliberation (synthesizer-must-not-have-been-perspective per `multi-agent-deliberation.md` v4 §Synthesis) and session-close validation (Tier 2 historically self-assessed by orchestrator). The boundary, per S062 P4 [`01d-perspective-cross-family-reviewer.md`, Q2] convergent synthesis:

- **Routine workspace checks may remain self-assessed** (Tier 2 Q1-Q9). The aliasing risk for these is bounded by Tier 1 + next-session Read + operator-discretionary audit.
- **Claims about unresolved validation debt, substantive progress, engine-definition change, and repeated warnings require stateful or distinct review.** These surfaces exhibit noticing-failure (writer misses pattern in own writing — operationally falsified at S051-S058 honest-limit chain) which compounds across sessions in a way that aliasing-failure (synthesizer collapses divergent perspectives) does not. Stateful review = cross-session pattern detection (Layer 1 check 26); distinct review = cross-family reviewer (Tier 2.5).

The MAD §Synthesis prohibition is alias-prevention; Tier 2.5 is noticing-failure-mitigation. Both serve cross-perspective integrity but address different failure modes (per S062 P2 [`01b`, Q2] articulation).

### Tier 1: Structural Checks

| # | Check | Source | Severity | Gate |
|---|-------|--------|----------|------|
| 1 | Required top-level files exist | workspace-structure | Fail | unconditional |
| 2 | Required directories exist | workspace-structure | Fail | unconditional |
| 3 | Each spec has YAML frontmatter with required fields | workspace-structure | Fail | unconditional |
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
| 26 | **Honest-limit text repetition (added v6)**: cross-session §8 honest-limit text-cluster detection over §2c retention-window 03-close.md files. Substrate-aware (`mcp__selvedge-retrieval__search`) preferred; grep-based fallback per §Graceful Degradation. WARN at ≥3-cluster; FAIL at ≥6-cluster. | this spec §Tier 2.5 + S062 D-221 Layer 1 | Fail/Warn | session ≥ 063 |
| 27 | **Cross-family reviewer audit (added v6)**: when Layer 2 trigger fires (engine-def-touching OR substantive-arc OR check 26 WARN/FAIL OR (z5) lifecycle event OR operator-discretionary), verify `provenance/<NNN-session>/04-tier-2-audit.md` exists AND its content names every check 26 WARN/FAIL emitted at this close (silent omission of (α) flags fails). | this spec §Tier 2.5 + S062 D-221 Layer 3 | Fail | session ≥ 063 AND Layer 2 trigger met |
| 28 | **(z5) Validation-debt lifecycle integrity (added v6)**: verify `validation-debt/index.md` rows have required fields, valid status enum, well-formed review_by_session; no rows past review_by_session without escalation_disposition rationale. | this spec §(z5) Validation-Debt Lifecycle + S062 D-221 Layer 4 | Fail | session ≥ 063 AND ledger exists |

(Check 24 was reserved at engine-v9 for retrieval-substrate validation but deferred per D-171; the gap is intentional.)

### Gating Conventions

**Presence-gating** (checks 11, 12, 13, 18, 21, 22, 27 sub-clause, 28 sub-clause): the check fires only when the relevant artefact exists.

**Session-number gating** with explicit constants in `validate.sh` per S006 D-039 precedent (avoid ambiguity-of-absence + bypass-by-omission):
- `TRIGGERS_MET_ADOPTION_SESSION=6` — checks 14, 15.
- `CRITERION4_ARTICULATION_SESSION=21` — checks 16, 17, 19.
- `READ_CONTRACT_ADOPTION_SESSION=22` — check 20.
- `RECORDS_CONTRACT_ADOPTION_SESSION=58` — check 25.
- `REVIEWER_AUDIT_ADOPTION_SESSION=63` — checks 26, 27, 28 (added v6).

**Closed-set extension discipline.** PARTICIPANT_ORGANISATION_CLOSED_SET extension requires named decision in session's `02-decisions.md` + same-session constant update. Routine provider additions are minor validator-data updates not triggering engine-version bump; substantive additions changing what counts as criterion-4-eligible are substantive.

**Substrate-aware fallback (check 26).** Substrate-aware path: invoke `mcp__selvedge-retrieval__search` over §2c retention-window with §8 honest-limit text fragments; emit WARN/FAIL per cluster threshold. Substrate availability detected via `.cache/retrieval.db` mtime + `.mcp.json` presence per `retrieval-contract.md` v1. Grep-based fallback: tokenise §8 honest-limit text per close; compute n-gram similarity (≥4-token shared sequences); emit WARN/FAIL per cluster threshold. Fallback is documentary-equivalent for honest-limit-text-repetition; substrate-aware preferred for cross-paraphrase robustness. Per `multi-agent-deliberation.md` v4 §Graceful Degradation: when preferred path unavailable, document the degradation, use the fallback, do not skip.

### Sequencing

Check 13 BLOCKED if check 12 fails. Check 14 BLOCKED if check 11 fails. Check 15 BLOCKED if check 12 fails. Check 27 BLOCKED if check 26 unavailable (substrate AND grep-fallback both unavailable); artefact-presence sub-clause runs independently.

### Honest Limits (mandatory inline documentation)

Each Tier 1 check that has a known-laundering surface carries an honest-limit comment block in `validate.sh` directly above the check + an inline NOTE in the check's failure message + a corresponding subsection in this specification. Divergence between any two of these three locations is a specification violation.

**Check 13 honest limit**: "This check verifies the session's claim is internally consistent with its manifests. It does not and cannot verify that the manifests' lineage claims are themselves true. Manifest truth relies on operator integrity and the `participant_selected_by` field's accountability." Known gaming modes per D-029 (Session 005): value-flipping; `unknown` laundering; paper-human classification; wrapper impersonation. Tier 2 Q6 is the designed counter-pressure.

**Check 14 honest limit**: "This check verifies consistency between a decision's self-declared `triggers_met:` and the session's multi-agent artefacts. It does not and cannot verify that the `triggers_met:` declaration is itself a truthful classification of the decision against D-016. The declaration's truth relies on operator integrity and the `triggers_rationale:` field's adversarial visibility to Tier 2 review." Known false-compliance per D-040 (Session 006): under-declaration; mono-perspective launder; strawman positions; fabricated load-bearing claim. Tier 2 Q7 is the designed counter-pressure.

**Check 15 honest limit**: "This check verifies consistency between a decision's self-declared `d023_*` triggers and the session's non-Claude participant manifests. It does not verify that a manifest labeled non-Claude in fact represents a non-Claude participant (that is check 13's consistency scope) nor that the substantive adequacy of any skip reason is genuine (a Tier 2 concern). The declaration's truth relies on operator integrity." Known false-compliance per D-040: mislabeled manifest; bogus skip annotation; pattern of skips.

**Check 26 honest limit (added v6)**: "This check verifies textual repetition of honest-limit content across the §2c retention-window's `03-close.md` files. It does not and cannot judge whether the repetition reflects genuine operational recurrence (legitimate) or ceremonial drift (the laundering surface that EF-058-tier-2-validation surfaces). The Tier 2.5 cross-family reviewer is the methodology's designed counter-pressure for the genuine-vs-ceremonial distinction." Anticipated false-compliance: paraphrase evasion (substrate-aware variant mitigates); splitting across sections (check scope is §8 honest-limits only); reset-by-numbering; genuine recurrence (reviewer is responsible for distinguishing).

**Check 27 honest limit (added v6)**: "This check verifies that when the Layer 2 (γ) reviewer mechanism triggers, the session committed a `provenance/<NNN-session>/04-tier-2-audit.md` artefact AND its content names every check 26 WARN/FAIL emitted at this session's close. It does not and cannot verify that the audit's substantive findings are correct, that the disposition table accurately reflects the audit's reasoning, or that the reviewer's family is genuinely non-Claude. The substrate-aware audit-quality assessment is Tier 2.5's reviewer-prompt + operator audit at resolving close (Layer 6)." Anticipated false-compliance: vacuous audit; (α)-flag-coverage by acknowledgment-only; Layer-2-trigger evasion.

**Check 28 honest limit (added v6)**: "This check verifies that `validation-debt/index.md` table rows have required fields, valid status enum membership, and well-formed review_by_session values. It does not and cannot verify that the items genuinely represent unresolved debt, that next_action descriptions are substantive, that owner_or_surface assignments are appropriate, or that escalation_disposition rationales are non-formulaic. The Tier 2.5 reviewer + operator audit are the counter-pressures for substantive adequacy." Anticipated false-compliance: stale-not-escalated; formulaic disposition; phantom item.

### Tier 2: Guided Assessment

The validator prints these questions for the assessor:

1. **Provenance continuity**: Did Read use prior provenance to understand past decisions? Were any past decisions re-proposed without acknowledgment?
2. **Specification consistency**: Are current specifications semantically consistent? Any contradictions or conflicting assumptions?
3. **Adversarial quality**: In deliberative work, did the adversarial perspective provide genuine challenge or concede too easily?
4. **Meaningful progress**: Is the methodology producing meaningful progress, or accumulating ceremony?
5. **Specification-reality alignment**: Are there specifications describing things that no longer exist, or things that exist without being specified?
6. **Cross-model-honesty evidence (paired with check 13)**: Name the concrete evidence — invocation transcript, CLI command, wall-clock gap, human presence — distinguishing genuine non-Claude from edited-manifest. (Skip if not cross-model.)
7. **Trigger-coverage plausibility (paired with checks 14, 15)**: For each `**Triggers met:**` decision, state whether the declared triggers are consistent with content. For any `**Non-Claude participation:** skipped` annotation, state whether reason is substantive and `retry_in_session:` credible. Flag mismatches and weak reasons.
8. **OI-004 closure-retrospective adequacy (paired with check 18)**: For each row marked frame-replacement-or-novel-mechanism in `oi-004-retrospective.md`, verify the cited synthesis section actually contains a non-Claude-originated reframing (not paraphrase). For the P4 assertion, verify cited divergence shows synthesis adopted a position contradicting (or substantively augmenting) Claude consensus, not merely supplementing. (Skip if no retrospective present.)
9. **Read-contract adherence (paired with check 22)**: Verify (a) §1 default-read enumeration was followed at session open; (b) any archive-surface records cited via `[archive: path]` convention; (c) any non-reads of relevant archive records declared in honest-limits with the gap they leave. Flag silent skips and witness-dumping (WX-22-1).
10. **Layered-mechanism engagement (added v6; paired with checks 26, 27, 28)**: Verify (a) §8 honest-limits sections were authored deliberately, distinguishing genuine new gaps from recurrences (for recurrences, was the lifecycle ledger row updated rather than the close re-recording the same text?); (b) if Layer 2 (γ) triggered, did the reviewer's audit substantively engage with the session's claims, or was the audit ceremonial?; (c) if a (z5) lifecycle item was closed/deferred, was disposition substantive (concrete next action or escalation rationale) or formulaic? Flag instances where the structural mechanism passed Tier 1 mechanically but the underlying discipline is not being engaged. The mechanism's value depends on engagement-quality, not artefact-presence.

### Tier 2.5: Cross-Family Reviewer Discipline (added v6 per S062 D-221 Layer 2)

**Trigger set.** Tier 2.5 triggers when ANY of the following conditions is met at session close:

- (a) **Engine-definition-touching** per OI-002 substantive-revision scope: any session that revises an engine-definition file enumerated in `engine-manifest.md` §3, ratifies an engine-version increment, or adds/removes engine-definition files.
- (b) **Substantive-arc-class** per S048+ precedent: any session that resolves an `engine-feedback/inbox/EF-*` substantive-arc record, executes Path AS / Path AS-MAD-execution / Path AS Shape-1, or completes a phase of a multi-session substantive arc.
- (c) **Layer 1 (α) WARN/FAIL emission**: any session where check 26 emits WARN (≥3-cluster) or FAIL (≥6-cluster) at close.
- (d) **Layer 4 (z5) lifecycle event**: any session that closes (status: resolved) or defers (status: deferred-with-rationale) a `validation-debt/index.md` lifecycle item; or any session past which a lifecycle item's `review_by_session` lapses without explicit re-disposition.
- (e) **Operator-discretionary**: any session where the operator surfaces a request for cross-family review.

If none fires, Tier 2.5 is out-of-scope; orchestrator answers Tier 2 normally; no `04-tier-2-audit.md` artefact.

**Reviewer family.** Non-Claude family per `multi-agent-deliberation.md` v4 §Heterogeneous-Participant Recording Schema. Acceptable provider organisations: any value in `tools/validate.sh` PARTICIPANT_ORGANISATION_CLOSED_SET excluding `anthropic`. Manifest records `participant_kind: non-anthropic-model` (or `human`).

**No-recent-perspective-overlap rule.** The reviewer at session N-close MUST NOT have been a perspective in any MAD whose decisions are being audited at session N-close (analogous to MAD §Synthesis synthesizer-identity rule). The rule applies prospectively from S064+ onward; **at S063 (the first triggered application + the spec-adoption session), the rule does not apply** because the only available cross-family perspective at S062 was codex/GPT-5.5 (P3 + P4), and the rule cannot be self-satisfying at the bootstrap. Layer 6 (operator audit at S063 close + observation window from S064+) substitutes for the rule's purpose at S063.

**Fallback discipline.** When no acceptable non-Claude provider is operationally available at session close (codex CLI broken; Gemini CLI not yet integrated; no human reviewer present), the session MAY skip Tier 2.5 with explicit honest-limit recording per `multi-agent-deliberation.md` v4 §Graceful Degradation. Skip MUST record: substantive `reason:` + `retry_in_session:`. Repeated skips across consecutive triggered sessions raise §10.4-M16 reopen warrant (b) operational-insufficiency.

**Reviewer audit shape.** The reviewer produces `provenance/<NNN-session>/04-tier-2-audit.md` with required frontmatter (`session`, `reviewer`, `reviewer_provider`, `reviewer_kind`, `reviewer_overlap_with_recent_mad_perspectives`, `trigger_condition`, `findings_count`, `findings_dispositioned`) + required sections:

- §1 Scope and trigger basis (which trigger fired; what artefacts read).
- §2 (α)-flag coverage (substantive engagement with each check 26 WARN/FAIL emitted; if no flags, "vacuous-by-scope").
- §3 Substantive evidence (citations to close §<N>, decisions D-NNN, validator output, lifecycle ledger rows; quote-over-paraphrase for load-bearing claims).
- §4 Disposition table (per flagged item: source citation, disposition `accepted | disputed | deferred | resolved`, rationale).
- §5 Stale-item escalation (lifecycle items past review_by_session at this close; reviewer confirms or escalates).
- §6 Reviewer metrics (overlap; findings_count; findings_dispositioned; duration_minutes; harness-telemetry digest availability).
- §7 Harness-telemetry digest (when available; else cite EF-059 deferred-implementation per Layer 5).
- §8 Reviewer cost note (tokens or wall-clock minutes; comparison to prior triggered sessions if available; per WX-62-1 5-field recording).

**Evidence floor (not finding floor).** Per S062 D-221 §1.4 + P3 [`01c`, Q4] + P4 [`01d`, Q4] convergent synthesis: a reviewer audit with `findings_count: 0` and a substantive §3 + (α)-flag-coverage IS passing. A reviewer audit with `findings_count: 0` and an empty/formulaic §3 IS NOT passing; check 27 fails on (α)-flag-coverage; operator audit detects the laundering. Mandatory-finding-floor was rejected per "incentivises weak findings."

### §(z5) Validation-Debt Lifecycle (lightweight) (added v6 per S062 D-221 Layer 4)

**Location.** `validation-debt/index.md` at workspace root. Engine-adjacent (required by engine; implementation-not-engine-definition per `engine-manifest.md` §3 boundary, analogous to `tools/validate.sh`).

**Format.** Single markdown file with table of lifecycle items. Required fields per row:

- `id`: `VD-NNN` format; append-only numbering; no reuse.
- `introduced_session`: session number where debt was first surfaced.
- `owner_or_surface`: who or what is responsible. Acceptable: person/role identifier; "this session's reviewer"; "engine-feedback record EF-NNN".
- `next_action`: substantive description (not formulaic "review again").
- `review_by_session`: session number by which next_action should be re-evaluated.
- `status`: `open | in-progress | resolved | deferred-with-rationale | escalated`.
- `escalation_disposition`: rationale text; required when status is `deferred-with-rationale` or `escalated`; "n/a" when `open`/`in-progress`/`resolved`.

Status enum + review_by_session lapse without escalation_disposition rationale fail check 28.

**Lifecycle operations.** Introduce (when check 26 WARN/FAIL OR operator-surfacing OR §8 honest-limit names new gap; reviewer at introducing session verifies row well-formedness). Update (next_action progresses; status changes; review_by_session reached; append-only edits with git history). Close (status → resolved; escalation_disposition → "n/a" or closure rationale citing resolving decision; Layer 2 trigger (d) fires). Defer (status → deferred-with-rationale; substantive rationale required; trigger (d) fires). Escalate (review_by_session lapsed without progress, owner unavailable, or scope exceeds engine; status → escalated; escalation_disposition names target).

**Records-family promotion deferred.** Per S062 §10.4-M18: lightweight markdown-table is initial implementation. Records-family promotion (`records/validation-debt/` per `records-contract.md` v1 phase-N) deferred to post-records-substrate phase-2/3 stabilisation. Activation: (a) repeated honest-limit recurrence across 3 sessions without status update; (b) lifecycle item dispositioned-without-rationale; (c) reviewer-cannot-identify-debt from ledger.

### §(z6) Harness-Telemetry Digest (specified-deferred) (added v6 per S062 D-221 Layer 5)

The (γ) reviewer's audit packet specification names the harness-telemetry-digest section as **required input when telemetry is available**. Digest content per S062 D-221 §2.1 Layer 5: failed tool calls, retries, repeated reads by file path, fallback route-around events, anomalous command patterns.

**Implementation deferred** per S062 D-225 EF-059 (`engine-feedback/inbox/EF-059-harness-telemetry-feed-for-tier-2-reviewer.md`) with named activation preconditions: (a) reviewer mechanism adopted at S063; (b) reviewer operating across ≥3 sessions per WX-62-1; (c) ≥1 instance documented where digest would have caught failed-tool-call or repeated-Read pattern given digest access. Triage scheduled ≥S066.

When telemetry is not available at a triggered session, the reviewer's §7 records "Harness-telemetry digest not available; EF-059 deferred-implementation."

### §Bootstrap-Paradox Layered Handling (added v6 per S062 D-221 Layer 6)

The MAD that decided the Tier-2.5 mechanism (S062) is itself a Tier-2.5-validation surface; the session that adopts the spec (S063) is the first triggered application of the rule it adopts. Per S062 D-221 §2.1 Layer 6, the paradox is handled via four mechanisms:

**Layer 6.1 — One-time operator audit at adoption sessions.** S062 close: operator audited the MAD's findings + direction; received "agrees with findings and direction chosen; proceed." S063 close: operator audits spec adoption + reviewer's first audit + (z5) lifecycle bootstrap.

**Layer 6.2 — Standing operator-audit cadence.** Operator audit solicited at: every substantive-arc resolving close + every engine-version bump + operator-discretionary at any close. Recorded as honest-limit annotation at audited close (when audit happens during close-write) or same-day session-open annotation (when audit happens between close and next-session-open).

**Layer 6.3 — 3-session post-S063 observation window (WX-62-1).** Watchpoint opens at S062 close per D-224; recording obligation begins at first post-S063-adoption triggered close. Window = 3 successful triggered applications (not 3 calendar sessions; only triggered count). 5-field recording per session: `reviewer_invoked` (yes-cross-family | yes-Claude-fallback | no-not-triggered | no-skipped); `reviewer_findings_count` (integer; 0 with rationale acceptable); `reviewer_cost` (tokens | wall-clock minutes); `findings_dispositioned` (count + table by category); `reviewer_finding_substantive` (operator-graded yes | no | unaudited). Window-closes outcome: mechanism-functioning-per-intent (continue, convert to standing observation); engine-conventional-no-findings-ceremony (§10.4-M16 reopen warrant (b) fires); high-cost-low-value (warrant (a) re-evaluation); missing-what-operator-audit-catches (warrant (b) explicit firing).

**Layer 6.4 — Validator warning for unaudited validation-discipline changes.** At sessions where check 27 detects validation-approach.md edit (or any spec edit substantively touching Tier 2 / Tier 2.5 / (z5) / (z6) machinery), the validator additionally checks for either an `04-tier-2-audit.md` artefact OR a §8 honest-limit annotation referencing operator audit. Absence of both fires WARN. (Bundled into check 27 implementation.)

### Tool Location and Behavior

`tools/validate.sh` is read-only; produces structured pass/fail/warning report; prints Tier 2 questions; detects (γ) reviewer audit artefact at `provenance/<NNN-session>/04-tier-2-audit.md` per check 27; exits code 0 if no Tier 1 failures, code 1 otherwise. Dependencies: standard Unix tools (bash 3.2+, grep, sed, awk) + git + optional substrate per `retrieval-contract.md` v1 (substrate-aware variant of check 26 falls back to grep).

### When to Run

- At session **start**, during/after Read.
- After **Produce**, to check new artifacts.
- Before **Close**, as final coherence check.
- **Before launching the (γ) reviewer at session close** (added v6): the validator's check 26 output is the reviewer's input for (α)-flag-coverage per check 27.

### Limitations

Automated structural checks verify form, not meaning. Passing all structural checks does not mean specifications are correct, provenance captures actual reasoning, decisions were well-considered, the methodology is serving its purpose, cross-model participation is genuine (check 13 honest limit), trigger declarations are truthful (checks 14/15 honest limits), evidence pointers truthful (check 16 honest limit in `validate.sh`), training-overlap disclosures truthful (check 17), retrospective content well-grounded (check 18; Tier 2 Q8), participant_organisation values factual (check 19), default-read budgets reflect file relevance (check 20), archive-pack content was the right artefact (check 21), citation supports the citing claim (check 22; Tier 2 Q9), honest-limit text repetition reflects ceremonial drift vs genuine recurrence (check 26 honest limit; Tier 2.5 reviewer is counter-pressure), reviewer audit content is substantive (check 27 honest limit; Layer 6 operator audit is counter-pressure), or (z5) lifecycle items represent genuine debt (check 28 honest limit; reviewer + operator audit are counter-pressures).

These deeper questions are the purpose of Tier 2 + Tier 2.5 (added v6), which depend on judgement.

**Tier 2 self-assessment by the orchestrator** is the methodology's discipline for routine workspace claims per §Principled Asymmetry above. The pre-v6 limitation language ("known limitation, mitigated by making the questions explicit and recording the assessment in provenance" + "further mitigated since Session 005 by the D-023 non-Claude-participation rule for meta-deliberations on self-assessment mechanisms") was empirically falsified for claims about unresolved validation debt + substantive progress + engine-definition change + repeated warnings by the S051-S058 honest-limit chain; v6 replaces naming-as-mitigation with the structural mechanism (Tier 2.5 + check 26 + (z5) lifecycle ledger + Layer 6 bootstrap-paradox handling) for those surfaces.

**Tier 2.5 self-assessment by the cross-family reviewer** is bounded by reviewer-prompt design + evidence-floor (vs mandatory-finding-floor) + Layer 6 operator audit at resolving close. Reviewer ability to launder is checked by check 27 + Q10 + Layer 6.

**Operator-audit cadence drift** is the engine's outermost laundering surface per S062 §10.4-M16 reopen warrant (c): if cadence drifts below 80% of qualifying sessions across a 10-session window, the engine has no internal cross-check.

The immutability check (check 10) is a basic heuristic; comprehensive immutability verification across git history is a potential future improvement.

Check 12 verifies key-presence not value-correctness (D-030 archival choice). Checks 13-15 are consistency-of-self-report not truthfulness; Tier 2 Q6/Q7 are designed counter-pressures. Checks 26-28 are structural-mechanism-engagement-discipline not substantive-quality verification; Tier 2 Q10 + (γ) reviewer + Layer 6 operator audit are designed counter-pressures.

### §10 First-Class Minorities (Cross-Reference) (added v6)

The S062 EF-058-tier-2-validation MAD preserved five first-class minorities, mirrored in `specifications/workspace-structure.md` v8 §10.4-M16 through §10.4-M20:

- **§10.4-M16 — P2 minimum-viable-response**. Position: minimum-viable response is (α) + (z1) operator-audit channel formalisation + asymmetry articulation; larger structural mechanism reserved for n≥3 sustained-pattern evidence. Status: rejected at S062; preserved as standing reopen-warrant. Reopen warrants per §10.4-M16: (a) sustained-pattern n=3; (b) adopted-direction operational insufficiency vs (α)+(z1); (c) operator-audit cadence drift below 80%; (d) records-substrate phase-N maturity → (z5) records-family promotion.

- **§10.4-M17 — P2 principled-asymmetry-articulation**. Position: regardless of direction adopted, v6 MUST articulate principled asymmetry. **Status at S063: adopted** — §Principled Asymmetry above incorporates requirement directly. Reopen warrant (a) articulation absence: now-satisfied at S063 close.

- **§10.4-M18 — P3 z5 lifecycle-ledger as required**. Position: EF-058 is fundamentally a validation-debt liveness problem; lifecycle tracking required at first adoption. **Status at S063: adopted** as Layer 4 (lightweight; records-family promotion deferred). Reopen warrants per §10.4-M18: (a) repeated honest-limit recurrence 3 sessions without lifecycle update; (b) lifecycle item dispositioned-without-rationale; (c) reviewer-cannot-identify-debt from packet.

- **§10.4-M19 — P3 z6 harness-telemetry-digest before raw-transcript**. Position: harness telemetry first as structured digest before raw-transcript review. **Status at S063: specified-deferred** via Layer 5 + EF-059. Reopen warrants per §10.4-M19: (a) failed-tool/repeated-Read operator-surface as discipline-gap; (b) reviewer-cost from raw-transcript noise; (c) anomalous-pattern absence in workspace artefacts.

- **§10.4-M20 — P1 δ-γ tiered routing required if narrower path adopted**. Position: δ-γ with tiered routing operationally-justified scope; narrower paths leave structural-prevention surface incomplete. **Status at S063: substantively adopted** as v6 direction. Reopen warrants per §10.4-M20: (a) honest-limit text drift recurs in 3-session window post-S062; (b) operator-surfaced Q4-laundering instance recurs; (c) cross-family availability becomes structurally reliable (universal R2 reconsidered).

Full minority text in `specifications/workspace-structure.md` v8 §10.4-M16 through §10.4-M20.

## Validation

To validate this specification:

1. Run `tools/validate.sh` and verify it performs the structural checks listed (1-23, 25, 26-28; check 24 reserved-not-active per engine-v9 deferral).
2. Verify the tool prints the ten guided questions (Q1-Q10).
3. Compare actual checks against the table; they should match.
4. Verify the tool is read-only and exits code 0/1 per Tier 1 failure presence.
5. Verify each check honest-limit subsection (13, 14, 15, 26, 27, 28) language matches the validate.sh comment block + failure message.
6. Verify check 13 BLOCKED for sessions where check 12 failed; check 14 BLOCKED if check 11 failed; check 15 BLOCKED if check 12 failed; check 27 BLOCKED if check 26 unavailable.
7. Verify session-number gating per constants: checks 14/15 ≥ S006; checks 16/17/19 ≥ S021; check 20 ≥ S022; check 25 ≥ S058; checks 26/27/28 ≥ S063.
8. Verify check 11/12/13/18 presence-gating per artefact; check 27 sub-clause Layer 2 trigger condition presence-gating; check 28 sub-clause `validation-debt/index.md` presence-gating.
9. Verify (γ) reviewer audit shape per §Tier 2.5 enforced by check 27 (artefact-presence + (α)-flag-coverage); operator audit at resolving close is substantive-quality counter-pressure.
10. Verify §Principled Asymmetry language is present (added v6 per S062 D-221 §2.2 + §10.4-M17).
