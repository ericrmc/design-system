---
session: 191
title: fr-s190-1-validate-sh-export-manifest-reconciliation — forward-reference-dispositions
generated_by: selvedge export --session
---

# Forward-reference dispositions

## FR-S190-12

- **Originating session.** S190 (`next_session_should` state-item seq 12).
- **Original ask.** FR-S190-1: implement DV-S190-2 first-step extending tools/validate.sh with sha256 reconciliation walking L5 files against export_manifest plus pytest case asserting non-zero exit on injected divergence.
- **Resolved.** addressed by DV-S191-1 (manifest_reconcile.sh + validate.sh extension + 13 pytest cases shipped per sealed DV-S190-2 D-B FR-D)
- **Resolved-at.** 2026-05-03T23:55:43.452Z

## FR-S190-18

- **Originating session.** S190 (`next_session_should` state-item seq 18).
- **Original ask.** FR-S187-15 carry-forward: harness-file reconciliation with cross-session anchoring still pending (D-B scoped to L5 only); consider folding into FR-S190-1 validate.sh scope.
- **Resolved.** addressed by DV-S191-1 R-1.2 (decline-fold per D-B P-4 what_not excluding harness cross-session anchoring; FR-S187-15 + FR-S188-14 remain separate)
- **Resolved-at.** 2026-05-03T23:55:43.498Z

## FR-S189-9

- **Originating session.** S189 (`next_session_should` state-item seq 9).
- **Original ask.** If operator absent and queue still empty of HIGH OIs: consider FR-S188-14 harness lifecycle export_manifest coverage as priority-2 tractable MEDIUM coding task per §1.5 v19 admissibility.
- **Resolved.** addressed by DV-S191-1 (S191 selected FR-S190-1 over FR-S188-14; freshest sealed-design implementation took priority-4 most-recent-FR slot)
- **Resolved-at.** 2026-05-03T23:55:43.544Z
