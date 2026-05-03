---
session: 191
title: fr-s190-1-validate-sh-export-manifest-reconciliation — decisions
generated_by: selvedge export
---

# Decisions

## D-1. S191 ships FR-S190-1 manifest_reconcile.sh implementing sealed DV-S190-2 D-B FR-D first-step.

**Kind:** substantive.  **Outcome:** adopt process_rule `process_rule:fr-s190-1-validate-sh-export-manifest-reconciliation`.

**Why.**

- (prior_decision) Sealed DV-S190-2 D-B synthesis names FR-D coding-kind work shipping P-4 schema_sketch steps 1-3 as the validate.sh-first smaller-mechanism intermediate; FR-S190-12 carries the named first-step ask. [DV-S190-2]
- (prior_decision) DV-S188-1 migration 044 ships export_manifest table carrying path+sha256+size_bytes as the substrate-side recovery index this reconciliation reads. [DV-S188-1]
- (engine_feedback) Codex shape-consult EF-S191-1 confirmed kind=coding plus all-kinds-pass-1 + L5-only-pass-2 split structurally sound and flagged four pre-emptions all addressed. [EF-S191-1]

**Effects.**

- creates tools/manifest_reconcile.sh standalone bash script with pass 1 + pass 2 reconciliation
- modifies tools/validate.sh adds bash tools/manifest_reconcile.sh as a step before pytest
- creates state/tests/test_manifest_reconcile.py 13 pytest cases covering sealed-design shapes

**Rejected alternatives.**

- **R-1.1.** Ship full FR-E substrate-receipt gate now per DV-S190-2 D-B P-1+P-2 ship-now stance instead of validate.sh-first.
  - (violates_gate) Sealed DV-S190-2 explicitly routes FR-E behind validate.sh-first measurement step; shipping FR-E now would bypass synthesis-encoded graduation timing.
- **R-1.2.** Fold FR-S190-18 harness-file cross-session anchoring into the same validate.sh scope.
  - (preserves_legacy_path) Synthesis D-B P-4 what_not excluded harness cross-session anchoring as needing distinct opening-session-anchor design; folding muddles the L5 divergence signal.
- **R-1.3.** Implement reconciliation as inline block inside tools/validate.sh rather than standalone tools/manifest_reconcile.sh.
  - (inferior_tradeoff) Inline block creates pytest-validate.sh recursion risk codex flagged at S191 open; standalone script is testable directly without re-entering validate.sh.
