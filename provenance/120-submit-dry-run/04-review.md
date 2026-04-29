---
session: 120
title: submit-dry-run — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **low** against `DV-S120-1`: Reviewer note: SQLite ROWID is not reserved across BEGIN IMMEDIATE/ROLLBACK, so a dry-run-returned id may equal the next real-submit id; superficially confusing but not a correctness defect.
  - **adjudicated.** Academic ROWID-reuse observation; identical behavior to any aborted INSERT today. No code change warranted.

## Terminal passes

- **iteration 1** — clean @ `ef8c0c976bad`
  - Reviewer audited rollback semantics, FS side-effect coverage, contextvar threading, nested closes_issue/opens_issue dispatch, retry path, envelope, ID allocation; one LOW adjudicated.
