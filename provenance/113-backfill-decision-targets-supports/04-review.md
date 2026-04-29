---
session: 113
title: backfill-decision-targets-supports — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high**: Reviewer flagged header scope mismatch: 17 UPDATEs vs 10 currently-NULL rows when reviewer queried the substrate.
  - **adjudicated.** Reviewer queried substrate post-apply and read remaining-NULL as scope. Pre/post counts confirm 17 effect UPDATEs applied (109 -> 92). Header counts match.
- **medium**: Forward-direction risk: handler still admits closes_issue effects without target if a future caller bypasses target field.
  - **adjudicated.** Out of scope for a backfill migration; T-27 already refuses post-v28 closes_issue without target_issue_id. Tightening opens_issue/supersedes is OI-086-003 family.

## Terminal passes

- **iteration 1** — findings @ `e859f0c`
  - Iter-1 returned 1 high (header-vs-current-state misread) and 1 medium (forward-direction drift); both adjudicated.
- **iteration 2** — clean @ `e859f0c`
  - Iter-2 clean: prior findings adjudicated, no new findings; backfill verified by pre/post NULL-count delta.
