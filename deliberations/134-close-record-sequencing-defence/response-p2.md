**Position.** Ship both defences, but treat Defence B as the broadest prevention. The S133 failure was not only “session-close lacked a close-record gate”; it was also “an atom violation surfaced too late and too opaquely for automation.” Keep SQL as the canonical enforcement layer, but add a Python parse-time mirror for atom format with structured errors. Add Defence A as a SQL trigger because close-record presence is cross-row session integrity. Do not add an atomic combined close kind yet; A+B remove the recurrence surface without reducing composability.

**Q1 (Defence A).** Yes. `session-close` should refuse if no `close_record` row exists for the session. The hard gate should live as a SQL trigger on `sessions.status='closed'`, analogous to T-18, T-19, and T-20. A handler preflight may improve the CLI message, but the canonical refusal belongs in SQL because the invariant is cross-row: a closed session must have its close artefact.

**Q2 (Defence B).** Yes, uniformly across all atom-bearing submit kinds. Narrowing to `close-record` fixes the incident but misses the systemic failure class. The CLI should validate atom text during payload deserialisation: 8-240 chars, no newlines, no fenced code, no pipe-table syntax. Errors should be structured, not generic: `E_ATOM_TOO_LONG`, `E_ATOM_TOO_SHORT`, `E_ATOM_NEWLINE`, `E_ATOM_FENCED_CODE`, `E_ATOM_PIPE_TABLE`, with field paths like `items[2]`.

**Q3 (atomic kind).** No for now. A combined `close-record-and-session-close` kind would remove one sequencing surface, but it would also collapse two meaningful operations. The operator may need to inspect or repair the close record before sealing the session. Defence A makes sequencing safe; Defence B makes the common close-record failure legible before a write transaction starts.

**Q4 (enforcement layer).** Both, with different jobs. SQL remains canonical for invariants that must hold regardless of writer: T-27, T-28, T-31 already show that bypass-resistant integrity gates belong in triggers. T-18, T-19, and T-20 show the same close-time pattern. Atom format is different: the SQL `CHECK` is already canonical for storage, but Python should mirror it at parse time for diagnostics and automation. External: I am importing the parse-time / transaction-time validation distinction from broader systems-design practice; treat as hypothesis, not warrant.

**Q5 (operator-side only).** No. A return-code guard in the close script is necessary hygiene, but not sufficient substrate defence. Constraints property 2 says models treat failure as cheap unless friction is structural. Property 5 says lessons do not survive across sessions without structural feedback loops. Leaving this to caller discipline recreates the same class of gap.

**Q6 (smallest shape).** Minimum durable change: add a close-time SQL trigger requiring a close record; add uniform Python atom validation at payload deserialisation; update caller behaviour so scripts stop on structured errors; add focused tests for the trigger and representative atom-bearing submit kinds.

**schema_sketch.**
- Add trigger, likely T-32, on `sessions` close transition.
- Refuse `status='closed'` when no `close_records.session_id = NEW.id`.
- Error code: `E_SESSION_CLOSE_WITHOUT_RECORD`.

**cli_surface.**
- Add `validate_atom(text, field_name) -> None`.
- Raise `AtomValidationError(code, field, detail)`.
- Call during payload deserialisation before handler `write_tx`.
- Return errors such as `E_ATOM_TOO_LONG: items[2] is 289 chars, max 240`.

**migration_path.**
- Land SQL migration and trigger test first.
- Add Python validator mirroring the existing `text_atoms.text` `CHECK`.
- Wire validator across all submit kinds with atom-bearing fields.
- Update close script to halt on non-zero / structured submit failure.

**what_not.**
- Do not create a combined close submit kind in this change.
- Do not weaken SQL `CHECK`.
- Do not solve OI-S133-1 here.
- Do not rely on operator memory as the primary defence.

**open_question.**
- Whether handler-level preflight for Defence A is worth adding purely for better CLI wording, given the SQL trigger will already refuse.

**risk.**
- Python and SQL atom rules can drift unless tests assert parity.
- Uniform validation may expose existing malformed caller payloads abruptly.
- Trigger wording must be precise enough that operators know to submit `close-record` first.

**what_lost.**
- A session can no longer be closed without a canonical close artefact.
- Callers lose the ability to defer atom-format failures to SQL insertion time.
- The engine accepts a small amount of mirrored validation logic in Python.
