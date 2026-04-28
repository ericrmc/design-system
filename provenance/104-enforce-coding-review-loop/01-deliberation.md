---
session: 104
title: enforce-coding-review-loop — deliberation
generated_by: selvedge export
---

# Deliberation

## D-8 — shape of substrate enforcement for the coding review loop

sealed_at: 2026-04-28T03:47:22.541Z

### P-1 (anthropic)

**Position.** Operator declares sessions.kind at open and substrate adds review_passes plus a trigger refusing close on a coding session without a terminal clean or halted pass.

**position.**
- The methodology already names the artefact and OI-083-001 is the structural-enforcement gap; substrate must enforce evidence rather than detect coding sessions.
- Operator-declared classification with substrate-enforced evidence is structurally equivalent to slug immutability under T-23, not a weaker form of detection.
- review_passes must be separated from review_findings because findings are per-iteration line items while a pass is the loops terminal outcome of clean or halted.
**schema_sketch.**
- review_passes table holds review_pass_id, session_id, iteration, outcome in clean or halted, outcome_atom_id, recorded_at, and optional object_id.
**cli_surface.**
- Add submit review-pass with a payload taking iteration, outcome of clean or halted, and a one-line summary of the terminal pass.
**schema_sketch.**
- Add a new trigger t26 that aborts close of a coding session unless a review_passes row exists for that session with outcome of clean or halted.
**migration_path.**
- Add kind column with default coding, backfill prior sessions to coding, add review_passes table, add t26 and a kind-immutability trigger mirroring T-23, and bump engine to v31.
**what_not.**
- This is not a way for the substrate to detect operator skipping the reviewer; a falsely declared spec_only kind is an audit concern handled by separate engine-definition close review.
- T-XX is not a replacement for T-20; T-20 catches open findings while T-XX catches the absence of a terminal pass and both apply together.
**open_question.**
- Should sessions.status admit a halted value or is it sufficient to record outcome halted on the review pass row while leaving status closed; lean toward adding halted to status.
**risk.**
- Operator default of coding is correct for self-development sessions but may be wrong for external-problem mode where many sessions are pure spec or methodology work.
- Halted-state encoding in status requires every existing trigger keyed on status closed including t11, t18, t19, and t20 to admit halted to keep their gates active.

### P-2 (openai)

**Position.** Enforce the loop from recorded change facts with a manifest-sealing reviewer pass that ties review to the actual executable behavioral changes, not to operator-declared session intent.

**position.**
- Enforce the loop from recorded change facts not session intent, with a code-change obligation that makes normal close impossible without a current clean reviewer pass or a typed halted record.
**schema_sketch.**
- Add session_artifact_changes recording change_id, session_id, path, operation in create modify delete, artifact_class, behavioral flag, decision_v2_id, and recorded_at.
- A behavioral row with an executable artifact_class creates or implies session_review_obligations with review_kind coding and status required.
- Add review_passes with iteration between 1 and 4, reviewer_agent_run_id, reviewed_through_change_id, result findings or clean, summary_atom_id, and tie review_findings to review_pass_id.
- A current clean pass requires result clean, reviewed_through_change_id equal to MAX change_id of executable behavioral changes, distinct reviewer role, and no open medium-plus findings.
- Add session_halts with unique session_id, halt_kind coding_review_nonconvergence, final_iteration equal to 4, unresolved_summary_atom_id, and a non-null issue_id.
**risk.**
- Operator declares session.kind at open is the wrong anchor because sessions mutate under context pressure and the declaration becomes stale or over-broad.
- A standalone review_passes table is insufficient because an agent can get one clean pass then make a late fix and close against a stale pass unless the pass seals a specific change frontier.
- Adding sessions.status halted naively risks bypassing every existing close trigger keyed to NEW.status closed; halt must either be a close subtype or every trigger must explicitly admit halted.
**schema_sketch.**
- Alternative shape introduces session_change_manifests with manifest_hash and review_seals over that hash, so the reviewer certifies exactly the change set that is closing.
**risk.**
- decision_effects has creates modifies and adds_migration but no deletes, while methodology says deletes of executable logic trigger review; objects.object_kind does not classify file artifacts.
**what_lost.**
- Do not lose the distinction between normal close and halt, and do not lose low-only findings which should be recordable without blocking close.
- Do not lose adjudication for medium-plus findings but require a subsequent clean pass after adjudication, and do not force review for nonbehavioral comments banners and prose-only edits.
- Most importantly do not lose staleness protection: a clean review before the final code mutation is not a clean review of the session.

### Synthesis

P-1 (declaration anchor + review_passes table) and P-2 (recorded-change frontier with manifest-hash sealing) converge on three points: (a) close-gating must be structural, not advisory; (b) review_passes is needed as a separate artefact from review_findings; (c) halted-state must be admitted as a distinct close-path so reviewers can record nonconvergence without lying about adjudication.

They diverge on the anchor. P-1 declares session.kind at open and binds enforcement to that declaration. P-2 argues this is the wrong anchor: under context pressure, sessions mutate (a spec-only session ends up patching CLI), so declaration goes stale or over-broad. P-2 instead binds enforcement to recorded change facts (a session_artifact_changes table) and to a manifest-hash frontier that the review_pass certifies.

Synthesis preserved as minority where applicable. P-2's full alternative (manifest-hash sealing over recorded artifact changes) requires substrate-side file-tracking the system does not have today and would multiply scope. The pragmatic adoption keeps P-1's declaration shape (session.kind, immutable post-open, default 'coding') as the anchor, but adopts P-2's staleness-protection insight by adding a head_sha field to review_passes that the operator must assert at submit-time. The substrate cannot verify head_sha against working-tree truth, but recording it makes the assertion durable for later audit and prevents the trivial late-fix loophole at the protocol level. P-2's manifest-mechanism alternative is recorded as a forward direction, opened as a follow-up issue.

Halted-state encoding adopted as P-1 proposed (sessions.status admits 'halted' as a distinct value), tightened by P-2's caveat: every existing close-gate trigger (T-11, T-18, T-19, T-20) must explicitly admit the halted path so it bypasses the medium+ findings gate while still requiring a structured review_pass row with outcome='nonconverged' and a referenced halt-issue.

Minority preserved: P-2's "enforce from recorded change facts, not intent" is a stronger structural form than the synthesis adopts. If declaration-based enforcement proves operator-policed in practice (i.e. operators routinely declare 'spec_only' falsely or coding-by-default fatigue produces noise), the next revision should escalate to artifact-tracking + manifest-sealing per P-2's alternative.

P-2 also surfaced that decision_effects.effect_kind admits 'creates' and 'modifies' but not 'deletes', though methodology §"Coding review loop" explicitly says "produces, modifies, or deletes executable logic" triggers the loop. Out of scope for this session; opens as a separate issue.


### Synthesis points

- **convergence C-1.** Both P-1 and P-2 agree review_passes must be a distinct artefact from review_findings.
- **convergence C-2.** Both agree halted-state needs structural admission so nonconverged loops can record honestly without faking adjudication.
- **divergence D-1.** P-1 anchors enforcement on declared session.kind; P-2 argues this fails under context pressure and recommends recorded-change facts as the anchor.
- **minority M-1.** P-2 manifest-hash sealing over session_artifact_changes preserved as forward direction if declaration-based enforcement proves operator-policed in practice.
