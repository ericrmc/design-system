# Engine-feedback Index

Thin index of operator-mediated engine/methodology feedback records. Full per-record detail lives in `engine-feedback/inbox/EF-*.md` (intake) and `engine-feedback/triage/EF-*.md` (triage).

This file is default-read surface in self-development mode per `specifications/read-contract.md` v4 §1 item 9. See `specifications/workspace-structure.md` v5 §engine-feedback for the full specification.

Created Session 036 per D-116 as the adoption artefact for the engine-feedback pathway. No feedback records present at adoption — the directory is in place for forthcoming external-application feedback return.

## Status summary

- **New** (inbox, not yet triaged): 3
- **Triaged** (triage-record exists, awaiting resolution): 0
- **Resolved** (triage-record + resolution pointer): 0
- **Rejected** (triaged with no action warranted): 0

## Records

| ID | Source workspace | Source session | Target | Severity | Status | Triage session | OI/Disposition |
|----|------------------|----------------|--------|----------|--------|----------------|----------------|
| [EF-047-brief-slot-template-hidden-arc-leakage](inbox/EF-047-brief-slot-template-hidden-arc-leakage.md) | selvedge-self-development | 047 | engine | friction | new (direct-to-inbox; out-of-session) | — | — |
| [EF-047-session-input-files-redundant-with-verbatim-capture](inbox/EF-047-session-input-files-redundant-with-verbatim-capture.md) | selvedge-self-development | 047 | methodology | observation | new (direct-to-inbox; out-of-session) | — | — |
| [EF-001-read-contract-budget-scaling-for-domain-artefacts](inbox/EF-001-read-contract-budget-scaling-for-domain-artefacts.md) | selvedge-disaster-response | 001 | engine | friction | new (direct-to-inbox; operator-relay) | — | — |

**Note on direct-to-inbox placement**: both records above originated in self-dev post-S047 out-of-session discussion, not from external-application execution. Operator directed direct placement in `inbox/` rather than fabricating provenance by routing through the external workspace's `outbox/` (which would contaminate that workspace's execution record). `source_workspace_id` accurately reflects self-dev origin. This is a forward-convention observation candidate: the `engine-feedback/` schema per `workspace-structure.md` v5 §engine-feedback describes the external-workspace→self-dev-inbox direction but does not forbid self-dev-originating records being placed directly in inbox; the practical discipline is accurate attribution via `source_workspace_id` and `reported_by` fields.

## Conventions

- **ID format**: `EF-<source-session-number>-<short-slug>` (e.g., `EF-002-dispatch-steady-state`). ID is stable across inbox/triage lifecycle; triage files cross-reference via `feedback_ref:` frontmatter field.
- **Status lifecycle**: `outbound` (in external workspace) → `inbox` (copied to self-dev workspace) → `triaged` (triage file written) → `resolved | rejected` (disposition recorded).
- **Retention**: intake files preserved verbatim; triage records additive (not overwriting intake).
- **OI promotion**: substantive feedback producing an OI records the OI pointer in the triage file's `opened_issue:` field and in this index's OI/Disposition column.
