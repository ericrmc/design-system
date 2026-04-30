---
perspective: P-3
family: anthropic
role: minimalist adversary
session: 134
---

**Position.** Neither Defence A nor Defence B is warranted on the evidence in this brief. S133's gap has a single, knowable, one-line proximate cause: an unguarded sequence ran two submits without checking the first's return code. The disciplined response is to fix the close script, add one prose sentence to `prompts/development.md` step 9 naming the return-code discipline, and watch for recurrence. Constraints property 5 demands structural prevention — and a version-controlled close script with `set -e` *is* structural; it runs on every close, lives in the repository, and is not exhortation. Constraints property 6 warns that each accretion consumes the bandwidth needed to see the next deficiency. Shipping T-3X plus a parse-time validation layer plus possibly an atomic kind, for one incident with a one-line fix, is exactly the recursive trap the engine has been subtracting against. Subtract first; add only with evidence the prose-and-script fix failed.

**Q1 (Defence A).** No. A close-record-required gate at trigger or handler level relocates the operator-discipline problem rather than removing it: a session whose close-record submission failed for any reason (atom overrun, schema refusal, future CHECK additions) cannot then be closed until the operator re-submits close-record successfully — which is *exactly* what the close-script return-code guard already enforces, one layer earlier and without schema coupling. The argument "a future operator might run submits manually" applies to every CLI invocation in this engine; accepting it as warrant for T-3X accepts it as warrant for indefinitely many future triggers.

**Q2 (Defence B).** No. The CHECK constraint at SQL is already enforcing atom shape, canonically, at the lowest layer. A parse-time mirror is ergonomic — it would surface a clearer error message at submit time rather than mid-transaction — but it is not load-bearing: the rule is enforced; the failure was detected; the close-record refused. What failed in S133 was not the substrate's atom rule; it was the script's response to a refusal it received correctly. Building a second validation layer to make the *first* layer's refusal arrive sooner does not prevent the actual S133 failure mode (ignored return code).

**Q3 (atomic kind).** No, emphatically. A combined `submit close-and-seal` removes composability, hides the close_record from inspection-before-seal, and adds a CLI verb the engine doesn't need. The two-step shape is the right shape; the error was in caller discipline, not in the shape.

**Q4 (enforcement layer).** Not applicable under this position — no new gate ships. If a gate ever does ship, the engine's history (T-18, T-19, T-20, T-23, T-27, T-28, T-29, T-31) argues SQL-trigger placement; but that decision should follow evidence the script-level fix failed.

**Q5 (operator-side only).** Yes — operator-side fix only, plus one prose sentence in `prompts/development.md` step 9 naming the return-code discipline (and noting `engine_feedback` requires an open session, so calibration-EF must precede session-close not follow it). This is the answer constraints property 2 actually points to: friction at the point where the agent's default is wrong. The agent's default was "run two submits sequentially without checking"; `set -e` in a committed script imposes that friction structurally, every run, with zero schema surface.

**Q6 (smallest shape).** Three artefacts, no engine bump:
- One-sentence addendum to `prompts/development.md` step 9: "Before `submit session-close`, verify the prior `submit close-record` returned 0; submit calibration-EF *before* session-close because `engine_feedback` requires an open session."
- Return-code guard in the close script under `tools/` (`set -euo pipefail` if shell, explicit `if r.returncode != 0: sys.exit(1)` if Python), committed alongside the prose change.
- Forward-reference open-issue OI-S134-X: "Watch for recurrence of close-record/session-close sequencing failure across S135–S144. If recurrence, escalate to substrate defence with evidence." Closes when the watch window elapses without recurrence.

**schema_sketch.** No schema change. No new triggers. No migration. Engine remains v40.

**cli_surface.** No new verbs. No handler changes. Existing CHECK constraint and existing handler dispatch unchanged.

**migration_path.**
- Edit `prompts/development.md` step 9 (single sentence).
- Edit/commit close script under `tools/` to guard return codes.
- Open OI-S134-X as a watch issue with explicit close criterion (10 sessions clean, or one recurrence triggering escalation).
- No engine-manifest change; no migration file; no version bump.

**what_not.**
- Not adding T-3X (close_record-required-at-close).
- Not adding parse-time atom-length validation.
- Not adding atomic close-and-seal kind.
- Not addressing OI-S133-1 (review-loop gap) — separate scope per §4.6.
- Not relaxing `engine_feedback` open-session requirement; the prose addendum tells callers to order calibration-EF before session-close.

**open_question.**
- How long is "watch for recurrence" — 10 sessions, 20, calendar quarter? Brief gives no precedent for watch-window durations.
- Does `prompts/development.md` step 9 have room for one more sentence without diluting existing instruction density? (Cannot resolve without reading the file.)
- Is there a subtraction-precedent for *removing* prose from step 9 to make room? Brief does not say.

**risk.**
- Recurrence: the prose-and-script fix could fail if a future operator bypasses the committed script and runs submits manually. Cost of recurrence: another missing close_record, recoverable from provenance the way S133 was. Bounded.
- Drift: prose addenda accumulate; in 50 sessions step 9 becomes a wall of text. Mitigation: subtraction discipline applies to prose too; revisit step 9 size at S144.
- Adversarial-loss: this position may simply be wrong. The brief shows the engine has chosen SQL triggers for analogous gates (T-27, T-28, T-31). The minimalist case loses if the affirmative perspectives can show the script-level fix is materially weaker than a trigger for *this specific* coupling.

**what_lost.**
- The certainty of trigger-level enforcement: a future caller who bypasses the script will not be caught by the substrate.
- A potentially cleaner error surface (Defence B's parse-time message).
- Symmetry with T-18/T-19/T-20 (close-time triggers covering decision/alternative/finding integrity but not close_record presence).
- The engine forgoes what might be the right structural defence in exchange for slack — the bandwidth constraint property 6 names. If the operator judges that slack less valuable than the defence, this position is the one that should lose.
