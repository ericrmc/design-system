---
session: 050
title: Decisions — retrieval substrate adoption MAD outcomes (Q1-Q8 resolutions per 01-deliberation.md synthesis) + new engine-definition spec retrieval-contract.md + engine-v8→v9 substantive bump + 5 new preserved first-class minorities + bundled-minor adoptions + D-133 M2 third-of-3 vindication disposition + housekeeping
date: 2026-04-24
status: complete
---

# Decisions — Session 050

Fourteen decisions. D-163 operator ratification + Q6 scope expansion. D-164–D-171 Q1–Q8 resolutions per synthesis in `01-deliberation.md`. D-172 new engine-definition spec + engine-v8→v9. D-173 phase-2 gate + 5 preserved minorities. D-174 bundled-minor adoptions. D-175 D-133 M2 third-of-3 vindication. D-176 housekeeping.

---

## D-163: Halt-1 Q1–Q5 ratifications adopted; Q6 external-application-portability scope expansion ratified

**Decision**: Operator Halt-1 response received at S050 open. Q1 (i) proceed with MAD; Q2 (a) canonicalise corrections in 00-assessment + edit triage + fresh shared-brief; Q3 (ii) rename options neutrally Substrate-1/2/3/4/N; Q4 (ii) P1 is neutral surveyor; Q5 (a) SESSION-LOG thin-row at close. Q6 additional operator agenda: substrate must include any externally-run engine applications (S046/S047 precedent) via workspace-relative bootstrapped database. Q6 is ratified as **scope expansion** — external-application inheritance (Q7 in the MAD agenda) is load-bearing, not deferrable.

**Operator Q6 verbatim** (preserved canonical):

> "include in consideration any externally run engine applications such as described in S046 and S047. These contain dense application artefacts and provenance that should also be able to benefit from the underlying mechanics, e.g. a bootstrapped database stored relative to that workspace."

**Triggers met:** [d016_3, d023_1]

**Triggers rationale:** `d016_3` fires because Q6's scope expansion creates multi-session coordination consequences (every substrate-design decision must now consider external-application portability). `d023_1` fires because the Q6 surfacing is operator-substantive direction at Halt-1.

**Rejected alternatives**: (a) defer Q6 to a later session — rejected because operator's scope expansion is framed for this MAD; (b) treat Q6 as advisory — rejected because the wording "should also be able to benefit" declares a design requirement.

**Non-Claude participation**: N/A at Halt-1 level; the ratifications flow into the MAD shared-brief §0 which all four perspectives read.

**Single-agent reason**: operator-directed ratification + scope expansion.

---

## D-164: Q1 primary substrate choice: Substrate-1 (SQLite FTS5)

**Decision**: Adopt SQLite FTS5 as the retrieval substrate for phase-1. All four perspectives converged. Rationales span P1's three tie-breakers (dependency floor for external-workspace portability; ecosystem maturity over 2–5 year horizon; snippet/highlight FTS5-native), P2's install-zero-beyond-Python pragma, P3's distribution-risk-minimisation under a Substrate-N3 framing, and P4's provisional-phase-1-only audit-positive.

**Triggers met:** [d016_1, d023_1, d016_2]

**Triggers rationale:** `d016_1` fires because substrate adoption is substantive per OI-002 heuristic (new load-bearing capability crossing engine-definition/engine-adjacent boundaries). `d023_1` fires because kernel-adjacent decisions require MAD per `multi-agent-deliberation.md` v4 §When Multi-Agent Deliberation Is Required. `d016_2` fires because the decision has downstream phase-2 kernel-amendment implications.

**Rejected alternatives with rationale**:
- Substrate-2 DuckDB+FTS: viable after §2a correction (stable not experimental) but adds +1 wheel (`duckdb` ~50MB) to every external-workspace bootstrap; ecosystem maturity 2 years vs 9 years; less mature MCP reference ecosystem. Preserved as first-class minority §10.4-M8 for structured-first substrate pivot if query class dominates (see D-173).
- Substrate-3 tantivy-py: scale mismatch (edge at 10^6+ files); Rust-wheel portability risk for external workspaces; API-breaking history on Python binding.
- Substrate-4 Whoosh-Reloaded: low ecosystem momentum in 2026; useful only as escape hatch if SQLite C extensions become constrained.
- Substrate-5 bm25s + SQLite (P1-surfaced): no functional win over Substrate-1; higher dependency floor (NumPy+SciPy); young project.
- Substrate-N1 Retrieval Ledger (P3-surfaced): not standalone; complementary instrumentation potentially adopted in phase-2.
- Substrate-N2 Structured Artefacts Replace Prose-As-Database (P3-surfaced): too disruptive for S050; correct reframe. Preserved as first-class minority §10.4-M10 (see D-173).
- Defer-and-stay-lexical-tools-only (P2's first-class defer case): closed by operator framing ("real scalable technical solutions") but preserved as first-class minority §10.4-M7 conditioned on phase-2-gate-failing-to-fire (see D-173).

**Non-Claude participation**: P3 (Outsider, Codex/GPT-5.5) surfaced Substrate-N1/N2/N3; P4 (Cross-Family Reviewer, Codex/GPT-5.5) recorded provisional-not-final status and flagged DuckDB minority preservation. Both non-Claude perspectives load-bearing to the decision shape.

---

## D-165: Q2 adoption scope: phase-1 minimum (2 tables + FTS + 2 MCP tools)

**Decision**: Phase-1 ships:
- Tables: `documents`, `identifiers`.
- Virtual: `docs_fts` FTS5 over `documents.body + title`.
- MCP tools: `search(query, k=10)`, `resolve_id(alias)`.
- Alias file: `specifications/aliases.yaml` with `schema_version: 1` (two-label).
- `.mcp.json` template and workspace-local `.cache/retrieval.db`.
- Indexer: `tools/build_retrieval_index.py` (~200 LOC).
- Server: `tools/retrieval_server.py` (~120 LOC).

Phase-1 does NOT ship: `edges` table, `frontmatter_kv` table, `aliases` DB table (YAML only), `traverse`/`warrants_currently_met`/`list_identifiers`/`verify_archive_path` MCP tools, post-commit hook, SKOS three-label, `syncs_with:` field, validator check 24, kernel §1 amendment.

**Triggers met:** [d016_1, d023_1, d016_3]

**Triggers rationale:** `d016_1` fires because adoption scope is substantive (new tables, new MCP tools, new phase-1 shipped artefacts). `d023_1` fires because MAD v4 requires deliberation on substantive engine-adjacent tooling bundle. `d016_3` fires because phase-2 gate creates multi-session coordination obligation through S053.

**Rejected alternatives**:
- P1's larger phase-1 (3 tools including `list_identifiers`, fuller file-plan edits): rejected per P4 audit as internal-inconsistency (full-kit surface preserved under phased-labelling); `list_identifiers` deferred to phase-2.
- P2's pure-FTS phase-1 without `identifiers` table: rejected per P4 audit as technical under-specification (resolve_id cannot work without it); `identifiers` table included in phase-1.
- P3's phase-1 (add `archive_paths` + minimal `edges` + `verify_archive_path`): rejected as premature; `edges` deferred to phase-2 pending measured-usage evidence.
- Full-kit phase-1 (all five design-space tables): rejected per P4 audit — unmeasured query-class data does not justify full maintenance surface at adoption.
- Defer adoption entirely: rejected per operator framing (closed by §2a + S049 D-157).

**Non-Claude participation**: P3 Substrate-N3 framing shapes the phase-1 minimum (source-of-truth-as-markdown-with-derived-read-model); P4 audit directly resolves P1 and P2's respective inconsistencies.

---

## D-166: Q3 kernel §1 amendment: no amendment in phase-1; soft amendment gated on phase-2

**Decision**: `methodology-kernel.md` v6 is NOT amended at S050. Phase-2 deliberation (if triggered per D-173) may add a soft §1a Warrant-evaluation sub-activity: "call `warrants_currently_met()` if available; fall back to prose-scan warrant evaluation and record the fallback in honest-limits". Not tool-required in phase-1 (the tool does not exist yet) and not tool-required in phase-2 either (soft amendment only).

**Triggers met:** [d016_2]

**Triggers rationale:** `d016_2` fires because the decision is a deliberate deferral of a methodology-kernel amendment (preserving the phase-2 amendment candidate). No `d016_1` substantive change is executed this session (kernel unamended). No `d023_*` fires (no spec edit).

**Rejected alternatives**:
- P1's hard amendment with degradation clause at S050: rejected — couples methodology correctness to tool operational state before operational evidence exists.
- P3's required-retrieval-checks-with-visible-degraded-mode at S050: adopted-in-spirit (via the new retrieval-contract.md per D-172 §Required behaviour) but not via kernel amendment at phase-1.
- P2+P4's defer-to-phase-2-with-soft-amendment: adopted.
- Hard amendment in phase-2: rejected per P4 laundering-audit anti-coupling rationale.

**Non-Claude participation**: P3's "required retrieval checks as contract, not tool call" reframing shapes the decision; P4 audit resolves P1's full-kit-surface-vs-phased-answer inconsistency on this Q.

---

## D-167: Q4 alias vocabulary: two-label with versioned schema

**Decision**: `specifications/aliases.yaml` adopts two-label schema with `schema_version: 1` frontmatter. Each entry: `canonical: <str>`, `kind: <str>`, `aliases: [<str>]`, optional `added_session: <int>`, `last_seen_session: <int>`. SKOS three-label (prefLabel/altLabel/hiddenLabel) deferred to phase-3+ pending measured alias behaviour.

**Triggers met:** [d016_2]

**Triggers rationale:** `d016_2` fires because a new specification file (`specifications/aliases.yaml`) is introduced with a versioned schema and defined semantics. Minor per OI-002 heuristic (scaffold with seed entries; normative rules live in `retrieval-contract.md` §2.3).

**Rejected alternatives**:
- P1's SKOS three-label at adoption: rejected — premature optimisation for vocabulary not yet exercised; `hiddenLabel` useful only after historical/misspelled variants accumulate.
- Single-label canonical-only (no aliases): rejected as insufficient; alias resolution is the phase-1 core use case.
- Defer alias vocabulary entirely to phase-2: rejected; `resolve_id` tool requires the alias file at phase-1.

**Non-Claude participation**: P3's two-level schema shape + P4's version-tagging-for-migration recommendation adopted.

---

## D-168: Q5 rebuild trigger: session-open mtime check only

**Decision**: Indexer rebuilds when `max(*.md mtime) > retrieval.db mtime` at MCP server startup. No git post-commit hook in phase-1. Stale/fresh status reported in tool responses where relevant.

**Triggers met:** [d016_2]

**Triggers rationale:** `d016_2` fires because the decision constrains an engine-adjacent tool's behaviour at a specific design locus (rebuild trigger mechanism). No spec edit directly; obligation lives in `retrieval-contract.md` §4.

**Rejected alternatives**:
- P1's both triggers (mtime + post-commit hook): rejected — hooks create invisible state, poor portability across fresh clones and external workspaces per P4 audit.
- Post-commit hook only: rejected — fresh clones without hooks have stale index until manually rebuilt.
- On-demand rebuild only (explicit tool call): rejected — requires operator-intervention discipline; fails silently otherwise.
- External tool watching filesystem (fswatch/inotify): rejected — introduces daemon dependency contrary to workspace-local minimalism.

**Non-Claude participation**: P4's hooks-as-invisible-state reasoning decisive; P3's report-stale/fresh-status requirement adopted.

---

## D-169: Q6 `syncs_with:` frontmatter field: defer; preserve declaration-of-intent distinction as first-class minority

**Decision**: No `syncs_with:` field adopted in phase-1. The conceptual distinction P3+P4 named — `edges` answer "what is cited"; `syncs_with:` answers "what must co-evolve" — is preserved as first-class minority §10.4-M11 per D-173. Phase-2 deliberation (if triggered) re-examines with the distinction explicitly preserved; no auto-fold-into-edges.

**Triggers met:** [d016_2]

**Triggers rationale:** `d016_2` fires because the decision is a deferral of a proposed spec-frontmatter field (`syncs_with:`). Preserved as first-class minority §10.4-M11; phase-2 deliberation re-examines. No substantive spec change this session.

**Rejected alternatives**:
- P1's fold-into-edges-at-phase-2: rejected per P3+P4 distinction-preservation; folding would lose the "declared co-evolution" semantic.
- Adopt `syncs_with:` at phase-1: rejected — no substrate to enforce the declaration; spec-field without enforcement is ceremony.
- Drop the `syncs_with:` concept entirely: rejected — the EF-047 original level-B rationale retains force even under substrate framing.

**Non-Claude participation**: P3+P4 named the distinction; both Claude perspectives treated `syncs_with:` as redundant-with-edges — non-Claude reframe load-bearing to the decision.

---

## D-170: Q7 external-application inheritance: engine-defined contract + engine-adjacent implementation (P3 middle path)

**Decision**: Adopt P3's middle path.
- **Engine-defined contract** (NEW engine-definition spec; see D-172): `specifications/retrieval-contract.md` declares required tool names (`search`, `resolve_id`), signatures, failure behavior (degraded mode with visible record), registry schemas, `.mcp.json` shape, and bootstrap contract.
- **Engine-adjacent implementation** (NOT added to `engine-manifest.md` §3 engine-definition file list): `tools/build_retrieval_index.py`, `tools/retrieval_server.py`, `.mcp.json` template, `specifications/aliases.yaml` scaffold.
- **Bootstrap integration**: `tools/bootstrap-external-workspace.sh` extended to copy implementation files + print `pip install mcp[cli] pyyaml` instructions + build initial index + update the workspace's `.mcp.json`.
- **Workspace-local state**: `.cache/retrieval.db` gitignored in every workspace; never shared across workspaces.
- **Promotion path**: engine-adjacent → engine-definition re-evaluable after ≥3 stable substrate versions + ≥1 successful external-workspace adoption + measured query-class data.

**Triggers met:** [d016_1, d023_1]

**Triggers rationale:** `d016_1` fires because the portability decision introduces a new engine-definition specification (`specifications/retrieval-contract.md` per D-172) and defines external-application inheritance mechanism. `d023_1` fires because engine-definition scope decisions require MAD per `multi-agent-deliberation.md` v4 §When Multi-Agent Deliberation Is Required.

**Rejected alternatives**:
- P1's engine-definition at adoption: rejected — binds methodology to propagate substrate implementation churn across every external workspace before substrate stability is demonstrated. Preserved as first-class minority §10.4-M9 per D-173 with specific activation warrant (inconsistent-inheritance signal).
- P2's pure engine-adjacent (no engine-defined contract): rejected — fails to give external workspaces the capability the operator explicitly expanded scope to require; an external workspace without a contract cannot verify compliance.
- Ancillary-local (implementation stays in self-dev only): rejected by operator Halt-1 Q6 scope expansion.
- Package-distributed substrate (pip installable `selvedge-retrieval` package): rejected at phase-1 as premature; can be reconsidered at promotion point if distribution becomes the pain.

**Non-Claude participation**: P3's middle path + P4's promotion-requires-stability-evidence both load-bearing.

---

## D-171: Q8 validator check 24: defer to phase-2 (gated on substrate availability + identifiers table existence)

**Decision**: `tools/validate.sh` does NOT add check 24 at S050. Phase-2 deliberation (if triggered) adds check 24 with narrow scope:
- For each `§10.x` / `§5.x` preserved-minority block in active specs: verify `identifiers` table has a row for the minority's canonical ID with `source_path` pointing to an active specification.
- Verify the minority's source-archive-path (from `§10.x "Source:"` field) resolves to an existing file.
- **Skip-if-substrate-absent**: the check is a no-op if `.cache/retrieval.db` is missing; does not fail the validator.
- **Hard-fail only once declared required**: phase-2 ships it skip-mode; phase-3 promotes to hard-fail.
- External workspaces: distinguish inherited-engine-minorities from application-local-minorities (schema on registries when phase-2 edges are added).

**Triggers met:** [d016_2]

**Triggers rationale:** `d016_2` fires because the decision defers a validator check addition. Preservation of the phase-2-gated addition per `retrieval-contract.md` §6. No `tools/validate.sh` edit this session.

**Rejected alternatives**:
- P1's phase-3 deferral: rejected as over-deferred; phase-2 gated-and-skip-absent is the right shape.
- Broader scope extending to every `[archive: path]` or every prose ID: rejected per P3+P4 — false-positive noise from historical prose, examples, partial references.
- Adopt at phase-1 with vacuous-on-missing-substrate mode: rejected — ceremony without function.

**Non-Claude participation**: P3's report-only-unresolved-ID-inventory-first staging + P4's skip-if-absent semantics adopted.

---

## D-172: New engine-definition spec `specifications/retrieval-contract.md` v1; engine-v8→v9 substantive bump

**Decision**: Create new engine-definition spec `specifications/retrieval-contract.md` v1. Add to `engine-manifest.md` §3 engine-definition file list. Bump `engine-manifest.md` §2 from engine-v8 to engine-v9. Add engine-v9 history entry in `engine-manifest.md` §7.

**retrieval-contract.md v1 §§ outline**:
- §1 Purpose and scope: the contract defines required retrieval capabilities that every Selvedge workspace (self-dev and external-application) must satisfy. Implementation shape is open; the contract constrains behaviour, not code.
- §2 Required tool names and signatures: `search(query, k=10)`; `resolve_id(alias)`.
- §3 Required failure behavior: tools must report availability, index freshness (mtime), and degraded-mode. Silent fallback is a contract violation.
- §4 Workspace-local state: the retrieval index lives at `.cache/retrieval.db` (or equivalent engine-adjacent-designated path) and is gitignored. Never shared across workspaces.
- §5 Bootstrap contract: `tools/bootstrap-external-workspace.sh` installs conforming implementation files + `.mcp.json` template + performs initial index build + validates `search`/`resolve_id` work locally.
- §6 Phase-2 gate and future extensions: contract v1 declares phase-1 surface; phase-2 extensions (edges/frontmatter/traverse/warrants) are version-2-of-this-contract.
- §7 Preserved minorities (or cross-ref to workspace-structure.md §10.4-M7 through M11).
- §8 Honest limits.

**`engine-manifest.md` v8→v9 changes**:
- Frontmatter `version: engine-v9`; `supersedes-engine-version: engine-v8`; `last-updated-session: 050`.
- §2 current version: engine-v9.
- §3 engine-definition file list: add `specifications/retrieval-contract.md`.
- §7 new engine-v9 entry: "Engine-v9 (Session 050). Added `specifications/retrieval-contract.md` declaring the required retrieval capabilities for Selvedge workspaces. Implementation is engine-adjacent per D-170. Phase-1 capability surface: `search` + `resolve_id` + workspace-local SQLite FTS5 index. Preservation window for engine-v8 closed at depth 2 (S049 + S050's pre-adoption state). First-ever engine-v bump driven by a substantive MAD adopting a new engine-definition spec (distinct from documentary-per-§5-sub-pattern precedent of S021/S023/S028/S033/S036/S048)."

**Triggers met:** [d016_1, d023_1, d016_3]

**Triggers rationale:** `d016_1` fires because a new engine-definition spec (`specifications/retrieval-contract.md` v1) is adopted — substantive per OI-002 heuristic (new load-bearing capability declaration). `d023_1` fires because the MAD produced this adoption. `d016_3` fires because the phase-2 gate establishes multi-session coordination through S053.

**Rejected alternatives**:
- Documentary bump only (no new spec; amend existing specs): rejected — the capability is novel; it earns its own spec rather than bloating any existing one.
- engine-v9 skip (stay at v8 with retrieval-contract.md as new file): rejected — the new spec is substantive per OI-002; engine-v is the right mechanism.
- Integrate retrieval contract into `workspace-structure.md` §retrieval: rejected — workspace-structure.md is at 5,340 words (under soft-warning) but substrate-contract material is conceptually distinct from workspace-directory-structure.

**Non-Claude participation**: P3's "engine-defined interface" framing is the conceptual backbone of the new spec.

---

## D-173: Phase-2 gate (WX-50-1 retrieval-substrate-use recording) + 5 new preserved first-class minorities (§10.4-M7 through §10.4-M11)

**Decision (a) — Phase-2 gate**: New watchpoint **WX-50-1 retrieval-substrate-use recording**. Every session close through S053 records retrieval use in a 3-field section:
- `tool_calls_by_type`: counts of `search` and `resolve_id` invocations in the session.
- `results_used_with_artefact_id`: list of `{tool, query, returned_artefact_path, used_in_decision_or_oi_or_minority_id}`.
- `fallbacks_due_to_missing_capability`: list of `{query_intent, why_phase_1_did_not_suffice}`.

**Phase-2 triggers** (any of):
- ≥2 sessions in S050–S053 record ≥1 entry in `results_used_with_artefact_id`.
- ≥1 session in S050–S053 records ≥1 entry in `fallbacks_due_to_missing_capability` where the missing capability is structured-filter (frontmatter_kv) or graph-traversal (edges/traverse).
- ≥1 external-workspace adoption records ≥1 useful domain-context query.

**If phase-2 does not fire**: pause expansion; §10.4-M7 activation warrant evaluates for phase-1-was-wrong determination.

**Decision (b) — 5 new preserved first-class minorities**: add to `specifications/workspace-structure.md` v5 §10.4-M7 through §10.4-M11 (or equivalent §Minorities block in `retrieval-contract.md` v1).

1. **§10.4-M7 P2 minimum-adoption / defer-with-instrumentation**. Source: `provenance/050-session/01b-perspective-incrementalist-skeptic.md` §1.3. Activation warrant: if phase-2 gate fails to fire across S050–S053 AND zero use recorded for phase-1 tools in ≥3 consecutive sessions, revisit whether phase-1 should have shipped at all. Reopen warrants: (a) phase-2 non-firing AND zero-use across 3+ consecutive sessions — revisit phase-1 adoption; (b) phase-1 tool use becomes operationally burdensome relative to evidence of value.
2. **§10.4-M8 DuckDB structured-first substrate**. Source: `provenance/050-session/01a-perspective-substrate-architect.md` §1.2 + §2 counter-frames + `01d-perspective-cross-family-reviewer.md` §7 dissent-rec 2. Activation warrant: any session in which phase-1 tool use shows structured-filter + graph-traversal queries dominate prose-search queries by ≥3× count over a 5-session window. Reopen: (a) query-class data demonstrates structured-first dominance; (b) SQLite FTS5 ecosystem churn that DuckDB-FTS does not share.
3. **§10.4-M9 P1 engine-definition-at-adoption**. Source: `01a-perspective-substrate-architect.md` §4.1 + `01d-perspective-cross-family-reviewer.md` §7 dissent-rec 3. Activation warrant: if external-workspace adoption exposes inconsistent inheritance (workspace A and workspace B have divergent substrate implementations producing different answers on equivalent queries), re-enter engine-definition case. Reopen: (a) inconsistent-inheritance signal; (b) ≥3 stable substrate versions + ≥1 successful external-adoption — promotion to engine-definition becomes considered.
4. **§10.4-M10 P3 Substrate-N2 structured-artefacts-as-source-of-truth**. Source: `01c-perspective-outsider-frame-completion.md` §2 Substrate-N2. Activation warrant: if substrate phase-2+ maintenance cost exceeds projections by ≥2× OR multi-hop cross-reference queries become the dominant operational burden, revisit Substrate-N2 as multi-session arc.
5. **§10.4-M11 P3+P4 `syncs_with:` declaration-of-intent distinction**. Source: `01c-perspective-outsider-frame-completion.md` Q6 + `01d-perspective-cross-family-reviewer.md` §7 dissent-rec 5. Activation warrant: at phase-2 deliberation on edges table, the fold-vs-preserve question is explicitly deliberated; `syncs_with:` is not auto-folded.

**Count impact**: 31 preserved first-class minorities → **36** at S050 close.

**Triggers met:** [d016_3, d023_1]

**Triggers rationale:** `d016_3` fires because WX-50-1 establishes multi-session coordination across S050–S053 (retrieval-substrate-use recording in every session close). `d023_1` fires because the 5 first-class minorities are MAD-preserved dissent per `multi-agent-deliberation.md` v4 §Preserve Dissent.

**Rejected alternatives**:
- Preserve fewer minorities (e.g., only 1 or 2): rejected — each of the five carries a distinct activation warrant with distinct firing condition; consolidation would lose specificity.
- Preserve more minorities (e.g., include P3's Substrate-N1 Retrieval Ledger): rejected — Substrate-N1 is a phase-2 candidate mechanism, not a position-against-phase-1-adoption.
- WX-50-1 gate uses raw tool-call frequency as signal: rejected per P4 — "invocation count measures use, not value"; the 3-field structure separates use from value.

**Non-Claude participation**: P3 surfaced M10 + contributed to M11; P4 consolidated the 5-item list.

---

## D-174: Bundled-minor EF-047 dispositions: EF-047-brief-slot-template adoption-practice-only; EF-047-session-inputs adopted-as-practice at S050

**Decision**:
- **EF-047-brief-slot-template-hidden-arc-leakage**: record `status: triaged` maintained; spec-level adoption deferred to next self-dev or external-arc session that exercises arc-plan brief slots (earliest: selvedge-disaster-response S002+ arc resumption). The S050 substrate adoption does not surface arc-plan-hidden-view leakage pressure; deferral is principled, not punting.
- **EF-047-session-input-files-redundant-with-verbatim-capture**: **adopted-as-practice at S050**. Observed: session-inputs pattern was reused implicitly at S050 (shared brief cites S049 design-space as the "prior synthesis" input without re-verbatim-capture). Spec-level minor documentary bundled with retrieval-contract.md v1 §Bootstrap contract note: session-inputs-as-prior-synthesis-reference is acceptable shape; verbatim capture is not re-required when the cited artefact is in-workspace provenance. No separate spec-amendment file this session.

**Triggers met:** [d016_2, d016_3]

**Triggers rationale:** `d016_2` fires for the minor documentary adoption of the session-inputs-as-prior-synthesis pattern (noted in `retrieval-contract.md` §5 bootstrap contract rather than as separate spec edit). `d016_3` fires because the brief-slot-template deferral continues cross-session coordination (next arc-resumption session).

**Rejected alternatives**:
- Adopt both EF-047 minors at S050: rejected for brief-slot-template — no operational pressure surfaced this session.
- Defer both: rejected for session-inputs — it is already practice and minor documentary captures it.
- Open an OI for brief-slot-template: rejected — disposition is cleanly-deferred, not unresolved.

**Non-Claude participation**: N/A (bundled-minor triage; Case Steward disposition under S049 D-161 authority).

---

## D-175: D-133 M2 third-of-3 verification window: vindicated

**Decision**: M2 (Convene-time 7-column matrix + Outsider-non-Claude lineage-constraint + synonym-drift guard + departure-discipline) vindicated at the third-of-3 verification-window threshold. Verification-window: S045 + S047 + S050 (per S048 D-154 interpretation adopted at S049 D-162(2) + D-159(6): "MAD-sessions-with-non-Claude" counting).

**Each verification-window datum**:
- **S045**: 5-perspective cross-family MAD on OI-016 domain-validation; Outsider seat non-Claude (Codex/GPT-5.5); matrix populated; synonym-drift guard distinct P3/P4; no mid-session departure.
- **S047**: 4-perspective two-family MAD on external-application arc-plan; Outsider seat non-Claude; matrix populated; synonym-drift guard distinct; no departure.
- **S050 (this session)**: 4-perspective two-family MAD on retrieval substrate; Outsider seat non-Claude; matrix populated in `01-deliberation.md §0`; synonym-drift guard distinct (P3 frame-completion produced Substrate-N1/N2/N3 + portability middle-path; P4 audited P1/P2 for Claude-lineage shared-frame-blindness + named 5 dissent-preservation items); no mid-session departure.

**M2 disposition**: **vindicated**. The 7-column matrix + lineage-constraint + synonym-drift-guard + departure-discipline produced observationally-distinct outcomes across 3 consecutive MAD sessions. No evidence that the discipline created drift-to-ritual or gamed the Outsider seat. Vindicated-as-routine-practice going forward.

**Triggers met:** [d016_3]

**Triggers rationale:** `d016_3` fires because S050 is the third-of-3 verification-window instance for the D-133 M2 convention (S045 + S047 + S050). No specification is edited by the vindication disposition itself (M2 is an operational discipline, not a spec); the disposition closes the multi-session verification coordination.

**Rejected alternatives**:
- Continued-preservation (not vindicated; keep running): rejected — three clean exercises across distinct MAD classes (OI-016 domain-validation; external-app arc-plan; substrate adoption) is the specified window.
- Discharge-not-vindicated: rejected — no evidence of discipline failure.
- Extend window to fourth instance: rejected — S048 D-154 interpretation locked the window at three; moving the goalposts would retrospectively alter the verification criterion.

**Non-Claude participation**: per §10.4-M2 preservation-preservation lineage — this session's non-Claude (P3+P4) participation is itself a data point for M2's verification window.

---

## D-176: Housekeeping (consolidated 14-item)

1. **D-129 standing discipline sixth consecutive clean exercise** (S046/S047/S048/S049/S050). 00-assessment.md §5b surfaced five considered-and-rejected session-shape alternatives with non-vacuous rationales. Convention remains operational. §5.12 Path-Selection Defender reopen warrant (a) does not fire. Sixth clean exercise post-graduation.
2. **D-138 folder-name default fifth consecutive exercise clean** (S046 build / S047 content-MAD / S048 default-agent-triage / S049 synthesis-meta-decision / S050 adoption-scheduled-MAD). `050-session` no suffix, no slug. Five consecutive sessions across five distinct classes.
3. **Path AS (Adoption-Scheduled) reified at n=2**. S049 first-instance + S050 second-instance (pre-scheduled at S048 D-155; ran as pre-scheduled MAD without mid-ratification reshape). Path AS now a reified default-agent path-label alongside Path A / Path OS / Path OC / Path PSD / Path PD / Path T.
4. **Engine-v8 preservation window closed at depth 2** (S049 + S050-pre-adoption-state). Engine-v9 takes over at S050 close per D-172.
5. **Active OIs**: 13 unchanged at S050 close. OI-019 sub-question (f) "extended-baseline visibility mechanism" cross-referenced in EF-047-retrieval-discipline triage; no closure at S050 (sub-question is territory for Substrate-N3 registries phase-2+ consideration, not retrieval-contract v1 scope).
6. **31 → 36 preserved first-class minorities** per D-173. §10.4-M1 through §10.4-M6 unchanged. §10.4-M7 through §10.4-M11 new.
7. **Engine-feedback status**: 0 new / 3 triaged → 0 new / 0 triaged / 4 resolved / 0 rejected. All three S050-scheduled EF-047 triage records transition to `status: resolved`.
8. **WX-43-1 OI-promotion**: cumulative explicit-instruction-variant window n=0-of-9 (S047 + S049 + S050). Baseline n=6-of-8 window closed at S045. OI-promotion threshold met on baseline; not promoted — pattern-consistency and the explicit-instruction variant's 0-of-9 clean-slate undercut the original concern. **WX-43-1 OI-promotion discharged-as-not-warranted** at S050 close.
9. **WX-34-1 SESSION-LOG**: pre-close 7951 words; post-thin-row forecast 7951 + ~180 = ~8131, breaching 8K hard-ceiling by ~131. Per operator Q5=(a) ratification, thin-row discipline held; the 8K breach is expected and disclosed. WX-34-1 carries forward as soft-warning-plus-breach; S051 restructure candidate (WX-34-1 forward observation: if S051 opens above 8K the restructure is forced).
10. **WX-24-1 MAD v4 no-growth streak**: S050 does not amend `multi-agent-deliberation.md` v4. Twenty-third-session no-growth streak from S042 reset. New record.
11. **WX-28-1 twenty-first close-rotation zero retention-exceptions**: S044 rotates OUT; S050 close enters. Twenty-one consecutive rotations S029–S050 all zero-retention-exceptions. Streak continues vindicated.
12. **§5.6 GPT-family-concentration fourth-consecutive-worst-case-side data point** (S044+S045+S047+S050). Per `01-deliberation.md §5` synthesis: §5.6 spirit-level observation carries forward **without** discharge/vindication this session — P3+P4 non-Claude contribution was substantive and load-bearing; no shared-frame collapse onto Claude consensus. But the fourth consecutive worst-case-side composition is a cumulative observation that deserves eventual spirit-level re-examination in a future MAD with non-GPT non-Claude participation.
13. **S047 D-150 deferred spec-amendment candidates (i)+(ii)+(iii)**: preserved for post-arc self-dev review. Candidate (iv) subsumed at S048 by D-153.
14. **S049 D-162 housekeeping items**: all carried forward observations applied at S050. `selvedge-disaster-response` external arc status: unchanged from S048 close; S002–S005 pending operator transport; S050 self-dev session does not block external arc progress. The substrate will become available to the external arc at the arc's next bootstrap-refresh (operator-discretionary).

**Triggers met:** [d016_3]

**Triggers rationale:** `d016_3` fires because housekeeping items include multi-session observations (D-129 sixth exercise; D-138 fifth exercise; §5.6 fourth-consecutive; WX-28-1 twenty-first rotation; WX-24-1 twenty-third-session no-growth streak). No specification is edited by housekeeping items themselves. No `d023_*` fires — MAD-derived items were decided in D-164–D-173; housekeeping is bookkeeping.

**Rejected alternatives**: piece-by-piece as individual decisions — rejected for density reasons; consolidated per S049 D-162 precedent.

**Non-Claude participation**: some items (§5.6 evaluation; D-133 M2 vindication) cross-reference non-Claude perspective contribution. Others (housekeeping) are single-orchestrator Case Steward bookkeeping.

---

## Summary table

| D | Subject | Class | Engine-v impact | Minorities preserved |
|---|---------|-------|-----------------|----------------------|
| D-163 | Halt-1 ratifications + Q6 scope expansion | operator-directed | none direct | — |
| D-164 | Q1 Substrate-1 SQLite FTS5 | substantive | supports v9 | §10.4-M8 (DuckDB) |
| D-165 | Q2 phase-1 minimum scope | substantive | supports v9 | §10.4-M7 (P2 minimum) |
| D-166 | Q3 no kernel amendment phase-1 | design (deferral) | none | — |
| D-167 | Q4 two-label aliases + schema_version | minor adoption | supports v9 | — |
| D-168 | Q5 session-open mtime only | design (implementation) | supports v9 | — |
| D-169 | Q6 defer `syncs_with:` | design (deferral) | none | §10.4-M11 (distinction) |
| D-170 | Q7 engine-defined contract + engine-adjacent | substantive | supports v9 | §10.4-M9 (P1 eng-def) |
| D-171 | Q8 defer check 24 | design (deferral) | none | — |
| D-172 | retrieval-contract.md v1 + engine-v8→v9 | substantive | **v9 bump** | — |
| D-173 | Phase-2 gate + 5 preserved minorities | substantive | supports v9 | §10.4-M7–M11 (5 total) |
| D-174 | Bundled-minor dispositions | minor | none | — |
| D-175 | D-133 M2 third-of-3 vindicated | methodology | none | — |
| D-176 | Housekeeping 14-item | bookkeeping | none | — |

End of decisions.
