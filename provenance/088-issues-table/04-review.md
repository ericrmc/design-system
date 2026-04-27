---
session: 088
title: issues-table — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **critical**: Migration 009 used capability column name on role_write_capabilities; actual column is write_op per 001-initial.sql.
  - **fixed.** Edit applied: capability renamed to write_op in role_write_capabilities INSERT.
- **critical**: Migration 009 objects_new omitted created_at column added by 003; INSERT SELECT would have silently dropped it.
  - **fixed.** objects_new now declares created_at TEXT NOT NULL with strftime default; INSERT SELECT preserves the column.
- **high**: Reviewer flagged absence of T-06 immutability triggers on the four new issue tables.
  - **adjudicated.** By design: issues.status is mutable across sessions via the disposition handler; T-06 on issues would block status transitions. Content immutability is enforced via text_atoms T-06.
- **medium**: Reviewer noted T-23 self-loop trigger fires only on INSERT not UPDATE; CHECK constraint covers UPDATE separately.
  - **adjudicated.** CHECK constraint covers UPDATE; trigger is belt-and-suspenders for INSERT-time diagnostic clarity. Symmetry not required.
- **critical**: _submit_issue admitted caller-supplied status at INSERT; could insert resolved without disposition row, breaking audit contract.
  - **fixed.** _submit_issue now refuses caller-supplied status other than open; INSERT hard-codes open. All transitions must go through submit issue-disposition.
- **medium**: _submit_issue_disposition and _submit_issue_link reuse rejection_reason atom_type instead of dedicated issue_disposition_reason or issue_link_reason types.
  - **adjudicated.** Adding new atom_types requires recreating text_atoms (CHECK is on CREATE); deferred to a follow-up. No live query collides today.
## Iteration 2

- **high**: Migration 009 rewritten to skip objects-table recreation; issues do not register in objects.object_kind. Cross-table T-01 citation of issues by alias not supported.
  - **adjudicated.** Approved: dispatch use-case satisfied; no live alias-resolution code targets OI-* prefix. Future cross-citation can ship via a separate migration widening objects.object_kind.
