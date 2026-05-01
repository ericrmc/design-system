---
session: 157
title: prompt-development-doc-gaps — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Bump prompt-development v12 to v13: §4 subagent-tool-class guidance and §6 spec-version payload-shape example.

**Kind:** substantive.  **Outcome:** supersede spec_version `prompt-development@13`.

**Why.**

- (engine_feedback) OI-S156-1 names §4 doc gap: Explore is read-only and rejects perspective-body Write at deliberation dispatch.
- (engine_feedback) OI-S156-2 names §6 doc gap: required session_no and supersedes for non-initial spec-version submits are not surfaced.
- (prior_decision) FR-S156-6 explicitly proposed rolling OI-S156-1 plus OI-S156-2 into a small spec_only batch as the next prompt-development bump.

**Effects.**

- supersedes SPEC-prompt-development-v12 — prompt-development active version v12 to v13.
- closes_issue OI-S156-1 — Close OI-S156-1 §4 subagent-tool-class doc gap.
- closes_issue OI-S156-2 — Close OI-S156-2 §6 spec-version payload-shape doc gap.

**Rejected alternatives.**

- **R-1.1.** Defer the doc gaps and ship a larger coding bump for harness ergonomic migrations 030+ instead (FR-S155-13 path).
  - (too_large_for_session) Harness ergonomic migrations are migrations-plus-handler scope; the doc gaps are 2 small inline edits and FR-S156-6 explicitly named them as the cheap follow-up.
- **R-1.2.** Consolidate both doc gaps into one combined advisory block instead of editing each section in place.
  - (inferior_tradeoff) Operator-discoverability is best when guidance lives where the relevant CLI surface is described; consolidation buries the §4 fix at distance from the deliberation flow.
