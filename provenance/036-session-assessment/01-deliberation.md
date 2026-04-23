---
session: 036
title: Deliberation synthesis — Path PD (PROMPT.md §Dispatch criterion correction + external-application feedback pathway)
date: 2026-04-23
status: complete
synthesiser: Case Steward (Claude Opus 4.7)
participants_family: cross-model
cross_model: true
non_claude_participants: 1
oi004_qualifying_participants: [Outsider]
---

# Session 036 Path PD — Deliberation Synthesis

Synthesis of four raw perspective outputs per `multi-agent-deliberation.md` v4 §Synthesis. Synthesiser is the Case Steward (distinct from the four deliberation perspectives per v4 §Synthesizer identity).

Raw source files:
- `[01A-perspective-reviser.md]` — Reviser (Claude subagent A)
- `[01B-perspective-skeptic-preserver.md]` — Skeptic-preserver (Claude subagent B, adversarial)
- `[01C-perspective-synthesiser.md]` — Synthesiser (Claude subagent C)
- `[01D-perspective-outsider.md]` — Outsider (non-Claude; OpenAI GPT-5.4 via `codex exec`)

## §1 Convergence map (coverage vs. genuine convergence)

**Strong convergence (4-of-4 across both families):**

- **Q3 (Q1/Q2 relationship).** All four perspectives independently conclude that Q1 (dispatch) and Q2 (feedback pathway) are **related by theme but architecturally distinct; solve in the same session with independent mechanisms; do not bundle into one mechanism.**
  - Reviser: "related by theme but independent by mechanism" `[01A, Q3]`.
  - Skeptic-preserver: "they should be treated as independent ... Bundling them into one mechanism would be a false economy" `[01B, Q3]`.
  - Synthesiser: "Treat Q1 and Q2 as distinct mechanisms with clean decomposition, but solve them in the same session" `[01C, Q3]`.
  - Outsider: "Dispatch is control-plane selection. Feedback is evidence-plane transfer. They should be adjacent in the specs, not fused." `[01D, Q3]`.
  - This is genuine cross-family convergence, not coverage. Load-bearing for the decision structure — supports separate decision records D-113 (dispatch) and D-116 (feedback pathway) rather than a single conflated decision.

**3-of-4 cross-family convergence:**

- **Q1 revision warranted.** Reviser + Synthesiser + Outsider argue revision is warranted; Skeptic-preserver dissents (prefers no-revision-warranted; fallback position: one-sentence clarification only). Cross-family weighting: 1 non-Claude (Outsider) + 2 Claude (Reviser, Synthesiser) for revision; 1 Claude (Skeptic-preserver) for no-revision.
- **Q2 pathway warranted.** Reviser + Synthesiser + Outsider argue pathway is warranted; Skeptic-preserver dissents (prefers "premature"; fallback position: single `engine-feedback.md` plain file). Cross-family weighting same as Q1.
- **Q4 engine-v7 bump.** Reviser + Synthesiser + Outsider converge on substantive classification per OI-002, hence engine-v7; Skeptic-preserver dissents (prefers zero substantive; fallback: might cross threshold but argues against reaching it).

**Coverage (single-perspective, not converged):**

- **Direction-6 hybrid structure** — Synthesiser + Outsider both propose hybrids, but **their hybrids differ substantively**:
  - Synthesiser hybrid: "direction 2 (structural signature) as the *primary* dispatch test, with direction 5 (Session-001 init discipline) as the *generative* discipline ... and direction 1 (`MODE.md`) as an *optional override*" `[01C, Q1]`.
  - Outsider hybrid: `MODE.md` as **primary and authoritative**; structural signature rejected as "encode accidental layout as identity"; PROMPT.md reads MODE.md first; narrow legacy-compatibility fallback `[01D, Q1]`.
  - This is a genuine cross-family divergence **within** the majority-for-revision. The Outsider's position is more restrictive (MODE.md-authoritative); the Synthesiser's is more layered (MODE.md-override). The Reviser's position (structural signature only; Direction 2 pure) is a third position within the majority.

- **Q2 specific shape** — 3-of-3 agree pathway warranted; shapes differ:
  - Reviser: OI frontmatter tag `scope: engine-feedback` reusing existing OI machinery; no new directory `[01A, Q2]`.
  - Synthesiser: `feedback.md` section in application close convention, optional OI-lift by operator `[01C, Q2]`.
  - Outsider: structured `engine-feedback/` directory with `outbox/` + `inbox/` + `triage/` subdirectories; `INDEX.md` as default-read; feedback-record frontmatter schema; triage-state-separate-from-intake `[01D, Q2]`.
  - The Outsider's structured proposal is the most elaborate and is cross-lineage-originated (explicit software-engineering RFC/issue-tracker framing per `[01D, Q2]` external-input flag).

- **Q6 WX-35-1** — split:
  - Reviser: defer to Session 037/038; option (c) incremental, standalone session `[01A, Q6]`.
  - Skeptic-preserver: option (b) SESSION-LOG-row-canonical convention `[01B, Q6]`.
  - Synthesiser: hybrid (b)+(c) — new forward convention + accept past drift + evaluation window `[01C, Q6]`.
  - Outsider: option (c) with forward convention ("when a session claims an OI file edit, validation or closeout must verify the file changed") `[01D, Q6]`; bundle a minimal note into Session 036 if engine files are being changed anyway.

## §2 Preservation of dissent

Per MAD v4 §Preserve dissent: Skeptic-preserver's no-revision-warranted position on Q1 + premature-on-Q2 position is preserved in full. See §6 below.

## §3 Q1 — Dispatch revision

### §3a Points of agreement (3-of-4 cross-family majority)

Revision is warranted. The current external-problem-branch criterion is a Session-001-only signature per the operator's agenda (confirmed at `00-assessment.md` §2a(i)); leaving it unchanged means the dispatcher fallback (line 24) fires on every external-application Session-002+ load. The cost of revision is bounded (specific file edits, bounded surface expansion) and the cost of preservation is unbounded-in-N (linear in external-application session counts).

### §3b Points of divergence within the majority

- **Reviser (`[01A, Q1]`)**: Direction 2 pure — structural signature via `applications/NNN-<slug>/brief.md` presence and `provenance/001-genesis/` for self-dev negative signal. No new files. Rejects Direction 1 as over-engineered.
- **Synthesiser (`[01C, Q1]`)**: Hybrid (Direction 2 primary + Direction 1 as optional override + Direction 5 init discipline).
- **Outsider (`[01D, Q1]`)**: Direction 1 primary (MODE.md authoritative) + rejects pure structural signature. Cross-lineage critique: *"A session log is an event record, not a mode declaration."* `[synth]` this is the category-error framing that load-bearingly shaped synthesis adoption toward MODE.md-centred hybrid rather than pure structural signature.

### §3c Synthesiser-adopted direction

**Adopt the Synthesiser's layered hybrid, informed by Outsider's category-error critique of pure structural signature**:

1. **Primary dispatch signal: `MODE.md` at workspace root** carrying `mode: self-development | external-problem` in frontmatter. Required at session-001 initialisation for all new workspaces; required adoption at Session 036 for the existing self-development workspace.
2. **Secondary signal (fallback when MODE.md absent)**: structural signature — presence of `applications/NNN-<slug>/brief.md` routes external-problem; presence of `provenance/001-genesis/` without any `applications/NNN-<slug>/brief.md` routes self-development.
3. **Tertiary fallback (both signals ambiguous or missing)**: halt and seek clarification from the operator per current line 24 semantics.

Rationale for synthesis-adopted direction: The Outsider's critique that a pure structural signature "encodes accidental layout as identity" is load-bearing `[01D, Q1]` — the self-development workspace has future latent ambiguity (a self-development session producing a `brief.md` artefact would mis-route under Reviser's pure Direction 2). MODE.md as explicit identity declaration resolves this. But requiring MODE.md *only* (Outsider's direction) introduces a must-exist invariant whose absence fails closed. The Synthesiser's layering (MODE.md optional override + structural signature as fallback) avoids the fail-closed risk for mature legacy workspaces while giving new workspaces the unambiguous identity Outsider calls for.

This is a **3-of-4 cross-family convergence on revision** + **Synthesiser direction within the majority**, informed by Outsider's category-error critique that forced the hybrid away from pure structural signature.

### §3d Specific revised PROMPT.md §Dispatch text

```
## Dispatch

At load, determine the workspace mode by the following ordered checks:

**1. `MODE.md` at workspace root (authoritative if present).** Read its frontmatter. If `mode: self-development` — this is the self-development application's source workspace; load `prompts/development.md`. If `mode: external-problem` — this is an external-problem application's workspace; load `prompts/application.md`. If `MODE.md` exists but carries an unrecognised `mode:` value, halt and seek clarification.

**2. Structural signature (fallback when `MODE.md` absent).** If the workspace contains the engine-definition files enumerated in `specifications/engine-manifest.md` §3 AND contains at least one `applications/NNN-<slug>/brief.md` file, this is an external-problem application's workspace; load `prompts/application.md`, and the loading session should create `MODE.md` at its close per §Session-001 obligation below. If the workspace contains the engine-definition files AND contains `provenance/001-genesis/` AND contains no `applications/NNN-<slug>/brief.md`, this is the self-development application's source workspace; load `prompts/development.md`, and the loading session should create `MODE.md` at its close if not already present.

**3. Ambiguous or uninitialised (halt).** If the workspace does not yet contain the engine-definition files, or if both the external-problem and self-development structural signatures fire (e.g., a workspace containing both genesis provenance and an `applications/NNN-<slug>/brief.md`), or if neither fires, halt and seek clarification from the operator. Do not attempt to infer the mode from partial evidence.

## Session-001 obligation for new workspaces

Session 001 of any new workspace (self-development or external-problem) MUST create `MODE.md` at workspace root before substantive work, containing:

    ---
    mode: self-development | external-problem
    workspace_id: <short stable identifier>
    created_session: 001
    engine_version_at_creation: <e.g., engine-v7>
    ---
    # Workspace mode marker
    
    (optional prose on the workspace's intent)

For external-problem workspaces, MODE.md additionally carries `application_brief: applications/NNN-<slug>/brief.md`.
```

Note: the self-development workspace (this workspace) creates its MODE.md in Session 036 as the adoption-session obligation; this is the only permitted post-Session-001 creation and is a one-time-per-workspace event.

## §4 Q2 — External-application feedback pathway

### §4a Points of agreement (3-of-4 cross-family majority)

Pathway is warranted. Engine improvements from external-application practice currently depend on operator memory (confirmed unanimously across majority perspectives). The Sessions 008 + 010 precedent with no surfaced feedback is genuinely ambiguous: could be (i) absence-of-need or (ii) absence-of-pathway `[01C, Q2]`. Preserving reading (i) via the Skeptic-preserver dissent is warranted, but the majority adopts that pathway formalisation is prudent regardless.

### §4b Points of divergence within the majority

- **Reviser (`[01A, Q2]`)**: reuse OI machinery via `scope: engine-feedback` frontmatter tag on OIs; no new directory.
- **Synthesiser (`[01C, Q2]`)**: `feedback.md` section in application close; optional OI-lift by operator on return.
- **Outsider (`[01D, Q2]`)**: structured `engine-feedback/` directory at workspace root with `outbox/`, `inbox/`, `triage/` subdirectories; per-feedback frontmatter schema (feedback_id, source_workspace_id, source_session, target_files, severity, status); separate triage-state from intake.

### §4c Synthesiser-adopted direction

**Adopt a structured `engine-feedback/` directory at workspace root per Outsider's direction, with simplifications** to reduce surface area per Synthesiser's integrative trade-off analysis:

1. **`engine-feedback/` at workspace root** (non-engine-definition; operator-managed). In external-application workspaces, the directory is an **outbox** — feedback files the external application's operator creates when methodology-level friction is observed. In the self-development workspace, the directory is an **inbox plus triage ledger** — feedback files the operator copies in from external workspaces, and triage records tracking disposition.
2. **Structured feedback file frontmatter** per Outsider's schema `[01D, Q2]`:
   ```yaml
   ---
   feedback_id: EF-NNN-<slug>
   source_workspace_id: <workspace id>
   source_session: NNN
   created_at: <ISO-8601>
   reported_by: operator | application-agent
   target: engine | methodology | other
   target_files: [<paths>]
   severity: blocker | friction | observation
   status: outbound | inbox | triaged | resolved | rejected
   ---
   ```
   Body sections: `Observation`, `Why It Matters`, `Suggested Change` (optional), `Evidence`, `Application-Scope Disposition`.
3. **Triage ledger** — separate file per feedback record at `engine-feedback/triage/EF-<id>.md` recording triage-session, classification (substantive | minor | non-applicable), decision outcome (opened-OI | watchpoint | direct-revision | rejected), resolution pointer. Triage is additive; original intake is not edited.
4. **`engine-feedback/INDEX.md`** at workspace root directory, default-read when present. Index thin one-line summary per feedback; lists counts by status.
5. **OI integration**: substantive feedback that warrants OI opening produces a new OI in `open-issues/` following existing conventions; the triage file cross-references the OI via `opened_issue:` pointer. Minor feedback can remain in triage-only.
6. **Retention**: feedback files preserved verbatim per read-contract discipline. Neither intake nor triage overwrite each other.
7. **Not default-read at scale**: per Outsider `[01D, Q2]`, individual feedback files are **not** default-read; `engine-feedback/INDEX.md` is default-read (when present) in self-development mode; individual files become activation-read when index shows `status: new` or when an OI cross-references them.

**Simplifications from Outsider's full proposal**:
- No `outbox/` subdirectory required — the external-workspace side places feedback directly under `engine-feedback/`; directory organisation is local discretion.
- `tools/validate.sh` extension for MODE.md validity is adopted minimally (check 23, new); full external-workspace-application-brief validation is deferred to Session 037+ (not this session's scope).

The Reviser's OI-tag-only proposal is preserved as first-class minority (activation warrant: "if engine-feedback/ directory in self-dev workspace accumulates fewer than 3 distinct feedback records over 10 sessions, reconsider collapsing to OI-tag-only per Reviser Direction `[01A, Q2]`").

The Skeptic-preserver's premature-feedback-pathway position is preserved as first-class minority (activation warrant: "if no feedback file flows into engine-feedback/inbox for 10 consecutive sessions post-adoption with no external applications in flight, Skeptic-preserver premature-formalisation position is retroactively vindicated").

## §5 Q3 / Q4 / Q5 / Q6 convergence

**Q3**: 4-of-4 convergence on independent mechanisms, same session. Adopted.

**Q4 (substantive revision scope + engine-v bump)**: 3-of-4 convergence on engine-v7 bump per OI-002 substantive heuristic. Files substantively touched:

1. `PROMPT.md` — §Dispatch revision per §3d above + new §Session-001 obligation section.
2. `specifications/workspace-structure.md` — add MODE.md + engine-feedback/ sections.
3. `specifications/read-contract.md` — add MODE.md to §1 default-read enumeration; add engine-feedback/INDEX.md conditional default-read clause.
4. `specifications/engine-manifest.md` — add `MODE.md` as workspace-identity file distinct from engine-definition files per Outsider's conceptual distinction `[01D, Q4]`; engine-v6 → engine-v7 entry in §2 + §7.
5. `prompts/application.md` — add §"Engine/methodology feedback" clause instructing external-application agents to file feedback to `engine-feedback/` when methodology-level friction is observed.
6. `prompts/development.md` — add one-sentence read obligation for `engine-feedback/INDEX.md` when it exists.
7. `tools/validate.sh` — new check 23 minimally validating MODE.md presence + mode-value for self-development workspace; extensions for external-workspace validation deferred.

**MODE.md file created** at workspace root for self-development (adoption-session one-time creation; not an engine-definition file per Outsider's distinction `[01D, Q4]`).

**engine-feedback/** directory + `INDEX.md` created at workspace root (empty-state; non-engine-definition).

**Q5 (first-class minority preservation)** per majority agreement with addition of Skeptic-preserver's dissent as dominant minority:

- **§10.4-M1 Skeptic-preserver no-revision-warranted on Q1** (full dissent preserved). Activation warrant: if 10 sessions post-adoption the new MODE.md + structural-signature dispatcher has been exercised zero times beyond the Session 036 self-development adoption event (i.e., no new workspace initialised, no external application begun), retroactively vindicates no-revision premature adoption; reconsider reverting PROMPT.md §Dispatch to engine-v6 form.
- **§10.4-M2 Skeptic-preserver premature-feedback-pathway on Q2** (full dissent preserved). Activation warrant: if no feedback file flows into engine-feedback/inbox for 10 consecutive sessions post-adoption with no external applications in flight during that window, position retroactively vindicates.
- **§10.4-M3 Reviser pure Direction 2 structural-signature dispatch** (rejected in favour of hybrid). Activation warrant: if MODE.md adoption proves burdensome, frequently stale, or inconsistently created at Session 001 of new workspaces across 3+ workspace initialisations, consider collapsing to pure structural signature.
- **§10.4-M4 Outsider pure Direction 1 MODE.md-only authoritative dispatch** (rejected in favour of hybrid with structural-signature fallback). Activation warrant: if the structural-signature fallback produces ambiguous routing in practice (e.g., a self-development workspace with legitimate `applications/NNN-<slug>/brief.md` content), consider removing fallback and requiring MODE.md.
- **§10.4-M5 Reviser OI-tag-only feedback pathway** (rejected in favour of structured engine-feedback/ directory). Activation warrant: if engine-feedback/ in self-dev accumulates <3 distinct feedback records over 10 sessions, reconsider collapsing to OI-tag per Reviser.
- **§10.4-M6 Outsider separate-prompt-files-operator-invoked** (rejected as over-fragmenting). Activation warrant: if MODE.md + fallback continues to produce dispatcher ambiguity beyond the Session 036 revision over 6 sessions, reconsider explicit operator-invoked separate prompt files.

**Q6 (WX-35-1 disposition)** — split decision, synthesiser-integrated direction: adopt **hybrid (b)+(c) per Synthesiser `[01C, Q6]` aligned with Outsider's forward convention `[01D, Q6]`**:

- **Forward convention (new)**: at session close, if close §1e narrative claims an OI file edit, the Case Steward must verify via `git log --oneline <path>` that the edit was actually committed. If verified, the narrative stands; if not verified, the narrative must explicitly state "claim retracted; file not edited this session". This is the Outsider's convention `[01D, Q6]` operationalised at session-close level. Add as minor amendment to `prompts/development.md` §Close, not engine-v-bumping on its own (per OI-002 heuristic — process discipline for close, not new normative content).
- **Incremental catch-up accepting past drift**: Session 036 does NOT retroactively backfill OI-004.md for Sessions 023–034. The 13-session gap remains visible in git history as a process scar per Outsider's "sometimes the honest artefact is the scar" reasoning `[01D, Q6]`.
- **Minimal Session 036 OI-004.md edit**: since Path PD is already a substantive engine revision (engine-v7), bundle a minimal OI-004.md catch-up note recording: (a) the Session 022 → Session 036 gap; (b) engine-v7 adoption without retroactive tally-narrative reconstruction; (c) operational tally values per SESSION-LOG rows as canonical. Per Outsider's "bundle a small note into the Session 036 revision if the engine files are already being changed" `[01D, Q6]`.
- **WX-35-1 watchpoint extension**: evaluation window 3 sessions post-close-convention adoption (Sessions 037/038/039) per Synthesiser `[01C, Q6]`.

## §6 First-class minority preservation (consolidated)

Per `multi-agent-deliberation.md` v4 §Synthesis (preserve dissent), the following minorities are preserved as §10.4 in `workspace-structure.md` v5 (new block) with full activation warrants per §5 above:

| ID | Source | Claim | Activation warrant summary |
|----|--------|-------|----------------------------|
| §10.4-M1 | Skeptic-preserver Q1 | No revision warranted to §Dispatch | 10-session zero-exercise → revert |
| §10.4-M2 | Skeptic-preserver Q2 | Feedback pathway premature | 10-session zero-inbox → retro-vindicate |
| §10.4-M3 | Reviser Q1 | Pure structural-signature dispatch | MODE.md burdensome across 3 workspaces → collapse |
| §10.4-M4 | Outsider Q1 | Pure MODE.md-authoritative dispatch | Structural-signature fallback ambiguous in practice → tighten |
| §10.4-M5 | Reviser Q2 | OI-tag-only feedback pathway | <3 feedback records in 10 sessions → collapse to tag |
| §10.4-M6 | Outsider Q5 | Separate prompt files (PROMPT-development.md + PROMPT-external.md) | Dispatcher ambiguity >6 sessions → split |

These six minorities bring total first-class engine minorities from 21 (Session 035 close) to 27 at Session 036 close. Minority status values on the 21 pre-Session-036 minorities unchanged.

## §7 OI-004 criterion-3 cross-lineage contributions from Outsider

Per MAD v4 §Closure Criteria for OI-004 criterion 3 (recorded impact), the following Outsider contributions from `[01D-perspective-outsider.md]` shaped synthesis decisions:

1. **Category-error framing**: *"A session log is an event record, not a mode declaration."* `[01D, Q1]` — This reframed the Q1 problem as mis-category rather than mis-heuristic. Shaped adoption toward MODE.md-authoritative + structural-signature-fallback hybrid rather than pure structural signature (Reviser's Direction 2).

2. **Critique of structural signature as accidental-layout-as-identity**: *"Structural signatures are tempting because they avoid another file, but they encode accidental layout as identity. That will fail again when a future workspace has both self-development material and application material for legitimate reasons."* `[01D, Q1]` — Load-bearing for rejecting Reviser's pure-Direction-2 proposal. Claude perspectives did not surface this latent ambiguity.

3. **Control-plane vs. evidence-plane distinction**: *"Dispatch is control-plane selection. Feedback is evidence-plane transfer."* `[01D, Q3]` — Reinforced the 4-of-4 convergence on independent mechanisms by naming why they should not be fused (architectural rather than merely pragmatic reason).

4. **Engine-feedback as upstream-issue-intake process**: *"Software projects distinguish between downstream bug reports, upstream patches, RFCs, incident reports, changelog entries, and issue trackers because they serve different evidentiary functions."* `[01D, Q2]` — Informed the structured `engine-feedback/` directory with outbox/inbox/triage separation per `[01D, Q2]` rather than OI-tag-only (Reviser) or prose-file (Synthesiser's light variant). External-input flagged per §5 constraint.

5. **Workspace-identity-file as distinct class from engine-definition file**: *"I would treat `MODE.md` as a required workspace file but not an engine-definition file copied identically across workspaces, because each workspace has distinct identity. The manifest should distinguish 'engine-definition files' from 'workspace identity files.'"* `[01D, Q4]` — This is a new conceptual category at engine-manifest level. Adopted in synthesis; reflected in `engine-manifest.md` §3 restructure for v7.

All five are cross-lineage-originated contributions that no Claude perspective independently produced and that shaped synthesis outcomes. This advances OI-004 criterion-3 cumulative tally by 5 data points (per Session 033 precedent for distinct-contribution counting). OI-004 voluntary:required advances from 11:9 → 12:9 (Outsider voluntary; d023_* not structurally required by MAD v4 §When Non-Claude Participation Is Required since PROMPT.md is not one of the four mandatory categories — but the session invited cross-family per operator directive and per Session 017/021/022/023/028/033 engine-v-bump precedent).

## §8 Limitations

Per MAD v4 §Limitations required content:

- **All four perspectives include three Claude-subagents (Reviser, Skeptic-preserver, Synthesiser).** Shared Claude training produces shared priors; convergence among them is weak evidence. The Outsider's cross-lineage contributions (§7) are what breaks the training-distribution correlation on this session.
- **The Outsider single-participant independence is weaker than a panel.** MAD v4 §Limitations warns: "A single non-Claude participant narrows OI-004 less than its presence suggests." Session 036 meets criterion 1 but does not provide multi-non-Claude diversity.
- **Brief-writing was Claude-family-authored.** Framing bias in the brief propagates to all four perspectives. The operator's pre-session framing of Q1 as "criterion-gap" may have primed all perspectives toward revision-as-answer; the Skeptic-preserver's no-revision dissent is preserved partly as a guard against this framing effect.
- **Synthesis is Claude-authored.** Citation discipline + quote-over-paraphrase + `[synth]` markers reduce but do not eliminate Claude-family synthesis risk.
- **Parallel isolation was realised via three separate Agent-tool subagent invocations for Claude subagents and one codex-exec invocation for Outsider.** Independence-preservation held: none of the four perspectives saw another's output during the independent phase. Verified via subagent-return-value inspection and codex session-id uniqueness.
- **One subagent (Skeptic-preserver) self-committed its perspective file to git before returning to the orchestrator.** This is an unexpected subagent behavior; the committed content is byte-identical to the assigned raw output (verified post-commit); no content integrity concern, but it is a transport-discipline anomaly noted in the Skeptic-preserver manifest's `transport_notes`.

## §9 Honest limits of this synthesis

- The `engine-feedback/` structure adopted is a simplification of Outsider's full proposal; specific subdirectory conventions (outbox/inbox/triage) are reduced to "intake + triage + INDEX.md" to bound Session 036 scope. Future sessions may re-introduce subdirectory structure if operational demand warrants; §10.4-M5 (Reviser OI-tag-only collapse) and §10.4-M6 are the opposite-direction activation warrants. This is a synthesis trade-off I am recording explicitly.
- The §Session-001 obligation text in §3d above assumes that new workspace initialisations will always happen via a fresh Session 001 that can create MODE.md before substantive work. The Session 036 adoption event for the existing self-development workspace is the one-time-per-workspace exception (created at close, not at Session 001). This one-time exception is recorded in the D-113 decision record.
- The WX-35-1 disposition bundles a minimal catch-up note into Session 036's OI-004.md edit (per §5 Q6 paragraph 4). This edit is the first OI-004.md edit since Session 022 (commit 2f2e70f). The git-log-verify forward convention catches future propagation; the 13-session narrative history is not reconstructed.
- No reference-validation.md edit required this session. Kernel §7 not touched. MAD v4 not touched. Validation-approach.md minor extension for check 23 if adopted; the extension is bounded and classified minor per OI-002 (new check is normative-content-addition borderline; given the simplicity of the check — presence + valid mode value — classify as minor per Session 033 D-108 Path L precedent for check 22 loop-bug repair; document in engine-manifest §7 v7 entry).

---

**Synthesiser attestation.** This synthesis was authored by the Case Steward (Claude Opus 4.7), distinct from the four deliberation perspectives. Citations are per `[raw-file, Q#]` convention. Synthesiser-original claims are marked `[synth]`. All four raw perspective outputs remain in place at `provenance/036-session-assessment/01[A-D]-perspective-*.md` with no post-submission edit (per MAD v4 §Synthesis quote-over-paraphrase). The Skeptic-preserver dissent on Q1 and Q2 is preserved at full strength per §6 above, not diluted.

**Next step.** Decide activity per `methodology-kernel.md` §5: D-113 (PROMPT.md §Dispatch revision + MODE.md creation), D-114 (engine-v6 → engine-v7 bump), D-115 (OI housekeeping + minority activation-clock + watchpoint advancement + eighth close-rotation + WX-33-1 evaluation + WX-35-1 disposition), D-116 (engine-feedback/ pathway + workspace-structure.md v5 §10.4 minority block + prompts/application.md + prompts/development.md + read-contract.md v4 updates).
