---
session: 087
title: redecompose-v2-specs — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **critical**: Reviewer asserts widened T-06 unintentionally admits body_canonical_in_substrate flips on all closed-session spec_version rows, not only the three backfilled ones.
  - **adjudicated.** Misread intent: the widening is deliberately broad to permit cross-session decomposition completion on any spec_version row.
- **medium**: Reviewer notes IS comparison is redundant vs = on body_canonical_in_substrate (NOT NULL column).
  - **adjudicated.** IS matches the pattern used by the prior T-06 status comparison in 001-initial.sql; consistency over micro-optimisation, no behavioural difference.
