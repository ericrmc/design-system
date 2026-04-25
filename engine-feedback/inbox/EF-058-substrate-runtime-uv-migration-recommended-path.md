---
feedback_id: EF-058-substrate-runtime-uv-migration-recommended-path
source_workspace_id: selvedge-self-development
source_session: 058
created_at: 2026-04-25T18:00:00Z
reported_by: operator
target: engine-adjacent
target_files:
  - tools/retrieval_server.py
  - tools/build_retrieval_index.py
  - .mcp.json
  - tools/bootstrap-external-workspace.sh
severity: friction
status: inbox
---

# EF-058 — Substrate runtime uv migration (recommended path; resolves MCP stdio transport unverified chain)

## Observation

Across S051–S058 every session close has recorded the honest-limit "MCP stdio transport remains unverified per S051-S057 chain" (see e.g. S058 close §8 honest-limit 3 + §6 Substrate use). The substrate has been exercised in-session via `.cache/venv/bin/python3` shelling out to import the FastMCP server module directly and calling registered tools through `tool_manager` introspection — the underlying SQLite queries work; what does not work is Claude Code calling `mcp__selvedge-retrieval__search` etc. as first-class tools.

The most likely cause is small. Current `.mcp.json` declares:

```json
"command": "python3",
"args": ["tools/retrieval_server.py"]
```

System `python3` does not have `mcp[cli]` or `pyyaml` installed (those packages were pip-installed into `.cache/venv/` at S051 D-178). When Claude Code spawns the server at startup, the import fails, the server crashes silently, Claude Code marks it unavailable, and we never see the tools. We then fall back to `.cache/venv/bin/python3 -c "..."` for everything and call the gap "honest-limit."

The deeper observation is that the workspace went off the operator's standing tooling instructions. CLAUDE.md §Tools specifies:

> "If you decide more are needed, you can install them using `uv tool` or ask the user to ratify your tool decision and install something on your behalf."

The S050 MAD landed on pip + venv without surfacing `uv` as the alternative. See `EF-058-claude-md-tools-clause-not-cross-checked-by-mad.md` (filed separately) for the methodology-level observation about that drift; this record handles the operational path.

## Why It Matters

1. **Substrate adoption was supposed to be appealable via MCP tools.** S050's whole point was making cross-reference navigation and ID resolution into first-class tools an agent calls the same way it calls Read or Bash. With the transport broken, that affordance is unrealised — every substrate use requires Bash + Python incantation, which means in practice it gets used by the Case Steward at session-open and rarely otherwise.

2. **§10.4-M13 (P3+P4 shallow-Direction-A warning) watch is structurally weakened by this gap.** That minority's activation warrant tracks "operators edit `records/sessions/index.md` body content as if it were source-of-truth." But if the substrate is hard to call, operators won't reach for `resolve_id`; they'll grep the index. The shallow-Direction-A failure mode becomes the path of least resistance precisely because the structured-record-as-source-of-truth path has 30s of friction per call.

3. **External-workspace bootstrap claims unverified discipline.** `tools/bootstrap-external-workspace.sh` prints `pip install 'mcp[cli]' pyyaml` instructions to operators of new workspaces. The self-dev workspace does not credibly demonstrate the contract works because its own server doesn't load via Claude Code. Per `records-contract.md` v1 §5 + `retrieval-contract.md` v1 §5 bootstrap obligations.

4. **Honest-limit chain is laundering passively.** Eight sessions of recording the gap without acting is exactly the shape that the laundering-audit P4 role is supposed to catch in deliberation. Recording while not investing the upfront cost normalizes the broken state.

## Suggested Change

Single-session Path L (minor implementation fix per OI-002) per S046 D-143 / S052 D-181 / S054 D-186 source-realignment precedent chain. Six-step recommended path:

1. **`tools/retrieval_server.py`** — declare deps inline (PEP 723) at the top:
   ```python
   # /// script
   # requires-python = ">=3.11"
   # dependencies = ["mcp[cli]", "pyyaml"]
   # ///
   ```
2. **`tools/build_retrieval_index.py`** — same PEP 723 block (deps `pyyaml` only; no `mcp[cli]` needed).
3. **`.mcp.json`** — change `command: "python3"` → `command: "uv"`; `args: ["run", "tools/retrieval_server.py"]`.
4. **`tools/bootstrap-external-workspace.sh`** — replace pip-install instructions with `uv` install instruction (one tool; uv handles per-script dep resolution from PEP 723 metadata). Remove `.cache/venv/` setup.
5. **`.cache/venv/` removal** — delete (gitignored anyway). Update any tool that hardcoded `.cache/venv/bin/python3` paths (none expected; the path was Case-Steward-invocation-side, not script-internal).
6. **Smoke-test** — restart Claude Code after the changes; verify `mcp__selvedge-retrieval__search`, `mcp__selvedge-retrieval__resolve_id`, `mcp__selvedge-retrieval__forward_references` appear in the agent's tool surface; call `resolve_id("S058")` and confirm it returns the records/sessions/S058.md record via tool call (not via Bash); record close-criterion in the resolving session's WX-58-1 5-field section.

Engine-v10 preserved (no engine-definition spec edits; no contract revision; runtime-only). No new validator check needed; existing check 25 covers records-substrate integrity. Possible minor amendment to `retrieval-contract.md` v1 §5.1 `.mcp.json` template shape (the template currently shows `"command": "python3"`); minor per OI-002 per S048 D-153 sub-pattern.

If the smoke-test surfaces a non-trivial defect (FastMCP version pinning issue; stdio handshake mismatch; `uv run` PATH issue under Claude Code's spawn environment), reclassify as substantive substrate fix and open new EF record. The current scope assumes config-shape problem with config-shape fix.

## Evidence

- **S058 close §8 honest-limit 3 + §6 Substrate use note**: chain-of-record across S051-S058 documenting MCP stdio unverified.
- **`.mcp.json` (current state)**: `"command": "python3"` — system Python, no venv path.
- **`.cache/venv/` (built S051 D-178)**: contains `mcp[cli]` and `pyyaml` packages; gitignored. The packages exist; the server can find them when invoked via `.cache/venv/bin/python3`; the harness invokes via system `python3` and cannot.
- **CLAUDE.md §Tools (operator-written, present from D-144 Session 046)**: "you can install them using `uv tool`."
- **S050 deliberation §1 Q5 + §2.7 + Q7 + 01-deliberation-§3 phase-2 gate**: the MAD landed on pip+venv; uv was not surfaced as an alternative; this is what the methodology-observation record (`EF-058-claude-md-tools-clause-not-cross-checked-by-mad.md`) tracks.
- **`tools/bootstrap-external-workspace.sh`**: prints "pip install 'mcp[cli]' pyyaml" or "uv tool install pyyaml && uv tool install mcp" — note the second line uses uv but for `uv tool install` (CLI-tools mode) which is wrong shape for library imports; PEP 723 + `uv run` is the right shape.

## Application-Scope Disposition

Self-dev-originated. Operator-surfaced post-session intake (S058-post-session discussion). Direct-to-inbox per `engine-feedback/INDEX.md` Note-on-direct-to-inbox-placement convention; precedent EF-054 (operator-surfaced S053-post-session) + EF-055 (operator-surfaced S055-post-session). `source_workspace_id: selvedge-self-development` accurately reflects self-dev origin. `reported_by: operator` reflects operator-surfacing channel.

Severity `friction` (not blocker): the substrate has worked operationally via fallback path across 8 sessions; records-substrate at S058 closed cleanly with check 25 PASS. The friction is that the affordance is unrealised — the substrate does not appear as tools to agents — and the honest-limit chain has been recording-not-acting.

Triage scheduled S059. Recommended classification: **defect-fix-shape Path T+L** (resolve same session) per S054 D-185 + S052 D-180 precedent. The 6-step path is concrete, bounded, and reversible. If S059 default-agent state finds this primary agenda, single-orchestrator Path T+L resolves within session; updates `retrieval-contract.md` v1 §5.1 template (minor); commits + restarts; smoke-tests at session-close.

If operator surfaces alternative agenda (e.g., phase-2 mirrored-minority migration per S058 D-199 forward-commitment + WX-58-1 phase-2 gate evaluation at S058 close), this record persists in inbox until next default-agent slot.

Forward observation: this record's resolution at S059 would discharge the WX-58-1 first observation's "MCP stdio transport remains unverified" implicit limit + structurally engage the §10.4-M13 minority-watch by making `resolve_id` calls cheap enough that operators reach for them.
