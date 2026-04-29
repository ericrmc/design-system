---
session: 118
title: enforce-opens-issue-target-issue-id — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Tighten target_issue_id enforcement at submit-time for opens_issue effects via T-29 and handler resolution.

**Kind:** calibration.  **Outcome:** adopt process_rule `decision_effects-opens-issue-target-issue-id`.

**Why.**

- (engine_feedback) EF-S117-1 observed 8/14 opens_issue effects carry NULL target_issue_id and proposed mirroring the engine-v28 closes_issue dispatch as the structural fix. [EF-S117-1]
- (prior_decision) DV-S098-1 established the closes_issue dispatch pattern at engine-v28 with T-27 refusing NULL target_issue_id and T-28 enforcing the resolved status precondition. [DV-S098-1]
- (constraint) Chain-walk export already paid the cost of word-boundary regex over target_descriptor to disambiguate OI-S110-1 from OI-S110-12; FK enforcement removes that fragile substring path entirely.

**Effects.**

- adds_migration 022_opens_issue_target_issue_id_enforcement.sql adds T-29 and bumps engine version.
- modifies _submit_decision_record opens_issue branch resolves target alias to target_issue_id and refuses NULL.
- bumps_engine engine-v33 to engine-v34 for opens_issue submit-time FK enforcement.
- modifies prompts/development.md step 5 documents opens_issue target alias requirement.

**Rejected alternatives.**

- **R-1.1.** Dispatch _submit_issue in-band from the opens_issue branch so the decision-record creates the issue row inline, mirroring closes_issue dispatch more literally.
  - (inferior_tradeoff) issue creation requires priority/title/summary/body; folding all four into decision_effects payload bloats the schema for marginal ergonomic gain over a separate issue-open submit.
- **R-1.2.** Add T-29 alone without modifying the handler, leaving operators to supply target_issue_id directly in the JSON payload.
  - (violates_gate) decision-record payload schema exposes target alias not target_issue_id; without handler resolution the trigger would refuse every existing operator pattern.
- **R-1.3.** Defer enforcement and let chain-walk continue to use the descriptor-substring fallback with the word-boundary regex tightening already in place.
  - (preserves_legacy_path) the substring fallback is fragile (regex assumes alias format) and any new alias scheme would break it; the FK is the durable fix.
