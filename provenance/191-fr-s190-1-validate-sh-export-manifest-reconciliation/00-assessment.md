---
session: 191
title: fr-s190-1-validate-sh-export-manifest-reconciliation — assessment
engine_version_at_open: engine-v52
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

S191 opens kind=coding under bare-PROMPT.md auto-proceed; sealed DV-S190-2 D-B FR-D ready to ship per P-4 schema_sketch steps 1-3.

## Agenda

1. Implement FR-S190-1: tools/manifest_reconcile.sh sha256 reconciliation walking export_manifest rows.
2. Step 1 manifest-row integrity all kinds (incl NULL session_no): exists + sha256 match + reject absolute/.. paths.
3. Step 2 L5 orphan discovery scoped to post-engine-v52 sessions only (avoid pre-adoption false positives).
4. Wire tools/validate.sh to invoke tools/manifest_reconcile.sh as a step before pytest.
5. Add state/tests/test_manifest_reconcile.py covering pass + missing + tampered + L5 orphan + NULL session_no row.
6. Spawn reviewer subagent (Explore read-only) per coding-review loop.
7. Pre-decision precheck + decision-record kind=substantive citing DV-S190-2 sealed design + DV-S188-1 export_manifest.
8. Dispose FR-S190-12 (FR-S190-1) closed by-mechanism; decline FR-S190-18 fold per D-B P-4 what_not.
9. Close-time engine-feedback (success-signal + audit-step + codex-shape-consult) and close-record.
