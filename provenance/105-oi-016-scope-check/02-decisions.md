---
session: 105
title: oi-016-scope-check — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Close OI-016 (pre-restart mechanism archived) and spawn OI-S105-1 for methodology kernel third-sense reconciliation

**Kind:** disposition.  **Outcome:** adopt issue `OI-016`.

**Why.**

- (prior_decision) DV-S092-1 deferred OI-016 awaiting new signal; this scope-check supplies the signal. [DV-S092-1]
- (constraint) Reference-validation.md cited in the OI-016 body was archived at the S076 engine-v16 restart; the bound resolution is no longer in the active engine.
- (spec_clause) methodology.md line 38 names three validation senses but the senses subsection enumerates only workspace and domain.

**Effects.**

- closes_issue OI-016 — superseded by S076 restart; pre-restart mechanism archived
- opens_issue OI-S105-1 methodology kernel third-sense reconciliation

**Rejected alternatives.**

- **R-1.1.** Keep OI-016 open and rewrite the body to describe the post-restart shape of the constraint.
  - (redundant_with_existing) Live concern is the smaller methodology line-38 inconsistency; rewriting OI-016 in those terms duplicates OI-S105-1 under stale alias.

## D-2. Remove kind=coding default from session-open handler; require explicit declaration from {coding, spec_only, meta}

**Kind:** calibration.  **Outcome:** adopt process_rule `session-open-requires-kind`.

**Why.**

- (operator_directive) Operator directed removing the default after this session was opened as kind=coding when its substantive work is spec_only.
- (engine_feedback) Default-to-coding silently mismatched session intent in this session; explicit declaration forces the operator to think before open.
- (prior_decision) Engine-v31 (S104) introduced sessions.kind with a default to bootstrap the coding review loop; the default was provisional during rollout. [DV-S104-1]

**Effects.**

- modifies selvedge/cli.py _submit_session_open: refuse on missing kind
- modifies SPEC-prompt-development-v6 — prompts/development.md §2 documents required kind enum
