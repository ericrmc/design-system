---
id: EF-075-reviewer-cost-not-optimization-target
source_workspace_id: selvedge-self-development
source_session: 075
target: methodology
severity: observation
status: new
reported_by: operator
filed_at: 2026-04-26
---

# Reviewer wall-clock + token count is optional, not an optimization target

## Summary

Operator note at S075 post-close intake: the reviewer's `duration_minutes` and `reviewer_cost` fields (currently REVD-2-quarantined per S073 D-279 with planned REVD-3 retrospective re-baseline post-S076) are **not** values the engine needs to optimize for. The audit mechanism's value justifies its cost; cost-measurement is not load-bearing.

This is a substantive reframe of the in-flight EF-067 disposition arc. The current plan (S071 D-264 + S073 D-279) treats reviewer cost as something that requires quarantine NOW (REVD-2) and harness-measurement LATER (REVD-3), with §10.4-M25 P1 audit-cost-budget threshold arithmetic re-activating against the harness-measured baseline once n≥2 stable observations exist. The operator note removes the "later" half of that plan: harness-measured reviewer cost is acceptable if convenient but not required, and the threshold arithmetic does not need to re-activate.

## Operator note (S075 post-close intake)

> "The wall-clock + token count for reviewer can be optional, it's not a cost you need to optimise for. The system needs the audit mechanism without a doubt, so it's worth it."

The framing is binding-policy on cost-treatment, not binding-policy on capture-mechanism (CM1+CM3 stay; reviewer_invocations: section in SCD-3 schema stays). What changes is whether populating that section's harness-measured fields is required vs optional, and whether §10.4-M25 P1 threshold arithmetic ever re-activates.

## Implications for in-flight arc

**EF-067 → REVD-3 disposition (S073 D-279)**: REVD-3 retrospective re-baseline becomes **optional** rather than scheduled. REVD-2 quarantine semantics (`producer_kind: agent-declared`, `authority_level: tertiary`, excluded from §10.4-M25 P1 threshold arithmetic) can persist indefinitely without REVD-3 transition.

**§10.4-M25 P1 audit-cost-budget threshold arithmetic suspension (S071 D-264 + extended at S073 D-279)**: suspension persists indefinitely, not "pending harness-measurement availability". The reopen warrant text in `validation-approach.md` v9 §Tier 2.5 reviewer self-report honest-limit subsection should be updated to reflect "indefinitely-suspended per operator-directive at S075" rather than "suspended pending REVD-3".

**SCD-3 schema reviewer_invocations: section (codified at S075 D-294 in v9 §(z6))**: schema stays as specified; populating `wall_clock_seconds` and `token_count` with `producer_kind: harness-measured` is **optional** rather than the eventual target state. Reviewer self-reports at `producer_kind: agent-declared` + `authority_level: tertiary` is the steady-state shape.

**VD-003 phase-3 activation gating condition (b)** (observation window data on β-phase substrate-use distinguishing durable behavior change from design-space-salience compliance): independent of this reframe. (b) is about substrate-use observation, not reviewer-cost observation. Continues to discharge at S076 review per existing schedule (n=5 first-triangulation-floor reached at S075).

**S073 D-279 REVD-2 → REVD-3 transition language**: stays as specified-but-conditional. The REVD-3 mechanism is preserved as standing capacity (cost data could become useful later if the engine's situation changes); operator-note sets the activation precondition to operator-discretionary rather than scheduled.

## Candidate disposition at S076 VD-003 review

S076 is the VD-003 review session. The natural place to integrate this reframe is in S076's VD-003 disposition. Possible shapes:

1. **VD-003 fully resolved at S076** with REVD-3 explicitly named as deferred-indefinite per operator-note; reviewer cost self-report stays REVD-2 quarantined as steady-state.
2. **VD-003 resolved at S076 with `reopen warrant`** preserving REVD-3 mechanism for future activation if cost-pressure surfaces operationally.
3. **Minor amendment to validation-approach.md v9** §Tier 2.5 reviewer self-report honest-limit subsection (or equivalent) codifying the indefinite-suspension framing per operator-directive.

Disposition selection is S076's call; not pre-ratifying at intake.

## Cross-linkage

- **EF-067 reviewer-wall-clock-self-report-unreliable** — directly affects this record's disposition; the original three-direction question (drop / subsume into EF-059 / honest-limit-only disclosure) is answered differently under this reframe: Direction C (honest-limit-only disclosure) becomes the steady-state shape rather than Direction B (subsume into (z6) digest with harness-measured fields) being the eventual target.
- **EF-059 harness-telemetry-feed-for-tier-2-reviewer** — orthogonal: EF-059 covers digest production for substrate-use telemetry, which remains in scope. Reviewer-cost telemetry is one section of the SCD-3 schema; this reframe makes that section optional rather than required.
- **§10.4-M25 P1 cadence-depth + audit-cost-budget co-preservation minority (S064)** — the audit-cost-budget half of M25 effectively becomes inactive under this reframe; the cadence-depth half is independent and continues.
- **S073 D-279 REVD-2 quarantine + REVD-3 retrospective re-baseline** — REVD-3 transition becomes operator-discretionary rather than scheduled.
- **S075 D-294 v9 §(z6) SCD-3 schema codification** — schema preserved; population of harness-measured reviewer_invocations fields becomes optional.
- **EF-075-reviewer-side-substrate-use** (sibling intake) — same operator-conversation; both observations were operator-surfaced together at S075 post-close. Cost-not-optimization-target framing reduces concern about substrate-querying overhead in the v4 template extension scope considered in that record.

## Triage notes

Operator-surfaced post-session intake at S075 close. **Ninth-of-record operator-surfaced intake** (after EF-054 + EF-055 + EF-058×3 + EF-067 + EF-068×2 + EF-073 + EF-075-reviewer-side-substrate-use). Observation-class shape but with substantive disposition implications for the in-flight EF-067 / VD-003 arc. **Operator-direct binding-policy** on cost-treatment per §10.4-M10 written-warrant clause (c) operator-surfacing channel pattern; not advancing the cumulative count at intake (the intake is post-close observation-class, not session-open direction-setting; consistent with EF-067 + EF-068×2 prior operator-surfaced post-close intakes).

The pattern: **operator-direct policy-level reframes of in-flight disposition arcs**, similar in shape to S074 D-286 supersession-then-resumption discipline applied at the post-close intake stage rather than the session-open direction-setting stage. Future Path-PD or Path-AS scope at S076+ to integrate.
