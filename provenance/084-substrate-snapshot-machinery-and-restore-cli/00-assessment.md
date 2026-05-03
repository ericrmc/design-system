---
session: 084
title: substrate-snapshot-machinery-and-restore-cli — assessment
engine_version_at_open: engine-v51
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

S082 shipped L1a init guard; OI-S081-3 + OI-S081-4 (L3 snapshots + restore CLI) carried forward from FR-S081-11 after S083 triage diversion.

## Agenda

1. Add migration 042 creating snapshot_catalog table with trigger CHECK enum (session_open, session_close, migrate, init_refused, init_forced, manual).
2. Implement selvedge/snapshots.py using sqlite3.Connection.backup() with sha256, source_db_sha256, sqlite_page_count capture.
3. Wire snapshot trigger fires at session-open + session-close + migrate --apply + init refused/forced paths.
4. Default retention policy: keep last 20 per trigger, keep 30 days, never prune newest same-trigger anchor.
5. Snapshots written under state/snapshots/ gitignored (workspace boundary, not git boundary).
6. Implement bin/selvedge restore --from --to --verify --confirm with exit-2 refusal when --to is live primary without --confirm.
7. Pytest coverage: trigger fires + sha match + restore happy path + refusal without --confirm + verify rejects sha mismatch.
8. Reviewer subagent loop per T-20; address medium-or-higher findings.
9. DV-S084-1 substantive decision-record closing OI-S081-3 + OI-S081-4; precheck required per T-33.
10. Defer deliberation-seal trigger to S086 OI-S081-7 marker arc (codex consult Q4) — out of scope per OI-S081-3 wording.
11. Defer engine-version bump to OI-S081-7 per FR-S081-14 plan.
