---
session: 086
title: substrate-invariant-audit — close
engine_version_at_close: engine-v20
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S086 audited substrate invariants and adjudicated 8 findings; surfaced OI-086-001..004 plus folded F1/F6/F7 into OI-085-001/002.

## Engine version

- engine-v20 (no version bump in S086).
## What was done

- Substrate-invariant audit: confirmed no open_issues table or submit-open-issue kind; all 272 spec_clauses have NULL source_decision_v2_id; refs and decisions_v2 invariants hold.
- Submitted 8 review_findings (F1 high; F2-F8 medium); adjudicated each per DV-S086-1 with disposition_text linking to OI-085-001/002 or OI-086-001..004.
- Authored OI-085-001 (long-overdue file) and OI-086-001..004 markdown carriers; updated open-issues/index.md to count 22 active.
## State at close

- All review_findings adjudicated; no medium-or-higher open. T-20 satisfied. Substrate at 35 tables; aliases coherent; refs zero-dangling; legacy_imports mixed-state per F8.
## Open issues

- OI-086-001 spec_clause source_decision_v2_id traceability (NULL on all 272 rows); fix paired with OI-085-001 re-decomposition.
- OI-086-002 single-active spec_version per spec_id needs partial unique index; OI-086-003 cited_object_id NOT NULL on cite-required bases needs lookup table.
- OI-086-004 legacy_imports.decomposition_status semantics (perspectives 1-5 ratified yet undecomposed; 6-8 in_progress yet 126 claims captured).
## What the next session should address

- Spawn spec-decomposition subagent for prompt-development v2, prompt-application v2, engine-manifest v20 to flip body_canonical_in_substrate=1 (OI-085-001).
- Either land OI-085-002 harness hook plus submit-open-issue and submit-engine-feedback kinds, or take OI-086-002 single-active partial unique index as a minimal-pass schema-migration session.
## Validator at close

- tools/validate.sh pending post-export; expected pass since no methodology/spec content authored. body_canonical_in_substrate=0 on three active v2 specs is a tracked condition, not a validator failure.
