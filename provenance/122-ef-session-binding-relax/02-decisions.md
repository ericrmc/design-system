---
session: 122
title: ef-session-binding-relax — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Ship bin/selvedge feedback wrapper that opens meta session, submits EF(s), and closes — covering single-EF and batch intake; engine_feedback.session_id remains NOT NULL.

**Kind:** substantive.  **Outcome:** adopt process_rule `feedback-intake-wrapper`.

**Why.**

- (deliberation) Cross-family deliberation 13 converged C-1 (reject schema relaxation), C-2 (adopt wrapper), C-3 (friction is operator-discipline drift).
- (engine_feedback) EF-S122-1 named the friction directly; peer hit it 3 times (S005, S006, S007) without surfacing as EF. [EF-S122-1]
- (constraint) engine_feedback.session_id NOT NULL is load-bearing across orient, anchor x3, monitor-external x3, subtract, alias indexer.

**Effects.**

- creates selvedge/feedback_cmd.py: cmd_feedback wrapping session-open + engine-feedback + close-record + session-close
- modifies selvedge/cli.py: adds feedback subcommand with --body, --flag, --batch support

**Rejected alternatives.**

- **R-1.1.** Make engine_feedback.session_id nullable (option A): simplest schema delta.
  - (breaks_invariant) Six query sites inner-join engine_feedback to sessions and key on workspace_session_no; alias namespace is per-session-defined; null-safe rewrites everywhere.
- **R-1.2.** Introduce a sentinel never-closing system session (option B).
  - (breaks_invariant) Violates T-29 immutability and unique-open-session invariant; collides with harvest-ef under concurrent open sessions.
- **R-1.3.** Auto-create transient session inside submit engine-feedback handler (option C).
  - (inferior_tradeoff) Hides ceremony rather than naming it; doubles substrate footprint per EF without provenance benefit; the wrapper does the same dance honestly.
- **R-1.4.** Status quo, no change (option E): document session-as-feedback-vehicle as deliberate.
  - (violates_gate) Four observed instances of friction (peer S005, S006, S007 + self-dev S122 near-miss); FR-S116-9 reopen criterion crossed.
