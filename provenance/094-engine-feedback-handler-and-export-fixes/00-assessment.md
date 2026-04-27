---
session: 094
title: engine-feedback-handler-and-export-fixes — assessment
engine_version_at_open: engine-v25
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

S094 opens with two known papercuts: engine_feedback has no submit handler (raw SQL still required), and export --issues prints files_written for dry-run plus does not reconcile open->resolved file moves.

## Agenda

1. Add submit engine-feedback handler with EF-S<wno>-<idx> alias allocation, refs recording, and role-capability check.
2. Make export dry-run-by-default semantics legible by switching the key to files_planned and adding a dry_run flag.
3. Make export --issues --write reconcile by deleting on-disk files no longer in the substrate target set.
