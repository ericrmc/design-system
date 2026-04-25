---
session: 057
title: Design-space — substrate-aware format and archive rethink for accretive default-read files (synthesis + S058 MAD menu)
date: 2026-04-25
status: synthesis-artefact
author: Case Steward (single-orchestrator synthesis)
scope: input to Session 058 dedicated multi-agent deliberation on EF-055
---

# Design-space — substrate-aware format and archive rethink for accretive default-read files

## Purpose of this document

This document synthesises a design-space for the question surfaced in `engine-feedback/inbox/EF-055-substrate-aware-format-and-archive-rethink-substantive-arc.md`. Per S057 operator surface ("What about Path AS / Path PD operator-surfaced for EF-055 dedicated MAD scheduling per D-192?") + Case Steward shape proposal + operator confirmation ("Confirm Shape 1"), S057 = Phase-1 synthesis/design-space session per S049 D-157 precedent; this artefact is the primary output. It is designed to be loaded as input to the S058 MAD; it is not itself a decision record. S058 produces the decision record.

The document mirrors the shape of `provenance/049-session/design-space.md`: problem restatement → workspace-state measurement → substrate-availability assessment → direction inventory → cost/benefit mapping → cross-spec interactions → S058 MAD pre-ratification → open questions → honest limits.

## §1 Problem restatement under EF-055 framing

The EF-055 record observes that **default-read files growing accretively impose a structural read-to-edit cost paid every session (or every substantive event)**. The cost compounds with workspace age and is not addressed by the existing periodic-restructure precedent chain (S022 R8a / S040 D-123 / S051 D-178), which defers ceiling pressure but does not change the linear-growth shape.

The intake names three direction candidates:
- **Direction A** (operator-stated preference at intake): substantive Substrate-N2 reframe arc activating §10.4-M10 — structured records as source-of-truth; markdown as witness; accretive blocks become thin indices pointing to per-record files; engine-v10 candidate.
- **Direction B**: tactical thin-index extension to `SESSION-LOG.md` alone via Path L+A — minor per OI-002 per S022/S040/S051 precedent chain; no engine-v bump; defers the broader question.
- **Direction C**: defer until §10.4-M10 written warrants ((a) phase-2+ maintenance time exceeds projection 2× across 3 consecutive sessions; (b) multi-hop cross-reference query class dominates ≥5× prose-search over a 5-session window) empirically fire.

Per S056 D-192, the triage authorises deliberation on these three directions but does not foreclose any of them. The operator's intake-time preference (Direction A) is durable input the S058 MAD will treat as one position to deliberate, not as foreclosure.

The problem can also be reframed under the S050 P3 Outsider lens: **the accretive-blocks question is the same question EF-047-retrieval-discipline surfaced, applied to the *write side* of the corpus.** EF-047 surfaced "agents cannot look where indices don't point" and adopted the engine-v9 read-side substrate (`search` + `resolve_id` + `forward_references`). EF-055 surfaces "writers cannot append-without-rereading-the-whole-file when the writer is constrained by per-file budgets" and asks whether a parallel write-side reframe is warranted.

The substrate availability changes the urgency calculus: with cross-reference navigation now in the substrate, prose specs no longer need to carry verbose summaries to be findable. The §10.4-M10 minority preserved at S050 D-172 ("the shared markdown-plus-index frame should not be mistaken for the only scalable answer; decisions, OIs, minorities, watchpoints, etc. may eventually become structured records with markdown as witness") is the explicit reframe target.

## §2 Workspace state (measured at S057 open)

### §2.1 Default-read aggregate composition

Per `tools/validate.sh` check 20 at S057 open: aggregate default-read = **78,619 words / 21 files**. Headroom to 90K soft = 11,381 words.

Per-file breakdown of default-read files relevant to EF-055:

| File | Words | Class | Growth shape |
|------|-------|-------|--------------|
| `SESSION-LOG.md` | 7,044 | development-provenance | strictly linear-per-session |
| `specifications/engine-manifest.md` | 5,184 | engine-definition | linear-per-engine-v bump |
| `specifications/workspace-structure.md` | 3,918 | engine-definition | linear-per-Path-PD-minority |
| `specifications/reference-validation.md` | 7,177 | engine-definition | linear-per-RV-revision-minority |
| `specifications/retrieval-contract.md` | 2,323 | engine-definition | linear-per-MAD-minority |
| `engine-feedback/INDEX.md` | 934 | non-engine-operator-managed | linear-per-feedback-record |
| `specifications/aliases.yaml` | 244 | engine-adjacent | bounded; already structured |
| `open-issues/index.md` | 667 | development-provenance | bounded by OI-resolution discipline (model exemplar) |

**Accretive sections within these files (the EF-055 reframe scope):**

| Section | Words | Entries | Avg/entry |
|---------|-------|---------|-----------|
| `engine-manifest.md` §7 (engine-v history) | 3,780 | 9 | 420 |
| `workspace-structure.md` §10.4 (preserved minorities) | 1,248 | 11 | 113 |
| `reference-validation.md` §10 (preserved minorities) | 1,814 | 9 | 201 |
| `retrieval-contract.md` §7 (preserved minorities) | 499 | 5 | 100 |
| `SESSION-LOG.md` (rows) | 7,044 | 56 | 126 (variance by session class) |
| `engine-feedback/INDEX.md` (records) | 934 | 8 | 117 |

**Total accretive content within default-read = ~15,300 words (~19% of default-read aggregate).** This is the structural surface EF-055 is asking the methodology to consider reframing.

### §2.2 Growth rates and ceiling pressure

`SESSION-LOG.md` is the most pressed file at S057 open:
- Post-S051-restructure: 4,621 words (S051 D-178 archive-pack point).
- S055 close: 6,598 words (+1,977 over 4 sessions; avg 494 words/session content-adaptive density).
- S056 close: 7,044 words (+446; soft warning fires second-consecutive close).
- Forecast S057 close: 7,300–7,500 (Path AS row content-adaptive density).
- **Hard ceiling pressure window**: at the current 350–500 words/session cadence, S058 close approaches 7,800–8,000 (hard ceiling); S059 close exceeds.

The existing precedent chain (S022 R8a / S040 D-123 / S051 D-178) handles this as periodic restructure. The intake observes that this chain "treats accretion as a periodic crisis to be deferred" — true, but also: it has worked through three rotations spanning ~50 sessions, with each restructure preserving the verbose form as archive-pack. The chain is reactive but operationally functional.

`reference-validation.md` v3 at 7,177 words is **already over the 6K soft threshold** since S033 v3 adoption. It has not been restructured because the §10 block (1,814 words) is preservation-load-bearing across 9 minorities and the rest is normative content. This is the closest example of an accretive file living over budget without restructure intervention.

`engine-manifest.md` §7 at 3,780 words / 9 entries is the most lopsided ratio: §7 carries 73% of the 5,184-word file. Each engine-v entry is 420 words on average; some entries (engine-v7 / engine-v8) are 800+ words. The pattern grows linearly with engine-v cadence; engine-v9→v10 (likely from EF-055's own Direction A adoption) would add ~600+ words.

`workspace-structure.md` §10.4 at 1,248 words / 11 minorities and `retrieval-contract.md` §7 at 499 words / 5 minorities are smaller absolute size; their reframe value is smaller per-block but the pattern-discipline value is uniform across the four accretive-spec-block targets.

### §2.3 Substrate availability at engine-v9

Per `retrieval-contract.md` v1 §2 phase-1 contract:
- `search(query, k)` — BM25-ranked prose search across 473 docs / 54,987 identifiers.
- `resolve_id(alias)` — canonical resolution + path + line + context.
- `forward_references(target)` — every line-precise occurrence of an identifier across the corpus (added S054 D-187 per EF-054).

These tools answer:
- "What was decided in S055?" — `forward_references('S055')` returns line-precise occurrences across all 14 files mentioning it.
- "What is §10.4-M5?" — `resolve_id('§10.4-M5')` returns canonical path + line + context.
- "Which engine-v established `read-contract.md` v5?" — `search('read-contract v5')` or `resolve_id('engine-v8')` returns the entry.

S055 first organic-use + S056 second + S057 third demonstrate the substrate works at session-open diagnostic time. S057 organic-use found zero previously-dropped forward-commitments (clean-propagation verification).

**This availability changes what prose specs need to do.** Pre-substrate, prose specs needed to carry verbose summaries because cross-reference navigation depended on prose-scan reading. With substrate available, detail can live in per-record files; indices can be truly thin (open-issues/index.md model: thin status + path pointer); cross-reference navigation is a substrate query, not a prose-scan.

### §2.4 The open-issues/index.md exemplar

`open-issues/index.md` (667 words, 19 active rows + 5 resolved) demonstrates the shape EF-055 directs at scale. Each row is one line: `| [OI-NNN](OI-NNN.md) | Title | Surfaced session | Status — one-line summary |`. Detail lives in per-OI files. Cross-reference uses `[OI-NNN](OI-NNN.md)` markdown links + substrate identifier resolution.

**The pattern's structural property**: linear growth in OI-count rather than session-count. With OI-resolution discipline, the index has remained bounded across 56 sessions while the workspace itself has grown ~50× in artefact count. This is the proof-of-concept the §10.4-M10 reframe argues should generalise.

### §2.5 What is *not* accretive (model exemplars within EF-055 scope)

- **`specifications/aliases.yaml`** (244 words, 8 canonical + ~20 alias mappings): bounded by alias-coverage discipline, not by engine-event cadence. Already structured (YAML schema_version 1). Intake says "no change" — confirmed.
- **`prompts/development.md` / `prompts/application.md` / `PROMPT.md`** (1,745 / 1,243 / 807 words): bounded by methodology shape, not by event cadence. Edited only on substantive prompt revision (S017 split, S036 dispatcher revision, S054 forward_references paragraph).
- **`identity.md` / `methodology-kernel.md` / `multi-agent-deliberation.md` / `validation-approach.md` / `read-contract.md`** (1,575 / 1,861 / 6,637 / 4,647 / 5,605 words): normative content; revised by spec-revision discipline; preserved-minority blocks within `multi-agent-deliberation.md` and `validation-approach.md` are bounded by their respective MAD/VA revision cadence, not session-level.

These files demonstrate that **default-read files are not all accretive by nature**. The pattern is specific to files that accumulate per-session or per-event records: SESSION-LOG (per-session), engine-manifest §7 (per-engine-v), spec §10/§10.4/§7 minority blocks (per-MAD-with-preserved-minority), engine-feedback INDEX (per-feedback-record).

## §3 The Substrate-N2 reframe (S050 P3 origin)

Per `provenance/050-session/01c-perspective-outsider-frame-completion.md` §2 Substrate-N2:

> **Decisions, OIs, minorities, watchpoints, archive citations, session summaries, and cross-spec sync obligations become structured source-of-truth records, with Markdown rendered or assembled from those records. The durable substrate is not "Markdown plus index"; it is a structured fact corpus, perhaps JSONL files under `records/` or a workspace-local SQLite database with exportable Markdown witnesses.**

Per the same source §1 frame critique:

> **Selvedge may not need a search product as much as it needs a fact discipline. The corpus is already heavily ID-structured. If each session writes durable thin rows for decisions, open issues, minorities, edges, and archive references, then a database can be rebuilt from those rows without re-interpreting prose.**

Per `provenance/050-session/01d-perspective-cross-family-reviewer.md` §3 convergence-check + §4 shared-frame-blindness:

> **The shared frame is "plain markdown remains canonical; a local Python-built index sits underneath; FastMCP exposes query tools." This frame is reasonable, but it is still a frame. The blind spots are: structured artefacts as source of truth ... P2 names some alternatives ... but treats them as fallback or rejection rather than as coequal designs.**

P3's S050 own §2 Substrate-N2 paragraph notes: "**This option is probably too disruptive for S050 adoption, but it is the correct counter-frame.**" P4 dissent-preservation rec 4 preserved Substrate-N2 as first-class minority.

EF-055 is the operator-surfaced activation of that minority. The reframe is no longer "too disruptive" because:
1. The substrate (engine-v9 phase-1) has stabilised across 7 sessions of organic use (S051–S057).
2. The accretive-block pattern has matured across 8 engine-v entries + 11 §10.4 minorities + 9 §10 RV minorities + 5 §7 retrieval minorities.
3. The SESSION-LOG.md soft-warning has fired second-consecutive close at S056; hard-ceiling pressure window opens S058.
4. Operator-surfacing as activation channel has precedent across S036/S043/S044/S045/S047 (Path PD/PSD/OC/OS/OS minority-activation pathway).

## §4 Direction inventory

### §4a Direction A — Substantive Substrate-N2 reframe arc (operator-stated preference)

**Scope**: Multi-session arc activating §10.4-M10. Re-design `read-contract.md` + `workspace-structure.md` + accretive-spec-blocks under the principle: *substrate is source-of-truth for cross-reference navigation; prose specs hold normative content only; accretive blocks become thin indices pointing to per-record files.*

**Concrete shape (per intake §Direction A; for S058 MAD to refine)**:

- **`SESSION-LOG.md`** → thin pointer-only index. Each row: `| NNN | YYYY-MM-DD | <one-sentence-title> | →path |` (~25–40 words asymptotic). Detail in `03-close.md` (already there; pre-existing thin-index discipline restored).
- **`specifications/engine-manifest.md` §7** → thin index per-engine-v: `| Engine version | Session | Bump-provenance class | →path |`. Detail moves to `specifications/engine-versions/v{N}.md` per-version files. Substrate handles `resolve_id('engine-v9')`.
- **`specifications/workspace-structure.md` §10.4** → thin index per-minority: `| §10.4-M | Title | Source-session | Status (preserved/discharged/activated/vindicated) | →path |`. Detail moves to `specifications/minorities/M-NNN.md` per-minority files.
- **`specifications/reference-validation.md` §10** → same pattern as §10.4.
- **`specifications/retrieval-contract.md` §7** → same pattern.
- **`engine-feedback/INDEX.md`** → already close to right shape; tighten if needed.
- **`specifications/aliases.yaml`** → no change (already structured/bounded).

**Engine impact**: engine-v10 candidate. Substantive revisions to:
- `read-contract.md` (§1 enumeration possibly extended; §4 archive-pack discipline possibly simplified; §2c retention-window value possibly revised given substrate makes "older closes" still queryable).
- `workspace-structure.md` (§10.4 reshape; possibly file-class extension for "per-record indexed files"; §provenance preservation discipline interactions).
- `engine-manifest.md` (§3 file enumeration if per-version directory adopted; §7 reshape).
- `reference-validation.md` (§10 reshape).
- `retrieval-contract.md` (§7 reshape).
- Possibly: new spec governing the per-record-file pattern.

**Implementation impact**:
- New per-record directory structure (e.g., `specifications/minorities/`, `specifications/engine-versions/`).
- Migration of existing accretive-block content to per-record files (preservation-discipline applies; archive-packs of pre-restructure state).
- Validator updates (check 20 default-read enumeration; check 22 archive-pack citation; possibly new check 25 for per-record-file integrity).
- `tools/build_retrieval_index.py` may need indexing-rule adjustments if directory structure changes.

**Multi-session arc length estimate**: 2–4 sessions (intake §Direction A "two-to-four-session arc estimated"). Possible compression (synthesis + adoption single MAD if scope is narrow); possible expansion (phase-3 multi-session if migration is staged).

**Risk profile**:
- Migration risk: per-record file proliferation may impose its own discoverability cost; substrate must reliably index across the new directory structure.
- Spec-coupling risk: §10.4 minorities are cross-referenced from many places (workspace-structure, retrieval-contract, validate.sh); reshape must preserve cross-references.
- Reversibility risk: per-record migration is low-reversibility under D-017 immutability; archive-pack-of-pre-restructure-state preserves witness but not easy rollback.
- Engineering load: substantial. Phase 2 MAD + Phase 3 implementation requires multi-session execution and substantive validator/tool updates.

**Reversibility**: low (per-record-file migration is structurally hard to undo without re-fragmenting and re-aggregating).

**Substrate-fit**: high. The reframe is exactly what the substrate was designed for; per-record files are query-targets that `resolve_id` and `forward_references` already handle.

### §4b Direction B — Tactical thin-index extension to SESSION-LOG.md alone

**Scope**: Apply the `open-issues/index.md` pattern to `SESSION-LOG.md` alone via Path L+A in the next routine-restructure session. Each row reduces to `| NNN | YYYY-MM-DD | <one-sentence-title> | →path |` (~25–40 words asymptotic). Pre-restructure preserved as archive-pack at `provenance/NNN-session/archive/pre-L-SESSION-LOG/` per S022 R8a / S040 D-123 / S051 D-178 chain.

**Engine impact**: minor per OI-002 per S022/S040/S051 precedent chain. No engine-v bump.

**Implementation impact**:
- Single-session execution (Path L+A).
- SESSION-LOG.md compressed to thin pointer-only rows; rows S001–S056 retroactively compressed (preservation-witness archive-pack).
- No spec edits; no validator updates; no tool updates.
- Existing per-session detail in `03-close.md` files unchanged.

**Coverage**: addresses `SESSION-LOG.md` alone. Does NOT address `engine-manifest.md` §7 / `workspace-structure.md` §10.4 / `reference-validation.md` §10 / `retrieval-contract.md` §7 / `engine-feedback/INDEX.md` accretive blocks.

**Risk profile**:
- Restructure-pattern drift: the S022 R8a → S040 D-123 → S051 D-178 chain shows the verbose-row-drift pattern recurs after each restructure (~10–15 sessions until next restructure pressure). Direction B alone does not change this; it just resets the drift counter.
- Forecloses Direction A?: NO. Direction B is a subset of Direction A (Direction A's SESSION-LOG-only restructure is identical to Direction B's restructure). Direction B as standalone preserves Direction A optionality for a later session.

**Reversibility**: medium. SESSION-LOG.md restructure is similar to S051 D-178 archive-pack (pre-restructure preserved verbatim).

**Substrate-fit**: low. Direction B does not change the structural shape; it just resets the linear-growth point.

### §4c Direction C — Defer until §10.4-M10 written warrants empirically fire

**Scope**: Preserve the existing structure. Allow §10.4-M10 to activate per its written warrants:
- (a) cumulative phase-2+ maintenance time exceeds projection 2× across 3 consecutive sessions; or
- (b) multi-hop cross-reference query class dominates ≥5× prose-search over a 5-session window.

Restrict near-term action to periodic SESSION-LOG restructure per existing precedent chain (S058–S060 candidate window per S055 D-190g + S056 D-193f + this S057 §3c).

**Engine impact**: zero. No spec edit. No engine-v bump.

**Implementation impact**: zero. Existing patterns continue.

**Risk profile**:
- §10.4-M10 written warrants are framed in cost-or-dominance terms; they may not fire even if the structural problem is real (the written warrants test for *runaway* cost, not for *baseline* cost-of-existence).
- Opportunity cost: the substrate's reframe-enabling property may decay if too many accretive entries accumulate before reframe (each entry adds migration cost).
- Operator-surfacing channel inherently bypasses the written warrants; if Direction C is adopted, the operator-surfacing precedent at EF-055 is recorded but no action follows.

**Reversibility**: high. Preserving status quo means future sessions can revisit at any time.

**Substrate-fit**: neutral. Substrate continues to be useful; reframe-enabling property unused.

### §4d Alternative architecture 1 — Per-block archive-pack rotation discipline

**Scope**: Apply close-rotation-style discipline to accretive spec sections. Each accretive block carries a "current window" of recent entries default-read, with older entries archive-packed by exclusion. E.g., `engine-manifest.md` §7 keeps the most recent 3 engine-v entries default-read; older entries archive-packed at `provenance/<adopting-NNN>/archive/engine-v-history/`.

**Comparison to Direction A**: addresses growth without restructuring file shape. Lower migration cost; lower substrate-fit (substrate still has to resolve archive-pack references).

**Risk**: archive-pack-by-block introduces a new archive-pack class with its own retention discipline; complexity grows. Likely worse than Direction A or B for engineering load.

### §4e Alternative architecture 2 — Hybrid: structured records for selected blocks only

**Scope**: Apply Substrate-N2 only to highest-cost blocks (e.g., `engine-manifest.md` §7 + SESSION-LOG.md), leaving lower-cost accretive blocks (workspace-structure §10.4, retrieval-contract §7) in current shape.

**Comparison to Direction A**: smaller migration scope; partial fix. Pattern-discipline value is reduced (different blocks behave differently across the spec set).

**Risk**: methodology asymmetry; future-session readers must remember which blocks are structured vs. prose. Likely worse than Direction A's uniform treatment for long-term maintenance.

### §4f Alternative architecture 3 — Substrate-N3 (write-time registries plus generated read model) per S050 P3 §2

**Scope**: Per `provenance/050-session/01c-perspective-outsider-frame-completion.md` §2 Substrate-N3: keep markdown as source of truth, but require close-time append or regeneration of structured registries (`identifiers.jsonl`, `edges.jsonl`, `archive_paths.jsonl`, `minorities.jsonl`, `sessions.jsonl`). The SQLite database is a generated read model from registries plus markdown FTS.

**Comparison to Direction A**: different reframe direction. N2 makes structured records source-of-truth; N3 keeps markdown source-of-truth but adds explicit write-time registries. N3 was P3's preferred shape at S050: "**This is my preferred Substrate-N shape: not 'choose DuckDB or SQLite and hope extraction is right', but 'make the facts explicit, then choose the smallest durable read model.'**"

**Risk**: changes write-side discipline (every session must append to registries at close); does not directly address EF-055's read-to-edit cost (writers still must read accretive prose blocks before editing).

**Substrate-fit**: high (registries directly feed substrate); but solves a different problem than EF-055 (write-to-registry vs. accretive-prose-cost).

### §4g Combination Direction A + Alternative architecture 3 (Substrate-N2 + Substrate-N3)

**Scope**: Direction A's per-record-file pattern + Substrate-N3's write-time registries. Per-record files are structured records; registries provide the relational view.

**Comparison to Direction A alone**: more comprehensive; longer arc. Direction A is the migration; Substrate-N3 is the operational discipline that maintains it.

**Risk**: scope expansion; combined arc estimate 3–6 sessions vs. Direction A's 2–4.

## §5 Cost/benefit mapping

The following matrix scores each direction against axes the S058 MAD will deliberate. Scores are qualitative (low / medium / high); ties indicate genuine open question for MAD deliberation.

| Axis | Dir A | Dir B | Dir C | Alt 1 (per-block archive rotation) | Alt 2 (hybrid partial) | Alt 3 (Substrate-N3) | A+Alt3 |
|------|-------|-------|-------|-----------------------------------|------------------------|----------------------|--------|
| Read-to-edit cost reduction | high | medium (SESSION-LOG only) | none | medium | medium (selected) | low | high |
| Structural friction reduction | high | low | none | medium | medium | medium | high |
| Substrate-fit | high | low | neutral | medium | medium | high | high |
| Engineering load (cost) | high | low | zero | medium | medium | medium | very high |
| Risk (migration / discoverability) | medium-high | low | zero | medium | medium-high | medium | high |
| Reversibility | low | medium | high | medium | medium | medium | low |
| Multi-session arc length | 2–4 | 1 | 0 | 2 | 2 | 2 | 3–6 |
| Engine-v10 candidate | yes | no | no | possible | possible | possible | yes |
| Pattern-discipline uniformity | high | low | neutral | medium | low | neutral | high |
| Operator-stated-preference fit | yes | partial subset | no | no | no | no | yes |
| §10.4-M10 activation | yes (substantive) | no | written-warrant-only | no | partial | no (different reframe) | yes |
| Opportunity cost | low (active migration) | medium (only resets drift) | medium-high (delays compounding) | medium | medium | medium | low |
| Forecloses other directions | partially (Dir B subsumed) | no (Dir A still possible) | no | no | no | no | n/a |

**Key observations from the matrix**:

1. **Direction A is the most substrate-fit and pattern-uniform** but has the highest engineering load and lowest reversibility.
2. **Direction B is the lowest-risk, lowest-cost option** but does not address the structural pattern; it only resets the drift point on `SESSION-LOG.md`.
3. **Direction C preserves the most optionality** but accepts the compounding cost of accretive blocks indefinitely (until written warrants fire).
4. **Alternative architectures 1/2/3 are partial-or-different reframes** that the MAD may explore as compromise positions.
5. **Combination A+Alt3 is the most comprehensive** but the longest arc.

The MAD's deliberation should specifically address:
- Whether the operator-stated Direction A preference should weight toward A (per S048 D-153 precedent for `operator_directed_resolution` — does NOT apply because EF-055 has no such field; precedent is durable-input-not-foreclosure).
- Whether Direction B as standalone is operationally adequate even if structurally insufficient (resets drift point; buys 30+ sessions of headroom; preserves Direction A optionality).
- Whether Direction C's risk profile (compounding cost; opportunity cost) is acceptable if §10.4-M10 written warrants are designed to test for runaway cost rather than baseline.

## §6 Cross-spec interactions

Direction A's substantive scope necessarily revisits multiple specs. The S058 MAD must consider these cross-spec interactions:

### §6.1 `read-contract.md` v5 interactions

- **§1 default-read enumeration**: would the per-record-file pattern require the enumeration to extend (e.g., `specifications/minorities/index.md` becomes default-read while individual `M-NNN.md` files become activation-read)? Or do per-record files remain archive-surface-by-exclusion with index-only default-read?
- **§2 per-file budget**: thin index files are well under budget by design; per-record files are individually under budget; aggregate budget is reduced.
- **§2c retention-window**: with substrate-backed cross-reference, "older closes" are still queryable. Does the 6-session window remain operationally necessary, or does the substrate enable longer windows or different retention discipline?
- **§4 archive-pack discipline**: per-record-file migration may simplify archive-pack discipline (less prose-block-archive-pack pressure).
- **§2d applications/ carve-out**: unaffected.

### §6.2 `workspace-structure.md` v6 interactions

- **§file-classes**: would per-record files constitute a new file class ("per-record-indexed files"), or extend "engine-definition" / "non-engine-operator-managed" classes?
- **§10.4**: reshape is the direct target; minorities migrate to `specifications/minorities/M-NNN.md`.
- **§provenance**: per-record-file immutability discipline (D-017) needs explicit treatment for per-record files (each minority's `M-NNN.md` is immutable once written, but new minorities can be added with new IDs).

### §6.3 `engine-manifest.md` interactions

- **§3 file enumeration**: per-version files (e.g., `specifications/engine-versions/v{N}.md`) classification — engine-definition? per-version-immutable-record? Need explicit treatment.
- **§7 history**: reshape direct target; existing entries migrate to per-version files.
- **§5 versioning discipline**: bump trigger may need amendment if per-version files are classified differently.

### §6.4 `reference-validation.md` v3 interactions

- **§10**: reshape direct target; minorities migrate to per-minority files.
- **§9 trigger 7 re-fire conditions**: cross-references to §10 minorities need updating.

### §6.5 `retrieval-contract.md` v1 interactions

- **§7**: reshape direct target; minorities migrate.
- **§7 / §10.4 mirroring discipline**: under per-record-file pattern, the §7 / §10.4 "mirror" question may dissolve (single per-record file per minority; both specs reference the same source).

### §6.6 `multi-agent-deliberation.md` v4 + `validation-approach.md` v5 interactions

- These specs do not currently carry §10-style minority blocks. They preserve dissent inline within each session's deliberation provenance. EF-055 reframe does not directly target them, but if the per-record-file pattern is adopted, the question arises whether MAD/VA should also have per-minority files.

### §6.7 `tools/validate.sh` + `tools/build_retrieval_index.py` interactions

- **Validator**: check 20 default-read enumeration must reflect any per-record-file additions to default-read scope. New check 25 candidate: per-record-file integrity (each `M-NNN.md` exists; cross-references resolve).
- **Build retrieval index**: per-record files are indexed naturally if they're under indexed paths; no major change required.

## §7 S058 MAD pre-ratification

### §7.1 MAD shape

**Recommended**: 4-perspective two-family MAD per D-133 M2 standing-discipline lineage-constraint matrix per S050 D-172 precedent.

**Family composition**: 2 Claude + 2 Codex/GPT-5.5 (or other non-Claude available at S058 time). Per `multi-agent-deliberation.md` v4 §When Non-Claude Participation Is Required, this is required for any decision that "Creates or substantively revises any specification in `specifications/`" (d016_2 trigger; engine-definition spec creation/revision is the substantive scope of EF-055 Direction A).

**OI-004 d023 implications**: a MAD that produces engine-v10 candidate with substantial spec revisions touches d023_4 (asserts a change in the state of OI-004) only if the reshape requires re-asserting OI-004 closure status. OI-004 was closed at S041; per `multi-agent-deliberation.md` v4 §Forward semantics of d023_4 in closed state, d023_4 fires only on proposed state-changes to OI-004. EF-055 Direction A does not propose OI-004 state-change; d023_4 does not fire by default. Non-Claude participation remains required per d023_2 (substantively revises `multi-agent-deliberation.md` if the reshape extends to MAD's own minority-preservation discipline; though current Direction A does not directly target MAD).

### §7.2 Perspective composition (recommended; for S058 MAD-session itself to ratify per S050 precedent)

Per S050 lineup precedent (P1 Substrate Architect / P2 Incrementalist Skeptic / P3 Outsider Frame-Completion / P4 Cross-Family Reviewer Laundering-Audit), the natural S058 lineup is:

- **P1 Reframer (Claude Opus 4.7)** — defends Direction A; surveys per-record-file mechanics; addresses migration risks. Equivalent role-shape to S050 P1 Substrate Architect.
- **P2 Conservator (Claude Opus 4.7)** — defends Direction C; surveys cost-of-status-quo; argues opportunity cost; defends written-warrant discipline. Equivalent role-shape to S050 P2 Incrementalist Skeptic.
- **P3 Outsider / Frame-Completion (Codex/GPT-5.5)** — surveys reframe alternatives (Substrate-N3; combination architectures; alternative engineering shapes); names blind spots in Claude perspectives. Equivalent role-shape to S050 P3.
- **P4 Cross-Family Reviewer / Laundering-Audit (Codex/GPT-5.5)** — audits P1 + P2 for laundering; convergence-check; preserved-minority recommendations. Equivalent role-shape to S050 P4.

**Per-perspective brief structure** per `multi-agent-deliberation.md` v4 §Stance Briefs:
1. Methodology context (shared, byte-identical) — Selvedge / engine-v9 / EF-055 framing
2. Problem statement (shared) — accretive default-read files; reframe scope; three intake directions + alternatives
3. Design questions (shared) — see §7.3 below
4. Role-specific stance (varies per perspective)
5. Response format (shared) — markdown per S050 brief shape
6. Constraint on external imports (shared)

### §7.3 Design questions for S058 MAD

The MAD must address (questions for S058 brief):

- **Q1 — Primary direction choice**: Direction A, B, C, or alternative architecture (1/2/3/A+Alt3)? Justify with cross-axis reasoning per §5 matrix.
- **Q2 — Adoption scope (if Direction A or substantive variant)**: which accretive blocks migrate in phase 1? Phase 2? What is the migration sequence?
- **Q3 — Per-record-file directory structure (if Direction A)**: `specifications/minorities/` vs. distributed-across-spec-source-directories? Naming convention (`M-NNN.md` vs. `<id>.md`)?
- **Q4 — Index format**: thin-table-row pattern per `open-issues/index.md` model? Status column convention? Path-pointer convention?
- **Q5 — Validator + tool updates**: new check 25 for per-record-file integrity? Build-retrieval-index.py rule changes?
- **Q6 — Cross-spec interactions**: §6.1–§6.7 above — which interactions are in-phase-1 scope vs. deferred?
- **Q7 — Multi-session arc shape**: 2 sessions (single-MAD adoption) vs. 3–4 sessions (staged migration)?
- **Q8 — Operator-stated preference treatment**: Direction A is operator-stated preference; does the MAD treat this as durable input (S048 D-155 precedent: pre-ratification preserved during deliberation but not foreclosure) or vote it as one position among others?

### §7.4 S058 MAD execution shape

**Single-session MAD** at S058 (not multi-session per perspective). Independent-phase per `multi-agent-deliberation.md` v4: 4 perspectives reason independently from shared brief; synthesis after all return; decision per `02-decisions.md`.

**Phase-3 adoption** (post-MAD): single-session per Direction (Direction A or substantial variant: substantive spec edits + engine-v10 + archive-pack preservation; Direction B: Path L+A SESSION-LOG-only restructure; Direction C: no action).

### §7.5 Honest limits on MAD pre-ratification

- This synthesis does NOT pre-commit Direction A/B/C choice. The MAD deliberates.
- This synthesis does NOT pre-commit perspective composition. The MAD-session ratifies its own composition first per S050 D-172 precedent.
- This synthesis does NOT pre-commit phase-3 adoption shape. That depends on direction adopted.
- The cost/benefit matrix in §5 is qualitative; the MAD may dispute scoring.
- The cross-spec interaction list in §6 is the Case Steward's enumeration; the MAD may identify additional interactions.

## §8 Open questions for S058

Beyond the §7.3 design questions, the MAD should consider:

1. **Substrate-availability assumption**: Direction A's pattern depends on substrate continuing to function. If `tools/retrieval_server.py` becomes unavailable (MCP API churn; FastMCP deprecation; Python ecosystem shifts), the per-record-file pattern degrades. Should the design require fallback discoverability (e.g., aggregate index file) for substrate-absent operation?

2. **Per-record-file immutability discipline**: D-017 immutability applies once a session closes. If a minority is re-discharged or re-vindicated in a later session, does the per-minority file get appended (multiple status entries chronologically) or does the index status get updated while the file remains stable?

3. **Multi-spec minority cross-references**: §10.4-M7 through §10.4-M11 are mirrored in `retrieval-contract.md` §7.1 through §7.5. Under per-record-file pattern, do both specs reference the same `M-NNN.md` file, or do mirrored minorities have separate files?

4. **Engine-version per-version files vs. §7 history block**: if `specifications/engine-versions/v{N}.md` per-version files are adopted, do they replace `engine-manifest.md` §7 entirely or coexist with a thin §7 index pointing at them?

5. **Migration ordering**: should `SESSION-LOG.md` migrate first (Direction B subset) or last (after spec-block patterns are proven)?

6. **Archive-pack discipline for pre-restructure state**: per S022 R8a / S040 D-123 / S051 D-178 precedent. Under Direction A, each accretive block reshape produces a pre-restructure archive-pack. The discipline scales but generates many archive-packs; should there be aggregate retention rules?

7. **External-application portability**: at engine-v10, external workspaces via `tools/bootstrap-external-workspace.sh` would inherit the per-record-file pattern. Is the bootstrap contract sufficient (per `engine-manifest.md` §6 + `retrieval-contract.md` v1 §5) or does it need extension?

8. **Cross-linkage to S047 D-150 deferred candidate (i)** (kernel §7 qualitative-multi-agent label): EF-055 triage record §Forward-dependency-observations names this as possible scope overlap with Direction A. The MAD may engage candidate (i) or defer per S047 D-150 chain.

## §9 Honest limits on this synthesis

1. **Single-orchestrator synthesis (no parallel research sub-agents).** The S049 design-space.md used parallel research sub-agents because the substrate-discipline scope had 11+ candidate technologies with technical depth requiring per-candidate feasibility research. S057 synthesis is reframe-direction (3 named directions + alternatives) more than technology-survey; single-orchestrator synthesis is appropriate. The Case Steward's framing here is one Claude perspective; the S058 MAD will have cross-family adversarial coverage.

2. **Direction inventory may be incomplete.** §4 lists Directions A/B/C from the intake plus Alternative architectures 1/2/3 plus Combination A+Alt3. The S058 MAD may identify additional directions or alternative shapes during independent-phase reasoning.

3. **Cost/benefit matrix scores are qualitative.** §5 scores are Case Steward's assessment; the S058 MAD may revise.

4. **Cross-spec interaction enumeration is bounded by Case Steward awareness.** §6 lists known interactions with `read-contract.md` / `workspace-structure.md` / `engine-manifest.md` / `reference-validation.md` / `retrieval-contract.md` / MAD/VA / validator/tools. The S058 MAD may identify additional interactions during independent-phase reasoning.

5. **Operator-stated Direction A preference treatment is unsettled.** EF-055 has no `operator_directed_resolution` frontmatter field; precedent (S048 D-153) does not apply. S057 confirmed Shape 1 (synthesis-then-MAD) suggests operator authorises full deliberation rather than short-circuit. The S058 MAD should treat the operator preference as durable input (recorded for consideration) but should be explicit about whether the final decision aligns with or diverges from the preference.

6. **§10.4-M10 written-warrants vs. operator-surfacing channel relationship**: the §10.4-M10 minority's written warrants are framed in cost-or-dominance terms; operator-surfacing as a third de-facto activation channel was acknowledged at S056 D-193h but not formalised in the minority text. The S058 MAD may amend the minority's activation warrants if Direction A is adopted.

7. **S050 raw-perspective references via plain path convention.** S050 perspectives are archive-surface-by-exclusion (S050 close rotated OUT at S056) but are NOT archive-packs (no manifest.yaml; preserved verbatim at original paths). Per `read-contract.md` v5 §3 archive-surface-by-exclusion + §6 archive citation convention (which is reserved for archive-pack directories or rotated `03-close.md` files), raw perspective files from rotated-out sessions are referenced by plain path (not `[archive: ...]` syntax). The S058 MAD will receive this synthesis as input + can re-read S050 raw perspectives directly via the cited paths.

8. **Substrate availability honest-limit.** §3 framing assumes engine-v9 substrate continues to function. MCP stdio transport remains unverified per S051–S057 close §8 honest-limit chain. Substrate has functioned via `.cache/venv/bin/python3` direct invocation + FastMCP `tool_manager` introspection across 7 sessions; assumed-stable for foreseeable horizon. If substrate breaks, Direction A reframe loses substrate-fit advantage.

9. **EF-055 intake says aliases.yaml has "no change" but lists it in `target_files`** — internal inconsistency in the intake. Synthesis treats aliases.yaml as bounded/structured/no-change per the body text disambiguating the frontmatter.

10. **No domain-validation on this synthesis itself**: the synthesis is workspace-validation only (Case Steward methodology check against `multi-agent-deliberation.md` v4 §Stance Briefs + S049 design-space.md precedent shape). Domain-validation will accumulate as S058 MAD perspectives engage and as adoption (if any) is exercised.

## §10 What this document is and is not

This is a **design-space synthesis**, not a decision record. It maps the deliberation surface for S058. It explicitly does NOT:
- Foreclose Direction A/B/C choice.
- Pre-commit the perspective composition.
- Pre-commit the phase-3 adoption shape.
- Pre-commit the migration sequence.
- Pre-commit cross-spec amendment scope.

It DOES:
- Restate the problem under EF-055 framing including operator-stated preference.
- Measure workspace state for accretive default-read files.
- Reference S050 P3 + P4 Substrate-N2 reframe origin via archive citations.
- Inventory directions including operator-stated A/B/C plus Case Steward alternatives.
- Score cost/benefit qualitatively across multiple axes.
- Enumerate cross-spec interactions for the MAD to consider.
- Pre-ratify the S058 MAD shape (4-perspective two-family per D-133 M2 + S050 lineup precedent).
- Pre-recommend perspective composition (with explicit "MAD ratifies own composition first" honest-limit).
- Frame design questions Q1–Q8 for the MAD brief.
- Surface 8 open questions that the MAD should consider beyond Q1–Q8.

## §11 Pre-ratification of S058 MAD

Per `multi-agent-deliberation.md` v4 §When Multi-Agent Deliberation Is Required + S048 D-155 / S049 D-159 / S050 D-172 precedent chain:

- **S058 = dedicated MAD session for EF-055** per S057 D-194 ratification + this design-space.md as input.
- **Shape**: 4-perspective two-family MAD per D-133 M2.
- **Family composition**: 2 Claude + 2 Codex/GPT-5.5 (or other non-Claude available; lineup ratified by S058 MAD itself per S050 precedent).
- **Perspective composition** (recommended for S058 MAD-session to ratify): P1 Reframer / P2 Conservator / P3 Outsider Frame-Completion / P4 Cross-Family Reviewer Laundering-Audit. Roles mirror S050 lineup adapted for EF-055 substantive scope.
- **Brief structure**: standard per `multi-agent-deliberation.md` v4 §Stance Briefs.
- **Design questions Q1–Q8**: per §7.3 above.
- **Open questions for MAD consideration**: per §8 above.
- **Engine-v impact**: engine-v10 candidate iff Direction A or substantial variant adopted; engine-v9 preserved iff Direction B or C alone.

The S058 session-open should: read this design-space.md in full as primary input; re-read S050 raw perspectives via `provenance/050-session/01a-perspective-substrate-architect.md` / `01b-perspective-incrementalist-skeptic.md` / `01c-perspective-outsider-frame-completion.md` / `01d-perspective-cross-family-reviewer.md` as needed; ratify perspective composition; commit briefs per `multi-agent-deliberation.md` v4 §Brief immutability; convene parallel sub-agents (Claude perspectives) + codex CLI invocations (non-Claude perspectives); synthesise; decide; commit.

The S057 close pre-ratifies this S058 shape. The S058 session itself is the next operational step.
