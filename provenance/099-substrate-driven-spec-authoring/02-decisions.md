---
session: 099
title: substrate-driven-spec-authoring — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Extend submit spec-version to accept inline body_md so handler writes the body file in-process within the same write transaction.

**Kind:** substantive.  **Outcome:** adopt engine_version `engine-v29`.

**Why.**

- (engine_feedback) EF-S098-3 names two iteration-1 findings adjudicated rather than fixed in S098 because the PreToolUse hook refuses direct edits to substrate-canonical files. [EF-S098-3]
- (operator_directive) Operator ratified the S099 proposed agenda to land OI-S090-5 substrate-CLI authoring before more sessions accumulate the same defer.

**Effects.**

- modifies _submit_spec_version accepts optional body_md and writes body_path in-process.
- bumps_engine engine-v28 to engine-v29
- closes_issue OI-S090-5 — OI-S090-5 resolved by inline body_md path.

**Rejected alternatives.**

- **R-1.1.** Build a spec-clause-driven body materialiser that regenerates body markdown from spec_clauses for every spec_version submit (Path A from OI-S090-5).
  - (too_large_for_session) Path A requires completing substrate decomposition for engine-manifest and prompt-development (body_canonical_in_substrate=0 today) before it can run; that is multi-session work outside S099 scope.
- **R-1.2.** Add a separate submit kind spec-body that writes the file then expects a follow-up submit spec-version to insert the row.
  - (inferior_tradeoff) Two-call surface splits an atomic intent across handlers; a partial state where the file is on disk but no spec_versions row exists would require operator-policed cleanup. Inline body_md keeps the write transactional.
