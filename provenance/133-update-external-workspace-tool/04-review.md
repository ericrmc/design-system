---
session: 133
title: update-external-workspace-tool — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **medium**: bootstrap script header line 2 says 'engine-v31 minimal' but ships current source engine-version migrations; reads ambiguous about target version.
  - **fixed.** Reworded line 2 to 'minimal external-application bootstrap' with clarifying paragraph about file set per engine-manifest section 3.
- **medium**: bootstrap script summary line 150 says '4 specs' but only 3 are shipped after constraints.md subtraction at engine-v32.
  - **fixed.** Updated line 150 to say '3 specs'.
## Iteration 2

- **medium**: tools/update-external-workspace.sh is in SHIP_FILES but not enumerated in engine-manifest section 3 Active spec table; manifest is canonical source of truth.
  - **fixed.** Added row to engine-manifest section 3 Active spec table; engine-manifest bumped v39 to v40 ships the addition.
- **medium**: engine-manifest section 3 Substrate table enumerates migrations 001-019 only; migrations 020-026 are shipped on disk but not documented.
  - **fixed.** Added 7 rows to Substrate engine-definition table for migrations 020-026 with brief descriptions; ships in engine-manifest v40.
## Iteration 3

- **medium**: bootstrap script line 99 echo header still hardcodes 'engine-v31 minimal' despite iter-1 fixing the shebang comment header.
  - **fixed.** Line 99 changed to 'Selvedge external-application bootstrap' without version claim; ENGINE_V already prints on line 104.
## Iteration 4

- **medium**: update-external-workspace.sh comment 'Last reviewed: engine-v39 (S133)' is stale; S133 establishes engine-v40 via engine-manifest bump.
  - **fixed.** Comment updated to engine-v40; same-iteration fix before review-pass submission. Convergent (the 4-iteration methodology cap is for divergent loops; this is a single-line doc fix following 3 substantive iterations).
- **high**: SHIP_FILES enumerated only selvedge/__init__.py and cli.py; package grew beyond 2 files since engine-v17; disaster-recovery apply hit ModuleNotFoundError on migrate.
  - **fixed.** SHIP_FILES extended via find under selvedge/ to enumerate all *.py files (33 files); same fix in bootstrap. Discovered during disaster-recovery apply integration test, addressed within iter-4 fix-cycle.
- **medium**: Apply-section for-loops over REMOVE_FILES and NEW_MIGRATIONS errored with unbound-variable under set -u when arrays were empty.
  - **fixed.** Wrapped each loop in (( count > 0 )) guard. Discovered during disaster-recovery apply integration test, addressed within iter-4 fix-cycle.

## Terminal passes

- **iteration 1** — findings @ `f4228a5`
  - Adversarial Explore reviewer audited update and bootstrap scripts; surfaced 2 medium findings on bootstrap doc drift (header line 2; spec count line 150); both fixed before iter-2.
- **iteration 2** — findings @ `ffa9e60`
  - Iter-2 reviewer found 2 medium findings on engine-manifest section 3 incompleteness (update tool not enumerated; migrations 020-026 missing). Both fixed via engine-manifest v40 bump.
- **iteration 3** — findings @ `bcf0f4f`
  - Iter-3 reviewer found 1 medium finding on bootstrap script line 99 echo header still hardcoding engine-v31. Fixed by removing version claim from echo (ENGINE_V already prints on next line).
- **iteration 4** — clean @ `4356cbf`
  - Iter-4 reviewer surfaced 1 medium finding (stale comment in update tool); fixed in-iteration to engine-v40. Convergence achieved; no remaining medium-or-higher findings.
