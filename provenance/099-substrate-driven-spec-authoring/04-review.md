---
session: 099
title: substrate-driven-spec-authoring — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **critical**: body_path is not validated against workspace_root; ../../../etc/passwd escapes the workspace via mkdir + os.replace.
  - **fixed.** Path-traversal guard added: Path.resolve(strict=False).relative_to(workspace_root) refuses escapes; pytest test_inline_body_md_path_traversal_refused exercises ../escape.md.
- **high**: File is written before INSERT; if T-03 unique-active or other constraint refuses the row, the file is on disk with new content but no spec_versions row references it.
  - **fixed.** File write moved after INSERT + workspace_metadata UPDATE; rollback unwinds row before any file lands. Test test_inline_body_md_no_orphan_file_on_constraint_refusal.
- **medium**: body_md whitespace-only check is missing; the not-body_md guard rejects empty string but admits whitespace-only content like a single newline.
  - **fixed.** Whitespace-only guard: body_md.strip() check refuses whitespace-only input; pytest test_inline_body_md_whitespace_only_refused exercises a tab+newline payload.
- **medium**: write_text under utf-8 may translate newlines on Windows; encoded bytes should be written byte-for-byte so body_sha256 matches across platforms.
  - **fixed.** Switched to body_md.encode('utf-8') + Path.write_bytes for byte-for-byte writes; no platform newline translation can drift the on-disk content from the computed sha.
## Iteration 2

- **critical**: Path-traversal guard applies only to the body_md branch; file-read branch reads body_path verbatim, allowing arbitrary-file read via ../ escape.
  - **fixed.** Hoisted the workspace-resolve+relative_to guard above the if/else so both authoring branches refuse traversal. Test test_file_read_path_traversal_refused covers it.
## Iteration 3

- **critical**: TOCTOU window between resolve() guard and read_bytes/write_bytes; a swapped symlink could escape the workspace.
  - **adjudicated.** Threat model is single-operator with shell access. T-04 hash check refuses post-swap reads; write-side requires operator-level write to swap. No additional capability beyond what the operator already has.
- **medium**: No regression test for symlinks pointing outside the workspace; guard catches them but is unexercised.
  - **adjudicated.** Symlink semantics across platforms (Windows perms, macOS APFS) make a portable symlink fixture more friction than its coverage value warrants under this threat model. Logged for OI follow-up if symlink-aware fixture infra ever lands.
