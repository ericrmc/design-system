---
session: 046
title: Decisions — S046 Path OS external-application bootstrap; single-orchestrator Case Steward; tools/bootstrap-external-workspace.sh produced + ancillary-tooling classification; tools/validate.sh minor bug fix (empty-provenance robustness + ls-glob set-e guard); auto-memory disabled for this workspace per operator directive; OI-019 sub-question (f) cross-linkage; engine-v7 preserved (preservation window count 10 new longest extended further)
date: 2026-04-24
status: complete
---

# Decisions — Session 046

## D-142: Bootstrap first external-application workspace at `/Users/ericmccowan/Development/selvedge-disaster-response/`; classify `tools/bootstrap-external-workspace.sh` as ancillary tooling (not engine-definition)

**Triggers met:** [none]

**Triggers rationale:** No engine-definition spec file is edited by this decision. The new bootstrap script is classified as ancillary tooling (see §Classification below), so it is not added to `engine-manifest.md` §3 and does not bump engine-v. No OI state transitions; no minority preservation; no read-contract revision; no kernel revision. The decision executes the already-specified `engine-manifest.md` §6 bootstrap contract end-to-end for the first time; the specification governing the work existed before this decision and is unchanged by it.

**Single-agent reason:** Infrastructure build-work on already-spec'd pathways, not spec revision. Engine-manifest.md §6 (engine-v7) names the 8-step bootstrap contract; `prompts/application.md` (engine-v1, extended S022 + S036) is the template; `MODE.md` workspace-identity convention (S036 D-113) is the schema; `workspace-structure.md` v5 §engine-feedback (S036 D-116) is the feedback pathway. None of this work requires deliberation on contested or under-determined questions. MAD v4 §When Multi-Agent Deliberation Is Required triggers are not met: no kernel §7 modification; no substantive MAD revision; no VA revision; no OI-004 state change; no reference-validation Cell 1; no engine-v bump proposal. D-133 M2 Convene-time role/lineage matrix does not apply (no perspectives convened); second-of-3 verification exercise carries forward to the next self-dev MAD session. Operator explicitly ratified single-orchestrator at Halt 1.

**Decision:**

1. **Architecture.** The disaster-response scenario candidate is run as an **external-problem application** in a **separate workspace** at `/Users/ericmccowan/Development/selvedge-disaster-response/`. This is the first genuine end-to-end exercise of `engine-manifest.md` §6 and the first use of `prompts/application.md` from a workspace other than the self-development source.

2. **Workspace bootstrapped this session.** `tools/bootstrap-external-workspace.sh` executed with target `/Users/ericmccowan/Development/selvedge-disaster-response/`, slug `disaster-response`, workspace id `selvedge-disaster-response`. Engine-v7 was derived from this workspace's `specifications/engine-manifest.md` §2 and written into the new workspace's `MODE.md` frontmatter at `engine_version_at_creation: engine-v7`. `MODE.md` carries `mode: external-problem` + `application_brief: applications/001-disaster-response/brief.md`. Engine-definition files copied flat per §3 (12 files: `PROMPT.md`, `prompts/development.md`, `prompts/application.md`, eight active specifications, `tools/validate.sh`). Superseded spec versions were NOT copied per §4. The new workspace's `validate.sh` smoke test passed post-fix (see D-143): 22 PASS / 0 FAIL / 3 WARN / Result PASS.

3. **Ancillary-tooling classification.** `tools/bootstrap-external-workspace.sh` is classified as **ancillary tooling**, not engine-definition. Rationale: engine-definition files are what sessions **load** to execute the methodology (per `engine-manifest.md` §3 enumeration and §1 "loading the engine means having these files available"). The bootstrap script is what the operator **runs once** to initialise a new workspace; it does not participate at session load time. Adding it to engine-manifest.md §3 would bump engine-v8 without evidence warranting the classification. Precedent: `tools/validate.sh` IS engine-definition because it runs each session; no other tools files exist at S045. S046 is the first post-validate.sh tools/ file and sets the classification default for future ancillary tools.

4. **Not copied into external workspaces.** Per §3 classification, the bootstrap script is NOT copied by itself. External workspaces that later need to spawn further workspaces must copy the script manually from a self-development source workspace. This preserves the per-§3 "copy-flat" contract without expanding it.

5. **Brief stub created; operator populates before Session 001.** `applications/001-disaster-response/brief.md` in the new workspace carries `<<slot>>` placeholders mirroring `prompts/application.md` §This application's context. The operator replaces each placeholder with scenario-specific content between this session's close and Session 001 of the external workspace. Session 001 Reads the populated brief per its own Read activity.

6. **First engine-feedback outbox bootstrapped.** `engine-feedback/outbox/README.md` was created in the new workspace, naming the schema from `workspace-structure.md` v5 §engine-feedback for the first time in a live external workspace. §10.4-M5 (Reviser OI-tag-only feedback pathway) observational window continues; first feedback record (if any) originates from Session 001+ of the new workspace.

**Forward observations feeding D-146 housekeeping:**

- Path OS has now been the path for S036 / S043 / S044 / S045 / S046 (five of the last eleven sessions). "Path OS" is broadening: S036 deliberative-two-scope, S043 deliberative-one-scope, S044 operator-corrective, S045 deliberative-two-observations, S046 operator-ratified build-work. Sub-class discrimination (e.g., Path OS-D deliberative vs. Path OS-B build) may become useful. Not proposing taxonomy now; flagging for forward observation.
- Session 046 is the **first post-D-138 folder-name default exercise** (`046-session`, no `-assessment` suffix, no slug). First data point on whether the new default scales cleanly across session classes. No operational friction observed.

---

## D-143: Minor bug fix to `tools/validate.sh` — empty-provenance robustness + `ls`-glob `set -e` guard (discovered during D-142 bootstrap smoke test)

**Triggers met:** [d016_3]

**Triggers rationale:** `d016_3` is the minor-update-to-existing-engine-definition-file trigger per MAD v4 recognised-identifier set. `tools/validate.sh` is engine-definition per `engine-manifest.md` §3; this decision edits it with no semantic change to what the checks validate (only pre-Session-001 empty-workspace edge-case robustness). Classified **minor** per OI-002 heuristic — bug-fix with no semantic change — matching direct precedent S030 D-100 (`workspace-structure.md` §SESSION-LOG stale-literal cleanup) and S033 D-108 (check 22 loop-bug repair). No engine-v bump per `engine-manifest.md` §5 ("typo corrections … do not increment engine version"; analogous to bug-fix-without-semantic-change here).

**Single-agent reason:** Bug fix discovered while running the bootstrap smoke test. The fix restores expected behaviour without changing what any check validates; deliberation would be out-of-proportion ceremony. Precedent S030 D-100 + S033 D-108 are both single-orchestrator minor validator edits.

**Decision:**

Two edits to `tools/validate.sh`, both defensive-coding hardening against empty-provenance-directory state (bootstrapped-but-pre-Session-001 external workspaces):

1. **`${provdirs[@]}` nounset guard.** Under `set -u` on Bash 3.2 (macOS default), referencing `"${provdirs[@]}"` when the array is empty errors with "unbound variable". All 12 unguarded `for dir in "${provdirs[@]}"` loops were changed to `for dir in ${provdirs[@]+"${provdirs[@]}"}` using the standard defensive idiom. Replace-all edit; no semantic change — the loops execute zero times on empty arrays as intended.

2. **Check 23 `ls`-glob + `basename` `set -e` guard.** In check 23 (MODE.md presence), `ls -d "$WORKSPACE_ROOT"/provenance/[0-9]*/ 2>/dev/null` exits with non-zero status when the glob has no matches (empty workspace), which kills the script under `set -e` despite `2>/dev/null`. Added `|| true` to both the `ls` and `basename` pipelines. Additionally, `current_session_num` is now normalised to `0` when empty or non-numeric (pre-Session-001 state), and the pre-adoption branch now **still verifies MODE.md** when the file is present — matching the bootstrap contract per `engine-manifest.md` §6 that MODE.md is required at Session 0 even though the session-number-based gate does not yet apply.

**Fix synchronised to bootstrapped external workspace.** The already-bootstrapped `/Users/ericmccowan/Development/selvedge-disaster-response/tools/validate.sh` was replaced with the fixed copy. Post-fix validator output on the new workspace: `Passed: 22 | Failed: 0 | Warnings: 3 | Result: PASS`. Self-dev validator unchanged in PASS/FAIL mix (the minor edits pass-through across 1063 existing checks).

**Forward observation.** Both bugs existed latent in self-dev's validate.sh but never fired because self-dev always has ≥1 provenance directory. The bootstrap exercise surfaced them on the first exposure to an empty-provenance workspace — demonstrating the "external application surfaces engine friction" model the §10.4-M2 observational window tracks. This session resolves the friction in self-dev directly; no engine-feedback outbox record is written because the external workspace has not yet opened Session 001 (there is no `source_session` to attribute). The discovery-and-resolution pattern is recorded here as §3 of `03-close.md` for future reference.

---

## D-144: Auto-memory disabled for this workspace per operator directive; `CLAUDE.md` amended

**Triggers met:** [none]

**Triggers rationale:** Workspace-level operator directive, not a spec change. No engine-definition file is edited. `CLAUDE.md` is neither engine-definition (per `engine-manifest.md` §3) nor development-provenance (per `workspace-structure.md` §3) — it is Claude Code harness configuration external to the engine. No OI state change; no trigger in the d016_*/d023_* namespace applies.

**Single-agent reason:** Direct operator instruction, no deliberation available or appropriate.

**Decision:**

1. **Memory files deleted.** Four files at `~/.claude/projects/-Users-ericmccowan-Development-complex-systems-engine/memory/` were deleted: `MEMORY.md`, `project_selvedge_engine.md`, `user_operator.md`, `reference_workspace.md`.

2. **`CLAUDE.md` amended with a `## Auto-memory disabled for this workspace` top-level clause.** The clause states that auto-memory is disabled, that the external memory directory is out-of-scope (no reads, no writes, no recreation), and that this instruction takes precedence over the system-prompt auto-memory guidance.

3. **All provenance lives in-workspace from S046 forward.** The in-workspace provenance files (`MODE.md`, `SESSION-LOG.md`, `open-issues/`, `specifications/`, `provenance/`, `engine-feedback/`, `CLAUDE.md`) remain the sole source of truth for future sessions.

**Spec-level recognition deferred.** The engine has no `specifications/memory-policy.md` and does not need one on present evidence. If future sessions find that the absence of a memory-policy spec produces operational friction (e.g., new agents starting to write to the memory directory despite CLAUDE.md), a spec amendment is a forward candidate.

---

## D-145: OI-019 cross-linkage — Session 046 external-application bootstrap is a data point on sub-question (f) extended-baseline visibility mechanism

**Triggers met:** [d009_1]

**Triggers rationale:** `d009_1` is the OI cross-linkage / per-OI amendment trigger. OI-019 (Path-selection work-channel and warrant-surface diversity, opened S043) sub-question (f) asks about "extended-baseline visibility mechanism periodic-vs-triggered-vs-narrow". The first exercise of external-workspace separation is a concrete mechanism by which long-horizon work can proceed without widening self-dev's §2c retention window — directly relevant evidence for sub-question (f).

**Decision:**

`open-issues/OI-019.md` is amended with a Session 046 cross-linkage entry recording:

- External-workspace separation is a mechanism for long-baseline scenario work (4–5 sessions, changing constraints) that does not require widening self-dev's 6-session retention window (§2c).
- The mechanism is orthogonal to retention-window tuning: external workspaces have their own §2c rotation, their own aggregate budget, and their own provenance; the self-dev window is unaffected by external-workspace session count.
- Implication for sub-question (f): "extended-baseline visibility" need not be a unified mechanism; separation of scenario-class work into application-specific workspaces is a structural alternative to retention-window tuning.
- Forward observation window: if the disaster-response scenario's 4–5 session arc completes without load-bearing cross-referencing back into self-dev from sessions older than 6, the external-workspace-separation mechanism is validated for 4–5-session scenario class; longer-arc work (10+ sessions) remains to test.

**Amendment scope.** `open-issues/OI-019.md` §Session 043+ activation triggers gains a short S046 entry. No other OI files are edited this session.

---

## D-146: Housekeeping — forward observations, engine-v disposition, close-rotation, verification-window advancements

**Triggers met:** [none]

**Triggers rationale:** No specification change; no OI state change other than the D-145 cross-linkage; no minority preservation. Housekeeping consolidates forward observations, watchpoint status, verification-window data points, and preservation-window disposition.

**Single-agent reason:** Aggregation of session-close bookkeeping.

**Decision:**

### §D-146a Engine-v disposition

**engine-v7 preserved.** Preservation window count at S046 close: **10** — **new longest engine-v preservation window extended further** (exceeding S045's 9). First engine-v to reach preservation depth 10 for any content class. No substantive engine-definition-file change this session. `validate.sh` edit is minor per D-143 classification and does not bump engine-v.

§5.4 Session 022 engine-v-cadence minority (activated-not-escalated) does NOT re-escalate; S046 is non-bump. Engine-v7 now preserves across five substantive-content sessions (S041 OI-004 closure, S043 Path PSD, S044 Path OC, S045 Path OS, S046 first external-application bootstrap) plus five non-substantive Path-A preservation sessions (S037, S038, S039, S040, S042).

### §D-146b D-129 third-of-3 verification exercise — vindication-side

S046 is the third-of-3 verification window session for D-129 (S043 adopted minor forward convention: default-agent session-open assessments MUST surface ≥1 considered-and-rejected non-Path-A alternative with one-sentence rationale). §5b of `00-assessment.md` surfaces **three** non-Path-A alternatives (Path A-pure watch / Path OS with MAD / Path OS-in-workspace) with non-vacuous rationales.

**Convention disposition: vindication-side third-of-3 → convention graduates to standing discipline.** Per D-129 text. All three verification-window sessions (S044, S045, S046) produced vindication-side evidence. §5.12 (Path-Selection Defender S043 preserve-position) reopen warrant (a) "D-129 convention degradation" does not fire; continues preserved with warrants armed.

### §D-146c D-133 M2 second-of-3 verification window — deferred (no MAD this session)

D-133 M2 Convene-time role/lineage matrix only fires when MAD is convened. S046 is single-orchestrator per D-142, so the second-of-3 verification exercise carries forward to the next self-dev MAD session. Verification window remains open: S047/S048/... until the next MAD session, which becomes second-of-3; subsequent MAD session becomes third-of-3. Timing is MAD-firing-dependent, not session-sequential.

### §D-146d Close-rotation

**Sixteenth close-rotation** at S046 close: S040 close (`provenance/040-session-log-preemptive-restructure/03-close.md`) rotates OUT of the default-read §2c 6-session retention window; S046 close enters. Post-rotation window: S041/S042/S043/S044/S045/S046. WX-28-1 seventeenth-of-N zero-retention-exceptions (vindicated pattern sustained; 18 consecutive rotations S029–S046 all zero).

### §D-146e Watchpoint and minority status

- **WX-24-1** (MAD word count): unchanged. No MAD amendment this session. 6,637 words stable. Fifth-of-N post-S042 reset observation; no-growth continues (new-record streak from S042 reset: 19-session no-growth streak tied with S045's record).
- **WX-24-3** (reference-validation label discipline): n=8 stable (no reference-validation Cell 1 this session).
- **WX-27-1**: thirteenth post-repair boundary holds.
- **WX-28-1**: 18-of-18 close-rotation zero retention-exceptions (see §D-146d).
- **WX-33-2**: stable at reference-validation.md v3 7,160 words.
- **WX-34-1**: standing discipline applied; substantive-row SESSION-LOG entry appropriate (Path OS first-external-application-bootstrap class + D-142/D-143/D-144/D-145 + engine-v7 preservation window count 10 new longest + auto-memory disabled + first `tools/` file added since S002).
- **WX-35-1**: standing discipline applied cleanly (see §1e of `03-close.md` for explicit file-edit claim retractions).
- **WX-43-1**: subagent self-commit cumulative unchanged (no subagents this session; n=6-of-8 at S045 close carries forward to next MAD session).
- **WX-44-1**: codex-CLI independence-phase breach observation unchanged (no codex invocation this session; n=2 at S045 close carries forward).
- **WX-44-2**: codex CLI model-version-drift discipline standing (no codex invocation this session).
- **First-class minorities engine-wide**: 31 at S046 close (unchanged from S045; no new minority; no discharge).

### §D-146f §10.4 observational windows

- **§10.4-M1/M2/M5** (Path PD S036 minorities): tenth-of-10 observational data point at S046 close per S045 §6 carry-forward. S046 produces:
  - **§10.4-M1 Skeptic-preserver no-revision-warranted on dispatcher**: MODE.md was **exercised for the first time outside self-dev** by the bootstrap writing `mode: external-problem`. No-revision position **not vindicated**; dispatcher revision served its purpose.
  - **§10.4-M2 Skeptic-preserver premature-feedback-pathway**: engine-feedback/outbox/ was **bootstrapped in a live external workspace** but no feedback record has flowed yet (the validate.sh bug fix was resolved in self-dev directly, not via outbox). Observational window at 10 closes without flow. Disposition: **continued preservation against future-event horizon** per S033 §10.3 5-session-window precedent extended to the §10.4 class; first feedback record would originate from Session 001+ of selvedge-disaster-response.
  - **§10.4-M5 Reviser OI-tag-only feedback pathway**: `engine-feedback/` in self-dev still accumulates zero records. Within 10 sessions post-adoption, zero records < 3-threshold from the minority's activation warrant. Per warrant text, "consider collapsing to OI-tag-only per Reviser's direction" — **activation-candidate**. However, the warrant is written against a period with no external applications in flight; S046 initialises one. Disposition: **continued preservation with activation-pending-on-selvedge-disaster-response-arc** — if that arc's 4–5 sessions produce zero feedback-outbox records AND zero-of-inbox throughput, Reviser's direction activates at the arc's close.
- **§10.4-M3/M4/M6** (Path PD S036 dispatcher-alternative minorities): unchanged; window thresholds not met.

### §D-146g Aggregate budget at close

Aggregate default-read surface post-close-rotation projected under soft 90K / hard 100K. Concrete measurement recorded in `03-close.md` §1f after SESSION-LOG.md row append.

### §D-146h OI-002 data point count

No spec edit this session classified minor or substantive (validate.sh edit is minor per D-143 but the classifier pattern is tooling-not-spec — OI-002 tracks spec-revision classification specifically). OI-002 data-point count unchanged at 15 from S045.

### §D-146i Forward observations (carry-forwards for S047+)

- **Operator populates brief + opens Claude Code in selvedge-disaster-response/**. Session 001 of the external workspace is a separate Claude Code invocation. S047 of self-dev will re-orient at session-open and triage any engine-feedback/inbox/ arrivals.
- **D-129 convention graduated to standing discipline**. S047+ default-agent assessments continue surfacing non-Path-A alternatives.
- **D-133 M2 verification window carries forward**. Second-of-3 exercise at next self-dev MAD session.
- **WX-43-1 n=6-of-8 threshold met** carries forward to next MAD session for OI-promotion evaluation.
- **WX-44-1 n=2 carries forward**; n=3 at a future MAD session would fire S047 close OI-promotion candidate per S045 §D-141d forward observation.
- **§10.4-M5 activation-pending on disaster-response arc**. Next-action evaluation at the close of that arc (external workspace Sessions 001–005 approximate).
