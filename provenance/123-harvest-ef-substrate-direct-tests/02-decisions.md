---
session: 123
title: harvest-ef-substrate-direct-tests — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Add substrate-direct harvest-ef test coverage closing OI-S121-1: dry-run plan, import+ledger, idempotency, since-session filter.

**Kind:** substantive.  **Outcome:** adopt process_rule `harvest-ef-substrate-direct-test-coverage`.

**Why.**

- (engine_feedback) EF-S121-1 named the absent harvest-ef test coverage as the root cause that let S119 and S120 ship on a red suite; closing this gap closes the loop EF-S121-1 surfaced. [EF-S121-1]
- (prior_decision) S121 deferred the substrate-direct test rewrite to OI-S121-1 explicitly; the gap was adjudicated intentional pending this session. [DV-S121-1]

**Effects.**

- creates harvest-ef substrate-direct test coverage in test_monitor_external
- closes_issue OI-S121-1 — OI-S121-1 substrate-direct harvest-ef test rewrite

**Rejected alternatives.**

- **R-1.1.** Defer harvest-ef test coverage further and rely on operator observation in production runs.
  - (no_feedback_loop) EF-S121-1 already established that absent tests let the review loop ship a red suite; further deferral repeats the same root cause and breaks the substrate-enforced coding review loop.
