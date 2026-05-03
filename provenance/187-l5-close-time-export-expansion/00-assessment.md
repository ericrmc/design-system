---
session: 187
title: l5-close-time-export-expansion — assessment
engine_version_at_open: engine-v51
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

S187 opens engine-v51 with substrate clean post-S185 recovery; OI-S081-6 HIGH remains as the named L5 close-export expansion under sealed DV-S081-1.

## Agenda

1. Implement five session-bounded export extractors (05-engine-feedback / 06-counterfactuals / 07-fr-dispositions / 08-prechecks / 09-chain-walks) in selvedge/export/session.py.
2. Add stale-file reconciliation removing any 05-09 file no longer produced by current substrate state, mirroring the issues-export pattern.
3. Add workspace-wide spec_versions index export at specifications/_versions.md regenerated each close.
4. Wire selvedge export --session N --write to additionally regenerate open-issues and spec_versions so the close-ceremony command emits everything in one shot.
5. Add pytest coverage for content shape, absence-when-no-rows, stale-file removal, idempotent rerun, and workspace-wide regen triggers.
6. Run reviewer subagent under T-30, address findings, re-invoke until clean.
7. Close ceremony: dispose FR-S186-13 plus FR-S081-13 plus FR-S084-13; close OI-S081-6; author engine-feedback rows; audit-step row; close-record + session-close.
