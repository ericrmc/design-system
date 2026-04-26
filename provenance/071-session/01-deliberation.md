---
session: 071
title: Synthesis — phase-2 MAD on three-record joint-scope (EF-067 + EF-059 + EF-068-substrate-load-bearing); 4-perspective two-family deliberation
date: 2026-04-26
status: complete
synthesizer: Case Steward (Claude Opus 4.7 1M context)
synthesizer_role: orchestrator-not-perspective per multi-agent-deliberation.md v4 §Synthesis synthesizer-identity rule
participants_family: cross-model
cross_model: true
non_claude_participants: 2
oi004_qualifying_participants: [outsider-frame-completion, cross-family-reviewer-laundering-audit]
---

# Synthesis — Session 071 phase-2 MAD

## §1 Synthesis approach

This synthesis maps the four perspectives' positions on Q1-Q10 + cross-product candidate selection + frame critiques + dissent-preservation. It does NOT decide; the Decide activity at `02-decisions.md` operates on this synthesis.

Synthesis discipline per `multi-agent-deliberation.md` v4 §Synthesis: claims attributing a position to a perspective cite source file and section/question via `[source-file, §X]` or `[source-file, Q#]`; synthesizer-original claims marked `[synth]`; quote over paraphrase for load-bearing claims; preserve dissent (majority/minority structure reported explicitly); convergence vs coverage distinction; alphabetical perspective ordering for synthesis (cross-family-reviewer-laundering-audit / harness-discipline-architect / incrementalist-conservator / outsider-frame-completion).

Cross-family weighted convergence per S058 D-199 + S062 D-220 precedent: 3-of-4 across-families adoption signal triggers same-session-bounded adoption OR multi-session phase-3 arc per direction adopted; below threshold preserves design-space + names follow-on phase-2 MAD or phase-3 shape.

## §2 Per-question synthesis

### §2.1 Q1 — Harness-side-enforcement vs spec-side-encouragement balance

**Convergence at 4-of-4 across families on the unifying frame**: spec-side encouragement is empirically insufficient for the cross-session-state-claim surfaces named in the three-record joint-scope. All four perspectives accept design-space §4.2's framing.

**Divergence on shift magnitude**: P1 favors decisive shift (`[01a-perspective-harness-discipline-architect.md, Q1]`: "the engine should shift decisively from spec-side-encouragement-only to harness-side-additional"). P2+P3+P4 favor targeted shift bounded by evidence-floor (`[01b-perspective-incrementalist-conservator.md, Q1]`: "partial harness-shift, not full"; `[01c-perspective-outsider-frame-completion.md, Q1]`: "Shift to harness-side enforcement for cross-session-state claims, not for everything"; `[01d-perspective-cross-family-reviewer-laundering-audit.md, Q1]`: "Shift to harness-side measurement, but do not collapse all surfaces into one enforcement jump").

**Cross-family weighted convergence**: 3-of-4 across families (P2+P3+P4) on targeted shift; cross-family signal (Claude P2 + codex P3 + codex P4). [synth] The targeted-shift framing — harness-side measurement for the three-record cross-session-state-claim surfaces, not generalised — is the operative direction.

### §2.2 Q2 — Minimum-viable per S062 §10.4-M16 P2 precedent vs full architectural shift

**Divergence**: P1 full architectural shift (`[01a, Q2]`: "(γ) full architectural shift via candidate. Minimum-viable response leaves Q1+Q4+Q5+Q6 underdetermined"). P2+P3+P4 minimum-viable-with-staged-extension (`[01b, Q2]`: "minimum-viable first; (γ) reserved for n≥3 sustained-pattern evidence on (z6)-specific surfaces"; `[01c, Q2]`: "Minimum viable is necessary but not sufficient... staged resolution: adopt a bounded β-like step immediately, but treat it as phase 1 of ε"; `[01d, Q2]`: "Minimum viable first, full root-cause arc second").

**Cross-family weighted convergence**: 3-of-4 across families (P2+P3+P4) on staged response. Cross-family signal preserved.

[synth] P3 + P4's framing extends P2's: bounded immediate correction (β-class) + multi-session arc for (γ) with named gating conditions. This is more progressive than P2's "defer (z6) entirely" position; P3+P4 commit to (γ) as target while gating implementation. P1's "full architectural shift" position is the principled-load-bearing-correctness stance; the cross-family majority's hybrid position is the principled-staged-correctness stance.

### §2.3 Q3 — Load-by-default vs preserve-deferred-tools-friction

**Convergence at 4-of-4 across families on load-by-default**. All four perspectives endorse `.mcp.json` load-by-default change per design-space §7 Q3 quantitative input (~1000 tokens trivial against ~200K context-window budget) (`[01a, Q3]`; `[01b, Q3]`; `[01c, Q3]`; `[01d, Q3]`).

[synth] Unanimous. The empirical n→0 substrate use chain at design-space §3.1 + the friction-differential at session-open-habit-forming-moment (per EF-068 intake §Observation point 2) decisively close the discoverability-via-friction defense.

### §2.4 Q4 — (z6) scope breadth

**Divergence on scope breadth**: P1 + P3 + P4 favor extended scope (failed-tool-call + repeated-Read + reviewer-cost + orchestrator-side telemetry). P2 favors failed-tool-call only IF (γ) adopted; defer (z6) entirely otherwise.

**Convergence on measurement-authority separation reframe** (P3-originated; P4-endorsed): `[01c, Q4]`: "I would narrow one item from design-space §5.4: `decision_claims_with_evidence_pointers` is not purely harness telemetry. The harness can measure that a decision cited a spec section or ledger row; it cannot measure that the citation was substantively adequate. That field should be typed as 'declared evidence pointer inventory,' not as ground truth."

P4 cross-family endorsement at `[01d, Q4]`: "'included in target schema' and 'hard precondition for every Tier 2.5 audit immediately' should be separated. D2.2 available-at-best-effort is the correct initial posture while the capture mechanism is proved. D2.1 always-available-always-read becomes appropriate only after the digest is generated by a mechanism that is not primarily agent-mediated."

[synth] P3's measurement-authority separation reframe is a load-bearing reframe per the cross-family-originated-and-adopted-at-MAD-execution reframe-architecture pattern (S058 Substrate-N3.5 + S062 z5+z6 + S064 substrate-led + z11 + z12 — pattern reified at n=3; this S071 reframe extends to n=4).

The reframe: digest records carry `producer_kind: harness-measured | post-hoc-reconstructed | agent-declared` + `authority_level` semantic distinction. This prevents future laundering of CM4 (in-session emission) into γ via YAML shape alone (P3 explicit at `[01c, Q5]`: "That prevents a future session from laundering CM4 into γ merely because the YAML shape exists"). The reframe is not merely additive; it changes how the digest schema is specified — the same field name with different `producer_kind` carries different evidentiary weight.

### §2.5 Q5 — Digest implementation locus

**Convergence at 3-of-4 across families on CM1/CM2 preferred + CM4 rejected as resolving-laundering**. P1 (`[01a, Q5]`: "CM1 preferred; CM2 acceptable as fallback; CM3 and CM4 rejected on laundering-surface-preservation grounds"). P3 (`[01c, Q5]`: "CM1 and CM2 are strongest because they displace self-report at the point of capture... CM4 is not harness-side measurement; it is structured self-report"). P4 (`[01d, Q5]`: "For a true (z6) resolution, CM1 or CM2 is required... CM4, in-session structured emission, is not enough to resolve EF-059/067/068").

P2 dissents toward CM3 if forced (`[01b, Q5]`: "if forced to choose: CM3 (post-hoc analysis via tools/build_retrieval_index.py extension) is the most-portable + least-harness-dependent + most-leverages-existing-infrastructure option"). P2's reasoning: portability cost favors CM3 at minimum-viable scope; CM3 leverages existing infrastructure.

[synth] Cross-family signal on CM1/CM2-preferred + CM4-explicitly-rejected. P2's CM3 preference is partial coverage (from minimum-viable framing); P3+P4's measurement-authority separation reframe partially absorbs P2's portability concern (CM3 entries can carry `producer_kind: post-hoc-reconstructed` with appropriate `authority_level` rather than being implicitly weakened).

### §2.6 Q6 — Reviewer self-report disposition

**Convergence at 3-of-4 across families on Direction-C-now + Direction-B-as-later-target via (z6)**. P2 (`[01b, Q6]`: "Direction C (honest-limit-only)... preserves §10.4-M25 P1 audit-cost-budget reopen-warrant with caveat"). P3 (`[01c, Q6]`: "Final state: Direction B... Until then: self-reported reviewer cost must not drive §10.4-M25 P1 budget thresholds. That is Direction A for authority, even if the prose note remains for historical traceability"). P4 (`[01d, Q6]`: "Direction C should land immediately: relabel reviewer cost fields as self-reported honest-limit material and prevent them from firing budget conclusions as if harness-measured. Direction B should be the phase-two target under (z6)").

P1 (`[01a, Q6]`) dissents toward Direction B immediately: "Direction A inactivates the §10.4-M25 P1 audit-cost-budget reopen-warrant — losing signal the workspace has declared structurally significant. Direction C preserves laundering-surface with disclosure".

[synth] Cross-family majority direction: Direction C now (immediate honest-limit subsection in `validation-approach.md` v7 disclosing reviewer self-report fields are not harness-measured ground truth) + suspend §10.4-M25 P1 budget-threshold arithmetic on self-reported values pending harness-measurement availability + Direction B as later target via (z6) phase-3 arc. This is more conservative than P1 (preserves field semantics during transition) and more progressive than P2's "preserves field with disclosure" (suspends budget arithmetic explicitly).

### §2.7 Q7 — Check 29 evidence-probe scope

**Convergence at 4-of-4 across families on 00-assessment + close-narrative scope (not close-only); WARN-only initially**. P1 (`[01a, Q7]`: "structured-frontmatter declaration plus close-narrative grep, frontmatter as authoritative source, grep as cross-check"). P2 (`[01b, Q7]`: "close-narrative grep + 00-assessment grep, WARN-only"). P3 (`[01c, Q7]`: "minimum viable check 29 should require a structured declaration in 00-assessment.md, mirrored or summarized in 03-close.md"). P4 (`[01d, Q7]`: "minimum should inspect both 00-assessment.md and 03-close.md").

**Convergence at 3-of-4 across families on structured declaration > pure grep** (P1+P3+P4 explicit; P2 prefers grep on grounds that frontmatter is itself self-report). [synth] P3's specific schema proposal at `[01c, Q7]` is operationally precise:

```
substrate_session_open: exercised | unavailable | skipped
substrate_evidence: <tool + target + result pointer or degradation reason>
```

P3 + P4 caveat: structured declaration is self-report until digest exists; treat as "evidence of declaration, not evidence of actual invocation until backed by harness telemetry" (`[01d, Q7]`). [synth] The schema's authority is bounded by the producer_kind separation per Q4 reframe; without harness backing, structured declaration is `producer_kind: agent-declared` and check 29 WARN-only is appropriate.

### §2.8 Q8 — Same-session-bounded vs multi-session phase-3 arc

**Convergence at 3-of-4 across families on hybrid (same-session-bounded β + multi-session γ arc)**. P2 (`[01b, Q8]`: "same-session-bounded adoption per S058 D-199 precedent for (α) or (β) scope... Hybrid (ε) bounded-then-extended is acceptable as fallback"). P3 (`[01c, Q8]`: "Hybrid adoption. Adopt β-bounded changes in the near term, then run γ as a multi-session phase-3 arc"). P4 (`[01d, Q8]`: "Hybrid adoption. Adopt a bounded (β)-like change on the S058 same-session-bounded model... Then run (γ) as a S062-style multi-session phase-3 arc").

P1 (`[01a, Q8]`) dissents toward multi-session-phase-3-arc-only for full (γ): "(γ)'s multi-spec scope is structurally analogous to S062 EF-058-tier-2-validation arc... S072 phase-3.1 + S073+ phase-3.2".

[synth] Cross-family majority: hybrid (ε) with explicit named gating conditions for γ phase-3 activation (per P4 explicit at `[01d, Q8]`: "after the capture locus is selected and one observation window can distinguish durable behavior change from design-space-salience compliance"). Same-session-bounded β adoption at S071 close + γ phase-3 arc named at S072+ with gating conditions.

### §2.9 Q9 — Bundle-vs-defer for EF-068-read-write-rebalance

**Convergence at 4-of-4 across families on defer; do not absorb into S071 phase-2 MAD scope**. P1 (`[01a, Q9]`: "defer; do not absorb into S071 phase-2 MAD scope. Open the four-record bundle only on operator-discretionary surface per S069 D-255"). P2 (`[01b, Q9]`: "defer per S069 D-255 separate-scope discipline... operator-discretionary, not phase-2-MAD-discretionary"). P3 (`[01c, Q9]`: "I would defer EF-068-read-write-rebalance from this S071 bundle... Opening the four-record bundle now risks mixing 'measure the surface' with 'redesign the surface' before the engine has evidence"). P4 (`[01d, Q9]`: "Do not open the four-record bundle at S071 by default... S069 D-255 preserves separate-scope with operator-discretionary reopen. That default should hold absent operator surface or a demonstrated hard dependency").

[synth] Unanimous. The S069 D-255 separate-scope default + operator-discretionary reopen warrant is preserved. EF-068-read-write-rebalance remains separate-scope at S072++. P4's explicit framing extends the position: "Bundling the sibling now risks exactly the laundering pattern P4 is tasked to audit: a valid concern gets pulled into a larger arc because the language sounds related, not because the decision dependency is necessary."

### §2.10 Q10 — Engine-v impact

**Convergence at 4-of-4 across families on engine-v13 at S071 close per (β) adoption + later substantive bump for (γ) per phase-3 arc**. P1 forecasts engine-v13 at S072 phase-3 close per (γ) (different timing); cross-family majority forecasts engine-v13 at S071 close per (β) + later substantive bump (likely engine-v14) at γ phase-3 close.

[synth] Cross-family majority direction: engine-v12 → engine-v13 at S071 close per (β) adoption (substantive `prompts/development.md` revision + `tools/validate.sh` check 29 + `validation-approach.md` v7 honest-limit subsection on reviewer self-report). Engine-v13 → engine-v14 at S072+ phase-3 close per (γ) adoption.

§10.4-M25 P2 cadence-depth concern: depth-7 at engine-v13 reset is engine-conventional (within engine-v9 depth-8 second-longest precedent); not cadence-precipitate. P4 (`[01d, Q10]`): "The §10.4-M25 cadence concern does not block v13, but it argues against hiding a large digest implementation inside a 'minor fix' narrative." [synth] The hybrid (ε) two-bump shape explicitly avoids the laundering P4 names.

## §3 Cross-product candidate convergence

**Per-perspective candidate position summary** (alphabetical by perspective for synthesis-time anchoring):

| Perspective | Family | Candidate position |
|-------------|--------|-------------------|
| Cross-Family Reviewer Laundering-Audit (P4) | codex/openai | (ε) Hybrid bounded-then-extended; (β) first-phase + (γ) committed-but-separately-gated |
| Harness-Discipline Architect (P1) | claude/anthropic | (γ) Full (z6) digest implementation; multi-session phase-3 arc per S062 D-220 |
| Incrementalist Conservator (P2) | claude/anthropic | (α) or (β) same-session-bounded per S058 D-199; defer (γ) until n≥3 (z6)-specific evidence |
| Outsider Frame-Completion (P3) | codex/openai | Modified (ε); (β) first-phase + (γ) target with measurement-authority separation reframe |

**Cross-family weighted convergence**: 3-of-4 across families (P2 + P3 + P4) on hybrid (ε) shape, with P3 + P4 measurement-authority-separation reframe extending the design-space §5.4 capture mechanism candidates with `producer_kind` semantic distinction. Cross-family signal: 1 Claude (P2) + 2 codex (P3 + P4). 3-of-4 across-families adoption signal threshold per S058 D-199 + S062 D-220 precedent: **REACHED**.

P1 dissent: full-(γ)-immediate position. Preserved as first-class minority per S062 §10.4-M16 reopen warrant pattern.

[synth] **Synthesis adoption direction**: (ε) Hybrid + measurement-authority separation reframe.

- **Phase 1 (β-class) at S071 close, same-session-bounded per S058 D-199**: load MCP retrieval tools by default (`.mcp.json`); promote `forward_references('S<NNN>')` from "additive to the contract minimum" / "not required" to required step at session-open in `prompts/development.md` §How to operate; add `tools/validate.sh` check 29 candidate (WARN-only; inspects 00-assessment.md + 03-close.md for structured declaration `substrate_session_open: exercised | unavailable | skipped` + `substrate_evidence:` pointer); add `validation-approach.md` v7 §Tier 2.5 honest-limit subsection on reviewer self-report (Direction C); explicitly suspend §10.4-M25 P1 audit-cost-budget arithmetic on self-reported values pending harness-measurement availability.

- **Phase 2 (γ phase-3 arc) at S072+ multi-session per S062 D-220**: specify (z6) digest schema with `producer_kind: harness-measured | post-hoc-reconstructed | agent-declared` + `authority_level` distinction per P3 measurement-authority separation reframe; specify (z6) capture mechanism (CM1 preferred; CM2 acceptable; CM3 acceptable as bridge with appropriate producer_kind; CM4 explicitly rejected as resolving-laundering); extend `validation-approach.md` v7 §(z6) substantively (v7 → v8); extend §Tier 2.5 audit shape to incorporate digest as required-when-available-with-D2.2-initial-posture; reviewer-prompt-template extension for digest input. Phase-3 activation gated by named conditions (P4 explicit at `[01d, Q8]`: "after the capture locus is selected and one observation window can distinguish durable behavior change from design-space-salience compliance").

## §4 Adoption shape

**Same-session-bounded adoption at S071 close for β-phase per S058 D-199 precedent**.

Spec-text changes at S071 close:

1. `.mcp.json` — load MCP retrieval tools by default (load-by-default for `mcp__selvedge-retrieval__forward_references` / `resolve_id` / `search`; remove deferred-loading + ToolSearch step requirement). Harness-config; not engine-definition.

2. `prompts/development.md` §How to operate — substantive revision: change `forward_references('S<NNN>')` from "useful diagnostic" / "additive to the contract minimum (`search` + `resolve_id`) and not required" to required step at session-open. Add precondition clause: substrate-availability-as-required-precondition (if substrate unavailable, session opens with explicit honest-limit + degradation per `multi-agent-deliberation.md` v4 §Graceful Degradation). Engine-definition substantive revision per OI-002 substantive-vs-minor heuristic.

3. `tools/validate.sh` check 29 candidate — new check; WARN-only initially per S058 D-204 mechanism-rollout discipline. Inspects current session's `00-assessment.md` for structured declaration:
```
substrate_session_open: exercised | unavailable | skipped
substrate_evidence: <tool + target + result pointer or degradation reason>
```
Cross-checks against `03-close.md` §X read-discipline-coverage section. Engine-definition substantive revision (new check; analogous to checks 26+27+28 added at S063 D-228).

4. `validation-approach.md` v7 — minor amendment: add §Tier 2.5 honest-limit subsection disclosing `duration_minutes` + `reviewer_cost` are reviewer self-reports and not harness-measured ground truth (Direction C from EF-067). Suspend §10.4-M25 P1 audit-cost-budget threshold arithmetic on self-reported values; preserve cost-observation surface for cross-session pattern observation only with explicit caveat. Engine-definition minor amendment per OI-002 (clarifying text edit + cross-reference; no structural change to mechanism).

5. `engine-feedback/INDEX.md` — three triage row dispositions extended (EF-067 + EF-059 + EF-068-substrate-load-bearing) per direction adopted; EF-067 transitions toward `resolved-via-multi-session-arc` per Direction C now + Direction B as later target via (z6); EF-059 transitions toward `phase-3-MAD-pre-ratified` per (γ) phase-3 arc; EF-068-substrate-load-bearing transitions toward `partially-resolved-at-β-phase + phase-3-deferred` per Direction 1 (a)+(b) at S071 + Direction 1 (c)+(d)+(e) + Direction 2 deferred to phase-3.

6. `validation-debt/index.md` — new row VD-003 introduced for (γ) phase-3 arc activation per P4 named-gating-conditions discipline. Tracks: (a) capture mechanism selection (CM1 vs CM2 vs CM3 with producer_kind); (b) observation window data on β-phase substrate-use (durable behavior change vs design-space-salience compliance distinction); (c) digest schema specification with producer_kind/authority_level. `review_by_session: S076` (5-session forward window per S063+S067 WX-62-1 precedent).

**Engine-version increment**: engine-v12 → engine-v13 at S071 close per substantive `prompts/development.md` revision + new `tools/validate.sh` check 29 + minor `validation-approach.md` v7 amendment.

## §5 Reframes adopted (cross-family-originated)

Per S058 + S062 + S064 cross-family-originated-and-adopted-at-MAD-execution reframe-architecture pattern (reified at n=3 prior; S071 reframe extends to n=4):

**§5.1 Measurement-authority separation reframe (P3-originated; P4-endorsed)**

Source: `[01c-perspective-outsider-frame-completion.md, Q5]` + `[01c, Frame critique]`. Endorsed at `[01d, Q4]` + `[01d, Q5]`.

The reframe: digest records carry `producer_kind: harness-measured | post-hoc-reconstructed | agent-declared` field + `authority_level` semantic distinction. Same field name carries different evidentiary weight per producer_kind. Prevents future laundering of CM4 (in-session emission) into γ via YAML shape alone.

Adopted at synthesis. Phase-3 (γ) digest schema specification at S072+ MUST include `producer_kind` + `authority_level` per this reframe. The reframe partially displaces design-space §5.4 (which named capture mechanism candidates without measurement-authority distinction) and extends design-space §6 (cross-product candidates) with a second axis (measurement-authority semantics).

[synth] This reframe also informs Q6 disposition: Direction A "drop fields entirely" can be reframed as "preserve fields with `producer_kind: agent-declared` + `authority_level: not-evidence` semantics" per P3 explicit at `[01c, Q6]`: "Direction A for authority, even if the prose note remains for historical traceability". Direction C-now is the spec-text mechanism; Direction-A-for-authority is the semantic interpretation.

**§5.2 Bundling-by-laundering audit framing (P4-originated)**

Source: `[01d-perspective-cross-family-reviewer-laundering-audit.md, Frame critique]`: "the (γ) bundle risks bundling-by-laundering. EF-068 Direction 1 (required substrate use), EF-067 Direction B (harness-measured reviewer cost), and EF-059 digest implementation each has independent merit. Bundling them can make the combined cost look inevitable because each part points at 'harness measurement.' The synthesis should preserve separate disposition for each: first-phase substrate habit correction, immediate reviewer-cost caveat, and separately scoped digest implementation."

Adopted at synthesis. The (ε) hybrid composition reflects this framing: separate dispositions per direction (substrate-habit-correction at β-phase; reviewer-cost-caveat at Direction C now; digest-implementation at γ phase-3 arc) rather than bundled-in-one-MAD-decision per (γ) candidate.

**§5.3 Operator-audit-as-load-shift-not-failure framing (P4-originated)**

Source: `[01d, Frame critique]`: "operator audit should not be framed only as evidence of engine failure... The right conclusion is not 'operator audit failed to prevent laundering,' but 'operator audit is currently carrying too much of the detection load.' That supports shifting load inward, while preserving Layer 6 as a live check during the transition."

Adopted at synthesis. The framing reframes the operator-audit-catches-what-in-session-discipline-missed pattern (S063+S064 + S067+S068 + S068+S069 reified at n=3) per design-space §3.1 + §10.2 observation 2. Operator-audit IS the workspace's outer counter-pressure functioning as designed per validation-approach.md v7 §Bootstrap-Paradox Layered Handling Layer 6.2; the harness-side measurement direction shifts load inward to engine but preserves Layer 6 as live check during transition.

## §6 First-class minorities preserved

Per `multi-agent-deliberation.md` v4 §Synthesis preserve-dissent discipline + S062 §10.4-M16 minority preservation pattern + S064 §10.4-M21-M25 minority preservation pattern:

**§6.1 §10.4-M26 candidate — P1 full-(γ)-immediate position (Session 071)**

Position: per `[01a, Q1+Q2+Q8]`: full (γ) digest implementation as the structural-correctness response per cross-session-state-claim discipline framing; multi-session phase-3 arc per S062 D-220 precedent; engine-v13 at S072 phase-3 close. Hybrid (ε) defers γ commitment; the empirical evidence chain at design-space §3.1 (n=5 substrate non-use) + §3.2 (n=3 reviewer self-report propagation) is operationally sufficient for γ commitment now per cross-session-state-claim verifiability requirement.

Source: `[01a, Q1, Q2, Q6, Q8, Cross-product candidate position, Dissent-preservation]`.

Reopen warrants:
- (a) **Sustained substrate non-use post-β**. After β lands at S071 close, if substrate non-use recurs at orchestrator self-report across ≥3 consecutive sessions despite spec-side requirement promotion, full (γ) is reopened.
- (b) **Reviewer-cost-trajectory laundering recurrence**. After β lands with Direction C, if a future operator audit surfaces a reviewer-cost-trajectory inaccuracy (analogous to EF-067 evidence at design-space §3.2), Direction B subsumption is reopened.
- (c) **Operational tractability shift**. If Claude Code hook surface stabilises or harness-telemetry capture mechanism becomes trivial, full (γ) is reopened on cost-side rather than evidence-side.

**§6.2 §10.4-M27 candidate — P2 (γ)-deferral-criteria position (Session 071; partly absorbed)**

Position: per `[01b, Q2+Q4+Q8+Cross-product candidate position+Dissent-preservation]`: (γ) scope is precipitate per S062 §10.4-M16 P2 reopen warrant criteria. The (z6)-specific surfaces (failed-tool-call + repeated-Read at concrete sessions) lack n≥3 evidence at present; n≥3 evidence-floor on (z6)-specific surfaces should gate phase-3 (γ) activation; records-substrate phase-2/3 stabilisation is natural pacing constraint.

Status: **partly absorbed** by (ε) hybrid synthesis. The minority preserves the **threshold for activating phase-3 (γ) at S072+**, not the phase-1 (β) adoption-direction question (which (ε) accommodates).

Source: `[01b, Q2+Q4+Q8+Cross-product candidate position+Dissent-preservation]`.

Reopen warrants:
- (a) (γ) phase-3 implementation introduces operational complexity that displaces operator-audit-as-laundering-detection without equivalent verification (operator-audit cadence drops below 80% across 10-session window per §10.4-M16 reopen warrant (c) pattern).
- (b) (γ) capture mechanism (CM1/CM2) portability friction blocks external-application engine load.
- (c) (z6) digest produces n≥3 sessions of measured behavior that diverges from spec-side expectation in ways that β would have caught — vindicating γ adoption-direction.
- (d) Records-substrate phase-2 mirrored-minorities + phase-3 feedback-records-family adoption stalled because (γ) phase-3 implementation absorbed substantive-arc capacity.

**§6.3 §10.4-M28 candidate — P3 measurement-authority-separation-as-load-bearing position (Session 071; substantively adopted)**

Position: per `[01c, Q4+Q5+Frame critique+Dissent-preservation]`: digest records MUST distinguish `producer_kind: harness-measured | post-hoc-reconstructed | agent-declared` + `authority_level`. Without that distinction, future sessions can launder CM4 into γ via YAML shape alone.

Status: **substantively adopted** at synthesis §5.1. Preserved as first-class minority against future-arc rollback or narrowing into "schema-only-without-producer-kind" framing.

Source: `[01c, Q4+Q5+Frame critique+Dissent-preservation]` + `[01d, Q4+Q5]` cross-family endorsement.

Reopen warrants:
- (a) Phase-3 (γ) digest spec adopted without producer_kind/authority_level fields; reframe operationally re-confirmed as primary discipline.
- (b) CM4 in-session emission entries treated as harness-measured-equivalent in any session's audit.
- (c) Future MAD on related arc surfaces measurement-authority concern independently.

**§6.4 §10.4-M29 candidate — P4 bundling-by-laundering audit position (Session 071; substantively adopted)**

Position: per `[01d, Frame critique+Cross-product candidate position+Dissent-preservation]`: separate dispositions per direction prevents bundling-by-laundering; (γ) bundle risks combined cost looking inevitable because each part points at "harness measurement" but each part has independent merit and independent cost.

Status: **substantively adopted** at synthesis §5.2. Preserved as first-class minority against future-arc bundling pressure.

Source: `[01d, Frame critique+Cross-product candidate position]`.

Reopen warrants:
- (a) Phase-3 (γ) implementation adopts bundled-direction shape that obscures per-direction cost.
- (b) Future MAD bundles related arcs without explicit per-direction cost analysis.
- (c) Operator-audit at phase-3 close surfaces bundling-by-laundering finding.

**Engine-wide first-class minorities count**: 50 entering S071 → **54 at S071 close** (4 new minorities §10.4-M26 through §10.4-M29). Per workspace-structure.md v9 §10.4 minority preservation pattern; mirrored cross-reference at validation-approach.md v7 §10 (will be updated at v8 if v7 → v8 substantive revision adopted at phase-3; at v7 minor amendment for Direction C, the §10 cross-reference is updated minor per OI-002).

## §7 Decision-procedure (3-of-4 across-families threshold check)

Cross-family weighted convergence per S058 D-199 + S062 D-220 precedent:
- Q1: 3-of-4 across families on targeted shift (P2 Claude + P3+P4 codex). **THRESHOLD MET**.
- Q2: 3-of-4 across families on staged response (P2 Claude + P3+P4 codex). **THRESHOLD MET**.
- Q3: 4-of-4 across families on load-by-default (unanimous). **THRESHOLD MET**.
- Q4: Mixed; 3-of-4 (P1+P3+P4) extended scope; 3-of-4 (P3+P4 + P1 implicit per measurement-authority-separation endorsement) measurement-authority separation reframe. **THRESHOLD MET on extended-scope-with-measurement-authority-separation**.
- Q5: 3-of-4 across families on CM1/CM2 preferred + CM4 explicitly rejected (P1 Claude + P3+P4 codex). **THRESHOLD MET**.
- Q6: 3-of-4 across families on Direction-C-now + Direction-B-as-later-target via (z6) (P2 Claude + P3+P4 codex). **THRESHOLD MET**.
- Q7: 4-of-4 across families on 00-assessment + close-narrative scope; 3-of-4 (P1+P3+P4) on structured declaration + grep cross-check (P2 prefers grep-only). **THRESHOLD MET**.
- Q8: 3-of-4 across families on hybrid (P2 Claude + P3+P4 codex). **THRESHOLD MET**.
- Q9: 4-of-4 across families on defer (unanimous). **THRESHOLD MET**.
- Q10: 4-of-4 across families on engine-v13 at S071 close (P1 timing differs but engine-v13 forecast unanimous). **THRESHOLD MET**.

**Cross-product candidate**: 3-of-4 across families on hybrid (ε) shape (P2 Claude + P3+P4 codex). **THRESHOLD MET**.

**Adoption shape**: same-session-bounded β at S071 close + multi-session γ phase-3 arc at S072+ per S058 D-199 + S062 D-220 hybrid precedent. **READY FOR DECIDE**.

## §8 Synthesis honest limits

1. **Synthesizer is Claude family**. Same as orchestrator + P1 + P2; cross-family reviewer family rule per `validation-approach.md` v7 §Tier 2.5 reviewer-family rule satisfied at MAD execution (P3+P4 codex; orchestrator anthropic). The Tier 2.5 (γ) reviewer at S071 close MUST be cross-family (preferred Gemini per §5.6 GPT-family-concentration window-ii consideration; codex acceptable fallback with reviewer overlap with P3/P4 disclosed).

2. **Claude-family weighting concern**. P2 + P1 are Claude-family; the cross-family weighted convergence calculation treats P2 (Claude) as part of the cross-family majority on the (ε) hybrid direction. The 3-of-4 across-families threshold IS met (P2 Claude + P3 codex + P4 codex), but the cross-family majority's strength is partly Claude-family (P2). [synth] This is the pattern the cross-family weighted-convergence threshold is designed to surface; P3+P4 codex independent endorsement of the (ε) hybrid + measurement-authority separation reframe + bundling-by-laundering audit framing is the cross-family signal that prevents Claude-family-internal-aliasing.

3. **P3 frame-completion's load-bearing reframe (measurement-authority separation) extends design-space §5.4 + §6 substantively**. The synthesis adopts the reframe at §5.1; phase-3 (γ) digest spec at S072+ MUST incorporate. [synth] Future revision opportunities at phase-3 + post-phase-3 observation may surface additional measurement-authority distinctions not pre-encoded at this S071 reframe.

4. **The Hawthorne-effect distinction (P1 honest-limit 3) about S071 substrate exercise being awareness-driven applies symmetrically to the synthesis**. The synthesizer (orchestrator at S071) has produced this synthesis under conditions where the design-space's substantive subject was salient throughout. Whether the synthesis adoption (β at S071 close + γ phase-3 arc deferred) preserves substrate-discipline durability post-adoption is itself testable empirically only at S072+ observation window.

5. **External imports flagged at perspectives**: P1 `[external import: instrumentation-locus convention]` (Q5) + `[external import: path-of-least-resistance UX framing]` (Q3); P2 `[external import: minimum-viable / minimum-revision pattern from skeptic-preserver methodology]` (Honest-limit 1); P3 `[external import: common observability/structured logging practice]` (Q5) + `[external import: common software-engineering observability and adapter-layer practice]` (Q5). [synth] Per PROMPT.md "Do not import ideas from outside the process" rule audit: these external imports are flagged at perspective-level; synthesis adoption of the measurement-authority separation reframe (which P3 partly grounds in the workspace's `retrieval-contract.md` contract-vs-implementation pattern + partly in external observability practice) accepts the external import as informing-not-load-bearing per the workspace-grounded portion's sufficiency.

6. **Phase-3 γ activation gating conditions per P4 explicit at `[01d, Q8]`**: "after the capture locus is selected and one observation window can distinguish durable behavior change from design-space-salience compliance." [synth] Operationalised: VD-003 lifecycle row (per §4 adoption shape) tracks (a) capture mechanism selection + (b) observation window data on β-phase substrate-use + (c) digest schema specification with producer_kind/authority_level. `review_by_session: S076` per 5-session forward window per S063+S067 WX-62-1 precedent.

7. **P2's (γ)-deferral-criteria position is partly absorbed by (ε) hybrid synthesis** per §6.2. The minority preserves the threshold-for-phase-3-γ-activation question, not the phase-1-β-adoption question. [synth] This is consistent with S058 + S062 precedent for cross-family-weighted-convergence direction adoption with absorbed-minority preservation discipline.

## §9 Path-justification per (z12) prompts/development.md discipline

The synthesis-adopted direction is **Path-AS phase-2 MAD execution → (β) at S071 close, same-session-bounded per S058 D-199 + (γ) phase-3 arc deferred to S072+ multi-session per S062 D-220**.

Per (z12) Path-justification at every close discipline (per `prompts/development.md` per S064 D-233 §10.4-M24 (z12) addition): the next-session recommendation will name the recommended Path explicitly.

[synth] Per `validation-approach.md` v7 §Tier 2.5 §7 Next-session-shape critique 5-condition test:
- (1) OIs unprogressed: OIs unchanged across n=6 retention sessions per assessment §3a; affirmative no-action justification per active substantive-class arc execution. NOT FIRES.
- (2) Inbox: three records on phase-3 surface (EF-067 + EF-059 + EF-068-substrate-load-bearing) actively progressing. NOT FIRES.
- (3) Watchpoints stale: no stale watchpoints. NOT FIRES.
- (4) Validation debt: VD-003 introduced at S071 close per §4 adoption shape; VD-001 + VD-002 both resolved at S067. NOT FIRES.
- (5) Recent closes Path-A pattern: only one Path A (S065) in retention window. NOT FIRES.

S072+ recommendation: Path L (single-orchestrator phase-3 implementation execution) OR Path-AS phase-3 design-space session per (γ) scope's multi-session arc shape. Phase-3 activation gated by VD-003 review at S076.

[synth] **Synthesis recommends Decide activity adopt this direction at `02-decisions.md`**.
