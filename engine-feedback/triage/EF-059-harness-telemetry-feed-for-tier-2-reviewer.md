---
feedback_ref: engine-feedback/inbox/EF-059-harness-telemetry-feed-for-tier-2-reviewer.md
triage_session: 068
status: deferred
classification: substantive-arc
---

# Triage — EF-059 Harness-Telemetry Feed for Tier 2 Reviewer

## Triage classification

**Classification: substantive-arc** (confirmed; this triage step ratifies S062 D-225's substantive-arc-class disposition per all activation preconditions now satisfied at S067-close + S067-post-close events).

EF-059 was filed at S062 close per S062 D-225 with three named activation preconditions:
- **(a)** Layer 2 (γ) reviewer mechanism adopted at S063 per S062 D-221.
- **(b)** Reviewer operating across ≥3 sessions per WX-62-1 observation window.
- **(c)** ≥1 instance documented where digest would have caught failed-tool-call or repeated-Read pattern given digest access.

**At S068 triage all three activation preconditions are satisfied**:
- **(a)** ✓ adopted at S063 D-228; engine-v11 ratified.
- **(b)** ✓ at S067 close per WX-62-1 closure 3-of-3 (cumulative pattern S063 v1 + S064 v2 + S067 v2 across two cross-family providers Gemini + codex).
- **(c)** ✓ extended at EF-067 to "≥1 instance documented where harness-measured duration would catch reviewer self-report inaccuracy". The S067 Gemini audit's `25 min` self-report (echoing the S063 baseline supplied in reviewer-prompt template) is a concrete instance where harness-measured wall-clock would have caught the inaccuracy. This extends the original (c) precondition's "failed-tool-call or repeated-Read pattern" framing to include the broader "harness-side measurement catches model-self-report inaccuracy" pattern.

The implementation arc is operationally activatable at S068+. Per S062 D-225 spec text + EF-058-tier-2-validation precedent (S057 Path AS Shape-1 phase-1 → S058 Path AS-MAD-execution → S058 same-session adoption shape; OR S061 phase-1 → S062 MAD → S063 phase-3 two-session arc shape): substantive-arc resolution proceeds via Path AS Shape-1 phase-1 synthesis at S069+.

## Triage disposition

**Disposition**: substantive-arc-deferred to S069+ Path AS Shape-1 phase-1 synthesis per D-251 cross-linkage joint-scope decision (bundled with EF-067).

**Joint-scope with EF-067 per D-251**:
- One design-space.md at S069+ surveys both EF-067 Direction A/B/C × EF-059 (z6) digest scope simultaneously.
- One MAD at S069+1 addresses both records' decisions.
- Implementation arc unified.

EF-067 strengthens EF-059 activation precondition (c) per concrete reviewer-self-report-inaccuracy instance.

**Resolution path forecast**:
- **S069+ Path AS Shape-1**: phase-1 synthesis on EF-059 + EF-067 joint-scope. Produces `provenance/<NNN-session>/design-space.md` surveying:
  - EF-059 (z6) digest scope: failed-tool-call detection; repeated-Read pattern detection; reviewer-cost measurement (per EF-067 cross-linkage); fallback-event recording; anomalous-pattern detection.
  - Implementation candidates: harness-side instrumentation hooks; transcript-parsing post-hoc digest; structured-log-emission protocol; tool-invocation-counter API.
  - EF-067 Directions A/B/C × EF-059 (z6) implementation choice cross-product.
  - Q1-Q10 design questions.
  - Pre-ratification of phase-2 MAD per S057 Path AS Shape-1 precedent.
- **S069+1 Path AS-MAD-execution**: 4-perspective two-family MAD per S058 + S062 lineup precedent (P1 Validator/Substrate Architect Claude + P2 Incrementalist Conservator Claude + P3 Outsider Frame-Completion non-Claude + P4 Cross-Family Reviewer non-Claude). Synthesizes adoption direction.
- **S069+2 Path L (single-orchestrator phase-3 adoption)** or same-session-bounded adoption per S062 D-220 precedent: implements adopted direction.

**Alternative dispositions considered and rejected**:

1. **Same-session-resolution at S068**: rejected. EF-059 (z6) implementation arc is multi-session per S062 D-225 spec. Single-orchestrator implementation at S068 would either adopt a narrow subset (which truncates the design-space) or skip the design-space-then-decide discipline.

2. **Defer further until additional (z6) surfaces accumulate**: rejected. All three named activation preconditions are satisfied. Continued deferral would not be principled per the activation-precondition discipline; it would be deferral-without-rationale.

3. **Separate-scope from EF-067**: rejected per D-251 cross-linkage joint-scope decision (see EF-067 triage record + D-251).

4. **Reject EF-059 (no action warranted)**: rejected. The activation preconditions exist precisely to gate the implementation arc to operationally-justified moments; (a) + (b) + (c) all satisfied means the gate is passed.

## Cross-linkage with EF-067

EF-067 strengthens EF-059 activation precondition (c). The reviewer-self-report-inaccuracy instance (S067 Gemini audit) is a concrete pattern that harness-telemetry digest would catch. This extends (z6) digest scope from the original "failed-tool-call + repeated-Read" framing to include "model-self-report-inaccuracy" detection — a strictly broader scope.

Joint-scope at S069+ Path AS Shape-1 design-space addresses:
- EF-059 (z6) primary scope: failed-tool-calls + repeated-Reads + fallback-events + anomalous-pattern detection.
- EF-067 cross-linkage: reviewer-cost-measurement (wall-clock + tokens) + reviewer-self-report-vs-harness-measured comparison.
- Direction B from EF-067 is structurally subsumed in (z6) extended scope.
- Direction A or C from EF-067 are standalone-EF-067 paths (not subsumed); design-space evaluates trade-offs.

**Decision per D-251**: joint-scope adopted.

## Forward-recommendation

S069+ Path AS Shape-1 phase-1 synthesis on EF-059 + EF-067 joint-scope per D-251.

Phase-2 MAD pre-ratified at S069+ Shape-1 close per S057 D-196 precedent.

Phase-3 implementation arc (adoption shape) determined by phase-2 MAD outcome per S062 D-220 precedent.

EF-059 triage record will be updated to `status: resolved` when phase-3 implementation lands.

## Notes

The S067 close §6 WX-62-1 5-field cumulative table characterised the mechanism as functioning across providers. EF-067 surfaces a refinement: the mechanism's evidence-base (reviewer-self-reported `duration_minutes` + `reviewer_cost`) is structurally unreliable. The (z6) digest scope addresses this evidence-base gap. The mechanism continues to function for substantive engagement (tripartite §3 evaluation; spec-text fidelity; refactor verification); the cost-measurement layer needs harness-side instrumentation per (z6).

This is consistent with `validation-approach.md` v7 §Tier 2.5 evidence-floor discipline ("findings_count: 0 with substantive §3 IS passing per evidence-floor discipline"): the substantive-§3 layer is reliable; the cost-self-report layer is the laundering surface that EF-059 (z6) addresses.
