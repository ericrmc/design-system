---
title: Engine Manifest
version: 1
status: active
created: 2026-04-22
last-updated: 2026-04-26
updated-by-session: 071
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

**`engine-v13`** (established Session 071 per D-265).

Subsequent engine versions (`engine-v11`, `engine-v12`, `engine-v13`, ...) increment per the versioning discipline in §5. The current engine version is always named by this §2.

### 3. Engine-definition files at `engine-v13`

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
| `specifications/retrieval-contract.md` | Declares the required retrieval capabilities for Selvedge workspaces (v1, added engine-v9). |
| `specifications/records-contract.md` | Declares the structured-record-as-source-of-truth discipline + fact-family directory pattern + bootstrap obligations (v1, added engine-v10). |
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


The eleven historical engine-version entries (engine-v1 through engine-v11) are preserved verbatim at `[archive: provenance/066-session/archive/pre-restructure-engine-manifest-history/]` per `read-contract.md` v6 §4-§7 archive-pack discipline. Migration was executed at S066 to remediate the 25K-token Read-tool ceiling crossing observed at S066 open per operator-surfaced priority directive. The current engine-version entry remains inline below; future engine-version entries land inline as they are ratified.

**Thin per-version index of historical entries** (full text at `[archive: provenance/066-session/archive/pre-restructure-engine-manifest-history/]`):

| Version | Established | Decision | Class |
|---------|-------------|----------|-------|
| engine-v1 | Session 017 | D-074 | First versioned engine definition |
| engine-v2 | Session 021 | D-082 | Preserved-minority + watchpoint activation (OI-004 criterion-4 articulation) |
| engine-v3 | Session 022 | D-084 | First-of-record new engine-definition spec added (read-contract.md v1) |
| engine-v4 | Session 023 | D-086 | Preserved-minority activation (read-contract.md budget recalibration) |
| engine-v5 | Session 028 | D-096 | First content-driven post-cadence-maturation; aggregate budget + close-rotation |
| engine-v6 | Session 033 | D-107 | Preserved-minority activation (kernel §7 sense rename) |
| engine-v7 | Session 036 | D-114 | First operator-surfaced agenda increment (MODE.md + engine-feedback) |
| engine-v8 | Session 048 | D-154 | First operator-directed inbox-record resolution (single-orchestrator) |
| engine-v9 | Session 050 | D-172 | First MAD-adopted new engine-definition spec (retrieval-contract.md v1) |
| engine-v10 | Session 058 | D-200 | Second MAD-adopted new spec (records-contract.md v1; substrate substantive) |
| engine-v11 | Session 063 | D-228 | First two-session-arc adoption (S062 deliberation + S063 phase-3 implementation) |
| engine-v12 | Session 064 | D-234 | First-of-record depth-0 preservation event; substantive validation-approach v6→v7 + 5 new minorities (45→50) |

- **`engine-v13`** — established Session 071 via D-265. Cross-family-weighted phase-2 MAD on three-record joint-scope (EF-067 + EF-059 + EF-068-substrate-load-bearing) per S069 D-256 + S070 D-260 pre-ratification chain. (ε) hybrid bounded-then-extended adoption per cross-family weighted convergence (3-of-4 across families: P2 Claude + P3 codex + P4 codex on (ε) hybrid; P1 Claude dissent on full (γ) preserved as §10.4-M26 first-class minority). β-phase same-session-bounded per S058 D-199 precedent at S071 close + γ phase-3 arc deferred to S072+ multi-session per S062 D-220 precedent + named gating conditions per VD-003 lifecycle row review at S076. Preservation depth at engine-v12: 6 (S064 ratified + S065-S070 preserved; matched/exceeded engine-v10 mark; second-place behind engine-v7 (11) + engine-v9 (8); third-place behind those two). Engine-v13 reset depth to 0 at S071. Substantive: substantive revision to one engine-definition prompt (`prompts/development.md`) + new check in one engine-definition tool (`tools/validate.sh` check 29) + minor amendment to one engine-definition spec (`validation-approach.md` v7 §Tier 2.5 reviewer self-report honest-limit subsection + §10 cross-reference extension + §Gating Conventions check 29 constant + §Tier 1 table check 29 row + §Honest Limits check 29 entry; v7 preserved per OI-002 minor classification) + minor amendment to one engine-definition spec (`workspace-structure.md` v9 §10.4-M26 through §10.4-M29 minorities; v9 preserved per OI-002 minor) + harness-config edit (`.mcp.json` / Claude Code settings; not engine-definition).

  - `prompts/development.md` substantive revision (engine-definition substantive per OI-002 substantive-vs-minor heuristic) — §How to operate paragraph: promotes `forward_references('S<NNN>')` from engine-v9 (S054 D-187) "useful diagnostic / additive to the contract minimum / not required" framing to **required step at session-open** per Direction 1 (b) from EF-068-substrate-load-bearing intake. Adds substrate-availability-as-required-precondition clause per Direction 1 (c). Adds structured-declaration requirement clause for `00-assessment.md` + `03-close.md` per Q7 cross-family convergence per `provenance/071-session/01-deliberation.md` §2.7. Engine-v13 driver per `engine-manifest.md` §5.

  - `tools/validate.sh` substantive update (engine-definition substantive per new check addition) — check 29 candidate added (WARN-only initially per S058 D-204 mechanism-rollout discipline). Inspects current session's `00-assessment.md` + `03-close.md` for substrate-use structured/prose declaration. Honest-limit comment block + new constant `CHECK_29_ADOPTION_SESSION=71` + check 29 implementation block.

  Substantive minor amendments to existing engine-definition specs bundled in the v13 adoption:

  - `specifications/validation-approach.md` v7 minor amendment (clarifying text edit + cross-reference + new honest-limit subsection; no structural change to mechanism per OI-002 minor classification; v7 retained). Adds §Tier 2.5 reviewer self-report honest-limit subsection (Direction C from EF-067; suspends §10.4-M25 P1 audit-cost-budget threshold arithmetic on self-reported values pending harness-measurement availability per (γ) phase-3 (z6) digest arc). Adds §Gating Conventions `CHECK_29_ADOPTION_SESSION=71` constant. Adds §Tier 1 check 29 table row. Adds §Honest Limits check 29 entry. Adds §10 First-Class Minorities cross-reference for §10.4-M26 through §10.4-M29 mirror entries.

  - `specifications/workspace-structure.md` v9 minor amendment (additions only; no removals; no revisions to existing text per OI-002 minor classification; v9 retained) — extends §10.4 with four new first-class minorities §10.4-M26 through §10.4-M29 from S071 MAD per D-266; minority count 50 → 54. Status update notes added to §10.4-M25 reopen warrants (a) + (b) per S071 status.

  Engine-adjacent updates:

  - `validation-debt/index.md` revised — VD-003 lifecycle row introduced per S071 D-268 (γ phase-3 arc activation gating; review_by_session: S076 per 5-session forward window per S063+S067 WX-62-1 precedent). Engine-adjacent per `engine-manifest.md` §3 boundary; not engine-definition.

  - `.mcp.json` / `.claude/settings.local.json` harness-config edit per S071 D-264 Direction 1 (a) load-by-default. Not engine-definition; harness-config only.

  - `engine-feedback/INDEX.md` three triage row dispositions extended per S071 D-267 (EF-067 + EF-059 + EF-068-substrate-load-bearing). Not engine-definition; thin-index.

  All other engine-definition files unchanged at engine-v13 boundary.

Engine-v13 is the twelfth engine-v-bump overall and follows engine-v12 at preservation depth 6. §5.4 Session 022 engine-v-cadence minority does NOT re-escalate at this bump per content-driven-bump precedent chain S028+S033+S036+S048+S050+S058+S062+S063+S064 extended through S071 (cadence concern separates from substantive-bump classification); §10.4-M25 P2 cadence-depth concern at engine-v13 reset to depth-0: depth-7 forecast at engine-v13 next-bump is engine-conventional within engine-v9 depth-8 second-longest precedent.

Engine-v13 introduces cross-family-originated-and-adopted-at-MAD-execution reframe-architecture pattern reified at n=4 (S058 Substrate-N3.5 + S062 z5+z6 + S064 substrate-led + z11 + z12 + S071 measurement-authority separation). Engine-conventional pattern.

**Key consequence at v13 adoption**: aggregate default-read surface forecast post-S071-close approximate range +500 to +2,500 words from S070 close 87,113 (close.md size dependent on direction-adopted scope; spec edits per (β)-phase + workspace-structure.md v9 + validation-approach.md v7 minor + engine-manifest.md v13 entry); range ~87,500-90,000 / 90K soft (headroom -500 to +2,500). EF-068-read-write-rebalance Direction 4 critique materially reified by trajectory; aggregate may approach or exceed 90K soft at S071 or S072 depending on phase-2 MAD outcome.

- **`engine-v12`** — established Session 064 via D-234. **First-of-record depth-0 preservation event** (engine-v11 ratified S063; engine-v12 ratifies S064; engine-v11 preservation depth 0 — unprecedented in workspace history). **First-of-record operator-audit-as-MAD-input activation pattern**: S064 MAD activated by operator audit at S063 resolving close (Layer 6.1 second half) which surfaced three substantive findings disputing first-instance §Tier 2.5 implementation (rule scope too restrictive; reviewer scope at first instance too narrow; reviewer must challenge default-Path-A). Path AS-MAD-execution per session-mid path-amendment (Path L → Path AS-MAD-execution per operator instruction). 4-perspective two-family MAD (P1 Reviewer-Mechanism Architect Claude + P2 Conservator Claude + P3 Outsider Frame-Completion codex/GPT-5.5 + P4 Cross-Family Reviewer Laundering-Audit codex/GPT-5.5) produced 5,425-word synthesis adopting same-session bounded adoption per cross-family weighted convergence at Q7. Substantive: substantive revision to one engine-definition spec + sub-clause additions to one engine-definition tool + minor amendments to two engine-definition specs + minor revision to one prompt + revision to one engine-adjacent file.

  - `specifications/validation-approach.md` v6 → v7 (substantive) — revises §Tier 2.5 reviewer-family rule (relaxed from "no perspective in audited MAD" to "not orchestrator/close-author/primary-implementer/accountable-doer + cross-family at family + audit-scope-conditional family exclusion when self-validating own load-bearing claim with conflict disclosure"); revises audit shape to require minimum-evidence-packet (retention-window closes + (z5) ledger + active watchpoints + engine-feedback inbox + open-issues) with scope-coverage table; adds §7 Next-session-shape critique with P3's 5-condition affirmative-no-action-justification test; revises §(z5) Validation-Debt Lifecycle to make ledger **authoritative-not-witness** with `authoritative: true` frontmatter declaration; adds tripartite audit distinction (close correctness / mechanism adequacy / trajectory discipline); adds Layer 6.5 bootstrap-limited-confidence labelling; adds (z7) reviewer-prompt-template versioning + lock-in-after-n=2 discipline; adds §10.4-M21 through M25 cross-reference. v6 preserved as `validation-approach-v6.md` `status: superseded`.

  - `tools/validate.sh` substantive update (sub-clause additions to existing checks) — check 27 sub-clauses for §7 Next-session-shape critique presence + scope-coverage table presence in audit frontmatter + bootstrap-limited-confidence label presence when session adopts revisions to §Tier 2.5 mechanism. Check 28 sub-clause for `authoritative: true` declaration in `validation-debt/index.md` frontmatter.

  Substantive minor amendments to existing engine-definition specs bundled in the v12 adoption:

  - `specifications/methodology-kernel.md` v6 §7 Validate **minor amendment** (single-paragraph cross-reference update for tripartite audit distinction; no rename of senses; no removed text). v6 retained.

  - `specifications/workspace-structure.md` v8 → v9 **minor amendment** (extends §10.4 with five new first-class minorities §10.4-M21 through §10.4-M25 from S064 MAD per D-234; minority count 45 → 50). v8 preserved as `workspace-structure-v8.md` `status: superseded`.

  - `prompts/development.md` minor revision — adds explicit Path-justification at every close (z12) + reviewer-prompt-template versioning hook (z7) + (z11) (z5) authoritative-not-witness disposition discipline.

  Engine-adjacent updates:

  - `validation-debt/index.md` revised — adds `authoritative: true` frontmatter declaration per (z11) (z5) authoritative-not-witness semantics. NOT added to engine-manifest.md §3 (engine-adjacent per S063 D-228 precedent).

  All other engine-definition files unchanged at engine-v12 boundary.

Engine-v12 is the eleventh engine-v-bump overall and follows engine-v11 at preservation depth 0 — first-of-record. §5.4 Session 022 engine-v-cadence minority does NOT re-escalate at this bump per content-driven-bump precedent chain S028+S033+S036+S048+S050+S058+S062+S063 extended through S064 (cadence concern separates from substantive-bump classification); however, the depth-0 instance is unprecedented and §10.4-M25 P2 cadence-depth concern is preserved as standing reopen-warrant — engine-v13 at S065 would create first-of-record 3-bump-in-3-sessions pattern fully activating §5.4.

Engine-v12 introduces a **new instance of operator-audit-as-MAD-input activation pattern** (first-of-record). All prior MADs were activated by inbox feedback (EF-047 / EF-055 / EF-058) or operator-surfaced agenda at session-open. The operator audit at S063 resolving close became the substantive activation surface for S064 MAD; future Layer 6.1 second-half audits may produce analogous activation events.

Engine-v12 reifies the **cross-family-originated-and-adopted-at-MAD-execution reframe-architecture pattern at n=3** (S058 Substrate-N3.5 + S062 z5+z6 + S064 substrate-led + z11 + z12). Engine-conventional pattern.

**Key consequence at v12 adoption**: engine-manifest.md grows by ~600-800 words (compact entry per S064 §1.5 deferral discipline; full restructure deferred to S065+). validation-approach.md v7 ~4,243 (down from v6's 4,483 due to tightening). workspace-structure.md v9 grows by ~1,800 words (5 new minorities). Net default-read aggregate forecast post-S064-close: ~84,500-85,500 / 90K soft (headroom ~4,500-5,500). Engine-manifest.md crosses 8K hard ceiling potentially; restructure-at-S065+ becomes blocking if check 20 emits FAIL.

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
