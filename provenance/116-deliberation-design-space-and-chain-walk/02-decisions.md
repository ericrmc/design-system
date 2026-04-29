---
session: 116
title: deliberation-design-space-and-chain-walk — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Chain-walk folds into OI-S114-1 v1 with bounded depth: default 3, hard cap 5, --max-depth flag, cycle handling, closed edge family.

**Kind:** substantive.  **Outcome:** adopt open_question `chain-walk-scope-for-anchor-trace-v1`.

**Why.**

- (deliberation) Synthesis takes P-2 on Q1: depth-1 anchor-only does not answer the original EF-S110-7 framing across multiple hops. [P-12-P-2]
- (engine_feedback) EF-S110-7 framed the gap as DV-S001-5 to DV-S002-1 to S003 cross-session lineage, requiring multi-hop walk. [EF-S110-7]
- (engine_feedback) EF-S115-1 surfaced chain-walk as the sideways shape neither S114 perspective named; out-of-frame would normalise the under-exploration pattern. [EF-S115-1]
- (prior_decision) DV-S114-1 chose anchor-rooted (not workspace) which both perspectives still affirm; depth was outside S114's frame, so v1 scope can extend without overturning. [DV-S114-1]

**Effects.**

- creates OI-S114-1 v1: chain-walk default depth 3, cap 5, --max-depth flag, visited-set cycles, deterministic order.
- modifies Edge family: supports, effects, alternatives_v2, perspectives, FR dispositions, spec_versions.superseded_by.

**Rejected alternatives.**

- **R-1.1.** Ship anchor-only at depth-1 as v1 per P-1; layer chain-walk as v1.5 follow-up after v1 lands and is used.
  - (inferior_tradeoff) v1 that does not answer the originating EF-S110-7 question normalises a partial deliverable; learning from a non-answering v1 is unhelpful learning.
- **R-1.2.** Refuse chain-walk entirely; keep anchor-only as the design and require operators to compose multiple anchor traces.
  - (inferior_tradeoff) Substrate joins exist post DV-S113-1; refusing chain-walk leaves operators on raw SQL for the originally-named EF-S110-7 use case.
- **R-1.3.** Ship chain-walk with default depth higher than 3 or unbounded with cap only, per P-2's preference for recursive default.
  - (inferior_tradeoff) Default depth 3 with cap 5 admits multi-hop traversal answering EF-S110-7 while honouring shared concern that appetite grows under unbounded defaults.

## D-2. Adopt reopen-on-new-reading convention as methodology v5: load-bearing post-close option-surfacing is a legitimate trigger for a follow-up session.

**Kind:** substantive.  **Outcome:** adopt spec_version `methodology`.

**Why.**

- (engine_feedback) EF-S115-1 names the under-exploration pattern: deliberation produces compromise inside the proposed frame; sideways shapes surface post-close. [EF-S115-1]
- (deliberation) P-1 affirmed reopen as the lightest cost-bearing remedy; substrate already admits supersession so the cost is social, not structural. [P-12-P-1]
- (deliberation) P-2 framed reopening as normal substrate supersession not failure; both perspectives align on cheapness of the recovery path. [P-12-P-2]

**Effects.**

- creates methodology v5: reopen-on-new-reading convention; load-bearing post-close surfacing triggers follow-up session.

**Rejected alternatives.**

- **R-1.1.** Adopt P-2's stronger Q2 remedy: triggered design-space-audit sub-activity plus reopen discipline together.
  - (inferior_tradeoff) One data point (S114 chain-walk) does not warrant adding a sub-activity; reopen criterion is a second instance accumulating, captured in DV-S116-3 deferral.
- **R-1.2.** Make the convention a workspace.md addition rather than methodology.
  - (inferior_tradeoff) Workspace covers file/structure conventions; deliberation discipline is methodology's domain alongside existing convene/synthesis paragraphs.
- **R-1.3.** Adopt no convention; trust that operator post-close dialogue plus FR-queue is already self-evidently the recovery path.
  - (inferior_tradeoff) Self-evidence has not held: S115 had to author EF-S115-1 to surface the pattern; explicit convention lowers recovery cost for the next instance.

## D-3. Defer triggered design-space-audit sub-activity until a second instance of the under-exploration pattern accumulates.

**Kind:** substantive.  **Outcome:** defer open_question `design-space-audit-sub-activity`.

**Why.**

- (engine_feedback) EF-S115-1 raises one instance of the under-exploration pattern; adopting machinery on one data point would itself be the under-exploration pattern in reverse. [EF-S115-1]
- (deliberation) P-1 rejected the sub-activity as ceremony per session for benefit only when framing is incomplete; P-2 admitted ritual risk if triggered too broadly. [P-12-P-1]
- (prior_decision) DV-S109-1 subtracted constraints.md as ceremony; the engine has been removing per-session cost that does not pay for itself, raising the bar for additions. [DV-S109-1]

**Rejected alternatives.**

- **R-1.1.** Adopt the triggered design-space-audit sub-activity now per P-2; trigger threshold = reframe flag, high-impact OI, or operator request.
  - (inferior_tradeoff) Trigger-threshold over-correction: one instance and three plausible thresholds; adopting now risks ritual that does not pay for itself.
- **R-1.2.** Refuse the sub-activity entirely with no defer or reopen criterion stated.
  - (inferior_tradeoff) P-2 minority M-1 names the risk that adopting only reopen leaves the pattern under-addressed; reopen criterion preserves the option without the cost.
