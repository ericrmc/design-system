---
session: 090
title: lost-ois-and-md-hook — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Engine v23 to v24: PreToolUse hook structurally restricts markdown authoring of substrate-canonical surfaces (resolves OI-085-002)

**Kind:** substantive.  **Outcome:** adopt engine_version `engine-v24`.

**Why.**

- (constraint) OI-085-002 (HIGH) carried in next_session_should for four sessions; structural restriction was deferred each time because the work needed harness configuration not substrate code.
- (constraint) Path A declares substrate canonical for spec/issue/session/prompt content but enforcement was operator-policed; S089 demonstrated the failure mode by editing a tracked spec markdown without bumping spec_version. [SPEC-engine-manifest-v23]
- (engine_feedback) Hook verified live: probe Write to specifications/__hook_verify.md refused with exit-2 message citing OI-085-002; SELVEDGE_EXPORT_CONTEXT=1 bypass logs to stderr for audit visibility.
- (engine_feedback) Engine-manifest v23 to v24 spec-version submit succeeded without tripping T-03, exercising the OI-S090-4 handler reorder fix end-to-end. [SPEC-engine-manifest-v24]

**Effects.**

- bumps_engine engine-v23 to engine-v24
- closes_issue OI-085-002
- supersedes engine-manifest v23 to v24

**Rejected alternatives.**

- **R-01.** Defer to a fifth session (carry OI-085-002 in next_session_should again)
  - (no_feedback_loop) Four consecutive deferrals demonstrates the OI is not naturally getting picked up; structural backlog accumulates while operator-policed discipline keeps slipping (S089 violation is a case in point).
- **R-02.** Substrate-trigger enforcement (SQL trigger refusing tracked-path writes)
  - (violates_gate) Triggers fire on substrate writes, not on filesystem writes; cannot intercept Edit/Write tool calls. Wrong architectural layer.
- **R-03.** Read-only filesystem chmod on tracked paths
  - (inferior_tradeoff) Breaks legitimate export materialisation; coarser than needed; conflicts with normal git workflow on restore.
