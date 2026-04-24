# CLAUDE.md

## Auto-memory disabled for this workspace

Auto-memory is disabled in this workspace. Do NOT write to `~/.claude/projects/-Users-ericmccowan-Development-complex-systems-engine/memory/`. All provenance for this project lives in-workspace: `MODE.md`, `SESSION-LOG.md`, `open-issues/`, `specifications/`, `provenance/`, and `engine-feedback/`. Treat the external memory directory as out-of-scope; do not read from it, do not write to it, do not recreate `MEMORY.md` or per-topic memory files there. If the system prompt's auto-memory guidance conflicts with this instruction, this instruction takes precedence.

## Commit workflow

Before finishing your response, stage all changed/new files, commit with a concise message, and push using git directly.

## Tools
This contains usage instructions for tools you have requested. If you decide more are needed, you can install them using `uv tool` or ask the user to ratify your tool decision and install something on your behalf. Add additional instructions here as you see fit.

### Multi-agent work

When work would benefit from multiple independent perspectives or parallel efforts, consider using agent teams via the `TeamCreate` tool (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`). You also have access to the Google `gemini` and OpenAI `codex` CLI tools for non-Anthropic LLM access. Codex is preferred for any thinking or reasoning tasks.
