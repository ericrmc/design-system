---
session: 179
title: substrate-hardening-determinism-arc-open — close
engine_version_at_close: engine-v49
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S179 ships 7-migration substrate-hardening arc per operator-named-mandate; engine v48 to v49; T-33 single-use-nonce precheck gate plus T-34/T-35/slug-UNIQUE/atom-widening; closes 5 OIs by-mechanism.

## Engine version

- engine-v48 to engine-v49 across migrations 033 to 039.
## What was done

- Migration 033 harness alias objects-registration; migration 034 legacy_unresolved_cites quarantine; migration 035 decision_prechecks plus T-33 single-use-nonce gate; migration 036 T-34 cite-NOT-NULL trigger.
- Migration 037 sessions.slug UNIQUE index; migration 038 T-35 spec_clauses source_decision_v2_id NOT NULL trigger; migration 039 atom-length widening to 480 chars on support_claim plus finding.
- selvedge/precheck.py new module with cmd_precheck CLI plus verify_and_consume_precheck handler with rowcount CAS guard; decision_v2 handler T-33 enforcement with kind-aware admit predicate.
- spec-version v22 supersedes v21 with section 5 precheck clause + T-34/T-35 gate documentation; 273 pytest cases pass (10 new for T-33/T-34/T-35/slug-UNIQUE/atom-length/harness-alias).
## State at close

- All 5 in-scope OIs resolved by-mechanism; 6 reviewer findings dispositioned (1 critical adjudicated; 1 high fixed via rowcount; 3 medium fixed or adjudicated; 1 low fixed); review-pass clean iter1.
## Open issues

- 20-plus hardening MEDIUM OIs remain open (review-loop substrate, manifest-hash seal, falsification expiry, trigger-predicate cluster, determinism cluster, typed-graph linkage); routed via FRs below per P-3 minority preserved.
## What the next session should address

- Backfill 747 legacy spec_clauses NULL source_decision_v2_id rows by joining via spec_section_id to spec_versions.source_decision_v2_id (closes finding-196 deferral).
- Pick from FR-cluster: review-loop substrate (OI-083-001/S133-1/S145-1); manifest-hash seal (OI-S104-1); harness expire CLI (OI-S125-2); trigger-predicate cluster (OI-S151-3/4 + OI-S159-1 + OI-S163-1).
- Watch T-33 calibration in practice across S180+; surface calibration-EF if precheck refuses legitimate decision-record or context-recompute friction proves disruptive (carries forward FR-S178-10 T-32 watch).
- Triage seal-grade EFs (EF-S173-1 plus EF-S172-1 plus EF-S174-1 plus EF-S175-1 plus EF-S176-1 plus EF-S176-2 plus EF-S178-1 plus EF-S179-1) at next operator-present session per FR-S178-9 carrying forward.
- If operator-present, pick atom_type splits (OI-S088-1) plus legacy_imports.decomposition_status (OI-086-004) cluster; deferred from S179 per scope discipline.
## Validator at close

- pytest 273 passed (10 new); migrate status 39 applied 0 pending; review-pass clean iter1; T-32 fired 14 chain-walks for DV-S179-1 cleanly; T-33 verified end-to-end in pytest.
