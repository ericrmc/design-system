---
session: 122
title: ef-session-binding-relax — deliberation
generated_by: selvedge export
---

# Deliberation

## D-13 — Relax engine_feedback.session_id NOT NULL so out-of-session EF submission stops costing a session-open ceremony

sealed_at: 2026-04-29T09:46:41.847Z

### P-1 (anthropic)

**Position.** Position D: keep schema intact and add a one-shot wrapper that opens a real session, submits the EF, and closes it — preserving substrate-wide coherence.

**position.**
- The right answer is D: a one-shot wrapper that performs the open/submit/close ceremony, leaving engine_feedback.session_id NOT NULL.
**what_not.**
- Reject A: nullable session_id forces six query sites (orient, anchor x3, monitor_external x3, subtract, peer alias indexer) to invent fallback partitions.
- Reject B: never-closing sentinel session violates T-29 immutability and the unique-open-session invariant.
- Reject C: per-EF transient sessions double write volume and pollute the timeline with meta ceremony rows operators wanted to avoid.
**schema_sketch.**
- The session itself IS the provenance trail: it carries engine_version_at_close, close_record, workspace_session_no for EF aliasing, surfaced_in, and the export anchor.
**cli_surface.**
- D wraps session-open + close-record + session-close into one command, achieving the ergonomics A claims with zero schema delta.
**risk.**
- Peer-harvest already calls _atom_session_id(conn, None); option A forces an ugly choice between landing peer EFs in self-dev or losing alias namespace.
**what_lost.**
- D documents-the-dance is reframed as a feature: the ceremony produces a real session whose close-record records why the session existed.
**open_question.**
- Four instances of friction is evidence a 6-step ceremony deserves a shortcut, not evidence the schema is wrong.
**migration_path.**
- D requires zero NULL-safe rewrites at six query sites, zero invariant breakage, and full backward-compat with harvest-ef.

### P-2 (openai)

**Position.** Position F: keep engine_feedback.session_id NOT NULL and add a feedback-intake wrapper that opens a normal kind=meta session around out-of-session EFs.

**position.**
- Keep engine_feedback.session_id NOT NULL and add a feedback-intake wrapper that opens a normal meta session for out-of-session EFs.
**what_not.**
- Reject A: it is small DDL but large semantic change, since alias derivation, orient/monitor joins, subtract aging, and export anchors all key off session.
**risk.**
- Nullable session_id turns inner joins and alias derivation into exception handling and makes out-of-session EFs visibly second-class.
**what_not.**
- Reject B: a sentinel always-open session breaks the unique-open-session invariant the rest of the substrate relies on.
- C and D are closer to right but per-EF transient sessions are noisy; a batched intake wrapper is the better missing option.
**cli_surface.**
- Wrapper opens one kind=meta intake session, submits one EF or harvest batch via _submit_engine_feedback, writes a minimal close record, and closes.
**migration_path.**
- Peer EFs remain session-bound, _me_read_peer_ef keeps working, and self-dev import can still reuse the normal handler inside the intake session.
**open_question.**
- The actual drift is operator discipline plus tooling: the peer put feedback-shaped facts in close prose where harvest-ef cannot see them.
**schema_sketch.**
- Fix the capture path and ceremony, not the core session provenance invariant; non-null session_id is load-bearing across the substrate.

### Synthesis

Both perspectives reject schema relaxation (A nullable, B sentinel session, C transient-per-EF) and converge on operator-tooling: keep engine_feedback.session_id NOT NULL and add a wrapper that opens a kind=meta session, submits the EF (or harvest batch), and closes the session in one CLI invocation. P-1 and P-2 differ only in scope — P-1 frames it as a single-EF shortcut (option D); P-2 extends to harvest-ef batches as well (option F). Reconciliation: ship the wrapper covering both 1-EF and N-EF intake. Frame-challenge accepted: friction is operator-discipline drift, not substrate flaw.

### Synthesis points

- **convergence C-1.** Reject schema relaxation (A,B,C); engine_feedback.session_id NOT NULL is load-bearing for aliases, orient, anchor, harvest, subtract.
- **convergence C-2.** Adopt operator-tooling: a wrapper command that opens kind=meta intake session, submits EF(s), closes — one CLI call.
- **convergence C-3.** Friction is operator-discipline drift around ceremony, not substrate flaw; the wrapper documents the dance honestly.
- **divergence D-1.** Scope: P-1 wrapper handles single-EF only (option D); P-2 wrapper also batches harvest-ef intake (option F). Reconcile: cover both.
