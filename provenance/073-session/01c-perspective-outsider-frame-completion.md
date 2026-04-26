---
session: 073
title: P3 Outsider Frame-Completion — Session 073 phase-2 MAD response
date: 2026-04-26
status: complete
perspective: outsider-frame-completion
committed_at: 2026-04-26T00:00:00+10:00
---

# P3 Outsider Frame-Completion

## Frame critique

The main missing axis is that §3b frames CM1/CM2/CM3 as mutually ranked capture mechanisms, but the portable design surface is better described as a capture-adapter contract with multiple producer implementations. That is my first reframe: **z8 capture-adapter-contract-before-capture-mechanism**. CM1 can be the first adapter for the current Claude Code self-development workspace, but treating it as the preferred end-state risks laundering current-harness familiarity into engine design. The engine’s evidence contract should survive migration to codex CLI, Gemini CLI, OpenAI Agents SDK, custom MCP agents, or non-interactive batch harnesses.

The second missing axis is validation locus. Check 26 is described as “substrate-aware,” but §3b and §3d blur live substrate availability, recorded substrate evidence, and harness runtime observability. My reframe is **z9 validator-as-evidence-consumer-not-live-harness-participant**. `tools/validate.sh` may run outside Claude Code’s MCP context, in CI, from a terminal, or under a different agent harness. It should validate declared evidence and digest shape; it should not depend on being able to perform the same substrate calls that the session-open actor performed.

The third missing axis is storage location versus evidentiary authority. SCD-4 records-substrate promotion is treated as a schema scope expansion, but “digest stored as YAML file” versus “digest stored as records-substrate row” is orthogonal to `producer_kind` and `authority_level`. I would keep SCD-4 out of immediate scope, while designing SCD-3 so the same digest envelope can later be inserted into records substrate without semantic migration.

Finally, Q8 needs a sharper distinction between reopening a warrant and bundling its implementation. Aggregate-budget pressure at S073 is real per §2, but the EF-068 read-write rebalance bundle is not the same problem as harness telemetry. My reframe is **z10 reopen-warrant-activation-is-not-implementation-bundling**. S073 can acknowledge the changed pressure and schedule the four-record bundle without coupling it to the γ digest implementation.

## Q1 — capture mechanism preferred end-state

My preferred end-state is **CM2 as the portable primary capture layer**, with **CM1 as the first workspace-local adapter** and **CM3 as the secondary reconstruction/audit bridge**.

§3b makes CM1 look low-cost and high-authority for the current Claude Code workspace, so it is reasonable as the first implementation. But as engine design, CM1 is only medium-portability by the brief’s own table. The Selvedge engine is not only a Claude Code procedure; §2 explicitly includes cross-workspace and orchestrator-side read-discipline telemetry. If the digest becomes part of reviewer authority, then a Claude-only producer hardens the wrong boundary.

CM3 should not be dismissed as merely weaker. It has lower authority than harness-emitted capture, but it is valuable precisely because it can check, reconstruct, and compare across harnesses. The stable target should be: primary producer when available, secondary reconstruction when not, agent declaration only as tertiary.

## Q2 — schema scope

I support **SCD-3 full extended schema**, but with a portability envelope added before ratification: `capture_adapter`, `capture_adapter_version`, `capture_capabilities`, and explicit `unobserved_fields` or equivalent.

The §3d schema already carries the essential S071 §10.4-M28 distinction: `producer_kind` and `authority_level`. That should remain load-bearing. However, a digest that lists fields without declaring what the capture path was capable of observing will create false equivalence between CM1, CM2, and CM3. For example, a post-hoc transcript parser may count visible tool calls but miss wall-clock or process-level failure detail. That is acceptable only if the digest declares the capture limits.

I do not support SCD-4 now. Records-substrate promotion may be desirable later, but it should not be bundled with the schema authority decision. Make the digest portable enough that SCD-4 is a storage migration, not a semantic rewrite.

## Q3 — reviewer availability discipline

I support **RAD-3 bridged transition**.

The end-state should be D2.1: a Tier 2.5 reviewer should always receive the best available digest, and if no digest exists after the rollout window, that absence should itself be review-relevant. But immediate RAD-1 would overfit to the first capture implementation and may punish non-Claude harnesses before the adapter contract exists.

During rollout, use D2.2 behavior with explicit absence recording: “digest unavailable,” `producer_kind` absent or tertiary, and reason. At a named gating session, likely aligned with the VD-003 S076 review, promote to D2.1 if capture has demonstrated durability.

## Q4 — reviewer self-report disposition

I support **REVD-2 partial deprecation now**, with a planned REVD-3 re-baseline after enough harness-measured data exists.

Full subsumption now would conflate two changes: the measurement source changed, and the underlying audit cost may have changed. The existing S063 self-report baseline should not be treated as commensurable with harness-measured wall-clock and token counts until a bridge interval exists. Preserve `duration_minutes` and `reviewer_cost` as `producer_kind: agent-declared` tertiary fields, add harness-measured fields in parallel, and resume §10.4-M25 threshold arithmetic only against the harness-measured trajectory once there are enough comparable observations.

## Q5 — check 26 substrate-aware branch

I support **CHKD-2 substrate-preferred-with-fallback**, with the important constraint that validation must inspect evidence rather than require live substrate access.

The validator should check whether session-open substrate use is evidenced in the digest, session record, or declared honest-limit path. It should not assume it is running inside Claude Code with MCP tools available. A CI run or external operator running `validate.sh` may have filesystem access but not substrate-call capability. Making check 26 a hard live-substrate requirement would reduce portability and create false failures outside the original harness.

CHKD-3 defers too much; EF-068 Direction 1(e) exists because substrate-use-required needs teeth. But CHKD-1 is too brittle until runtime context and evidence source are separated.

## Q6 — engine-v cadence

I support **EVD-3 multi-step bump**.

A single substantive bump would hide too many moving pieces: capture adapter contract, digest schema, validator branch, reviewer prompt behavior, and eventual hard-precondition activation. The cleaner cadence is: first minor bump for adapter contract and schema draft; second minor bump for implementation and validator soft checks; then substantive bump when reviewer availability and self-report disposition become normative.

This also preserves a clear audit trail if CM1 proves easy locally but weak portably.

## Q7 — reviewer-prompt-template extension scope

I support a **minimum-viable extension now**, followed by full extension after the z7 lock-in condition.

The immediate prompt-template change should require reviewers to read the digest when available, distinguish primary/secondary/tertiary evidence, and flag absent digest conditions. Full telemetry-driven reviewer behavior should wait until there are at least two successful digest-bearing reviews. Otherwise the template may encode assumptions from the first capture adapter rather than from the digest contract.

I would also version the reviewer prompt template explicitly. Prompt-template evolution is part of the engine feedback loop, not just editorial copy.

## Q8 — bundle-vs-defer EF-068-read-write-rebalance

I do **not** support bundling the four-record EF-068 read-write rebalance implementation into the γ digest arc. I do support activating the reopen warrant procedurally.

The aggregate budget is over the soft limit per §2, so pretending nothing changed would be weak. But adding structural read-write rebalance to the same phase-3 implementation that is selecting capture, schema, validator, and reviewer discipline increases the chance of obscured causality. If later review shows improved aggregate behavior, it will be unclear whether the change came from digest telemetry, close rotation, or structural rebalance.

Record the warrant as active, schedule it as separate S074+ scope, and keep γ focused on measurement infrastructure.

## Q9 — implementation-locus session-shape

I support **Path-AS at S074+**, not a single-orchestrator Path L.

The design requires multiple separable decisions: adapter contract, current-workspace adapter, post-hoc reconstruction bridge, validator evidence semantics, and reviewer prompt behavior. A single-orchestrator implementation would be faster, but it would also privilege the current harness and reduce scrutiny of portability assumptions. Path-AS fits the already adopted multi-session phase-3 arc from §1.

## Q10 — cross-spec interaction depth

I support a **substantive `validation-approach.md` bump**, minor amendments to read/retrieval contracts, and either a small appendix or bounded new contract for harness telemetry if the current spec layout cannot express adapter semantics cleanly.

The key is not the number of files touched; it is whether the digest contract is stored somewhere neutral enough that it does not become “Claude hook behavior” by implication. `validation-approach.md` should carry normative use in review and validation. Read/retrieval contracts need minor alignment for session-open evidence and future records-substrate compatibility. A new full spec class is only justified if the adapter contract cannot be made precise as an appendix.

## Cross-product candidate position

I advocate a new candidate: **(γ-6) portable adapter-contract staged hybrid**.

Its shape is:

- Capture: CM2 portable primary end-state, CM1 first local adapter, CM3 secondary reconstruction bridge.
- Schema: SCD-3, plus capture adapter/capability metadata; defer SCD-4 storage promotion.
- Reviewer availability: RAD-3, with D2.1 activated only after named gating.
- Self-report: REVD-2 now, REVD-3 after harness-measured bridge data.
- Check 26: CHKD-2, evidence-consuming and runtime-portable.
- Cadence: EVD-3 multi-step.
- Prompt template: minimum viable now, full after z7-style n=2 digest-bearing review lock-in.
- EF-068 read-write rebalance: activate warrant, do not bundle implementation.
- Implementation locus: Path-AS.

This differs from γ-5 because γ-5 still centers CMD-4 as CM1+CM3 staged coverage. My position says the missing durable primitive is not “CM1 plus CM3”; it is a portable adapter contract that allows CM1, CM2, and CM3 to be compared without pretending they have the same authority or observability.

If synthesis rejects γ-6 as too broad, my fallback is γ-5 modified to name CM2 as the end-state rather than leaving portability as an aspiration.

## Honest limits

- I am reasoning only from the embedded brief and have not inspected the actual S072 design-space, specs, validator, or workspace records.
- I do not know whether the current Claude Code hook surface can emit every §3d field without fragile workarounds.
- I do not know whether transcript availability is consistent enough for CM3 to reconstruct reliable token, wall-clock, or failed-tool data.
- I cannot verify whether `validate.sh` currently has any substrate-aware primitives or whether check 26 can cleanly inspect evidence without live MCP access.
- I cannot assess implementation cost for CM2 beyond the brief’s “medium” characterization.
- I may be overweighting portability relative to the self-development workspace’s immediate operational needs.
- I do not know whether records-substrate promotion has hidden maturity blockers beyond §10.4-M18 as summarized.

## Dissent-preservation

If synthesis adopts γ-1, γ-2, γ-4, or γ-5 without naming CM2 or an equivalent adapter contract as the preferred end-state, preserve a **P3 portable-capture-adapter minority warrant**: reopen if the engine is run under a non-Claude harness, if digest production fails outside Claude Code, or if reviewer audit treats CM1 output as generally authoritative rather than harness-specific.

If synthesis adopts RAD-1 immediately, preserve a **bridged-availability minority warrant**: reopen on the first absent digest caused by deployment mechanics rather than agent noncompliance, or at VD-003 S076 if the hard precondition blocks review continuity.

If synthesis adopts REVD-1 now, preserve a **measurement-transition minority warrant**: reopen when harness-measured audit cost diverges materially from the S063 self-report baseline, because the baseline may have changed measurement authority rather than behavior.

If synthesis bundles EF-068 read-write rebalance into γ implementation, preserve a **scope-causality minority warrant**: reopen if later retention or aggregate-budget claims cannot distinguish effects from close rotation, digest telemetry, and read-write restructuring.
