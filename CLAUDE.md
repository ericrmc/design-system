# CLAUDE.md

## Commit workflow

Before finishing your response, stage all changed/new files, commit with a concise message, and push using git directly.

## Tools
This contains usage instructions for tools you have requested. If you decide more are needed, you can install them using `uv tool` or ask the user to ratify your tool decision and install something on your behalf. Add additional instructions here as you see fit.

### Multi-agent work

When work would benefit from multiple independent perspectives or parallel efforts, consider using agent teams via the `TeamCreate` tool (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`). You also have access to the Google `gemini` and OpenAI `codex` CLI tools for non-Anthropic LLM access. Codex is preferred for any thinking or reasoning tasks.

### mempalace (orchestrator-convenience, non-engine)

`mempalace` v3.1.0 is installed via `uv tool`. It is classified as orchestrator-convenience tooling, analogous to the `gemini`/`codex` CLIs above. **It is NOT part of `engine-manifest.md` §3 and is NOT required by any specification.** External-application workspaces loading the engine do not inherit the dependency; fresh clones of this workspace can operate without it. This classification is load-bearing for the engine's text-only portability claim; do not promote mempalace into any engine-definition file without a dedicated deliberation.

Suggested use: when a single Read would exceed the 25,000-token ceiling (SESSION-LOG.md, open-issues.md, aggregated provenance search), orchestrators may run `mempalace search "<query>" --wing complex-systems-engine` or `mempalace wake-up --wing complex-systems-engine` to retrieve candidate matches.

**Critical caveats (per Session 020 hands-on finding; see `provenance/020-workspace-scaling-deliberation/01b-perspective-tooler.md`):**

- Despite the `mempalace --help` description ("Find anything, exact words"), `search` is semantic/vector-ranked, not exact-string match. Exact-string queries like `D-074` may return zero results containing that string even when the string exists in indexed files. Use `Grep` for exact-string verification.
- `wake-up` output is drawer-count-dominated rather than recency-weighted; it is useful for fresh-session priming but does not substitute for reading SESSION-LOG.md.
- `mine` does not deduplicate versioned specs — superseded `-v2.md` / `-v3.md` files are indexed alongside current canonical files and may rank above them.
- mempalace output is **candidate-discovery only.** Every cited claim must be reconfirmed against the source file via Read before inclusion in session artefacts. Treating mempalace output as authoritative is the laundering risk (OI-015-adjacent, WX-20-1 watchpoint).

Initialisation (one-time, if adopted): `mempalace init . && mempalace mine .` in workspace root. The init creates `mempalace.yaml` + `entities.json` in the workspace root — both are gitignored. The palace state itself lives at `~/.mempalace/palace/`, outside the workspace.

Re-mine cadence: manual, typically at session close after substantive file changes. Not a spec requirement; orchestrators not using mempalace need not re-mine.
