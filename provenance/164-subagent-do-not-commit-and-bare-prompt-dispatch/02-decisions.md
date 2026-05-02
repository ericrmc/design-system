---
session: 164
title: subagent-do-not-commit-and-bare-prompt-dispatch — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Bump prompt-development v15 to v16: §4 subagent do-not-commit boilerplate clause and §1.5 bare-PROMPT.md auto-proceed dispatch with codex shape-consult.

**Kind:** substantive.  **Outcome:** supersede spec_version `prompt-development@16`.

**Why.**

- (engine_feedback) EF-S161-2 surfaced subagent commit fragmenting provenance; FR-S161-18 explicitly named do-not-commit boilerplate as the spec-only remedy. [EF-S161-2]
- (operator_directive) Operator directed bare-PROMPT.md auto-proceed default with codex shape-consult for substantive paths and wait-for-direction when input has additional text.
- (prior_decision) Prior prompt-development bump DV-S157-1 carried §4 subagent-tool-class clause; this bump extends §4 and §1.5 in the same surface. [DV-S157-1]

**Effects.**

- supersedes prompt-development v15 superseded by v16 carrying §4 do-not-commit and §1.5 dispatch-mode clauses.

**Rejected alternatives.**

- **R-1.1.** Defer §1.5 dispatch-mode change; keep universal wait-for-confirmation and only ship §4 do-not-commit clause.
  - (operator_override) Operator explicitly directed both clauses in the same turn; splitting would defer half against operator direction with no efficiency win on a single spec_only bump.
- **R-1.2.** Make do-not-commit a harness-side gate (subagent prompt linter or git-hook refusal) rather than a spec clause.
  - (too_large_for_session) Harness-side enforcement requires coding scope (prompt linter or scoped git hooks) and was named as the v2 graduation path; spec-clause discipline is the v1 step per the typed-observation to gate progression.
- **R-1.3.** Auto-proceed on any unprescriptive operator input including generic terms (continue, next, keep going).
  - (operator_override) Operator directed wait-for-direction whenever input has text beyond the bare PROMPT.md; generic terms still signal operator presence even though they are unprescriptive.
