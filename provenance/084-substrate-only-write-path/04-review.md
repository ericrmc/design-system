---
session: 005
title: substrate-only-write-path — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **critical**: Calibrated-block bypass admits any DDL between markers without structural validation; could slip destructive operations.
  - **fixed.** _validate_calibrated_block now refuses non-recreation statements inside the marker pair; only CREATE TABLE/INSERT/DROP/ALTER RENAME/CREATE INDEX/CREATE TRIGGER admitted.
- **critical**: Migration 003 ordering: refs recreation before objects; rollback semantics unclear.
  - **adjudicated.** The .pre-migrate-backup mechanism restores both tables atomically; ordering is correct because old triggers reference old objects. Comment in 003 names the dependency.
- **critical**: Export crashes/renders empty when review_finding has disposition=open and disposition_atom_id is NULL.
  - **fixed.** _export_session_provenance now renders no-disposition-recorded placeholder when disposition_atom_id is NULL.
- **high**: T-20 trigger fires on any open medium+ finding regardless of code-bearing target; comment promised narrower scope.
  - **adjudicated.** Operator wants strict refusal; conservative trigger (any open medium+ blocks close) is more protective than narrowing to code-bearing kinds. Comment to be tightened in a future migration.
- **high**: GLOB pattern (asterisk pipe asterisk pipe asterisk) on text_atoms.text false-positives on prose with two pipe characters.
  - **adjudicated.** Deliberate: pipes forbidden in atoms by design to prevent accidental markdown table syntax. Authors rephrase using slashes or commas. Documented in prompts.
- **high**: text_atoms CHECK forbids LF (char 10) but not CR (char 13); CRLF line endings would slip through.
  - **fixed.** Migration 004 adds T-21 BEFORE INSERT and UPDATE triggers refusing CR in atom text.
- **high**: No tests for new Path-A handlers, calibrated marker, or export.
  - **adjudicated.** Test coverage gap acknowledged; deferred to OI-084-002 immediate follow-up. Operator-policed for now; same precedent as S082 mid-session test deferrals.
- **medium**: Engine-version banners inconsistent: validate.sh, cli.py docstring, manifest.
  - **fixed.** All three banners updated to engine-v20; manifest frontmatter version=20.
- **medium**: _atom_session_id did not check session status before atom inserts; T-06 surfaced as raw constraint violation.
  - **fixed.** _atom_session_id now refuses closed sessions with E_REFUSAL_T06 by default; require_open=False opt-out preserved for read paths.
- **medium**: role_write_capabilities seed missing __cli__ objects insert.
  - **adjudicated.** Verified via query: __cli__ objects insert was seeded in migration 001. Reviewer false positive.
- **medium**: Export decision_effects query lacks ORDER BY effect_id; non-deterministic markdown.
  - **fixed.** ORDER BY effect_id added to the SELECT in _export_session_provenance.
- **medium**: T-18/T-19 do not enforce on legacy decisions; backward-compat exemption not documented.
  - **adjudicated.** Intentional exemption for legacy decisions during v19 to v20 transition. Pre-v20 sessions are closed; T-06 protects them; new substantive decisions must use decisions_v2 path.
- **low**: Alias formats inconsistent across handlers (A-S, DV-S, RF-S, C-S).
  - **adjudicated.** Format follows a stable convention: prefix-letters indicate object kind. Documented in handler comments.
- **high**: Latent bug: migrate runner reports success on a migration that does not INSERT into schema_migrations; UPDATE no-ops silently. Migration 003 hit this.
  - **fixed.** Migrations 003 and 004 now include INSERT INTO schema_migrations placeholder; manually backfilled the 003 row. Tracked as OI-084-003 to harden the runner with a post-apply existence check.
