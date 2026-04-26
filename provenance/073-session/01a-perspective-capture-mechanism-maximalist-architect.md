---
session: 073
title: Capture-Mechanism-Maximalist Architect — Session 073 phase-2 MAD response
date: 2026-04-26
status: complete
perspective: capture-mechanism-maximalist-architect
committed_at: 2026-04-26T08:00:00Z
---

# Capture-Mechanism-Maximalist Architect

## Frame critique

The brief is well-structured and load-bearing on the right axes (capture mechanism, schema scope, reviewer availability discipline, self-report disposition, check 26 branch, engine-v cadence, template extension, bundle-vs-defer, session-shape, cross-spec depth). My principal frame critique is that the cross-product candidate enumeration (γ-1) through (γ-5) is presented as a roughly even-weighted decision surface, when the structural argument from §10.4-M28 (measurement-authority separation, substantively adopted at S071 D-263) and §10.4-M29 (bundling-by-laundering audit) actually privileges the maximal end of the spectrum more than the brief's pacing-language admits. If `producer_kind` and `authority_level` are load-bearing distinctions in the digest schema (per §3d), then any γ implementation that ships a partial schema or tertiary-only capture mechanism creates exactly the laundering surface §10.4-M29 was preserved to audit against. The brief's neutrality between (γ-2) and (γ-1) is itself a frame I push back on.

Second frame critique: the brief's §3a observation table treats S071+S072+S073 substrate-use non-zero as "n=2 observation point" toward Hawthorne disambiguation, with first triangulation at n=4-5 across S074-S076. This pacing argument is real, but it is not symmetric with the laundering-surface cost. Each session that ships under partial-γ accrues digest records with `producer_kind: agent-declared` for fields that COULD be `harness-measured`. Those records are durable artifacts. A "bridged transition" framing (RAD-3) underweights the asymmetry: bridging-toward-harness-measured leaves a tail of agent-declared records that retrospective re-baseline (REVD-3) is designed precisely to address. The brief surfaces REVD-3 but treats it as an option rather than a structural requirement of any partial-shift trajectory.

Third frame critique: the brief's Q1 enumeration (CM1 vs CM2 vs CM3; CM4 explicitly rejected) is correct in rejecting CM4 (whatever that was — likely an agent-declared-only end-state, which would defeat the measurement-authority separation reframe). But the brief's CMD-4 framing in (γ-1) and (γ-5) — "CM1+CM3 hybrid" — should be reframed: this is not a hybrid in the bridge-then-replace sense; it is a multi-context primary-authority strategy where CM1 is primary in Claude Code contexts and CM3 is primary in offline/non-hook contexts. Both surfaces produce primary-authority records under measurement-authority separation. This reframe matters for Q3 (RAD-1) because the always-available precondition becomes structurally satisfiable in both contexts.

Fourth frame critique: the aggregate-budget pressure (91,571 / 90K soft, 1,571 over) is a real constraint and S073 MUST include aggregate-reducing action, but this is a session-shape constraint, not a γ-scope constraint. Resolving the budget pressure via close-rotation or default-read trim is independent of the γ phase-3 scope decision. The brief correctly separates these but the proximity in §2 risks reading as a coupling.

## Q1 — capture mechanism preferred end-state

Position: **CMD-4 (CM1+CM3 hybrid as multi-context primary-authority strategy).**

Reasoning: CM1 (Claude Code hooks PreToolUse + PostToolUse) is the strongest primary-authority surface available in the dominant execution context for this workspace. It captures tool invocations at the harness level with no agent-side mediation; this is the structural property that earns `producer_kind: harness-measured` and `authority_level: primary` per §10.4-M28. CM2 (external wrapper) has higher portability but introduces process-tree introspection complexity for a marginal cross-harness-tool benefit that this workspace does not currently exercise. CM3 (post-hoc transcript-reconstruction) is `authority_level: secondary` per §3b, but it is the only surface that covers offline reconstruction and non-hook contexts (e.g., codex/gemini CLI invocations from the orchestrator). CMD-4 ships both CM1 (primary; Claude Code contexts) and CM3 (primary-by-context; offline reconstruction), with explicit `producer_kind` distinguishing the two records.

Rejecting CMD-1 (CM1-only) leaves codex/gemini CLI invocations uncaptured at primary authority — a significant laundering surface given §5.6 GPT-family-concentration window-ii observation. Rejecting CMD-3 (CM3-only) accepts secondary authority where primary is achievable. CMD-4 is the structurally honest end-state under measurement-authority separation.

[external import] Claude Code's PreToolUse/PostToolUse hooks emit JSON events to configured commands per `.claude/settings.json`; the hook surface is documented and stable. I flag this as external import; the workspace has not committed to a specific hook API surface.

## Q2 — schema scope

Position: **SCD-3 (full extended schema).**

Reasoning: The schema candidate in §3d enumerates the load-bearing fields: `tool_calls`, `read_invocations`, `substrate_calls`, `files_read_at_session_open`, `decision_claims_with_evidence_pointers`, `reviewer_invocation_*`. Each of these maps to a specific audit surface that §10.4-M29 (bundling-by-laundering audit) was preserved to detect. Shipping SCD-2 (substrate_calls extension only) leaves `decision_claims_with_evidence_pointers` and `reviewer_invocation_*` as agent-declared, which is exactly the laundering surface. Shipping SCD-1 (original-EF-059-only) is structurally regressive given §10.4-M28 substantive adoption at S071. SCD-4 (records-substrate-promotion) is correctly deferred per S062 §10.4-M18 maturity gate; that constraint is binding.

SCD-3 is the minimum schema that honors §10.4-M28 and §10.4-M29 jointly. Anything less defers the audit surface to a future session under the same Hawthorne-vs-durable framing the brief is trying to disambiguate, which is circular.

## Q3 — reviewer availability discipline

Position: **RAD-1 (D2.1 always-available-always-read; digest is hard precondition for Layer 2 (γ) reviewer).**

Reasoning: If the digest is structurally optional input to the reviewer (RAD-2), then reviewer audits across sessions become non-comparable: some have harness-measured fields, some do not. The reviewer-prompt-template lock-in at v2 per S067 D-246 (z7) lock-in-after-n=2 specifically rewards comparability. RAD-1 makes digest availability a hard precondition; if unavailable, the reviewer audit defers. This is the strongest discipline.

Counter-argument the brief surfaces: bridged transition (RAD-3) accommodates deployment-window absence. I accept the deployment-window concern but argue CMD-4 (CM1+CM3) makes the always-available precondition satisfiable in both Claude Code and offline contexts at γ ratification. The bridged window is short and structurally bounded.

## Q4 — reviewer self-report disposition

Position: **REVD-3 (Direction B full subsumption + retrospective re-baseline).**

Reasoning: REVD-1 (full subsumption now) deprecates `duration_minutes` + `reviewer_cost` self-report and replaces with harness-measured. REVD-2 (partial-deprecation) preserves both surfaces with `producer_kind` annotation; this is a laundering surface — the agent-declared record persists with no forcing function for the harness-measured record to supersede it. REVD-3 adds retrospective re-baseline: post-(γ) harness-measured value becomes the new baseline against which prior agent-declared values are explicitly compared and re-anchored. This is the structural completion of measurement-authority separation: the prior agent-declared records are not erased (their provenance is preserved) but they are no longer the reference baseline for §10.4-M25 P1 audit-cost-budget threshold arithmetic.

§10.4-M25 reopen warrant requires harness-measured baseline to re-activate threshold arithmetic; REVD-3 is the move that discharges the suspension cleanly. REVD-2 leaves §10.4-M25 in indefinite suspension because the threshold arithmetic cannot operate on mixed agent-declared/harness-measured fields.

## Q5 — check 26 substrate-aware branch

Position: **CHKD-1 (substrate-aware with required precondition).**

Reasoning: β-phase substrate-use codification at S071 D-264 promoted `forward_references('S<NNN>')` to required step at session-open. β-phase is spec-side discipline; the harness-side enforcement gap is exactly what EF-068-substrate-load-bearing Direction 1 (e) was activated to close. CHKD-2 (substrate-preferred-with-fallback) leaves the harness-side gap open: a session can pass validation without substrate calls. CHKD-3 (defer) is structurally regressive.

CHKD-1 makes substrate calls a hard precondition checked at the harness layer (validate.sh check 26 substrate-aware branch). Sessions without substrate calls FAIL validation. This is the move that lets us empirically distinguish durable behavior change from design-space-salience compliance: if substrate calls are harness-required, the Hawthorne-vs-durable distinction collapses (because compliance is structural, not behavioral), and the residual signal is whether the substrate calls produced load-bearing evidence pointers (decision_claims_with_evidence_pointers) — which is the actual question of interest.

## Q6 — engine-v cadence

Position: **EVD-1 (single substantive bump engine-v13 → engine-v14 at S074 ratification).**

Reasoning: γ phase-3 implementation is a single coherent scope: capture mechanism + schema + RAD discipline + REVD disposition + check 26 + reviewer-prompt-template extension + cross-spec amendments. Splitting into EVD-2 (two-step) or EVD-3 (multi-step) introduces engine-v transitions where intermediate states are themselves preserved at non-trivial preservation depth. The current engine-v13 preservation depth is 0 (just ratified at S071); adding intermediate engine-v14-minor + engine-v15-substantive + ... versions multiplies the preservation surface for marginal pacing benefit.

EVD-1 also reduces the cross-spec amendment count: a single substantive bump amends `validation-approach.md` v7 → v8, `multi-agent-deliberation.md` v4 → v5 (template extension), `prompts/development.md` (substrate precondition strengthened from spec-side to harness-side), `tools/validate.sh` (check 26 substrate-aware branch + check 29 promoted from WARN to PASS/FAIL with substrate evidence-probe). One coherent edit set, one engine-v transition.

## Q7 — reviewer-prompt-template extension scope

Position: **Full reviewer-prompt-template extension (template v3 candidate scope per (z7)).**

Reasoning: Per S067 D-246 (z7) lock-in-after-n=2: template v2 is locked-in for the bootstrap_status: limited-confidence + bootstrap_status: none scopes. Template v3 candidate scope at γ phase-3 ratification extends the reviewer prompt to consume the full digest schema (all fields enumerated in §3d), including `decision_claims_with_evidence_pointers` and `reviewer_invocation_*`. Minimum-viable extension would consume only the substrate_calls and tool_calls fields, leaving evidence-pointer audit and reviewer-cost feedback at agent-declared authority.

The template v3 extension is the move that activates the §10.4-M23 P3 substrate-led reviewer-judged frame at full scope: the reviewer judges substrate use AND evidence-pointer load-bearing AND reviewer-cost calibration jointly, all from harness-measured input. Partial extension defers the load-bearing audit to template v4 in a future engine-v transition.

## Q8 — bundle-vs-defer EF-068-read-write-rebalance

Position: **Defer EF-068-read-write-rebalance per S069 D-255 separate-scope (do NOT bundle).**

Reasoning: The S069 D-255 operator-discretionary reopen warrant explicitly preserves EF-068-read-write-rebalance as separate scope. Bundling into γ phase-3 expands the implementation surface to include read-discipline rebalance discussions that are orthogonal to the capture-mechanism + digest-schema axis. The aggregate-budget pressure at S073 (1,571 over soft) is itself partial evidence of EF-068-read-write-rebalance Direction 4 critique materially reifying — but γ phase-3 is not the right vehicle to address it.

Defer EF-068-read-write-rebalance to a separate Path-AS arc after γ phase-3 ratification. The γ implementation will produce harness-measured aggregate-read telemetry as a side-effect (via `read_invocations` + `files_read_at_session_open` schema fields), which is itself input to the EF-068-read-write-rebalance scope when it activates. This is sequencing, not deferral-as-rejection.

## Q9 — implementation-locus session-shape

Position: **Path L phase-3 implementation per direction adopted (single-orchestrator at S074+).**

Reasoning: Phase-2 MAD has run at S073 (this session) producing the direction adoption. Phase-3 implementation is mechanical given the direction: edit `tools/validate.sh`, write the hook scripts (CM1 surface), write the post-hoc reconstruction tool (CM3 surface), amend specs, extend the reviewer-prompt-template. None of these require independent perspectives at perspective-formation discipline. Path-AS at S074+ would be over-specification for an implementation arc; the design-space is closed.

If implementation surfaces a substantive disagreement during execution (e.g., a CM1 hook API surface that turns out unsuitable), that disagreement triggers a fresh design-space session at S075+ per Path-AS Shape-1 phase-1 precedent. The default at S074+ is Path L.

## Q10 — cross-spec interaction depth

Position: **Substantive engine-v14 bump (substantive cross-spec interaction depth).**

Reasoning: The cross-spec amendment surface for γ phase-3 maximal-scope is:
- `validation-approach.md` v7 → v8: substantive (digest schema specification, producer_kind/authority_level discipline, check 26 substrate-aware required-precondition branch, reviewer-prompt-template v3 extension consumed at audit time).
- `multi-agent-deliberation.md` v4 → v5: substantive (reviewer-prompt-template v3 extension).
- `prompts/development.md`: substantive (substrate precondition strengthened from spec-side encouragement at v13 to harness-side enforcement at v14; β-phase becomes γ-phase structurally).
- `tools/validate.sh`: substantive (check 26 substrate-aware branch + check 29 promotion from WARN to PASS/FAIL).
- `read-contract.md` v6: minor (digest fields not counted in aggregate-read budget; cross-reference to `validation-approach.md` v8).
- `records-contract.md` v1: minor (digest record class added to records taxonomy; SCD-4 records-substrate-promotion still deferred per S062 §10.4-M18).
- `engine-manifest.md`: minor (engine-v14 ratification entry).

This is a substantive engine-v14 bump. Minor-only would understate the scope and risk under-preservation of the transition.

## Cross-product candidate position

I advocate **(γ-1) maximal-scope** as primary, with **(γ-2) (ε)-hybrid-default-scope** as second-best.

Reasoning: (γ-1) is the structurally honest response to §10.4-M28 (measurement-authority separation, substantively adopted) and §10.4-M29 (bundling-by-laundering audit). It ships CMD-4 + SCD-3 + RAD-1 (RAD-3 in the brief's (γ-1) is bridged transition; I refine to RAD-1 with explicit short bridged window) + REVD-3 + CHKD-1 + EVD-1. Resolution: 3-4 sessions at S074-S077; risk: medium-high but the medium-high risk is exactly the surface §10.4-M29 was preserved to audit during implementation, which is healthy.

(γ-2) is acceptable second-best because it preserves SCD-3 (full extended schema) — the load-bearing schema decision — while pacing CMD-1 (CM1-only), RAD-2 (D2.2 best-effort), REVD-2 (partial-deprecation), CHKD-2 (substrate-preferred-with-fallback), EVD-2 (two-step). The cost is that §10.4-M25 audit-cost-budget threshold arithmetic remains suspended longer (REVD-2 is laundering-adjacent), and the harness-side substrate enforcement gap remains open (CHKD-2 fallback). Acceptable for pacing but structurally inferior to (γ-1).

(γ-3) minimum-viable-γ is rejected: SCD-2 (substrate_calls only) leaves the evidence-pointer audit and reviewer-cost surface as agent-declared, which is the laundering surface §10.4-M29 was preserved to detect. CHKD-3 defers the substrate-aware branch indefinitely. (γ-3) is structurally insufficient response to §10.4-M28.

(γ-4) capture-mechanism-first staged is rejected: phase-3.1 ships CMD-1 + minor schema, then phase-3.2 ships SCD-3 + RAD-2 + REVD-2. This sequencing accrues digest records under the minor schema before SCD-3 is in place; those records are durable laundering-adjacent artifacts that REVD-3-equivalent retrospective re-baseline must address later. Sequencing without retrospective re-baseline is incoherent.

(γ-5) hybrid CMD-4 staged is rejected for similar reasons: the staging across SCD-2→SCD-3 and REVD-2→REVD-3 multiplies engine-v transitions without reducing the durable laundering-adjacent record surface.

## Honest limits

1. **Cost of full-shift adoption.** Maximal-scope γ phase-3 ships substantial implementation work in 3-4 sessions: hook scripts, post-hoc reconstruction tool, schema validator, template v3 extension, multiple substantive spec bumps. This is non-trivial; (γ-2) reduces this surface materially and that reduction is real. My position underweights pacing-feasibility.

2. **Portability friction surface.** CM1 binds to Claude Code per §10.4-M27 P2 reopen warrant (b). CMD-4 (CM1+CM3) partially mitigates via CM3 offline-reconstruction primary-authority-by-context, but the `.claude/settings.json` per-workspace setup is real friction for cross-workspace adoption. If this workspace later spawns sister workspaces, the portability cost compounds.

3. **Records-substrate phase-2/3 pacing constraint.** §10.4-M27 P2 reopen warrant (d) and S062 §10.4-M18 maturity gate both bind: SCD-4 (records-substrate-promotion) is correctly deferred. But the digest-records-vs-records-substrate boundary may surface implementation friction at γ phase-3 that the brief does not yet resolve.

4. **[external import] uncertainty on Claude Code hook API stability.** I have flagged Claude Code PreToolUse/PostToolUse hook surface as external import. The workspace has not committed to a specific API surface; if the hook API surface is less stable than I assume, CM1 implementation cost is higher.

5. **Hawthorne-vs-durable disambiguation collapsed-not-resolved.** CHKD-1 (substrate-required) collapses the Hawthorne-vs-durable disambiguation by structural enforcement. But the residual question — whether substrate calls produce load-bearing evidence pointers — is itself a behavioral question that CHKD-1 does not resolve. My position pushes the disambiguation surface, not eliminates it.

6. **REVD-3 retrospective re-baseline scope ambiguity.** Retrospective re-baseline against agent-declared values from S001-S073 is the formal move, but the operational discipline (do we re-baseline ALL prior records or only post-§10.4-M25 records?) is not specified in the brief. My REVD-3 position requires a follow-on specification decision.

7. **Aggregate-budget pressure at γ implementation.** Each γ implementation session at S074-S077 will itself accrue close-narrative scaffolding-loaded text under substantive-arc-class scope. The aggregate may exceed soft warning bands repeatedly. My position does not address aggregate-budget pressure at implementation time.

## Dissent-preservation

If synthesis adopts (γ-2)/(γ-3)/(γ-4)/(γ-5), preserve maximal-scope position as **§10.4-M30 candidate (P1 capture-mechanism-maximalist position; S073)**.

Minority warrant: maximal-scope γ phase-3 is the structurally honest response to §10.4-M28 measurement-authority separation and §10.4-M29 bundling-by-laundering audit. Partial-shift trajectories accrue durable agent-declared records that REVD-3-equivalent retrospective re-baseline must later address; sequencing without retrospective re-baseline is incoherent. CMD-4 (CM1+CM3) is the multi-context primary-authority strategy that satisfies RAD-1 always-available precondition in both Claude Code and offline contexts.

Activation triggers (any of):
- (a) Synthesis adopts (γ-3) or (γ-4) without retrospective re-baseline discipline; first observation window evidence (S074-S076) shows agent-declared digest records persist as load-bearing baseline for §10.4-M25 audit-cost-budget threshold arithmetic.
- (b) γ phase-3 implementation under (γ-2)/(γ-5) surfaces the laundering-adjacent record surface §10.4-M29 was preserved to detect; reviewer audit at S077+ flags a digest record under `producer_kind: agent-declared` for a field that COULD be `harness-measured`.
- (c) β-phase observation window data at S076 shows substrate-use compliance regression (substrate calls drop below S071-S073 baseline) under any γ-scope that does not include CHKD-1 substrate-required precondition; Hawthorne effect confirmed empirically.
- (d) Cross-family reviewer audit at γ phase-3 ratification (γ reviewer required per Layer 2) explicitly surfaces the partial-schema laundering surface as material concern.

Reopen warrants:
- (i) §10.4-M28 measurement-authority separation reframe is augmented or refined in a way that lifts the structural honest-response argument for maximal-scope.
- (ii) Records-substrate phase-2/3 maturity (per §10.4-M18 gate) advances enough to absorb digest-record class into records-substrate scope (SCD-4 activation), at which point the maximal-scope argument is partially absorbed.
- (iii) Cross-workspace portability cost materially exceeds projection; CMD-4 binding to Claude Code becomes load-bearing concern for engine-v15+ portability.

Preserve §10.4-M30 with explicit reference to §10.4-M26 (S071 P1 full-(γ)-immediate position; this is the same position-class evolved across the multi-session phase-3 arc).
