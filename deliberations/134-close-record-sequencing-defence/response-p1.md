---
perspective: P-1
family: anthropic
role: atomic-coupling advocate
session: 134
generated_at: 2026-04-30
---

**Position.** The S133 gap is a textbook constraints.md property-5 failure: detection (the 240-char CHECK fired on `items[2]`) without a structural feedback loop into prevention (session-close ran anyway). The load-bearing fix is structural coupling at the SQL layer — a new T-3X trigger that refuses `UPDATE sessions SET status='closed'` whenever no `close_records` row exists for that `session_id`. This closes the surface for every caller — the current Python close script, a future ad-hoc operator command, a yet-unwritten handler — without relying on anyone to remember a return-code check. Defence B (atom-length pre-check in the Python CLI) is worth shipping as friction-reducing ergonomics, but it is *additive*, not substitutive: pre-checking atom length addresses one class of close-record refusal, while T-3X addresses the entire structural sequencing surface (handler bugs, transient SQL errors, partial-application failures, future kinds we have not imagined). Ship both. T-3X is primary; Defence B is secondary. No atomic combined kind.

**Q1 (Defence A).** Yes, and the gate lives at the SQL trigger layer as T-3X on the `sessions` table, firing on `UPDATE OF status` when `NEW.status='closed'`. Refusal raises `E_SESSION_CLOSE_WITHOUT_CLOSE_RECORD`. Putting the gate in the Python handler `_submit_session_close` is insufficient on its own — a direct SQLite write, a future alternate handler, or a maintenance script bypasses it. The trigger is the canonical, hard-to-bypass enforcement point. A handler-level pre-check that surfaces the same refusal before transaction-open is fine as a UX layer, but it is not the warrant — the trigger is.

**Q2 (Defence B).** Yes, ship it, scoped uniformly across all atom-bearing submit kinds (not narrowed to close-record). Validating atom length, newline-absence, no-fenced-code, no-pipe-table at payload deserialisation produces structured `E_ATOM_LENGTH`, `E_ATOM_NEWLINE`, `E_ATOM_FENCED_CODE`, `E_ATOM_PIPE_TABLE` errors *before* `write_tx` opens. This avoids partial-atom-creation rollbacks and gives the operator a clear, parse-time error rather than a mid-transaction CHECK failure. Structured codes, not generic `ValueError` — the engine's pattern is named errors.

**Q3 (atomic kind).** No. A combined `close-record-and-session-close` kind would add CLI surface, a new handler, and migration cost without adding enforcement that T-3X does not already provide. Worse, it would erode the substrate's grammar — close-record and session-close are conceptually distinct artefacts (one is a content row, one is a state transition) and merging them into a single submit muddies that distinction. With T-3X in place, keeping them separate preserves flexibility (e.g. amending a close_record before closing, multiple close_records if the schema later permits) at zero structural-safety cost.

**Q4 (enforcement layer).** SQL trigger for the structural gate (T-3X); Python handler for the atom pre-check. Precedent is unambiguous: T-18, T-19, T-20 enforce close-time integrity at the trigger layer; T-27, T-28, T-31 enforce decision/effect integrity at the trigger layer. The engine has consistently chosen triggers for cross-row gates. Atom-shape validation, by contrast, is a payload-parsing concern — it is appropriate at the Python layer because it is about *how* a request is shaped, not about *what* state the substrate may end up in. The CHECK on `text_atoms.text` remains as the canonical enforcement; the Python pre-check is an early-failure UX layer above it.

**Q5 (operator-side only).** No. Property 2 says friction at points where the agent's defaults are wrong must be structural, not exhortative. Property 5 says prevention must be structural — pre-commit gates, derived counters, integrity-checked references — not reliance on the agent remembering. A return-code-checked close script is exhortative: it works only as long as every caller remembers to write the check. T-3X is structural: the substrate refuses, regardless of caller. Operator-side-only is precisely the failure mode constraints.md was written to forbid.

**Q6 (smallest shape).** One migration adding T-3X, plus a Python pre-check function called by all atom-bearing handlers. That is the minimum that prevents recurrence without re-creating the accretion pathway. Engine bump v40 to v41.

**schema_sketch.**
- `state/migrations/027-close-record-required-at-close.sql`: `CREATE TRIGGER t31_close_requires_close_record BEFORE UPDATE OF status ON sessions WHEN NEW.status='closed' AND OLD.status<>'closed' BEGIN SELECT RAISE(ABORT, 'E_SESSION_CLOSE_WITHOUT_CLOSE_RECORD') WHERE NOT EXISTS (SELECT 1 FROM close_records WHERE session_id = NEW.session_id); END;`
- (Trigger number is illustrative; pick the next free t-NN.)

**cli_surface.**
- No new CLI verbs. `bin/selvedge submit session-close` gains a refusal path surfacing `E_SESSION_CLOSE_WITHOUT_CLOSE_RECORD`.
- All atom-bearing `bin/selvedge submit <kind>` calls gain pre-deserialisation validation surfacing `E_ATOM_LENGTH` / `E_ATOM_NEWLINE` / `E_ATOM_FENCED_CODE` / `E_ATOM_PIPE_TABLE` before `write_tx`.

**migration_path.**
- One forward-only SQL migration adding T-3X.
- Python handler module gains `_validate_atoms(items: list[str]) -> None` called at the top of every atom-bearing `_submit_*` handler.
- engine-manifest bumps v40 to v41; manifest enumerates new migration and pre-check.
- No data backfill required (S133's missing close_record is reconstructable from EFs and DV-S133-1; that recovery is operator-policy, not in scope here).

**what_not.**
- Atomic combined close-record+session-close kind (rejected per Q3).
- Relaxing `engine_feedback`-requires-open-session — separate coupling concern; do not bundle.
- Resolving OI-S133-1 (review-loop static-vs-runtime gap) — separate deliberation.
- Backfilling S133's missing close_record via substrate workaround — that's operator policy.

**open_question.**
- Should `engine_feedback` grow a bounded "calibration window" admitting one post-close EF? My instinct is no — keep the gate strict, force a fresh session as S134 did — but the brief does not give me enough to commit.
- Should T-3X also fire on `INSERT INTO sessions ... status='closed'` for defence-in-depth, or is the contiguity trigger T-10 enough?

**risk.**
- T-3X could block a legitimate emergency-close path if one ever becomes necessary. Mitigation: there is no such path today; if one is needed, add it deliberately rather than leaving the gate open by default.
- Python pre-check duplicates the SQL CHECK. Mild duplication risk: the two could drift. Mitigation: pre-check derives bounds from a single constants module; the CHECK remains canonical.

**what_lost.**
- The ability to close a session before recording a close_record. This was never a desired capability — its existence is exactly the bug. Loss is purely the loss of the failure mode.
- A small amount of CLI flexibility for ad-hoc maintenance — refusals will fire on hand-written closes that skip close-record. This is the point.
