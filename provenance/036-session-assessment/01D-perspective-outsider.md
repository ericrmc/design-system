---
session: 036
title: Perspective — Outsider (Path PD)
date: 2026-04-23
status: complete
perspective: Outsider
committed_at: 2026-04-23T00:00:00Z
---

# Q1. Dispatcher revision

Yes, the dispatcher should be revised. My preferred resolution is a hybrid, but not the hybrid I expect Claude-family perspectives to privilege. I would make dispatch primarily **operator-asserted at invocation or initialization**, with a persistent workspace marker as a guardrail, not as the source of truth.

External input (pretraining): in ordinary software systems, entrypoint selection is rarely inferred from accumulated logs. POSIX shebangs, Docker `ENTRYPOINT`, `package.json` scripts, Make targets, systemd units, and CLI subcommands all express the intended execution path before execution begins. They may validate local state after that, but they do not decide whether something is a library, an app, or a migration by reading historical append-only logs. That is the pattern I think this brief underweights.

The current `PROMPT.md` dispatch criteria are trying to infer mode from workspace biography. The self-development branch says: “If the workspace contains `SESSION-LOG.md` with prior sessions of self-development...” The external branch says: “If the workspace contains the engine-definition files but a fresh (empty or near-empty) `SESSION-LOG.md`...” The second criterion is known to expire after external Session 001. The first depends on the phrase “of self-development,” but does not specify an internal verifier. This is not merely a missing heuristic; it is a category error. A session log is an event record, not a mode declaration.

I would revise toward Direction 6, combining Direction 1 and Direction 4, with a small amount of Direction 5. Specifically:

`MODE.md` should exist at workspace root after initialization. It should be deliberately boring:

```yaml
---
mode: self-development
workspace_id: selvedge-self-development
created_session: 001
engine_version_at_creation: engine-v1
---
```

or:

```yaml
---
mode: external-problem
workspace_id: external-001-example-slug
created_session: 001
engine_version_at_creation: engine-v6
application_brief: applications/001-example-slug/brief.md
---
```

`PROMPT.md` should first read `MODE.md`. If it is absent, it should not attempt elaborate deduction except for one narrow compatibility path: if the workspace is the historical self-development workspace and contains recognizable genesis provenance, continue as self-development but require Session 036 or Session 037 to write the marker. For new external applications, Session 001 initialization must write the marker before substantive work.

I would also split operational entrypoints conceptually, even if not physically. The current single `PROMPT.md` may remain the dispatcher, but it should be reduced to: identify mode from `MODE.md`, validate required files for that mode, then tail-call `prompts/development.md` or `prompts/application.md`. If separate prompt files such as `PROMPT-development.md` and `PROMPT-external.md` are too disruptive, preserve a single dispatcher but treat explicit mode as the architectural contract.

My dissent: I do not favor a purely structural signature, such as “presence of `applications/NNN-<slug>/brief.md` means external.” The self-development workspace already contains `applications/` because it has produced external artefacts. Structural signatures are tempting because they avoid another file, but they encode accidental layout as identity. That will fail again when a future workspace has both self-development material and application material for legitimate reasons.

I also do not favor `SESSION-LOG.md` frontmatter as the primary mechanism. A log can carry mode metadata, but a log should remain a log. If mode is needed before deciding how to interpret the log, putting mode inside the log makes the dispatcher depend on the thing it is trying to classify.

# Q2. Operator-mediated feedback pathway

There should be a first-class feedback pathway, but it should resemble an upstream issue intake process more than a loose notes folder.

External input (pretraining): software projects distinguish between downstream bug reports, upstream patches, RFCs, incident reports, changelog entries, and issue trackers because they serve different evidentiary functions. A good feedback pathway preserves the raw report, records triage, links to resolution, and distinguishes “reported” from “accepted.” The Selvedge engine should copy that discipline rather than inventing an ad-hoc memory hole named “feedback.”

I propose a non-engine directory at workspace root:

`engine-feedback/`

In external-application workspaces, this directory is an **outbox**. In the self-development workspace, it is an **inbox plus triage ledger**. The directory is not itself part of the engine definition, but the engine specs should define its optional semantics.

In an external workspace:

`engine-feedback/outbox/EF-<external-session>-<short-slug>.md`

Each file should be a structured record with frontmatter:

```yaml
---
feedback_id: EF-002-dispatch-steady-state
source_workspace_id: external-001-example-slug
source_session: 002
created_at: 2026-04-23T00:00:00Z
reported_by: operator
target: engine
target_files:
  - PROMPT.md
  - specifications/engine-manifest.md
severity: friction
status: outbound
---
```

Body sections should be standardized but lightweight:

`Observation`
What happened in the external application.

`Why It Matters`
What engine or methodology behavior was implicated.

`Suggested Change`
Optional. The reporter may leave this blank.

`Evidence`
Links or copied snippets from the external workspace.

`Application-Scope Disposition`
Why the external application did or did not resolve it locally.

In the self-development workspace, the operator copies the file verbatim to:

`engine-feedback/inbox/EF-<source-workspace-id>-<feedback-id>.md`

A self-development session then triages it. The triage state should not overwrite the original report. Add a separate file:

`engine-feedback/triage/EF-<source-workspace-id>-<feedback-id>.md`

with fields:

```yaml
---
feedback_ref: engine-feedback/inbox/EF-external-001-example-slug-EF-002-dispatch-steady-state.md
triage_session: 036
status: accepted
classification: substantive
opened_issue: open-issues/OI-006.md
resolved_by: provenance/036-session-assessment/
---
```

This preserves raw intake and keeps interpretation separate.

For read-contract integration, I would not make every feedback file default-read. That will not scale. Instead, add `engine-feedback/INDEX.md` as default-read when present. The index lists new, active, deferred, and closed feedback records. `specifications/read-contract.md` should require default read of the index in self-development mode. The individual inbox files become activation-read when the index shows `status: new` or when an OI points to them.

For OI integration, substantive feedback should become or attach to an open issue. Minor feedback can remain in the feedback triage ledger with `classification: minor` and be bundled into the next housekeeping session. Watchpoints can be recorded either in the triage file or promoted to OI if they require repeated activation. First-class minority should be preserved inside the self-development provenance when a feedback item is deliberated and rejected.

The important distinction is that external feedback should be preserved verbatim. Summary-only intake is insufficient because it loses the downstream context, which is often the whole point. The operator may mediate transfer, but should not be required to normalize or interpret the feedback before self-development sees it.

# Q3. Relationship between Q1 and Q2

The two problems are related by theme but should not be solved by one mechanism. Q1 concerns **entrypoint identity**. Q2 concerns **upstream feedback flow**. Combining them too tightly would create a brittle meta-control file that tries to be both a mode marker and an issue tracker.

`MODE.md` can contain a pointer such as:

```yaml
feedback_outbox: engine-feedback/outbox
```

for external workspaces, and:

```yaml
feedback_inbox: engine-feedback/inbox
```

for self-development. But the dispatcher should not inspect feedback to determine mode. The dependency should run one way only: mode selection determines whether feedback is read as external outbox, self-development inbox, or ignored.

This separation matters because feedback may exist in both modes. An external workspace has outbound feedback. The self-development workspace has inbound feedback. A future hybrid or test workspace may have neither. If the dispatcher reads `engine-feedback/` as a mode signal, the same class of structural ambiguity will recur.

My dissent here is against the pleasing symmetry of “both are boundary problems, therefore one boundary mechanism.” They are architecturally distinct. Dispatch is control-plane selection. Feedback is evidence-plane transfer. They should be adjacent in the specs, not fused.

# Q4. Substantive revision scope

This is a substantive engine revision and should bump `engine-v6` to `engine-v7` under `specifications/engine-manifest.md §5`.

Expected file changes:

`PROMPT.md`
Revise dispatch lines 18–26 so `MODE.md` is authoritative. The fallback should be narrower: absent marker plus ambiguous state halts; absent marker plus recognized legacy self-development workspace may proceed only to create/adopt marker.

`prompts/development.md`
Add read behavior for `engine-feedback/INDEX.md` and a requirement to triage new inbound feedback when activated by the operator or when the index marks new items.

`prompts/application.md`
Add instruction that application sessions may record engine/methodology feedback in `engine-feedback/outbox/` when the operator identifies such feedback or when the session produces a boundary friction record.

`specifications/workspace-structure.md`
Define `MODE.md` as a required workspace identity file for all initialized workspaces. Define `engine-feedback/` as optional non-engine content with outbox/inbox semantics depending on mode.

`specifications/read-contract.md`
Add default-read treatment for `MODE.md`; add conditional default-read for `engine-feedback/INDEX.md` in self-development mode.

`specifications/engine-manifest.md`
Update engine version to v7 and include `MODE.md` status. I would treat `MODE.md` as a required workspace file but not an engine-definition file copied identically across workspaces, because each workspace has distinct identity. The manifest should distinguish “engine-definition files” from “workspace identity files.”

`specifications/methodology-kernel.md` or `specifications/validation-approach.md`
Only minimal change, if any. Do not over-expand kernel doctrine for what is operational plumbing. If a principle is needed, add a short note that external-application practice can produce self-development inputs through operator-mediated feedback records.

`tools/validate.sh`
Add checks that `MODE.md` exists and has valid `mode`. For external workspaces, validate that `application_brief` exists. For self-development, validate that development provenance exists. If `engine-feedback/INDEX.md` exists, optionally validate that listed files exist.

This is not a minor wording patch. OI-002, if it tracks substantive-versus-minor classification, should classify this as substantive because it changes session entry semantics, workspace initialization requirements, read-contract defaults, and validation. The change is still bounded: no need to rewrite MAD v4 or the full methodology kernel unless deliberation uncovers deeper identity claims.

# Q5. First-class minority preservation

Rejected directions worth preserving:

Pure structural dispatch should be preserved as a minority because it keeps workspace setup lightweight and avoids adding identity files. Its activation warrant: if `MODE.md` proves burdensome, frequently stale, or inconsistently copied, structural dispatch may be revisited with a stricter and better-designed signature.

`SESSION-LOG.md` frontmatter dispatch should be preserved because it minimizes file count and puts identity near session history. Its activation warrant: if the project later chooses to make `SESSION-LOG.md` a real database-like ledger rather than a thin index, centralizing workspace metadata there may become defensible.

Separate prompt files with operator-selected invocation should be preserved more strongly than I expect others to do. Its activation warrant: if autodispatch continues to create ambiguity, remove autodispatch. Require the operator to invoke `PROMPT-development.md` or `PROMPT-external.md` directly. This is less elegant but more explicit, and explicit entrypoints are common in mature tooling.

No-revision fallback should be preserved only as a weak minority. It is operationally safe but knowingly preserves repeated friction. Its activation warrant: if Session 036 wants to avoid engine-v7 churn and no external Session-002 is imminent, deferral is acceptable. But as a design answer, it is inadequate.

For feedback intake, preserve a minority for “feedback becomes OI directly.” That is simpler. Its activation warrant: if `engine-feedback/` becomes a parallel issue tracker, collapse it into OI. My reason for rejecting it now is evidentiary: raw external reports and self-development issue framing are different artefacts.

Also preserve a minority for non-operator-mediated cross-workspace references. External input (pretraining): upstream/downstream workflows often use direct issue links, branches, or patches instead of human-carried reports. Activation warrant: if the engine gains a multi-workspace registry or automation layer, feedback should move by reference or generated patch rather than manual copying. I do not recommend that now because the brief explicitly requires operator-mediated intake and the current engine appears file-local.

# Q6. WX-35-1 disposition

I recommend option (c): incremental catch-up from Session 036 forward, unless the same editing session is already touching `open-issues/OI-004.md` for another substantive reason. Do not spend a standalone Session 036 backfill on a 13-session historical claimed-but-unexecuted file-edit gap.

The reason is not that the gap is unimportant. It is that retroactive backfill can create a false sense of historical cleanliness. The durable fact is that the SESSION-LOG row claimed an edit that did not occur. That should remain visible as a process defect. The better correction is to adopt a forward convention: when a session claims an OI file edit, validation or closeout must verify the file changed, or the session log must explicitly say that the canonical record is the log row and the OI file was not edited.

I would bundle a small note into the Session 036 revision if the engine files are already being changed: record WX-35-1 as a known historical discrepancy, state that no retroactive content reconstruction was attempted, and require future OI dispositions to name the canonical artefact. If `open-issues/OI-004.md` is touched for nearby reasons, add a minimal “Session 036 catch-up note” rather than reconstructing thirteen sessions.

My dissent from likely process-heavy perspectives: not every inconsistency deserves archival repair. Sometimes the honest artefact is the scar. The engine should improve its forward write discipline rather than spend scarce deliberation budget manufacturing a tidier past.

<!-- codex session id: 019db9c3-02bc-7522-8f78-35f1e6502980 -->
