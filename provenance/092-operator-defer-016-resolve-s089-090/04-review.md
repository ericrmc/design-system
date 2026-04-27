---
session: 092
title: operator-defer-016-resolve-s089-090 — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **critical**: _submit_issue_work_item does not enforce same-session membership between issue and work_item.
  - **adjudicated.** Cross-session linkage is design intent per DV-S089-1 (M:N admits one work_item closing multiple issues across sessions); this very session links S092 work_items to S089-surfaced issues.
- **medium**: _submit_issue_work_item validates work_item_id existence but not issue_id existence; inconsistent error path between alias and id forms.
  - **fixed.** Handler now SELECTs the issue_id when passed directly, raising E_NOT_FOUND consistently; pytest test_issue_work_item_unknown_issue_id_refused covers it.
- **medium**: T-25 string comparison on lease_expires_at assumes ISO8601 format without column-level CHECK enforcement.
  - **adjudicated.** ISO8601 lex ordering is a pre-existing workspace convention used by T-16 since migration 010; column-level CHECK enforcement is out of scope for OI-S089-2.
