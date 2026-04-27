# Open Issues — Index

Active and resolved issues, one-line status summaries. Full per-OI detail lives in `open-issues/OI-NNN.md`; resolved issues in `open-issues/resolved/OI-NNN.md`.

This file is the default-read surface entry point per `specifications/read-contract.md` §1. Per-OI files are default-read when relevant to the current session's work; otherwise they are accessed by explicit reference per `read-contract.md` §6.

## Active issues

| OI | Title | Surfaced | Status |
|----|-------|----------|--------|
| [OI-002](OI-002.md) | Threshold for substantive revision vs. minor correction | Session 001 | Open — heuristic stable; 16th data point Session 041 |
| [OI-005](OI-005.md) | Sub-activities and work-type variants | Session 001 | Unblocked; W1 addressed Session 011; W4 addressed Session 009 |
| [OI-006](OI-006.md) | Cross-references between specifications | Session 001 | Open — deferred until need arises |
| [OI-007](OI-007.md) | Scaling the open issues format | Session 001 | Open — count 13; directory split adopted Session 022 per D-084 R8b |
| [OI-008](OI-008.md) | Persisting validation reports | Session 002 | Open — deferred |
| [OI-009](OI-009.md) | Monitor for drift-to-ritual in multi-agent deliberation | Session 003 | Monitor — G/O/K/S criterion-package operational |
| [OI-011](OI-011.md) | Intra-family model mixing as a deliberation-quality lever | Session 004 | Open |
| [OI-012](OI-012.md) | `validate.sh` hard-coded `02-decisions.md` path | Session 009 | Open — deferred; no active collision pressure |
| [OI-013](OI-013.md) | Non-file external artefacts | Session 009 | Open — monitor; no activation trigger fired |
| [OI-014](OI-014.md) | Domain-actor receipt shape variance | Session 009 | Open — monitor; interdependent with OI-016 |
| [OI-015](OI-015.md) | Laundering enforcement gap in domain reading | Session 011 | Open — Session 024 is positive exercise (6th) |
| [OI-016](OI-016.md) | Domain-validation pathway under user unavailability | Session 013 | **Resolved — provisionally-v2** (Session 033 per D-106/D-107/D-108; kernel v5→v6 + reference-validation v2→v3 substantive; engine-v5→v6; re-opens on (a) §9 trigger 7 re-fire at n=3 / (b) label-discipline violation / (c) scope-reversal); counter at 2-of-3 (Session 018 + 032) |
| [OI-018](OI-018.md) | Revisit engine-manifest.md §5 bump-trigger criteria | Session 023 | Open — deferred; §5.4 cadence minority activated Session 023 (activated-not-escalated; R9 window aged out Session 026; §5.4 not re-escalated by Session 028 engine-v5 bump per 3-of-4 convergence) |
| [OI-019](OI-019.md) | Path-selection work-channel and warrant-surface diversity | Session 043 | Open — five-perspective cross-family deliberation at S043 Path PSD produced 4-of-5 convergence that something forward should change but no 3-of-5 convergence on specific mechanism; seed perspectives at provenance/043-session-assessment/ |
| [OI-079-001](OI-079-001.md) | Table-budget calibration: 17 vs 078 D-10's ≤16 | Session 079 (backfilled S081) | **Resolved S081 D-1** (ratify 17 via existing breach clause; manifest enumeration aligned 15→17); minority forward as OI-081-001 |
| [OI-081-001](OI-081-001.md) | Replace table-count budget with derived-only check? | Session 081 | Open — LOW (post-gate); blocked on 078 D-5 release gate; carries P-2-adversarial minority from S081 deliberation |
| [OI-083-001](OI-083-001-coding-review-substrate-enforcement.md) | Substrate enforcement of the coding review loop | Session 083 | Open — MEDIUM; mechanism is operator-policed at v19; substrate gate deferred to future session |
| [OI-083-002](OI-083-002-coding-review-severity-taxonomy.md) | Worked rubric for the coding review loop's severity taxonomy | Session 083 | Open — LOW; needs 2–3 real code-producing sessions of empirical signal first |
| [OI-085-002](OI-085-002-structural-markdown-restriction.md) | Structural restriction of markdown authoring (substrate-canonical paths) | Session 085 | Open — HIGH; harness-hook fix; F6 and F7 of S086 audit fold into precondition #2 |
| [OI-086-001](OI-086-001-spec-clause-source-decision-not-null.md) | spec_clause source_decision_v2_id traceability is unenforced and unused | Session 086 | Open — MEDIUM; covers F2 + F3 of S086 audit; deferred under DV-S086-1 |
| [OI-086-002](OI-086-002-single-active-spec-version-per-spec-id.md) | Single-active spec_version per spec_id is orchestrator-only, not schema-enforced | Session 086 | Open — MEDIUM; covers F4 of S086 audit; deferred under DV-S086-1 |
| [OI-086-003](OI-086-003-cited-object-id-not-null-on-cite-required-bases.md) | cited_object_id NOT NULL on cite-requiring decision_supports / alternative_rejections bases | Session 086 | Open — MEDIUM; covers F5 of S086 audit; deferred under DV-S086-1 |
| [OI-086-004](OI-086-004-legacy-imports-decomposition-status-semantics.md) | legacy_imports.decomposition_status does not reflect actual decomposition coverage | Session 086 | Open — MEDIUM; covers F8 of S086 audit; deferred under DV-S086-1 |

Active count: **21** (OI-016 is hybrid-state: in the resolved table and carrying active triggers; kept in active list for operational reachability; OI-079-001 also hybrid — resolved-table entry below, kept active here for the OI-081-001 follow-up linkage). OI-080-001 closed at S082; moved to resolved. S085 surfaced OI-085-001 + OI-085-002; S086 surfaced OI-086-001..004 from the substrate-invariant audit. OI-085-001 resolved at S087 (engine-v21 ships migration 008 + redecomposition).

## Resolved issues

| OI | Title | Resolved | Session |
|----|-------|----------|---------|
| [OI-001](resolved/OI-001.md) | Naming the methodology (Selvedge) | 2026-04-20 | 012 |
| [OI-003](resolved/OI-003.md) | Automated validation | 2026-04-17 | 002 |
| [OI-004](resolved/OI-004.md) | Incorporating genuinely independent perspectives | 2026-04-24 | 041 |
| [OI-010](resolved/OI-010.md) | Cross-model or human participation mechanism | 2026-04-18 | 005 |
| [OI-017](resolved/OI-017.md) | Engine-vs-methodology reframing | 2026-04-22 | 017 |
| [OI-079-001](OI-079-001.md) | Table-budget calibration: 17 vs 078 D-10's ≤16 | 2026-04-27 | 081 (file kept in active dir for OI-081-001 linkage) |
| [OI-080-001](resolved/OI-080-001.md) | T-06 missing on `deliberations` UPDATE; T-13 admits sealed_at re-timing | 2026-04-27 | 082 (migration 002 + selvedge migrate runner shipped; xfails flipped) |
| [OI-085-001](resolved/OI-085-001.md) | Re-decompose prompt-development v2 + prompt-application v2 + engine-manifest v20 into spec_clauses | 2026-04-27 | 087 (migration 008 widens T-06; three v2 rows flipped to body_canonical_in_substrate=1; engine v20→v21) |

## Conventions

- **Issue numbering** is strictly append-only: OI-001 was first, OI-002 second, etc. Numbers are never reused.
- **Status** values in per-OI files are canonical; this index's Status column is a one-line summary that may abbreviate.
- **Resolution** does not delete the issue; it moves the file to `resolved/` with frontmatter `status: resolved` and fills `resolved-in-session` + `resolved-on`.
- **Re-opening** is permitted if a resolved issue's resolution turns out to have been premature or conditional (see OI-016 for an example of the hybrid "resolved-provisional" state).

## Pre-Session-022 history

Prior to Session 022, all open issues lived in a single `open-issues.md` file at the workspace root. Session 022 D-084 R8b exercised the `workspace-structure.md` v3 "unless the number of issues makes a single file unwieldy" split-authorisation clause, migrating the single-file content verbatim into this directory structure. Every historical annotation in the pre-Session-022 file is preserved in the corresponding `OI-NNN.md` file; nothing was summarised or compressed.

The pre-migration `open-issues.md` is preserved as an archive-pack witness at `provenance/022-workspace-scaling-trajectory/archive/pre-R8b-open-issues/`.
