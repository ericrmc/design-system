---
session: 086
title: substrate-invariant-audit — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Adjudicate S086 audit findings; surface new open-issues for schema-invariant gaps deferred under 078 D-5 release gate.

**Kind:** disposition.  **Outcome:** adopt issue `substrate-invariant-gaps-S086`.

**Why.**

- (operator_directive) S086 prompt scopes the work as audit and calibration under the 078 D-5 release gate; structural fixes are out of session.
- (review_finding) Eight findings F1 through F8 name schema invariants the substrate does not currently enforce or that contradict prior commitments.
- (prior_decision) OI-085-002 disposition path already names submit-open-issue and submit-engine-feedback as preconditions, covering F6 and F7.

**Effects.**

- opens_issue OI-086-001 spec_clause source_decision_v2_id NOT NULL
- opens_issue OI-086-002 single-active spec_version per spec_id
- opens_issue OI-086-003 cited_object_id NOT NULL on cite-required bases
- opens_issue OI-086-004 legacy_imports decomposition_status semantics
- modifies open-issues/index.md adds four S086 OIs

**Rejected alternatives.**

- **R-1.1.** Land structural fixes now: NOT NULL CHECKs, single-active spec_version trigger, decomposition_status derived view, plus migration and tests, in this session.
  - (too_large_for_session) Eight schema invariants plus migration authoring plus reviewer loop cannot be done coherently in one calibration-and-audit session.
