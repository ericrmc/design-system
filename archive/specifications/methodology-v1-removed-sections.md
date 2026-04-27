---
title: methodology-v1 removed sections (per 078 D-7)
status: superseded
superseded-by: methodology-v2 (engine-v17, session 079)
superseded-on: 2026-04-27
provenance: provenance/079-substrate-vertical-slice/
---

# Sections removed from methodology.md by 079 application of 078 D-7

This file preserves the prose of three sections of `methodology.md` v1 (engine-v16) that 079 removed when applying 078 D-7. Preservation per `methodology.md` v1 §Preservation: "specifications evolve through new versions, not silent edits. When a spec is revised, the prior version is preserved (in archive or under a versioned filename) and the new version takes its place at the canonical filename."

The three sections are listed in the order they appeared in v1.

---

## §"When to review at close" (removed in full per D-7 step 1)

A separate **reviewer** audits the session at close when:

- The session changed engine-definition files (specifications, prompts, tools).
- A structural validation check warned or failed.
- The operator requests a review.

The reviewer must not be the session's orchestrator, the close author, or the primary implementer of the work being audited. The reviewer reads the session's record (assessment, deliberation if any, decisions, close, produced artefacts) and produces an audit at `provenance/NNN-<slug>/04-review.md` reporting:

1. **Close correctness** — does the close accurately record what was decided, what was produced, and what state the workspace is in?
2. **Mechanism adequacy** — did the methodology's mechanisms function as designed for this session?
3. **Trajectory discipline** — across the recent sessions, is the methodology doing substantive work or accumulating ceremony?

A reviewer's findings are inputs to subsequent sessions. The reviewer does not fix problems; the next session does.

**Replacement in v2:** "Close-time review is superseded until the substrate distinguishes prevention from audit; D-2 conditional re-introduction governs."

**Why removed.** 078 D-2 cuts the LLM reviewer at first cut; 078 D-7 step 1 removes the spec section. Conditional re-introduction in 080+ governs whether a reviewer returns and in what shape.

---

## §"Validation senses" — third bullet only (provisional reference substitute, removed per D-7 step 2)

> **Provisional reference substitute** — when a session produces an external-intent artefact and no domain-actor is available, the session may compare its artefact to a sealed reference under blind conditions. This is a provisional substitute for domain validation, not an equal third sense; an artefact validated this way carries the label `validation: reference-provisional` and is qualified by the cross-family pretraining-recoverability of the reference.

**Why removed.** 078 D-7 step 2 collapses validation senses to workspace + domain only. Provisional-reference-substitute was the engine-v6 (session 033 OI-016 resolution) accommodation for user-unavailability; under engine-v17's external-pressure orientation (D-5 release gate; first external-problem trial gating further self-development), the substitute is unnecessary scaffolding. If it is needed in 080+, it returns through the same conditional path as the LLM reviewer.

---

## §"What this kernel does not say" (removed in full per D-7 step 3)

This kernel intentionally does not specify:

- A retrieval substrate, a records substrate, or any database schema. The next two sessions will design these.
- Multi-agent orchestration patterns beyond the deliberation pattern above. The next two sessions will design distributed-context-agent architectures.
- A read budget or a default-read surface. The seventy-five-session engine accumulated a closed-enumeration default-read that grew until it consumed half the agent's context window; the successor design will not repeat that mistake.
- An audit-shape for reviewer outputs beyond the three reporting axes above. The next two sessions will redesign the audit shape against the actual database substrate.

These omissions are deliberate. The kernel here is the minimum that allows session 077 to run. Session 077 will deliberate on what the next-generation engine should add.

**Why removed.** 078 D-7 step 3: meta-disclaimers about what 077 did not say have been superseded by 078's commitments themselves (D-1 substrate-shape, D-2 agent set, D-9 substrate technology). The "did-not-say" list is no longer load-bearing once the said-list closes the gaps.
