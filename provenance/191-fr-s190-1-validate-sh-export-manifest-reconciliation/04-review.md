---
session: 191
title: fr-s190-1-validate-sh-export-manifest-reconciliation — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high**: Pass 2 SQL query at line 113 of manifest_reconcile.sh interpolates $REL directly into single-quoted string without escaping; if slug ever contains a quote (past integrity failure or future schema gap), the query fails and produces false-positive L5-orphan report
  - **fixed.** Pass 2 restructured to pre-fetch ALL_MANIFEST_PATHS once and use grep -qxF for membership; no per-row SQL interpolation remains. Test test_quote_in_slug_does_not_break_pass_2 confirms a slug carrying quotes/semicolons does not break the pass.
- **medium**: sessions.slug has no CHECK constraint in schema (only application-level kebab-case validation via Python); if a future schema edit permits non-kebab slugs or a direct SQL injection lands a malformed row, Pass 2 false-positives are possible
  - **fixed.** Bash-layer slug guard added rejecting empty/path-separator/.. slugs in pass 2 before SDIR construction; test test_slug_with_path_separator_rejected covers the escape/me shape. Defence-in-depth against future malformed substrate rows even if no SQL CHECK lands.
- **low**: Pass 1 empty-manifest guard ([ -z "$REL_PATH" ] && continue) correctly handles both completely empty manifest and single-line read with empty vars; tested and verified
  - **adjudicated.** (no disposition recorded)
- **low**: Path normalization via $WORKSPACE/$REL_PATH works correctly across macOS and Linux even with leading ./ or // variants; tested and verified on both platforms
  - **adjudicated.** (no disposition recorded)
- **low**: Path-traversal rejection via case "*..*)" does not false-positive on legitimate directory names because no provenance/ entries contain .. as a substring; verified across live workspace
  - **adjudicated.** (no disposition recorded)
- **low**: workspace_session_no is INTEGER per schema (PRAGMA table_info confirmed); $WNO in Pass 2 is always numeric from SQL query result, preventing injection via non-integer session_no
  - **adjudicated.** (no disposition recorded)
- **low**: Pytest fixture intentionally creates only export_manifest + sessions tables (minimal schema); this is appropriate since script is read-only and does not exercise migrations 001-043; existing tests pass 344 total including 10 new tests
  - **adjudicated.** (no disposition recorded)
- **low**: Pre-adoption skip logic uses "session has any manifest row" as adoption signal; this is correct for post-engine-v52 sessions (migration 044 first creates export_manifest table), matching sealed design
  - **adjudicated.** (no disposition recorded)
- **high**: Pass 2 error handling via error-suppression suppresses SQL syntax errors silently; a malformed query produces empty result triggering false-positive L5-orphan report with no diagnostic context
  - **fixed.** Inner per-row sqlite3 call removed in pass 2 restructure; the only remaining suppressed sqlite3 call (HAS table-exists check) is now unsuppressed and will surface real errors. The HAS_SESSIONS check sqlite3 call also unsuppressed.
- **medium**: Export pipeline uses parameterized queries for manifest writes (SQLite question-mark placeholders), providing defense-in-depth against sql-injection in stored paths; manifest-reconcile.sh should match this discipline
  - **fixed.** Pass 2 no longer interpolates path strings into SQL; only INTEGER session_no remains in pass 2 SQL via JOIN clause (m.session_no = s.workspace_session_no), and integer values are typesafe. Bash-layer matches export-pipeline parameterization discipline by avoiding string interpolation entirely.
- **low**: validate.sh integration places manifest-reconcile.sh between substrate validate and pytest per sealed design (P-4 schema_sketch step 1); verified correct positioning in file
  - **adjudicated.** (no disposition recorded)
- **low**: Test coverage includes 10 pytest cases covering clean pass, missing-on-disk, sha-mismatch, L5-orphan, pre-adoption-skip, NULL-session-no rows, absolute-path-rejection, path-traversal-rejection, and missing-DB warn-and-pass; matches sealed design test spec
  - **adjudicated.** (no disposition recorded)
## Iteration 2

- **low**: Iteration-2 audit confirms iter-1 HIGH/MEDIUM (45/46/53/54) closed correctly: pass-2 grep-qxF membership replaces SQL interpolation, error-suppressions removed, bash-layer slug+wno guards add defence-in-depth, no new vulnerabilities introduced.
  - **adjudicated.** Re-review iteration 2 reports clean across portability (Darwin/Linux), partial-substrate handling (HAS/HAS_SESSIONS gates), test coverage (13 cases including SQL-injection regression + slug-escape + path-quote-no-misreport), and exit-code propagation. validate.sh uses if-conditional not pipefail so manifest_reconcile.sh exit 1 surfaces correctly.

## Terminal passes

- **iteration 2** — clean @ `2123497bfa86`
  - Iter-1 surfaced 2 HIGH (45 SQL inject in pass-2 path interpolation; 53 error-suppression masks SQL syntax errors) plus 2 MEDIUM (46 sessions.slug no CHECK; 54 parameterized-query discipline gap); all four dispatched fixed by pass-2 grep-qxF restructure plus bash slug+wno guards. Iter-2 audit confirmed closures sound and no new issues introduced.
