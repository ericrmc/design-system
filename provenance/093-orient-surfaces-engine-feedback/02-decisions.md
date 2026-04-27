---
session: 093
title: orient-surfaces-engine-feedback — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Surface untriaged engine_feedback rows in bin/selvedge orient so triage signal is visible at session-open.

**Kind:** substantive.  **Outcome:** adopt process_rule `orient-surfaces-untriaged-feedback`.

**Why.**

- (engine_feedback) EF-S092-3 surfaced that engine_feedback authoring requires raw SQL today; the corollary is that filed rows are invisible to orient and silently age until subtract-eligibility flags them at P_TRIAGE=3.
- (operator_directive) Operator directed that orient include feedback items so they can be read and triaged into other records during the next session-open.

**Effects.**

- modifies _orient_sections + _orient_markdown gain an untriaged_feedback section filtering disposition IS NULL

**Rejected alternatives.**

- **R-1.1.** Leave orient unchanged and rely on subtract-eligibility (P_TRIAGE=3 sessions) to surface feedback for triage.
  - (no_feedback_loop) Feedback filed in S092 stays invisible until S095 under the aging path; operator triage cadence is per-session, not every-three.
- **R-1.2.** Add a separate selvedge feedback subcommand that prints untriaged rows on demand.
  - (redundant_with_existing) orient is already the dispatch packet; a parallel command splits the surface a session author has to read.
