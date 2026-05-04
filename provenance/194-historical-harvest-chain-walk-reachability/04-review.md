---
session: 194
title: historical-harvest-chain-walk-reachability — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high**: orient relevant_history_anchored query returns rows-per-anchor (multiple per feedback) but rh_total counts DISTINCT feedback_id; LIMIT 10 caps anchor-rows not unique-feedbacks breaking elision-count math.
  - **fixed.** selvedge/orient.py rh_total query changed to COUNT(*) anchor edges (matches LIMIT-10 row semantics); regression test test_orient_total_counts_anchor_edges_not_distinct_efs added asserting dual-anchor EF counts as 2.
- **low**: Test suite missing edge case: no test for empty anchor-target set scenario where 0 active specs plus 0 recent decisions.
  - **adjudicated.** Empty-anchor-target edge case left uncovered at v1: query handles correctly (returns 0 rows) and has no failure mode; coverage gap acceptable per low severity.

## Terminal passes

- **iteration 2** — clean @ `adb65e5`
  - S194 iter-2 clean; iter-1 HIGH (elision math) fixed and regression-tested; iter-1 LOW adjudicated.
