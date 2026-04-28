---
session: 102
title: rename-citable-alias-to-alias — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Rename objects.citable_alias and issues.citable_alias to alias via ALTER TABLE RENAME COLUMN

**Kind:** schema_migration.  **Outcome:** adopt migration `016-rename-citable-alias-to-alias`.

**Why.**

- (operator_directive) Operator named OI-S101-1 the preferred path and authorised the full rename across both tables in one session.
- (constraint) Several read-paths in cli.py already aliased the column to alias (e.g. o.citable_alias AS alias); the storage rename removes that indirection.

**Effects.**

- adds_migration 016-rename-citable-alias-to-alias.sql
- modifies objects.citable_alias renamed to objects.alias
- modifies issues.citable_alias renamed to issues.alias; T-22 trigger reissued
- bumps_engine engine-v29 to engine-v30
- closes_issue OI-S101-1 — OI-S101-1 column rename for query ergonomics

**Rejected alternatives.**

- **R-1.1.** Use the calibrated table-recreation dance (CREATE _new + INSERT + DROP + RENAME) per migrations 003 and 015 to rebuild objects and issues with the renamed column.
  - (breaks_invariant) First attempt failed at COMMIT with FOREIGN KEY constraint failure: dropping objects orphans dozens of referrers (spec_versions, decisions, perspectives, etc.) within the same transaction even though the rename is by-name.
- **R-2.1.** Ship a payload-shim accepting both alias and citable_alias on the four issue handlers to preserve backwards compatibility for any external caller.
  - (redundant_with_existing) This workspace is the only caller; the operator authorised a hard cut, and a shim adds enduring complexity for transient compatibility.
- **R-3.1.** Split the rename across two sessions (objects this session, issues next).
  - (operator_override) Operator directed do it all this session; splitting would leave the substrate inconsistent across a session boundary.
