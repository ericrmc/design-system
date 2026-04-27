---
session: 076
title: Engine restart — decisions
date: 2026-04-27
---

# Decisions

## D-1 — Trim the active specification set to four files

**What.** Replace the prior nine active specifications with four:

- `specifications/methodology.md` — kernel, identity, when to convene multiple agents, when to review at close, validation senses, preservation, engine-feedback, self-hosting.
- `specifications/constraints.md` — what 75 sessions taught us about LLM agents; the brief that informs the successor design.
- `specifications/workspace.md` — file classes, session structure, decisions, specifications discipline.
- `specifications/engine-manifest.md` — thin enumeration of the active engine.

**Why.** The seventy-five-session run accumulated ~3000 lines of active specification across nine files plus ~3200 lines of superseded versions. `applications/075-selvedge-restart/selvedge-problem-statement.md` documents the structural failure mode: the closed-enumeration default-read consumed roughly half the agent's context window at session-open, foundational instructions decayed under that load, and the engine lost its capacity to perceive its own deficiencies. The successor design (sessions 077–078) cannot run from a saturated starting surface; the trim is the precondition for the successor design's deliberation.

**Rejected.**

- *Keep the existing active set and just delete superseded versions.* Rejected because the active set itself was the saturated surface; deleting only the `*-vN.md` files would not address the foundational decay.
- *Trim incrementally over multiple sessions.* Rejected because incremental trim was the engine's failure mode for accumulation in reverse — locally reasonable additions accumulated to a saturated whole. A discontinuity is needed to break the accretion logic.
- *Keep `read-contract.md`, `records-contract.md`, and `retrieval-contract.md` as the substrate spec set even though the substrate is being replaced.* Rejected because the substrate they specify is precisely what the database successor replaces. Retaining them would force the successor design to negotiate against three retiring specs rather than design freshly against the constraints document.

**Open.** The four-file surface is the minimum that allows session 077 to run. Session 077 is expected to produce a design space that will likely add to or rearrange this set; session 078 will design the solution.

## D-2 — Move retired files to `archive/pre-restart/`

**What.** Move all superseded `specifications/*-vN.md` files, the prior active specifications now folded or deleted, and the substrate tools (`retrieval_server.py`, `build_retrieval_index.py`, `digest_emitter.py`, `digest_reconstructor.py`, `bootstrap-external-workspace.sh`) to `archive/pre-restart/specifications/` and `archive/pre-restart/tools/`. Do not delete; preserve the seventy-five-session record in workspace-visible form.

**Why.** Git history alone is not adequate as a preservation surface for a restart of this magnitude — the operator and future sessions will need to read prior content in workspace navigation, and the prior content remains valid as the empirical record from which `constraints.md` is drawn. Moving to a workspace archive keeps the record visible without loading it into the active engine.

**Rejected.**

- *Delete outright.* Rejected; preservation is the methodology's discipline. Even at restart, prior decisions and rejected alternatives remain valid context for re-proposals.
- *Keep at canonical locations with `status: superseded`.* Rejected; the validator and the engine-manifest enumerate active engine-definition files, and superseded files at canonical locations would conflict with the new minimal active set.

**Open.** None.

## D-3 — Establish `engine-v16` as the trim-and-restart version

**What.** Bump the engine version to `engine-v16`. Record in `engine-manifest.md` §Current engine version. Treat this as a discontinuity: prior engine-version history is preserved at `archive/pre-restart/specifications/engine-manifest.md` (the prior file), not retained inline.

**Why.** A version increment is warranted by the substantive change to most engine-definition files. A discontinuity flag is warranted by the scope: this is not an additive revision but a restart against an explicit constraint document. Engine-version increments after engine-v16 will be normal substantive bumps under the new minimal arrangement.

**Rejected.**

- *Reset to `engine-v1`.* Rejected; engine-version numbers are a stable reference point in prior provenance and external-application records (e.g., `selvedge-disaster-response`'s session 001). Resetting to v1 would create ambiguity in those records.
- *Use a different naming convention (e.g., `engine-restart-v0`).* Rejected; the convention is established and the trim, while substantive, is an evolution along the same engine-version axis.

**Open.** Sessions 077 and 078 will likely produce `engine-v17`, `engine-v18`, or further with the introduction of the database substrate and the multi-agent orchestration layer.

## D-4 — Replace executable prompts and dispatcher with thin versions

**What.** Rewrite `PROMPT.md`, `prompts/development.md`, `prompts/application.md` to thin versions that point at the minimal spec set, name what to read, and state operating discipline tersely. The prior three files totaled ~227 lines; the new versions total roughly 130 lines combined.

**Why.** The prior development.md carried six paragraphs of substrate-tool requirements, structured-declaration requirements, file-edit-claim discipline, cross-family-reviewer-invocation pattern, scope-discipline routing, validation-debt-lifecycle disposition discipline, authoritative-not-witness ledger discipline, explicit-Path-justification rules, and reviewer-prompt-template versioning rules. All of these are tied to the engine-v9 through engine-v15 substrate that the trim retires. The successor design will reintroduce whichever of these remain warranted, against the database substrate it produces.

**Rejected.**

- *Keep the operating-discipline paragraphs and only remove substrate references.* Rejected; many of the disciplines were responses to substrate-specific failure modes (substrate-aware branch CHKD-2, harness-telemetry-digest schema, validation-debt ledger authoritative-not-witness) that no longer exist after the trim.

**Open.** The next two sessions will deliberate which disciplines warrant reintroduction.

## D-5 — Replace `tools/validate.sh` with a minimal structural validator

**What.** Replace the validator's twenty-nine checks with a small bash script that verifies presence of the active engine-definition file set, `MODE.md`, `provenance/`, and (for the latest session directory) `00-assessment.md` and `03-close.md`. The new validator is ~75 lines of bash; the old was substantially larger and referenced retired check-numbers (check 25 records-contract, check 26 substrate-aware branch, check 27 reviewer-audit-shape, check 28 validation-debt-ledger, check 29 substrate-session-open).

**Why.** The old validator's checks were tied to retired specifications; running it against the new minimal arrangement would emit cascade failures unrelated to actual workspace integrity. A thin validator that maps to the new minimal arrangement is more truthful than a heavy validator emitting false positives.

**Rejected.**

- *Keep all twenty-nine checks and let them fail; add the new minimal checks alongside.* Rejected; per the operator's brief, the validator's failures here are not signal — they are the expected consequence of a deliberate spec trim, and conflating them with real workspace integrity issues would degrade the validator's signal-to-noise ratio for session 077 onward.

**Open.** Session 078 will likely design a database-backed validator that runs pre-commit rather than at close. The current minimal validator is a placeholder.

## D-6 — Disable the harness-telemetry PostToolUse hook

**What.** Empty `.claude/settings.json` to remove the PostToolUse hook that ran `tools/digest_emitter.py` on every tool call. Leave a no-op stub at `tools/digest_emitter.py` so that any in-flight session whose hook configuration was loaded at start does not error mid-session. The original `digest_emitter.py` is preserved at `archive/pre-restart/tools/digest_emitter.py`.

**Why.** The harness-telemetry digest was the engine-v15 capture-adapter for substrate-tool-use measurement, designed to feed reviewer audits with harness-measured rather than agent-self-reported wall-clock and token counts. With the substrate retired and the reviewer audit shape itself in the redesign scope, the digest is unmoored. Continuing to run the hook would emit per-tool-call records into a directory whose schema is being deprecated.

**Rejected.**

- *Keep the hook running and let it write to the now-orphan provenance digest directory.* Rejected; orphan writes accumulate state that the next two sessions will have to disposition. Cleaner to stop writing now and let the successor design decide what telemetry the next-generation engine wants.

**Open.** Sessions 077 and 078 will likely specify a successor capture mechanism (database row inserts on tool calls, or harness-side telemetry against a new schema). The stub `digest_emitter.py` and the `.claude/settings.json` empty state can be cleaned up in those sessions.

## D-8 — Reject all open engine-feedback records as superseded by the restart

**What.** Mark the nine still-open engine-feedback records (three `new` plus six `triaged`/`triaged-partially-resolved`/`triaged-deferred-to-phase-3`) as **rejected** with disposition `engine-v16 restart supersession`. Record the blanket disposition at `engine-feedback/triage/EF-076-engine-v16-restart-supersession.md`. Update `engine-feedback/INDEX.md` status summary to 0 new / 0 triaged / 10 resolved / 9 rejected, and update each row's Status column to mark rejected with prior-status preserved for context.

The nine rejected records: EF-075-integrity-by-construction-not-after-the-fact-detection, EF-075-reviewer-cost-not-optimization-target, EF-075-reviewer-side-substrate-use, EF-068-substrate-load-bearing-and-harness-telemetry, EF-068-read-write-rebalance, EF-067-reviewer-wall-clock-self-report-unreliable, EF-059-harness-telemetry-feed-for-tier-2-reviewer, EF-058-claude-md-tools-clause-not-cross-checked-by-mad, EF-047-brief-slot-template-hidden-arc-leakage.

**Why.** Each open record raises a concern against specifications or tooling that the engine-v16 trim retires. Carrying them as backlog into session 077 would force the successor design to either disposition each as a point-fix against the new arrangement or to declare each individually irrelevant. The cleaner move is to disposition them as a blanket supersession at session 076 close; the underlying concerns the records carry are preserved as inputs to `specifications/constraints.md` (which was distilled from the same empirical record). The successor design is the architectural response to the concerns; it should not be required to justify itself against per-record dispositions framed in the prior arrangement's vocabulary.

**Rejected.**

- *Carry the open records into session 077 as triage backlog.* Rejected; this is the accretion logic that produced the saturated active-spec set in the first place. Locally reasonable triage decisions accumulated to a saturated whole.
- *Reject only the three new EF-075 records and leave the six triaged records as triaged-partially-resolved.* Rejected; the partial-resolution narratives are entirely tied to substrate work being retired (γ-phase digest, reviewer-prompt-template v3, REVD-2 quarantine semantics, validation-debt VD-003 review). The "partial resolution" disposition is meaningful only against a substrate that no longer exists.

**Open.** None. The blanket supersession is a closure event, not a deferral.

## D-7 — Carry over prior workspace state without modification

**What.** Do not touch the existing `provenance/001-genesis/` through `provenance/075-session/`, `applications/008-morning-unfurl/`, `applications/010-household-decision-protocol/`, `applications/075-selvedge-restart/`, `engine-feedback/`, `open-issues/`, `validation-debt/`, or `records/` directories. They remain in place as historical record.

**Why.** The trim is scoped to the engine-definition surface (specs, prompts, tools). Workspace-scope state (provenance, applications, feedback, issues, ledger) is the empirical record from which `constraints.md` was drawn; deleting it would erase the evidence base for the very findings the successor design responds to. The successor design (sessions 077–078) will decide what to migrate, what to archive, and what to delete from the workspace-scope state once the database substrate exists.

**Rejected.**

- *Move all of `provenance/001-` through `075-` to archive.* Rejected; provenance is per the methodology's preservation discipline immutable after close, and moving it would suggest it is no longer part of the workspace's record. It is — it is the record from which the successor design draws.
- *Migrate the engine-feedback inbox into the new engine.* Rejected at this scope; the trim is engine-definition only. Engine-feedback triage is a substantive disposition decision that belongs in session 077 or 078.

**Open.** Sessions 077 and 078 will likely propose a partial migration of workspace-scope state into the database substrate, or designate some of it as archive-only.
