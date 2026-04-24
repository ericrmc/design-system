---
title: Perspective — P2 Incrementalist / Maintenance Sceptic (Session 050)
session: 050
perspective: incrementalist-skeptic
perspective_family: claude
perspective_role: incrementalist-skeptic
date: 2026-04-24
status: immutable-at-commit
---

# P2 — Incrementalist / Maintenance Sceptic

## 0. Top-line position

Adopt, but adopt minimally. The "defer" case is respectable and I will argue it seriously in §1, but the workspace has crossed an honest threshold where the write-side preservation discipline has produced structure the read-side tools can no longer reach efficiently, and a modest substrate earns its keep in 6–12 months. I recommend **Substrate-1 (SQLite FTS5), phase 1 only**: one regular-contentful FTS5 virtual table over whole files, plus exactly two MCP tools (`search`, `resolve_id`), plus a resolver over a two-label aliases file, plus workspace-relative `.cache/` location, plus ripgrep as documented floor. Nothing else in this session.

I reject full-kit adoption and I reject the "five tables at once" design-space shape (§3.2 of design-space). The 2500-word scepticism that follows is not reflexive contrarianism — it is the specific observation that in a methodology whose distinctive claim is "diverse perspectives reasoning together produces durable artefacts over years," a substrate that costs 400–500 LOC + 2 MCP files + 1 .mcp.json + 1 aliases file + 1 new validator check + 1 kernel amendment, all committed in one session, is not an increment. It is an architecture. And an architecture that enters engine-definition and bootstraps into every future external-application workspace is a decision about the dependency floor of the Selvedge methodology in perpetuity. That decision deserves a much smaller first bite.

## 1. Baseline case for "defer"

The operator's framing correction at S049 ("real scalable technical solutions … real engineering rigour") rules out pure-discipline answers but does not mandate adoption this session. Defer is a legitimate first-class option.

### 1.1 What is wrong with continuing ripgrep + grep + git-log + validate.sh?

Honest answer at current scale: **not much**. The measured state in design-space §2.1–§2.6 and brief §3 reveals that the tools already in hand are doing real work.

- `tools/validate.sh` runs 1,129 structural assertions across 23 checks in a single pass. These are SELECT-JOIN-AGGREGATE queries encoded in bash. Design-space §2.5 is correct that "the workspace is already running a database, just without saying so." The implicit database exists; the question is whether lifting it into an explicit substrate pays back the migration cost.
- `rg -l 'D-152'` returns workspace-wide hits in ~50–150ms (design-space §7.2). That is fast enough for a Case Steward who reads at human-plus-agent latency.
- `git log -S 'retrieval discipline'` surfaces removed prose across 49 sessions with zero installed dependencies. Design-space §7.1 is right that this is a capability no FTS table reproduces — if history is where the evidence lives, git is the substrate.
- The 19-file / 66K-word default-read surface fits comfortably in a 200K-token context. Anthropic's own contextual-retrieval blog post (design-space §6.4 bullet 2) says RAG/embeddings are not needed below ~200K tokens. The read-contract discipline already enforces "load the right small set rather than index the large set."
- The 1.4M-word full corpus sounds large but is 12-month-old growth at a rate of ~28K words/session. The substrate being considered is sized for corpora an order of magnitude larger than what this workspace will reach before S100.

The design-space acknowledges this in §11: "no quantitative measurement of actual-query-class frequency has been performed." I want to sit with that for a paragraph. **We do not have a measured query-volume-by-class inventory of what the Case Steward actually tries to retrieve in a session and fails.** What we have is a narrative argument (EF-047) that retrieval asymmetry exists, a measured static workspace state (design-space §2), and an operator directive that framed it as substrate not discipline. The directive is authoritative on framing; it is not authoritative on "therefore adoption this session." The empirical question "how many Case Steward reads per session would have been faster or more complete with a structured retrieval tool?" has not been measured and cannot be measured retrospectively from text artefacts alone.

### 1.2 Falsifying condition for defer

Defer is not "never". Defer means "not S050; revisit at S055 or S060 with measurement." The falsifying condition — what evidence would force adoption — must be concrete and measurable. Candidates:

- **(F1)** Three consecutive sessions record an honest-limit of the form "at least one load-bearing claim in §X referenced an archive-surface record I did not read because traversal cost was prohibitive under current tools." If this fires, the retrieval asymmetry is producing actual harm to reasoning quality, not just ceremony.
- **(F2)** A validator check failure (e.g., a preserved-minority activation warrant misfires because the warrant's firing condition referenced an identifier that had drifted to a new canonical form across sessions and the Case Steward missed the drift). This would be a **quality** failure traceable to retrieval, not an **ergonomics** failure.
- **(F3)** Corpus growth crosses 3× the default-read hard ceiling for three consecutive sessions without a corresponding close-rotation action; i.e., the write-side shrinking discipline starts failing under volume.
- **(F4)** A single-orchestrator Case-Steward session reports a concrete wrong answer produced in synthesis because a relevant decision, minority, or OI was not surfaced by `rg` + manual walk of default-reads.

If none of F1–F4 fires in 5 sessions, defer was correct. If any fires, adoption is vindicated on evidence, not anticipation.

### 1.3 Counter-argument to defer

The substrate-adopter's strongest rebuttal: "By the time F1–F4 fires visibly, the retrieval asymmetry has already been silently degrading reasoning quality for an unknown number of sessions. You cannot detect silent retrieval-failure from text artefacts alone, because the artefacts never record the decision the Case Steward didn't make because they didn't find the relevant prior." I concede this is a real problem. My response: that same silent-degradation argument applies to *any* future-proofing tax I could name (a graph store; embeddings; a full RDF ontology; agent memory). The asymmetry does not privilege this specific substrate. It privileges **measurement**. If the concern is silent degradation, the first adoption should be **instrumentation that surfaces it**, not architecture that presumes its shape.

**Defer with instrumentation** is therefore my fallback-to-defer recommendation: add a single validator check and a single close-file field (`retrieval-self-assessment: …`) that asks the Case Steward at close whether any read in the session was "I searched but couldn't find" or "I gave up traversing because cost was prohibitive." Three such data points across 5 sessions vindicates adoption. This is 40 LOC of validator and one line of spec amendment.

But I don't think the operator's framing allows this interpretation. "Real scalable technical solutions … not constrained by watching growth" reads to me as a directive against "measure first, adopt later if measurement confirms." So defer-with-instrumentation is my bid for P3/P4 to carry if they see an opening. Otherwise I move to minimal adoption.

## 2. Baseline case for "minimal adoption"

If we must adopt something — and under the operator's framing I grant we must — the smallest useful substrate has exactly the following shape.

### 2.1 Phase 1: the minimum viable substrate

**One database. One FTS table. Two MCP tools. Two aliases columns. Ripgrep as floor.**

```
# Table (SQLite FTS5, regular content-carrying)
docs_fts(path, body, title, session)  -- FTS5 virtual table with BM25

# Aliases (YAML file, not a table)
specifications/aliases.yaml
  - canonical: "D-152"
    aliases: ["Decision 152", "the Path T decision"]

# MCP tools (exposed via FastMCP stdio)
search(query, k=10) -> [{path, snippet, score}]
resolve_id(alias) -> {canonical, source_path} | null

# Indexer
tools/build_retrieval_index.py -- walks *.md, tokenizes body, inserts to FTS5
  session-open mtime check (no git hook; no post-commit automation)

# MCP registration
.mcp.json  (project-scoped, committed)

# Storage
.cache/retrieval.db  (gitignored)
```

**That is the entire first phase.** Estimated LOC: 120–180 indexer, 80–120 MCP server, 10–20 lines of aliases.yaml + .mcp.json. Total new files: 4 (`tools/build_retrieval_index.py`, `tools/retrieval_server.py`, `specifications/aliases.yaml`, `.mcp.json`). Total modified files: 1 (`.gitignore` to add `.cache/retrieval.db`). No kernel amendment. No validator check 24. No `syncs_with:` frontmatter field. No engine-manifest §3 list modification. No `edges` table. No `frontmatter_kv` table. No `warrants_currently_met` tool. No `traverse` tool. No `list_identifiers` tool. No post-commit hook. No SKOS three-label vocabulary.

### 2.2 What this fails to do and whether that is OK for 6–12 months

Failures by design (all OK for phase 1):

- **No graph traversal.** "Find every decision that modified a spec that a minority's activation warrant depends on" must still be done by hand via `rg` + read. **OK**: design-space §11 acknowledges no measurement of this query class frequency exists; if it turns out to be dominant, phase 2 adds an `edges` table. If it turns out to be rare, we never add one.
- **No frontmatter filter queries.** "Every decision whose `triggers_met` includes `d016_2`" still runs as `rg '^\*\*Triggers met:\*\*.*d016_2'`. **OK**: ripgrep already does this fast. Adding a `frontmatter_kv` table is a JOIN that FTS5 handles awkwardly per design-space §4.3; the syntactic friction is not worth the ~50ms `rg` saves.
- **No `warrants_currently_met` tool.** Preserved minorities must still be evaluated by prose scan at session-open. **OK for now**: the validator check 24 proposed in design-space §9.4 presumes the `identifiers` table exists; without it the check is vacuous. Minority activation-warrant evaluation is *currently* done by hand and has been for 49 sessions; the vindicated-not-retracted rate (§10.4-M1 through M6 in workspace-structure.md v5; 31 first-class minorities preserved) suggests this has not been a capability failure so far.
- **No kernel §1 amendment.** The Read activity does not call a tool. **OK for now**: introducing a substrate-dependent kernel amendment locks the kernel's load-bearing semantics to the substrate's availability — which creates exactly the "tool unavailable / index stale / MCP server down → kernel amended but can't execute" failure mode that design-space Q3 correctly raises as a question. Phase 1 treats the MCP tools as *advisory* supplements to manual read, not replacements.
- **No alias discipline in any spec.** `aliases.yaml` is populated as aliases are identified. **OK**: SKOS three-label (design-space §3.3) is premature optimisation for a vocabulary we have not yet exercised. Two-label (canonical + aliases) is the simplest shape that can be refactored to SKOS later without breaking callers.
- **No validator check 24.** **OK**: check 24 should be added in phase 2 *after* the substrate has proved stable across 3 sessions, so the check does not create a new fragility (index-missing → validator fails).

### 2.3 What phase-1 does do

- ID lookup faster than `rg` for the ID-crisp query class (design-space §2.2 measured dominant): sub-millisecond vs 50–150ms. Real win, measurable.
- Alias resolution as first-class operation: "what is `M5`?" returns `§10.4-M5` via `resolve_id`. This was entirely prose-only before.
- Ranked prose search with snippets: search over the full archive-surface corpus, not just default-reads. The first query-class where the substrate genuinely exceeds `rg`'s grep-with-no-ranking return.
- Demonstrable in a single session: one Case Steward session uses `search("retrieval discipline")` and `resolve_id("M5")` during live work and reports whether the tool was faster / more complete / caught something prose-scan missed.

**This is the minimum that lets us measure whether the substrate pays back.** Adding anything beyond this in phase 1 is speculation about what we will want. The phase-2 gate in §5 is the place to answer that.

## 3. Cost surface per candidate

Each Substrate option evaluated on: dependency floor; rebuild time; index size; code LOC; docs burden; debugging surface; external-workspace dependency propagation. I weight external-workspace propagation heavily per §2b of the brief.

### 3.1 Substrate-1 — SQLite FTS5

- **Dependency floor**: Python 3.8+ (stdlib `sqlite3` with FTS5 compiled-in on macOS; Linux/Windows may need `pyyaml`). `mcp[cli]` for FastMCP. That is **2 installs** beyond Python: `mcp[cli]` and `pyyaml`. If an external-workspace host has no Python, that's also an install.
- **Rebuild time**: 140ms for this corpus (design-space §3.5 measured).
- **Index size**: ~18 MiB (design-space §4.1; ~20% of workspace total). Acceptable; gitignored.
- **Code LOC**: phase-1 minimal ~300 LOC total. Full-kit per design-space §4.1: 400–500 LOC.
- **Docs burden**: FTS5 tokenizer footgun is real (design-space §4.3: unquoted `D-152` parses as boolean `D NOT 152`). Documenting this once is ~30 lines in read-contract or a new retrieval spec. Low.
- **Debugging surface**: `sqlite3 retrieval.db '.schema'` works from stock CLI. Query plans via `EXPLAIN QUERY PLAN`. Highly inspectable.
- **External-workspace propagation**: each new external workspace pays {Python 3.8+, sqlite3 FTS5, pyyaml, mcp[cli]}. macOS default Python typically has FTS5 enabled; a Linux VPS host might not. This is a real tax but a known-manageable one.

### 3.2 Substrate-2 — DuckDB + FTS

- **Dependency floor**: Python + `duckdb` wheel. DuckDB's FTS extension is loaded at runtime via `INSTALL fts; LOAD fts;`. Per §2a correction, stable not experimental — I retract the design-space §5.3 concern from my evaluation.
- **Rebuild time**: ~150ms comparable. Rebuild is **non-incremental** (design-space §5.3): full drop + rebuild of FTS index. Fine at 1.4M words; problematic at 10×.
- **Index size**: comparable ~15–20 MiB.
- **Code LOC**: marginally more than SQLite because DuckDB Python package surface is richer (arrays, STRUCT types). Full-kit estimate per design-space §5.1 adds `edges` + `DuckPGQ` optional; phase-1 equivalent is also ~300 LOC.
- **Docs burden**: DuckDB's syntax is richer but also less familiar to operators who know SQLite. Ecosystem for MCP integration is younger (design-space §5.3: "less mature ecosystem for MCP integration"). Medium-plus.
- **Debugging surface**: DuckDB CLI, good inspection. `EXPLAIN` works. DuckPGQ if adopted adds a graph-query syntax (`USING KEY`) that is a **new language to learn**.
- **External-workspace propagation**: every new external workspace pays {Python, `duckdb` wheel install at ~30MB, optional DuckPGQ extension, mcp[cli]}. The wheel is a pure install, no system dependency. But the **ecosystem tax** — Case Stewards and operators across external workspaces now need to know DuckDB + FTS extension + DuckPGQ + SQL/PGQ — is substantially higher than SQLite's well-known surface.

**My read on Substrate-1 vs Substrate-2**: design-space §5.4 notes the query-class argument for DuckDB ("structured-filter + graph-traversal queries dominant"). But §11 admits this dominance is *qualitative, not measured*. Adopting Substrate-2 to benefit from strengths on a query class whose dominance is unmeasured is adoption-by-anticipation. Under minimal-adoption, **Substrate-1 is correct because SQLite is already available in every environment that has Python** and adds zero novel ecosystem.

### 3.3 Substrate-3 — tantivy-py

Scale mismatch per design-space §6.2. At 457 files both substrates return microsecond results. Rust-backed throughput edge materialises at 10^6+ documents. **Reject in phase 1 and phase 2.** Reconsider only if F3 (§1.2) fires and external-workspace corpora cross 10^4 files (unlikely before 2028).

### 3.4 Substrate-4 — Whoosh-Reloaded

Per design-space §6.7, useful escape hatch when SQLite C extensions are constrained. **Reject as primary** in phase 1; keep on the menu as contingency only. Ecosystem momentum is low in 2026 (same §). No positive case for choosing it.

### 3.5 Substrate-N (P3-surfaced)

I have not seen P3's output at launch. Plausible candidates P3 might surface:

- **(N-a) Agent memory / Claude projects as retrieval**: rejected by CLAUDE.md local override (auto-memory disabled for this workspace). Not portable across external-application workspaces (disaster-response's external Claude Code runs with its own memory settings). **Scope-misfit for the brief.**
- **(N-b) Convention-over-tooling: ID-prefix conventions + better default-read chunking**: attractive; costs zero dependencies. But addresses only the ID-lookup query class and does not solve archive-surface prose retrieval. **Complementary, not substrate.**
- **(N-c) Query-log as substrate (instrument Case Steward reads, drive substrate shape from measured queries)**: this is essentially my §1.3 "defer-with-instrumentation." If P3 surfaces it, it is the strongest reframe from my stance. I concede it is better than my adoption recommendation *if* the operator's framing allows measurement-before-architecture.
- **(N-d) Structured artefacts replacing unstructured markdown** (e.g., move decisions from prose to YAML): would shrink the substrate need, but is a write-side restructure that invalidates 49 sessions of provenance-citation convention. **Reject**: the write-side discipline is stable and correct; the asymmetry is on the read side.

I pre-emptively grant P3 weight on N-b and N-c if surfaced. N-a and N-d I would push back on.

## 4. Bootstrap cost for external applications

Q6/Q7 of the brief names external-application portability as load-bearing. I need to evaluate the Selvedge pitch carefully here because it **is** a distinguishing feature.

### 4.1 The Selvedge pitch under the Q6 scope expansion

The methodology is domain-general. External workspaces (selvedge-disaster-response at S046/D-142; any future ones) produce dense application artefacts. Each workspace carries its own workspace-relative bootstrapped index. Dependency floor paid by every external workspace is brief §2b list: Python + `mcp[cli]` + `pyyaml` + {SQLite FTS5 or DuckDB}.

### 4.2 Concrete scenario: a new external-application workspace at Session 0

Operator bootstraps `selvedge-<new-domain>/` at 2027-Q1. The current `tools/bootstrap-external-workspace.sh` (S046 D-142 ancillary tooling) is extended to install the substrate. Steps the operator executes:

1. Run `bootstrap-external-workspace.sh <target-path>`: copies engine-definition files + `tools/build_retrieval_index.py` + `tools/retrieval_server.py` + `.mcp.json` template.
2. `pip install mcp[cli] pyyaml` (and optionally `duckdb` if Substrate-2).
3. First session-open: indexer runs on empty workspace (takes <100ms), produces empty `.cache/retrieval.db`.
4. MCP server registered at project scope; Claude Code picks it up.

**Total new-workspace tax**: 1 bootstrap-script call + 1 `pip install` + 1 first-index build. Under 2 minutes of human-operator time.

Is this OK tax? Three ways to evaluate:

- **OK as a feature**: every Selvedge external workspace gets a local retrieval substrate without per-workspace re-implementation. The engine's "methodology-for-domain-projects" pitch gains a concrete capability, not just a process.
- **Acceptable but not free**: the Python + MCP dependency floor now applies to *every* external workspace. An operator who wants to use Selvedge on, say, a paper-and-pen reasoning project must install Python. This is a real constraint on the methodology's reach. But given Claude Code itself is a CLI tool with a Python-adjacent ecosystem, operators already have Python-adjacent environments. Floor is low.
- **Not OK if…**: the substrate generates capacity drift. If Case Stewards in external workspaces start *relying* on the substrate in ways that bind future engine versions to its specific shape, the engine loses the optionality to revise retrieval architecture later. This is my biggest concern and is §5's phase-2 gate.

### 4.3 The load-bearing risk: bootstrap-time substrate drift

If the substrate ships as **engine-definition** (brief §4 Q7 candidate (a)), every external workspace inherits byte-identically. Revising the substrate requires a new engine version (engine-v9 → v10), propagating to every external workspace at next bootstrap. Over 5 years this means every external workspace's substrate eventually inherits every engine-side revision.

If the substrate ships as **engine-adjacent tooling** (brief §4 Q7 candidate (b)), external workspaces copy at bootstrap, and revisions propagate only at the next bootstrap of that workspace (i.e., never after initial bootstrap, unless operators re-run). This creates **version fragmentation** but preserves each workspace's stability.

**My Q7 recommendation: engine-adjacent (b), not engine-definition.** Rationale: the substrate is new in S050; it has not demonstrated stability across versions; binding it to engine-definition now locks the methodology into propagating substrate drift. Engine-adjacent keeps the door open. After 3+ stable substrate versions across 2+ external workspaces, reconsider promotion to engine-definition.

### 4.4 Scenario cost summary

For the projected 1–3 external workspaces over the next 12 months: the bootstrap tax is acceptable. For a hypothetical 20-external-workspace future (which the operator's framing does not currently claim), the tax compounds: 20 workspaces × 4 dependencies × N revisions = a propagation surface large enough to deserve a separate engineering cycle. **Neither scenario is falsified by phase-1 minimum**, because phase-1 minimum keeps the dependency surface small enough that a future revision (e.g., ejecting SQLite for something else) is a one-LOC change in `build_retrieval_index.py`.

## 5. Phased-adoption plan with go/no-go gates

### Phase 1 — ship at S050 close (this session executes phase 1 only)

**Deliverables (as §2.1)**:

- `tools/build_retrieval_index.py` (FTS5 only; no edges; no frontmatter_kv).
- `tools/retrieval_server.py` (two tools: `search`, `resolve_id`).
- `specifications/aliases.yaml` (two-label; seed with 5–10 entries manually).
- `.mcp.json` (project scope; committed).
- `.gitignore` add `.cache/retrieval.db`.
- `tools/bootstrap-external-workspace.sh` extended to install the above files + print `pip install` instructions.

**Deliberately NOT in phase 1**:

- No kernel §1 amendment.
- No validator check 24.
- No `edges` table, no `frontmatter_kv` table, no `warrants_currently_met` tool.
- No `traverse` tool, no `list_identifiers` tool.
- No SKOS three-label.
- No post-commit hook.
- No `syncs_with:` frontmatter field.
- No engine-manifest.md §3 inclusion (substrate is ancillary, not engine-definition).

**Measurable demonstrations at S050 close**:

- `time python tools/build_retrieval_index.py` ≤ 500ms.
- `mcp__selvedge_retrieval__search("preservation minority")` returns ≥1 result from `workspace-structure.md` §10.4.
- `mcp__selvedge_retrieval__resolve_id("M5")` returns `§10.4-M5`.
- Smoke test: indexer builds over `selvedge-disaster-response/` workspace (ahead of next bootstrap, optional).

### Phase 2 — gate at S053 (3 sessions after adoption)

**Phase 2 triggers iff AT LEAST ONE of the following fires in S050–S053:**

- **(P2-a)** Case Steward records in 2+ session closes that a `search` or `resolve_id` call materially changed a synthesis decision (surfaced a prior OI, preserved-minority, or decision that prose-scan would have missed).
- **(P2-b)** An honest-limit of form F1 (§1.2) appears in ≥1 session close *despite the phase-1 tools being available* — i.e., the tools are not enough for the reasoning.
- **(P2-c)** External-application workspace (disaster-response or new) adopts the substrate and reports ≥1 use of `search` that added value vs local grep.

**Phase 2 deliverables if gate passes:**

- Add `frontmatter_kv` table + `list_identifiers` tool. Rationale: frontmatter-filter queries measured as common.
- Add `edges` table + `traverse` tool **iff** (P2-a) or (P2-b) evidence specifically points to multi-hop traversal failures. Otherwise defer to phase 3.
- Amend kernel §1 Read with a *soft* Warrant-evaluation sub-activity: call `warrants_currently_met` if available, fall back to prose scan if not. Tool-optional, not tool-required.
- Add validator check 24: preserved-minority substrate-pointer coverage, **gated on substrate availability** (i.e., check 24 skips cleanly if index is missing rather than failing).

**Phase 2 does NOT trigger:**

- If fewer than 1 of (P2-a/b/c) fires → defer phase 2 to S056; re-evaluate.
- If ≥3 consecutive sessions report "I didn't use the tool" → substrate is not earning its keep; phase 2 deferred indefinitely; phase-1 remains in place or gets deprecated.

### Phase 3 — indefinite / open-ended

Reached only if phase 2 is successful and new pressures emerge. Candidate phase-3 additions:

- SKOS three-label alias vocabulary (if two-label proves insufficient).
- `syncs_with:` frontmatter field (if spec-layer declaration-of-intent proves distinct from extracted-references).
- Engine-manifest.md §3 promotion (substrate from ancillary to engine-definition).
- Post-commit hook for auto-rebuild.
- DuckPGQ or recursive-CTE graph traversal if phase-2 `edges` table is insufficient.

No gates pre-specified; phase 3 requires a dedicated MAD at that session.

### Go/no-go gate summary

```
Phase 1 → Phase 2: ≥1 of (P2-a, P2-b, P2-c) fires within 3 sessions
Phase 2 → Phase 3: ≥2 of (expanded triggers TBD at phase 2 launch)
Phase 1 → Phase 1 (maintain): fewer than 1 trigger fires; substrate proves unused; deprecation candidate
```

This is what "incremental adoption" looks like concrete. Not rhetoric.

## 6. Answers to Q1–Q8

**Q1 — Primary substrate choice.** Substrate-1 (SQLite FTS5). Rationale: zero install beyond Python + FastMCP; FTS5 native in macOS default Python; operator's dismissed-as-weightless preference aside, the technical case (design-space §4.2: stdlib, inspectable, ecosystem maturity) still holds on its own merits; DuckDB's structural advantages (design-space §5.2) are anticipation-based without measured query-class data. If P1/P3 surfaces a compelling alternative, I open-mindedly reconsider — but **within phase-1 minimum**, not full-kit. Defer-and-stay-lexical-tools-only is respectable (§1) but the operator framing closes it.

**Q2 — Adoption scope.** **Minimal (FTS + search + resolve_id only) for phase 1**, with phased gates to expand (§5). Full-kit is premature commitment. Incremental three-phase as design-space §8.2 Q2 names is directionally right but stages too much in phase 1; my §5 phase-1 is narrower.

**Q3 — Kernel §1 amendment shape.** **Defer amendment to phase 2.** A kernel amendment that binds to a tool creates a semantic coupling between kernel correctness and tool availability — exactly the failure mode design-space §3.6 correctly raises. Phase-1 treats MCP tools as advisory supplements; kernel §1 Read remains as current. When phase 2 adds `warrants_currently_met`, the amendment should be *soft*: "call the tool if available, fall back to prose scan if not." Not tool-required.

**Q4 — Alias vocabulary.** **Two-label (canonical + aliases) for phase 1.** SKOS three-label (prefLabel/altLabel/hiddenLabel) is premature for a vocabulary that has not been exercised. Two-label is refactorable to SKOS later without breaking callers. Defer SKOS to phase 3 if it is ever needed.

**Q5 — Rebuild trigger.** **Session-open mtime check only** (lazy). No git post-commit hook in phase 1. Hooks create implicit state: a developer who clones the repo gets no hook until they run `git config core.hooksPath` or equivalent. External-workspace hosts may not run hooks at all. Session-open lazy rebuild is the self-contained answer. Adopt post-commit hook in phase 3 if rebuild latency becomes a pain.

**Q6 — Cross-spec `syncs_with:` frontmatter field.** **Defer.** Under phase-1 minimum there is no `edges` table to make the field redundant-vs-load-bearing question concrete. Phase 2 re-evaluates once `edges` exists. The EF-047 original level-B rationale is directionally sound but under-evidenced; waiting until `edges` is in hand lets the deliberation be grounded.

**Q7 — External-application inheritance shape (LOAD-BEARING).** **Engine-adjacent tooling (brief §4 candidate (b)), not engine-definition (a).** Rationale §4.3: the substrate is new; it has not demonstrated stability across versions; binding it to engine-definition now propagates substrate drift to every external workspace forever. Engine-adjacent preserves optionality. After 3+ stable versions and 2+ external-workspace adoptions, **reconsider** promotion to engine-definition in a dedicated session (not this one). Integrate with `tools/bootstrap-external-workspace.sh` as S046 D-142 precedent established.

**Q8 — Validator check 24 scope.** **Defer to phase 2.** Phase-1 minimum does not create the `identifiers` table that check 24 would verify against. Adding check 24 before the identifiers-table exists is vacuous (validator would pass by default). Phase 2 adds check 24 **gated**: skip if `.cache/retrieval.db` is missing; fail only if it is present *and* missing preserved-minority pointers. Scope: preserved-minority pointer verification only — do NOT extend to every `[archive: path]` citation (overreach) or every ID reference (extreme overreach). Run in external-workspaces only on substrate-adopted ones.

## 7. Counter-frames: the strongest argument against my skeptic position

**P1's likely strongest rebuttal**: "The incremental path's real cost is not the LOC or dependencies — it is the **session budget**. Adopting phase-1 at S050 and then coming back to phase-2 in S053 and phase-3 in S056 is three sessions of structural work spread over ~6 weeks. If the full-kit is achievable in one session, why not pay the cost once and get to stable operation faster? Incremental adoption pays back only if the phase-1→2→3 transitions are meaningful — and you've just said phase 2 is gated on evidence that may not materialise, which means phase 1 may be a permanent architecture. At which point minimalism isn't incremental, it's just undershot."

This is fair and I concede it partially. My response:

- **Concede**: if phase 1 is permanent, it *is* undershot relative to the full-kit ambition. The risk is real.
- **Rebut**: but the full-kit has the symmetric failure mode that is worse — if phase-1 features (FTS + resolve_id) are what the workspace actually uses, full-kit's `edges` + `warrants_currently_met` + SKOS + post-commit hook become *code we maintain for ceremony*. Maintenance cost of unused substrate over 5 years is not small. I would rather under-ship and grow than over-ship and prune.
- **Concede further**: P1's "pay cost once" argument dominates if the session-budget is the scarce resource and the code is well-understood. But the code *isn't* well-understood yet — 300 LOC of indexer vs 500 LOC of indexer is the same learning investment if we don't yet know which queries actually matter. **Deferring the parts we haven't designed for evidence is a better investment.**
- **Shared ground**: P1 and I agree substrate adoption is happening. We disagree on whether "all at once" or "earn it" is the right cadence. That disagreement should be preserved as minority even if P1+P3+P4 converge on full-kit (per §6 of brief: "Preserve all provenance: minority positions that do not converge will be recorded").

**P4's laundering audit might raise**: "P2's 'defer with instrumentation' (§1.3) reads as scepticism hedging. Either commit to adoption with criteria, or commit to defer. The hybrid is the kind of mid-path that lets incrementalism avoid both falsification conditions."

Concede: fair. My primary position is **phase-1 minimum adoption**. §1.3 is a fallback if operator framing opens it, explicitly tagged.

## 8. Measurable adoption criteria

What would have to be true to vindicate (or falsify) the incremental path?

### Vindication criteria (incremental wins)

- **(V1)** At S053 close, ≥1 of (P2-a, P2-b, P2-c) has fired → phase 2 trigger met, substrate is earning its keep, phased adoption working.
- **(V2)** At S053 close, no "substrate unavailable" failure has been reported — indexer runs cleanly, MCP server registers, `search` + `resolve_id` work. The substrate infrastructure is operationally stable.
- **(V3)** Between S050–S053, the ≤500ms rebuild cost and ≤20 MiB index size hold (design-space §3.5 measured targets).
- **(V4)** External-workspace (disaster-response) adopts the substrate at next bootstrap-refresh; reports ≥1 useful query in a domain context.

### Falsification criteria (incremental wrong, full-kit would have been better)

- **(F-incr-1)** 3+ sessions record "I tried `search` but had to fall back to `rg` and manual read because phase-1 scope didn't cover the query." Pattern: `frontmatter_kv` / `edges` / `traverse` is missing when wanted. Full-kit would have had them.
- **(F-incr-2)** Phase 2 gate fails to fire for 5+ sessions → substrate underutilised → either phase 1 shouldn't have shipped or it's actively being avoided. Either answer is informative.
- **(F-incr-3)** Maintenance cost of phase-1 tools across 5 sessions exceeds the cost estimate — if the indexer needs repeated fixes, the "minimal" claim was false.

### What is NOT a vindication/falsification signal

- Frequency of `search` calls per session. Low call frequency is consistent with "the tool works and is used when needed"; high call frequency is consistent with "workspace has more retrieval needs than expected." Neither refutes incremental.
- Index size growth rate. Not a correctness signal; a workspace-growth signal.
- Whether other Selvedge workspaces adopt the substrate. External adoption is evidence about portability design, not about whether the substrate itself is right for self-dev.

### Session-specific commitment

At S050 close: phase-1 deliverables shipped; 4 smoke tests pass (§5 phase-1 measurable demonstrations); phase-2 gate explicitly documented in a new lightweight close-file field (`retrieval-gate-status: 0-of-3-triggers-fired`) updated each session through S053.

This is concrete-measurable, not aspirational. P4's laundering-audit standard should find it meets the bar.

---

## 9. Close

My stance is compressed: **adopt the smallest substrate that delivers a measurable capability (SQLite FTS5 + two MCP tools + two-label aliases), treat it as engine-adjacent tooling rather than engine-definition, defer kernel amendments and validator extensions until substrate value is demonstrated, and gate further phases on measured evidence.**

If P1 argues for full-kit, I expect my phase-1 minimum to be preserved as first-class minority unless P1 produces a measured query-class distribution proving the missing pieces (edges, frontmatter_kv, warrants_currently_met) are load-bearing from day one. Design-space §11 honestly acknowledges this data does not exist. Without it, adoption by anticipation creates maintenance cost; adoption by evidence — which is what phase gates implement — is the engineering-rigour answer to the operator's "real scalable technical solutions" directive.

The operator directive rules out pure-discipline minimalism. It does not rule out **minimum viable substrate with demonstrated path to more**. That is what I am proposing.
