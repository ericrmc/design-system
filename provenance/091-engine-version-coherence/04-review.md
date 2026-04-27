---
session: 091
title: engine-version-coherence — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **medium**: Handler does not assert rowcount==1 after metadata UPDATE; would silently no-op if the metadata row is absent, reproducing the silent-drift bug. T-20 loop on engine-version coherence.
  - **fixed.** Captured cursor; raise E_VALIDATION when rowcount != 1; error message names invariant + likely cause.
- **medium**: Migration 011 backfill encodes engine-v24 as snapshot, not derived from spec_versions; comment misleading on replay semantics. T-20 loop on engine-version coherence.
  - **adjudicated.** Migration runner apply-once enforces no-replay; structural handler propagation is load-bearing. Filed OI-S091-1 (LOW) for future re-snapshot or derive-from-spec_versions refactor.
