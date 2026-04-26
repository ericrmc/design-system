---
session: 073
title: Minimum-Viable Conservator — Session 073 phase-2 MAD response
date: 2026-04-26
status: complete
perspective: minimum-viable-conservator
committed_at: 2026-04-26T08:00:00Z
---

# Minimum-Viable Conservator

## Frame critique

The S073 problem statement is correctly scoped to the (γ) cross-product candidate selection, but the framing tilts toward presuming that VD-003 gating condition (a) "capture mechanism selection finalised" requires a *primary-authority* end-state commitment at S073. That conflates two distinct discharges: (i) finalising *which* capture mechanism the engine will adopt as its eventual primary-authority anchor, versus (ii) finalising *enough* of a capture mechanism stance to discharge the gating condition for phase-3 entry. The minimum-viable reading discharges (ii) without committing to (i): a CM3 post-hoc-reconstruction bridge with an explicit upgrade-warrant to CM1/CM2 satisfies VD-003 (a) at the lowest portability and implementation cost, while preserving the option to re-evaluate at the n=4-5 observation triangulation point (S074-S076).

Second, the design-space brief-extension §3a observation table — n=2 substrate-use observation points (S072 + S073 session-open both non-zero with high forward_references hit counts) — is *under-evidenced* for the question it is being asked to answer. Two sessions of compliance is consistent with both durable behavior change *and* design-space-salience compliance (the recursive Hawthorne-effect concern named at S071 §10.4-M27 and VD-003 lifecycle row gating condition (b)). The synthesis should resist treating §3a as load-bearing for selecting (γ-1)/(γ-2) maximal/default scopes; it is at most weak evidence that the β-phase spec-side discipline is not visibly failing, which is the precondition for *any* γ phase-3, not a warrant for maximal γ phase-3.

Third, the aggregate-budget pressure at S073 (91,571 / 90K soft, 1,571 over) is itself a design constraint pushing toward minimum-viable scope. Per `read-contract.md` v6 §2b, S073 MUST include an aggregate-reducing action. A maximal (γ-1) implementation candidate that ships a full SCD-3 schema + REVD-3 retrospective re-baseline + CHKD-1 check-26 substrate-aware branch + a substantive engine-v14 spec revision *adds* default-read load to the aggregate budget rather than reducing it. Minimum-viable γ scope (γ-3) is the only candidate that plausibly composes with an aggregate-reducing close-rotation in the same session.

Fourth, the framing of §10.4-M27 as "partly absorbed" at S071 should be read carefully: the (γ)-deferral-criteria *position* was partly absorbed by VD-003 gating-condition codification, but the *minimum-viable instinct* — that γ phase-3 when activated should ship at smallest scope discharging the gates — was not absorbed and remains live for S073. This perspective re-asserts that instinct.

## Q1 — capture mechanism preferred end-state

CMD-3 (CM3 post-hoc transcript-reconstruction only, as bridge with explicit upgrade-warrant to CM1/CM2 at S076 VD-003 review).

Reasoning: CM3 is the highest-portability mechanism (works offline, harness-agnostic, no Claude Code hook dependency, no external wrapper deployment). Its weakness — secondary-authority per §10.4-M28 measurement-authority separation — is *exactly* the property the producer_kind/authority_level schema fields were designed to surface honestly. CM3 + producer_kind: post-hoc-reconstructed + authority_level: secondary discharges VD-003 (a) without locking the engine into Claude-Code-specific tooling (CM1) or premature cross-harness wrapper engineering (CM2). At S076 review, with n=4-5 observation data and one or two implementation cycles of CM3 experience, the engine can re-evaluate whether the secondary-authority gap warrants CM1 or CM2 promotion. S071 D-263 framing already names "CM3 acceptable as bridge" — minimum-viable defends the bridge.

## Q2 — schema scope

SCD-2 (substrate_calls extension only).

Reasoning: SCD-2 extends the EF-059 (z6) digest with the single field most directly responsive to the β-phase observation question — substrate_calls — without committing to the full SCD-3 extended schema (read_invocations + files_read_at_session_open + decision_claims_with_evidence_pointers + reviewer_invocation_wall_clock_seconds + reviewer_invocation_token_count). SCD-3 collides with the records-substrate phase-2/3 pacing constraint preserved at S062 §10.4-M18 (SCD-4 records-substrate promotion deferred). The decision_claims_with_evidence_pointers field in particular is a substantial schema commitment that should not be made until the substrate-led-reviewer-judged frame (§10.4-M23) has been engaged on its own merits. SCD-2 is the smallest schema scope discharging VD-003 (c) "digest schema specification with producer_kind/authority_level finalised" — producer_kind/authority_level are top-level fields in SCD-2 just as in SCD-3.

## Q3 — reviewer availability discipline

RAD-2 (D2.2 available-at-best-effort).

Reasoning: RAD-1 (D2.1 always-available-always-read as hard precondition) is a meaningful escalation of the engine's session-open ceremony. It risks reviewer-availability outage cascading to session-blocking failure modes that the engine has not yet stress-tested. RAD-2 preserves reviewer operability — best-effort availability with graceful-degradation semantics — while still incentivising routine reviewer use. RAD-3 (bridged transition window) is plausible but adds an extra mechanism (the bridge) that is itself a pacing commitment we have no n>=2 evidence is needed. Minimum-viable defends RAD-2 with a reopen warrant: if at S076 n=4-5 observation reveals reviewer-availability gaps producing measurement holes, escalate to RAD-3 or RAD-1.

## Q4 — reviewer self-report disposition

REVD-2 (partial-deprecation: preserve `duration_minutes` + `reviewer_cost` self-report fields with producer_kind: agent-declared annotation).

Reasoning: REVD-1 full subsumption now is correct in principle (§10.4-M29 bundling-by-laundering audit motivates harness-measured replacement of self-reports) but premature in practice while CMD-3 post-hoc reconstruction is the bridge mechanism. Self-report fields with producer_kind: agent-declared + authority_level: tertiary continue to surface the data while honestly marking its provenance. REVD-3 (REVD-1 + retrospective re-baseline) is a substantial scope expansion that adds re-work cost without commensurate evidence value at n=2 observation. REVD-2 is the minimum-viable disposition that respects §10.4-M28 measurement-authority separation without paying REVD-1's full transition cost.

## Q5 — check 26 substrate-aware branch

CHKD-3 (defer substrate-aware branch to post-γ).

Reasoning: `tools/validate.sh` check 29 was added at S071 close as a WARN-only β-phase substrate-use evidence-probe. It is the right surface for substrate-use telemetry at S073. Adding a check 26 substrate-aware branch (CHKD-1) before n=4-5 observation data exists is premature — we don't yet know what failure modes the branch should fire on. CHKD-2 (light substrate-aware branch) is a middle path but spreads the validator-side spec change across two engine-v cycles. CHKD-3 keeps validator changes scoped to check 29's WARN-only probe through the γ phase-3 cycle and revisits at S076 with observation data. Defending the smallest validator-side spec footprint is core to the minimum-viable stance.

## Q6 — engine-v cadence

EVD-2 (two-step bump: engine-v14 minor at S073 capturing the SCD-2 schema + RAD-2 + REVD-2 commitments; substantive engine-v15 deferred to S074+ for the smaller-scope phase-3.2 implementation arc).

Reasoning: EVD-1 (single substantive engine-v14 bump at S073) overpacks the version transition with both schema commitment and full implementation, increasing rollback cost if S076 observation triangulation reveals problems. EVD-3 (defer engine-v bump to phase-3 close) defers ratification of the schema decision past the point where it becomes load-bearing for S074+ implementation. EVD-2 ratifies the schema + availability + self-report decisions at engine-v14 minor (lower preservation-depth cost) and reserves the substantive engine-v15 bump for an implementation cycle that has triangulation evidence behind it. This composes with `prompts/development.md` substantive-revision discipline and avoids the "substantive bump on under-evidenced commitments" failure mode.

## Q7 — reviewer-prompt-template extension scope

Minimum-viable reviewer-prompt-template extension: add the §[Substrate-use evidence probe] section instructing reviewers to perform Layer-1 substrate evidence checks (forward_references count + resolve_id anchor checks for decision claims with evidence pointers) and report findings_count. Defer the full substrate-led reviewer-judged frame extension (§10.4-M23) to the records-substrate phase-2/3 maturity window.

Reasoning: The reviewer-prompt-template was locked-in-after-n=2 at S067 D-246 (z7) lock-in discipline. Each substantive extension to the template carries lock-in cost. Minimum-viable extension surfaces the substrate-use evidence dimension reviewers most need to engage — the β-phase observation question — without committing to the broader substrate-led frame transformation. This pairs naturally with REVD-2 partial-deprecation: reviewer-prompt extends to *check* substrate use, not to *judge* the engine on substrate-led reframe terms.

## Q8 — bundle-vs-defer EF-068-read-write-rebalance

Defer per S069 D-255 separate-scope warrant. Address aggregate-budget pressure (91,571 / 90K soft, 1,571 over) via close-rotation alone (WX-28-1 forty-second close-rotation S066 OUT S073 IN, with retention-exception discipline if needed).

Reasoning: EF-068-read-write-rebalance is a meaningfully different scope than the (γ) capture mechanism + schema + availability + self-report cluster. Bundling it into S073 phase-2 MAD synthesis collides with three prior discipline commitments: (i) S069 D-255 operator-discretionary reopen warrant — the warrant is open but un-operator-surfaced; (ii) the periphrastic-form discipline reified at n=3 (S068 + S069 + S070) which is sensitive to keyword-heuristic over-fire on bundled scope; (iii) the third-of-record all-triaged-no-new engine-feedback state preserved at S071 — bundling an additional scope element risks reactivating new-state. Minimum-viable defends: aggregate-budget addressable via close-rotation; EF-068-read-write-rebalance reopen warrant remains operator-surfaced for a future session.

## Q9 — implementation-locus session-shape

Path L phase-3 implementation across S074-S075 same-session-bounded per S058 D-199 precedent for each step (not multi-session arc per S062 D-220 precedent, given minimum-viable scope's smaller substantive footprint).

Reasoning: With (γ-3) minimum-viable scope, the implementation cluster (CMD-3 post-hoc reconstruction tooling + SCD-2 schema codification + RAD-2 availability discipline + REVD-2 self-report annotation + minimum-viable reviewer-prompt extension) plausibly fits two same-session-bounded β-phase-style cycles rather than a multi-session γ phase-3.1/3.2/3.3 arc. Path L is preferred over Path AS because the design-space-then-decide discipline has been discharged at S072 design-space + S073 phase-2 MAD; the implementation arc need not re-enter design-space mode. S074 = CMD-3 + SCD-2 implementation; S075 = RAD-2 + REVD-2 + reviewer-prompt extension; S076 = VD-003 review with observation data.

## Q10 — cross-spec interaction depth

Substantive but smaller engine-v14 bump touching: `validation-approach.md` v7 → v8 (SCD-2 schema + RAD-2 availability + REVD-2 self-report annotation); `prompts/development.md` (β-phase + minimum-viable γ phase-3 step references); `tools/validate.sh` (check 29 stays WARN-only; no new checks). Other engine-definition specs (`methodology-kernel.md` v6, `multi-agent-deliberation.md` v4, `read-contract.md` v6, `records-contract.md` v1, `retrieval-contract.md` v1, `workspace-structure.md` v9) NOT touched.

Reasoning: The engine-v13 substantive amendment at S071 already rebalanced the spec cluster; engine-v14 should be a focused follow-on rather than a second cluster-wide rebalancing. Limiting cross-spec footprint to `validation-approach.md` + `prompts/development.md` keeps the preservation-depth cost low (engine-v13 entered S072 at depth 0, currently at depth 1 entering S073 — engine-v14 minor reset depth without crossing the engine-v9 preservation-depth-8 mark).

## Cross-product candidate position

Defend (γ-3) minimum-viable γ scope: CMD-3 + SCD-2 + RAD-2 + REVD-2 + CHKD-3 + EVD-2.

Reasoning across the cross-product: (γ-1) maximal scope overcommits on under-evidenced n=2 observation; (γ-2) (ε)-hybrid-default-scope is the median position the design-space brief tilts toward but does not address aggregate-budget pressure or records-substrate phase-2/3 pacing constraint; (γ-4) capture-mechanism-first staged is plausible but its CMD-1 phase-3.1 commits to Claude-Code-specific tooling on n=2 evidence; (γ-5) hybrid CMD-4 staged contradicts the design-space §3b explicit rejection of CM4. (γ-3) is the unique candidate that (i) discharges VD-003 (a)+(c) gating conditions, (ii) composes with aggregate-budget pressure via close-rotation, (iii) preserves records-substrate phase-2/3 pacing per §10.4-M18, (iv) honors the §10.4-M28 measurement-authority separation reframe via producer_kind/authority_level fields without committing to primary-authority end-state on n=2 evidence, (v) leaves the upgrade-warrant to CM1/CM2 + REVD-1 + SCD-3 + CHKD-1 explicitly open at S076 review.

The minimum-viable resolution chain: S073 ratify (γ-3) → S074-S075 implement → S076 VD-003 review with n=4-5 triangulation → re-evaluate upgrade-warrants with evidence.

## Honest limits

1. **Resolution-chain timing.** Minimum-viable defers the primary-authority commitment to S076 review. If S074-S075 implementation reveals that CM3 post-hoc reconstruction has higher implementation cost than estimated (reconstruction tooling has the medium-high implementation rating per §3b), the deferred CM1 commitment may turn out to have been the cheaper path and minimum-viable will have paid bridge-cost without bridge-value.

2. **Portability friction trade-off.** CM3 secondary-authority does not anchor §10.4-M28 measurement-authority semantics as strongly as CM1 primary-authority. The honest reading is that minimum-viable accepts a *softer* discharge of VD-003 (a) than (γ-1)/(γ-4) would provide. Reviewers who weight measurement-authority anchoring strongly may legitimately judge (γ-3) under-discharges the gate.

3. **n=2 observation under-evidence.** This perspective leans on the n=2 observation point being too thin to warrant maximal scope, but the same thinness undercuts confidence in *any* γ phase-3 selection. Minimum-viable's defense is "smallest commitment under thin evidence" not "no commitment under thin evidence."

4. **Records-substrate phase-2/3 pacing assertion.** §10.4-M18 SCD-4 records-substrate promotion was deferred at S062, but the precise pacing constraint (when does records-substrate phase-2/3 maturity arrive?) is not externally tracked with a session-bounded review point. SCD-2 vs SCD-3 distinction relies on this pacing constraint remaining load-bearing.

5. **EF-068-read-write-rebalance deferral.** Defending Q8 deferral assumes close-rotation alone closes the 1,571-word aggregate-budget gap. If the S073 close.md word count + reviewer audit puts aggregate further over soft, close-rotation may be insufficient and EF-068 may need to be re-engaged sooner than this position assumes.

6. **EVD-2 two-step cadence.** Two-step engine-v14 minor + engine-v15 substantive carries higher preservation-depth churn than EVD-1 single-bump. If S076 review concludes the schema commitments were correct, EVD-1 would have been more efficient; EVD-2's option-value comes from rollback capacity.

7. **Reviewer-prompt-template lock-in cost.** Adding even a minimum-viable substrate-use evidence-probe section to the template re-engages the lock-in-after-n=2 discipline. If the section needs revision at S076 based on observation evidence, lock-in cost compounds.

## Dissent-preservation

If synthesis adopts (γ-1) maximal / (γ-2) (ε)-hybrid-default / (γ-4) capture-mechanism-first-staged / (γ-5) hybrid CMD-4 staged:

**Minority warrant**: Preserve minimum-viable (γ-3) position as new first-class minority §10.4-M30 candidate. The minority warrant: γ phase-3 at maximal/default/staged scope risks (i) overcommitting on n=2 observation evidence; (ii) under-honoring the records-substrate phase-2/3 pacing constraint per §10.4-M18; (iii) increasing default-read aggregate load against `read-contract.md` v6 §2b pressure; (iv) compounding reviewer-prompt-template lock-in cost prematurely.

**Activation triggers** for reopening at S076 VD-003 review:
- (a) If n=4-5 observation triangulation reveals durable behavior change indistinguishable from design-space-salience compliance (the Hawthorne-effect concern), minimum-viable's "ship smallest, observe more" instinct is vindicated and the dissent activates as warrant for not escalating further.
- (b) If implementation cost of (γ-1)/(γ-2)/(γ-4)/(γ-5) at S074-S075 exceeds estimates by >50% relative to (γ-3) baseline, minimum-viable activates as rollback warrant.
- (c) If aggregate-budget pressure at S076 exceeds 92K, minimum-viable activates as evidence that γ phase-3 scope contributed to the pressure and a phase-3.2 retrenchment is warranted.

**Reopen warrants**:
- S076 VD-003 review per existing lifecycle.
- Operator-discretionary reopen per S069 D-255 precedent if CM3 post-hoc reconstruction tooling cost exceeds CM1 hook implementation cost on actual implementation evidence.
- Substrate-led reviewer-judged frame engagement per §10.4-M23: if a future session adopts the substrate-led frame, minimum-viable γ scope's compatibility with that frame (via SCD-2 substrate_calls field as the natural extension point) becomes a load-bearing argument.

The dissent should be preserved at first-class minority status, not absorbed into majority synthesis, because the minimum-viable instinct is structurally distinct from any of (γ-1)/(γ-2)/(γ-4)/(γ-5): it asserts a *pacing* claim about evidence-to-commitment ratio, not a *scope* claim about which specific elements to include.
