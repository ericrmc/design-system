---
session: 098
title: closes-issue-effect-wiring — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Wire closes_issue via handler-side dispatch plus refusal trigger; add typed target_issue_id column.

**Kind:** substantive.  **Outcome:** adopt engine_version `engine-v28`.

**Why.**

- (engine_feedback) EF-S096-3 documents that closes_issue is enum-only with no trigger or handler that flips issues.status, leaving orchestrator discipline as the sole coupling. [EF-S096-3]
- (deliberation) Both perspectives converge on handler-side dispatch and on deferring opens_issue; divergence resolved by adopting P-2 identity and P-1 enforcement.
- (prior_decision) Engine-v25 and v26 moved cross-table coherence into the substrate via T-22 and T-24; a refusal trigger continues that line.

**Effects.**

- adds_migration 014-closes-issue-wiring.sql adds target_issue_id and refusal trigger
- modifies _submit_decision_v2 dispatches closes_issue via _submit_issue_disposition
- creates BEFORE INSERT trigger refuses closes_issue without resolved target issue
- bumps_engine engine-v27 to engine-v28
- closes_issue EF-S096-3 closes_issue dispatch gap addressed

**Rejected alternatives.**

- **R-1.1.** Extend objects.object_kind to admit issue and backfill an objects row per issue so target_object_id resolves uniformly via T-01.
  - (inferior_tradeoff) Broadens the objects ontology to satisfy a single resolution path; admitting issues raises secondary lifecycle and descriptor questions.
- **R-1.2.** Pure substrate trigger that flips issues.status and inserts the issue_dispositions row without handler involvement.
  - (violates_gate) Would force reason atom synthesis inside SQL, bypassing application-layer text_atoms guards on length and shape.
- **R-1.3.** Refuse the closes_issue and opens_issue values from the effect_kind enum entirely so orchestrators must use only explicit submit kinds.
  - (preserves_legacy_path) Leaves the enum values as misleading dead vocabulary and removes the natural place to record closure intent next to the deciding decision.
- **R-1.4.** Wire opens_issue symmetrically by synthesizing an issues row from the effect with default priority and a descriptor-derived title.
  - (too_large_for_session) Manufacturing title and priority from a single descriptor makes issue quality depend on implicit policy rather than explicit data.

## D-2. Smoke-test that DV-S098-1 wiring actually flips the target issue's status.

**Kind:** procedural.  **Outcome:** ratify process_rule `closes_issue-handler-smoke-test`.

**Why.**

- (prior_decision) DV-S098-1 wired closes_issue dispatch; this decision exercises the path end-to-end. [DV-S098-1]

**Effects.**

- closes_issue OI-S098-1 — smoke-test confirms handler dispatch and t27/t28 invariants hold

## D-3. boundary-120char descriptor.

**Kind:** procedural.  **Outcome:** ratify process_rule `boundary-120`.

**Why.**

- (prior_decision) verifying boundary.

**Effects.**

- closes_issue OI-S098-1 — xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
