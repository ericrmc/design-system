---
session: 084
title: substrate-snapshot-machinery-and-restore-cli — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Ship L3 boundary snapshots via SQLite Connection.backup at session-open + close + migrate + init triggers plus restore CLI; closes OI-S081-3 + OI-S081-4 per FR-S081-11.

**Kind:** substantive.  **Outcome:** adopt process_rule `l3-snapshots-and-restore-cli`.

**Why.**

- (prior_decision) S081 DV-S081-1 sealed L3 snapshots via SQLite Connection.backup at session-open + close + migrate + init triggers plus mandatory restore CLI per C-3 + C-4. [DV-S081-1]
- (prior_decision) S082 DV-S082-1 shipped L1a init guard closing OI-S081-1 + OI-S081-8; S084 layers L3 + restore CLI on top per FR-S081-11. [DV-S082-1]
- (engine_feedback) S084 codex-shape-consult by gpt-5.5 confirmed single-arc kind=coding; recommended retention defaults + state/snapshots/ gitignored. [EF-S084-1]

**Effects.**

- adds_migration 042-snapshot-catalog.sql creates snapshot_catalog with trigger CHECK enum + UNIQUE(path) + two indexes.
- creates selvedge/snapshots.py take_snapshot via Connection.backup; pid-suffix path defends UNIQUE(path) per RF-S084-16.
- creates selvedge/restore_cmd.py bin/selvedge restore --from --to --verify --confirm; E_LIVE_PRIMARY exit-2 refusal.
- modifies init_cmd.py + migrations.py + submit/__init__.py wire snapshot triggers post-commit; session.py returns wno on close.
- modifies .gitignore adds state/snapshots/ per codex Q3; runtime recoverability beats clone portability.
- closes_issue OI-S081-3 — OI-S081-3 L3 snapshot machinery shipped at four trigger points.
- closes_issue OI-S081-4 — OI-S081-4 bin/selvedge restore CLI with --confirm exit-2 refusal pattern shipped.

**Rejected alternatives.**

- **R-1.1.** Ship L3 snapshots without restore CLI; defer restore to a follow-up arc.
  - (inferior_tradeoff) S081 DV-S081-1 P-2 named backups-without-restore as decorative; codex Q1 reaffirmed ship-together to avoid apparent-safety-without-recovery.
- **R-1.2.** Place state/snapshots/ inside the git boundary committed alongside provenance.
  - (inferior_tradeoff) Snapshot bytes balloon git history; codex Q3 chose runtime recoverability over clone portability since clones rebuild snapshots forward.
- **R-1.3.** Add deliberation-seal as a fifth snapshot trigger this arc.
  - (too_large_for_session) OI-S081-3 wording named only session-open + close + migrate + init; deliberation-seal deferred to S086 OI-S081-7 marker arc.
- **R-1.4.** Bump engine version to v52 marker on this arc.
  - (preserves_legacy_path) OI-S081-7 owns engine-version marker coupling L1a + snapshot_catalog + L5 export-manifest per FR-S081-14; collapsing into S084 forecloses L5 scope.
