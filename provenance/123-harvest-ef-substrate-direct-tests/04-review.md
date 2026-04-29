---
session: 123
title: harvest-ef-substrate-direct-tests — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **critical**: Reviewer claimed harvested_engine_feedback count assertions in test_harvest_ef_dry_run_lists_unharvested_rows would silently fail under cross-test pollution.
  - **adjudicated.** False positive: clean_substrate is function-scoped (conftest.py), so the self-dev substrate is reset before every test and harvested_engine_feedback is empty at assertion time. No cross-test pollution is possible.
- **high**: Peer schema variance branches in _me_read_peer_ef (objects.alias, objects.citable_alias, neither) lack test coverage; only the alias-present path is exercised.
  - **adjudicated.** Out of scope for OI-S121-1, which named the substrate-direct semantic rewrite (S110), not the protective schema-variance branches that pre-date it. Tracked under follow-up OI-S123-1.
- **high**: Peer-error paths E_PEER_BUSY, E_PEER_OPEN_FAILED, and E_PEER_SCHEMA_UNSUPPORTED in _me_read_peer_ef have zero test coverage.
  - **adjudicated.** Out of scope for OI-S121-1; defensive peer-error paths are not what the issue was opened to cover. Tracked under OI-S123-1.
- **high**: Concurrent-harvest race recovery (E_REFUSAL_UNIQUE branch in _me_harvest_ef catching duplicate harvested_engine_feedback inserts) is untested.
  - **adjudicated.** Out of scope for OI-S121-1; concurrent-harvest race recovery is not the substrate-direct semantic shift the issue named. Tracked under OI-S123-1.
- **medium**: Duplicate of critical finding: ledger count assertions assumed unfiltered queries could see prior-test rows.
  - **adjudicated.** Duplicate of finding 137 above; same false-positive reasoning applies (clean_substrate is function-scoped).
- **medium**: Hardcoded engine-v34 string in _seed_peer_ef close-record items may drift from current engine version.
  - **adjudicated.** Cosmetic; matches the same hardcoded-version pattern in the existing peer_workspace fixture (engine-v31 string). Close-record item text is not parsed by any handler, so drift carries no behavior risk.

## Terminal passes

- **iteration 1** — findings @ `7f02a9e`
  - Iter-1 reviewer surfaced 1 critical and 3 high findings; all adjudicated as false-positive or out-of-scope and tracked under follow-up OI-S123-1.
- **iteration 2** — clean @ `7f02a9e`
  - Iter-2 clean after adjudicating iter-1 findings and adding _harvest_ef docstring; full pytest suite (178 passed) and tools/validate.sh both green.
