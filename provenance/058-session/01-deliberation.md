---
session: 058
title: Deliberation synthesis — EF-055 substantive-arc 4-perspective two-family MAD; Substrate-N3.5 pilot toward Direction A adopted; engine-v10 candidate; new spec records-contract.md v1; SESSION-LOG.md phase-1 migration to structured records as proving slice
date: 2026-04-25
status: synthesis-complete
synthesis_by: Case Steward (Claude Opus 4.7 1M context; orchestrator; not one of the deliberation's perspectives per multi-agent-deliberation.md v4 §Synthesis)
participants_family: cross-model
cross_model: true
non_claude_participants: 2
oi004_qualifying_participants: [outsider-frame-completion, cross-family-reviewer]
---

# Deliberation — Session 058

## §0 Perspectives at a glance

| Perspective | Family | Model | Role | Words |
|-------------|--------|-------|------|-------|
| P1 Substrate-Methodology Architect | Claude | claude-opus-4-7 | Neutral surveyor; advocacy emerges from evaluation per S050 P1 precedent | ~2,950 |
| P2 Incrementalist Conservator | Claude | claude-opus-4-7 (parallel subagent) | Argues Direction C with explicit falsifying conditions | ~3,500 |
| P3 Outsider Frame-Completion | Codex | gpt-5.5 reasoning-effort xhigh | Substrate-N3.5 reframe: structured records authoritative; Markdown as witness | ~2,470 |
| P4 Cross-Family Reviewer / Laundering-Audit | Codex | gpt-5.5 reasoning-effort xhigh | Audits P1+P2+P3; convergence-check; dissent-preservation recommendations; own gate-bound recommendation | ~2,200 |

**D-133 M2 Convene-time matrix verification**: 4 seats / 2 families / 2 Claude (Opus 4.7 1M context) + 2 Codex (gpt-5.5 xhigh) / Outsider seat non-Claude (gpt-5.5) per 22-for-22 convention / synonym-drift guard: P3 frame-completion distinct from P4 laundering-audit — distinct roles exercised distinctly (P3 proposed Substrate-N3.5 as alternative architecture not in design-space.md §4 inventory; P4 audited P1+P2+P3 specifically and recommended a different narrower phase-1 than P1). Departure-discipline: no mid-session composition revision.

**§5.6 GPT-family-concentration observation**: 2 Codex + 2 Claude + 0 non-GPT-non-Claude — **fifth consecutive worst-case-side substantive-deliberation data point** (S044+S045+S047+S050+S058). Discharge/continued-preservation evaluable at close §5.

**WX-43-1 explicit-instruction variant**: P1 + P2 (Claude subagents) received do-not-self-commit instruction in launch prompts. P3 + P4 (codex) ran in `--sandbox read-only` mode (cannot commit). Cumulative explicit-instruction-variant window: n=0-of-13 self-commit breaches across S047 (3) + S049 (3) + S050 (4) + S058 (3 — P1/P2 honoured; P3/P4 sandboxed not applicable to discipline measurement).

**P4 first-invocation refusal**: at first launch, P4 correctly refused the audit because canonical perspective files (`01a/01b/01c-perspective-*.md`) had not yet been wrapped — the codex raw log only contained the prompt. P4's refusal was methodology-correct: "producing the P4 document now would fabricate convergence and dissent findings from stance briefs. That would be laundering, not audit." After Case Steward wrapped P1+P2+P3 to canonical filenames and committed at `a2c9805`, P4 was re-launched with explicit canonical paths and produced the audit recorded above. **First-of-record P4-blocked-on-precondition event** in workspace history; demonstrates the laundering-audit role's anti-laundering-by-process discipline.

## §1 Q-by-Q convergence/divergence map

### Q1 — Primary direction

**Cross-family weighted convergence (3-of-4 substantive-arc; 1-of-4 deferral)**:
- P1: A+Alt3 staged with phase-1 = SESSION-LOG.md + workspace-structure.md §10.4 [`01a`, Q1].
- P2: Direction C (defer until §10.4-M10 written warrants empirically fire); Direction B as contingent fallback if SESSION-LOG.md hard-ceiling breach [`01b`, Q1].
- P3: Substrate-N3.5 pilot toward Direction A (write-time structured records authoritative; existing Markdown remains human witness during proving interval) [`01c`, Q1].
- P4 own recommendation: gate-bound Substrate-N3.5 pilot toward Direction A; closest to P3's Q1 but with P2's warrant discipline and narrower phase-1 than P3 [`01d`, Q1].

**Synthesis position**: adopt **Substrate-N3.5 pilot toward Direction A** with phase-1 narrowed to `SESSION-LOG.md` only as proving slice. The synthesis position is closer to P4 than to P1 because P4's narrower phase-1 prevents premature commitment to broader migration before the pattern earns trust; closer to P3 than to P1 because P3's source-of-truth-vs-witness distinction is the substantive activation of §10.4-M10 (whereas P1's pure Direction A risks "thin index plus per-record Markdown" which P3 + P4 both name as Substrate-N2 only superficially). Direction A adoption requires the structured-record-as-source-of-truth interpretation, not the sharded-Markdown interpretation.

**Quote-over-paraphrase for load-bearing claim** (P3 [`01c`, Q1]):
> "I also would not adopt full Direction A immediately if 'A' means migrating accretive Markdown blocks into per-record Markdown files and thin indexes. That is a useful archive-rotation pattern, but it is not necessarily Substrate-N2."

P4 endorsement [`01d`, Q1]:
> "P3's N3.5 is the best substantive distinction: structured records must be authoritative, with Markdown as generated or checked witness."

**Why not Direction C (P2 isolated)**: P2's argument is the strongest available against substantive-arc adoption — §10.4-M10 written warrants ((a) maintenance-cost-2× across 3 sessions; (b) multi-hop-dominance-5× over 5 sessions) have not literally fired. P4 [`01d`, Q1] explicitly addresses this: "a file-size warning is adjacent evidence, not the same warrant." [synth] Synthesizer accepts P2's narrow reading: WX-34-1 SESSION-LOG.md ceiling pressure is NOT a literal §10.4-M10 warrant fire. However, the substantive-arc adoption does not depend on §10.4-M10 warrant fire — it depends on operator surfacing of EF-055 + S057 D-194/D-195/D-196 ratification + S058 D-198 (this session). The §10.4-M10 minority's pre-committed warrants gate one mechanism for activation; operator-surfacing is a third de-facto activation channel acknowledged at S056 D-193h + operationally exercised at S057 D-194-D-196 (the dedicated MAD scheduling). P2's warrant-discipline position is preserved as first-class minority §4.1 below.

**Why not full P1 A+Alt3 (P1 isolated on broader phase-1)**: P1's two-block phase-1 (SESSION-LOG.md + workspace-structure.md §10.4) is "attractive but too broad for first proof" per P4 [`01d`, Q2]. The synthesis takes P4's narrower-phase-1 position because: (a) the §10.4 minority migration interacts with retrieval-contract.md §7.4 mirrored minorities, pulling additional cross-spec scope into phase-1 that P1 acknowledges-yet-discounts; (b) per P4 [`01d`, Q6]: "P1's phase-1 cross-spec surface is larger than its 'two blocks' framing suggests, because mirrored minorities pull `retrieval-contract.md` into scope"; (c) P4's normalized phase-2 gate explicitly requires soak-evidence before broader migration. P1's broader-phase-1 position is preserved as first-class minority §4.3 below for activation if SESSION-LOG.md pilot proves too narrow.

### Q2 — Adoption scope

**Convergence 3-of-4 on SESSION-LOG.md-only phase-1 (P2, P4, P3-Q7-narrowed); divergence 1-of-4 (P1 wants two blocks)**.

P1 [`01a`, Q2]: "Phase-1 (S058 MAD adoption + first migration): SESSION-LOG.md migration to `provenance/sessions/S<NNN>.md` per-session files, plus workspace-structure.md §10.4 migration to `specifications/minorities/M-NNN.md` per-record files."

P2 [`01b`, Q2]: "If Direction A is adopted despite my recommendation, the smallest phase-1 scope that honours the operator surfacing without committing to the broader arc is: `SESSION-LOG.md` only."

P3 [`01c`, Q7] narrows from broader Q2 list to: "Session 058 should decide the architecture and migrate one narrow proving slice, ideally `SESSION-LOG.md` plus the record schema needed to support it."

P4 [`01d`, Q2]: "Phase 1 should be `SESSION-LOG.md` only plus the record contract required to make it authoritative."

**Synthesis position**: phase-1 = `SESSION-LOG.md` only. Phase-2 (S059) = mirrored minorities (workspace-structure §10.4 ↔ retrieval-contract §7) per P4's recommendation. Phase-3 (S060+) = engine-version history + reference-validation §10 + feedback metadata.

### Q3 — Per-record-file directory structure

**Convergence 3-of-4 on `records/` fact-family directories (P3, P4, P1-partial); divergence 1-of-4 (P2 prefers spec-local distribution)**.

P1 [`01a`, Q3]: `specifications/minorities/` for cross-spec minorities; spec-local for spec-internal minorities.

P3 [`01c`, Q3]:
```text
records/sessions/
records/minorities/
records/engine-versions/
records/feedback/
records/edges/
```

P4 [`01d`, Q3] endorses P3's pattern: "Use fact-family directories, not spec-owned Markdown directories, for source records."

**Synthesis position**: adopt **`records/<fact-family>/`** root directory at workspace root (not under `specifications/`). Initial fact-family directories: `records/sessions/` (phase-1); `records/minorities/`, `records/engine-versions/`, `records/feedback/` (phase-2+). File-class discipline per P3 + P4 convergence: distinguish `structured-source-record` (authoritative) / `markdown-witness` (generated or validator-checked projection) / `human-provenance` (immutable session provenance per existing convention). Workspace-structure.md v7 codifies these classes.

P1's `specifications/minorities/` position preserved as activation-warrant-bearing alternative if cross-spec mirrored discipline becomes problematic (§4.4 below).

### Q4 — Index format

**Convergence 4-of-4 on open-issues thin-table pattern as model exemplar; convergence 3-of-4 (P3 + P4 + implicit P1) on index-as-projection-not-source**.

P1 [`01a`, Q4]: thin table `[ID | Title | Status | Path | Anchor session]`.

P3 [`01c`, Q4]: thin row `ID | Status | Short title | Source record | Witness/path | Last touched`. "Indexes should stop being the fact source."

P4 [`01d`, Q4]: thin row `ID | Status | Summary | Source record | Witness/path | Anchor session | Last status event`. "If the index row and the record disagree, the record should win and the validator should fail."

**Synthesis position**: adopt thin-table-row pattern with columns `ID | Status | Title | Source record | Witness/path | Anchor session | Last status event` (P4's columns). Authority discipline: source record > index row; check 25 verifies index-record consistency.

### Q5 — Validator + tool updates

**Convergence 4-of-4 on new check 25; divergence on phase-timing and scope detail**.

P1 [`01a`, Q5]: phase-1 check 25 verifying frontmatter `id` matches row ID; status field consistency.

P2 [`01b`, Q5]: check 25 if Direction A proceeds; staging strategy via feature branch + synthetic broken-row fixture.

P3 [`01c`, Q5]: phase-1 check 25 narrow at first; six checks (unique IDs / index-row points to existing record / required fields / mirrored references resolve to canonical / generated witness paths exist / no silent unrecorded entries).

P4 [`01d`, Q5]: phase-1 check 25; "P2's suggestion that check 25 can be deferred until after a `SESSION-LOG.md` pilot is too weak; a pilot without integrity validation cannot prove the pattern." Seven checks (unique IDs / required fields / index-record consistency / no orphan records / no orphan index rows / valid status enums / record-witness drift detection).

**Synthesis position**: adopt check 25 in phase-1 (S058) per P4's necessity argument. Initial scope: P3+P4 union — unique ID / required frontmatter fields / index-row points to existing record / no orphan records / no orphan index rows / valid status enum (closed/superseded/archived for sessions) / no record-witness drift. `tools/build_retrieval_index.py` extension to index structured records as first-class objects (not merely follow markdown links) — phase-1 implementation; basic indexing is sufficient at S058; refinement over phase-2+. Test fixtures: at minimum one valid record + one missing-field fixture; expand at phase-2.

### Q6 — Cross-spec interactions

**Convergence on phase-1 essential set; divergence on scope of phase-1 cross-spec edits**.

Phase-1 essential (synthesised from P1+P3+P4):
- NEW spec: `records-contract.md` v1 — defines structured-record schema, witness discipline, fact-family directory structure, source-of-truth-vs-witness authority discipline. Mirrors `retrieval-contract.md` v1 adoption pattern at S050 (engine-defined contract; engine-adjacent implementation; bootstrap obligations).
- `workspace-structure.md` v6→v7 — adds three file-classes (`structured-source-record` / `markdown-witness` / per existing `human-provenance`) per §file classes section; adds `records/` directory to top-level structure §Top-level structure; cross-references `records-contract.md`.
- `read-contract.md` v5→v6 — §1 default-read enumeration update: SESSION-LOG.md replaced by `records/sessions/index.md` (thin pointer-only); §2 budget unchanged (thin index well under 6K soft); §2c retention-window clause updated since substrate makes "older closes" still queryable.
- `engine-manifest.md` — engine-v10 entry added; `records-contract.md` added to §3 engine-definition file enumeration.
- `tools/validate.sh` — check 25 added.
- `tools/build_retrieval_index.py` — record-aware indexing.

Phase-2+ deferrable (synthesis adopts P4 [`01d`, Q6]):
- `engine-manifest.md` §7 reshape — at phase-3 when engine-version migration occurs.
- `reference-validation.md` v3→v4 §10 reshape — at phase-3.
- `retrieval-contract.md` v1→v2 §7 reshape — at phase-2 with mirrored-minority migration.
- `multi-agent-deliberation.md` v4 §Provenance Layout — likely at phase-3+ when MAD-internal records are considered; not phase-1 scope.

### Q7 — Multi-session arc shape

**Convergence 4-of-4 on 3-session arc**.

P1 [`01a`, Q7]: S058 phase-1 (architecture + first migration); S059 phase-2 (remaining §10/§7 blocks); S060 phase-3 (registries + soak observation).

P3 [`01c`, Q7]: S058 architecture + SESSION-LOG.md migration; S059 minorities + mirrored references; S060 engine-version history + feedback metadata.

P4 [`01d`, Q7]: same shape as P3; phase-2 gate explicitly normalised: "check 25 passes; retrieval resolves 100% of migrated IDs; fallback index is readable without substrate; default-read word count decreases by at least the migrated `SESSION-LOG.md` body minus thin-index overhead; two consecutive closes add session records without editing a long accretive block; no record/witness drift is detected."

**Synthesis position**: 3-session arc S058 → S059 → S060. **S058 = phase-1 (architecture ratification + new spec + cross-spec minor revisions + SESSION-LOG.md migration to records/sessions/ + check 25 + retrieval-index extension + archive-pack pre-migration state + engine-v10 ratified)**. S059 = phase-2 (mirrored minorities migration; gated on P4's normalized phase-2 conditions). S060 = phase-3 (engine-version history + feedback metadata + decision on Markdown-witness generation). Phase boundaries: phase-2 begins only after one-session soak post-S058 with no record-witness drift detected; phase-3 begins only after phase-2 soak.

### Q8 — Operator-stated preference treatment

**Convergence 4-of-4 on durable-input-not-foreclosure**.

P1 [`01a`, Q8]: "I take operator preference as evidence that the operator is seeing the structural-friction signal directly... I do not score Direction A higher on any matrix axis because of operator preference."

P2 [`01b`, Q8]: "Confirming Shape 1 (synthesis + MAD) is precisely the operator saying: 'I want my preference adversarially tested.' Defaulting toward A on operator-preference grounds would be misreading the surfacing."

P3 [`01c`, Q8]: "The preference is best satisfied by staging toward actual Substrate-N2, not by immediate maximal migration."

P4 [`01d`, Q8]: "The preference should affect interpretation, not outcome selection. Specifically, it clarifies that 'Direction A' means structured records as source-of-truth and Markdown as witness."

**Synthesis position**: durable-input-not-foreclosure per all four perspectives. **Critical interpretation per P4**: operator preference clarifies the *substance* of Direction A as structured-records-source-of-truth (not sharded-Markdown). The synthesis adopts a substantial variant — "Substrate-N3.5 pilot toward Direction A" — which honours operator preference's substantive content while not foreclosing deliberation outcome.

## §2 Phase-1 adoption architecture (synthesised)

**Substrate-N3.5 pilot toward Direction A** at phase-1 minimum scope (SESSION-LOG.md only).

### §2.1 New engine-definition spec: `records-contract.md` v1

Mirrors the `retrieval-contract.md` v1 adoption pattern at S050.

Sections:
- §1 Scope and framing — declares structured records as source-of-truth for selected fact families; Markdown as witness or projection; rejects (at phase-1) sharded-Markdown-as-Substrate-N2 framing.
- §2 Required record families (phase-1) — `records/sessions/` only at phase-1.
- §2.1 Session record schema — frontmatter (id, session, date, title, summary, status, anchor_close); body (one-paragraph expansion if useful; thin discipline).
- §3 Required failure behaviour — record without canonical id is invalid; index-record drift is validation failure.
- §4 Workspace-local state — `records/` directory at workspace root; gitignored cache regenerated from records.
- §5 Bootstrap contract for external-application workspaces — `tools/bootstrap-external-workspace.sh` extended to copy `records/` empty directory + `records-contract.md` reference.
- §6 Phase-2 gate (WX-58-1 records-discipline-soak recording) — check 25 passes; retrieval resolves 100% of migrated IDs; fallback index readable without substrate; default-read aggregate decreases ≥7K words; no record-witness drift detected; two consecutive closes add session records without editing long accretive block.
- §7 Preserved first-class minorities (Session 058 records-substrate MAD) — see §4 below for full text + activation warrants; this §7 mirrors the language for spec-local readability.
- §8 Versioning — phase-2 (v1→v2) adds mirrored-minority record family + retrieval-contract v1→v2 §7 reshape; phase-3 (v2→v3) adds engine-version + feedback record families.

### §2.2 SESSION-LOG.md migration mechanics

- Each existing SESSION-LOG.md row becomes one file `records/sessions/S<NNN>.md` with frontmatter `{id: S<NNN>, session: <NNN>, date: <YYYY-MM-DD>, title: <one-sentence>, summary: <one-sentence>, status: closed, anchor_close: provenance/<NNN>-session/03-close.md}`. Body: optional one-paragraph expansion (currently SESSION-LOG.md row content's "One-sentence decision-surface summary" cell becomes the body; some rows have multi-cell content which moves to body verbatim per S051 D-178 thin-row preservation discipline).
- `records/sessions/index.md` is the thin table replacing SESSION-LOG.md as default-read. Columns per §1 Q4 above.
- SESSION-LOG.md itself: archived at `provenance/058-session/archive/pre-records-SESSION-LOG/` per S022 R8a / S040 D-123 / S051 D-178 archive-pack precedent. SESSION-LOG.md is removed from §1 default-read enumeration; replaced by `records/sessions/index.md`.

### §2.3 Validator: check 25

```
Check 25: structured-record integrity (records-contract.md v1)
  - For each <records/<family>/index.md>: verify each row points to an existing record file
  - For each <records/<family>/*.md>: verify required frontmatter fields present
  - Verify no orphan records (every record file's id appears in its family's index)
  - Verify no orphan index rows (every index row's path resolves)
  - Verify status enum membership per family (sessions: closed | superseded | archived)
  - Verify no record-witness drift (status in record matches status in index row)
```

Check 25 emits FAIL on any failure. Phase-1 implementation focuses on `records/sessions/`; phase-2+ extends to additional families.

### §2.4 Retrieval-index extension

`tools/build_retrieval_index.py` is extended to index structured records as first-class retrieval objects:
- Walk `records/<family>/*.md` (in addition to existing `*.md` walk).
- Parse frontmatter; extract `id` as canonical identifier; extract `kind` from family name (sessions, minorities, etc.).
- Insert into `documents` table with `kind: record-<family>`.
- Insert into `identifiers` table with canonical = `id`.

Phase-1: minimal extension (just walk records/ tree). Phase-2+: more sophisticated record-aware queries.

### §2.5 Engine-v10 trigger

This bump is content-driven per §5 versioning discipline + S028 D-096 / S033 D-107 / S036 D-114 / S048 D-154 / S050 D-172 content-driven-bump precedent chain. New engine-definition spec (`records-contract.md` v1) + substantive revisions to three engine-definition specs (`workspace-structure.md` v6→v7; `read-contract.md` v5→v6; `engine-manifest.md` §3 enumeration extension). §5.4 cadence minority does NOT re-escalate per the precedent chain — content-driven bump after a 7-session preservation window post-S050 D-172.

### §2.6 Not in phase-1 (deferred with explicit gates per §3)

- Mirrored minority records (workspace-structure §10.4 ↔ retrieval-contract §7) — phase-2.
- Engine-version history records (engine-manifest §7) — phase-3.
- Feedback metadata records (engine-feedback/INDEX.md) — phase-3.
- Reference-validation §10 minorities — phase-3.
- Markdown-witness auto-generation pipeline — phase-3+.
- Edges family records (`records/edges/`) — phase-3+ (interacts with retrieval-contract §7.5 syncs_with minority).

## §3 Phase-2 gate (per P4 normalized recommendation)

**Through S058 close + S059 open + S060 open**, every session close records records-discipline use in a `## Records substrate use (WX-58-1)` section with five fields:

```markdown
## Records substrate use (WX-58-1)

- check_25_status: pass | fail | warn
- migrated_id_resolution: <count of records/<family>/*.md ids resolved by `resolve_id` / total records>
- fallback_index_readable: yes | no | not-tested
- record_witness_drift: <count of detected drifts>
- session_record_added_without_editing_accretive_block: yes | no | n/a
```

**Phase-2 fires** iff ALL of:
- Check 25 passes at S058 close + S059 close.
- ≥95% of migrated IDs resolve at S059 close.
- Fallback index (`records/sessions/index.md`) readable without substrate at S058 close.
- Zero record-witness drifts detected through S059 close.
- S059 close added session record without editing SESSION-LOG.md (which is by then archive-surface).

**If phase-2 fires**: S059 may proceed with mirrored-minority migration (workspace-structure §10.4 ↔ retrieval-contract §7); engine-v10→v11 candidate or engine-v10 minor amendment per OI-002 heuristic.

**If phase-2 does NOT fire**: phase-1 paused (not deprecated); §4.1 Conservator minority's activation warrant evaluates; possible rollback via archive-pack restoration.

## §4 Preserved first-class minorities (Session 058 records-substrate MAD)

Four first-class minorities preserved from this MAD per `multi-agent-deliberation.md` v4 §Preserve dissent + P4 dissent-preservation recommendations [`01d`, Dissent-Preservation Recommendations]. Engine-wide minority count at S058 close: **40** (36 at open + 4 new). Minority-index authoritative cross-reference will live in `specifications/workspace-structure.md` v7 §10.4-M12 through §10.4-M15; this §4 block duplicates the activation-warrant language for deliberation-local readability. Per the synthesis position adopting Substrate-N3.5 records-as-source-of-truth + cross-spec mirrored canonical record discipline, the §10.4 minority-index will itself be migrated to `records/minorities/` at phase-2; until then, §10.4 in workspace-structure.md is the canonical home.

### §4.1 P2 warrant-gated deferral (Direction C / B fallback)

**Position**: "Direction C (defer until §10.4-M10 written warrants empirically fire), with Direction B held as a contingent fallback if SESSION-LOG.md ceiling pressure forces a tactical local action before either warrant fires." [`01b`, Q1]

**Source**: `provenance/058-session/01b-perspective-incrementalist-conservator.md` §Q1.

**Activation warrant**: if no §10.4-M10 telemetry exists by S060 (i.e., no measurable maintenance-cost or multi-hop-dominance signal collected), OR phase-1 cost exceeds projected maintenance savings across two closes (S058 + S059), the Conservator's deferral position is vindicated and the substantive arc is rolled back via archive-pack restoration. Per P2 falsifying conditions (4): if substrate operational maturity is genuinely uncertain (MCP stdio transport remains unverified end-to-end), Direction A's structured-record dependency on substrate is putting load on an unverified layer.

**Reopen warrants**: (a) check 25 noisy or expensive (high false-positive rate); (b) record-witness drift detected within two sessions; (c) phase-1 migration fails to reduce default-read load by ≥7K words.

### §4.2 P3 + P4 shallow-Direction-A warning (records-must-be-source-of-truth)

**Position**: "Per-record Markdown plus thin indexes ... is not necessarily Substrate-N2." [`01c`, Frame Critique + Q1]; "if migrated records lack structured authoritative fields, or Markdown witnesses remain manually authoritative" [`01d`, Dissent-Preservation Recommendations 2].

**Source**: `provenance/058-session/01c-perspective-outsider-frame-completion.md` §Frame Critique + §Q1; `provenance/058-session/01d-perspective-cross-family-reviewer.md` §Counter-Frames.

**Activation warrant**: if migrated `records/sessions/*.md` lack structured authoritative frontmatter (e.g., status enum violations not caught by check 25), OR Markdown witnesses (e.g., `records/sessions/index.md` body content) become manually authoritative rather than projection-from-records, OR phase-2+ migration produces sharded-Markdown without strict source-of-truth discipline, this minority's substantive direction (true Substrate-N2 with structured records authoritative) becomes preferred revision direction.

**Reopen warrants**: (a) phase-1 SESSION-LOG.md migration retains Markdown-as-source-of-truth in practice (operators edit `records/sessions/*.md` body content rather than frontmatter); (b) phase-2 mirrored-minority migration creates duplicate source files instead of canonical record; (c) bootstrap contract does not propagate record-schema discipline to external workspaces.

### §4.3 P1 broader-phase-1 (SESSION-LOG.md + workspace-structure.md §10.4)

**Position**: "Phase-1 (S058 MAD adoption + first migration): SESSION-LOG.md migration to `provenance/sessions/S<NNN>.md` per-session files, plus workspace-structure.md §10.4 migration to `specifications/minorities/M-NNN.md` per-record files." [`01a`, Q2]

**Source**: `provenance/058-session/01a-perspective-substrate-methodology-architect.md` §Q1 + §Q2.

**Activation warrant**: if SESSION-LOG.md phase-1 pilot earns trust at S059 (check 25 clean; no drift; ≥95% resolution) AND default-read aggregate reduction is less than projected because §10.4 minority block continues accreting, the broader-phase-1 position is preferred for an accelerated phase-2 (mirror minorities migrated at S059 in single-session rather than 2-session staging).

**Reopen warrants**: (a) phase-1 soak shows pattern is robust enough to migrate two blocks per phase rather than one; (b) §10.4 minority block crosses 1,500 words during phase-1 soak (currently ~1,248 with M12-M15 added at S058 close).

### §4.4 P2 spec-local distributed minority directories

**Position**: "specifications/<spec-name>/minorities/M-NNN.md (distributed-across-spec-source-directories) over a centralised specifications/minorities/ directory. Rationale: minorities are spec-local artefacts that derive context from their parent spec." [`01b`, Q3]

**Source**: `provenance/058-session/01b-perspective-incrementalist-conservator.md` §Q3.

**Activation warrant**: if any cross-spec mirrored minority's status or text diverges across specs after migration to canonical `records/minorities/M-NNN.md`, the spec-local distribution position is vindicated as preferred direction.

**Reopen warrants**: (a) `applies_to:` or equivalent metadata fails to scale across mirrored facts; (b) external-workspaces inherit mirrored-minority dependencies without inheriting the originating spec context; (c) substrate cannot reliably distinguish mirrored-fact references from spec-local references.

## §5 Shared-frame-blindness assessment (per P4)

P4 named the shared Claude+derivation frame [`01d`, Counter-Frames]:
> "P1 and P2 do not converge on direction, but they share a quieter frame: the migration object is a Markdown block. P1 wants to move selected blocks into per-record files and indexes; P2 wants to delay, or if forced, pilot on `SESSION-LOG.md` as per-session Markdown rows. Both pay less attention than P3 to authority: which artifact is the fact source?"

**Session 058 data point for §5.6 GPT-family-concentration evaluation**: the P3 + P4 cross-family contribution is **substantive and load-bearing** in this synthesis. The Substrate-N3.5 reframe (P3-originated) was not in design-space.md §4 inventory and would not have surfaced from Claude-only deliberation. P4's audit + own recommendation was decisive in narrowing phase-1 from P1's two-block proposal to one-block (SESSION-LOG.md only). Cross-family adversarial coverage produced a synthesis that differs materially from what 4 Claude perspectives would have produced. Worst-case-side composition (2 Codex + 2 Claude + 0 non-GPT-non-Claude) did NOT produce worst-case-outcome.

**§5.6 minority window-ii observation at S058**: fifth consecutive worst-case-side substantive-deliberation data point (S044+S045+S047+S050+S058). Per §5.6 reopen-warrant (i) external-review-cites-narrow-record: not yet materialised at S058. Per §5.6 reopen-warrant (ii) S047-close-without-non-GPT-non-Claude: window-ii closed at S047 close per §5.6 minority text strict reading. Spirit-level §5.6 question carries forward: **continued-preservation-against-future-event-horizon** disposition adopted per S033 §10.3 + S042 D-127 6-session-elapsed-zero-event precedent. No discharge or vindication at S058; preserved unchanged.

## §6 Case Steward meta-notes

- **WX-43-1 explicit-instruction variant**: P1 + P2 (Claude subagents) instructed do-not-self-commit; both honoured. P3 + P4 (codex --sandbox read-only) cannot commit by sandbox; not applicable to discipline measurement. Cumulative explicit-instruction-variant n=0-of-13 self-commit breaches.
- **P4 first-invocation refusal**: methodology-correct; preserves laundering-audit role discipline. First-of-record event in workspace history; operationalises the role's anti-laundering-by-process discipline. Recorded at §0 above + close §10 meta-observations + 02-decisions.md D-205 housekeeping sub-section.
- **P3 frame-completion impact**: Substrate-N3.5 reframe is the load-bearing distinction. P3 originated; P4 endorsed; synthesis adopts. Without P3's contribution, the synthesis would have defaulted to P1's "thin index plus per-record Markdown" pattern that P3 + P4 explicitly named as Substrate-N2-only-superficially. This is a clean cross-family frame-completion event — n=2 Substrate-Nn-reframes originated at S050 P3 (Substrate-N1/N2/N3) and now S058 P3 (Substrate-N3.5). Pattern: P3 Outsider role consistently surfaces alternative-architecture reframes the Claude perspectives miss.
- **P4 dissent-preservation rec mapping**: P4's 4 recommendations map directly to §4.1–§4.4 above. Rec 3 (P1's staged substantive-arc if synthesis chose C/B) does not apply since synthesis adopted substantive arc; preserved instead as §4.3 broader-phase-1 minority. Rec 4 (canonical mirrored-minority records) is NOT preserved as minority because synthesis adopts canonical-mirrored-record discipline at phase-2; the alternative (spec-local distributed) is preserved as §4.4.
- **D-133 M2 third-of-3 (S045/S047/S050) verification window** previously vindicated at S050; this S058 MAD continues the convention cleanly. 4-of-4 instances held at S058 (Convene-time matrix + lineage-constraint Outsider non-Claude + synonym-drift function-audit P3-frame-completion vs P4-laundering-audit + departure-discipline no mid-session revision).
- **§10.4-M2 (Skeptic-preserver continued preservation)**: pathway exercised at adoption edge (S057 D-194/D-195/D-196 → S058 substantive deliberation); 8 lifecycle records → 8 unchanged + EF-055 transitions triaged→resolved at S058 close → 0 new / 1 triaged / 7 resolved / 0 rejected. Continued preservation consistent.
- **§10.4-M10 (Substrate-N2 reframe minority)**: this MAD is the operational activation. Minority operational-exercise complete at S058. Per design-space.md §8 open question 1 + S057 close §10 meta-observation 9 + this S058 D-200 below: **operator-surfacing channel formalised as third written warrant** for §10.4-M10 alongside (a) maintenance-cost-2× and (b) multi-hop-dominance-5×. New written warrant (c): operator-surfacing of §10.4-M-N-activation. The minority's substantive direction (structured-records-as-source-of-truth) is partially adopted at phase-1 (sessions only); full activation pending phase-2/phase-3 broader migration.
- **No minority retracted by synthesis**.

## §7 Handoff to §2 decisions

This deliberation resolves:

- **Q1** → Substrate-N3.5 pilot toward Direction A (3-of-4 substantive; 1-of-4 deferral).
- **Q2** → Phase-1 minimum: SESSION-LOG.md only (3-of-4 narrow-phase-1).
- **Q3** → `records/<fact-family>/` directory at workspace root (3-of-4).
- **Q4** → Thin-table-row pattern with authority discipline (records authoritative; index projection); columns per P4.
- **Q5** → Check 25 in phase-1 (4-of-4 timing; P2-deferral overruled per P4 necessity argument).
- **Q6** → Phase-1 essential cross-spec edits: new spec records-contract.md v1 + workspace-structure.md v6→v7 + read-contract.md v5→v6 + engine-manifest.md engine-v10 entry + tools/validate.sh check 25 + tools/build_retrieval_index.py record-aware extension.
- **Q7** → 3-session arc S058 → S059 → S060 with normalised phase-2 gate (4-of-4 shape; P4 normalised gate).
- **Q8** → Operator preference durable-input-not-foreclosure; preference clarifies Direction A substance as structured-records-authoritative (4-of-4).

Ancillary decisions required at §2:
- Engine-v9→v10 bump (new spec + new behaviour + 3 substantive spec revisions per OI-002 heuristic).
- SESSION-LOG.md pre-migration archive-pack at `provenance/058-session/archive/pre-records-SESSION-LOG/`.
- §10.4-M10 written-warrant amendment (add operator-surfacing channel as warrant (c)).
- §4 four new first-class minorities §10.4-M12 through §10.4-M15.
- EF-055 lifecycle transition triaged→resolved.
- D-133 M2 fourth-of-N continued-vindication.
- WX-58-1 records-discipline-soak observation window opens (S058–S060 phase-2 gate).
- Housekeeping (close-rotation, D-129 thirteenth exercise, D-138 thirteenth folder, etc.).
- SESSION-LOG.md row at close — but SESSION-LOG.md is being migrated this session, so the S058 row goes into `records/sessions/S058.md` plus the new index.

End of deliberation.
