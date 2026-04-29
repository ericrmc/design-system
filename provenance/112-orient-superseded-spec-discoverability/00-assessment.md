---
session: 112
title: orient-superseded-spec-discoverability — assessment
engine_version_at_open: engine-v33
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

Engine-v33 active; FR-S111-7 directs addressing OI-S110-1 (orient does not surface superseded specs or supersession rationale).

## Agenda

1. Extend _orient_sections to compute recent spec supersessions joining decision_effects, objects, spec_versions, decisions_v2.
2. Render a Recent supersessions section in _orient_markdown bounded to most recent N=10 with truncation hint.
3. Record the decision with support citing OI-S110-1 and FR-S111-7 plus rejection of dedicated subcommand alternative.
4. Run a reviewer subagent on the cli.py change and iterate until clean.
5. Author engine_feedback observation and dispose FR-S111-7 and the OI-S110-1 portion of FR-S110-11.
