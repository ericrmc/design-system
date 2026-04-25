---
title: Records Contract
version: 1
status: active
created: 2026-04-25
created-in-session: 058
last-updated: 2026-04-25
updated-by-session: 058
supersedes: none
---

# Records Contract

## Purpose

This specification declares the **structured-record-as-source-of-truth** discipline that engine-v10 introduces for selected fact families. It fixes the **contract** (record schemas, witness discipline, fact-family directory structure, failure behaviour, bootstrap obligations) without fixing the **implementation** (the specific indexing code, the specific witness-generation pipeline, etc.).

This split is deliberate: the engine owns the contract; the implementation is engine-adjacent (not enumerated in `engine-manifest.md` §3 except for this contract spec itself). Implementations may evolve independently of the methodology's version line.

Adopted Session 058 per D-199 + D-201 + D-200 as resolution of `engine-feedback/inbox/EF-055-substrate-aware-format-and-archive-rethink-substantive-arc.md` per S057 D-194/D-195/D-196 + S058 4-perspective two-family MAD synthesis. First phase of a staged adoption: phase-1 scope is `records/sessions/` only; phase-2/3 scope is gated on the WX-58-1 records-discipline-soak evidence window (§6 below).

This specification adopts the **Substrate-N3.5 framing** per `provenance/058-session/01c-perspective-outsider-frame-completion.md` §Q1: structured records are authoritative for selected fact families; Markdown remains as witness or projection (generated or validator-checked) but is NOT authoritative for migrated facts. Per P4 [`provenance/058-session/01d-perspective-cross-family-reviewer.md`, Q1] endorsement: "structured records must be authoritative, with Markdown as generated or checked witness." This framing distinguishes structured-records-as-source-of-truth from sharded-Markdown patterns that look similar but preserve Markdown-as-source-of-truth.

## Specification

### §1 Scope and framing

The records substrate is a **source-of-truth layer** for selected fact families. Records are authoritative; per-family `index.md` files are projection/witness. Markdown specs may render or reference records but do not own the facts.

Three framings the contract explicitly rejects:

1. **Sharded-Markdown-as-Substrate-N2.** Rejected at phase-1. Per-record Markdown files arranged into thin indexes is a useful archive-rotation pattern, but it is not Substrate-N2 unless records are structurally authoritative (frontmatter source-of-truth + body witness-only-or-projection). Sharded Markdown that preserves Markdown-as-source-of-truth is preserved as activation warrant for §10.4-M13 first-class minority — see §7.2 below.

2. **Single-monolithic-records-database.** Phase-1 uses workspace-relative file-system structure (`records/<family>/<id>.md`) to preserve inspectability + portability + archive-pack discipline. A future phase may consolidate to a single database per the §10.4-M10 Substrate-N2 minority's substrate-consolidation reading; the contract leaves space for that path without committing.

3. **Operator-mentioned candidates carrying deliberation weight.** Per S050 §1 frame critique convention. Every contract direction is evaluated on technical merits; no records-substrate inherits prior status from operator surfacing.

### §2 Required record families (phase-1 contract)

At phase-1 adoption (Session 058) every Selvedge workspace MUST expose **one** record family with associated index.

#### §2.1 Family: `records/sessions/`

Schema:

```yaml
---
id: S<NNN>
session: <NNN>
date: <YYYY-MM-DD>
title: <one-sentence title>
summary: <one-sentence decision-surface summary>
status: closed | superseded | archived
anchor_close: provenance/<NNN>-session/03-close.md
---

<optional one-paragraph body expansion if existing row content has multi-paragraph density>
```

Field discipline:
- `id` (required): canonical identifier `S<NNN>` where NNN is zero-padded session number. Authoritative; substrate `resolve_id` returns this canonical.
- `session` (required): integer session number for filter-and-sort.
- `date` (required): ISO-8601 date.
- `title` (required): one-sentence title under 200 characters.
- `summary` (required): one-sentence decision-surface summary under 500 characters; optional one-paragraph expansion in body.
- `status` (required): enumeration. `closed` for sessions whose `03-close.md` is committed; `superseded` if a later session retroactively re-classifies (rare); `archived` if rotated past retention window.
- `anchor_close` (required): workspace-relative path to the canonical session close.

Body discipline: optional. Existing SESSION-LOG.md rows with verbose multi-cell content (post-S041 content-adaptive density per S051 D-178 thin-row preservation) preserve the existing one-sentence-summary in `summary` field; longer per-cell content moves verbatim into body if present. Body content is NOT authoritative; the canonical detail lives at `anchor_close` per existing thin-index discipline.

#### §2.2 Required index file: `records/sessions/index.md`

Thin pointer-only file. Default-read surface entry replacing `SESSION-LOG.md` per `read-contract.md` v6 §1 item 5.

Format:

```markdown
# Session Records — Index

Thin pointer-only index. Each record's canonical detail lives in `records/sessions/S<NNN>.md` per this file's row pointers; its session-close detail lives in `provenance/<NNN>-session/03-close.md` per the `anchor_close` field. This file is default-read surface and must remain under the per-file budget in `specifications/read-contract.md` §2.

| ID | Status | Title | Source record | Witness/path | Anchor session | Last status event |
|----|--------|-------|---------------|--------------|----------------|-------------------|
| [S001](S001.md) | closed | <title> | S001.md | provenance/001-genesis/03-close.md | 001 | closed S001 |
...
```

Authority discipline: source record (frontmatter) > index row. Validator check 25 verifies index-row-record consistency; on mismatch, the record wins and the validator emits FAIL.

### §3 Required failure behaviour

An implementation conforming to this contract MUST:

1. **Reject record without canonical id.** Records lacking `id` frontmatter field are invalid; check 25 emits FAIL.
2. **Reject status enum violation.** Records with status outside the enum (sessions: `closed | superseded | archived`) are invalid; check 25 emits FAIL.
3. **Reject missing required frontmatter fields.** Records missing any required field per §2.1 are invalid; check 25 emits FAIL.
4. **Reject orphan records.** Records present in `records/<family>/` but absent from `records/<family>/index.md` are invalid; check 25 emits FAIL.
5. **Reject orphan index rows.** Index rows pointing to non-existent record files are invalid; check 25 emits FAIL.
6. **Reject record-witness drift.** Index-row status field disagreeing with source-record status field is invalid; check 25 emits FAIL.

A session whose record-substrate is partially broken MAY proceed under fallback discoverability (the index file is readable as flat Markdown without substrate) but its `03-close.md` honest-limits section MUST record the substrate state and the scope of fallback.

### §4 Workspace-local state

- The records directory lives at `records/` at workspace root.
- Per-fact-family subdirectories (`records/<family>/`) hold record files.
- Per-family `index.md` thin pointer-only file at `records/<family>/index.md` — default-read surface entry per `read-contract.md` v6 §1.
- Per-record files at `records/<family>/<id>.md` — NOT default-read surface; read at session-scope-as-needed (similar to `applications/` carve-out per `read-contract.md` v5 §2d).

Records are **immutable post-creation** per D-017 immutability extended to records-substrate. Re-classification (e.g., `closed` → `superseded`) appends a new status event to the body or modifies status field with full provenance trail in the modifying session's `02-decisions.md`. Per `01-deliberation.md` §1 open-question-2: "append, not overwrite" — D-017 immutability applies to provenance once a session closes; records-substrate inherits this discipline.

### §5 Bootstrap contract for external-application workspaces

When `tools/bootstrap-external-workspace.sh` initialises a new external-application workspace (per `engine-manifest.md` §6), it MUST additionally:

1. Copy `specifications/records-contract.md` to the new workspace's `specifications/`.
2. Create empty `records/` directory at workspace root.
3. Create empty `records/sessions/` subdirectory.
4. Create empty `records/sessions/index.md` thin index file with header only (no rows).
5. Validate that check 25 passes on the empty workspace.

The bootstrap contract does NOT require:
- Pre-populating any record files (records accumulate as sessions execute).
- Auto-generation of Markdown witnesses (deferred to phase-3+).
- Any network access.

### §6 Phase-2 gate (WX-58-1 records-discipline-soak recording)

Every session close from S058 through S060 inclusive records records-discipline use in a `## Records substrate use (WX-58-1)` section with five fields:

- `check_25_status`: pass | fail | warn.
- `migrated_id_resolution`: count of `records/<family>/*.md` ids resolved by `resolve_id` / total records.
- `fallback_index_readable`: yes | no | not-tested.
- `record_witness_drift`: count of detected drifts.
- `session_record_added_without_editing_accretive_block`: yes | no | n/a.

**Phase-2 fires** iff ALL of:
- Check 25 passes at S058 close + S059 close.
- ≥95% of migrated IDs resolve at S059 close.
- Fallback index readable without substrate at S058 close.
- Zero record-witness drift through S059 close.
- S059 close adds session record without editing SESSION-LOG.md (which is by then archive-surface).

**If phase-2 fires**, S059 may proceed with mirrored-minority migration: workspace-structure §10.4 ↔ retrieval-contract §7 minorities consolidate to canonical `records/minorities/<id>.md` files; both spec index rows point to the same canonical record. Engine-v10→v11 candidate or engine-v10 minor amendment per OI-002 heuristic.

**If phase-2 does NOT fire** in S058–S060, phase-1 is paused (not deprecated); the §7.1 minority's activation warrant evaluates next; possible rollback via archive-pack restoration at `provenance/058-session/archive/pre-records-SESSION-LOG/`.

Phase-3+ (engine-version history records `records/engine-versions/`; reference-validation §10 records; feedback metadata records; Markdown-witness auto-generation pipeline; edges family records `records/edges/` interacting with retrieval-contract §7.5 syncs_with minority) require their own dedicated MAD at that time.

### §7 Preserved first-class minorities (Session 058 records-substrate MAD)

Four first-class minorities preserved from the S058 MAD per `multi-agent-deliberation.md` v4 §Preserve dissent + P4 dissent-preservation recommendations [`01d`, Dissent-Preservation Recommendations]. Engine-wide minority count at S058 close: **40** (36 at open + 4 new). Minority-index authoritative cross-reference lives in `specifications/workspace-structure.md` v7 §10.4-M12 through §10.4-M15; this §7 block duplicates the activation-warrant language for records-contract-local readability and is kept in sync at the same schema version.

#### §7.1 P2 warrant-gated deferral (Direction C / B fallback)

**Position**: "Direction C (defer until §10.4-M10 written warrants empirically fire), with Direction B held as a contingent fallback if SESSION-LOG.md ceiling pressure forces a tactical local action before either warrant fires." [`01b`, Q1]

**Source**: `provenance/058-session/01b-perspective-incrementalist-conservator.md` §Q1.

**Activation warrant**: if no §10.4-M10 telemetry exists by S060, OR phase-1 cost exceeds projected maintenance savings across S058+S059, the Conservator's deferral position is vindicated and the substantive arc may be rolled back via archive-pack restoration.

**Reopen warrants**: (a) check 25 noisy or expensive (high false-positive rate); (b) record-witness drift detected within two sessions; (c) phase-1 default-read load reduction <7K words.

#### §7.2 P3+P4 shallow-Direction-A warning (records-must-be-source-of-truth)

**Position**: "Per-record Markdown plus thin indexes ... is not necessarily Substrate-N2." [`01c`, Q1/Frame Critique]; "if migrated records lack structured authoritative fields, or Markdown witnesses remain manually authoritative" [`01d`, Dissent-Preservation Recommendations 2].

**Source**: `provenance/058-session/01c-perspective-outsider-frame-completion.md` §Frame Critique + §Q1; `provenance/058-session/01d-perspective-cross-family-reviewer.md` §Counter-Frames.

**Activation warrant**: if migrated `records/sessions/*.md` lack structured authoritative frontmatter, OR Markdown witnesses become manually authoritative, OR phase-2+ migration produces sharded-Markdown without strict source-of-truth discipline, this minority's substantive direction (true Substrate-N2 with structured records authoritative) becomes preferred revision direction.

**Reopen warrants**: (a) phase-1 SESSION-LOG.md migration retains Markdown-as-source-of-truth in practice (operators edit body content rather than frontmatter); (b) phase-2 mirrored-minority migration creates duplicate source files; (c) bootstrap contract does not propagate record-schema discipline to external workspaces.

#### §7.3 P1 broader-phase-1 (SESSION-LOG.md + workspace-structure.md §10.4)

**Position**: "Phase-1 (S058 MAD adoption + first migration): SESSION-LOG.md migration to `provenance/sessions/S<NNN>.md` per-session files, plus workspace-structure.md §10.4 migration to `specifications/minorities/M-NNN.md` per-record files." [`01a`, Q2]

**Source**: `provenance/058-session/01a-perspective-substrate-methodology-architect.md` §Q1 + §Q2.

**Activation warrant**: if SESSION-LOG.md phase-1 pilot earns trust at S059 (check 25 clean; no drift; ≥95% resolution) AND default-read aggregate reduction is less than projected because §10.4 minority block continues accreting, the broader-phase-1 position is preferred for accelerated phase-2 (mirror minorities migrated at S059 in single-session rather than 2-session staging).

**Reopen warrants**: (a) phase-1 soak shows pattern is robust enough to migrate two blocks per phase rather than one; (b) §10.4 minority block crosses 1,500 words during phase-1 soak (currently ~1,800 with M12-M15 added at S058 close).

#### §7.4 P2 spec-local distributed minority directories

**Position**: "specifications/<spec-name>/minorities/M-NNN.md (distributed-across-spec-source-directories) over a centralised specifications/minorities/ directory. Rationale: minorities are spec-local artefacts that derive context from their parent spec." [`01b`, Q3]

**Source**: `provenance/058-session/01b-perspective-incrementalist-conservator.md` §Q3.

**Activation warrant**: if any cross-spec mirrored minority's status or text diverges across specs after migration to canonical `records/minorities/M-NNN.md`, the spec-local distribution position is vindicated as preferred direction.

**Reopen warrants**: (a) `applies_to:` or equivalent metadata fails to scale across mirrored facts; (b) external-workspaces inherit mirrored-minority dependencies without context; (c) substrate cannot reliably distinguish mirrored-fact references from spec-local references.

### §8 Versioning

This specification is at **v1**. Version bumps follow the standard spec-revision discipline in `workspace-structure.md`:

- **v1 → v2**: phase-2 adoption (mirrored-minority migration). Adds `records/minorities/` family + retrieval-contract.md v1→v2 §7 reshape + workspace-structure.md §10.4 → thin index pointing to records/minorities/.
- **v2 → v3**: phase-3 adoption. May include `records/engine-versions/` (engine-manifest.md §7 reshape); `records/feedback/` (engine-feedback/INDEX.md migration); reference-validation.md v3→v4 §10 reshape; `records/edges/` (interacts with §7.5 syncs_with minority); Markdown-witness auto-generation pipeline.

Each phase transition is a MAD-required substantive revision per `multi-agent-deliberation.md` v4 §When Multi-Agent Deliberation Is Required.

## Validation

To validate this specification:

1. Confirm `records/sessions/index.md` exists with thin-table pattern per §2.2.
2. Confirm `records/sessions/S<NNN>.md` exists for every session in workspace history (S001 through current).
3. Confirm each record has required frontmatter fields per §2.1.
4. Confirm status enum membership per §2.1.
5. Confirm `tools/validate.sh` check 25 verifies records-substrate integrity per §3.
6. If the substrate is available in the agent's execution context, confirm `resolve_id("S<NNN>")` returns a record pointing to `records/sessions/S<NNN>.md` for each migrated session.
7. Confirm pre-migration SESSION-LOG.md preserved as archive-pack at `provenance/058-session/archive/pre-records-SESSION-LOG/` per `read-contract.md` v6 §4-§7 archive-pack discipline.

### §9 Honest limits

- **Phase-1 scope is narrow.** Only `records/sessions/` family is migrated at S058 per `01-deliberation.md` §1 Q2 3-of-4 narrow-phase-1 convergence. Phase-2 mirrored-minority migration + phase-3 engine-version history + feedback metadata are deferred per WX-58-1 phase-2 gate.
- **Markdown-witness auto-generation deferred.** Phase-1 retains `records/sessions/index.md` as manually-edited file (with check 25 enforcing record-witness consistency). Phase-3+ may add auto-generation pipeline.
- **Record-witness drift detection at phase-1 is structural, not semantic.** Check 25 verifies index-row-status matches record-frontmatter-status; it does NOT verify that summary or title fields match. Future phase-2 may extend.
- **Cross-workspace records consolidation out of scope.** A self-dev workspace's records substrate is independent of any external-application workspace's records substrate. Cross-workspace queries are not supported at phase-1.
- **Authority discipline depends on operator habit.** Validator check 25 catches drift but does not prevent operators from editing `records/sessions/index.md` body content as if it were source-of-truth. Per §7.2 reopen-warrant (a): if this pattern emerges, the source-of-truth discipline is at risk and §10.4-M13 minority becomes preferred revision direction.
- **Backward compatibility broken at engine-v10.** External-application workspaces bootstrapped pre-engine-v10 do not have `records/`; they must re-bootstrap or manually create the directory + index per §5.
- **Substrate-availability assumption (records read-side).** The retrieval substrate (engine-v9 phase-1) provides `resolve_id` + `search` over records-substrate. If MCP stdio transport remains unverified per S051-S058 chain, fallback discoverability via `records/sessions/index.md` flat-Markdown-readable preserves operational continuity. Per `01-deliberation.md` §1 open-question-1 4-of-4 convergence on fallback discoverability essential.
