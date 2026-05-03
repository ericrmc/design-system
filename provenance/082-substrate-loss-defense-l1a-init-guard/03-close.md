---
session: 082
title: substrate-loss-defense-l1a-init-guard — close
engine_version_at_close: engine-v51
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S082 ships L1a init-guard substrate refusal in selvedge/init_cmd.py with --really-force escape plus prompts/development.md §4 subagent boilerplate part-two extension; closes OI-S081-1 + OI-S081-8.

## Engine version

- engine-v51 unchanged; L1a guard ships against the v51 marker established at S081.
## What was done

- L1a init guard implemented in selvedge/init_cmd.py (predicate: any sessions row exists; refusal text names row count + recovery + --really-force override).
- selvedge/cli.py argparse adds --really-force flag to init subparser as the deliberate destructive override.
- state/tests/test_init_guard.py adds 9 tests covering predicate edges (missing, empty, live, corrupt, partial-init, no-flag, refusal-message).
- prompts/development.md §4 boilerplate split into part-one do-not-commit + part-two do-not-mutate-substrate via SPEC-prompt-development-v1.
- DV-S082-1 sealed (substantive, target_kind=process_rule, 4 alternatives, 4 chain-walks; precheck nonce verified against substrate).
- T-30 review loop iter-1 surfaced 5 findings (2 HIGH test-gap, 3 MEDIUM); iter-2 clean.
## State at close

- 294 pytest pass (+9 test_init_guard cases over 285 baseline); validate.sh 17 ok / 0 fail; round-trip.sh failures pre-existing and unrelated to L1a.
- Substrate spec_versions chain begins at v1 post-S180-wipe; engine-manifest.md narrative claims v22 to v23 history not reflected in substrate rows; reconciliation deferred to FR-S082-1.
- OI-S180-1 stays open: step-5 (boilerplate) shipped here; rebuild-from-provenance.py per FR-S080-9 still pending; full closure couples both.
## Open issues

- OI-S081-1 + OI-S081-8 closed by-mechanism via DV-S082-1 effects (closes_issue handler dispatch in same write_tx).
- OI-S081-2 (L2b subagent tempdir-clone) + OI-S081-3 (L3 snapshot machinery) + OI-S081-4 (restore CLI) remain HIGH for S083 per FR-S081-11.
- OI-S081-5 (L4B legacy extractor) + OI-S081-6 (L5 export expansion) + OI-S081-7 (engine-v51 marker schema) remain for S084..S086 per FR-S081-12..14.
## What the next session should address

- FR-S082-1 reconcile prompt-development substrate spec_version chain post-wipe within OI-S081-6 territory; either rebuild via OI-S081-5 legacy extractor or accept post-wipe-v1 canonical and update engine-manifest narrative.
- FR-S082-2 implement OI-S081-2 L2b subagent tempdir-clone isolation via SQLite backup API plus OI-S081-3 L3 boundary snapshots at session-open + close + migrate + init triggers per FR-S081-11.
- FR-S082-3 ship OI-S081-4 bin/selvedge restore CLI with --confirm token and CI-exercised restore drill per C-4 + FR-S081-16 watch.
- FR-S082-4 watch M-1 P-3 minimalist warning carry-forward: surface calibration-EF if any L1a refusal fires on legitimate workflow >2x in S083+ per FR-S081-15.
## Validator at close

- tools/validate.sh 17 ok / 0 fail; pytest 294 pass; review-loop converged at iter-2 clean; T-20 admits session-close.
