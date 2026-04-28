---
session: 106
title: disaster-response-arc-restart — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Adopt arc-plan v2 for disaster-response external trial: 7 committed phases over 21 sessions plus adaptive extension to 30 on EF-yield evidence at S021 retrospective

**Kind:** substantive.  **Outcome:** adopt process_rule `disaster-response-arc-v2`.

**Why.**

- (deliberation) P-2 cross-family critique decisive on engine-surface mapping over domain-flavoured axes; surface taxonomy honest about what each reveal exercises. [P-9-P-2]
- (operator_directive) Operator named seven to ten constraint changes across approximately thirty sessions as the trial shape; adaptive 21+9 satisfies both the gate count and the evidence-yield discipline.
- (constraint) Constraints six warns growth without external pressure produces internal elaboration; capping at 21 with extension-on-evidence respects this.

**Effects.**

- creates applications/001-disaster-response-arc/arc-plan.md (v2)
- supersedes S047 arc-plan five-session v1 placed in provenance/047-session/

**Rejected alternatives.**

- **R-1.1.** Adopt 5-session arc per S047 unchanged with the original four reveal axes (P-3 minimalist position).
  - (inferior_tradeoff) v7 empirical evidence shows baseline alone consumes 3 sessions; 4 reveals after baseline is too few to exercise the engine surfaces named.
- **R-1.2.** Adopt fixed 27-session 9-phase shape with 8 domain-flavoured reveals (P-1 pragmatic-hybrid position as proposed).
  - (inferior_tradeoff) P-2 critique decisive: domain-flavoured 8 axes overlap on engine surfaces (coordination plus legal plus political fold to authority conflict); honest surface mapping reduces to 6 axes plus baseline plus meta.

## D-2. Define v31 bootstrap scope: engine-definition file set, selvedge package, migrations, PreToolUse hook, .claude/settings.json, validate.sh, then bin/selvedge init and workspace_metadata seed; defer rebuild to S107 coding session

**Kind:** substantive.  **Outcome:** adopt process_rule `bootstrap-external-workspace-v31-scope`.

**Why.**

- (deliberation) Synthesis convergence C-2 across all three perspectives on bootstrap minimalism; intersection of P-1 P-2 P-3 file lists is the recommended scope. [P-9-P-2]
- (prior_decision) Engine-v7 bootstrap script archived at archive/pre-restart/tools/ references retired specs and is unsalvageable in its current form.
- (spec_clause) Engine-manifest spec section three enumerates the active engine-definition file set; bootstrap copies exactly that set without ancillary cargo.

**Effects.**

- opens_issue Rebuild tools/bootstrap-external-workspace.sh per S106 scope (S107 coding session)

**Rejected alternatives.**

- **R-2.1.** Include retrieval substrate plus aliases.yaml seed plus .mcp.json in the bootstrap (matches engine-v7 era script's accumulated cargo).
  - (redundant_with_existing) Engine-v31 has no retrieval substrate; aliases.yaml and .mcp.json are not engine-definition; copying them would re-accumulate the cargo P-3 names as drift.
- **R-2.2.** Migrate the existing v7 disaster-response workspace forward in place rather than fresh bootstrap.
  - (preserves_legacy_path) Engine-v31 substrate refuses prose-state patterns the v7 markdown workspace embodies; in-place migration would smuggle legacy assumptions into the new substrate.

## D-3. Adopt hybrid orchestration: operator-driven external sessions plus monitor-external CLI in self-dev with three subcommands status next-input harvest-ef; defer implementation to S108 coding session

**Kind:** substantive.  **Outcome:** adopt process_rule `external-workspace-orchestration-mechanism`.

**Why.**

- (deliberation) P-1 and P-2 converge on thin three-subcommand scope; P-2 emphasises tool is load-bearing only if it reduces context-loss and transport errors, must be deleted if it becomes status theatre. [P-9-P-2]
- (constraint) Constraints six names operator-as-diagnostic-substrate as the structural feature 75 self-dev sessions silently relied on; thin tooling preserves the operator-as-transport role rather than replacing it.
- (operator_directive) Operator named monitor-external as the generic name (not arc-monitor or arc-driver), reusable beyond this single arc.

**Effects.**

- opens_issue Implement bin/selvedge monitor-external (S108 coding session)

**Rejected alternatives.**

- **R-3.1.** Pure operator transport (Option A): no CLI tooling; operator does all status reads, input drafting, and EF transport manually.
  - (inferior_tradeoff) Preserved as activation-warranted minority M-1 (P-3 position); not selected as primary because mechanical transport across 21+ sessions accumulates per-session cost the operator should not pay if the substrate can be queried directly.
- **R-3.2.** Headless subprocess orchestration (Option C): self-dev spawns Claude Code in external workspace via Bash for each session.
  - (breaks_invariant) Removes the human reviewer constraints six names as non-optional; rejected by all three perspectives.

## D-4. Hard reset external workspace: archive existing v7 selvedge-disaster-response into self-dev archive directory; bootstrap fresh from current engine-v31

**Kind:** substantive.  **Outcome:** adopt process_rule `external-workspace-disposition`.

**Why.**

- (deliberation) Synthesis convergence C-1 across all three perspectives; engine has changed too much for honest migration. [P-9-P-1]
- (prior_decision) Engine-v31 substrate-only writes (engine-v20 D-2) refuse the prose-state pattern the v7 markdown workspace embodies; migration would smuggle pre-substrate assumptions in.
- (constraint) Constraints one prose-state and two failure-as-cheap properties show that mixing pre-substrate artefacts into substrate-canonical engine creates the friction-without-feedback failure mode the engine was redesigned to prevent.

**Effects.**

- creates archive/v7-trial-2026-04-24-disaster-response/ (v7 workspace move target)
- opens_issue Archive v7 disaster-response workspace before S107 bootstrap rebuild

**Rejected alternatives.**

- **R-4.1.** Inherit v7 artefacts (system-model, assumption-ledger, response-plan, risk-register) into the new v31 workspace as S001 starting state.
  - (inferior_tradeoff) Smuggles prose-state assumptions (Markdown-table-as-database) into substrate-canonical engine-v31; P-1 names the cost as faithful to neither substrate.
- **R-4.2.** Leave v7 workspace stale and select a different external-problem application for the trial.
  - (too_large_for_session) Designs a new application brief, identifies new validators, repeats the bootstrap setup cycle; not justified when the v7 brief content remains good source material.

## D-5. Place arc-plan v2 at applications/001-disaster-response-arc/arc-plan.md in self-dev workspace as mutable artefact across arc-revision sessions; bootstrap does not copy it into the external workspace

**Kind:** substantive.  **Outcome:** adopt process_rule `arc-plan-v2-placement`.

**Why.**

- (deliberation) Synthesis convergence C-3 across all three perspectives on mutable applications/-class placement. [P-9-P-1]
- (prior_decision) S047 sealed-in-provenance placement was tried and proved wrong about cadence (5-session estimate off by approximately six times); a mutable copy lets later self-dev sessions revise the arc when reality contradicts.
- (spec_clause) Workspace spec section File classes admits applications/ as mutable artefact class; arc-plan is application-coordination material, not session provenance, so it belongs there.

**Effects.**

- creates applications/001-disaster-response-arc/arc-plan.md

**Rejected alternatives.**

- **R-5.1.** Seal arc-plan v2 in provenance/106-session/arc-plan.md per D-017 immutability (matches S047 placement).
  - (inferior_tradeoff) Immutability prevents adaptive extension at S021 and any mid-arc revision when empirical evidence contradicts the planned shape; S047 demonstrated this cost.
