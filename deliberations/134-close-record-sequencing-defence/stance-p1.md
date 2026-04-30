---
perspective: P-1
family: anthropic
role: atomic-coupling advocate
---

## Role-specific stance — P-1 (Atomic-Coupling Advocate)

You carry the load of arguing that the **primary defence is structural coupling between close-record and session-close**: session-close must refuse if no close_record row exists for the session, full stop. This is the operator's named Defence A, and your job is to build the strongest case for it as the load-bearing fix.

Your concerns:

- The S133 incident is exactly the failure mode constraints.md property 5 describes: detection (CHECK refusal on the over-length atom) without a structural feedback loop into prevention (session-close still ran). The system caught the error, then proceeded as if it hadn't. That is the textbook structural-feedback-loop gap.
- Without Defence A, the close-record contract is enforced only by operator discipline at the close script layer — exactly the "exhortative" enforcement constraints.md property 2 says doesn't work. Even with a return-code-checked close script, a future operator (or agent) running the submits manually can still produce a status='closed' session without a close_record row. Substrate-level enforcement closes the surface.
- The engine's pattern for cross-row integrity (T-18, T-19, T-20, T-27, T-28, T-31) is SQL-level triggers. A new T-3X — "refuse UPDATE sessions SET status='closed' WHERE NOT EXISTS (SELECT 1 FROM close_records WHERE session_id = NEW.session_id)" — fits the existing pattern exactly. No new mechanism, no new layer.
- Defence B (atom pre-check) is *additive*, not substitutive. Pre-checking atom length in Python is good ergonomics, but it does not address the structural sequencing gap. A pre-check that catches the 289-char overrun still leaves room for *other* failure modes between close-record and session-close (handler bugs, transient SQL errors, partial-application failures). Defence A is the load-bearing structural fix; Defence B is a friction-reducing complement.
- The engine_feedback-requires-open-session post-close blocker is a related coupling gap. If your stance permits, name whether engine_feedback should grow a "calibration window" admitting one feedback row after close-time, or whether the right answer is to keep that gate strict (operator must open a fresh session — which is what S134 did).

Argue for Defence A as the primary, structural, must-ship fix. Argue Defence B is worth shipping but secondary. Take a position on Q3 (atomic combined kind): your default instinct should lean *no* — atomic coupling adds CLI surface without adding enforcement that T-3X doesn't already provide. But if you're persuaded otherwise by the brief, say so.

Take a position on Q4 (enforcement layer): default to **SQL trigger** for the structural gate, **Python handler** for the pre-check. Cite the trigger-history precedent.

Be specific about migration shape: a single `state/migrations/02X-close-record-required-at-close.sql` adding T-3X, and a Python-handler addition for atom pre-check. Engine bump: v40 to v41.
