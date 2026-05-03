-- Migration 043: bump workspace_metadata.init_session_offset from 79 to 179.
--
-- Why:
--   The S180 substrate-wipe (subagent ran selvedge init --force against the
--   live primary substrate, unlinking S001-S179 of recorded session state)
--   left the disk record of S001-S179 intact under provenance/ but reinitialised
--   the substrate with init_session_offset=79. The five post-wipe sessions
--   S080-S084 (slugs s-audit-180, substrate-loss-defense-design,
--   substrate-loss-defense-l1a-init-guard, tool-selection-canonical-reminder-triage,
--   substrate-snapshot-machinery-and-restore-cli) wrote provenance folders
--   080-..., 081-..., 082-..., 083-..., 084-... that shadow the pre-wipe
--   folders at the same numeric prefixes. Continuing on the current offset
--   would extend the collision through S179 (every future session would
--   shadow a pre-wipe folder).
--
-- Path selected (operator at S085-open, three options enumerated):
--   Path A: bump init_session_offset 79 -> 179 so future sessions number
--           S185+. Substrate keeps S080-S084 aliases as historical record;
--           the five existing collision folders remain on disk as historical
--           artefacts of the wipe + recovery arc.
--
-- Paths rejected:
--   Path B (substrate renumber S080-S084 -> S180-S184 via T-06 carve-out):
--           T-06 (text_atoms_no_mut_after_close_upd) refuses UPDATE on text_atoms
--           whose created_session_id is closed; 84 atom rows reference S08x in
--           closed-session prose. Renumber-by-UPDATE would require disabling T-06
--           which the engine specifically defends against (per DV-S081-1
--           substrate-loss-defense-v1).
--   Path C (snapshot-rollback + replay S080-S084 work as S180-S184):
--           too_large_for_session; replay loses authentic calibration EFs.
--
-- Cites: DV-S081-1 (substrate-loss-defense-v1; T-06 immutability load-bearing).
--
-- Mechanism:
--   Single UPDATE on workspace_metadata. No schema change. No data backfill.
--   Existing sessions.workspace_session_no values (80, 81, 82, 83, 84) are
--   not modified; future sessions compute workspace_session_no as
--   init_session_offset + session_no = 179 + 6 = 185 for the next session_no.
--
-- Reversibility:
--   Reversible by UPDATE workspace_metadata SET value='79' WHERE key='init_session_offset'.
--   Operator-discretionary; no substrate gate prevents reversal.

BEGIN;

UPDATE workspace_metadata SET value = '179' WHERE key = 'init_session_offset';

INSERT INTO schema_migrations (name, sha256) VALUES ('043-bump-init-session-offset.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
