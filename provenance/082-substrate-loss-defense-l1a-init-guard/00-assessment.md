---
session: 082
title: substrate-loss-defense-l1a-init-guard — assessment
engine_version_at_open: engine-v51
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

S082 opens at engine-v51 against FR-S081-10 routing the smallest substrate-loss-defense slice: L1a init guard plus subagent-boilerplate amendment.

## Agenda

1. Implement L1a in selvedge/init_cmd.py: refuse --force when sessions table has any row; --really-force escapes; refusal names evidence and recovery path.
2. Amend prompts/development.md §4 subagent-discipline boilerplate to forbid init/migrate/sqlite-mutation against primary substrate per OI-S180-1 step 5.
3. Codex shape-consult adopted: predicate-(a) any-sessions-row-exists over fixture-allowlist; canonical file is development.md not PROMPT.md.
4. Run T-30 reviewer subagent loop on the Python change; address medium-or-higher findings before close.
5. Dispose FR-S081-10 and FR-S080-10 by-mechanism; defer L2b L3 L4 L5 to S083+ per FR-S081-11..14 routing.
