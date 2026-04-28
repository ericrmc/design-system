---
session: 099
title: substrate-driven-spec-authoring — assessment
engine_version_at_open: engine-v28
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

Engine-v28 ships closes_issue dispatch; manifest body still at v27 and prompt-development body lacks the closes_issue contract clause because S097/S098 hit OI-S090-5 substrate-authoring friction.

## Agenda

1. Land a substrate-driven spec-body authoring path so spec_versions can be authored without Bash heredoc bypassing the PreToolUse hook.
2. Use the new path to ship engine-manifest v28 with the engine-v28 history entry and the closes_issue dispatch surface notes.
3. Use the new path to ship prompt-development v4 documenting the closes_issue effect contract surfaced in S098.
4. Run the reviewer subagent loop on the handler change; address all medium-or-higher findings.
5. Triage EF-S098-3 (blocker) as addressed; observation/calibration EFs decide carry vs dispose.
6. Dispose forward-references this session resolves (FR-S098-8 minimum).
