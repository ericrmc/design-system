---
session: 098
title: closes-issue-effect-wiring — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **medium** against `DV-S098-1`: UNIQUE constraint on decision_effects does not include target_issue_id; two closes_issue effects on different issues with same descriptor would collide.
  - **fixed.** Migration 015 recreates decision_effects with UNIQUE extended to include target_issue_id; calibrated table-recreate non-destructive.
- **medium** against `DV-S098-1`: target_descriptor min length is 2 (table CHECK) but reason_atom_id needs 8-240; a 2-7 char descriptor would fail with an unhelpful atom CHECK error.
  - **fixed.** Handler in _submit_decision_v2 now refuses target_descriptor shorter than 8 chars with a clear E_VALIDATION message before reaching the atom CHECK.
- **high** against `DV-S098-1`: Export query for decision_effects reads only target_object_id and target_descriptor; closes_issue rows render without naming the closed issue alias, losing audit information.
  - **fixed.** _export_session_provenance now reads target_issue_id and renders effect lines as kind alias dash descriptor, preserving issue identity in 02-decisions.md.
- **medium** against `DV-S098-1`: Reviewer requests an automated test of the BEFORE INSERT trigger ordering; in-session smoke test exists but no pytest fixture under OI-S090-2.
  - **adjudicated.** In-session smoke tests covered all five trigger and validation paths; persistent pytest fixture remains under OI-S090-2 which tracks the broader Path A test gap.
- **medium** against `DV-S098-1`: Multiple closes_issue effects in one decision are sequentially atomic; reviewer flags lack of explicit documentation that all-or-nothing is the contract.
  - **adjudicated.** Atomic-rollback behaviour is correct; documenting it in prompts/development.md is blocked by OI-S090-5 substrate-spec authoring friction. Tracked there.
- **low** against `DV-S098-1`: prompts/development.md effect-kind list does not yet document the closes_issue payload contract (target alias plus target_descriptor closure reason).
  - **adjudicated.** PreToolUse hook refuses direct prompts/development.md edit; substrate-spec authoring path tracked under OI-S090-5. Migration 014 comments and EF-S096-3 carry the contract for next session.
- **low** against `DV-S098-1`: engine-manifest spec is at version 27; an engine-v28 entry documenting migration 014 has not been authored.
  - **adjudicated.** Engine-manifest spec_version bump to v28 deferred under OI-S090-5; current_engine_version metadata is the operative source of truth and migration 014 is self-documenting.
## Iteration 2

- **medium** against `DV-S098-1`: Handler descriptor validation has a lower bound (>=8) but no upper bound; descriptors 121-240 chars pass the handler then fail the decision_effects.target_descriptor CHECK with an opaque message.
  - **fixed.** Handler now refuses descriptor outside 8-120 chars; verified 7/121 refused with clear E_VALIDATION and 120 accepted at the boundary.
