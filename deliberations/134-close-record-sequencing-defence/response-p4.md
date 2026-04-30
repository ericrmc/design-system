---
perspective: P-4
family: anthropic
role: enforcement-layer specialist
session: 134
---

**Position.** The S133 gap is not one bug but two enforcement-layer mismatches. Cross-row coupling (close_record-required-at-close) is an *invariant* and belongs in SQL as T-3X, matching the established pattern of T-18/19/20/27/28/31. Atom-format validation already lives in SQL as a column CHECK; the missing piece is a *parse-time mirror* in the Python CLI for ergonomics — earlier diagnostics, structured error codes, no half-built transactions. These are different layers because they do different jobs. Conflating them into a single combined-kind submit (Defence γ in my stance) smuggles invariant-work into a CLI verb, reduces composability, and creates a third kind that future handlers will have to special-case. Layer coherence is the principle: trigger for invariants, handler for ergonomics, prompt for direction-setting.

**Q1 (Defence A).** Yes — session-close must refuse if no `close_records` row references the session. The gate lives in SQL as T-3X, on `UPDATE OF status ON sessions WHEN NEW.status='closed'`, refusing if `(SELECT COUNT(*) FROM close_records WHERE session_id = NEW.session_id) = 0`. Trigger-level, not handler-level, because the analogous gates (T-18/19/20/27/28/31) all live in SQL and the reason is structural: any caller that writes the row must hit the gate, not just `_submit_session_close`. The Python handler may additionally short-circuit with a friendlier error before issuing the UPDATE, but that is ergonomic; the warrant is the trigger.

**Q2 (Defence B).** Yes — uniform across all atom-bearing submit kinds, not narrowed to close-record. The text_atoms CHECK is uniform; the parse-time mirror must be uniform or the layer policy is incoherent. Error shape: structured `E_ATOM_LENGTH`, `E_ATOM_NEWLINE`, `E_ATOM_FENCE`, `E_ATOM_PIPE_TABLE` codes with offset/atom-index, not generic `ValueError`. This makes the contract programmable: a script chaining submits can branch on the code rather than parse a string. Crucially, parse-time validation prevents the partial-atom-creation-then-rollback pattern that bit S133 — the handler never opens a write_tx if the payload is malformed.

**Q3 (atomic kind).** No. An atomic `submit close-and-seal` is more invasive than necessary and violates layer coherence. It removes the sequencing surface by removing the sequence — but the sequence is not the problem; *unguarded* sequencing is. With T-3X the unguarded path refuses, so the sequence becomes safe. A combined kind also costs composability: future close-time work (analytic snapshots, export hooks, derived counters) would have to be jammed into one transaction or split back out. It also adds a third kind that every future handler-level audit must reason about. Reject γ.

**Q4 (enforcement layer).** SQL triggers for cross-row invariants (T-18/19/20/27/28/31 establish the pattern; T-3X extends it). SQL CHECK for column-local invariants (text_atoms.text already does this). Python handlers for parse-time ergonomics, dispatch, and friendly errors that arrive *before* a write_tx opens. Prompt for direction-setting — telling agents *which* kind to submit and *when*, never for enforcement. Each layer earns its keep by what it uniquely provides: triggers are bypass-resistant, handlers offer programmable diagnostics, prompts shape intent. Mixing them — e.g. relying on a Python check to defend an invariant — is exactly the structural-feedback failure constraints.md property 5 names.

**Q5 (operator-side only).** No. A return-code guard in the close script is necessary but not sufficient. Properties 2 and 5 cut against operator-side-only: property 2 says retry is the universal recovery and friction must be structural; property 5 says detection-without-prevention creates a clean-up service. A guarded close script is *exhortation in code form* — the next script-author will forget. The trigger makes forgetting impossible at the SQL layer, regardless of writer.

**Q6 (smallest shape).** Three deltas: (1) migration adding T-3X close_record-required trigger on sessions; (2) `selvedge/cli.py` payload-validation pass running uniform atom-format checks before any handler dispatch, raising `E_ATOM_*` codes; (3) one prompt-development.md sentence pointing at the new contract. No combined kind. No engine_feedback relaxation. No retroactive close_record for S133 — that gap is reconstructable from EF/DV/OI rows already present.

**On engine_feedback-on-closed-session.** Keep strict. The NOT NULL session_id is an invariant of the same family as T-3X — feedback always belongs to a session. The S133 recovery via opening S134 to author the calibration-EF *worked* and gave the calibration its own provenance and deliberation context; that is structural, not friction. Relaxing to allow post-close EFs (or NULL session_id) trades a clean invariant for a recovery convenience the operator does not need. Flag for synthesis: this is a position, not a warrant.

**schema_sketch.**
- migration `027_t3x_close_record_required.sql`: trigger `t3x_close_requires_close_record` on `sessions` BEFORE UPDATE OF status WHEN NEW.status='closed' AND OLD.status='open', RAISE if `(SELECT COUNT(*) FROM close_records WHERE session_id = NEW.session_id) = 0`.
- no schema change to text_atoms; CHECK already in place.
- no schema change to engine_feedback.

**cli_surface.**
- `selvedge/cli.py`: pre-dispatch validator `validate_atoms(payload, kind)` runs uniform 8–240/no-newline/no-fence/no-pipe-table checks; raises `AtomFormatError` with code `E_ATOM_LENGTH|NEWLINE|FENCE|PIPE_TABLE` and `(atom_path, offset, length)` context.
- exit codes: distinct non-zero for atom-format vs. trigger refusal so scripts can branch.
- no new submit kinds.

**migration_path.**
- engine-v41 ships migration 027 + cli.py validator + prompt-development.md sentence.
- update-external-workspace.sh enumerates 027 and the engine-manifest bumps.
- S134 close exercises T-3X live (the close_record for S134 will be the first write under the new gate).

**what_not.**
- no atomic close-and-seal kind.
- no engine_feedback relaxation (post-close EFs, NULL session_id).
- no retroactive close_record for S133.
- no resolution of OI-S133-1 (review-loop iter cap) here.
- no per-kind atom-format narrowing.

**open_question.**
- does T-3X need a paired trigger refusing close_record INSERT for already-closed sessions, or is the existing immutability of closed-session rows enough?
- should `AtomFormatError` distinguish "atom" (typed-atom row) from "free-text field" violations, or is one code-family adequate?

**risk.**
- T-3X firing during legitimate close-record-then-session-close transactions if both run in one write_tx and ordering inside the tx matters — must verify SQLite trigger fires on the post-INSERT state of close_records.
- parse-time validator drift from CHECK if either evolves without the other; mitigate by sourcing both from one regex/length constant table.
- ergonomic E_ATOM_* codes proliferating beyond the four listed.

**what_lost.**
- single-call close convenience (must still issue two submits, now safely sequenced).
- ability to recover via post-close EF without opening a fresh session — kept as a structural cost, not a bug.
- a small amount of CLI flexibility: malformed payloads now refuse before write_tx, so handlers cannot use partial-INSERT-then-rollback as a soft-validation path (none currently do).
