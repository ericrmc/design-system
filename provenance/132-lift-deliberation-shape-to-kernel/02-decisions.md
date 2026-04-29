---
session: 132
title: lift-deliberation-shape-to-kernel — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Lift S131 deliberation-shape content from prompts/development.md to specifications/methodology.md kernel; trim development.md, fix application.md, bump engine-manifest v34 to v39

**Kind:** calibration.  **Outcome:** adopt spec_version `methodology`.

**Why.**

- (operator_directive) Operator identified that S131 deliberation-shape content is kernel-level and applies to both modes; calibration moves content to methodology.md preserving DV-S131-1 substantive scope without re-deliberating.
- (prior_decision) DV-S131-1 substantively decided the content via 6-perspective cross-family deliberation; this calibration corrects only the location, preserving scope and content unchanged. [DV-S131-1]
- (engine_feedback) EF-S131-2 calibration documented orchestrator's framing-bias slip pattern; same pattern repeated at meta level in S131 file-choice; structural correction warranted. [EF-S131-2]
- (operator_directive) Single-agent codex spot-check confirmed move-to-kernel framing with caveats: human/domain brief equivalence, cross-family scope preservation (methodology-touching), engine-manifest version-jump explicit narrative.

**Effects.**

- modifies methodology.md When-to-convene section absorbs S131 disciplines
- supersedes methodology v6 superseded by v7
- modifies prompts/development.md section 4 trimmed to mode-specific bits
- supersedes prompt-development v9 superseded by v10
- modifies prompts/application.md adds kernel pointer; fixes validation-senses drift
- supersedes prompt-application v2 superseded by v3
- modifies engine-manifest narrative addendum recording S131 + S132 + v35-v38 backfill
- supersedes engine-manifest v34 superseded by v39
- bumps_engine engine-v38 to engine-v39 via atomic-propagation

**Rejected alternatives.**

- **R-1.1.** Leave S131 content in prompts/development.md only; status quo from S131 close.
  - (violates_gate) External-problem applications inheriting prompts/application.md would receive weaker deliberation discipline through no principled reason; methodology.md is the kernel both modes inherit by design.
- **R-1.2.** Re-create specifications/multi-agent-deliberation.md as a separate spec carrying S131 content.
  - (preserves_legacy_path) methodology.md header explicitly notes it replaces the prior split across methodology-kernel.md, identity.md, multi-agent-deliberation.md, validation-approach.md; re-creating MAD spec re-fragments the kernel.
- **R-1.3.** Run a substantive 6-perspective deliberation about the move before relocating.
  - (inferior_tradeoff) Content was already deliberated in S131 with 6 perspectives and 7 convergences; relocation is calibration not substance; single-agent codex spot-check is appropriate ceremony per operator directive.
