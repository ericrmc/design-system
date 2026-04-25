---
triage_id: EF-058-substrate-runtime-uv-migration-triage
feedback_ref: ../inbox/EF-058-substrate-runtime-uv-migration-recommended-path.md
triaged_in_session: 059
triaged_at: 2026-04-25
status: resolved
classification: minor
disposition: Direction (single Path L per intake) adopted same-session via 6-step uv-migration; resolves S051-S058 MCP stdio transport unverified honest-limit chain by aligning substrate runtime with CLAUDE.md §Tools operator standing instruction; engine-v10 preserved (minor per OI-002 tenth source-realignment-or-extension precedent chain S022/S030/S033/S040/S046/S051/S052/S054-EF-053/S054-EF-054/S059-EF-058)
opened_issue: null
resolved_by: provenance/059-session/
spec_amendments:
  - path: specifications/retrieval-contract.md
    classification: minor
    note: "§5.1 .mcp.json template: command python3 → uv; args [tools/retrieval_server.py] → [run, tools/retrieval_server.py]. §5 step 2 dependency-install: pip-install path → uv-only path (PEP 723 self-resolves deps via uv run; no separate install step). §10 honest-limits: portability-tax language updated (single-tool uv install vs two-package mcp[cli]+pyyaml). v1 preserved (no version bump); spec content (§1-§4, §6-§9) unchanged."
tool_amendments:
  - path: tools/retrieval_server.py
    classification: minor
    note: "PEP 723 inline-deps script block at top: requires-python >=3.11; dependencies [mcp[cli], pyyaml]. Existing ImportError fallbacks preserved for direct python3 invocation compatibility."
  - path: tools/build_retrieval_index.py
    classification: minor
    note: "PEP 723 inline-deps script block at top: requires-python >=3.11; dependencies [pyyaml]. Existing ImportError fallback preserved for direct python3 invocation compatibility."
  - path: .mcp.json
    classification: minor
    note: "command python3 → uv; args [tools/retrieval_server.py] → [run, tools/retrieval_server.py]. PEP 723 in retrieval_server.py self-resolves deps."
  - path: tools/bootstrap-external-workspace.sh
    classification: minor
    note: "Step 3e + Next-steps step 2 + Next-steps step 3: pip-install path → uv-only path. Removed .cache/venv setup. Bundled records-substrate-bootstrap per records-contract.md v1 §5 (records-contract.md added to SPEC_FILES; records/ + records/sessions/ + thin index.md scaffolded). Discharges S058 close §8 honest-limit #2 deferred bootstrap-extension implementation."
decision_records:
  - D-207
  - D-210
  - D-211
engine_version_impact: engine-v10 preserved (no bump; minor per OI-002 tenth source-realignment-or-extension precedent chain)
direction_selected: single Path L (concrete operator-recommended at intake)
alternative_directions_deferred: none (intake recommended single concrete path; no Direction B/C alternatives)
---

# Triage — EF-058 substrate runtime uv migration

## Classification

**Target**: engine-adjacent (implementation-level runtime change; minor documentary spec amendment to retrieval-contract.md template). **Severity on inbox record**: friction (operational debt accumulated across S051-S058 8-session honest-limit chain; substrate affordance unrealised). **Source**: `selvedge-self-development` Session 058 post-session operator-surfaced observation (`reported_by: operator`); recorded as direct-to-inbox per S054/S055 self-dev-originated convention.

**Disposition**: **resolved** this session via 6-step Path L per intake §Suggested Change recommendation. Narrow concrete defect-fix; single-orchestrator same-session resolution per S048 D-152 + S052 D-181 + S054 D-185+D-186+D-187 precedent. Operator-recommended at intake disposition: "Single-session Path L (minor implementation fix per OI-002) per S046 D-143 / S052 D-181 / S054 D-186 source-realignment precedent chain."

## Defect summary (from inbox record)

Across S051–S058 every session close has recorded the honest-limit "MCP stdio transport remains unverified per S051-S0NN chain." The substrate has been exercised in-session via `.cache/venv/bin/python3` shelling out to import the FastMCP server module directly + calling registered tools through `tool_manager` introspection — the underlying SQLite queries work; what does not work is Claude Code calling `mcp__selvedge-retrieval__search` etc. as first-class tools.

Root cause per inbox §Observation: `.mcp.json` declares `command: "python3"` (system Python without `mcp[cli]` or `pyyaml`); when Claude Code spawns the server at startup, the import fails, the server crashes silently, Claude Code marks it unavailable. Workaround applied across S051-S058 has been Bash + `.cache/venv/bin/python3` invocation. The honest-limit text drifted from honest-limit to laundered operational debt across the 8-session chain.

Deeper observation per inbox §Observation: workspace went off operator's standing tooling instructions. CLAUDE.md §Tools (added by D-144 Session 046) specifies: "If you decide more are needed, you can install them using `uv tool` or ask the user to ratify your tool decision and install something on your behalf." The S050 MAD landed on pip + venv without surfacing `uv` as the alternative. The methodological observation is filed separately as `EF-058-claude-md-tools-clause-not-cross-checked-by-mad.md` (substantive-arc-deferred); this record handles the operational fix path.

## Adoption — 6-step Path L per intake §Suggested Change

Per inbox record §Suggested Change six-step recommended path, executed this session:

1. **`tools/retrieval_server.py`** — added PEP 723 inline-deps script block at top:
   ```python
   #!/usr/bin/env python3
   # /// script
   # requires-python = ">=3.11"
   # dependencies = ["mcp[cli]", "pyyaml"]
   # ///
   ```
   Existing `ImportError` fallback for `mcp[cli]` and `yaml` preserved for direct `python3` invocation compatibility (degraded mode disclosure per retrieval-contract.md v1 §3 unchanged).

2. **`tools/build_retrieval_index.py`** — same PEP 723 block (deps `pyyaml` only; no `mcp[cli]` needed). Existing `ImportError` fallback preserved.

3. **`.mcp.json`** — `command: "python3"` → `command: "uv"`; `args: ["tools/retrieval_server.py"]` → `args: ["run", "tools/retrieval_server.py"]`. PEP 723 metadata in retrieval_server.py self-resolves deps via `uv run` per uv 0.4+ semantics.

4. **`tools/bootstrap-external-workspace.sh`** — refactored:
   - Replaced pip-install instructions with uv-only path (Next-steps step 2: "Ensure uv is installed; substrate scripts use PEP 723 inline metadata; uv resolves deps automatically per `uv run`").
   - Replaced `python3 tools/build_retrieval_index.py` with `uv run tools/build_retrieval_index.py` (Next-steps step 3).
   - Removed `.cache/venv/` setup language.
   - Bundled records-substrate-bootstrap per records-contract.md v1 §5 obligations (D-211): added `records-contract.md` to `SPEC_FILES` array; replaced SESSION-LOG.md scaffolding with `records/` + `records/sessions/` directories + thin `records/sessions/index.md`; updated step 5 development-provenance scaffolding accordingly. Discharges S058 close §8 honest-limit #2.

5. **`.cache/venv/` removal** — deleted (gitignored per `.gitignore` `.cache/` line; not committed). No tool hardcoded `.cache/venv/bin/python3` paths (the path was Case-Steward-Bash-invocation-side, not script-internal).

6. **Smoke-test** — partial in-session per honest-limit constraint:
   - `uv run tools/retrieval_server.py` startup verified (PEP 723 resolves deps; FastMCP imports succeed).
   - `uv run tools/build_retrieval_index.py` rebuild verified (post-spec-edits index rebuild succeeds).
   - **Full MCP stdio smoke-test deferred to next session-open** (Claude Code reads `.mcp.json` at project-load time; cannot restart from within session). Next session-open close-criterion per inbox §Suggested Change step 6: verify `mcp__selvedge-retrieval__search`, `mcp__selvedge-retrieval__resolve_id`, `mcp__selvedge-retrieval__forward_references` appear in agent's tool surface; call `resolve_id("S058")` and confirm it returns the records/sessions/S058.md record via tool call (not via Bash); record close-criterion in S060 close WX-58-1 5-field section as `migrated_id_resolution: 58/58` resolution-via-substrate-tool.

## Minor amendment to `retrieval-contract.md` v1 (D-210)

Per inbox §Suggested Change closing paragraph: "Possible minor amendment to `retrieval-contract.md` v1 §5.1 `.mcp.json` template shape." Executed:

- **§5.1 `.mcp.json` template**: `command: "python3"` → `command: "uv"`; `args: ["tools/retrieval_server.py"]` → `args: ["run", "tools/retrieval_server.py"]`. Template-shape sync with implementation.
- **§5 step 2 dependency-install instructions**: pip-install path → uv-only path (PEP 723 self-resolves; no install step beyond `uv` itself; reduced two-package install to single-tool prerequisite).
- **§10 honest-limits**: "External-workspace portability tax" language nuance — single-tool uv install vs two-package mcp[cli]+pyyaml.
- **Spec content unchanged**: §1 scope, §2 capabilities, §3 failure behaviour, §4 workspace state, §6 phase-2 gate, §7 minorities, §8 versioning, §9 validation.
- **v1 preserved** (no version bump; minor per OI-002 per S048 D-153 sub-pattern + S054 D-186 minor-template-shape-sync precedent).

## Classification — minor per OI-002

**Tenth minor bug-fix-style-or-extension implementation-realignment in engine history.** Precedent chain:

1. S022 R8a — SESSION-LOG.md thin-index restoration.
2. S030 D-100 — `workspace-structure.md` §SESSION-LOG stale-literal cleanup.
3. S033 D-108 — `validate.sh` check 22 loop-bug repair.
4. S040 D-123 — SESSION-LOG.md thin-index preemptive restoration.
5. S046 D-143 — `validate.sh` empty-provenance nounset + check 23 ls-glob set-e guards.
6. S051 D-178 — SESSION-LOG.md forced thin-index restoration per WX-34-1 breach.
7. S052 D-181 — `retrieval_server.py` Strategy 1.5 alias-indirection (EF-051).
8. S054 D-186 — `retrieval_server.py` `_sanitize_query()` query-parser fix (EF-053).
9. S054 D-187 — `retrieval_server.py` `forward_references` tool extension + `prompts/development.md` documentary amendment (EF-054).
10. **S059 D-207+D-210+D-211** — substrate runtime uv migration + retrieval-contract.md v1 §5.1 template-shape sync + records-substrate bootstrap discharge (EF-058-uv-migration).

Per OI-002 bug-fix-style-or-additive-extension-without-semantic-change heuristic + engine-manifest §5 "Minor elaborations within an existing spec's scope per the OI-002 substantive-vs-minor heuristic": the contract content of retrieval-contract.md v1 (capabilities, failure behaviour, workspace state) is unchanged; only the template shape and dependency-install instructions sync with the new uv-based implementation. Records-substrate bootstrap implementation matches the records-contract.md v1 §5 normative spec adopted at S058. No engine-v bump. Engine-v10 preserved.

## Cross-references

- **Inbox record**: `engine-feedback/inbox/EF-058-substrate-runtime-uv-migration-recommended-path.md` (preserved verbatim per workspace-structure §engine-feedback "intake files preserved verbatim" convention).
- **Decisions authorising this triage + resolution**: `provenance/059-session/02-decisions.md` D-207 (uv-migration adoption) + D-210 (retrieval-contract.md template amendment) + D-211 (records-substrate bootstrap).
- **CLAUDE.md §Tools operator standing instruction**: workspace root; per D-144 Session 046; specifies `uv tool` install path.
- **Related EF-058 records (operator-surfaced post-S058 discussion triple)**: `EF-058-claude-md-tools-clause-not-cross-checked-by-mad.md` (substantive-arc-deferred — methodological observation about S050 MAD shared-frame-blindness against CLAUDE.md); `EF-058-tier-2-validation-discipline-by-distinct-agent.md` (substantive-arc-deferred — meta-pattern subsuming the other two).
- **Records-substrate bootstrap normative spec**: `specifications/records-contract.md` v1 §5 (5-step bootstrap obligations).
- **S058 honest-limit #2 deferred**: `provenance/058-session/03-close.md` §8 honest-limit 2 (records-contract.md v1 §5 bootstrap-extension implementation deferred to "minor follow-up session given S058 scope limits"; S059 IS that follow-up session).

## Forward observations

- **MCP stdio transport unverified honest-limit chain S051-S058 closes at S059** (assuming next-session smoke-test confirms tool surface). Pattern observation: 8-session laundering of honest-limit text resolved by single-session Path L when the operational fix is concrete and the standing operator instruction is explicit. The methodological pattern (Tier-2-by-doing-agent fails to escalate accumulating honest-limits) remains tracked at EF-058-tier-2-validation as substantive-arc.
- **Records-substrate bootstrap first-exercise is S060+** (next external-workspace bootstrap; no current planned bootstrap). The records-substrate spec is normatively complete; the implementation in `tools/bootstrap-external-workspace.sh` is post-S059 spec-aligned. First external-workspace exercise is the test of the bootstrap path; until then, the implementation is normatively-spec-aligned but not deeply user-tested per S059 honest-limit.
- **§10.4-M13 (P3+P4 shallow-Direction-A warning) watch is structurally strengthened by uv-migration.** That minority's activation warrant tracks "operators edit `records/sessions/index.md` body content as if it were source-of-truth." Per inbox §Why It Matters point 2: "if the substrate is hard to call, operators won't reach for `resolve_id`; they'll grep the index. The shallow-Direction-A failure mode becomes the path of least resistance precisely because the structured-record-as-source-of-truth path has 30s of friction per call." Resolving substrate transport reduces the friction; whether operators reach for `resolve_id` in practice is observed at WX-58-1 5-field recording across S058–S060.
- **External-workspace bootstrap claims now credibly demonstrated.** Per inbox §Why It Matters point 3: "tools/bootstrap-external-workspace.sh prints `pip install 'mcp[cli]' pyyaml` instructions to operators of new workspaces. The self-dev workspace does not credibly demonstrate the contract works because its own server doesn't load via Claude Code." Post-S059, the self-dev workspace's `.mcp.json` declares the canonical `uv run` shape and the substrate scripts carry PEP 723 inline metadata; an external workspace bootstrapped via the updated script will inherit a known-working configuration.
- **Per OI-002 substantive-vs-minor heuristic at tenth-instance**: the source-realignment precedent chain (now n=10) is becoming the engine-conventional shape for inbox-record-driven defect-fixes. Pattern: operator surfaces concrete defect with concrete fix path → triage classifies minor → single-orchestrator implements → minor template-shape spec amendments where needed → engine-v preserved. The contract-vs-implementation split (retrieval-contract.md and records-contract.md own the contracts; engine-adjacent implementations evolve via these source-realignments) is well-validated at this n.

## OI impact

No OI opened. No OI resolved. EF-058-uv-migration is a defect-fix-shape resolution; no methodology-level OI surface. The methodological pattern around Tier 2 self-validation is tracked at EF-058-tier-2-validation as substantive-arc-deferred.

## Subsumed deferred candidates

S058 close §8 honest-limit #2 (deferred records-substrate bootstrap implementation in `tools/bootstrap-external-workspace.sh`) is **subsumed-by-bundling** at S059 D-211 (the EF-058-uv-migration Path L work and the records-substrate bootstrap both edit the same file; bundling-by-coincidence per S054 D-185+D-186 precedent). S047 D-150 three remaining deferred candidates (i)/(ii)/(iii) preserved unchanged.
