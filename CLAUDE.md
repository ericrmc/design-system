# CLAUDE.md

## Auto-commit hook

Before finishing your response, write a concise commit message summarizing what you did to `.claude/commit-message.txt`. A Stop hook will use this file for `git commit` and then push. If you don't write the file, the hook falls back to a diff-based summary.
