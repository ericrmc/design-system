---
session: 126
title: harvested-ef-disaster-recovery-triage — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Triage 8 undisposed harvested engine-feedback rows from disaster-recovery peer; 3 reinforcements preserved, 5 gaps tracked as OI-S126-1 through OI-S126-5.

**Kind:** disposition.  **Outcome:** ratify open_question `harvested-ef-batch-S110-disaster-recovery`.

**Why.**

- (engine_feedback) EF-S110-9 names a cluster of typed-graph thinning across S001-S004 worth tracking through arc close. [EF-S110-9]
- (prior_decision) DV-S110-1 commissioned harvest-ef as the substrate-direct sync path; triage closes the disposition loop on harvested rows. [DV-S110-1]

**Effects.**

- opens_issue OI-S126-1 — application.md docs gap
- opens_issue OI-S126-2 — kind taxonomy fit for external-problem
- opens_issue OI-S126-3 — close-record items creation-only handler gap
- opens_issue OI-S126-4 — next_session_should null-state FR noise
- opens_issue OI-S126-5 — typed-graph thinning in external-problem sessions
