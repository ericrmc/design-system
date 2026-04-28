---
session: 107
title: bootstrap-v31-rebuild — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **critical**: SQL injection via unvalidated workspace-id argument: line 194 interpolates $WORKSPACE_ID into UPDATE statement; arg-3 input bypasses the kebab-case regex that constrains $SLUG.
  - **fixed.** Added kebab-case regex validation on $WORKSPACE_ID matching the existing $SLUG check (script lines 56-62 in revised file); injection vector verified refused via test (workspace-id with single-quote gives exit 3, target not created).
- **medium**: No partial-failure cleanup: if init or post-init UPDATE fails the script leaves a half-bootstrapped target the operator must clean by hand; trap on ERR would clean up.
  - **fixed.** Added trap on EXIT that rm -rf removes a half-built target on non-zero exit; happy path verified retains target on success (rc=0 path skipped); installs after the refuse-to-overwrite check so it cannot delete an unrelated existing path.
- **medium**: Engine-manifest §3 file-set enumeration is stale (lists migrations 001-010, current is 001-018); reviewer flagged but bootstrap is correct against actual current set.
  - **adjudicated.** Out of scope for S107 coding kind: engine-manifest §3 freshness is spec_only work, not a bootstrap defect; reviewer confirmed bootstrap correct against actual migration set. Future spec_only session updates manifest §3 enumeration.

## Terminal passes

- **iteration 1** — findings @ `f5a4523f4d7e`
  - Iter 1 reviewer surfaced 1 critical (SQL injection via workspace-id) and 2 medium findings (idempotency cleanup; manifest staleness).
- **iteration 2** — clean @ `f5a4523f4d7e`
  - Iter 2 reviewer audited fixes for findings 80 and 81 plus adjudication for 82; verdict clean of medium-or-higher findings, no new findings introduced.
