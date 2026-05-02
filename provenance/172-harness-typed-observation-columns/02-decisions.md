---
session: 172
title: harness-typed-observation-columns — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Land migration 030 adding nullable typed-observation atoms (closure_kind on harness, conflict_kind on dissent) per DV-S152-1 hybrid pathway.

**Kind:** schema_migration.  **Outcome:** adopt migration `030-harness-typed-observation-columns.sql`.

**Why.**

- (prior_decision) DV-S152-1 ratified hybrid typed-observation pathway: nullable opt-in conflict_kind closure_kind atoms on harness substrate kind, no enum, kernel agnostic. [DV-S152-1]
- (spec_clause) Methodology v9 names the typed-observation pathway clause carried by OI-S152-1 with OI-S152-2 governing graduation-review trigger criteria. [SPEC-methodology-v9]
- (prior_decision) DV-S171-1 v19 priority-2 admits tractable MEDIUM-OI burndown ahead of untriaged EFs under bare-prompt auto-proceed; FR-S171-11 names this session as v19 first calibration point. [DV-S171-1]
- (engine_feedback) OI-S152-1 narrow scope (two columns, no enum) is exactly the tractable shape the v19 priority-2 clause names; this session is the burndown demonstration. [EF-S171-2]

**Effects.**

- adds_migration state/migrations/030-harness-typed-observation-columns.sql
- modifies selvedge/submit/harness.py harness-dissent + harness-seal admit typed-observation atoms
- modifies selvedge/submit/_schemas.py harness-dissent + harness-seal optional entries
- closes_issue OI-S152-1 — OI-S152-1 typed-observation columns on harness substrate kind

**Rejected alternatives.**

- **R-1.1.** Bundle OI-S152-1 with OI-S151-1 ergonomic-fix scope into one joint migration set per FR-S155-13 joint-shipping ask.
  - (too_large_for_session) Bare-prompt auto-proceed; v19 priority-2 names tractable single-purpose tasks; joint scope multiplies surface beyond v19 first-calibration absorption.
- **R-1.2.** Add CHECK enum on conflict_kind closure_kind enumerating canonical values harvested from disaster-response arc.
  - (violates_gate) DV-S152-1 explicitly rejected immediate-promote; methodology v9 names no canonical values; sub-type count instability across single arc precluded enum-elevation.
