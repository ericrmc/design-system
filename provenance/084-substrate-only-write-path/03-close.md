---
session: 084
title: substrate-only-write-path — close
engine_version_at_close: engine-v20
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S084 ships engine-v20 Path A: substrate is the only writable surface for session state and specifications; markdown becomes a generated export.

## Engine version

- engine-v19 to engine-v20 (per S084 D-2).
## What was done

- Migrations 003 and 004 applied; T-15 calibrated marker shipped; 14 new tables added.
- selvedge CLI gains 10 new submit kinds and the export subcommand.
- All three S084 perspectives decomposed into 3 perspective-positions and 126 perspective-claim rows.
- 39 legacy rows (13 decisions, 21 alternatives, 5 perspectives) preserved as legacy_import atoms.
- All six engine-definition documents decomposed into 46 spec_sections and 272 spec_clauses.
- Coding review loop ran on the changeset; 3 critical, 7 high, 2 medium, 1 low findings; all medium-or-higher addressed.
- Both prompts rewritten to require CLI-only writes; no markdown authoring of session phases.
## State at close

- Substrate sessions=5; deliberations=3; perspectives=8; perspective_positions=3; perspective_claims=126; decisions_v2=3; alternatives_v2=5.
- Substrate text_atoms over 200; spec_sections=46; spec_clauses=272; legacy_imports=42; review_findings=14 (all medium-or-higher disposed).
- Migrations: 4 applied (001, 002, 003, 004). validate --precommit passes.
## Open issues

- OI-084-001 deferred: spec_clause_links empty; cross-reference linking pass for queries.
- OI-084-002 deferred: pytest coverage for Path A handlers, calibrated marker, export round-trip.
- OI-084-003 deferred: harden migrate runner with post-apply schema_migrations row existence check.
- OI-084-004 deferred: _submit_spec_version inserts new active before marking prev superseded; T-03 refuses; needs reorder.
## What the next session should address

- Re-run spec decomposition for engine-manifest v20 (was v19 at decomposition time).
- Build minimal pytest coverage for Path A handlers and export determinism.
- Cadence-read for human reviewer-subtractor: now five sessions hot since S080.
## Validator at close

- tools/validate.sh reports 17 ok / 0 fail at this commit.
