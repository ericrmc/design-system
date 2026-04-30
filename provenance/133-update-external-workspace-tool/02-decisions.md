---
session: 133
title: update-external-workspace-tool — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Ship tools/update-external-workspace.sh; fix tools/bootstrap-external-workspace.sh stale constraints.md spec copy loop

**Kind:** substantive.  **Outcome:** adopt process_rule `engine-update-propagation`.

**Why.**

- (operator_directive) Operator selected option (c) — ship the update tool first, then use it on disaster-recovery — after S132 surfaced the missing-tool gap and the stale-bootstrap-script bug.
- (spec_clause) engine-manifest section 3 enumerates the engine-definition file set canonically; both bootstrap and update tools must derive their ship list from this same source-of-truth. [SPEC-engine-manifest-v39]
- (prior_decision) DV-S109-1 subtracted constraints.md at engine-v32; bootstrap script never updated to drop it from spec copy loop, creating a latent bug that surfaces on next external bootstrap. [DV-S109-1]

**Effects.**

- creates tools/update-external-workspace.sh new script for engine-update propagation
- modifies tools/bootstrap-external-workspace.sh remove constraints.md from spec list

**Rejected alternatives.**

- **R-1.1.** Skip the tool; document a manual rsync command in workspace.md or methodology.md for operators to copy-paste each update.
  - (inferior_tradeoff) Manual rsync recipe leaves no pre-flight checks (open-session, mode mismatch) and no subtracted-file cleanup; constraints.md case shows latent bugs accumulate without structural propagation.
- **R-1.2.** Build update logic into bin/selvedge as a substrate-aware subcommand (e.g. bin/selvedge propagate --target <path>).
  - (too_large_for_session) Substrate-aware subcommand requires Python handler design and substrate role-capability; shell tool matches existing bootstrap precedent and ships the gap-filler in one session.
- **R-1.3.** Parse engine-manifest section 3 markdown table at runtime to derive SHIP_FILES instead of hard-coding the list.
  - (inferior_tradeoff) Markdown parsing is fragile across formatting drift; hard-coded list with explicit comment pointing at engine-manifest section 3 matches bootstrap precedent and audits each touch.
