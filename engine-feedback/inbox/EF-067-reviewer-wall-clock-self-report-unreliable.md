---
feedback_id: EF-067-reviewer-wall-clock-self-report-unreliable
source_workspace_id: selvedge-self-development
source_session: 067
created_at: 2026-04-26T12:45:00Z
reported_by: operator
target: methodology
target_files:
  - provenance/067-session/04-tier-2-audit.md
  - provenance/067-session/03-close.md
  - specifications/validation-approach.md
  - engine-feedback/inbox/EF-059-harness-telemetry-feed-for-tier-2-reviewer.md
severity: observation
status: new
---

## Observation

The Tier 2.5 (γ) reviewer audit at `provenance/067-session/04-tier-2-audit.md` §8 reports `Wall-clock duration: 25 minutes (including thorough diff and source code review)` and `Estimated token usage: ~35,000 tokens`. The operator surfaced post-S067-close that **Gemini does not have wall-clock access; the 25-minute figure is the model's self-report echoing the S063 baseline that the Case Steward supplied in the reviewer-prompt template** as a reference comparison ("Compare to S063 baseline (~25 minutes; ~45,000 tokens) and S064 baseline (~55 minutes)"). The token estimate has the same caveat — Gemini does not have a token counter accessible to its own reasoning chain.

Actual wall-clock evidence: file mtimes show `00-assessment.md` at 12:18 and `04-tier-2-audit.md` at 12:29 — the entire S067 work-stretch (refactor + validate + VD-002 update + reviewer invocation + audit-write) was ~11 minutes. The reviewer invocation alone was approximately 3-5 minutes (with quota-throttling retries visible in `/tmp/s067-gemini-reviewer-output.log`).

The S063 first triggered (γ) reviewer audit (`provenance/063-session/04-tier-2-audit.md`) likely has the **same self-report problem** in its own §8 — that's where the "25 min" baseline used as the cross-session reference originated. The S064 codex audit's `~55 min` may also be a self-report; codex's behaviour around wall-clock self-reporting is similarly suspect.

The unreliable figures propagated into:
- `provenance/067-session/04-tier-2-audit.md` §6 (`duration_minutes: 25`).
- `provenance/067-session/03-close.md` §6 WX-62-1 5-field recording (`reviewer_cost: ~25 wall-clock minutes`) + cumulative cross-session table comparing S063 / S064 / S067 wall-clock.
- The S067 commit message body (cost variance "25-55 min / 35K-70K tokens").
- `provenance/067-session/02-decisions.md` D-246 (cost variance language).
- The §10.4-M25 P1 audit-cost-budget evaluation (`reviewer-cost growth >2× over S063 baseline (~25 wall-clock minutes / ~45,000 tokens)` reopen-warrant text).

## Why It Matters

This is a **methodology-level laundering surface** distinct from EF-058-tier-2-validation's origin concern but operationally adjacent:

1. **Reviewer self-report is treated as evidence.** The §Tier 2.5 audit shape per `validation-approach.md` v7 explicitly names `duration_minutes` as a frontmatter field and `reviewer_cost` as a WX-62-1 5-field recording field. Both fields are populated by reviewer self-report; neither is harness-measured. The fields are then used in `§10.4-M25 P1 audit-cost-budget` reopen-warrants ("reviewer-cost growth >2× over S063 baseline") — a budget threshold whose triggering signal is the unreliable self-report.

2. **Cross-session comparison amplifies the problem.** The S063 baseline that I cited in the S067 reviewer-prompt template was itself likely a Gemini self-report (S063 reviewer was Gemini). Subsequent reviewers anchor to that baseline because the prompt template instructs them to. The chain of self-reports anchored to the original self-report is a closed loop: each reviewer compares its self-report to the prior reviewer's self-report; no harness-measured ground truth ever enters the chain.

3. **EF-059 cross-linkage.** This observation directly extends EF-059's `(z6) harness-telemetry-digest` scope. EF-059 named "failed-tool-calls" and "repeated-Reads" as the digest's intended detection targets. **Reviewer-cost measurement is structurally the same kind of harness-side measurement** — it requires the harness (not the model under review) to record the metric. EF-067 could be subsumed by EF-059 if the (z6) digest specification is extended to include `reviewer_invocation_wall_clock_seconds` + `reviewer_invocation_token_count` as required fields. Alternatively EF-067 stands alone as a more narrowly-scoped patch (drop the unreliable fields entirely; require harness-measured fields only when available).

4. **The S067 audit cited the self-report values in its own §3 trajectory-discipline section** (`§3c Trajectory discipline: ... reviewer family choice ... maintains the cross-family audit discipline`). The audit's substantive engagement was real (tripartite §3; refactor verified); but its cost-self-report cannot be cited as evidence of audit-cost discipline.

## Suggested Change

Three candidate directions (not pre-committed; for triage):

**Direction A — drop reviewer self-report fields entirely.** Remove `duration_minutes` from `validation-approach.md` v7 §Tier 2.5 audit-shape frontmatter. Remove `reviewer_cost` from WX-62-1 5-field recording (or rename to `reviewer_cost_self_reported` with an explicit honest-limit caveat in spec text). Remove cost-comparison cross-session table from close-narratives. The §10.4-M25 P1 audit-cost-budget reopen-warrant becomes inactive (or is rewritten to use a harness-measurable proxy). Smallest scope; closes the laundering surface immediately. Reviewer audits remain valid on substantive engagement (tripartite §3); cost-budget discipline is deferred to harness-telemetry availability.

**Direction B — subsume into EF-059 (z6) digest scope.** Extend EF-059's `(z6) harness-telemetry-digest` specification (in `validation-approach.md` v7 §(z6)) to include `reviewer_invocation_wall_clock_seconds` + `reviewer_invocation_token_count` as harness-measured fields. The (z6) implementation arc (currently deferred per S062 D-225 activation preconditions; (a) reviewer mechanism adopted ✓ at S063; (b) ≥3 sessions per WX-62-1 ✓ at S067; (c) ≥1 instance documented where digest would have caught failed-tool-call or repeated-Read pattern given digest access — arguably extends to "≥1 instance documented where harness-measured duration would have caught a reviewer self-report inaccuracy" per this EF-067) becomes activatable now. Larger scope; addresses the root cause; defers correction until (z6) implementation lands.

**Direction C — flag as honest-limit only; preserve current spec.** Add a §Tier 2.5 honest-limit subsection to `validation-approach.md` v7 disclosing that `duration_minutes` and `reviewer_cost` are reviewer self-reports and do not constitute harness-measured ground truth. Continue using the fields with the explicit caveat. Smallest spec-text change; preserves the cost-comparison cross-session pattern but with honest disclosure. The §10.4-M25 P1 audit-cost-budget reopen-warrant is preserved with the same honest-limit caveat. Closes the implicit-evidence-treatment problem without committing to harness-measurement.

**Cross-linkage with EF-059**: Direction B is the (z6)-extension path; Direction A is the minimum-viable-response path; Direction C is the disclosure-only path. The triage decision depends on EF-059 triage scope at S068+ — if EF-059 triage adopts the (z6) implementation arc, EF-067 should subsume into the same arc (Direction B). If EF-059 triage defers (z6) further, Direction A or C are the standalone responses.

## Evidence

- `provenance/067-session/04-tier-2-audit.md` §6 (`duration_minutes: 25`) + §8 (`Wall-clock duration: 25 minutes`).
- `/tmp/s067-reviewer-prompt.md` §Audit shape — the line "§8 Reviewer cost note: tokens (estimated) or wall-clock minutes. Compare to S063 baseline (~25 minutes; ~45,000 tokens) and S064 baseline (~55 minutes)" — this is the source of the baseline that Gemini echoed.
- `/tmp/s067-gemini-reviewer-output.log` — quota-throttling retry pattern visible (multiple `Attempt 1 failed: ... Retrying after Xs...` lines with 5-7s backoffs); actual reviewer wall-clock duration approximately 3-5 minutes including retries.
- File mtimes: `provenance/067-session/00-assessment.md` at 12:18; `provenance/067-session/04-tier-2-audit.md` at 12:29 — the full S067 work-stretch (refactor + validate + VD-002 update + reviewer invocation + audit-write) was ~11 minutes total.
- `provenance/063-session/04-tier-2-audit.md` §8 (the original baseline source) — unaudited at S063 close per S063 close §6 honest-limit on first-of-record reviewer baseline.
- `engine-feedback/inbox/EF-059-harness-telemetry-feed-for-tier-2-reviewer.md` — cross-linkage to (z6) harness-telemetry-digest scope per Direction B.
- `provenance/067-session/03-close.md` §6 + §8 + §10 propagation surface.
- `provenance/067-session/02-decisions.md` D-246 propagation surface.

## Application-Scope Disposition

**Self-development workspace** (this workspace). The observation surfaced post-S067 close in operator-surfaced discussion. The S067 close is committed and immutable per D-017; correction belongs in S068 per the workspace's "errors recorded in subsequent sessions" discipline.

S068 triage scope candidates:
- **Bundle with EF-059 triage** (which is operationally schedulable from S068+ per WX-62-1 closure at S067; activation precondition (b) "≥3 sessions per WX-62-1 observation window" satisfied). EF-067 surfaces an additional concrete instance where the (z6) digest would have caught a discipline-gap (reviewer-self-report inaccuracy); this strengthens EF-059's activation evidence per its precondition (c).
- **Standalone Path PD or Path AS Shape-1** if scope-coherent independent of EF-059 (Direction A or C are tractable single-orchestrator).
- **Operator-discretionary** depending on operator preference for direction.

The S068 close at minimum should record an honest-limit annotation acknowledging the propagated S067 wall-clock self-report surface; whether the spec/audit-shape is amended at S068 depends on triage outcome.

**Operator-audit cadence note**: this finding emerged from operator post-close audit per `validation-approach.md` v7 Layer 6.2 standing cadence ("operator-discretionary at any close"). Layer 6.2 functioned as designed at S067 — operator audited the close-narrative + reviewer audit and surfaced a substantive concern that the in-session orchestrator + reviewer did not catch. **This is a working example of the bootstrap-paradox layered handling per `validation-approach.md` v7 §Bootstrap-Paradox Layered Handling Layer 6**: the layered cross-checks include operator-audit precisely because in-session reviewer + orchestrator can share blind spots. The operator-audit-as-laundering-detection pattern was first-of-record at S063 + S064 resolving closes (operator surfaced S063 first-instance findings disputing first-instance §Tier 2.5 implementation that drove S064 MAD); EF-067 is the **second-of-record operator-audit-catches-what-in-session-discipline-missed event**.
