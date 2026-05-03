---
session: 188
title: oi-s081-7-engine-v52-marker — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Ship engine-v52 marker via migration 044 coupling snapshot_catalog deliberation_seal trigger plus export_manifest recovery index closing OI-S081-7.

**Kind:** schema_migration.  **Outcome:** adopt migration `044-engine-v52-marker`.

**Why.**

- (prior_decision) S081 DV-1 substrate-loss-defense-v1 C-9 sealed write-capability framing names engine-v52 marker as the wrapper that ships the deliberation-seal snapshot trigger plus export-manifest recovery index plus L1a-snapshot coupling. [DV-S081-1]
- (engine_feedback) S188 codex-shape-consult endorsed single-arc kind=coding for OI-S081-7 implementation; flagged export_manifest identity (recovery-index keyed UNIQUE path) plus SQLite CHECK widening table-rebuild plus reorder migration-then-VALID_TRIGGERS-then-API-then-handler-wire. [EF-S188-1]

**Effects.**

- adds_migration 044-engine-v52-marker.sql widens snapshot_catalog.trigger CHECK plus adds export_manifest plus bumps engine-v52.
- modifies selvedge/snapshots.py admits deliberation_seal trigger plus keep_reason override threading.
- modifies selvedge/init_cmd.py tags init_refused+init_forced as pre_destructive_anchor.
- modifies selvedge/submit/__init__.py wires post-commit take_snapshot(deliberation_seal).
- modifies selvedge/submit/deliberation.py surfaces workspace_session_no for snapshot tagging.
- creates selvedge/export/manifest.py record_manifest_entry plus workspace_relative helpers.
- modifies selvedge/export/session.py + spec_versions.py + issues.py write manifest rows + DELETE-before-unlink reconciliation.
- creates state/tests/test_engine_v52_marker.py 9 pytests covering migration plus dispatch plus manifest semantics.
- closes_issue OI-S081-7 — OI-S081-7 engine-v52 marker migration coupling shipped end-to-end.

**Rejected alternatives.**

- **R-1.1.** Split into separate sessions (migration + handler-wiring; export_manifest as its own arc) per codex Q1 prompt.
  - (redundant_with_existing) Codex Q1 endorsed single-arc as appropriate when the session is land engine-v52 marker plumbing; the three pieces share recovery semantics plus test fixtures.
- **R-1.2.** Key export_manifest UNIQUE(session_no, kind, path) instead of UNIQUE(path) per codex Q2 alternative.
  - (inferior_tradeoff) Path is the recovery identity by construction since each emitted file occupies one workspace path; (session_no, kind, path) admits multiple-rows-per-path which an INSERT OR REPLACE recovery index does not need.
