# Engine-feedback Index

Thin index of operator-mediated engine/methodology feedback records. Full per-record detail lives in `engine-feedback/inbox/EF-*.md` (intake) and `engine-feedback/triage/EF-*.md` (triage).

This file is default-read surface in self-development mode per `specifications/read-contract.md` v4 §1 item 9. See `specifications/workspace-structure.md` v5 §engine-feedback for the full specification.

Created Session 036 per D-116 as the adoption artefact for the engine-feedback pathway. No feedback records present at adoption — the directory is in place for forthcoming external-application feedback return.

## Status summary

- **New** (inbox, not yet triaged): 0
- **Triaged** (triage-record exists, awaiting resolution): 0
- **Resolved** (triage-record + resolution pointer): 0
- **Rejected** (triaged with no action warranted): 0

## Records

| ID | Source workspace | Source session | Target | Severity | Status | Triage session | OI/Disposition |
|----|------------------|----------------|--------|----------|--------|----------------|----------------|
| (none at Session 036 close) | | | | | | | |

## Conventions

- **ID format**: `EF-<source-session-number>-<short-slug>` (e.g., `EF-002-dispatch-steady-state`). ID is stable across inbox/triage lifecycle; triage files cross-reference via `feedback_ref:` frontmatter field.
- **Status lifecycle**: `outbound` (in external workspace) → `inbox` (copied to self-dev workspace) → `triaged` (triage file written) → `resolved | rejected` (disposition recorded).
- **Retention**: intake files preserved verbatim; triage records additive (not overwriting intake).
- **OI promotion**: substantive feedback producing an OI records the OI pointer in the triage file's `opened_issue:` field and in this index's OI/Disposition column.
