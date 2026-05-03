---
session: 189
title: oi-s180-1-close-markdown-only-recovery — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Close OI-S180-1 by-mechanism: accept markdown-only recovery posture for pre-S180 substrate; reject rebuild-from-provenance as structurally lossy.

**Kind:** substantive.  **Outcome:** adopt issue `OI-S180-1`.

**Why.**

- (prior_decision) S186 L4B legacy-substrate-summary established markdown export is one-way (rows to text_atoms) with no FK structure to roundtrip; rebuild produces false typed authority from lossy source. [DV-S186-2]
- (prior_decision) Substrate-loss-defense-v1 design specifies L4B as inventory layer not rebuild; the design itself frames rebuild-from-export as out-of-scope and operator-curated if ever attempted. [DV-S081-1]
- (engine_feedback) Codex non-Anthropic shape-consult endorsed tactical close kind=meta with explicit FR-S080-9 supersede and warning against inferring typed rows from aliases or treating markdown as canonical. [EF-S189-1]

**Effects.**

- closes_issue OI-S180-1 — OI-S180-1 substrate-wipe rebuild + subagent destructive-op hardening

**Rejected alternatives.**

- **R-1.1.** Ship tools/rebuild-from-provenance.py per FR-S080-9 attempting partial reconstruction of substrate rows from markdown exports despite lossiness.
  - (inferior_tradeoff) Markdown export is structurally lossy (text_atoms only no FK structure); partial rebuild produces false substrate authority indistinguishable from genuine rows yet missing alias resolution and provenance walks per S186 inventory.
- **R-1.2.** Hold OI-S180-1 open indefinitely as future-debt awaiting operator-directed manual curation rebuild path.
  - (redundant_with_existing) S186 inventory plus markdown archive already constitute the recovery surface; holding the OI HIGH adds queue-noise without naming an actionable next step the engine can dispatch under bare-prompt auto-proceed.
