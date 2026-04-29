---
session: 128
title: fr-null-state-annotation — deliberation
generated_by: selvedge export
---

# Deliberation

## D-15 — FR null-state noise: refuse, annotate, elide, or discipline-only

sealed_at: 2026-04-29T20:38:55.882Z

### P-1 (anthropic)

**Position.** Annotate null-state FR items at orient render time; no submit-side refusal and no default elision.

**position.**
- Add a null_state boolean per FR item in _orient_sections; render [null-state] alongside [rot: ...]; do not elide; do not refuse at submit.
**schema_sketch.**
- No schema change; substrate row stays unchanged; per-item null_state flag exists only in the rendered orient packet.
- Detection rule: text matches a small phrase pattern (from orient queue, next highest-priority, next FR/OI) AND has no resolvable OI-/FR-/DV-/EF- alias citation.
**cli_surface.**
- No new flag on bin/selvedge orient; markdown shows [null-state] after FR text; --json output gains null_state: bool per FR item.
**migration_path.**
- No migration needed; change is purely render-time in selvedge/orient.py and applies uniformly to existing and future rows.
**what_not.**
- Reject refuse-at-submit: too brittle, false-refusal risk on legitimate generic-but-actionable items lacking aliases.
- Reject elide-by-default: removes audit signal from a surface whose stated purpose is a live read; --show-null-state would only relocate noise.
- Reject discipline-only: that is the current state and demonstrably leaks; section 8.5 already requires disposition yet the queue accumulates advisory items.
**what_lost.**
- Lose a dedicated null-state mechanism (column or status); acceptable given small sample and maintenance cost of schema for a heuristic.
**risk.**
- Pattern drift: phrasing operators use for placeholder items will evolve; mitigate by co-locating the pattern with FR_ISSUE_CITE_RE in paths.py for one-file calibration.
**open_question.**
- Should section 8.5 be tightened to dispose any FR tagged null-state from prior sessions when current session has not addressed it? Likely yes, separate prompt edit.

### P-2 (openai)

**Position.** Refuse null-state next_session_should at submit (option A) plus a one-time B/C cleanup for existing rows.

**position.**
- Null-state next_session_should items must not register as undisposed FRs; if no concrete action, artifact, decision, or cited issue, it is hygiene not a forward reference.
**schema_sketch.**
- Add canonical fr_state field with values open, disposed, rotted, null_state; not just render metadata.
- Add fr_null_reason in no_actionable_referent, selector_placeholder, duplicate_queue_instruction; and fr_registerable bool defaulting true for ordinary items.
- Mixed items split semantically: cited OIs remain actionable FRs; the generic selector phrase is annotated as null or ignored.
**cli_surface.**
- Add selvedge fr lint-null with --apply for cleanup; selvedge close validate enforces registerability at close-time.
- selvedge orient --include-null-state as escape hatch; default render excludes null_state items entirely.
- Submit-time refusal message: close-state item has no actionable referent; record as session note or cite a concrete OI/FR.
**migration_path.**
- Step 1: detect exact and near-exact null-state phrases conservatively. Step 2: mark pure cases like FR-S117-11 as null_state.
- Step 3: for mixed cases preserve cited OIs as actionable and mark only the generic selector clause as null.
- Step 4: re-render orient packets with null-state hidden by default. Step 5: update section 8.5 to require next_session_should name a concrete referent.
**what_not.**
- Reject discipline-only: guidance may reduce future cases but the system already knows enough to prevent the obvious pattern programmatically.
- Reject annotate-only: annotated junk still occupies the queue and pays attention tax unless render policy learns to hide it.
**what_lost.**
- Lose a tiny amount of historical texture; future readers see less closing-session intent. Acceptable since the canonical row remains recoverable.
**risk.**
- Classifier overreach: keep first pass conservative and exact-pattern based to avoid swallowing legitimate items.
- Risk of hiding a weak but real action; mitigate via dry-run review of the lint-null --apply step before bulk migration.
**open_question.**
- Should null_state count as a disposition or non-registration? Prefer non-registration for new items and null_state disposition for legacy rows.
- Mixed FR splitting needs a canonical representation before bulk migration to avoid loss of cited-OI actionability.

### Synthesis

Both perspectives reject discipline-only and converge that null-state next_session_should items pollute the FR queue. They diverge on enforcement strength: P-1 favors render-time annotation only (no schema, no submit refusal, no elision); P-2 favors a canonical fr_state column plus close-record refusal plus default elision plus mixed-item splitting plus a lint CLI. Synthesis takes P-1 as the immediate step (single-file orient.py change, no migration) because (a) the current sample shows one pure null-state case in 22 FRs, too thin to design schema around; (b) substrate enforcement gates should encode invariants, not stylistic preferences; (c) annotation makes the noise actionable at next-close section 8.5 disposition. Preserve P-2's enforcement direction as a minority position: if null-state items recur after annotation lands, reopen with schema column, submit refusal, and mixed-splitting. Open question: tighten prompts/development.md section 8.5 to name null-state disposition explicitly; defer to a separate decision in this session.

### Synthesis points

- **convergence C-1.** Both perspectives reject discipline-only; null-state items must be detected and visibly differentiated from actionable FRs.
- **divergence D-1.** P-1 favors render-time annotation with no schema; P-2 favors substrate column fr_state plus submit refusal plus default elision.
- **minority M-1.** P-2 mixed-item splitting and lint CLI preserved as recurrence-trigger direction; reopen if annotation alone fails.
