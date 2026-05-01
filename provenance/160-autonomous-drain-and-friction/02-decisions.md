---
session: 160
title: autonomous-drain-and-friction — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Adopt autonomous-drain mode and friction-reduction CLI: ship bin/selvedge drain, drain-status, submit-help; §1.5 SELVEDGE_AUTONOMOUS branch.

**Kind:** substantive.  **Outcome:** adopt process_rule `autonomous-drain-mode-and-friction-cli`.

**Why.**

- (operator_directive) Operator at S159 close directs more agent autonomy over engine self-improvement; current per-session ratification is too deep for operator to follow at queue depth ~20+ items.
- (operator_directive) Operator names two friction modes the CLI must address: agents hit Python exceptions on wrong field names; agents query substrate excessively to discover schema.
- (operator_directive) Operator scope: build the script (bin/selvedge drain) and the env var (SELVEDGE_AUTONOMOUS=1) for local-only autonomous session driving; no /schedule remote agents.
- (engine_feedback) EF-S159-2 friction surface this session: synthesis_point labels not citable in supports; exemplifies the wrong-field-causes-Python-exception pattern submit-help addresses. [EF-S159-2]
- (prior_decision) DV-S159-1 v2 promotion-trigger pattern (operator-policed v1 with calibration-EF graduation gate) is the same pattern autonomous-mode applies: ship the v1 driver and graduate when usage shows what to harden. [DV-S159-1]

**Effects.**

- creates bin/selvedge drain shell driver invoking claude -p per iteration with halt-on-conditions.
- creates bin/selvedge drain-status JSON CLI exposing queue/halt/session state for the driver.
- creates bin/selvedge submit-help <kind> CLI printing payload shape lengths enums per submit kind.
- modifies prompts/development.md add §1.5 SELVEDGE_AUTONOMOUS=1 branch with halt-on-conditions enumerated.
- modifies .claude/settings.local.json permissions allowlist for headless drain claude -p invocations.
- supersedes prompt-development v15 to v16 carrying §1.5 autonomous-mode branch.
- supersedes engine-manifest v46 to v47 enumerating new CLI verbs and the drain script in the active file set.
- bumps_engine engine-v46 to engine-v47 because new CLI verbs land in the active engine.

**Rejected alternatives.**

- **R-1.1.** Cross-family deliberation on autonomous-mode shape before shipping (per methodology §When-to-convene methodology-changing trigger).
  - (operator_override) Operator explicitly directed scope (script and env var); methodology §Skipping-triggered admits operator-directed skip with reason recorded; cost of cross-family unwarranted for prompt-language addition with bounded surface area.
- **R-1.2.** Ship submit-help via dynamic AST introspection of handler source rather than a static schema registry.
  - (inferior_tradeoff) AST parsing is brittle to handler refactors and obscures intent; static registry is authoritative single-source-of-truth and easier to keep current.
- **R-1.3.** Make autonomous-mode a separate CLI verb (e.g. bin/selvedge run-autonomous) rather than env-var-keyed branch in PROMPT.md dispatch.
  - (inferior_tradeoff) Operator scope says env var; env var keeps PROMPT.md as the single dispatch surface and keeps the claude -p invocation simple (one prompt input only).
- **R-1.4.** Defer engine-manifest bump (treat new CLI verbs as tooling not engine-definition).
  - (inferior_tradeoff) engine-manifest §3 file set enumerates bin/selvedge and selvedge/ Python; new CLI verbs land in the active engine and the bump rule applies (engine-manifest §Versioning).
