---
session: 202
title: rolling-renewal-cycle-primitive-scoping — engine-feedback
generated_by: selvedge export --session
---

# Engine feedback

## EF-S202-1

- **flag.** observation
- **disposition.** (none)

**codex-shape-consult: S202 rolling-renewal cycle primitive (FR-S196-16 ratification)** — non-Anthropic-family read on session-shape and design-knot priorities for OI-S196-6.

**SESSION-SHAPE VERDICT.** SINGLE-SHIP. Codex argues evidence arc is mature enough that a coding session should decide-and-ship v1; six knots are implementation-shaping not discovery-blocking. Orchestrator preserves this as alternative R-1.1 in S202 procedural DV; meta-first chosen for substrate-recorded codex consult before deliberation-open (provenance-strength).

**KNOT POSITIONS (codex stance).** (1) Cycle-row locus: standalone `cycle_ledger` rows with required primary object FK and optional typed links; AR-child-only would collapse C-6 into C-1 sub_type. (2) Substantial classifier: hybrid — agent-judged + cited for substantial=true, plus substrate-assisted diff metadata; engine should not pretend semantic significance is mechanically derivable. (3) Auto-SR suppression: cycle row IS proof of observation; non-substantial emits no SL; substantial may cite SL when real supersession relation exists. (4) Trigger counter typing: typed `cycle_trigger` rows; query-only too implicit, handler-only hides important reasoning object. (5) Closure-path: reuse `closure_shape` from S201; new path enum would prematurely fork closure semantics. (6) Cross-artefact coupling v1: land polymorphic immediately with narrow object-kind allowlist; AR-only wrong starting abstraction given generalization core to C-6.

**GENERALIZATION-BLIND-SPOTS.** (a) Disaster-recovery overemphasizes improvement/worsening trajectories; many renewal cycles are no-material-change loops where stability itself is meaningful signal — operator's named cross-app concern. (b) Snapshots may bias toward operational allocations when other domains need attestations, thresholds, reviewer identity, confidence, policy-version context. (c) Closure may feel like incident-resolution; subscriptions/compliance/calibration often close by rollover, expiry, replacement, or stable continuation.

**PRIORITY-ORDERING.** Load-bearing-now: cycle-row-locus + auto-SR-suppression + trigger-counter-typing — these define whether C-6 is actually a primitive, whether it avoids SL noise, whether N-cycle reasoning is inspectable. Deferrable-v2: substantial-classifier-refinement + closure-path-expansion + broader-cross-artefact-rollout — ship cited hybrid classification simply, reuse closure_shape, narrow object-kind allowlist.

## EF-S202-2

- **flag.** observation
- **disposition.** (none)

**design-knot-inventory: S202 C-6 rolling-renewal cycle primitive scoping (6 knots for next coding session deliberation).**

**Knot 1 — cycle-row locus.** Polymorphic via objects-FK with object_kind admit-list at v1 (codex P-3 stance); AR-child-only collapses C-6 into C-1 sub_type and is rejected. Standalone `cycle_ledger` table with required `subject_object_id` FK to objects.object_id; admit-list at v1 includes assumption only, with explicit forward-direction for issue/decision_v2 once second-arc evidence surfaces.

**Knot 2 — substantial classifier.** Hybrid per codex: agent-judged-with-cite for substantial=true (substrate refuses uncited substantial-claim), substrate-assisted diff metadata optional. Two values: substantial | non-substantial (closed CHECK enum). Substantial requires `classification_reason_atom` 8-480; non-substantial admits NULL.

**Knot 3 — auto-SR-suppression mechanism.** Cycle row IS the substrate proof of observation per codex; non-substantial cycles emit zero supersession_ledger rows. Substantial cycles MAY cite an SL row via optional `citing_supersession_object_id` FK; handler does not auto-emit SL — operator/agent decides if supersession relation exists.

**Knot 4 — trigger counter typing.** Typed `cycle_trigger` child rows per codex; query-only implicit, handler-only hidden. Trigger row carries: parent_cycle_id (or parent_subject_id), trigger_kind closed-enum (n-consecutive-substantial | n-consecutive-non-substantial | window-elapsed | threshold-crossed), threshold_n, current_count, fired_at NULL until satisfied. Defer to v2 if scoping-density too high; v1 may ship cycles without typed triggers and add at v2 via calibration-EF graduation.

**Knot 5 — closure-path mechanism.** Reuse C-3 closure_shape enum from S201 per codex; no new cycle-specific closure_path enum. When parent assumption transitions to status=closed, closure_shape applies; cycle_ledger does NOT carry its own closure_shape column at v1 (cross-artefact unification deferred per DV-S201-1 binding).

**Knot 6 — cross-artefact coupling at v1.** Polymorphic immediately per codex with narrow allowlist (assumption only at v1); object_kind admit-list extends at v2 once cross-app evidence accumulates. Cycle alias format CYC-S<wno>-<seq> per S197/S198/S201 alias precedent.

**Codex priority-ordering for next session.** Load-bearing v1: knots 1, 3, 6 (locus + suppression + polymorphism). Deferrable-v2: knots 2, 4, 5 (classifier-refinement + trigger-typing + closure-path-expansion). Ship cited hybrid classification simply (substantial bool + reason atom), reuse closure_shape, narrow object-kind allowlist.

## EF-S202-3

- **flag.** observation
- **disposition.** (none)

**audit-step:** 4 load-bearing interpretive choices, 3 covered by sealed-decision-and-EF exclusions plus 1 lifted to AR-S202-1.

(1) Meta-first session-shape vs codex SINGLE-SHIP verdict: covered by DV-S202-1 R-1.1 rejection-reason (provenance-strength tradeoff over session-count optimization).

(2) Cross-application generalization commitment: lifted-to AR-S202-1 (operator-named at S202 turn, codex blind-spot-1 confirms, statement registers polymorphic-allowlist-at-v1 framing for next coding session deliberation).

(3) Skip 3-perspective formal deliberation in meta: accepted-implicit per S196 triage-meta precedent (meta sessions do not require deliberation_open + 3 perspectives + capture subagent + counterfactuals; codex consult recorded as EF-S202-1 substrate-resident observation IS the substantive non-Anthropic-family read; next coding session opens deliberation against the knots).

(4) Six-knot decomposition framing vs different knot count: accepted-implicit per codex-ratified inventory at EF-S202-1 (codex priority-ordering 1+3+6 load-bearing + 2+4+5 deferrable confirms 6-knot framing; codex would have surfaced missing or excessive knots in shape-consult).
