---
session: 188
title: oi-s081-7-engine-v52-marker — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **critical**: Path normalization in manifest.py _relative_path() falls back to str(path) when outside workspace_root; could write absolute paths to manifest, breaking portability and cross-machine recovery. Should raise error instead of silently falling back.
  - **fixed.** Same as finding 38: manifest._relative_path raises ValueError on out-of-workspace paths; record_manifest_entry catches and returns False. Reviewer subagent submitted duplicate findings 31-37 alongside the orchestrator-submitted 38-44; both batches address the same defect set.
- **high**: Outdated help text in cli.py:197 references engine-v51; should be updated to engine-v52 post-migration 044 to avoid operator confusion.
  - **adjudicated.** Same as finding 40: cli.py engine-v51 reference is historical anchor (where the widening landed at engine-v51 + migration 041), not a current-version claim; clarified parenthetical.
- **high**: Orphaned manifest entries possible: session.py and issues.py unlink stale files, then DELETE from export_manifest; if DELETE fails, the manifest row persists for a deleted file, degrading index integrity.
  - **fixed.** Same as finding 39: reordered DELETE manifest row BEFORE unlink in session.py + issues.py; DELETE failure now leaves both file and row intact.
- **high**: Test coverage gap: test_export_manifest_records_session_files does not explicitly verify that harness files are recorded in export_manifest with kind=harness; SESSION_FILE_KINDS mapping is tested but harness files are not.
  - **adjudicated.** Same as finding 41: kind=harness admission verified by test_migration_044 inspecting CHECK enum; full harness-lifecycle coverage warrants its own test arc, deferred via next_session_should.
- **medium**: snapshots.py _record_catalog_row builds two distinct INSERT statements (lines 244-273) based on whether keep_reason is set; could consolidate to single INSERT with COALESCE(?, DEFAULT) for clarity and maintainability.
  - **adjudicated.** Same as finding 44: split INSERT branches preserve column DEFAULT semantics when keep_reason is None; consolidating via COALESCE would obscure DEFAULT. Cosmetic; accept-implicit per ceremony-subtraction discipline.
- **medium**: Code duplication in session.py:397 and issues.py:142: both duplicate _relative_path logic instead of calling the function from manifest.py, risking divergence if the function is updated.
  - **fixed.** Same as finding 42: extracted manifest.workspace_relative public helper; session.py + issues.py now call it instead of duplicating the resolve+relative_to logic.
- **medium**: Test coverage gap: no test for stale-file reconciliation. test_export_manifest_records_session_files should include a test case where files are deleted between exports and manifest rows are cleaned up.
  - **fixed.** Same as finding 43: added test_export_manifest_stale_reconciliation_drops_row_and_file covering the unlink + manifest DELETE path.
- **high**: _relative_path falls back to absolute path on workspace_root mismatch, silently corrupting the manifest cross-machine portability.
  - **fixed.** manifest._relative_path now raises ValueError on out-of-workspace paths; record_manifest_entry catches and returns False so a configuration bug cannot silently land an absolute path in the substrate.
- **high**: Stale-file reconciliation in session.py and issues.py unlinks BEFORE DELETE FROM export_manifest; DELETE failure leaves orphan rows pointing at nonexistent files (not self-healing).
  - **fixed.** Reordered session.py + issues.py to DELETE manifest row BEFORE unlink; DELETE failure now leaves both file and row intact (recoverable on next export) instead of orphan-row + missing-file.
- **medium**: selvedge/cli.py:197 precheck --target-kind help text references engine-v51 + migration 041; should mention current engine-v52.
  - **adjudicated.** Help text reads as historical (where the widening landed at engine-v51 + migration 041), not a current-version claim; clarified parenthetical to engine-v51 widening. Engine-v52 marker does not change precheck target-kinds.
- **medium**: test_export_manifest_records_session_files does not explicitly assert kind=harness rows for harness file emissions.
  - **adjudicated.** Schema-level admission of kind=harness is verified by test_migration_044 inspecting the CHECK enum. End-to-end harness-lifecycle coverage (open/seal/expire/reopen across the harness substrate) warrants its own dedicated test arc; deferred via FR rather than added to this session.
- **medium**: session.py and issues.py duplicate path normalization logic instead of calling _relative_path from manifest.py; risks divergence on future change.
  - **fixed.** Added manifest.workspace_relative public helper; session.py and issues.py now call it instead of duplicating the resolve+relative_to logic.
- **medium**: No pytest covers stale-file reconciliation cleaning up corresponding export_manifest rows alongside the on-disk delete.
  - **fixed.** Added test_export_manifest_stale_reconciliation_drops_row_and_file: plants a stale 06-counterfactuals.md + manifest row, runs export, asserts both unlinked.
- **low**: _record_catalog_row branches on keep_reason for two near-identical INSERTs; could consolidate but split is harmless.
  - **adjudicated.** Two near-identical INSERT branches in _record_catalog_row preserve the column DEFAULT semantics when keep_reason is None; consolidating via COALESCE would obscure the DEFAULT. Cosmetic; accept-implicit per ceremony-subtraction discipline.

## Terminal passes

- **iteration 2** — clean @ `55790a0cfee5`
  - iter-2 clean. 4 fixes verified (38+39+42+43); 3 adjudicated (40+41+44). 9 new tests pass; full suite 334 pass at engine-v52.
