---
session: 110
title: harvest-ef-substrate-direct — close
engine_version_at_close: engine-v33
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

Substrate-direct harvest-ef shipped (engine-v33); 9 disaster-recovery EF rows imported; three-iteration review converged clean.

## Engine version

- engine-v32 to engine-v33.
## What was done

- Migration 019 adds harvested_engine_feedback ledger; UNIQUE(peer_workspace_id, peer_feedback_id), FK to objects+sessions.
- _me_harvest_ef rewritten to read peer engine_feedback rows substrate-direct via file:?mode=ro with busy_timeout+query_only PRAGMAs.
- _me_status switched from md-glob to peer engine_feedback table read; ef_rows=None signals legacy peer schema.
- Cross-family deliberation_id=10 (P-1 anthropic, P-2 codex/openai) converged on Option 1 over md round-trip.
- Three reviewer iterations: 8 findings total (2 high, 6 medium), all fixed in-iteration; iter-3 clean.
- Live harvest brought 9 peer rows in including EF-S005-1 (now self-dev EF-S110-7); re-run skipped all 9 via ledger.
- Opened OI-S110-1 (superseded-spec discoverability), OI-S110-2 (S109 stale body_path), OI-S110-3 (decision_effects/supports backfill).
## State at close

- Engine v33 active; 8 untriaged engine_feedback rows from disaster-recovery + EF-S110-10 reflection; 29 open issues.
## Open issues

- OI-S110-3 noted as prerequisite for EF-S110-7 triage via issue-note; cross-typed-row link gap surfaced in EF-S110-10.
## What the next session should address

- Address OI-S110-2 (stale body_path, smallest), OI-S110-1 (orient discoverability), OI-S110-3 (effects/supports backfill) before EF-S110-7 design work.
- Then triage EF-S110-7 cross-session provenance reframe: deliberate report shape (--report vs --graph vs other) with cross-family perspective.
## Validator at close

- Three-iteration review loop: iter-1 findings, iter-2 findings, iter-3 clean. Live harvest+re-run smoke-tested ledger idempotency.
