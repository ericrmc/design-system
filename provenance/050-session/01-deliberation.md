---
session: 050
title: Deliberation synthesis — retrieval substrate adoption under operator §2a correction-overlay + Halt-1 Q6 external-application-portability scope expansion; 4-perspective two-family MAD P1 Substrate Architect + P2 Incrementalist Skeptic + P3 Outsider Frame-Completion + P4 Cross-Family Reviewer Laundering-Audit
date: 2026-04-24
status: synthesis-complete
synthesis_by: Case Steward (Claude orchestrator)
---

# Deliberation — Session 050

## §0 Perspectives at a glance

| Perspective | Family | Model | Role | Words |
|-------------|--------|-------|------|-------|
| P1 Substrate Architect | Claude | claude-opus-4-7 | Neutral surveyor per Halt-1 Q4; advocacy emerges from evaluation | 6,329 |
| P2 Incrementalist Skeptic | Claude | claude-opus-4-7 | Minimum viable; defer as first-class option; phased gates | 5,142 |
| P3 Outsider Frame-Completion | Codex | gpt-5.5 xhigh | Substrate-as-fact-discipline reframe; Substrate-N1/N2/N3 surfaced | ~2,300 |
| P4 Cross-Family Reviewer | Codex | gpt-5.5 xhigh | Laundering audit; convergence-check; shared-frame-blindness | ~2,100 |

**D-133 M2 Convene-time matrix (per S045 R2 + M2 lineage-constraint)**: 4 seats / 2 families / 2 Claude (Opus 4.7 1M context) + 2 Codex (gpt-5.5 xhigh) / Outsider seat non-Claude (gpt-5.5) per 21-for-21 convention / synonym-drift guard: P3 frame-completion distinct from P4 laundering-audit — distinct roles exercised distinctly (P3 proposed Substrate-N1/N2/N3 and reframed the problem; P4 audited P1+P2 specifically for Claude-lineage patterns and named blind spots). Departure-discipline: no mid-session composition revision; all four perspectives landed within target length.

**§5.6 GPT-family-concentration observation**: 2 Codex + 2 Claude + 0 non-GPT-non-Claude — fourth consecutive worst-case-side substantive-deliberation data point (S044+S045+S047+S050). Discharge/continued-preservation evaluable at close §5 below.

**WX-43-1 explicit-instruction variant**: all four perspectives received do-not-self-commit instruction in shared-brief §0c. Observed: 4-of-4 honoured the instruction (no git operations attempted by any perspective; Case Steward committed). Cumulative explicit-instruction-variant window: n=0-of-9 self-commit breaches across S047 (3) + S049 (3) + S050 (4).

## §1 Q-by-Q convergence/divergence map

### Q1 — Primary substrate choice

**Convergence 4-of-4**: Substrate-1 SQLite FTS5. Rationales differ:
- P1: three tie-breakers (dependency floor for external-workspace portability; ecosystem maturity over 2–5 year horizon; snippet/highlight FTS5-native).
- P2: zero install beyond Python+FastMCP; adoption-by-anticipation (DuckDB structured-filter dominance) is unevidenced.
- P3: minimize distribution risk; SQLite under a registries-first architecture (Substrate-N3).
- P4: provisional phase-1 only; DuckDB preserved as minority if structured queries prove dominant.

**Divergence**: depth of the commitment.
- P1: primary-substrate-final.
- P2: primary-substrate-provisional (but firm in phase 1).
- P3: read-model under a Substrate-N3 architecture that treats **write-time registries** as the actual substrate.
- P4: provisional-not-final; requires measured query evidence before foreclosing DuckDB.

**Preserved minority**: DuckDB structured-first substrate (P4 dissent-preservation rec 2). If structured-filter + graph-traversal queries prove dominant in measured evidence, SQLite may be wrong long-term substrate despite phase-1 win.

### Q2 — Adoption scope

**Divergence 3-of-4 vs 1-of-4 outlier**:
- P1: phase-1 = `documents` + `identifiers` + `docs_fts` + 3 MCP tools (`search`, `resolve_id`, `list_identifiers`); phase-2 adds `edges`+`frontmatter_kv`+`traverse`+`warrants_currently_met`; phase-3 adds validator check 24 + kernel §1a amendment.
- P2: phase-1 = single FTS5 table + 2 MCP tools (`search`, `resolve_id`); nothing else.
- P3: phase-1 = `documents` + `identifiers` + `archive_paths` + minimal `edges` + 3 MCP tools (`search`, `resolve_id`, `verify_archive_path`); defer `warrants_currently_met`.
- P4: P2's phase-1 minimum is safer. Don't silently adopt P1's larger surface under phased language.

**P4 identified P1's highest laundering risk**: P1's Architecture §3 proposes the full schema + all tools + all file-plan edits (`methodology-kernel.md`, `engine-manifest.md`, `validation-approach.md`, `validate.sh`, `read-contract.md`) — full-kit surface — while Q2 says "phase-1 is only 3 tools". The answer labels itself phased but preserves the full-kit surface in the architecture section. Genuine inconsistency.

**P4 identified P2's technical under-specification**: P2's `resolve_id(alias) -> {canonical, source_path}` cannot work without an identifiers table. The phase-1 shape must name the identifiers table explicitly rather than smuggling it.

**Preserved minority**: P1's larger surface-area phase-1 (P4 dissent-preservation rec 1 captures the mirror: P2's defer-with-instrumentation).

### Q3 — Kernel §1 amendment shape

**Convergence 3-of-4 (P2+P3+P4) on soft-or-defer; P1 outlier**:
- P1: hard amendment now (§1a Warrant-evaluation sub-activity, with degradation clause if substrate unavailable).
- P2: defer amendment to phase 2; soft when added ("call tool if available; prose-scan fallback").
- P3: required retrieval checks now (phrased as contract, not tool call); degraded mode must be visible in session record; silent fallback is methodology failure.
- P4: no hard amendment in phase 1; if later, soft.

**Synthesis**: no kernel amendment in phase 1. A kernel rule that depends on an unproven MCP server couples methodology to tool operational state before evidence exists. Phase 2 may add a soft sub-activity.

### Q4 — Alias vocabulary

**Convergence 3-of-4 on two-label; P1 outlier on SKOS-three-label**:
- P1: SKOS three-label (prefLabel/altLabel/hiddenLabel) at adoption.
- P2: two-label (canonical + aliases) at adoption; SKOS in phase 3 if needed.
- P3: two-level schema (canonical + observed_aliases + optional kind/source_session/notes).
- P4: two-label first; YAML schema version-tagged so SKOS upgrade is clean.

**Synthesis**: two-label with explicit `schema_version: 1` in the YAML.

### Q5 — Rebuild trigger

**Split 2-of-4 vs 2-of-4**:
- P1: both (mtime + post-commit hook).
- P2: mtime-only (no hooks; hooks are invisible state).
- P3: both, with session-open mtime authoritative; post-commit is convenience; stale/fresh must be reported.
- P4: mtime-only in phase 1; optional repeat on tool-call if cheap.

**P4's reasoning is decisive**: post-commit hooks are invisible state, poorly portable across fresh clones and external workspaces, awkward to guarantee through bootstrap. P3's agreement that mtime is authoritative and hooks are convenience supports deferring hooks.

**Synthesis**: session-open mtime check only in phase 1. Post-commit hook deferred to phase 3+.

### Q6 — `syncs_with:` frontmatter field

**Convergence 4-of-4 on defer-phase-1; divergence on the conceptual question**:
- P1: fold into `edges` at phase 2.
- P2: defer; re-evaluate when `edges` exists.
- P3: keep as declaration-of-intent, distinct from extracted edges (edges = what's cited; syncs_with = what must co-evolve).
- P4: defer, but preserve the distinction.

**Synthesis**: defer implementation; **explicitly preserve the P3/P4 declaration-of-intent distinction as a first-class minority** (P4 dissent-preservation rec 5). When `edges` exists (phase 2), re-evaluate with the distinction on the table — do not fold-in-by-default.

### Q7 — External-application inheritance (LOAD-BEARING per Halt-1 Q6)

**Divergence 3-of-4 on engine-adjacent/middle-path vs 1-of-4 (P1) engine-definition**:
- P1: engine-definition (add substrate files to `engine-manifest.md` §3 at v8→v9).
- P2: engine-adjacent tooling. Promotion to engine-definition only after 3+ stable versions + 2+ external-workspace adoptions.
- P3: **middle path** — engine-defined *contract* (required tool names, bootstrap behavior, failure behavior, registry schemas) + adjacent-copied *implementation* + workspace-local generated state.
- P4: engine-adjacent for now; promotion requires stability evidence.

**P3's middle path is the strongest resolution**: it addresses P1's correct concern (that the kernel/validator depending on a tool-inconsistently-inherited would be asymmetry per OI-017 spirit) without locking the methodology to substrate implementation churn (P2's correct concern). The contract is engine-definition; the implementation is engine-adjacent.

**Synthesis**: adopt P3's middle path.
- NEW engine-definition spec: `specifications/retrieval-contract.md` — declares required tool names, shapes, failure behavior, registry schemas, bootstrap contract.
- ENGINE-ADJACENT tooling (not added to `engine-manifest.md` §3): `tools/build_retrieval_index.py`, `tools/retrieval_server.py`, `.mcp.json` template, `specifications/aliases.yaml` (scaffold).
- `tools/bootstrap-external-workspace.sh` extended per §2 below.
- `.cache/retrieval.db` workspace-local, gitignored.

**Preserved minority**: P1's engine-definition at adoption (P4 dissent-preservation rec 3). The promotion question is explicitly live: re-evaluate at S053–S055 if substrate proves stable and at least one external-workspace has exercised it.

### Q8 — Validator check 24 scope

**Convergence 3-of-4 on defer-to-phase-2; P1 outlier on phase-3**:
- P1: phase-3.
- P2: phase-2 gated on substrate availability (skip if absent; fail if present + missing pointers).
- P3: start with minority + archive-path verification; report-only unresolved-ID inventory first.
- P4: defer until identifiers table exists (which is phase-1 under synthesis below); minority + archive-path scope; skip-if-absent.

**Synthesis**: defer check 24 to phase 2. When added: narrow scope (preserved-minority pointer coverage + archive-path existence); skip-if-substrate-absent; hard-fail only once declared required. External-workspace behavior per P3: distinguish inherited engine minorities from application-local minorities.

## §2 Phase-1 adoption architecture (synthesized)

**Substrate-1 (SQLite FTS5) implemented under Substrate-N3 framing (P3) at phase-1 minimum scope (P2 corrected by P4):**

### §2.1 Tables + FTS (phase-1)

```sql
CREATE TABLE documents (
  path TEXT PRIMARY KEY,
  kind TEXT NOT NULL,
  session INTEGER,
  mtime REAL NOT NULL,
  title TEXT,
  frontmatter_json TEXT,
  body TEXT NOT NULL
);

CREATE TABLE identifiers (
  id_text TEXT NOT NULL,
  id_kind TEXT NOT NULL,
  canonical TEXT NOT NULL,
  source_path TEXT NOT NULL,
  line INTEGER,
  context_snippet TEXT,
  PRIMARY KEY (id_text, id_kind, source_path, line)
);
CREATE INDEX idx_ids_canonical ON identifiers(canonical, id_kind);

CREATE VIRTUAL TABLE docs_fts USING fts5(
  path UNINDEXED, title, body,
  content='documents', content_rowid='rowid',
  tokenize='porter unicode61 tokenchars ''-_§'''
);
```

Phase-1 schema is 2 tables + 1 FTS virtual table. **Not** phase-1**: `frontmatter_kv`, `edges`, `aliases` table (aliases stays in YAML in phase-1).

### §2.2 MCP tools (phase-1)

```python
@mcp.tool()
def search(query: str, k: int = 10) -> list[dict]:
    """BM25 full-text search. Returns [{path, snippet, score}]."""

@mcp.tool()
def resolve_id(alias: str) -> dict | None:
    """Resolve an alias or canonical identifier to its authoritative location.
    Returns {canonical, kind, source_path, line, context} or None."""
```

Two tools. **Not** phase-1: `list_identifiers`, `traverse`, `warrants_currently_met`, `verify_archive_path`.

### §2.3 Alias file (phase-1)

`specifications/aliases.yaml`:

```yaml
schema_version: 1
aliases:
  - canonical: "§10.4-M5"
    kind: minority
    aliases: ["M5", "Reviser OI-tag-only", "§10.4-minority-5"]
  # ... populated incrementally
```

Two-label with versioned schema for future SKOS migration.

### §2.4 Indexer (phase-1)

`tools/build_retrieval_index.py` — Python stdlib + `pyyaml`:
1. Walk `*.md`; exclude `.git/`, `.cache/`, `.claude/`, superseded spec versions matching `-v[0-9]+\.md$`.
2. Parse frontmatter + body; classify `kind`; extract `session` from path.
3. Regex-extract IDs per a centralised pattern registry (D-NNN, OI-NNN, §N-MN, WX-N-N, session, engine-vN, EF-*, d01N_N).
4. Load `aliases.yaml`; resolve `id_text → canonical`.
5. INSERT `documents` → INSERT `identifiers` → rebuild `docs_fts`.
6. `VACUUM` + `PRAGMA integrity_check`.

Estimated ~200 LOC.

### §2.5 MCP server (phase-1)

`tools/retrieval_server.py` — FastMCP stdio server with the two tools above. ~120 LOC.

### §2.6 Rebuild trigger (phase-1)

Session-open mtime check. MCP server checks `max(*.md mtime) > retrieval.db mtime` on startup; rebuilds if stale. No post-commit hook.

### §2.7 External-application portability (phase-1)

- NEW engine-definition spec: `specifications/retrieval-contract.md` — declares the required tool names (`search`, `resolve_id`), their signatures, failure behavior (fallback to lexical tools with visible degradation record), registry schemas, the `.mcp.json` shape, and the bootstrap contract (what must be installed; what must work after bootstrap).
- Implementation is engine-adjacent (not added to `engine-manifest.md` §3 engine-definition file list).
- `tools/bootstrap-external-workspace.sh` extended: copies `tools/build_retrieval_index.py` + `tools/retrieval_server.py` + `specifications/aliases.yaml` template + `.mcp.json` template; prints `pip install` instructions for `mcp[cli]` + `pyyaml`; builds initial index; prints next-steps output.
- External workspaces carry their own workspace-local `.cache/retrieval.db` (gitignored).

### §2.8 Not in phase-1 (deferred with explicit gates)

- `edges` table + `frontmatter_kv` table.
- `traverse` + `warrants_currently_met` + `list_identifiers` + `verify_archive_path` MCP tools.
- Kernel §1a Warrant-evaluation sub-activity.
- Validator check 24.
- `syncs_with:` frontmatter field.
- SKOS three-label alias vocabulary.
- Post-commit git hook.
- Engine-manifest.md §3 inclusion for substrate implementation files.

## §3 Phase-2 gate (per P4 normalized recommendation)

**Through S053, every session close records retrieval use in a 3-field section**:

```markdown
## Retrieval substrate use (WX-50-1)

- **tool_calls_by_type**: {search: N, resolve_id: N}
- **results_used_with_artefact_id**: [{tool, query, returned_artefact_path, used_in_decision_or_oi_or_minority_id}]
- **fallbacks_due_to_missing_capability**: [{query_intent, why_phase_1_did_not_suffice}]
```

**Phase-2 fires when** any of:
- Two sessions in S050–S053 record ≥1 useful result (entry in `results_used_with_artefact_id`).
- One session records ≥1 entry in `fallbacks_due_to_missing_capability` where the missing capability is structured-filter or graph-traversal.
- One external-workspace adoption records ≥1 useful domain-context query.

**Phase-2 does NOT fire** if the triggers are not met in S050–S053. Otherwise **pause expansion** (do not necessarily deprecate).

**Phase-2 deliverables (if triggered)**:
- Add `edges` table + `frontmatter_kv` table + `list_identifiers` + `traverse` + `warrants_currently_met` + `verify_archive_path` MCP tools (as evidence dictates; not auto all).
- Add validator check 24 (gated; minority + archive-path scope).
- Soft amend `methodology-kernel.md` §1 Read with Warrant-evaluation sub-activity (tool-optional).
- Re-evaluate `syncs_with:` question with the distinction preserved per §1 Q6 above.

Phase-3 and beyond: dedicated MADs at that time.

## §4 Preserved first-class minorities (per P4 dissent-preservation recommendation)

The MAD preserves five first-class minorities from this deliberation. Each carries a specific activation warrant; preservation is engine-wide (in the adopted retrieval-contract.md §Minorities block or as annex to §10.4 in `workspace-structure.md`).

1. **P2 minimum-adoption / defer-with-instrumentation** (§10.4-M7 candidate). *Position*: adoption should earn expansion through measured use, not anticipated architecture. *Activation warrant*: if phase-2 gate fails to fire across S050–S053 AND zero use recorded for phase-1 tools in ≥3 consecutive sessions, revisit whether phase-1 should have shipped at all.

2. **DuckDB structured-first substrate** (§10.4-M8 candidate). *Position*: if structured filters and graph traversal prove dominant, SQLite may be the wrong long-term substrate despite winning phase-1. *Activation warrant*: any session in which phase-1 tool use shows structured-filter / graph-traversal queries dominate prose-search queries by ≥3× count over a 5-session window.

3. **Engine-adjacent before engine-definition** (§10.4-M9 candidate). *Position*: portability can be load-bearing without making unstable retrieval code part of the engine-definition file set. Since this is the *synthesis* position, the mirrored minority is **P1's engine-definition-at-adoption**: the capability is important enough that it warrants engine-definition classification now, not deferred. *Activation warrant*: if an external-workspace adoption exposes inconsistent inheritance (workspace A and workspace B have divergent substrate implementations that produce different answers), the engine-definition case re-enters deliberation.

4. **Structured artefacts as source-of-truth reframe** (§10.4-M10 candidate; P3 Substrate-N2). *Position*: the shared markdown-plus-index frame should not be mistaken for the only scalable answer; decisions, OIs, minorities, etc. may eventually become structured records with markdown as witness. *Activation warrant*: if the substrate's phase-2+ maintenance cost exceeds projections by ≥2× OR if multi-hop cross-reference queries become the dominant operational burden, revisit Substrate-N2 as a multi-session arc.

5. **`syncs_with:` as declaration-of-intent** (§10.4-M11 candidate; P3+P4). *Position*: extracted edges may not replace explicit co-evolution commitments; "what is cited" ≠ "what must co-evolve". *Activation warrant*: phase-2 `edges` existence does not auto-fold `syncs_with:`; phase-2 deliberation re-examines with this distinction explicitly preserved.

**Count impact**: 31 preserved first-class minorities → 36 at S050 close (5 new from this MAD). Minority index update required in `specifications/workspace-structure.md` v5 §10.4 (or a retrieval-contract.md §Minorities block if the new spec hosts them — Decide at §2 decisions).

## §5 Shared-frame-blindness assessment (per P4)

P4 named the shared Claude+derivation frame: *"plain markdown canonical + local Python-built index + FastMCP exposure + external workspaces through bootstrap + each workspace indexes itself in isolation."* This frame dominates P1+P2+P3 despite P3's partial reframe.

**Session 050 data point for EF-047-session-inputs forward-observation** (shared-frame-blindness measurement): P3's Substrate-N1 (retrieval ledger) + Substrate-N2 (structured artefacts replace prose) + part of P3's portability reframe (engine-defined contract + adjacent-copied implementation) count as genuine frame-completion NOT within the shared Claude frame. P4 explicitly named the blind spots. The MAD did NOT exhibit 4-of-4 shared-frame convergence; P3 surfaced alternatives that the Claude perspectives did not, and P4 audit-confirmed this.

**§5.6 GPT-family-concentration evaluation**: per P4's shared-frame assessment, the Codex-family contribution (P3+P4) is **substantive and load-bearing** in this synthesis. The §2 architecture adopts P3's middle path (Q7) and P4's normalized phase-2 gate (§3 above). The fourth-consecutive-substantive-deliberation data point supports continued-preservation of §5.6 minority (no 2-of-4-Claude frame-collapse; worst-case-side composition did not produce worst-case-outcome). Spirit-level §5.6 observation carries forward but no discharge/vindication at S050.

## §6 Case Steward meta-notes

- **WX-43-1 explicit-instruction variant**: 4-of-4 honoured; cumulative window n=0-of-9 across S047+S049+S050.
- **P4 internal-inconsistency flag on P1**: the full-kit-surface-vs-phased-answer tension. Resolved in §2 by removing `list_identifiers` from phase-1 and deferring all file-plan edits except the new `retrieval-contract.md`.
- **P4 smuggled-identifiers flag on P2**: resolved by keeping the `identifiers` table in phase-1 (P2 would accept under P4's correction; the smuggling was technical, not intentional).
- **P3 frame-completion impact**: the `retrieval-contract.md` spec is a direct adoption of P3's "engine-defined contract" (§2.7 + Q7 synthesis). The substrate-as-fact-discipline framing shapes the contract's requirements on write-time registry behaviour (though phase-1 does not ship registries; only the contract leaves space for them at phase-2).
- **Preserved minorities**: §4 above. These are engine-scope minorities per workspace-structure.md v5 §10.4 conventions; each carries specific activation warrant. Count: +5 → total 36.
- **No minority retracted by synthesis**.
- **D-133 M2 third-of-3 verification window** vindication: S045 + S047 + S050 all exercised Convene-time 7-column matrix + lineage-constraint (Outsider MUST non-Claude) + synonym-drift guard + departure-discipline. All four instances held cleanly at S050. Window recommendation: **vindicated** (see §2 D-163 below for formal decision).
- **§10.4-M2 (Skeptic-preserver continued preservation)**: pathway exercised at adoption edge (triage→resolved transition candidate). Continued preservation consistent; no discharge trigger.
- **§10.4-M5 (Reviser OI-tag-only discharged-as-vindicated)**: S048 disposition preserved.

## §7 Handoff to §2 decisions

This deliberation resolves:

- **Q1** → Substrate-1 SQLite FTS5 (4-of-4).
- **Q2** → Phase-1 minimum: `documents` + `identifiers` + `docs_fts` + 2 MCP tools (`search`, `resolve_id`). Phase-2 gated per §3.
- **Q3** → No kernel amendment in phase-1; soft amendment in phase-2 if triggered.
- **Q4** → Two-label aliases with `schema_version: 1`.
- **Q5** → Session-open mtime only.
- **Q6** → Defer; preserve declaration-of-intent distinction as first-class minority.
- **Q7** → Engine-defined contract + engine-adjacent implementation (P3 middle path).
- **Q8** → Defer to phase-2 gated.

Ancillary decisions required at §2:
- Bundled-minor EF-047-brief-slot-template + EF-047-session-inputs dispositions.
- Housekeeping (close-rotation, D-129 exercise clean, D-138 folder clean, etc.).
- SESSION-LOG Q5=(a) thin-row at close.
- Engine-v8→v9 bump (new spec + new engine-adjacent tooling + substantive new behaviour per OI-002 heuristic).

End of deliberation.
