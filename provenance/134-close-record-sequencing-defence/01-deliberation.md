---
session: 134
title: close-record-sequencing-defence — deliberation
generated_by: selvedge export
---

# Deliberation

## D-18 — Substrate defences against close-record / session-close sequencing failure

sealed_at: 2026-04-30T00:42:59.066Z

### P-1 (anthropic)

**Position.** Ship T-3X SQL trigger refusing session-close without a close_record as primary structural fix; add Python atom pre-check as additive ergonomics. No combined kind.

**position.**
- Q1: Yes. Defence A gate lives at SQL trigger T-3X on sessions UPDATE OF status raising E_SESSION_CLOSE_WITHOUT_CLOSE_RECORD; handler check is UX, trigger is the warrant.
- Q2: Yes ship Defence B uniformly across all atom-bearing submit kinds with structured E_ATOM_LENGTH/NEWLINE/FENCED_CODE/PIPE_TABLE codes before write_tx opens.
- Q3: No combined kind. T-3X already provides enforcement; merging close-record and session-close erodes substrate grammar without safety gain.
- Q4: SQL trigger for the structural cross-row gate (per T-18/19/20/27/28/31 precedent); Python handler for atom-shape pre-check; CHECK on text remains canonical.
- Q5: No, operator-side-only fails properties 2 and 5; return-code discipline is exhortative; T-3X is structural and refuses regardless of caller.
- Q6: Smallest shape is one migration adding T-3X plus a Python pre-check function called by all atom-bearing handlers; engine bumps v40 to v41.
**schema_sketch.**
- Migration 027-close-record-required-at-close.sql adds trigger t31_close_requires_close_record BEFORE UPDATE OF status on sessions raising when no close_records row exists for session_id.
- Trigger number is illustrative; pick the next free t-NN.
**cli_surface.**
- No new CLI verbs. bin/selvedge submit session-close gains a refusal path surfacing E_SESSION_CLOSE_WITHOUT_CLOSE_RECORD.
- All atom-bearing submit kinds gain pre-deserialisation validation surfacing E_ATOM_LENGTH/E_ATOM_NEWLINE/E_ATOM_FENCED_CODE/E_ATOM_PIPE_TABLE before write_tx.
**migration_path.**
- One forward-only SQL migration adding T-3X.
- Python handler module gains _validate_atoms(items) called at the top of every atom-bearing _submit_ handler.
- engine-manifest bumps v40 to v41; manifest enumerates new migration and pre-check.
- No data backfill required; S133 missing close_record is reconstructable from EFs and DV-S133-1; recovery is operator policy not in scope.
**what_not.**
- Atomic combined close-record+session-close kind (rejected per Q3).
- Relaxing engine_feedback-requires-open-session — separate coupling concern; do not bundle.
- Resolving OI-S133-1 (review-loop static-vs-runtime gap) — separate deliberation.
- Backfilling S133 missing close_record via substrate workaround — operator policy, not in scope.
**open_question.**
- Should engine_feedback grow a bounded calibration window admitting one post-close EF? Instinct no, but brief insufficient to commit.
- Should T-3X also fire on INSERT INTO sessions with status=closed for defence-in-depth, or is contiguity trigger T-10 enough?
**risk.**
- T-3X could block a legitimate emergency-close path. Mitigation: no such path today; add deliberately if needed rather than leaving gate open by default.
- Python pre-check duplicates SQL CHECK risking drift. Mitigation: pre-check derives bounds from a single constants module; CHECK remains canonical.
**what_lost.**
- Ability to close a session before recording a close_record. Never a desired capability; loss is purely the loss of the failure mode.
- A small amount of CLI flexibility for ad-hoc maintenance — refusals fire on hand-written closes that skip close-record. This is the point.

### P-2 (openai)

**Position.** Ship both defences. Defence A as SQL trigger for cross-row session integrity; Defence B as uniform Python parse-time atom validation. No combined close kind yet.

**position.**
- Q1: Yes session-close should refuse without close_record. Hard gate lives as SQL trigger on sessions.status=closed analogous to T-18/19/20; handler preflight only improves CLI message.
- Q2: Yes Defence B uniformly across all atom-bearing submit kinds with structured codes E_ATOM_TOO_LONG/TOO_SHORT/NEWLINE/FENCED_CODE/PIPE_TABLE and field paths.
- Q3: No combined kind for now. Operator may need to inspect/repair close record before sealing; A makes sequencing safe, B makes failures legible pre-write_tx.
- Q4: SQL canonical for cross-writer invariants (T-27/28/31, T-18/19/20); Python mirrors atom format at parse time for diagnostics; CHECK remains canonical for storage.
- Q5: No. Return-code guard is necessary hygiene but insufficient. Properties 2 and 5 demand structural friction; caller discipline recreates the gap class.
- Q6: Add close-time SQL trigger requiring close record; uniform Python atom validation; callers stop on structured errors; tests for trigger and submit kinds.
**schema_sketch.**
- Add trigger likely T-32 on sessions close transition.
- Refuse status=closed when no close_records.session_id matches NEW.id.
- Error code: E_SESSION_CLOSE_WITHOUT_RECORD.
**cli_surface.**
- Add validate_atom(text, field_name) returning None.
- Raise AtomValidationError(code, field, detail).
- Call during payload deserialisation before handler write_tx.
- Return errors such as E_ATOM_TOO_LONG: items[2] is 289 chars, max 240.
**migration_path.**
- Land SQL migration and trigger test first.
- Add Python validator mirroring the existing text_atoms.text CHECK.
- Wire validator across all submit kinds with atom-bearing fields.
- Update close script to halt on non-zero or structured submit failure.
**what_not.**
- Do not create a combined close submit kind in this change.
- Do not weaken SQL CHECK.
- Do not solve OI-S133-1 here.
- Do not rely on operator memory as the primary defence.
**open_question.**
- Whether handler-level preflight for Defence A is worth adding purely for better CLI wording given the SQL trigger will already refuse.
**risk.**
- Python and SQL atom rules can drift unless tests assert parity.
- Uniform validation may expose existing malformed caller payloads abruptly.
- Trigger wording must be precise enough that operators know to submit close-record first.
**what_lost.**
- A session can no longer be closed without a canonical close artefact.
- Callers lose the ability to defer atom-format failures to SQL insertion time.
- The engine accepts a small amount of mirrored validation logic in Python.

### P-3 (anthropic)

**Position.** Neither defence warranted on evidence. Fix close script with set -e, add one-sentence prose addendum to development.md step 9, watch for recurrence. Subtract first; add only with evidence.

**position.**
- Q1: No. Defence A relocates rather than removes operator-discipline; close-record submission failures still need re-submission, exactly what return-code guard already enforces one layer earlier.
- Q2: No. SQL CHECK already canonical; parse-time mirror is ergonomic but not load-bearing. S133 failure was script ignoring return code, not substrate atom rule.
- Q3: No emphatically. Combined submit close-and-seal removes composability, hides close_record from inspection-before-seal, adds CLI verb; error was caller discipline not shape.
- Q4: Not applicable; no new gate ships. If gate ever did, history (T-18/19/20/23/27/28/29/31) argues SQL trigger; decision should follow evidence script-level fix failed.
- Q5: Yes operator-side only plus prose sentence in development.md step 9 naming return-code discipline; set -e in committed script imposes friction structurally.
- Q6: Three artefacts no engine bump: prose addendum to development.md step 9, return-code guard in close script, forward-reference OI-S134-X watch issue.
**schema_sketch.**
- No schema change. No new triggers. No migration. Engine remains v40.
**cli_surface.**
- No new verbs. No handler changes. Existing CHECK constraint and existing handler dispatch unchanged.
**migration_path.**
- Edit prompts/development.md step 9 (single sentence).
- Edit and commit close script under tools/ to guard return codes.
- Open OI-S134-X as watch issue with explicit close criterion (10 sessions clean, or one recurrence triggering escalation).
- No engine-manifest change; no migration file; no version bump.
**what_not.**
- Not adding T-3X (close_record-required-at-close).
- Not adding parse-time atom-length validation.
- Not adding atomic close-and-seal kind.
- Not addressing OI-S133-1 (review-loop gap) — separate scope per section 4.6.
- Not relaxing engine_feedback open-session requirement; prose addendum tells callers to order calibration-EF before session-close.
**open_question.**
- How long is watch for recurrence — 10 sessions, 20, calendar quarter? Brief gives no precedent for watch-window durations.
- Does prompts/development.md step 9 have room for one more sentence without diluting existing instruction density? Cannot resolve without reading file.
- Is there a subtraction-precedent for removing prose from step 9 to make room? Brief does not say.
**risk.**
- Recurrence: prose-and-script fix could fail if future operator bypasses committed script and runs submits manually. Cost: another missing close_record, recoverable, bounded.
- Drift: prose addenda accumulate; in 50 sessions step 9 becomes wall of text. Mitigation: subtraction discipline applies to prose; revisit step 9 size at S144.
- Adversarial-loss: position may be wrong. Engine has chosen SQL triggers for analogous gates (T-27/28/31); minimalist case loses if script-level fix is materially weaker.
**what_lost.**
- Certainty of trigger-level enforcement: future caller bypassing the script will not be caught by the substrate.
- A potentially cleaner error surface (Defence B parse-time message).
- Symmetry with T-18/T-19/T-20 (close-time triggers covering decision/alternative/finding integrity but not close_record presence).
- Engine forgoes what might be the right structural defence in exchange for slack — the bandwidth constraint property 6 names.

### P-4 (anthropic)

**Position.** S133 is two enforcement-layer mismatches: cross-row coupling belongs in SQL as T-3X; atom CHECK already exists, add Python parse-time mirror for ergonomics. Layer coherence is the principle. Reject combined kind.

**position.**
- Q1: Yes session-close must refuse without close_records row. Gate is SQL T-3X on UPDATE OF status when NEW.status=closed; trigger-level matches T-18/19/20/27/28/31 precedent.
- Q2: Yes uniform across all atom-bearing kinds with structured E_ATOM_LENGTH/NEWLINE/FENCE/PIPE_TABLE codes; prevents partial-atom-creation rollback that bit S133.
- Q3: No. Atomic submit close-and-seal violates layer coherence and removes sequence rather than guarding it; T-3X makes unguarded path refuse. Costs composability.
- Q4: SQL triggers for cross-row invariants; SQL CHECK for column-local; Python handlers for parse-time ergonomics; prompt for direction-setting. Each layer earns its keep uniquely.
- Q5: No. Return-code guard is necessary but insufficient — exhortation in code form. Trigger makes forgetting impossible at SQL layer regardless of writer.
- Q6: Three deltas — migration adding T-3X trigger; cli.py uniform pre-dispatch atom-format validator raising E_ATOM_* codes; one development.md sentence pointing at new contract.
**schema_sketch.**
- Migration 027_t3x_close_record_required.sql: trigger t3x_close_requires_close_record on sessions BEFORE UPDATE OF status when NEW.status=closed AND OLD.status=open, RAISE if no close_records row.
- No schema change to text_atoms; CHECK already in place.
- No schema change to engine_feedback.
**cli_surface.**
- selvedge/cli.py adds pre-dispatch validate_atoms(payload, kind) running uniform 8-240/no-newline/no-fence/no-pipe-table checks; raises AtomFormatError with code and context.
- Exit codes: distinct non-zero for atom-format vs trigger refusal so scripts can branch.
- No new submit kinds.
**migration_path.**
- engine-v41 ships migration 027 plus cli.py validator plus prompt-development.md sentence.
- update-external-workspace.sh enumerates 027 and the engine-manifest bumps.
- S134 close exercises T-3X live; the close_record for S134 will be the first write under the new gate.
**what_not.**
- No atomic close-and-seal kind.
- No engine_feedback relaxation (post-close EFs, NULL session_id).
- No retroactive close_record for S133.
- No resolution of OI-S133-1 (review-loop iter cap) here.
- No per-kind atom-format narrowing.
**open_question.**
- Does T-3X need a paired trigger refusing close_record INSERT for already-closed sessions, or is the existing immutability of closed-session rows enough?
- Should AtomFormatError distinguish atom (typed-atom row) from free-text field violations, or is one code-family adequate?
**risk.**
- T-3X firing during legitimate close-record-then-session-close transactions if both run in one write_tx and ordering matters; verify trigger fires on post-INSERT state.
- Parse-time validator drift from CHECK if either evolves without the other; mitigate by sourcing both from one regex/length constant table.
- Ergonomic E_ATOM_* codes proliferating beyond the four listed.
**what_lost.**
- Single-call close convenience (must still issue two submits, now safely sequenced).
- Ability to recover via post-close EF without opening a fresh session — kept as a structural cost, not a bug.
- Small CLI flexibility: malformed payloads now refuse before write_tx, so handlers cannot use partial-INSERT-then-rollback as soft-validation (none currently do).

### Synthesis

# S134 deliberation synthesis — close-record sequencing defence

Four perspectives submitted (P-1 anthropic atomic-coupling, P-2 openai cross-family, P-3 anthropic adversarial-minimalist, P-4 anthropic enforcement-layer-specialist). Synthesizer was not a perspective (orchestrator). Brief was committed before perspectives launched.

## Convergences

**C-1. Ship Defence A as SQL trigger T-3X refusing UPDATE sessions SET status='closed' when no close_records row exists for the session.** Independent convergence across [P-1, Q1], [P-2, Q1], [P-4, Q1]. P-2 is cross-family (openai) and arrived at SQL-trigger placement reasoning from the same evidence as P-1 and P-4 without coordination — this is independent-distribution convergence, not shared-prior agreement. All three cited the existing pattern of T-18/19/20/27/28/31 as the analogous gate-history precedent. The warrant is constraints property 5: detection without structural prevention creates a clean-up service.

**C-2. Ship Defence B as uniform parse-time atom validation in selvedge/cli.py with structured E_ATOM_* error codes (LENGTH, NEWLINE, FENCE/FENCED_CODE, PIPE_TABLE) raised before any handler write_tx opens.** Convergence across [P-1, Q2], [P-2, Q2], [P-4, Q2]. All three argued uniform across all atom-bearing submit kinds (rejecting close-record-only narrowing) and structured codes over generic ValueError. Cross-family convergence. Rationale per [P-1, schema_sketch]: prevents the partial-atom-creation-then-rollback pattern that bit S133.

**C-3. Reject atomic combined close-and-seal submit kind.** Unanimous convergence across all four perspectives [P-1, Q3], [P-2, Q3], [P-3, Q3], [P-4, Q3] — including the adversarial P-3 ("no, emphatically"). Reasoning across the four converged on: combined kind reduces composability, hides close_record from inspection-before-seal, adds CLI surface without adding enforcement that T-3X does not already provide [synth: composing the four reasons].

**C-4. Layer-coherence policy — SQL triggers for cross-row invariants; Python handlers for parse-time ergonomics; prompts for direction-setting.** Convergence across [P-1, Q4], [P-2, Q4], [P-4, Q4]. P-4 named the principle explicitly; P-1 and P-2 instantiated it. P-2 flagged its parse-time-vs-transaction-time framing as external-import-treated-as-hypothesis [P-2, Q4]; the engine's internal trigger-history evidence (§4.4 of brief) provides independent warrant.

## Coverage (raised but not multi-perspective convergence)

**COV-1. Keep engine_feedback NOT NULL session_id strict — operator opens fresh session for post-close calibration-EFs.** Position raised by [P-3, Q6] (prose addendum tells callers to author calibration-EF before session-close) and [P-4, "On engine_feedback-on-closed-session"] (S134's recovery via fresh session worked and gave the calibration its own provenance). [P-1, open_question] flagged this with instinct=keep-strict but did not commit. [P-2] silent. Three perspectives lean keep-strict, none oppose; recorded as coverage rather than convergence because P-2 did not address.

**COV-2. T-3X paired-trigger questions (insertion-side guards).** [P-1, open_question] raises whether T-3X should also fire on `INSERT INTO sessions ... status='closed'` for defence-in-depth; [P-4, open_question] raises whether close_record INSERT for already-closed sessions needs a paired refusal. Both flagged as implementation-time decisions; [synth] resolution: T-22 (sessions_workspace_no_required_ins) and T-10 (sessions_contiguous) plus the immutability triggers around closed sessions cover the insertion-side; T-3X focuses on the close-time UPDATE path, which is the documented entry point. Defer to implementation review.

## Minority

**M-1. Operator-side fix only — neither substrate defence is warranted.** [P-3, Position; Q1; Q5; Q6]. P-3 argues:
- The S133 proximate cause is a one-line script-level gap (unguarded sequencing); a `set -e` close script committed under tools/ is structural in the sense constraints property 5 requires (version-controlled, runs every close, not exhortation in agent memory) [P-3, Q5].
- Defence A relocates rather than removes operator discipline: a session whose close-record submission failed for any reason cannot then be closed until close-record succeeds — which is precisely what return-code-checking accomplishes one layer earlier without schema coupling [P-3, Q1].
- Constraints property 6 warns each accretion consumes the bandwidth needed to see the next deficiency; shipping a trigger plus parse-time validator for one incident with a one-line fix is the recursive trap [P-3, Position].
- P-3 names its own loss-condition: "if the affirmative perspectives can show the script-level fix is materially weaker than a trigger for this specific coupling" [P-3, risk].

**Why M-1 does not prevail [synth]**: the affirmative case meets P-3's loss-condition. (a) Cross-family P-2 independently chose the SQL-trigger placement, weakening the "shared-prior accretion bias" reading P-3 implies. (b) [P-4, Q5] makes the sharper argument that a script-level guard *is* exhortation in code form — the next script-author (human or agent) writing a different close path will not carry the discipline; the trigger does. (c) Constraints property 2's "friction at the points where the agent's defaults are wrong must be structural, not exhortative" applies to *every* caller, not just the current close script [P-1, Q5]. P-3's minority is preserved as-is, not diluted.

## Decision-readiness

The synthesis supports a substantive decision recording C-1 through C-4 as adoptions, COV-1 as the engine_feedback strictness reaffirmation, M-1 as the rejected alternative with its loss-reason cited. Engine bump v40 to v41. Implementation deltas: one migration adding T-3X; selvedge/cli.py atom-validation pass; one prompts/development.md sentence pointing at the new contract; engine-manifest enumeration. No data backfill (S133 close_record gap remains reconstructable via DV-S133-1 + EFs).


### Synthesis points

- **convergence C-1.** Ship Defence A as SQL trigger T-3X refusing session-close UPDATE when no close_records row exists.
- **convergence C-2.** Ship Defence B as uniform parse-time atom validator with structured E_ATOM_* error codes.
- **convergence C-3.** Reject atomic combined close-and-seal submit kind; keep two-step shape.
- **convergence C-4.** Layer-coherence: SQL triggers for cross-row invariants, Python handlers for parse-time ergonomics, prompts for direction.
- **minority M-1.** Operator-side fix only — script-level return-code guard plus prose addendum, no substrate defences.
