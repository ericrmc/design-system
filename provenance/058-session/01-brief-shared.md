---
session: 058
title: Shared brief — 4-perspective two-family MAD on EF-055 substrate-aware format and archive rethink (substantive-arc)
date: 2026-04-25
status: brief-immutable-at-commit
brief_committed_anchor: this commit
---

# Shared brief — Session 058 MAD on EF-055

**Brief immutability**: this file's §1, §2, §3, §5, §6 sections are byte-identical across all four perspectives. §4 role-specific stance varies per perspective and lives in each `01X-perspective-<role>.md` raw output file frontmatter or in a parallel `01X-brief-<role>.md` if substantively differentiated. This brief is committed before any perspective is launched per `multi-agent-deliberation.md` v4 §Brief immutability.

---

## §1 Methodology context (shared)

You are reasoning as one of four perspectives in a multi-agent deliberation within the **Selvedge engine**, a self-developing methodology for designing complex systems through diverse-perspective deliberation that produces durable artefacts and preserves reasoning. The engine is at **engine-v9** (established Session 050 per D-172).

The methodology runs sessions; each session reads workspace state, deliberates, decides, produces, validates, records, and closes. Substantive decisions (those modifying engine-definition specifications) require multi-agent deliberation per `multi-agent-deliberation.md` v4. At least one perspective must be from a non-Claude family for decisions touching kernel + MAD + VA-Tier-2 specs (cross-family adversarial coverage; per `multi-agent-deliberation.md` v4 §Limitations, "All Claude-subagent perspectives share a model family. Shared training produces shared blind spots: the same cultural priors, argumentative reflexes, refusal patterns, and aesthetic preferences").

This deliberation has 4 perspectives: P1 Substrate-Methodology Architect (Claude Opus 4.7) + P2 Incrementalist Conservator (Claude Opus 4.7 parallel subagent) + P3 Outsider / Frame-Completion (Codex / GPT-5.5 reasoning-effort xhigh) + P4 Cross-Family Reviewer / Laundering-Audit (Codex / GPT-5.5 reasoning-effort xhigh; distinct from P3). 2 Claude + 2 codex/GPT non-Claude per D-133 M2 standing-discipline lineage-constraint matrix.

Synthesis after independent-phase produces `01-deliberation.md` per `multi-agent-deliberation.md` v4 §Synthesis: citation discipline (cite source-file + Q#); `[synth]` markers for synthesizer-original claims; quote-over-paraphrase for load-bearing claims; convergence-vs-coverage distinction; preserve dissent.

**Engine state at session-open** (you reason from this state; do not modify):
- 13 active open issues (`open-issues/index.md`).
- 36 first-class minorities preserved engine-wide (`workspace-structure.md` v6 §10.4 + spec-local §10/§7 blocks).
- 8 engine-feedback lifecycle records (1 external + 7 self-dev-originated; 6 resolved + 2 triaged + 0 new).
- Engine-v9 preservation depth: 7 sessions (S050→S057); second-longest in workspace history after engine-v7 11-session record (S036→S048).
- Phase-1 retrieval substrate operational: `search` + `resolve_id` + `forward_references` MCP tools per `retrieval-contract.md` v1.

## §2 Problem statement (shared)

### §2.1 EF-055 framing

You are deliberating on `engine-feedback/inbox/EF-055-substrate-aware-format-and-archive-rethink-substantive-arc.md` (committed Session 055 post-close as operator-surfaced intake; triaged at S056 per D-191 + D-192 as substantive-arc deferred-to-MAD; S057 produced design-space.md as primary input + pre-ratified this S058 MAD per D-194 + D-195 + D-196).

**Observation (verbatim from EF-055 intake)**: "Files in the workspace's default-read surface that grow accretively impose a structural read-to-edit cost paid every session (or every substantive event). The cost compounds with workspace age and is not addressed by the existing periodic-restructure precedent chain (S022 R8a / S040 D-123 / S051 D-178), which defers ceiling pressure but does not change the linear-growth shape."

The intake names three direction candidates:
- **Direction A** (operator-stated preference at intake): substantive Substrate-N2 reframe arc activating §10.4-M10 — structured records as source-of-truth; markdown as witness; accretive blocks become thin indices pointing to per-record files; engine-v10 candidate.
- **Direction B**: tactical thin-index extension to `SESSION-LOG.md` alone via Path L+A — minor per OI-002 per S022/S040/S051 precedent chain; no engine-v bump.
- **Direction C**: defer until §10.4-M10 written warrants ((a) phase-2+ maintenance time exceeds projection 2× across 3 consecutive sessions; (b) multi-hop cross-reference query class dominates ≥5× prose-search over a 5-session window) empirically fire.

Per S056 D-192 + S057 D-196: triage authorises deliberation; operator preference is durable input not foreclosure (no `operator_directed_resolution` frontmatter field; S048 D-153 short-circuit precedent does NOT apply).

### §2.2 Workspace state (measured at S057 open per design-space.md §2)

Default-read aggregate at S057 close: **80,161 words / 21 files** (validator-measured). Headroom to 90K soft ceiling: ~9,839 words.

Per-file breakdown of default-read files relevant to EF-055 (measured at S057 open):

| File | Words | Class | Growth shape |
|------|-------|-------|--------------|
| `SESSION-LOG.md` | 7,390 (S057) | development-provenance | strictly linear-per-session |
| `specifications/engine-manifest.md` | ~5,184 | engine-definition | linear-per-engine-v bump |
| `specifications/workspace-structure.md` | ~3,918 | engine-definition | linear-per-Path-PD-minority |
| `specifications/reference-validation.md` | 7,177 | engine-definition | linear-per-RV-revision-minority |
| `specifications/retrieval-contract.md` | ~2,323 | engine-definition | linear-per-MAD-minority |
| `engine-feedback/INDEX.md` | ~934 | non-engine-operator-managed | linear-per-feedback-record |
| `specifications/aliases.yaml` | ~244 | engine-adjacent | bounded; already structured |
| `open-issues/index.md` | ~667 | development-provenance | bounded by OI-resolution discipline (model exemplar) |

**Accretive sections within default-read** (~15,300 words / ~19% of aggregate):

| Section | Words | Entries | Avg/entry |
|---------|-------|---------|-----------|
| `engine-manifest.md` §7 (engine-v history) | ~3,780 | 9 | 420 |
| `workspace-structure.md` §10.4 (preserved minorities) | ~1,248 | 11 | 113 |
| `reference-validation.md` §10 (preserved minorities) | ~1,814 | 9 | 201 |
| `retrieval-contract.md` §7 (preserved minorities) | ~499 | 5 | 100 |
| `SESSION-LOG.md` (rows) | 7,390 | 56 | 132 |
| `engine-feedback/INDEX.md` (records) | ~934 | 8 | 117 |

**Ceiling pressure**: SESSION-LOG.md at 7,390 words crosses 6K soft warning third-consecutive close (per WX-34-1). At S057 row-density cadence (~330-400 words/session), S058 close approaches 7,720-7,790; S059 close approaches 8,050-8,180 (8K hard ceiling breach). reference-validation.md v3 at 7,177 words is **already over the 6K soft threshold** since S033 v3 adoption.

### §2.3 Substrate-N2 reframe origin (S050 P3 + P4 per archive-surface citations)

Per `provenance/050-session/01c-perspective-outsider-frame-completion.md` §2 Substrate-N2 (preserved verbatim):

> "Decisions, OIs, minorities, watchpoints, archive citations, session summaries, and cross-spec sync obligations become structured source-of-truth records, with Markdown rendered or assembled from those records. The durable substrate is not 'Markdown plus index'; it is a structured fact corpus, perhaps JSONL files under `records/` or a workspace-local SQLite database with exportable Markdown witnesses."

Per same source §1 Frame Critique:

> "Selvedge may not need a search product as much as it needs a fact discipline. The corpus is already heavily ID-structured. If each session writes durable thin rows for decisions, open issues, minorities, edges, and archive references, then a database can be rebuilt from those rows without re-interpreting prose."

P3's S050 own §2 Substrate-N2 paragraph noted: "**This option is probably too disruptive for S050 adoption, but it is the correct counter-frame.**" P4 dissent-preservation rec 4 preserved as first-class minority §10.4-M10 per S050 D-172.

S050 P3 also surfaced **Substrate-N3** as a practical bridge: "keep Markdown as source of truth, but require close-time append or regeneration of structured registries (`identifiers.jsonl`, `edges.jsonl`, `archive_paths.jsonl`, `minorities.jsonl`, perhaps `sessions.jsonl`). The SQLite or DuckDB database is then a generated read model from registries plus Markdown FTS." P3 named Substrate-N3 as their "preferred Substrate-N shape: not 'choose DuckDB or SQLite and hope extraction is right', but 'make the facts explicit, then choose the smallest durable read model.'"

Phase-1 retrieval substrate (engine-v9) implements the read-model layer: `search` + `resolve_id` + `forward_references`. S055/S056/S057 organic-use established that the substrate provides genuine cross-reference navigation that previously required prose-scan reading.

### §2.4 Cost/benefit matrix (qualitative per design-space.md §5; you may dispute)

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

### §2.5 Cross-spec interactions (Direction A scope per design-space.md §6)

Direction A's substantive scope necessarily revisits multiple specs:

- **`read-contract.md` v5**: §1 default-read enumeration may extend; §2 budget calibration; §2c retention-window value (substrate makes "older closes" still queryable); §4 archive-pack structure simplification.
- **`workspace-structure.md` v6**: file-class extension for "per-record-indexed files"; §10.4 reshape; §provenance per-record-file immutability discipline.
- **`engine-manifest.md`**: §3 file enumeration if per-version directory adopted; §7 reshape; §5 versioning trigger.
- **`reference-validation.md` v3**: §10 reshape.
- **`retrieval-contract.md` v1**: §7 reshape; §7/§10.4 mirroring discipline question.
- **MAD/VA**: do not currently carry §10-style minority blocks (preserve dissent inline within deliberation provenance); EF-055 reframe does not directly target them.
- **`tools/validate.sh` + `tools/build_retrieval_index.py`**: check 20 default-read enumeration; possibly new check 25 for per-record-file integrity; index-rule adjustments if directory structure changes.

## §3 Design questions (shared)

Address each Q1-Q8 in your response. Frame opinions explicitly; cite reasoning.

**Q1 — Primary direction choice**: Direction A, B, C, or alternative architecture (1/2/3/A+Alt3)? Justify with cross-axis reasoning per the matrix in §2.4. Articulate the position you reach without seeing other perspectives' answers.

**Q2 — Adoption scope (if Direction A or substantive variant)**: which accretive blocks migrate in phase 1? Phase 2? What is the migration sequence? If you do not adopt Direction A, what should phase scope look like for the direction you do adopt?

**Q3 — Per-record-file directory structure (if Direction A)**: `specifications/minorities/` vs. distributed-across-spec-source-directories? Naming convention (`M-NNN.md` vs. `<id>.md`)? File-class classification?

**Q4 — Index format**: thin-table-row pattern per `open-issues/index.md` model? Status column convention? Path-pointer convention? If different from open-issues exemplar, why?

**Q5 — Validator + tool updates**: new check 25 for per-record-file integrity? Build-retrieval-index.py rule changes? What's the testing strategy for new checks?

**Q6 — Cross-spec interactions**: which §6 interactions are in-phase-1 scope vs. deferred? Specifically: which of `read-contract.md` revisions, `workspace-structure.md` revisions, `engine-manifest.md` revisions, `reference-validation.md` revisions, `retrieval-contract.md` revisions, `tools/validate.sh` revisions are essential at phase-1; which are deferrable?

**Q7 — Multi-session arc shape**: 2 sessions (single-MAD adoption with phase-3 in same session) vs. 3-4 sessions (staged migration)? What constitutes a clean phase-boundary for staging?

**Q8 — Operator-stated preference treatment**: Direction A is operator-stated preference; how should the MAD treat this? Durable input (S048 D-155 precedent) or one position among others? What is your specific interpretation, and how does it affect your own answer to Q1?

### Open questions (consider beyond Q1-Q8 if you have insight)

Per design-space.md §8:

1. **Substrate-availability assumption**: Direction A's pattern depends on substrate continuing to function. Should the design require fallback discoverability (e.g., aggregate index file) for substrate-absent operation?

2. **Per-record-file immutability discipline**: D-017 immutability applies once a session closes. If a minority is re-discharged or re-vindicated in a later session, does the per-minority file get appended (multiple status entries chronologically) or does the index status get updated while the file remains stable?

3. **Multi-spec minority cross-references**: §10.4-M7 through §10.4-M11 are mirrored in `retrieval-contract.md` §7.1 through §7.5. Under per-record-file pattern, do both specs reference the same `M-NNN.md` file, or do mirrored minorities have separate files?

4. **Engine-version per-version files vs. §7 history block**: if `specifications/engine-versions/v{N}.md` per-version files are adopted, do they replace `engine-manifest.md` §7 entirely or coexist with a thin §7 index pointing at them?

5. **Migration ordering**: should `SESSION-LOG.md` migrate first (Direction B subset) or last (after spec-block patterns are proven)?

6. **Archive-pack discipline for pre-restructure state**: per S022 R8a / S040 D-123 / S051 D-178 precedent. Under Direction A, each accretive block reshape produces a pre-restructure archive-pack. Should there be aggregate retention rules?

7. **External-application portability**: at engine-v10, external workspaces via `tools/bootstrap-external-workspace.sh` would inherit the per-record-file pattern. Is the bootstrap contract sufficient or does it need extension?

8. **Cross-linkage to S047 D-150 deferred candidate (i)** (kernel §7 qualitative-multi-agent label): EF-055 triage record §Forward-dependency-observations names this as possible scope overlap with Direction A. Should the MAD engage candidate (i) or defer per S047 D-150 chain?

## §5 Response format (shared)

Produce a markdown document with the following sections:

1. **Frame Critique** (~200-400 words): is the problem-frame in §2 the right frame? Are there reframes you would propose? What is the question that the deliberation is really answering?

2. **Q1 — Primary direction** (~300-500 words): your direction choice with cross-axis reasoning.

3. **Q2-Q8 — Secondary questions** (~80-200 words each): focused answers to each design question.

4. **Open questions you address** (~50-150 words each, only those you have specific insight on; skip others).

5. **Anti-laundering self-check** (~100-200 words): what criteria did you strain to make your answer work? What would falsify your position?

6. **Counter-frames for the dominant Claude position** (P3 + P4 only; ~200-400 words): if P1 + P2 likely converge on X, what shared assumption are they making that may be wrong?

7. **Dissent-preservation recommendations** (P4 only; ~100-300 words): what positions, if they lose synthesis, should be preserved as first-class minorities? With what activation warrants?

Target total length: P1 ~3,000-5,000 words; P2 ~2,500-4,000 words; P3 ~2,000-3,500 words; P4 ~2,000-3,500 words.

## §6 Constraint on external imports (shared)

Reason primarily from this brief. If your reasoning surfaces an external concept (a design pattern from your pretraining; a tool you have read about; a methodology from a different domain), introduce it explicitly with the marker `[external]:` and explain why it bears on the question. Do not commit external ideas as if they emerged from the brief alone.

The brief contains:
- §1 methodology context.
- §2 problem statement including measurement, Substrate-N2 origin, cost/benefit matrix, cross-spec interactions.
- §3 design questions Q1-Q8 + 8 open questions.

You should not need to read workspace files during the independent phase. If a question requires workspace lookup beyond the brief, flag it explicitly and proceed under best-available understanding.

This brief is the deliberation's anchor. Independence is preserved by all four perspectives reasoning from this byte-identical brief without seeing each other's answers until synthesis. The synthesis step is the highest-risk single-agent re-entry point per `multi-agent-deliberation.md` v4 §Limitations; preserve dissent verbatim and quote rather than paraphrase load-bearing claims.

End of shared brief.
