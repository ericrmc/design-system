---
title: Engine Manifest
version: 1
status: active
created: 2026-04-22
last-updated: 2026-04-24
updated-by-session: 048
supersedes: none
---

# Engine Manifest

## Purpose

This specification names what constitutes the **Selvedge engine** at any given engine version. The engine is the current loadable implementation of the Selvedge methodology (per `identity.md` v2 layered denotation): a file set that, when loaded together, executes the methodology's nine-activity process against an application's context. The manifest makes the engine pointable-at, versionable, and cleanly separable from the workspace's own development-provenance.

Created Session 017 per D-074 as the resolution of OI-017 (engine-vs-methodology reframing). Its minimal scope is deliberate: the manifest enumerates and declares invariants, but does not restate the content of the specifications it enumerates.

## Specification

### 1. Engine definition

The **Selvedge engine** is the current loadable implementation of the Selvedge methodology, consisting of the file set enumerated in §3 at the engine version named in §2. Loading the engine means having these files available and treating them as a closed unit for the purposes of executing a session.

The engine is distinct from:
- The **methodology** — the abstract-approach, domain-general mechanic that the engine realises (named "Selvedge" per `identity.md` v2).
- The **development-provenance** — the self-development application's own accumulated reasoning trail (`SESSION-LOG.md`, `open-issues.md`, `provenance/`).
- Any **specific application** — a particular run of the engine against a problem (self-development or external-problem).

### 2. Current engine version

**`engine-v8`** (established Session 048 per D-154).

Subsequent engine versions (`engine-v9`, `engine-v10`, ...) increment per the versioning discipline in §5. The current engine version is always named by this §2.

### 3. Engine-definition files at `engine-v8`

The following files constitute the engine at the current version:

| File | Role |
|------|------|
| `PROMPT.md` | Thin dispatcher: names the three layers and two operating modes; points to `prompts/development.md` and `prompts/application.md`. |
| `prompts/development.md` | Executable prompt for the self-development application (this workspace's entry point). |
| `prompts/application.md` | Template prompt for external-problem applications (loads the engine by reference to this manifest; specifies application-context slots). |
| `specifications/methodology-kernel.md` | Kernel: defines the nine-activity execution semantics. |
| `specifications/multi-agent-deliberation.md` | Defines multi-perspective deliberation triggers, non-Claude participation, recording schema. |
| `specifications/validation-approach.md` | Two-tier validation: structural checks and guided-assessment questions. |
| `specifications/workspace-structure.md` | Defines file classes, top-level structure, provenance conventions. |
| `specifications/identity.md` | Records the name Selvedge and the three-layer denotation. |
| `specifications/reference-validation.md` | Defines reference-validation as the third sense of validation. |
| `specifications/read-contract.md` | Defines the access discipline: default-read surface vs archive surface (v1, added engine-v3). |
| `specifications/engine-manifest.md` | **This file.** |
| `tools/validate.sh` | Executable: runs the Tier 1 structural checks from `validation-approach.md`. |

An external-application workspace that clones the engine should copy (or reference) these files and nothing else from the source workspace.

### 3a. Workspace-identity files (added engine-v7)

Workspace-identity files are per-workspace identity declarations distinct from engine-definition files. They are **required by the engine** (the dispatcher consults them) but are **not copied byte-identically** across workspaces — each workspace writes its own content at initialisation.

At `engine-v7`:

| File | Role |
|------|------|
| `MODE.md` | Workspace mode marker declaring `mode: self-development | external-problem` and workspace identity metadata. Consulted by `PROMPT.md` §Dispatch as authoritative signal (with structural-signature fallback). Created at Session 001 of any new workspace per `PROMPT.md` §Session-001 obligation. See `specifications/workspace-structure.md` §MODE.md for schema. |

The workspace-identity-file class is the Outsider's frame-completion contribution at Session 036 Path PD per `provenance/036-session-assessment/01D-perspective-outsider.md` Q4, recorded as an OI-004 criterion-3 data point.

External application workspaces create their own `MODE.md` during Session 001 initialisation per §6 bootstrap contract below.

### 4. What is explicitly NOT part of the engine

The following are development-provenance, application-scope, or workspace-identity; they are **not** copied byte-identically when an external application initialises the engine, though some (notably `MODE.md`) are required to exist:

- `MODE.md` (workspace-identity; each workspace writes its own content per §3a)
- `SESSION-LOG.md` (development-provenance)
- `open-issues/` (development-provenance)
- `provenance/` (development-provenance: all session records)
- `applications/NNN-*/` (application-scope: prior application outputs, not reusable as engine load)
- `engine-feedback/` (non-engine operator-managed; optional; see `workspace-structure.md` v5 §engine-feedback)
- `specifications/*-v1.md`, `*-v2.md`, `*-v3.md`, `*-v4.md` (superseded spec versions: preserved in the workspace but not active engine definition)

This manifest's own version history is also not part of the engine load; the current `engine-manifest.md` is what counts.

### 5. Versioning discipline

The engine version (`engine-v1`, `engine-v2`, ...) increments when any file in §3 changes in substance. "In substance" means:

- A new engine-definition file is added to §3.
- An existing engine-definition file receives a substantive revision (v-bump per the spec-revision discipline in `workspace-structure.md`).
- An engine-definition file is removed or superseded.

The engine version does **not** increment on:
- Typo corrections or formatting adjustments.
- Minor elaborations within an existing spec's scope (per the OI-002 substantive-vs-minor heuristic).
- Updates to development-provenance or application-scope files.
- Changes to `SESSION-LOG.md`, `open-issues.md`, or `provenance/`.

Engine-version increments are declared by a decision record in the session that executes the increment. The decision names the file(s) changed and the new engine version.

### 6. Loading the engine / minimal external-application initialisation contract

An external application workspace is initialised by:

1. **Copy the engine-definition file set** (§3) into a fresh directory (or reference them from a canonical engine repository). The copy is flat: maintain the same paths (`PROMPT.md`, `prompts/`, `specifications/`, `tools/`).
2. **Create fresh development-provenance files** in the new workspace:
   - Empty `SESSION-LOG.md` (header only).
   - Empty `open-issues/index.md` (header only) and `open-issues/` directory.
   - Empty `provenance/` directory.
3. **Create the first application directory** `applications/001-<slug>/` containing at minimum a `brief.md` carrying:
   - The problem statement.
   - Constraints (domain constraints; time constraints; stakeholder constraints).
   - Stakeholders (who holds the problem; who will receive the artefact; who validates).
   - Success condition (what the artefact must do for the application to be considered successful).
4. **Create the workspace-identity file `MODE.md`** at workspace root per `workspace-structure.md` v5 §MODE.md and `PROMPT.md` §Session-001 obligation. For external-problem applications the frontmatter carries `mode: external-problem` + `workspace_id` + `created_session: 001` + `engine_version_at_creation` + `application_brief: applications/001-<slug>/brief.md`.
5. **Optionally create `engine-feedback/`** at workspace root for outbox-mode feedback accumulation during the application's lifetime. The directory is optional at Session 001 and may be created later when the first feedback record is written.
6. **The execution prompt is selected by the dispatcher** per `PROMPT.md` §Dispatch. With `MODE.md` present and `mode: external-problem`, the dispatcher loads `prompts/application.md` automatically; no manual prompt-selection copy is required.
7. **Record the engine version loaded.** The first session's provenance (e.g., `provenance/001-*/00-assessment.md`) should name the engine version (`engine-v7` or later) the workspace was initialised from. This record complements the `engine_version_at_creation` value in `MODE.md`.
8. **Run Session 001** per the loaded execution prompt. The session Reads the application's initial state (the `brief.md` + the engine specifications), Assesses what the application's first increment should be, Convenes perspectives, Deliberates, Decides, Produces the first artefact or design fragment, Validates, Records, and Closes.

The critical rule per Outsider [Session 017 01d Q6]: **external application workspaces inherit the engine, not the engine's autobiography.** The development-provenance of the Selvedge engine's own development is preserved in this source workspace; it does not travel with the engine to an external application.

Engine-feedback flows in the **reverse direction** from this bootstrap: an external application may produce feedback about the engine/methodology during its execution; such feedback flows operator-mediated from the external workspace's `engine-feedback/` (outbox role) back into the self-development source workspace's `engine-feedback/inbox/` for triage. This reverse flow is specified in `specifications/workspace-structure.md` v5 §engine-feedback. It is distinct from the forward bootstrap above.

### 7. Engine version history

- **`engine-v1`** — established Session 017 via D-074. First versioned engine definition. File set per §3. Corresponds to the post-Session-017 state of the workspace: `methodology-kernel.md` v4 + scope-clarification sentence; `multi-agent-deliberation.md` v3 + minor scope-applicability sentence; `validation-approach.md` v3 + minor scope-applicability sentence; `workspace-structure.md` v3; `identity.md` v2; `reference-validation.md` v1; `tools/validate.sh` as of Session 005/006 last substantive change; `PROMPT.md` as thin dispatcher; `prompts/development.md` and `prompts/application.md` as created by D-074. Subsequent intra-engine-v1 changes (Session 019: `reference-validation.md` v1 → v2; Session 020: `workspace-structure.md` v3 minor amendment) did not bump the engine version because v3 minor amendments do not trigger §5 bump per OI-002 heuristic.

- **`engine-v2`** — established Session 021 via D-082. Substantive revisions to three engine-definition files: `multi-agent-deliberation.md` v3 → v4 (added §Criterion-4 Articulation for OI-004; §Acceptable Participant Kinds for OI-004; six new Layer 2 manifest fields; one new synthesis frontmatter field; one new session-level participants.yaml block; four-state OI-004 lifecycle with §Closure Procedure for OI-004); `validation-approach.md` v3 → v4 (added §Tier 2 Q8; documented gating conventions for new checks 16-19); `tools/validate.sh` substantive update (added checks 16, 17, 18, 19; added CRITERION4_ARTICULATION_SESSION constant; added PARTICIPANT_ORGANISATION_CLOSED_SET constant; added Tier 2 Q8 print-out). v3 of the two specs preserved as `multi-agent-deliberation-v3.md` and `validation-approach-v3.md` (both `status: superseded`). All other engine-definition files unchanged at engine-v2 boundary: `PROMPT.md`, `prompts/development.md`, `prompts/application.md`, `methodology-kernel.md` v4, `workspace-structure.md` v3, `identity.md` v2, `reference-validation.md` v2, `engine-manifest.md` (this file, frontmatter `last-updated: 2026-04-22` + `updated-by-session: 021`).

- **`engine-v3`** — established Session 022 via D-084. First engine-v-bump to add a new engine-definition file: `specifications/read-contract.md` v1 (new; defines default-read surface vs archive surface access discipline). Substantive revisions to multiple engine-definition files: `methodology-kernel.md` v4 → v5 (§1 Read revised to name default-read vs archive distinction); `workspace-structure.md` v3 → v4 (substantive — adds `open-issues/` directory replacing `open-issues.md` file per v3 split-authorisation clause; adds archive-pack subdirectory convention; cross-references to read-contract.md; SESSION-LOG.md text restored to thin-index form); `validation-approach.md` v4 → v5 (added §Tier 2 Q9 for read-contract adherence; documented gating conventions for new checks 20, 21, 22); `tools/validate.sh` substantive update (added checks 20, 21, 22; added READ_CONTRACT_ADOPTION_SESSION, DEFAULT_READ_HARD_WORD_CEILING, DEFAULT_READ_SOFT_WORD_CEILING constants; added Tier 2 Q9 print-out). Substantive revisions to prompts: `prompts/development.md` lines 19, 25, 43 revised for read-contract discipline; `prompts/application.md` analogous Read-section revision for external-application consistency. v4 of the two revised specs preserved as `methodology-kernel-v4.md`, `workspace-structure-v3.md`, `validation-approach-v4.md` (all `status: superseded`). All other engine-definition files unchanged at engine-v3 boundary: `PROMPT.md` (thin dispatcher unchanged), `multi-agent-deliberation.md` v4 (unchanged; cross-referenced from workspace-structure.md v4 and read-contract.md for provenance layout continuity), `identity.md` v2, `reference-validation.md` v2. Session 022 additionally performed retroactive migrations under the new read-contract: R8a SESSION-LOG.md restored to thin one-liner index; R8b `open-issues.md` split into `open-issues/` directory with per-OI files; R8c Session 014 Outsider perspective (96,651 words) archive-packed at `provenance/022-workspace-scaling-trajectory/archive/014-oi016-outsider/`; R8c' Session 022's own Outsider raw (22,611 words) archive-packed at session close. Mempalace R3 `CLAUDE.md` paragraph removed per E.1 (Session 020 §5.4 warrant trigger 1 satisfied; not engine-definition). Engine-v3 is the first engine-v-bump to introduce a new engine-definition spec file (beyond the original eleven at v1).

- **`engine-v4`** — established Session 023 via D-086. Substantive revision to one engine-definition file + substantive update to `tools/validate.sh`: `read-contract.md` v1 → v2 (§2 budget values recalibrated 15,000 → 8,000 hard and 10,000 → 6,000 soft per empirical 3.0× tokens-per-word ratio correcting v1's 1.3× assumption; §2 Rationale rewritten; §2a aggregate default-read surface report added with advisory threshold ≥90,000 and activation threshold ≥100,000; §5.1/§5.2/§5.3/§5.5 minorities added; §10 versioning updated); `tools/validate.sh` constants `DEFAULT_READ_HARD_WORD_CEILING` 15000 → 8000 and `DEFAULT_READ_SOFT_WORD_CEILING` 10000 → 6000; new aggregate reporter constants `DEFAULT_READ_AGGREGATE_ADVISORY=90000` and `DEFAULT_READ_AGGREGATE_ACTIVATION=100000`; check 20 output extended with aggregate report per §2a (informational not pass/fail/warn). v1 of read-contract.md preserved as `read-contract-v1.md` with `status: superseded`. All other engine-definition files unchanged at engine-v4 boundary: `PROMPT.md`; `prompts/development.md`; `prompts/application.md`; `methodology-kernel.md` v5; `multi-agent-deliberation.md` v4; `validation-approach.md` v5; `workspace-structure.md` v4; `identity.md` v2; `reference-validation.md` v2; `engine-manifest.md` (this file, documentary update per Session 021 sub-pattern). Engine-v4 is the second engine-v-bump in adjacent sessions (engine-v3 Session 022; engine-v4 Session 023) and the third in four sessions (engine-v2 Session 021; engine-v3 Session 022; engine-v4 Session 023). **Session 022 §5.4 Skeptic engine-version-cadence minority warrant activates at engine-v4 adoption:** "three engine-v-bumps in four adjacent sessions OR external-application portability confusion." Post-activation escalation trigger per Session 023 D-086 R9: any further engine-v-bump in Sessions 024/025/026 elevates §5.4 to substantive and forces a dedicated engine-manifest §5 revision deliberation in that session. OI-018 tracks this as an open issue for Session 024+. Known consequence of v4 adoption: `specifications/multi-agent-deliberation.md` at 6,403 words exceeds new 6,000-word soft warning and fires on adoption; this is designed soft-warning function per read-contract.md v2 §2; Session 024 responds per §8 remediation options. **Engine-v4 preserved across Sessions 024–027 (five consecutive non-bump sessions):** D-086 R9 automatic escalation window aged out at Session 026 close (three-of-three non-bump sessions across 024/025/026). §5.4 cadence minority status at Session 027 close: activated-not-escalated; reassessment at Session 028+ on content grounds alone. §5.3 aggregate-hard-budget minority activation warrant fires at Session 027 close (aggregate crosses 100,000-word threshold). §5.2 Skeptic no-change minority retroactively vindicated Session 027.

- **`engine-v5`** — established Session 028 via D-096. First engine-v-bump in response to a preserved minority's activation warrant firing (the §5.3 Pacer aggregate-hard-budget minority, preserved Session 023, activated Session 027). Substantive revision to one engine-definition file + substantive update to `tools/validate.sh`: `read-contract.md` v2 → v3 (§2b aggregate hard budget added at 100K hard / 90K soft; §2c close-rotation rule added at 6-session retention window; §1 item 7 revised from "every close" to "6 most recent closes"; §2a role clarified as informational sensor layer supplementing §2b budget enforcement; six new first-class minorities §5.6–§5.11 preserved with activation warrants; §10 versioning updated); `tools/validate.sh` constants `AGGREGATE_BUDGET_ADOPTION_SESSION=28` (new), `DEFAULT_READ_AGGREGATE_HARD=100000` (new), `DEFAULT_READ_AGGREGATE_SOFT=90000` (new), `DEFAULT_READ_CLOSE_RETENTION_WINDOW=6` (new); check 20 default-read detection revised to apply close-rotation (most recent 6 sessions); check 20 aggregate-report promoted from informational to pass/fail/warn against new §2b budget at engine-v5; check 22 extended to accept rotated-close references of the form `[archive: provenance/<NNN-title>/03-close.md]` per read-contract.md v3 §2c. v2 of read-contract.md preserved as `read-contract-v2.md` with `status: superseded`. All other engine-definition files unchanged at engine-v5 boundary: `PROMPT.md`; `prompts/development.md`; `prompts/application.md`; `methodology-kernel.md` v5; `multi-agent-deliberation.md` v4; `validation-approach.md` v5; `workspace-structure.md` v4; `identity.md` v2; `reference-validation.md` v2; `engine-manifest.md` (this file, documentary update per Session 021/023 sub-pattern).

Engine-v5 is the fourth engine-v-bump overall (v2 Session 021; v3 Session 022; v4 Session 023; v5 Session 028) and the first after a five-session preservation window (024–027 non-bump sessions). The bump is content-driven: the §5.3 activation warrant fired at Session 027 close, and Session 028 deliberation (3-of-4 cross-family convergence including Outsider) adopted aggregate hard budget at revised values. §5.4 Session 022 cadence minority does not re-escalate at this bump — R9 automatic escalation window aged out Session 026, and the bump follows a five-session preservation window, reflecting the engine's capacity for both restraint and necessary revision. OI-018 remains open; Session 028 does not engage engine-manifest §5 revision, per 3-of-4 convergence to keep cadence question separate (see `provenance/028-session-assessment/01-deliberation.md` §5b).

- **`engine-v6`** — established Session 033 via D-107. Second engine-v-bump in response to a preserved minority's activation warrant firing (the Session 014 §10.1 Skeptic "provisional substitute" framing minority, preserved Session 014 in `reference-validation.md` v1 §10, activated Session 032 per `reference-validation.md` v2 §9 trigger 7 firing at Session 032 PD-A REJECT). Substantive revisions to two engine-definition files: `methodology-kernel.md` v5 → v6 (§7 third-sense rename "Reference validation" → "Provisional reference substitute"; one-sentence mandatory-dissent citation-discipline principle added to §7 pointing to `reference-validation.md` §8 for operational detail; scope-statement paragraph strengthened with saturation-profile-dependent evidential-value language, cross-family-symmetric carve-out, MAY/MUST NOT/MUST citation-discipline modals, methodology-level vs methodology-consistent distinction; grandfather clause for pre-v6 `reference-validated` labels); `reference-validation.md` v2 → v3 (rename-sync of sense terminology throughout; §1 C3 Stage (b) Condition 3 extended with sub-case 3a asymmetric-retrieval vs sub-case 3b cross-family-symmetric-reproduction; §4 L1b extended with sub-case recording for 3a/3b; §8 label renamed `validation: reference-validated` → `validation: reference-provisional` with grandfather clause; §8 mandatory-dissent three-element citation-discipline clause added with session-scoped sealing gate / frontmatter propagation / close-rotation check enforcement; §9 trigger 7 text refreshed with firing-event record and three re-fire conditions; §10 extended with three new Session 033 first-class minorities §10.3 Skeptic-preserver minimal-revision + §10.3 Outsider "Constraint-derivation probe" naming + §10.3 Reviser separate-OI-for-detection-gap). v5 of `methodology-kernel.md` preserved as `methodology-kernel-v5.md` with `status: superseded`; v2 of `reference-validation.md` preserved as `reference-validation-v2.md` with `status: superseded`. Minor (non-substantive) update to `tools/validate.sh` check 22 loop-bug repair per D-108 Path L (per-line-of-grep-rn with inner grep -oE concatenating multiple archive tokens → per-match via grep -HoE); classified minor per OI-002 heuristic (bug-fix with no semantic change to what check 22 validates; Session 024 D-088 R6 / Session 030 D-100 precedent). All other engine-definition files unchanged at engine-v6 boundary: `PROMPT.md`; `prompts/development.md`; `prompts/application.md`; `multi-agent-deliberation.md` v4; `validation-approach.md` v5; `workspace-structure.md` v4; `identity.md` v2; `read-contract.md` v3; `engine-manifest.md` (this file, documentary update per Session 021/023/028 sub-pattern).

Engine-v6 is the fifth engine-v-bump overall (v2 Session 021; v3 Session 022; v4 Session 023; v5 Session 028; v6 Session 033) and the second post-cadence-maturation content-driven bump (v5 was first). The bump is content-driven: `reference-validation.md` v2 §9 trigger 7 fired at Session 032 close, and Session 033 deliberation (3-of-4 cross-family convergence: Outsider GPT-5.4 + Reviser Claude + Synthesiser Claude; Skeptic-preserver Claude dissent preserved as §10.3) adopted the activated minority's direction per D-106 + D-107. §5.4 Session 022 cadence minority does not re-escalate at this bump — five-session preservation window (029/030/031/032 non-bumps; v6 at 033), content-driven rather than cadence-driven, and Session 028 D-096 3-of-4 convergence precedent holds (cadence question separate from substantive bump). OI-018 remains open; Session 033 does not engage engine-manifest §5 revision, per explicit preservation of the Session 028 precedent. This is the first engine-v-bump to execute a preserved-minority's pre-committed revision direction end-to-end (activation Session 032 → adoption Session 033); cf. Session 028 §5.3 conversion (preserved Session 023 → converted-to-active-spec Session 028) which was a threshold-adoption pattern rather than a minority-activation-adoption pattern.

**Key consequence at v6 adoption:** aggregate default-read surface is unchanged in direction (no new close-rotation event at v6; Session 033 close enters the 6-session retention window at close per §2c standard rotation). Projected post-close aggregate ~68–72K (Session 027 close rotates out; Session 033 substantive close enters). Well within §2b soft 90K / hard 100K ceilings.

- **`engine-v7`** — established Session 036 via D-114. **First engine-v-bump driven by an operator-surfaced agenda item** (as distinct from prior bumps driven by preserved-minority activation warrants or watchpoint firings). The operator surfaced at Session 036 open that `PROMPT.md` §Dispatch had a criterion-gap for external-problem Session-002+ workspaces (the "fresh / empty / near-empty" criterion is a Session-001-only signature), and additionally surfaced a second scope — the absence of a clearly identified operator-mediated feedback pathway from completed external applications back to self-development. Both scopes were addressed in a single Path PD four-perspective cross-family deliberation (Reviser + Skeptic-preserver + Synthesiser Claude-subagents; Outsider via OpenAI GPT-5.4 through `codex exec`). 3-of-4 cross-family convergence on revision-warranted for both Q1 (dispatcher) and Q2 (feedback pathway); 1-of-4 Skeptic-preserver dissent preserved as §10.4-M1 + §10.4-M2 first-class minority in `workspace-structure.md` v5. 4-of-4 convergence on "independent mechanisms, same session" for Q3 (Q1/Q2 relationship). Substantive revisions to four engine-definition files and two prompts:

  - `PROMPT.md` — §Dispatch rewritten to consult `MODE.md` as authoritative signal with structural-signature fallback; §Session-001 obligation added for new workspaces; §Engine-feedback pathway cross-reference added. (Pre-v7 content preserved in git history at commits prior to the v7 adoption commit; no PROMPT-v6.md physical file created per Session 017 precedent.)
  - `specifications/workspace-structure.md` v4 → v5 — adds `MODE.md` workspace-identity-file class and §MODE.md normative section; adds `engine-feedback/` directory with mode-dependent outbox/inbox/triage semantics and §engine-feedback normative section; adds §10.4 first-class-minority block preserving six Session 036 Path PD minorities. v4 preserved as `workspace-structure-v4.md` with `status: superseded`.
  - `specifications/read-contract.md` v3 → v4 — adds `MODE.md` to §1 default-read enumeration at new item 0; adds conditional `engine-feedback/INDEX.md` default-read clause at §1 item 9 (self-development mode, when file exists). No change to §2 per-file budget, §2b aggregate budget, §2c close-rotation, §4–§7 archive-pack mechanism. v3 preserved as `read-contract-v3.md` with `status: superseded`.
  - `specifications/engine-manifest.md` (this file) — §3 heading updated to `engine-v7`; §3a workspace-identity files subsection added naming `MODE.md`; §4 exclusion list updated; §6 bootstrap contract extended with MODE.md creation step and engine-feedback reverse-flow note.
  - `prompts/application.md` — adds §Engine-feedback clause instructing external-application agents to file feedback to `engine-feedback/` when methodology-level friction is observed.
  - `prompts/development.md` — adds read obligation for `engine-feedback/INDEX.md` at session open when the file exists; adds git-log-verification convention for claimed OI-file edits per WX-35-1 forward discipline (see §Close).

  Minor updates (non-engine-v-bumping on their own but bundled into the v7 adoption): `tools/validate.sh` gains **check 23** verifying `MODE.md` presence at workspace root with recognised `mode:` value (self-development enforcement only at this session; external-workspace validation extensions deferred to Session 037+); `open-issues/OI-004.md` receives a minimal catch-up note per WX-35-1 Q6 disposition (b+c hybrid) recording the Session 022 → Session 036 unrecorded-edits gap + adoption of SESSION-LOG-row-canonical-with-forward-git-log-verification convention, without retroactive 13-session reconstruction.

  Workspace-identity file `MODE.md` created at workspace root for this self-development workspace (one-time post-hoc adoption per `PROMPT.md` §Session-001 obligation — `marker_adopted_session: 036` in frontmatter distinguishing retroactive from at-init creation).

  All other engine-definition files unchanged at engine-v7 boundary: `methodology-kernel.md` v6; `multi-agent-deliberation.md` v4; `validation-approach.md` v5; `identity.md` v2; `reference-validation.md` v3.

Engine-v7 is the sixth engine-v-bump overall (v2 Session 021; v3 Session 022; v4 Session 023; v5 Session 028; v6 Session 033; v7 Session 036). It is the third post-cadence-maturation content-driven bump (v5 + v6 + v7). §5.4 Session 022 engine-v-cadence minority (activated-not-escalated) does NOT re-escalate at this bump per Session 028 D-096 / Session 033 D-107 content-driven-bump precedent chain (cadence concern separates from substantive-bump classification). OI-018 remains open; Session 036 does not engage `engine-manifest.md` §5 revision.

Engine-v7 is the first engine-v-bump **driven by an operator-surfaced agenda item** rather than by preserved-minority activation warrant (v5 was §5.3 activation; v6 was §9 trigger 7 firing) or watchpoint firing. This represents a new class of substantive-revision provenance that the engine's discipline accommodates: operator-directed substantive revision co-deliberated through the multi-agent deliberation schema without bypassing the preservation and dissent-recording machinery. The Skeptic-preserver's no-revision dissent on both Q1 and Q2 is preserved as §10.4-M1 and §10.4-M2 with activation warrants that will retroactively vindicate premature-formalisation if the new mechanisms go unexercised for 10 sessions.

**Key consequence at v7 adoption:** aggregate default-read surface gains `MODE.md` (~200 words) and conditionally `engine-feedback/INDEX.md` (~100 words at adoption, thin-header). Close-rotation continues standard per §2c. Projected post-close aggregate well under §2b soft 90K. No close rotates out specifically for v7 adoption; Session 030 close rotates out at Session 036 close per standard rotation mechanics.

**Key consequence at v5 adoption:** aggregate default-read surface is reduced from 105,399 (pre-session) to approximately 55,000 (post-rotation) via Session 028 close-rotation first exercise. Sessions 002–022 `03-close.md` files (20 files, ~56,180 words) rotate to archive-surface by exclusion per revised §1 item 7. Files remain physically at their paths; the access-discipline category changes. Sessions 023–028 close files plus Session 028's own close (6 total) remain default-read per §2c 6-session retention window. Post-rotation aggregate well below both §2b soft (90K) and hard (100K) ceilings — comfortable forward headroom.

- **`engine-v8`** — established Session 048 via D-154. **First engine-v-bump driven by operator-directed resolution of an inbox engine-feedback record** (as distinct from prior bumps driven by preserved-minority activation warrants, `§9` trigger firings, watchpoint firings, or operator-surfaced-agenda mid-session deliberation). Operator-directed resolution of EF-001 (`engine-feedback/inbox/EF-001-read-contract-budget-scaling-for-domain-artefacts.md`; source_workspace_id `selvedge-disaster-response`, source_session 001) carried the `operator_directed_resolution` frontmatter field declaring the resolution direction as not-for-deliberation; Session 048 adopts that direction via single-orchestrator implementation. Substantive revision to one engine-definition file + minor clarification to one prompt:

  - `specifications/read-contract.md` v4 → v5 (substantive) — §1 gains a closing paragraph ("Applications directory clarification") making explicit that `applications/NNN-<slug>/` is outside the §1 closed enumeration and is read at session scope rather than at session-open-in-full; §2d new section codifying the per-file-budget carve-out for `applications/` + the chunked-read-on-demand mechanism (existing Read-tool `offset`/`limit` parameters) + optional `applications/NNN-<slug>/index.md` navigation-pointer pattern; §2d explicitly names what the carve-out does NOT change (§1 enumeration closure preserved; §2 budget applies to §1 files; §2b aggregate scope unchanged; §2c close-rotation unchanged; §3 archive-surface discipline unchanged; §4–§9 archive-pack discipline unchanged); §10 versioning updated. Subsumes S047 D-150 deferred spec-amendment candidate (iv) (`read-contract.md` §1 vs. `prompts/application.md` §Read ambiguity) by direction. No change to §2 per-file budget values, §2a sensor thresholds, §2b budget values, §2c retention-window value, or §4–§7 archive-pack mechanisms. v4 preserved as `read-contract-v4.md` with `status: superseded`.
  - `prompts/application.md` §Read (minor documentary clarification per OI-002) — Workspace-reading bullet rewritten to enumerate `read-contract.md` §1 items explicitly (MODE.md; active-status specs; PROMPT.md + prompts; SESSION-LOG; open-issues/index; prior 03-close.md files subject to §2c close-rotation; currently-active session provenance; conditionally engine-feedback/INDEX.md in self-development mode) and to remove the pre-v8 "and `applications/`" inclusion that produced the S047 P3 Outsider's latent spec contradiction; Domain-reading bullet restructured to name §Domain reading — `applications/` scope explicitly, to reference `read-contract.md` v5 §2d, and to name the chunked-read-on-demand mechanism + optional index file. Classification: minor documentary (brings prompt's Read enumeration into alignment with `read-contract.md` §1 closure + codifies session-scope-read-as-needed language; no new normative rule beyond what §2d introduces). No prior version of `prompts/application.md` is preserved as a separate file because `prompts/*` files are prompt text with history in git rather than versioned-via-suffix documents (Session 017 establishing precedent; `PROMPT.md` dispatcher was rewritten at engine-v7 without physical versioned-file preservation per same precedent).

  All other engine-definition files unchanged at engine-v8 boundary: `PROMPT.md`; `prompts/development.md`; `methodology-kernel.md` v6; `multi-agent-deliberation.md` v4; `validation-approach.md` v5; `workspace-structure.md` v5; `identity.md` v2; `reference-validation.md` v3; `engine-manifest.md` (this file, documentary update per Session 021/023/028/033/036 sub-pattern). `tools/validate.sh` unchanged: check 20 (default-read per-file budget) is not affected by the v5 revision at constants level because `applications/` files were already not in the default-read aggregate counted by check 20 (§1 was already closed pre-v5); the §2d carve-out makes the pre-existing behaviour explicit and extends it by documentation, adding no new enforcement mechanism. No new validator check is required.

Engine-v8 is the seventh engine-v-bump overall (v2 Session 021; v3 Session 022; v4 Session 023; v5 Session 028; v6 Session 033; v7 Session 036; v8 Session 048) and the fourth post-cadence-maturation content-driven bump (v5 + v6 + v7 + v8). §5.4 Session 022 engine-v-cadence minority (activated-not-escalated) does NOT re-escalate at this bump per Session 028 D-096 / Session 033 D-107 / Session 036 D-114 content-driven-bump precedent chain (cadence concern separates from substantive-bump classification). Engine-v8 follows an 11-session preservation window (S037–S047 all non-bump; S048 substantive) — equalling-and-slightly-exceeding the longest prior preservation run, reinforcing the content-driven-bump precedent. OI-018 remains open; Session 048 does not engage `engine-manifest.md` §5 revision.

Engine-v8 introduces a **new class of substantive-revision provenance**: operator-directed inbox-record resolution. The prior bumps traced the following provenance classes: v2–v4 came from preserved-minority / watchpoint activation; v5–v6 came from preserved-minority activation; v7 came from operator-surfaced mid-session deliberation; v8 comes from operator-directed-resolution on an inbox feedback record with the direction pre-declared as not-for-deliberation by the operator. This class is compatible with the engine's preservation-and-dissent-recording machinery: the feedback record itself is the preservation artefact; the `operator_directed_resolution` frontmatter field makes the non-deliberation explicit; the adopting session documents the adoption as a single-orchestrator implementation of a pre-ratified direction rather than as a deliberation. The pattern does not bypass deliberation when deliberation is warranted; it recognises that some operator interventions (narrow, directionally clear) are appropriately handled as single-orchestrator implementations.

**Key consequence at v8 adoption:** aggregate default-read surface is effectively unchanged in aggregate (the carve-out clarifies pre-existing exclusion of `applications/` from §1 enumeration; it does not add or remove any file from the §1 count). `read-contract.md` word count grows from 4,762 to approximately 5,624 (comfortable under §2 6K soft warning). Close-rotation continues standard per §2c; Session 042 close rotates OUT at Session 048 close per standard rotation mechanics.

Future engine-version increments will extend this history in this section.

## Validation

To validate this specification:

1. Confirm the files enumerated in §3 all exist at the declared paths.
2. Confirm that any file NOT enumerated in §3 but present in the workspace is either (a) in §4's explicit exclusion list, or (b) a superseded spec version, or (c) clearly out-of-scope (e.g., `.git`, `.gitignore`, `.claude`, `.serena`).
3. Confirm that `identity.md` v2 references this manifest as the definition of the engine at the current version.
4. Confirm that `workspace-structure.md` v3 references the same three file-class distinction this manifest implies (engine-definition / development-provenance / application-scope).
5. When a session executes a substantive revision to an engine-definition file, confirm the session's decision record declares a new engine version in this manifest's §2 and §7.
6. When an external application workspace is first initialised, confirm its Session 001 provenance records the engine version loaded per §6.5.
7. Confirm that no engine-version increment has occurred without a decision record authorising it (guard against silent engine-version drift).
