---
title: Engine-v16 restart — blanket rejection of open engine-feedback records
date: 2026-04-27
session: 076
disposition: rejected-by-supersession
applies-to:
  - EF-075-integrity-by-construction-not-after-the-fact-detection
  - EF-075-reviewer-cost-not-optimization-target
  - EF-075-reviewer-side-substrate-use
  - EF-068-substrate-load-bearing-and-harness-telemetry
  - EF-068-read-write-rebalance
  - EF-067-reviewer-wall-clock-self-report-unreliable
  - EF-059-harness-telemetry-feed-for-tier-2-reviewer
  - EF-058-claude-md-tools-clause-not-cross-checked-by-mad
  - EF-047-brief-slot-template-hidden-arc-leakage
---

# Engine-v16 restart — blanket rejection of open engine-feedback records

At session 076 close, the nine engine-feedback records listed in `applies-to` are marked **rejected by supersession**. The rejection is operator-directed and applies because the engine-v16 trim retires the specifications and tooling against which each concern was raised. The successor design (sessions 077–078) addresses the underlying concerns at the architectural level rather than as point-fixes against the retired arrangement.

## Per-record supersession rationale

- **EF-075-integrity-by-construction-not-after-the-fact-detection** — the operator's critique that the engine detects integrity failures at audit time rather than preventing them at write time. Subsumed into `specifications/constraints.md` §2 ("Models treat failure as cheap") and the design implication that "friction at write time, not at audit time" is a successor requirement. Sessions 077–078 design the database substrate that enforces integrity at write.

- **EF-075-reviewer-cost-not-optimization-target** — the operator's policy that reviewer wall-clock and token count are optional rather than a budget threshold. Subsumed by the trim itself: the audit-shape elaborations on `validation-approach.md` v9 (reviewer-cost budget arithmetic, harness-measured invocation fields, REVD-3 retrospective re-baseline) are removed. Sessions 077–078 will redesign the reviewer audit shape.

- **EF-075-reviewer-side-substrate-use** — the observation that reviewer-prompt-template v3 instructed reviewers to inspect digest output but not to query the retrieval substrate. Superseded because the retrieval substrate, the digest schema, and reviewer-prompt-template v3 are all retired. Successor design will specify reviewer-side data access against whatever substrate it produces.

- **EF-068-substrate-load-bearing-and-harness-telemetry** — direction to make substrate use load-bearing at session-open and to extend digest scope to read-discipline telemetry. Superseded; the substrate is retired. The underlying concern (agents do not use available tools without structural friction) is preserved in `specifications/constraints.md` §2.

- **EF-068-read-write-rebalance** — direction to demote default-read surface and reduce forced-write rate. Operationally discharged by the trim itself: the closed-enumeration default-read is removed in `specifications/workspace.md`, and the housekeeping/forced-write rate is left unspecified pending the successor design.

- **EF-067-reviewer-wall-clock-self-report-unreliable** — observation that reviewer self-reported time was unreliable; three candidate dispositions (drop / subsume into digest / honest-limit-only). Superseded; reviewer self-report fields and the digest are both retired. Sessions 077–078 may reintroduce harness-measured reviewer telemetry against whatever substrate is built.

- **EF-059-harness-telemetry-feed-for-tier-2-reviewer** — proposal for a harness-telemetry digest as Tier 2.5 reviewer input. Superseded; the (z6) digest schema is retired with the trim. Sessions 077–078 may specify a successor reviewer-input arrangement.

- **EF-058-claude-md-tools-clause-not-cross-checked-by-mad** — observation that the S050 MAD landed on pip+venv without considering `uv` despite CLAUDE.md §Tools. Superseded; the underlying concern (single-perspective deliberation can miss known operator preferences) is preserved in `specifications/methodology.md` §When to convene multiple agents and `specifications/constraints.md` §3.

- **EF-047-brief-slot-template-hidden-arc-leakage** — concern about arc-plan slot-template hidden-view leakage in `prompts/application.md`. Superseded; the rewritten `prompts/application.md` is thin and does not carry the v8-era slot-template structure. Sessions 077–078 may reintroduce richer slot semantics if the successor design warrants.

## What is preserved

The operator-mediated observations themselves are preserved in `engine-feedback/inbox/` and `engine-feedback/triage/` as historical record. The empirical signal they carry — that the engine was over-instrumented, that reviewer cost was a false optimisation target, that integrity detection-after-the-fact was the wrong shape — is an input to the successor design, not a backlog of pending work.

## What this rejection does not do

- It does not endorse the underlying failure modes or pretend they are solved. The successor design is responsible for the architectural response.
- It does not delete the inbox or triage records. Preservation discipline applies; the records remain as the empirical base from which `specifications/constraints.md` was distilled.
- It does not change the engine-feedback pathway specification. The new `specifications/methodology.md` §Engine-feedback pathway describes the simpler path forward (single-file records at `engine-feedback/EF-<session>-<slug>.md`); the inbox/triage subdirectory structure from the prior arrangement persists in the workspace and can be migrated or archived when the successor design specifies the disposition.
