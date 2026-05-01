---
session: 158
title: ef-s157-1-alias-resolution-friction — deliberation
generated_by: selvedge export
---

# Deliberation

## D-22 — EF-S157-1 alias-resolution split surface remedy: spec-callout vs widen-resolver vs schema-widening

sealed_at: 2026-05-01T20:45:34.512Z

### P-1 (anthropic)

**Position.** Ship B but generalize the diagnostic to a basis-vs-cite-kind matrix; reject C for S158 since OI-086-003 recurrence pressure is bounded and decreasing.

**schema_sketch.**
- No schema change.
**cli_surface.**
- E_REFUSAL_T01 still fires, but detail includes alias-kind (issue/forward-reference/unknown) plus a basis-specific hint guiding the operator to the right cite.
- Optional dry-run lint surface unchanged; same diagnostic message reproduces under --dry-run.
**migration_path.**
- No migration. Code change in selvedge/aliases.py _resolve_alias_to_object_id plus optional basis-aware wrapper invoked from decision_v2.py support/rejection paths.
**what_not.**
- Reject A alone: leaves the operator-facing diagnostic mute on the structural reason, perpetuating the same slip.
- Reject C now: schema split would force migration, basis-enum debate, export/anchor traversal updates, and test burden disproportionate to current recurrence.
- Reject narrow B (OI/FR-only literal-prefix detection): solves the present incident but ignores the more general failure mode of basis-cite kind mismatch.
- Reject basis=issue: issues are records of gaps, not warrant classes; the EF that surfaced the issue or the DV that opened it carries the warrant.
**open_question.**
- Should the diagnostic also fire when cite resolves to an object whose object_kind mismatches the basis (e.g. basis=engine_feedback, cite=DV-...)?
- Where does the basis-vs-object_kind matrix live: hardcoded in handler, or as a small lookup table seeded by migration?
**risk.**
- Diagnostic-message logic accumulates; if matrix lives in code it is not substrate-introspectable.
- Operators may rely on the message instead of internalising the typing, blunting the prompt-development section 5 callout.
- Detection by literal alias-prefix is fragile if alias formats evolve; T-22 catches drift but regex detection deserves a unit test.
**what_lost.**
- First-class issue and forward-reference citation on supports/rejections is forgone for now; provenance from decision-record back to issue is via claim-text only, not via FK; object-edge query traversal remains incomplete.

### P-2 (openai)

**Position.** Ship B: spec callout plus clearer handler error; minimum sufficient remedy. A leaves a false diagnostic; C treats one S157 slip as a schema mandate.

**schema_sketch.**
- No schema change.
**cli_surface.**
- Submit still refuses with E_REFUSAL_T01, but cite: OI-S156-1 says it is an issue alias, not an object alias.
- FR-... gets the same non-object guidance; it must not pretend cited_object_id can store a forward-reference.
- Query surface stays unchanged: support and rejection cites join only through objects.
**migration_path.**
- No migration; patch prompt-development section 5 plus a narrow handler diagnostic branch and focused tests.
- Migration 021 already records why issue refs cannot populate cited_object_id; S158 should not reopen that as DDL.
**what_not.**
- Reject A alone: it preserves the misleading story that a registered issues.alias is simply unresolved.
- Reject C for S158: resolver widening alone fails the FK, and real widening drags export, anchor traversal, checks, and tests.
- Reject basis=issue: an issue is not a warrant class; cite the surfacing EF/DV object or fold the OI into the claim.
**open_question.**
- Should the diagnostic recommend citing EF-S157-1, the opening DV, or the disposition DV when several object anchors exist?
- Should FR detection query close-state tables, or classify only by FR-... shape to avoid new coupling?
**risk.**
- Operators may keep issue references in claim text, so issue-to-support provenance remains invisible to object-edge queries.
- Alias-format drift can stale the diagnostic unless tests cover legacy OI-NNN and session-form OI-SNNN-N.
- OI-086-003 remains open, so a future recurrence cluster may force a broader schema change later.
**what_lost.**
- No first-class support/rejection cite to issues or FRs; object-only citation topology remains intact but incomplete.
- We forgo the decision_effects.target_issue_id precedent even though it proves split FKs can work when pressure is real.

### Synthesis

P-1 (anthropic) and P-2 (openai-codex) converge on path B: spec-callout in prompt-development §5 plus clearer handler diagnostic. Both reject A alone (preserves a misleading "unresolved alias" message that hides the structural reason) and reject C for S158 (OI-086-003 has been open since S086 with bounded-residual recurrence — 24 OI-mentioning + 9 FR-mentioning NULL-cite supports per substrate count from migration 021 — none of which has forced structural action yet). Both reject `basis='issue'` (issues are records of gaps not warrant classes; cite the surfacing EF or opening DV instead).

Convergence covers: no schema change; no migration; spec callout in §5 to encode the operator-facing typing rule; diagnostic improvement in `_resolve_alias_to_object_id` to detect issue-shape (`OI-...`) and forward-reference-shape (`FR-...`) aliases and emit a guidance message; tests covering legacy `OI-NNN` and session-form `OI-SNNN-N` alias shapes.

Divergence on diagnostic scope: P-1 argues for a basis↔cite kind matrix detection (catches more general failure modes like basis=engine_feedback+cite=DV-... mismatches); P-2 argues for a narrower OI/FR-shape branch with a basis-conditional hint. The narrower form is the minimum sufficient remedy; the broader form risks accumulating diagnostic logic in code without substrate introspectability. Synthesis: ship the narrower P-2 form (OI/FR shape detection with basis-aware hint message) and defer the broader basis↔cite-kind matrix as a forward-reference if the recurrence pattern shifts.

Both perspectives flag the same residual risk: object-edge query traversal from decision-record to issue/FR remains incomplete (provenance via claim-text only). Both keep OI-086-003 explicitly open as the placeholder for structural fix when recurrence pressure forces it.

Open question (P-1): should diagnostic also fire on basis-cite kind mismatch even when the cited alias resolves? Deferred — out of scope for S158 narrow remedy.

Open question (P-2): which object anchor to recommend (surfacing EF, opening DV, disposition DV)? Synthesis: recommend the surfacing EF first (it carries the original observation), with fallback "or fold the alias into claim text" so operators not over-prescribed.


### Synthesis points

- **convergence C-1.** Path B: prompt-development §5 callout + handler diagnostic detecting OI-/FR- shape with basis-aware hint; no schema change.
- **convergence C-2.** Reject C now; OI-086-003 stays open as placeholder for structural fix when recurrence pressure forces it.
- **divergence C-3.** Diagnostic scope: P-1 broader basis↔cite kind matrix vs P-2 narrower OI/FR shape branch; synthesis ships narrower, defers broader.
