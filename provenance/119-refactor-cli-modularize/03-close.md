---
session: 119
title: refactor-cli-modularize — close
engine_version_at_close: engine-v34
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S119 split selvedge/cli.py (4507 lines) into per-concern modules with extracted submit-handler helpers; behavior-preserving refactor under DV-S119-1.

## Engine version

- engine-v34 unchanged (refactor only; no spec or schema bumps).
## What was done

- Split cli.py into selvedge/{paths,errors,connection,aliases,migrations,init_cmd,id_allocate,query,recover,validate,subtract,orient,schema,monitor_external}.py.
- Created selvedge/submit/ package: __init__ (handlers + cmd_submit), _helpers, session, legacy_decision, deliberation, decision_v2, spec, review, assessment, close, issue, feedback.
- Created selvedge/export/ package: __init__ (cmd_export), session, issues, anchor.
- Extracted _link_object helper (insert objects + UPDATE typed.object_id) and _next_no helper (COALESCE(MAX)+1 per-parent counter); applied across submit handlers.
- cli.py reduced to 156 lines: argparse setup + main dispatch only.
## State at close

- Smoke-test green (orient, schema, query, validate, export --session/--issues/--provenance --anchor, migrate --status, --help on every subcommand).
- Reviewer subagent (Explore, adversarial) audited iter-1 and reported no medium-or-higher findings; review-pass outcome=clean against head_sha=615550a.
## Open issues

- No new issues opened. FR-S118-10 (dry-run/sandbox harness) intentionally left undisposed; carries to next session.
## What the next session should address

- Land FR-S118-10: implement --dry-run or sandboxed test harness for write-path submits per EF-S118-1 friction; the modular cli surface now keeps that change scoped.
- Address next highest-priority open issue from orient queue if FR-S118-10 work blocks; OI-S104-2 (decision_effects.effect_kind deletes) and OI-S105-1 (third validation sense) remain low-friction candidates.
## Validator at close

- validate --precommit: ok at S119 close; head_sha=615550a; reviewer iter-1 clean.
