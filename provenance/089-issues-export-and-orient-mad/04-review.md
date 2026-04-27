---
session: 089
title: issues-export-and-orient-mad — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high**: Issue export emitted compressed-body files without flagging that pre-S088 bodies are substrate-truncated; operators reading git could assume completeness.
  - **fixed.** Footer line added to every exported issue file noting substrate-canonical provenance and 4000-char cap.
- **high**: selvedge orient packet returned unbounded open_issues; large workspaces would blow context windows.
  - **fixed.** Cap added: top 30 by priority then surfaced_session_id; total_count and truncated flag exposed; markdown footer points at full-list query.
- **medium**: Reviewer questioned T-24 semantics: should it admit issue resolve when all linked work_items are completed? Yes — current code requires status IN (queued,leased) to fire refusal, so completed/failed admit the resolve.
  - **adjudicated.** By design: T-24 refuses only while work is actively in flight (queued or leased).
