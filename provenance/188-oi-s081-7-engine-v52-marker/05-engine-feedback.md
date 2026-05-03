---
session: 188
title: oi-s081-7-engine-v52-marker — engine-feedback
generated_by: selvedge export --session
---

# Engine feedback

## EF-S188-1

- **flag.** observation
- **disposition.** addressed-by-DV-S188-1 (codex-shape-consult Q1+Q2+Q3+Q4 folded into migration design and reorder)

**codex-shape-consult:** S188 session shape confirmed by gpt-5.5 (single-arc kind=coding OK; no perspective convening required since OI-S081-7 is implementation of S081 DV-1 sealed design). Q1 single-arc admitted. Q2 export_manifest framed as recovery index (not audit log) keyed (session_no,kind,path) UNIQUE replace-on-rerun, sha256 post-write, no rows for unwritten files. Q3 omissions surfaced and folded: snapshot_catalog CHECK widening needs SQLite table rebuild; relative path normalization vs absolute; sha256 computed after file write; failed-export rows omitted; engine version monotonicity check; trigger allowlist sweep beyond VALID_TRIGGERS. Q4 reorder adopted: migration -> VALID_TRIGGERS -> take_snapshot keep_reason API -> deliberation-seal handler wire -> export_manifest writes -> tests -> reviewer.

## EF-S188-2

- **flag.** observation
- **disposition.** (none)

**audit-step:** 2 load-bearing interpretive choices.

1. UNIQUE(path) on export_manifest vs (session_no,kind,path): accepted-implicit — recorded as DV-S188-1 R-1.2 alternative with explicit rejection rationale (path is recovery identity by construction since each emitted file occupies one workspace path).
2. Defer harness-lifecycle test coverage to FR vs land in S188: deferred-to-FR — FR-S188-N (next_session_should item) carries the harness manifest test arc, with finding 41 adjudication noting schema-level admission of kind=harness already covered by test_migration_044.

Micro-decisions excluded: file ordering of changes (codex Q4 reorder); local naming (workspace_relative helper); two-branch INSERT in _record_catalog_row preserved per finding-44 adjudication.
