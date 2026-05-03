---
session: 187
title: l5-close-time-export-expansion — decisions
generated_by: selvedge export
---

# Decisions

## D-1. S187 ships OI-S081-6 L5 close-time export expansion across 8 enumerated artefacts per sealed DV-S081-1.

**Kind:** substantive.  **Outcome:** adopt issue `OI-S081-6`.

**Why.**

- (prior_decision) DV-S081-1 sealed substrate-loss-defense-v1 with L5 close-export expansion across 8 enumerated artefacts as load-bearing layer; this ships that layer. [DV-S081-1]
- (engine_feedback) EF-S187-1 records gpt-5.5 codex-shape-consult endorsing single-arc kind=coding plus stale-file reconciliation as the one hard requirement; folded into design. [EF-S187-1]

**Effects.**

- creates selvedge/export/l5_session_artefacts.py producing 05-09 session-bounded files when rows present
- creates selvedge/export/spec_versions.py producing specifications/_versions.md as workspace-wide ledger
- modifies selvedge/export/__init__.py wires --session N --write to trigger issues + spec_versions regen
- modifies selvedge/export/session.py merges L5 files into plan plus reconciles stale 05-09 on rerun
- closes_issue OI-S081-6 — OI-S081-6 closed by-mechanism: L5 close-time export expansion shipped

**Rejected alternatives.**

- **R-1.1.** Defer L5 to S188 by collapsing into OI-S081-7 engine-v52 marker migration coupling snapshot_catalog plus L5 export-manifest tables
  - (operator_override) FR-S186-13 plus FR-S081-13 explicitly assigned L5 to S187; OI-S081-7 deferred to S188 per FR-S186-14 keeps the two issues mechanically distinct.
- **R-1.2.** Include full result_text bodies in 09-chain-walks.md so substrate-wipe leaves the chain-walker output recoverable verbatim rather than via re-walk
  - (inferior_tradeoff) result_text averages 8KB per anchor with 10-30 anchors per session producing 80-240KB duplicate prose per close; sha256 receipts plus regenerable text preserves proof shape cheaper.
- **R-1.3.** Emit empty 05-09 files even when no rows exist so the close evidence has stable filenames present in every session dir
  - (inferior_tradeoff) empty marker files train operators to grep through stub content; absence of a file is itself meaningful provenance and stale-file reconciliation handles rows-deleted explicitly.
