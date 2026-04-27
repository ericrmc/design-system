---
session: 085
title: prompt-spec-bump — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Bump prompt-development and prompt-application to v2; defer re-decomposition

**Kind:** schema_migration.  **Outcome:** ratify spec_version `prompts-v2`.

**Why.**

- (operator_directive) Operator asked to update prompts so next session knows the v20 substrate-only flow.
- (review_finding) S084 markdown edits broke spec_versions sha invariant; v1 rows pointed at stale sha.

**Effects.**

- supersedes SPEC-prompt-development-v1
- supersedes SPEC-prompt-application-v1
- creates SPEC-prompt-development-v2
- creates SPEC-prompt-application-v2

**Rejected alternatives.**

- **R-1.1.** Re-decompose v2 into spec_clauses immediately (full substrate-canonical re-author).
  - (too_large_for_session) Re-decomposition is a focused subagent task; bundling it here would blow the session.
