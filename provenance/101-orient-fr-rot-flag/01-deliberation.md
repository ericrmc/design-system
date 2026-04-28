---
session: 101
title: orient-fr-rot-flag — deliberation
generated_by: selvedge export
---

# Deliberation

## D-7 — orient --fr-rot design: scope, detection mechanism, and CLI surface

sealed_at: 2026-04-28T01:17:22.407Z

### P-1 (anthropic)

**Position.** Read-only orient annotation built on regex extraction over existing FR text; no schema change, value at orient time only.

**cli_surface.**
- --fr-rot flag toggles inline annotation in the existing Forward references section; default packet byte-identical without the flag.
**schema_sketch.**
- No schema change; _orient_sections gains one regex pass and one parameterized IN(...) query against issues.
**migration_path.**
- No migration; pure read-side change. Historical FRs handled via regex sweep, not backfill.
**what_not.**
- No close_state_item_cites table; no typed-cite payload extension to close-record.
- No bin/selvedge rot subcommand and no forward-reference-disposition --auto mode.
**risk.**
- False positives possible if OI-NNN tokens appear as counter-examples or quoted strings; trust erosion in annotation.
- False negatives if FRs reference issues by paraphrase rather than alias; cleanup-in-seconds degrades to cleanup-in-minutes.
**what_lost.**
- Recovery is cheap: add close_state_item_cites later if regex demonstrably underperforms; irreversible schema move should follow evidence.

### P-2 (openai)

**Position.** Hybrid v1: structured citations on new close-records plus regex fallback for legacy FRs; narrow to issue-resolved/absent only.

**schema_sketch.**
- New close_state_item_cites table with object_type=issue only in v1; submit-time alias resolution refuses misspelled aliases by construction.
**cli_surface.**
- orient --fr-rot emits a separate Rotting forward-references section after the FR queue; default orient stays clean.
**migration_path.**
- Migration adds close_state_item_cites; close-record handler accepts cites array; legacy FRs stay text-only and rely on regex fallback.
**what_not.**
- No inline annotation in the default packet; default orient stays clean.
- No backfill of structured cites from prose; no auto-disposition; no bin/selvedge rot subcommand.
**risk.**
- Schema cost paid even if regex fallback alone would have been adequate; cites table may stay near-empty if operators do not use payload field.
**what_lost.**
- If too narrow, operators miss FRs obsoleted by superseded decisions, inactive specs, old engine versions; under-reporting not false authority.

### P-3 (anthropic)

**Position.** Inline annotation in the default orient packet, no flag, no schema change; rot is a property of every orient render or do not build it.

**cli_surface.**
- Render-time inline annotation in every orient run; no --fr-rot flag, no separate section, no rot subcommand, no --propose mode.
**schema_sketch.**
- No schema change at all; persisting a derivation is the prose-state failure mode in reverse.
**migration_path.**
- No migration; render-only feature touching _orient_sections only.
**what_not.**
- No close_state_item_cites table; no structured-citation submit parameter.
- No --fr-rot flag; opt-in surfacing of cleanup signals is exactly the pattern that produced 30 undisposed FRs in the first place.
**risk.**
- Operators may learn to skim past [cites resolved] markers like CI badges; rot then accumulates invisibly with longer orient packet.
**open_question.**
- Whether the friction is real enough to justify any feature; do-nothing remains a defensible alternative.
**what_lost.**
- If annotation too noisy, recovery is cheap (delete code) but interim distrust of orient packet costs more than never-decorated baseline.

### Synthesis

All three perspectives converged on scope (cited-issue resolved or absent only; no engine-version, spec-version, age, or decision-supersession), on historical handling (leave text-only, no backfill), and on excluding both a separate rot subcommand and auto-disposition modes.

Divergence on detection mechanism: P-1 and P-3 argued for regex-only at orient time, citing constraints.md against persisting derivations and the irreversibility of schema additions; P-2 argued for hybrid (structured cites going forward + regex fallback for legacy) on the grounds that submit-time alias resolution refuses misspelling by construction. The hybrid case is real but pays a permanent submit-path tax for value that arrives only at the next orient.

Divergence on CLI surface: P-1 wants an opt-in --fr-rot flag with inline annotation; P-2 wants an opt-in --fr-rot flag with a separate Rotting section; P-3 argues against any flag, on the grounds that opt-in cleanup tooling produced the 30-FR backlog in the first place — surfacing rot as a property of every orient render is the only way it becomes load-bearing.

P-3's anti-flag framing is the strongest single argument: the friction EF-S100-1 named is recurring (every cleanup session does the mental cross-reference), and an opt-in flag only addresses the sessions in which the operator remembers to use it.

Minority view preserved: P-3 also argued do-nothing is defensible if the friction is small, and warned that annotation noise could erode trust in orient. The chosen design narrows annotation to rotted FRs only (not every cited FR) to mitigate this.

### Synthesis points

- **convergence C-1.** Rot scope is cited-issue resolved or absent only; engine-version, spec-version, age, decision-supersession excluded.
- **convergence C-2.** Historical FRs stay text-only; regex sweep handles them; no backfill of structured citations from prose.
- **convergence C-3.** No bin/selvedge rot subcommand and no auto-disposition; FR disposal stays an explicit operator submit.
- **divergence D-1.** Detection mechanism splits: P-1/P-3 regex-only no schema, P-2 hybrid with new close_state_item_cites table for going-forward.
- **divergence D-2.** CLI surface splits: P-1 opt-in flag inline, P-2 opt-in flag separate section, P-3 always-on inline no flag.
- **minority M-1.** P-3 holds do-nothing defensible if friction small; warns annotation noise could erode trust in orient packet.
