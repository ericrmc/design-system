# Open Issues — Index

Active and resolved issues, one-line status summaries. Full per-OI detail lives in `open-issues/OI-NNN.md`; resolved issues in `open-issues/resolved/OI-NNN.md`.

This file is the default-read surface entry point per `specifications/read-contract.md` §1. Per-OI files are default-read when relevant to the current session's work; otherwise they are accessed by explicit reference per `read-contract.md` §6.

## Active issues

| OI | Title | Surfaced | Status |
|----|-------|----------|--------|
| [OI-002](OI-002.md) | Threshold for substantive revision vs. minor correction | Session 001 | Open — heuristic stable; 13th data point Session 028 |
| [OI-004](OI-004.md) | Incorporating genuinely independent perspectives | Session 001 | **Articulated; awaiting closure-retrospective** (state 3/4 per MAD v4); tally 8-of-3; voluntary:required 10:8; criterion-3 cumulative 68 |
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
| [OI-016](OI-016.md) | Domain-validation pathway under user unavailability | Session 013 | **Open — pending kernel §7 revision per §9 trigger 7 firing at Session 032 PD-A REJECT**; counter advanced 1-of-2 → 2-of-2 (Session 018 D2 + Session 032 PD-A); kernel §7 revision deliberation required Session 033 |
| [OI-018](OI-018.md) | Revisit engine-manifest.md §5 bump-trigger criteria | Session 023 | Open — deferred; §5.4 cadence minority activated Session 023 (activated-not-escalated; R9 window aged out Session 026; §5.4 not re-escalated by Session 028 engine-v5 bump per 3-of-4 convergence) |

Active count: **13** (OI-016 is hybrid-state: in the resolved table and carrying active triggers; kept in active list for operational reachability).

## Resolved issues

| OI | Title | Resolved | Session |
|----|-------|----------|---------|
| [OI-001](resolved/OI-001.md) | Naming the methodology (Selvedge) | 2026-04-20 | 012 |
| [OI-003](resolved/OI-003.md) | Automated validation | 2026-04-17 | 002 |
| [OI-010](resolved/OI-010.md) | Cross-model or human participation mechanism | 2026-04-18 | 005 |
| [OI-017](resolved/OI-017.md) | Engine-vs-methodology reframing | 2026-04-22 | 017 |

## Conventions

- **Issue numbering** is strictly append-only: OI-001 was first, OI-002 second, etc. Numbers are never reused.
- **Status** values in per-OI files are canonical; this index's Status column is a one-line summary that may abbreviate.
- **Resolution** does not delete the issue; it moves the file to `resolved/` with frontmatter `status: resolved` and fills `resolved-in-session` + `resolved-on`.
- **Re-opening** is permitted if a resolved issue's resolution turns out to have been premature or conditional (see OI-016 for an example of the hybrid "resolved-provisional" state).

## Pre-Session-022 history

Prior to Session 022, all open issues lived in a single `open-issues.md` file at the workspace root. Session 022 D-084 R8b exercised the `workspace-structure.md` v3 "unless the number of issues makes a single file unwieldy" split-authorisation clause, migrating the single-file content verbatim into this directory structure. Every historical annotation in the pre-Session-022 file is preserved in the corresponding `OI-NNN.md` file; nothing was summarised or compressed.

The pre-migration `open-issues.md` is preserved as an archive-pack witness at `provenance/022-workspace-scaling-trajectory/archive/pre-R8b-open-issues/`.
