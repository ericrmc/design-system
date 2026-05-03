---
session: 081
title: substrate-loss-defense-design — close
engine_version_at_close: engine-v51
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S081 deliberation-only session: 4-perspective deliberation adopts DV-S081-1 substrate-loss-defense-v1 design package; engine v50 to v51 via mid-session calibration migration 041 unblocking T-33 process_rule decisions.

## Engine version

- engine-v50 to engine-v51 via migration 041 (decision_prechecks.target_kind CHECK widening) plus selvedge/precheck.py + selvedge/cli.py + selvedge/submit/decision_v2.py:77 patches.
## What was done

- Convened 4 cross-family perspectives (P-1 anthropic layered-defense + P-2 openai cross-family + P-3 anthropic minimalist + P-4 anthropic operator-ergonomics) on substrate-loss defense design.
- Sealed deliberation D-1 with 3 counterfactuals + 9 convergences + 3 divergences + 3 minorities preserved (M-1 minimalist + M-2 every-tx-snapshot + M-3 phased-rollout).
- Adopted DV-S081-1 substrate-loss-defense-v1 package: L1a init guard + L2b subagent clone + L3 boundary snapshots with restore CLI + L4B extractor + L5 close-export expansion + engine-v51 marker.
- Opened OI-S081-1..8 cluster as implementation handoff (each layer a separate workstream); rejected R-1.1 P-1 maximal + R-1.2 P-3 minimalist + R-1.3 L2a-only + R-1.4 L4A-skip + R-1.5 L4C-replay + R-1.6 phased-rollout.
- Shipped calibration migration 041 + decision_v2.py handler fix + test updates (test_export.py + test_path_a_kinds.py) to unblock T-33 for non-decision_v2 target_kinds; 285 pytest pass.
## State at close

- Substrate: 1 sealed deliberation, 4 perspectives, 174 perspective-claims, 3 counterfactuals, 15 synthesis-points, 1 decision_v2 (DV-S081-1), 9 issues open including OI-S180-1 + 8 new OI-S081-N implementation handoffs.
- Working tree: state/migrations/041 plus selvedge/precheck.py + selvedge/cli.py + selvedge/submit/decision_v2.py + state/tests/test_export.py + state/tests/test_path_a_kinds.py edits; 3 EFs authored at close.
## Open issues

- OI-S180-1 HIGH stays open (umbrella for substrate-wipe remediation); OI-S081-1..8 newly opened tracking each implementation workstream for S082+ pickup.
## What the next session should address

- S082 implements OI-S081-1 (L1a init --force live-substrate refusal in selvedge/init_cmd.py with --really-force escape) plus OI-S081-8 (PROMPT.md §4 subagent-discipline boilerplate amendment) as the smallest defense slice.
- S083 implements OI-S081-3 (L3 snapshot machinery via SQLite Connection.backup at session-open + close + migrate + init triggers) plus OI-S081-4 (bin/selvedge restore CLI with --confirm token).
- S084 implements OI-S081-2 (L2b subagent tempdir-clone isolation via SQLite backup API; SELVEDGE_READONLY remains advisory) plus OI-S081-5 (L4B legacy-substrate extractor one-shot run).
- S085 implements OI-S081-6 (L5 close-time export expansion across 8 enumerated artefacts: open-issues, spec_versions, EFs, counterfactuals, FR-disp, prechecks, chain-walks, harness state).
- S086 ships OI-S081-7 (engine-v51 marker migration coupling: snapshot_catalog + L5 export-manifest tables; collapses with prior session if scope permits).
- Watch M-1 P-3 minimalist warning carrier-forward: if any defense fires on legitimate workflow >2x in S082+, surface calibration-EF demanding override-routinization triage per P-3 risk thesis.
- Watch C-4 restore-CLI tested-recovery requirement: OI-S081-4 must include CI-exercised restore drill or it does not close per P-2 + P-4 convergence; otherwise snapshot machinery is decorative.
## Validator at close

- pytest 285 pass (1 fix to test_export.py + 6 fixes to test_path_a_kinds.py for the precheck-target-kind decoupling); migrate 41 applied 0 pending; substrate validate clean (no precommit run yet).
