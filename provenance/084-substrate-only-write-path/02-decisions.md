---
session: 005
title: substrate-only-write-path — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Override 078 D-5 release gate (operator-directed) for the Path A substrate-only-write-path revision

**Kind:** procedural.  **Outcome:** ratify process_rule `release_gate_override`.

**Why.**

- (operator_directive) Operator directed: override the gate, this should already be done as per constraints.md.
- (spec_clause) constraints.md S1 names structured state belongs in a database that refuses malformed input.
- (prior_decision) S083 D-2 set precedent: operator can lift the self-imposed gate when directing kernel revision.

**Effects.**

- modifies 078 D-5 release gate

**Rejected alternatives.**

- **R-1.1.** Hold the gate; defer Path A until the external trial completes.
  - (operator_override) The operator named the requirement explicitly and the deliberation surfaced no impediment to shipping.

## D-2. Adopt Path A substrate-only-write-path; bump engine-v19 to engine-v20

**Kind:** substantive.  **Outcome:** adopt engine_version `engine-v20`.

**Why.**

- (operator_directive) Operator ratified Path A (P-1 strictest) at S084 ratification step. [DV-S005-1]
- (deliberation) Deliberation 3 surfaced three load-bearing positions; operator chose strictest after weighing tradeoffs.
- (constraint) constraints.md S1 says structured state belongs in a database refusing malformed input.
- (review_finding) S083 close itself authored four markdown files before noting the substrate gap; same failure mode as constraints S1.

**Effects.**

- adds_migration 003-substrate-strict-write-path.sql
- adds_migration 004-text-atoms-cr-guard.sql
- creates selvedge export subcommand
- modifies prompts/development.md (CLI-only flow)
- modifies prompts/application.md (CLI-only flow)
- bumps_engine engine-v19 to engine-v20

**Rejected alternatives.**

- **R-2.1.** Path B (P-3 pragmatic): keep body_md as render hint, move load-bearing content into facet tables.
  - (operator_override) Operator chose strictest path; render-hint body_md leaves the prose-in-rows door open and constraints S2 names that exact failure.
- **R-2.2.** Path C (P-2 friction-only): keep prose; add word-count gates, defect-pattern validators, whole-document spec blobs.
  - (operator_override) Operator wanted strict refusal not friction; the LLM-author failure mode P-2 named is real but Path A addresses it via closed enums and length-bounded atoms.
- **R-2.3.** Defer the change as methodology-expanding active-spec content under 078 D-5 release gate.
  - (operator_override) The release gate is operator-overridden at DV-S005-1 with reason recorded; deferral is incompatible with the directive.

## D-3. T-15 admits non-destructive CHECK-relaxation table-recreation via calibrated marker pair

**Kind:** calibration.  **Outcome:** ratify process_rule `T-15-calibrated`.

**Why.**

- (operator_directive) Operator ratified: check relaxation is fine; sibling-table workaround is uglier and poisons joins.
- (deliberation) P-3 surfaced the issue as Q1: widening object_kind/relation CHECKs needs DROP+recreate which T-15 forbids.
- (review_finding) S084 reviewer F1 demanded structural validation of block contents; runner now rejects non-recreation statements inside markers.

**Effects.**

- modifies selvedge/cli.py _t15_violations admits T-15-CALIBRATED-BEGIN/END marker pair
- creates _validate_calibrated_block: refuses non-recreation DDL inside markers

**Rejected alternatives.**

- **R-3.1.** Use sibling _v2 tables for new object kinds and relations; keep T-15 strict.
  - (inferior_tradeoff) Sibling tables poison every JOIN against objects/refs; UNION views are read-time tax for query-time benefit only.
