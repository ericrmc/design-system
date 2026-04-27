---
title: Engine version history (engine-v1 through engine-v15)
status: archive
created: 2026-04-27
captured-by-session: 076
source: specifications/engine-manifest.md (engine-v15 prior to trim)
---

# Engine version history — pre-restart

This file preserves the seventy-five-session run's engine-version history in workspace-visible form. The prior `specifications/engine-manifest.md` (engine-v15) is preserved at `archive/pre-restart/specifications/engine-manifest-v15.md`. Full provenance for each engine-version increment is in `provenance/<NNN-session>/02-decisions.md` of the session named in the table below.

## Versions

| Version | Established | Decision | Class |
|---------|-------------|----------|-------|
| engine-v1 | Session 017 | D-074 | First versioned engine definition |
| engine-v2 | Session 021 | D-082 | Preserved-minority + watchpoint activation |
| engine-v3 | Session 022 | D-084 | First new engine-definition spec added (read-contract.md v1) |
| engine-v4 | Session 023 | D-086 | Preserved-minority activation (read-contract budget recalibration) |
| engine-v5 | Session 028 | D-096 | First content-driven post-cadence-maturation; aggregate budget + close-rotation |
| engine-v6 | Session 033 | D-107 | Preserved-minority activation (kernel §7 sense rename) |
| engine-v7 | Session 036 | D-114 | First operator-surfaced agenda increment (MODE.md + engine-feedback) |
| engine-v8 | Session 048 | D-154 | First operator-directed inbox-record resolution (single-orchestrator) |
| engine-v9 | Session 050 | D-172 | First MAD-adopted new engine-definition spec (retrieval-contract.md v1) |
| engine-v10 | Session 058 | D-200 | Second MAD-adopted new spec (records-contract.md v1; substrate substantive) |
| engine-v11 | Session 063 | D-228 | First two-session-arc adoption; Tier 2.5 (γ) reviewer mechanism activated |
| engine-v12 | Session 064 | D-234 | First-of-record depth-0 preservation; substantive validation-approach v6→v7 |
| engine-v13 | Session 071 | D-265 | (β)-phase substrate-discipline; (ε) hybrid bounded-then-extended |
| engine-v14 | Session 074 | D-291 | Operator-directed; google reviewer-role exclusion; family-distinctness removed |
| engine-v15 | Session 075 | D-298 | (γ-6) phase-3.1 implementation: SCD-3 digest schema + capture-adapter + check 26 |
| engine-v16 | Session 076 | D-1..D-7 | Trim-and-restart: nine specs reduced to four; substrate retired pending redesign |

## What ended at engine-v15

- The closed-enumeration default-read surface (`read-contract.md` v6) reached ~90,000 words across the active engine, half the agent's context window at session-open.
- The substrate tooling (retrieval-contract.md v1 + records-contract.md v1) was operational across sessions 050–075; harness-telemetry digest emitter was activated in session 075.
- The Tier 2.5 (γ) reviewer mechanism had matured across reviewer-prompt-template v1 (S063) → v2 (S064) → v3 (S075) with lock-in-after-n=2 discipline; google provider was permanently excluded from reviewer roles at S074 per operator directive after sustained findings_count=0 pattern.
- The validation-debt ledger held VD-003 (γ-phase-3 substrate-arc gating) in-progress at session 075 close, with review_by_session=S076.
- 60 first-class minorities were preserved engine-wide.

The engine-v16 trim retires the substrate-contract specifications (read, records, retrieval) and the audit-shape elaborations on validation-approach.md, replacing them with `methodology.md`, `constraints.md`, `workspace.md`, and `engine-manifest.md`. The retired material is preserved at `archive/pre-restart/specifications/`. The substrate tools are preserved at `archive/pre-restart/tools/`. The seventy-five-session provenance and engine-feedback record remain in their canonical locations as the empirical base from which `specifications/constraints.md` is drawn.

## Pointer to the empirical record

The findings that drove the trim are documented in:

- `applications/075-selvedge-restart/selvedge-problem-statement.md` — the operator's synthesis of seventy-five sessions of self-development.
- `specifications/constraints.md` — the trimmed engine's distillation of the operator's brief into six properties of LLM agents and the design implications for the successor.
- `provenance/001-genesis/` through `provenance/075-session/` — the full session-by-session record.
- `engine-feedback/INDEX.md` plus `engine-feedback/inbox/` and `engine-feedback/triage/` — operator-mediated observations about the methodology itself across the run.
