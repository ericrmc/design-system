# Deprecated harness-telemetry digest emitter (engine-v15).
# Retained as a no-op stub at engine-v16 because the Claude Code PostToolUse
# hook references this path and the hook config is loaded at session start.
# The successor design (sessions 077-078) will replace the harness-telemetry
# arrangement entirely; the hook should be removed from .claude/settings.json
# in a fresh session, after which this stub can also be deleted.
#
# The original implementation is preserved at archive/pre-restart/tools/digest_emitter.py.
import sys
sys.exit(0)
