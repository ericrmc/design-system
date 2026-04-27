---
session: 088
title: issues-table — close
engine_version_at_close: engine-v22
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S088 ships engine-v22: substrate-native issues table replaces 25 markdown OIs as the canonical dispatch surface; three-perspective deliberation, MAD synthesis, two-iteration coding review, subagent backfill.

## Engine version

- engine-v21 to engine-v22 via migration 009 + four new CLI submit kinds.
## What was done

- Convened three-perspective deliberation (P-1 anthropic-pragmatic, P-2 codex-cross-family, P-3 anthropic-adversarial); 3 positions + 82 claims captured.
- Sealed deliberation 4; recorded 5 convergence + 5 divergence + 2 minority synthesis-points.
- DV-S088-1 adopts schema synthesis: closed five-status enum, title+summary atoms with optional legacy_import body, dedicated link/note/disposition tables, four CLI kinds.
- Migration 009 ships issues + issue_links + issue_notes + issue_dispositions tables; T-22 alias GLOB, T-22a terminal-status invariant, T-23 self-loop refusal.
- CLI handlers added to selvedge/cli.py: submit issue / issue-disposition / issue-link / issue-note; reviewer iteration 2 surfaced critical INSERT-status bypass which was fixed.
- Backfill subagent migrated 29 of 30 markdown files into issues rows; orchestrator manually adjudicated OI-079-001 (free-text status). Final: 31 issues, 23 open, 8 resolved.
- Markdown OI files deleted; open-issues/index.md rewritten as a CLI pointer; substrate becomes single source of truth.
- engine-manifest.md updated to v22; spec-version v22 submitted; v22 decomposed (6 sections, 90 clauses); body_canonical_in_substrate=1 on all six active specs.
## State at close

- current_engine_version=engine-v22; 31 issues in substrate; no open review findings; dispatch query verified end-to-end (returns OI-016 + OI-085-002 as top-priority HIGH).
## Open issues

- OI-S088-1: dispositions/links reuse rejection_reason atom_type; future migration should add dedicated atom types via text_atoms recreation.
- Three other items remain from S087 close: _submit_spec_version handler bugs (INSERT-active-then-flip-prev order; no-op UPDATE on already-superseded prev trips T-06).
## What the next session should address

- Either fix _submit_spec_version handler order, or work the dispatch queue: OI-016 / OI-085-002 (both HIGH) are top-of-queue.
## Validator at close

- Pending bash tools/validate.sh post-export; expected pass.
