---
session: 186
title: substrate-loss-defense-l2b-and-l4b — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high**: Three error paths in cmd_clone_substrate lack test coverage: src_conn.connect() failure, backup() failure, and sidecar unlink() exceptions (DV-S081-1 L2b subagent tempdir-clone).
  - **fixed.** Added test_clone_refuses_when_dst_is_a_directory + test_clone_refuses_corrupt_source covering the dst=dir backup() failure and src-corrupt branches plus cleanup-on-failure invariant. Sidecar-unlink OSError branch is platform-permissions-dependent and remains uncovered by design (warning-emit only, non-fatal). 8/8 clone tests now pass.
- **medium**: clone-substrate does not explicitly document that clones landing in /tmp are subject to OS-level temp reclamation and may be silently deleted before the orchestrator calls rm -f. If subagent execution is slow or if cleanup is forgotten, clones may leak or vanish unpredictably.
  - **fixed.** Updated clone_cmd.py docstring with explicit Cleanup posture paragraph naming macOS /var/folders + Linux tmpfs reclamation behaviour and recommending --to <persistent-path> for durability. Stderr output expanded to call out OS reclamation in the post-clone hint.

## Terminal passes

- **iteration 1** — findings @ `eab8acc8cd68`
  - Iteration 1 surfaced 2 findings: HIGH error-path coverage gap plus MEDIUM cleanup-doc; both addressed before iteration 2.
- **iteration 2** — clean @ `eab8acc8cd68`
  - Iteration 2 confirmed both finding-26 + finding-27 fixes are real and sufficient; 8/8 clone tests pass; no regressions.
