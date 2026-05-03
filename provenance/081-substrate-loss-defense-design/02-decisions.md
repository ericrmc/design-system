---
session: 081
title: substrate-loss-defense-design — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Adopt substrate-loss-defense-v1 design: L1a init guard + L2b subagent clone + L3 boundary snapshots with restore CLI + L4B extractor + L5 close-export expansion + engine-v51 marker

**Kind:** substantive.  **Outcome:** adopt process_rule `DV-S081-1`.

**Why.**

- (operator_directive) Operator opened OI-S180-1 HIGH after subagent init --force wiped substrate at S180 and explicitly convened cross-family deliberation rather than naming the answer. [S080]
- (operator_directive) Operator framing data-is-non-critical inverts cost/benefit toward defense-not-reconstruction; operator added L5 mid-deliberation as sixth dimension. [S081]
- (deliberation) P-1 layered-defense architect position: ship L1+L2+L3+L4B together; defense-in-depth required when single-layer proven bypassable at S180. [P-1-P-1]
- (deliberation) P-2 cross-family position: write-capability containment broader than subagent-runs-init; restore CLI mandatory or backups are decorative; L5 mandatory artifacts enumerated. [P-1-P-2]
- (deliberation) P-3 minimalist position preserved as M-1: defenses-in-depth themselves rot via override-routinization; warning carried forward. [P-1-P-3]
- (deliberation) P-4 operator-ergonomics position: defenses must ship with named documented escape hatches; L2a-alone breaks reviewer dry-run; phased-rollout option preserved as M-3. [P-1-P-4]
- (deliberation) Synthesis adopted package combines load-bearing C-1 (L1a) + C-2 (L4B) + C-3 (snapshot via SQLite backup) + C-4 (restore CLI) + C-7 (no every-tx snapshot) + C-8 (L5 export) + C-9 (write-capability framing). [A-S081]
- (engine_feedback) S180 reviewer-subagent ran bin/selvedge init --force during migration verification, wiping every session/decision/spec-version/issue/EF/deliberation row; OI-S180-1 documents the incident and remediation set. [C-S080]

**Effects.**

- opens_issue OI-S081-1 — L1a init --force live-substrate refusal implementation in selvedge/init_cmd.py
- opens_issue OI-S081-2 — L2b subagent tempdir-clone isolation via SQLite backup API
- opens_issue OI-S081-3 — L3 snapshot machinery at session-open + close + migrate + init triggers
- opens_issue OI-S081-4 — bin/selvedge restore CLI with --from --to --verify and exit-2 refusal
- opens_issue OI-S081-5 — L4B one-shot legacy-substrate extractor
- opens_issue OI-S081-6 — L5 close-time export expansion across 8 enumerated artifacts
- opens_issue OI-S081-7 — engine-v51 marker migration coupling L1a + snapshot_catalog + L5 export-manifest
- opens_issue OI-S081-8 — prompts/development.md §4 subagent-discipline boilerplate amendment

**Rejected alternatives.**

- **R-1.1.** Ship P-1 maximal package: snapshot on every write_tx + L1a + L1b + L2a + L4B as one engine-v51 arc with conservative-on defaults across all triggers.
  - (inferior_tradeoff) P-2 + P-4 cross-family C-7 convergence: every-tx snapshot is latency dominator and operator-fatigue trainer; bounded triggers strictly dominate.
  - (inferior_tradeoff) P-4 risk: snapshot-on-every-write trains operators to disable defenses wholesale; the marginal recovery point is not worth the steady cost.
- **R-1.2.** Ship P-3 minimalist package: L1a guard + PROMPT.md clause only; no L2 code, no L3 snapshots, no L4 extractor, no L5 export expansion, no engine-version bump.
  - (inferior_tradeoff) C-9 cross-perspective convergence: threat model is write-capability-containment broadly, not specifically subagent-runs-init; prompt-only isolation is ignorable by future subagents.
  - (operator_override) Operator added L5 mid-deliberation explicitly broadening close-time export; minimalist package forecloses that direction by construction.
  - (inferior_tradeoff) L1a alone has no fallback if a different destructive op (not init) wipes substrate; P-3 itself names this as accepted-cost which the synthesis declines to accept.
- **R-1.3.** Ship L2a (read-only env var) as the only subagent isolation primitive; no tempdir clone.
  - (inferior_tradeoff) P-4 named: L2a silently breaks reviewer subagents that legitimately validate migrations via dry-run BEGIN/ROLLBACK, which is exactly the audit pattern S177-S180 relied on.
  - (inferior_tradeoff) P-2 named: env vars are memory not isolation boundary; they leak into parent shell and get forgotten.
- **R-1.4.** Ship L4A skip-reconstruction-entirely; treat S180 as new genesis with provenance markdown as historical evidence only.
  - (inferior_tradeoff) P-1 + P-4 named: loses DV alias index and open-issue continuity that downstream sessions cite by ID; L4B preserves citations cheaply at one-shot script cost.
- **R-1.5.** Ship L4C faithful multi-session replay of S001-S179 with migration-step-advance logic against synthetic intermediate-engine substrates.
  - (inferior_tradeoff) P-1 + P-2 + P-4 converge: multi-session migration-step-advance is its own substrate-risk surface and creates false confidence; data-non-critical framing makes the cost unjustified.
- **R-1.6.** Ship as phased-rollout per P-4 M-3: L1a alone in S081 (this session), observe one session of friction, layer L2+L3+L4B+L5 in S082+ to bound blast radius.
  - (operator_override) Operator added L5 mid-deliberation indicating urgency; deferring to S082+ would defer the export expansion that operator named as an active concern.
  - (inferior_tradeoff) This session is deliberation-only; the implementation IS phased into S082+ via OI-S081-1..8 cluster, so the M-3 risk-management goal is met by the FR handoff structure not by partial design adoption.
