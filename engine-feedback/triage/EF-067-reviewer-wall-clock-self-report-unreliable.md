---
feedback_ref: engine-feedback/inbox/EF-067-reviewer-wall-clock-self-report-unreliable.md
triage_session: 068
status: deferred
classification: substantive-arc-via-cross-linkage
---

# Triage — EF-067 Reviewer Wall-Clock Self-Report Unreliable

## Triage classification

**Classification: substantive-arc-via-cross-linkage**.

EF-067 admits three candidate directions (A/B/C per intake §Suggested Change). The choice between them is non-trivial and cross-linked with EF-059 `(z6) harness-telemetry-digest` scope. Specifically:

- **Direction A** (drop self-report fields entirely from `validation-approach.md` v7 §Tier 2.5 audit-shape frontmatter + WX-62-1 5-field recording per Layer 6.3): bounded; same-session or near-session resolvable; closes laundering surface immediately at minimum scope. Analogous to S062 §10.4-M16 P2 minimum-viable-response position.
- **Direction B** (subsume into EF-059 (z6) digest scope; extend (z6) spec to include harness-measured `reviewer_invocation_wall_clock_seconds` + `reviewer_invocation_token_count`): structurally subsumes EF-067 in EF-059's larger implementation arc; addresses root cause via harness-measurement; defers correction until (z6) implementation lands.
- **Direction C** (honest-limit-only disclosure): smallest spec-text change; preserves cost-comparison cross-session pattern with explicit caveat; preserves §10.4-M25 P1 audit-cost-budget reopen-warrant with caveat.

The Direction-A-vs-B-vs-C decision is itself substantive-arc-class scope per `multi-agent-deliberation.md` v4 §When Multi-Agent Deliberation Is Required clause 3 (the question is one on which reasonable practitioners could genuinely disagree — the session author can name three plausible positions before deliberation begins). Cross-linkage with EF-059 makes the decision joint-scope: Direction B is a candidate because the (z6) digest scope can subsume the reviewer-cost-measurement concern; Direction A or C are the standalone-EF-067 paths that don't depend on (z6) implementation.

**Per S062 D-225 EF-059 deferred-implementation precedent + S061 Path AS Shape-1 phase-1 synthesis precedent**: substantive-arc-class with cross-linkage is appropriately resolved through Path AS Shape-1 phase-1 synthesis (design-space.md surveying Directions A/B/C × EF-059 (z6) implementation choice; Q1-Q10 design questions; pre-ratification of phase-2 MAD).

## Triage disposition

**Disposition**: substantive-arc-deferred-via-cross-linkage to **joint-scope with EF-059** at S069+ Path AS Shape-1 phase-1 synthesis per D-251 (cross-linkage joint-scope decision).

**Resolution path forecast**:
- **S069+ Path AS Shape-1**: phase-1 synthesis on EF-059 + EF-067 joint-scope. Produces `provenance/<NNN-session>/design-space.md` surveying Directions A/B/C × (z6) digest-scope question + Q1-Q10 design questions + pre-ratification of phase-2 MAD per S057 Path AS Shape-1 precedent.
- **S069+1 Path AS-MAD-execution**: 4-perspective two-family MAD per S058 + S062 lineup precedent. Synthesizes adoption direction.
- **S069+2 Path L (single-orchestrator phase-3 adoption)** or same-session-bounded adoption per S062 D-220 precedent: implements adopted direction.

The arc shape is analogous to EF-058-tier-2-validation arc S061 (Shape-1) → S062 (MAD-execution) → S063 (phase-3). Joint-scope with EF-059 means one design-space surveys both records simultaneously.

**Alternative dispositions considered and rejected**:

1. **Same-session-resolution adopting Direction A at S068**: rejected at triage scope. S068 is Path T (single-orchestrator triage); adopting Direction A requires substantive revision to `validation-approach.md` v7 (drop fields from audit-shape contract + drop `reviewer_cost` field semantics from WX-62-1 5-field per Layer 6.3 + add §Honest limits subsection disclosing reviewer self-report limitation). This is engine-definition substantive revision per OI-002 substantive scope; engine-version increment to thirteenth-engine-version. Single-orchestrator implementation of bounded Direction A without first surveying A/B/C alternatives in a phase-1 synthesis (per Path AS Shape-1 precedent) would skip the workspace's design-space-then-decide discipline. **Path L could be adopted at S069+ post-triage if operator surfaces preference for Direction A as minimum-viable-response**; the triage classification preserves that option without committing to it.

2. **Separate-scope EF-067 triage to Direction A standalone**: rejected because the cross-linkage with EF-059 (Direction B path) is operationally significant; separating scope risks adopting Direction A at S069+ Path L while EF-059 (z6) implementation arc later surfaces the same surface differently, requiring rework. Joint-scope addresses both records in one design-space-then-decide cycle.

3. **Reject EF-067 (no action warranted)**: rejected because the operator surfaced concrete substantive concern (per Layer 6.2 cadence audit at S067 post-close); the laundering surface is real (reviewer-self-report-treated-as-evidence per intake §Why It Matters point 1); workspace has discipline for addressing operator-surfaced concerns.

4. **Defer EF-067 indefinitely (until additional instances accumulate)**: rejected because EF-067 is the n=1 concrete instance, but EF-059's activation precondition (c) was already satisfied per EF-067 strengthening; the (z6) digest implementation arc is operationally activatable. Indefinite deferral would not advance the engine forward.

## Cross-linkage with EF-059

EF-067 Direction B is **structurally subsumed in EF-059 (z6) digest scope**. EF-067 strengthens EF-059 activation precondition (c) by providing a concrete instance where harness-measured duration would catch a reviewer self-report inaccuracy. The (z6) digest implementation arc, when adopted, would add `reviewer_invocation_wall_clock_seconds` + `reviewer_invocation_token_count` as harness-measured fields available to the §Tier 2.5 reviewer; EF-067's underlying concern (reviewer self-report unreliable) is resolved as a side-effect of EF-059's primary scope (harness-telemetry digest for failed-tool-call + repeated-Read pattern detection).

Joint-scope rationale:
- One design-space surveys both records.
- One MAD addresses both questions.
- Direction B decision is the primary EF-067-vs-EF-059 cross-linkage choice.
- Implementation arc is unified.

Separate-scope rationale (rejected):
- EF-067 admits Direction A (minimum-viable; bounded) which doesn't require EF-059 (z6) implementation.
- EF-059 (z6) implementation is larger arc; adopting Direction A independently could resolve EF-067 sooner.

**Decision per D-251**: joint-scope adopted. EF-067 is bundled with EF-059 in S069+ Path AS Shape-1 phase-1 synthesis.

## Forward-recommendation

S069+ Path AS Shape-1 phase-1 synthesis on EF-067 + EF-059 joint-scope per D-251. Pre-ratify phase-2 MAD at S069+1 (or S069 close if operator surfaces preference for combined-session shape).

EF-067 triage record will be updated to `status: resolved` when phase-3 implementation lands (per resolution chain analogous to S058 D-199 → S063 D-228 EF-058-tier-2-validation resolved-via-multi-session-arc).
