# Engine-feedback Index

Thin index of operator-mediated engine/methodology feedback records. Full per-record detail lives in `engine-feedback/inbox/EF-*.md` (intake) and `engine-feedback/triage/EF-*.md` (triage).

This file is default-read surface in self-development mode per `specifications/read-contract.md` v4 §1 item 9. See `specifications/workspace-structure.md` v5 §engine-feedback for the full specification.

Created Session 036 per D-116 as the adoption artefact for the engine-feedback pathway. First non-empty inbox state reached post-Session 047; first full inbox→triage cycle executed at Session 048.

## Status summary

- **New** (inbox, not yet triaged): 1
- **Triaged** (triage-record exists, awaiting resolution): 1
- **Resolved** (triage-record + resolution pointer): 3
- **Rejected** (triaged with no action warranted): 0

## Records

| ID | Source workspace | Source session | Target | Severity | Status | Triage session | OI/Disposition |
|----|------------------|----------------|--------|----------|--------|----------------|----------------|
| [EF-051-aliases-yaml-not-consulted-at-query-time](inbox/EF-051-aliases-yaml-not-consulted-at-query-time.md) | selvedge-self-development | 051 | engine-adjacent | friction | new — S051 substrate smoke-test surfaced `resolve_id()` does not consult `specifications/aliases.yaml` at query time; 0-of-8 seed aliases resolve; contradicts retrieval-contract.md v1 §2.2 | — | awaiting S052+ triage; implementation-level fix candidate (Direction A index-time reverse-remap OR Direction B query-time aliases consultation); minor per OI-002 if impl-only; no engine-v bump unless §2.2 narrowed |
| [EF-047-brief-slot-template-hidden-arc-leakage](inbox/EF-047-brief-slot-template-hidden-arc-leakage.md) ([triage](triage/EF-047-brief-slot-template-hidden-arc-leakage.md)) | selvedge-self-development | 047 | engine | friction | triaged — S050 D-174 defers spec-level adoption to next self-dev or external-arc session exercising arc-plan brief slots (earliest selvedge-disaster-response S002+) | 048 | disposition per S050 D-174: deferral is principled, not punting; S050 MAD surface did not exercise arc-plan-hidden-view leakage pressure |
| [EF-047-session-input-files-redundant-with-verbatim-capture](inbox/EF-047-session-input-files-redundant-with-verbatim-capture.md) ([triage](triage/EF-047-session-input-files-redundant-with-verbatim-capture.md)) | selvedge-self-development | 047 | methodology | observation | **resolved** (S050 D-174 adopted-as-practice) | 048 | practice-level adopted at S050 (session-inputs-as-prior-synthesis-reference is acceptable shape without re-verbatim-capture when cited artefact is in-workspace provenance); minor documentary captured in retrieval-contract.md v1 §5 bootstrap-contract-note |
| [EF-001-read-contract-budget-scaling-for-domain-artefacts](inbox/EF-001-read-contract-budget-scaling-for-domain-artefacts.md) ([triage](triage/EF-001-read-contract-budget-scaling-for-domain-artefacts.md)) | selvedge-disaster-response | 001 | engine | friction | **resolved** (S048 D-153 + D-154) | 048 | adopted via read-contract.md v4→v5 (§1 clarification + §2d carve-out) + minor prompts/application.md §Read clarification + engine-v7→v8; subsumes S047 D-150 (iv) |
| [EF-047-retrieval-discipline-and-text-system-scaling-ceiling](inbox/EF-047-retrieval-discipline-and-text-system-scaling-ceiling.md) ([triage](triage/EF-047-retrieval-discipline-and-text-system-scaling-ceiling.md)) | selvedge-self-development | 047 | methodology | friction | **resolved** (S050 D-164 through D-173 + D-172 engine-v9) | 048/050 | adopted via new engine-definition spec specifications/retrieval-contract.md v1 + engine-adjacent tooling (tools/build_retrieval_index.py + tools/retrieval_server.py + specifications/aliases.yaml + .mcp.json) + bootstrap-script substrate-install step + workspace-structure.md v5→v6 (+5 first-class minorities §10.4-M7 through §10.4-M11) + engine-v8→v9 bump + WX-50-1 phase-2 gate (retrieval-substrate-use recording across S050–S053); OI-019 sub-question (f) cross-referenced but not closed (sub-question is phase-2+ territory) |

**Note on direct-to-inbox placement**: both records above originated in self-dev post-S047 out-of-session discussion, not from external-application execution. Operator directed direct placement in `inbox/` rather than fabricating provenance by routing through the external workspace's `outbox/` (which would contaminate that workspace's execution record). `source_workspace_id` accurately reflects self-dev origin. This is a forward-convention observation candidate: the `engine-feedback/` schema per `workspace-structure.md` v5 §engine-feedback describes the external-workspace→self-dev-inbox direction but does not forbid self-dev-originating records being placed directly in inbox; the practical discipline is accurate attribution via `source_workspace_id` and `reported_by` fields.

## Conventions

- **ID format**: `EF-<source-session-number>-<short-slug>` (e.g., `EF-002-dispatch-steady-state`). ID is stable across inbox/triage lifecycle; triage files cross-reference via `feedback_ref:` frontmatter field.
- **Status lifecycle**: `outbound` (in external workspace) → `inbox` (copied to self-dev workspace) → `triaged` (triage file written) → `resolved | rejected` (disposition recorded).
- **Retention**: intake files preserved verbatim; triage records additive (not overwriting intake).
- **OI promotion**: substantive feedback producing an OI records the OI pointer in the triage file's `opened_issue:` field and in this index's OI/Disposition column.
