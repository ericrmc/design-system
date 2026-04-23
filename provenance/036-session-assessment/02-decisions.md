---
session: 036
title: Decisions — Path PD (PROMPT.md §Dispatch revision + engine-feedback pathway + engine-v7 bump + housekeeping)
date: 2026-04-23
status: complete
---

# Session 036 Decisions

Session 036 executes **Path PD** (operator-surfaced agenda; operator ratified via "Path PD. Extra reading: Any completed external applications (stored outside this workspace) may also have FEEDBACK about their execution or issues related to methodology or engine workings. There should be a clearly identified pathway for the operator to input this to inform internal development."). The operator's input expanded Path PD scope to cover both the dispatcher gap (§2a in `01-brief-shared.md`) and the feedback pathway (§2b). Four-perspective cross-family deliberation per MAD v4 schema: Reviser + Skeptic-preserver + Synthesiser (Claude subagents) + Outsider (OpenAI GPT-5.4 via `codex exec`). 3-of-4 cross-family convergence on Q1 and Q2 revision-warranted; 4-of-4 convergence on Q3 independent-mechanisms-same-session; 1-of-4 Skeptic-preserver dissent preserved as §10.4-M1 and §10.4-M2 first-class minorities.

See `provenance/036-session-assessment/01-deliberation.md` for synthesis.

---

## D-113: PROMPT.md §Dispatch revision (MODE.md authoritative + structural-signature fallback + §Session-001 obligation)

**Triggers met:** [d016_1, d016_2, d016_3]

**Triggers rationale:** d016_1 fires because D-113 modifies `methodology-kernel.md` — FALSE, D-113 does not modify kernel; REMOVE d016_1. Let me re-state accurately: d016_1 reads "modifies `methodology-kernel.md`"; D-113 does not modify the kernel. d016_2 fires ("creates or substantively revises any specification in `specifications/`") because D-113 substantively revises `PROMPT.md` — note D-113's primary edit target is `PROMPT.md` at workspace root, not a file in `specifications/`; strict reading of d016_2 would exclude. However, d016_2 has been read broadly in prior sessions to cover engine-definition file revisions (PROMPT.md is engine-definition per engine-manifest §3); following Session 017 D-074 precedent for PROMPT.md substantive revision firing d016_*. d016_3 fires because Q1 had multiple plausible positions (seven enumerated directions + no-revision) and perspectives genuinely disagreed. **Corrected triggers: [d016_2, d016_3]** (d016_1 does not apply; d016_4 not separately asserted).

**Triggers met (corrected):** [d016_2, d016_3]

**Decision:** Revise `PROMPT.md` §Dispatch to consult `MODE.md` at workspace root as the authoritative dispatch signal, with structural-signature fallback (presence of `applications/NNN-<slug>/brief.md` routes external-problem; presence of `provenance/001-genesis/` without any `applications/NNN-<slug>/brief.md` routes self-development), and narrowed operator-halt fallback only when both structural signatures fire or neither fires. Add new §Session-001 obligation requiring all new workspaces to create `MODE.md` at Session 001 before substantive work. Permit one-time retroactive post-hoc adoption for pre-existing workspaces via `marker_adopted_session:` frontmatter field (applied to this workspace at Session 036 close).

**Rationale:** 3-of-4 cross-family convergence on revision-warranted (Reviser + Synthesiser + Outsider) per `[01-deliberation.md, §3]`. The current external-problem branch criterion is a Session-001-only signature; leaving it unrevised means operator-halt fires on every external-application Session-002+ load (cost scales linearly in external-application session counts; cost of revision is bounded). Within the majority, Outsider's category-error framing (*"A session log is an event record, not a mode declaration"* `[01D, Q1]`) and cross-lineage critique of pure structural signature as *"encode accidental layout as identity"* `[01D, Q1]` shifted synthesis adoption away from Reviser's pure Direction 2 (structural-signature-only) toward the Synthesiser-layered hybrid (MODE.md authoritative + structural-signature fallback). The layering preserves the single-entry-point abstraction (avoiding Outsider's minority direction of separate prompt files per `[01D, Q5]`) while handling the steady-state dispatch for Sessions 002+ that motivated the operator's agenda.

**Rejected alternatives:**
- **Skeptic-preserver no-revision-warranted** per `[01B, Q1]`: preserved as first-class minority §10.4-M1 in `workspace-structure.md` v5 with activation warrant "if 10 sessions post-adoption the new dispatcher has been exercised zero times beyond the Session 036 self-dev adoption, retroactively vindicates premature adoption; reconsider reverting to pre-v7 form."
- **Reviser pure Direction 2 (structural signature only)** per `[01A, Q1]`: preserved as §10.4-M3 (activation on 3+ new-workspace MODE.md-inconsistency events).
- **Outsider pure Direction 1 (MODE.md-only; no structural fallback)** per `[01D, Q1]`: preserved as §10.4-M4 (activation on 2+ dispatcher-fallback ambiguity events within 6 sessions).
- **Direction 3 (SESSION-LOG frontmatter)**, **Direction 4 (separate prompt files per `[01D, Q5]`)**: Direction 4 preserved as §10.4-M6 (activation on dispatcher ambiguity >6 sessions post-adoption); Direction 3 not preserved as first-class minority (Outsider: "a log should remain a log"; no perspective argued strongly for it).

**Executed changes:** `PROMPT.md` substantively revised per §3d of `01-deliberation.md`; pre-v7 content preserved in git history at commit prior to Session 036 Path PD adoption (no PROMPT-v6.md physical file per Session 017 precedent). `MODE.md` created at workspace root with `mode: self-development` + `workspace_id: selvedge-self-development` + `created_session: 001` + `marker_adopted_session: 036` + `engine_version_at_marker_adoption: engine-v7`.

---

## D-114: engine-v6 → engine-v7 bump

**Triggers met:** [d016_2]

**Triggers rationale:** d016_2 fires because D-114 substantively revises `specifications/engine-manifest.md` (§2 version string + §3 heading + §3a new subsection + §4 exclusion-list update + §6 bootstrap-contract extension + §7 engine-v7 history entry). d016_1 does not fire (kernel not modified). d016_3 does not separately fire for D-114 (the engine-v bump mechanics are procedural, not substantively contested — 3-of-4 convergence on substantive-classification and v-bump in the Path PD deliberation); the underlying substantive disagreement was adjudicated in D-113 / D-116. d016_4 not asserted.

**Decision:** Advance engine-v6 to engine-v7 per `engine-manifest.md` §5 versioning discipline. Update §2 to name `engine-v7` as current; update §3 heading; add §3a "Workspace-identity files" subsection naming `MODE.md`; update §4 exclusion list to include `MODE.md` (workspace-identity), `engine-feedback/` (non-engine operator-managed), and v4-suffixed superseded specs; extend §6 bootstrap contract with MODE.md creation step (new item 4) and engine-feedback reverse-flow note; add §7 engine-v7 history entry documenting content-driven operator-agenda-driven bump.

**Rationale:** 3-of-4 cross-family convergence on substantive-classification under OI-002 heuristic per `[01-deliberation.md, §5 Q4]`. D-113 + D-116 substantively revise four engine-definition files (`PROMPT.md`, `workspace-structure.md`, `read-contract.md`, `engine-manifest.md`) plus two executable prompts (`prompts/development.md`, `prompts/application.md`). Per engine-manifest §5, "substantive revision to any file in §3" triggers engine-v bump. §5.4 Session 022 engine-v-cadence minority (activated-not-escalated) does NOT re-escalate per Session 028 D-096 / Session 033 D-107 content-driven-bump precedent — engine-v7 is the third consecutive content-driven bump (v5/v6/v7) all following preservation windows of varying length.

**Rejected alternatives:**
- Skeptic-preserver preferred-minimal-or-no-revision scope (per `[01B, Q4]`): if revision were text-only one-sentence clarification, classification might remain minor per OI-002 and no v-bump would fire. Majority rejected this scope in D-113 and D-116; v-bump follows from majority-scope classification.

**Executed changes:** `specifications/engine-manifest.md` edited in place (no v-suffix preservation — `engine-manifest.md` is itself the manifest; it carries its own v1 frontmatter and appends engine-v history in §7). Frontmatter `last-updated: 2026-04-23`, `updated-by-session: 036`.

---

## D-115: OI housekeeping + minority activation-clock + watchpoint advancement + eighth close-rotation + WX-33-1 evaluation + WX-35-1 disposition

**Triggers met:** [none]

**Single-agent reason:** Housekeeping per long precedent chain (D-077/D-091/D-093/D-097/D-099/D-101/D-103/D-105/D-108/D-110/D-112 all `[none]`-classified). OI-004 catch-up note bundled into this decision per Outsider's Q6 disposition (*"If `open-issues/OI-004.md` is touched for nearby reasons, add a minimal 'Session 036 catch-up note' rather than reconstructing thirteen sessions"* `[01D, Q6]`). Minority activation-clock advancements are mechanical per activation-warrant text; watchpoint data points are observational; close-rotation is mechanical per `read-contract.md` v4 §2c; WX-33-1 evaluation outcome follows directly from data points recorded.

**Decision:**

1. **OI-004 catch-up note added to `open-issues/OI-004.md`** per WX-35-1 hybrid (b)+(c) disposition. Records Session 036 voluntary-non-advancing-with-criterion-3-contribution (no d023_* trigger fires strictly per `multi-agent-deliberation.md` v4 enumeration — `PROMPT.md` + `workspace-structure.md` + `read-contract.md` + `engine-manifest.md` are not in the d023_1/d023_2/d023_3 list; `methodology-kernel.md` not touched; no OI-004 state change asserted). Tally **unchanged at 8-of-3** required. Voluntary:required advances from 11:9 to **12:9** (Session 036 is voluntary-non-advancing with five Outsider cross-lineage contributions shaping outcome). Criterion-3 cumulative advances from 69 to **74** per five contributions enumerated in `01-deliberation.md` §7. Canonical record for Sessions 023–034 remains SESSION-LOG.md rows + each session's `03-close.md` §1e narrative; this file's absence of state-history entries for Sessions 023–034 is acknowledged as process scar, not reconstructed.

2. **Minority activation-clock advancements**:
   - **§10.3 Skeptic-preserver minimal-revision (Session 033)**: Session 036 is third data point in 5-session rollback-evaluation window (Sessions 034–038). Session 036 adopts engine-v7 forward revision, not v6 → v5 rollback. **Third non-vindication-direction data point** (3-of-5; window continues through Session 038).
   - **§10.3 Outsider "Constraint-derivation probe" naming (Session 033)**: operational-watch continues. No external-reader misunderstanding event Session 036. No data point.
   - **§10.3 Reviser separate-OI-for-detection-gap (Session 033, WX-33-1 tracked)**: Session 036 is **third and final** data point in WX-33-1 3-session evaluation window (Sessions 034–036). Session 036 did not surface a material design question about cross-family-symmetric detection-mechanism gap that would have been easier to engage as dedicated OI. **Third non-vindication-direction data point (3-of-3); WX-33-1 evaluates to watchpoint-only-approach vindicated**; Reviser separate-OI-for-detection-gap minority does **not vindicate**. Its preservation continues for future reassessment if cross-family-symmetric pattern recurs.
   - **§5.11 Skeptic-preserver pressure-signal-audit (Session 028)**: no data point (no budget-firing event Session 036).
   - **§5.4 Session 022 engine-v-cadence**: activated-not-escalated; Session 036 engine-v7 bump does NOT re-escalate per D-096 / D-107 precedent; §5.4 status unchanged.
   - **Six new first-class minorities §10.4-M1 through §10.4-M6 preserved from Session 036 Path PD deliberation** per D-113 and D-116 adoption and `workspace-structure.md` v5 §10.4. See `01-deliberation.md` §6 and `workspace-structure.md` v5 §10.4 for full text. Activation warrants recorded.

3. **Watchpoint advancement**:
   - **WX-24-1 MAD growth**: MAD unchanged at 6,386 words. **15-session no-growth streak** at Sessions 023–036 inclusive. New longest in watchpoint history.
   - **WX-24-2 budget-literal drift**: no exercise Session 036; validator aggregate-report string literal "engine-v5 budget" persists as non-load-bearing formatting artefact (noted at Session 035 open; not fired).
   - **WX-24-3 Outsider pre-response workspace exploration**: n=6 stable at session open → **n=7 at Session 036 close** (Outsider perspective-participation in Session 036 Path PD deliberation continues the cross-family participation pattern).
   - **WX-27-1 archive-token citation fragility**: no re-firing (third post-repair session boundary; structural repair at Session 033 D-108 Path L holds).
   - **WX-28-1 close-rotation-exception-frequency**: **eighth steady-state data point at zero exceptions** (0-of-8 in 10-session window). Two sessions (037/038) remain before cumulative evaluation at Session 038 close.
   - **WX-33-1 cross-family-symmetric detection-mechanism gap**: **third data point recorded in non-vindication direction; evaluation at Session 036 close: watchpoint-only-approach vindicated (0-of-3 surfaced design-question events across Sessions 034/035/036)**. The Reviser separate-OI-for-detection-gap minority from Session 033 §10.3 does not vindicate. Watchpoint continues as forward observation for potential future cross-family-symmetric patterns.
   - **WX-33-2 reference-validation.md v3 per-file soft-warn**: stable at 7,160.
   - **WX-34-1 SESSION-LOG.md row-verbosity**: Session 036 is second-of-3 evaluation data point. Session 036 close row will be substantive-length (engine-v-bump session per Session 032/033 precedent); discipline is to construct the row honestly without padding. Forward-discipline per Session 035 applies: restraint scopes to Path-A-shape rows, not substantive-session rows. Actual Session 036 row size to be measured at close.
   - **WX-35-1 OI-004.md state-history gap**: **disposition adopted Session 036 per hybrid (b)+(c) Synthesiser-Outsider direction**. Forward convention adopted in `prompts/development.md` §Close. OI-004.md catch-up note bundled into Session 036 (per this D-115). 13-session gap preserved as process scar (not reconstructed). Watchpoint continues: 3-session evaluation window Sessions 037/038/039 to verify the new forward convention holds.

4. **Eighth close-rotation steady-state rotation**: per `read-contract.md` v4 §2c, at Session 036 close Session 030 close rotates out of default-read; Session 036 close enters. Default-read holds at 19 close-files count unchanged. Physical paths unchanged. No retention-exception decisions recorded. Projected post-close aggregate reported at close per validator check 20.

5. **Minor housekeeping**: `open-issues/index.md` updated for Session 036 voluntary:required 11:9 → 12:9 + criterion-3 cumulative 69 → 74 on OI-004 row. OI-018 row status unchanged (§5.4 not re-escalated at engine-v7 per D-114 §7 entry). Per this D-115's git-log-verify discipline applied at close: `index.md` edit will be git-log-verified before close-commit.

**Rationale:** Pure housekeeping per long precedent. No multi-agent deliberation required (not substantive; no activation warrant fires on the housekeeping itself). The bundling of OI-004 catch-up note is per Outsider's explicit Q6 direction `[01D, Q6]`; the minority activation-clock data points are mechanical.

**Rejected alternatives:**
- Standalone WX-35-1 disposition session (Reviser `[01A, Q6]` preferred): rejected per Outsider bundling-suggestion + Synthesiser integrative proposal; bundling into Session 036 housekeeping is efficient and does not violate anti-laundering because the session is already substantive for other reasons.

---

## D-116: engine-feedback/ pathway + workspace-structure.md v5 + read-contract.md v4 + prompts/application.md + prompts/development.md

**Triggers met:** [d016_2, d016_3]

**Triggers rationale:** d016_2 fires because D-116 substantively revises `workspace-structure.md` (v4 → v5), substantively revises `read-contract.md` (v3 → v4), and adds §engine-feedback normative specification to workspace-structure.md (all specification-scope). d016_3 fires because Q2 had multiple plausible shapes (OI-tag-only per Reviser; prose-file-section per Synthesiser; structured outbox/inbox/triage per Outsider; premature-do-nothing per Skeptic-preserver) and perspectives genuinely diverged on which. d016_1 does not fire (kernel unchanged). d016_4 not separately asserted.

**Decision:** Create `engine-feedback/` directory at workspace root with mode-dependent semantics (outbox in external workspaces; inbox+triage+INDEX.md in self-development workspace). Adopt Outsider-direction structured feedback record schema (feedback_id, source_workspace_id, source_session, created_at, reported_by, target, target_files, severity, status) with simplifications: no outbox subdirectory in external workspaces (feedback files placed directly under `engine-feedback/`); three subdirectories only in self-development side (`inbox/`, `triage/`, and `INDEX.md` as thin index). Add `INDEX.md` as conditional default-read in self-development mode per `read-contract.md` v4 §1 item 9. Add `engine-feedback/` specification section to `workspace-structure.md` v5 (replaces v4; §engine-feedback normative block + §file-classes extension + §top-level structure update + §Validation items 8 and 9). Add §Engine-feedback pathway clause to `prompts/application.md` instructing external-application agents on feedback intake. Add engine-feedback/INDEX.md read obligation to `prompts/development.md` §How to operate + file-edit-claim-discipline convention to §Close (for WX-35-1 forward discipline per D-115). Preserve `workspace-structure.md` v4 as `workspace-structure-v4.md` with `status: superseded`. Preserve `read-contract.md` v3 as `read-contract-v3.md` with `status: superseded`.

**Rationale:** 3-of-4 cross-family convergence on pathway-warranted per `[01-deliberation.md, §4]`. Outsider's upstream-issue-intake-process framing (with raw-intake / triage-ledger separation) is cross-lineage-originated and materially shaped adoption — Claude perspectives (Reviser OI-tag-only, Synthesiser light-file-section, Skeptic-preserver premature-do-nothing) did not produce the raw-vs-triage separation that allows the engine to preserve downstream context verbatim while still running self-development triage discipline per MAD v4 §Synthesis conventions. The simplifications from Outsider's full proposal (removing outbox subdirectory in external workspaces; reducing self-dev subdirectories to two + INDEX) bound Session 036 scope while preserving the critical architectural distinction (control-plane dispatch vs evidence-plane feedback per `[01D, Q3]`).

**Rejected alternatives:**
- **Skeptic-preserver premature-feedback-pathway** per `[01B, Q2]`: preserved as §10.4-M2 (activation warrant: 10-session zero-inbox → retroactively vindicate).
- **Reviser OI-tag-only** per `[01A, Q2]`: preserved as §10.4-M5 (activation warrant: <3 feedback records in 10 sessions → collapse to tag).
- **Synthesiser application-close §feedback.md section** per `[01C, Q2]`: not preserved as first-class minority (partial overlap with adopted direction's engine-feedback/ intake file; Synthesiser's proposal is a subset of the adopted structured approach).
- **Outsider full outbox/inbox/triage structure with subdirectories in external workspace side** per `[01D, Q2]`: adopted with simplification (single-level engine-feedback/ in external; subdirectories only in self-development); Outsider's full proposal is the adopted direction's over-structure limit; not preserved as separate minority (adopted substantively; simplifications are scope-bounding per D-113 + D-114 session-scope discipline).

**Executed changes:**
- `engine-feedback/` directory created at workspace root with `inbox/` + `triage/` subdirectories + `INDEX.md` thin-index.
- `specifications/workspace-structure.md` v4 → v5: §Purpose notes v5 additions; §File classes extended to four classes (workspace-identity added); §Top-level structure updated with MODE.md + engine-feedback/; §MODE.md added; §engine-feedback added; §Validation extended with items 8 + 9; §10.4 first-class-minority block added preserving six Session 036 Path PD minorities.
- `specifications/workspace-structure-v4.md` created as copy of pre-Session-036 `workspace-structure.md` content with frontmatter updated to `status: superseded` + `superseded-by: workspace-structure.md v5`.
- `specifications/read-contract.md` v3 → v4: §1 item 0 added (MODE.md default-read); §1 item 9 added (conditional engine-feedback/INDEX.md); §10 versioning extended with v4 entry.
- `specifications/read-contract-v3.md` created as copy of pre-Session-036 `read-contract.md` content with frontmatter updated to `status: superseded` + `superseded-by: read-contract.md v4`.
- `prompts/application.md` updated with §Engine-feedback pathway clause.
- `prompts/development.md` updated with engine-feedback/INDEX.md read obligation in §How to operate + file-edit-claim-discipline convention in §Close.
- `tools/validate.sh` extended with check 23 (MODE.md presence + mode-value verification).

---

## Session 036 validator state

Pre-session (Session 036 open): 828 pass / 0 fail / 3 warn PASS.

Projected at close (per validator run after all decisions executed prior to this commit): approximately 852 pass / 0 fail / 3 warn PASS. Three designed soft-warns persist (MAD v4 6,386; reference-validation v3 7,160; SESSION-LOG.md grows with Session 036 row — projected 7,500–8,000 under 8K hard ceiling; discipline applied).

## Summary

| D | Title | Triggers | Files changed | Engine-v? |
|---|-------|----------|---------------|-----------|
| D-113 | PROMPT.md §Dispatch revision | [d016_2, d016_3] | PROMPT.md (substantive), MODE.md (created) | no-bump-on-its-own |
| D-114 | engine-v6 → engine-v7 | [d016_2] | engine-manifest.md (§2, §3, §3a added, §4, §6, §7) | **v6 → v7** |
| D-115 | Housekeeping + WX-33-1 evaluation + WX-35-1 disposition | [none] (Single-agent reason) | OI-004.md (catch-up note), open-issues/index.md | — |
| D-116 | engine-feedback pathway + workspace-structure v5 + read-contract v4 | [d016_2, d016_3] | workspace-structure.md (→v5), read-contract.md (→v4), prompts/application.md, prompts/development.md, tools/validate.sh (check 23), engine-feedback/INDEX.md (created) | bundled into D-114 |
