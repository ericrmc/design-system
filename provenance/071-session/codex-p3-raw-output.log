---
session: 071
title: Perspective Outsider Frame-Completion — staged enforcement with measurement-authority separation
date: 2026-04-26
status: complete
perspective: outsider-frame-completion
committed_at: 2026-04-26T06:19:50Z
---

## Q1 — Shift to harness-side enforcement for cross-session-state claims, not for everything

The design-space §4.1-§4.3 frames the common surface correctly: the engine has spec-side encouragement where it needs measured evidence. I would not generalize this into “every discipline needs harness enforcement.” The `validation-approach.md` v7 §Principled Asymmetry already draws the right boundary: “Routine workspace checks may remain self-assessed,” while claims about unresolved validation debt, substantive progress, engine-definition change, and repeated warnings require stateful or distinct review.

EF-067, EF-059, and EF-068-substrate-load-bearing all sit on the latter side. Reviewer cost trajectory, repeated Read/tool-failure patterns, and substrate-at-session-open compliance are cross-session-state claims. They should not be accepted as prose self-report once the engine has named them as load-bearing. The shift should be targeted: harness-side measurement for these surfaces, guided self-assessment elsewhere.

## Q2 — Minimum viable is necessary but not sufficient

The S062 §10.4-M16 P2 precedent matters, but EF-059’s activation preconditions are now satisfied per `engine-feedback/triage/EF-059-harness-telemetry-feed-for-tier-2-reviewer.md`, and EF-068 extends the same missing primitive. A pure α/β resolution would close only the easiest visible symptom: substrate non-use at session open. It would not resolve reviewer-cost laundering or failed-tool/repeated-Read invisibility.

I therefore favor a staged resolution: adopt a bounded β-like step immediately, but treat it as phase 1 of ε, not as closure of the joint-scope. The root-cause direction remains γ, but γ should be specified as a measurement contract before committing to a specific capture mechanism.

## Q3 — Load substrate tools by default

Load-by-default is warranted. Design-space §7 Q3 estimates the schema cost around 1,000 tokens for the three retrieval tools, trivial against the session-open context budget. The empirical record is stronger than the theoretical concern: EF-068-substrate-load-bearing reports that “organic-use opportunity” produced n→0 use, and design-space §3.1 extends the pattern to n=5 by S070.

The deferred-tool friction is not valuable pedagogy if it reliably prevents use. Discoverability can be preserved through `prompts/development.md` text and explicit session-open reporting; it does not require hiding the tools behind ToolSearch.

## Q4 — z6 scope should include all three measured surfaces, but separate measured facts from semantic claims

The digest should cover failed tool calls, repeated Reads, reviewer invocation wall-clock/token count where available, and orchestrator-side substrate/read telemetry. These are the measurement primitives shared across EF-059, EF-067, and EF-068.

I would narrow one item from design-space §5.4: `decision_claims_with_evidence_pointers` is not purely harness telemetry. The harness can measure that a decision cited a spec section or ledger row; it cannot measure that the citation was substantively adequate. That field should be typed as “declared evidence pointer inventory,” not as ground truth. The reviewer then judges adequacy under Tier 2.5 §3, consistent with `validation-approach.md` v7’s tripartite audit distinction.

## Q5 — No CM is Pareto-dominant; specify digest authority first

CM1 and CM2 are strongest because they displace self-report at the point of capture. CM1 is attractive for this workspace if Claude Code hooks are available, but it binds the engine’s first implementation to one harness. CM2 is more portable but adds an operational layer. CM3 is useful as backfill or independent reconstruction if transcripts exist, but it is weaker than live capture. CM4 is not harness-side measurement; it is structured self-report and should not be treated as γ.

The design-space §5.4 candidates are adequate as implementation candidates, but they miss a prior axis: digest records need `producer_kind` and `authority_level`. A digest emitted by CM1/CM2 can carry “harness-measured”; CM3 can carry “post-hoc reconstructed”; CM4 can carry “agent-declared.” That prevents a future session from laundering CM4 into γ merely because the YAML shape exists. This reframe is grounded in the workspace’s own `retrieval-contract.md` §Purpose split between contract and implementation, though the producer/authority vocabulary is also influenced by [external import: common software-engineering observability and adapter-layer practice].

## Q6 — Direction B final; A-for-authority during transition; C only as disclosure

EF-067’s A/B/C framing conflates field presence with evidentiary authority. My position:

- Final state: Direction B. Reviewer wall-clock and token count belong in z6 as harness-measured fields.
- Until then: self-reported reviewer cost must not drive §10.4-M25 P1 budget thresholds. That is Direction A for authority, even if the prose note remains for historical traceability.
- Direction C alone is too weak if the self-report remains numerically active.

So I would preserve reviewer self-report only as explicitly non-evidentiary disclosure, and suspend budget-warrant arithmetic until harness-measured values exist.

## Q7 — Check 29 should use structured 00-assessment declaration plus close corroboration

Close-narrative grep alone is too late and too heuristic. Design-space §7 Q7 correctly notes the check 27 over-fire precedent. The minimum viable check 29 should require a structured declaration in `00-assessment.md`, mirrored or summarized in `03-close.md`:

`substrate_session_open: exercised | unavailable | skipped`
`substrate_evidence: <tool + target + result pointer or degradation reason>`

This remains self-report until z6 exists, so WARN-only is right. But structured declaration is better than substring grep, and 00-assessment coverage catches the actual session-open surface rather than allowing end-of-session retrofitting.

## Q8 — Hybrid adoption

Adopt β-bounded changes in the near term, then run γ as a multi-session phase-3 arc. This matches design-space §10.2 observation 5: α/β can be same-session-bounded; γ requires multi-session implementation. It also avoids letting “γ is hard” become renewed deferral, because EF-059’s triage says all activation preconditions are satisfied and continued deferral would be “deferral-without-rationale.”

## Q9 — Do not open the four-record bundle now

I would defer EF-068-read-write-rebalance from this S071 bundle. It is structurally related through the broader “passive maintenance” concern, but operationally distinct. The current three-record scope asks how to make cross-session-state claims observable. The sibling read/write rebalance asks whether default-read and forced-write surfaces should be reduced or reweighted.

Those questions should use telemetry produced by this arc. In particular, z6 `files_read_at_session_open` and substrate-use data can later show whether default-read is wasteful, insufficient, or merely unmeasured. Opening the four-record bundle now risks mixing “measure the surface” with “redesign the surface” before the engine has evidence. Preserve the operator-discretionary reopen warrant from EF-068 triage, but do not activate it by default.

## Q10 — β is engine-v13; γ is substantive and likely a later version bump

Any prompt or validator change is an engine-definition change under the manifest discipline, so β is an engine-v13 candidate even if narrow. Full γ is more than a minor amendment: it changes `validation-approach.md` §(z6), Tier 2.5 audit inputs, reviewer prompt expectations, and potentially read-contract behavior. If staged, I would expect v13 for β and a later substantive bump for the digest contract and implementation. Collapsing both into one v13 is possible but increases bootstrap risk.

## Cross-product candidate position

I favor ε, modified in two ways: first-stage β should include load-by-default, required `forward_references('S<NNN>')`, and WARN-only structured check 29; second-stage γ should begin by specifying digest authority semantics before choosing CM1/CM2/CM3.

I oppose α as too weak: it repeats the spec-side pattern except for `.mcp.json`. I oppose δ as a primary response because check 26 substrate-awareness is useful but narrow; it demonstrates substrate preference inside validation, not telemetry coverage for the three-record joint-scope. I oppose immediate full γ if it means committing to Claude-Code-specific CM1 before the digest contract is stable. I support γ as the destination.

The adoption shape should be hybrid: same-session-bounded minimum viable enforcement, followed by a non-optional phase-3 digest arc with named acceptance criteria.

## Frame critique

The design-space §3-§7 covers the main choice surface well. The missing frame is measurement-authority separation. “Digest exists” is not enough; the engine must preserve whether a field is harness-measured, post-hoc reconstructed, or agent-declared. Without that distinction, the workspace can recreate EF-067 in YAML form.

Second, check 29 should not be framed as “did the narrative mention substrate?” The more precise frame is “did the session produce a session-open evidence object?” That can start as structured self-report and later become digest-backed.

Third, reviewer-prompt-template version should be a digest input. `validation-approach.md` v7 already includes `reviewer_prompt_template_version` and z7 lock-in-after-n=2. If reviewer cost fields or digest-required inputs vary by template version, the digest and audit should record that coupling explicitly.

## Honest limits

I reason only from the supplied briefs, records, and adjacent specs/tool snippets. I have no access to the other S071 perspectives or the orchestrator’s synthesis context.

My “producer_kind / authority_level” reframe is partly grounded in the workspace’s contract-vs-implementation pattern from `retrieval-contract.md`, but also reflects [external import: common observability/structured logging practice]. Treat it as a candidate vocabulary, not as committed workspace doctrine.

As a codex-family participant, I reduce Claude-family framing concentration at organisation level, but I still share broad software-engineering priors with other model families.

## Dissent-preservation

If synthesis adopts α or β as full closure, preserve this dissent: minimum viable substrate enforcement does not resolve EF-059 or EF-067; it only reduces one EF-068 symptom.

If synthesis adopts immediate γ, preserve this dissent: the digest contract should distinguish harness-measured, post-hoc reconstructed, and agent-declared fields before any implementation is allowed to satisfy z6.

If synthesis opens the four-record bundle, preserve this dissent: read/write rebalance should be informed by telemetry from this arc, not bundled into the measurement-primitive decision.