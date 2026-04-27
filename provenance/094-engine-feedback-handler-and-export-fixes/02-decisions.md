---
session: 094
title: engine-feedback-handler-and-export-fixes — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Add submit engine-feedback handler and fix export dry-run/reconcile UX (engine-v26).

**Kind:** substantive.  **Outcome:** adopt engine_version `engine-v26`.

**Why.**

- (engine_feedback) EF-S092-4 noted that engine_feedback authoring still required raw SQL, violating substrate-only-writes. [EF-S092-4]
- (engine_feedback) EF-S092-1 reported that export --issues without --write printed files_written though it had not written. [EF-S092-1]
- (engine_feedback) EF-S092-2 reported that export --issues --write left stale top-level paths after open->resolved transitions. [EF-S092-2]

**Effects.**

- creates submit handler engine-feedback in selvedge/cli.py with EF-S<wno>-<idx> alias allocation
- modifies _export_issues: dry_run flag, files_planned/files_written split, reconcile via files_deleted
- modifies _export_session_provenance: dry_run flag, files_planned/files_written split
- bumps_engine engine-v25 -> engine-v26

**Rejected alternatives.**

- **R-1.1.** Refuse export entirely without --write or an explicit --dry-run flag.
  - (inferior_tradeoff) Default-to-dry-run with a legible files_planned key preserves the safer default and matches the existing CLI shape.
- **R-1.2.** Defer the engine-feedback handler until a deferred markdown-authoring path lands in S095.
  - (violates_gate) Without a handler the only authoring path is raw SQL which breaks substrate-only-writes today.
