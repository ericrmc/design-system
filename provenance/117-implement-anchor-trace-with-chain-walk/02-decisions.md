---
session: 117
title: implement-anchor-trace-with-chain-walk — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Implement OI-S114-1 v1: bin/selvedge export --provenance --anchor with bounded chain-walk over the closed edge family.

**Kind:** substantive.  **Outcome:** adopt issue `OI-S114-1`.

**Why.**

- (prior_decision) DV-S116-1 set v1 scope: default depth 3 hard cap 5 visited-set cycles deterministic order closed edge family. [DV-S116-1]
- (prior_decision) DV-S114-1 fixed the surface as anchor-only markdown projection with --graph and workspace mode deferred. [DV-S114-1]
- (engine_feedback) EF-S110-7 framed the original gap as a multi-hop cross-session causal chain stakeholders cannot reach without raw SQL. [EF-S110-7]
- (review_finding) T-30 reviewer subagent passed clean across closed-family coverage cycles depth bounds alias resolution determinism resource and CLI ergonomics.

**Effects.**

- modifies selvedge/cli.py adds anchor-trace export and --provenance --anchor --max-depth flags
- creates provenance/anchor-traces/<alias>.md materialised by --write
- closes_issue OI-S114-1 — Anchor-trace export shipped per DV-S114-1 surface and DV-S116-1 chain-walk scope; reviewer clean.

**Rejected alternatives.**

- **R-1.1.** Expand session-as-neighbour to all sibling decisions/EF/specs so a transit through a session surfaces every artefact in it.
  - (inferior_tradeoff) EF-S110-7 depth 3 measured 49 nodes under broad expansion versus 22 after tightening; sibling EFs diluted the causal chain.
- **R-1.2.** Skip the descriptor-substring fallback in _decisions_citing_issue and rely solely on target_issue_id FK.
  - (inferior_tradeoff) 8 of 14 opens_issue effects carry NULL target_issue_id; without fallback OI- anchors miss their originating decisions.
