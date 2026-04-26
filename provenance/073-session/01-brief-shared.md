---
session: 073
title: Shared brief — S073 phase-2 MAD on γ phase-3 (z6) digest implementation arc per S071 D-263 (ε) hybrid + VD-003 + S072 D-272 pre-ratification
date: 2026-04-26
status: complete
---

# Shared brief — Session 073 phase-2 MAD

## §1 Methodology context

You are participating in the **Selvedge engine's** self-development application as a perspective in a **multi-agent deliberation (MAD)** at Session 073. The engine's discipline (per `specifications/multi-agent-deliberation.md` v4 §Stance Briefs + §Mechanism + §Synthesis): perspectives form positions independently from the same brief, without seeing each other's outputs; a synthesis step then produces a single record preserving convergence, divergence, and minorities.

The current engine version is **engine-v13** (ratified S071 per D-265). Active engine-definition specs include `methodology-kernel.md` v6, `validation-approach.md` v7, `multi-agent-deliberation.md` v4, `read-contract.md` v6, `records-contract.md` v1, `retrieval-contract.md` v1, `workspace-structure.md` v9, `engine-manifest.md`, `prompts/development.md` (engine-v13 substantive amendment per S071 D-264 promoting `forward_references('S<NNN>')` to required step at session-open + structured-declaration requirement + substrate-availability-as-required-precondition), `tools/validate.sh` (with check 29 WARN-only β-phase substrate-use evidence-probe).

**Path-AS Shape-1 multi-session phase-3 arc** is in motion since S072: (a) S072 = phase-3 design-space session producing `provenance/072-session/design-space.md` (~7,561 words; this brief's primary extension content); (b) **S073 = phase-2 MAD execution (this session)** on direction selection within (γ) scope; (c) S074+ = phase-3 implementation per direction adopted.

The S071 phase-2 MAD adopted **(ε) hybrid bounded-then-extended** composition per cross-family weighted convergence (3-of-4 across families: P2 Claude + P3+P4 codex on (ε); P1 Claude dissent on full (γ)-immediate preserved as §10.4-M26 first-class minority). The β-phase Direction 1 (a)+(b)+(c)+(d) was adopted at S071 close codifying substrate-use-required at session-open in spec-side discipline. The γ-phase deferred elements are:

1. **EF-068-substrate-load-bearing Direction 1 (e)**: implement `tools/validate.sh` check 26 substrate-aware branch.
2. **EF-068-substrate-load-bearing Direction 2 (D2.1 vs D2.2)**: extend EF-059 (z6) digest scope to orchestrator-side read-discipline telemetry; make digest Tier 2.5 reviewer input always-available-always-read (D2.1) vs available-at-best-effort (D2.2).
3. **EF-059 full (z6) harness-telemetry digest implementation**: capture mechanism + digest schema + reviewer-prompt-template extension + `validation-approach.md` v7 → v8 substantive revision.
4. **EF-067 Direction B subsumption into EF-059 (z6) digest scope**: deprecate `duration_minutes` + `reviewer_cost` self-report fields in favor of harness-measured fields.
5. **Measurement-authority separation reframe** (substantively adopted at S071 D-263 §5.1; preserved at §10.4-M28): digest records MUST distinguish `producer_kind: harness-measured | post-hoc-reconstructed | agent-declared` + `authority_level`.

Per VD-003 lifecycle row (status: open; review_by_session: S076): phase-3 activation gating conditions (a) capture mechanism selection finalised + (b) observation window data on β-phase substrate-use distinguishing durable behavior change from design-space-salience compliance + (c) digest schema specification with producer_kind/authority_level finalised.

## §2 Problem statement

**Select the (γ) phase-3 implementation direction**: which cross-product candidate (γ-1) maximal-scope vs (γ-2) (ε)-hybrid-default-scope vs (γ-3) minimum-viable-γ-scope vs (γ-4) capture-mechanism-first-staged-rollout vs (γ-5) hybrid-CMD-4-with-staged-EVD-3 should be adopted at S073 phase-2 MAD synthesis?

The decision discharges VD-003 gating condition (a) capture mechanism selection + (c) digest schema specification per measurement-authority separation. Gating condition (b) observation window data is structurally downstream and discharged at S074-S076 retention window per VD-003 review at S076.

The decision also addresses:
- **Q1 capture mechanism preferred end-state** (CM1 Claude Code hooks vs CM2 external wrapper vs CM3 post-hoc transcript-reconstruction).
- **Q2 schema scope** (SCD-1 original-EF-059-only vs SCD-2 substrate_calls-extension vs SCD-3 full-extended-schema vs SCD-4 records-substrate-promotion).
- **Q3 reviewer availability discipline** (RAD-1 D2.1-always-available-always-read vs RAD-2 D2.2-available-at-best-effort vs RAD-3 bridged transition).
- **Q4 reviewer self-report disposition** (REVD-1 full-subsumption-now vs REVD-2 partial-deprecation vs REVD-3 full-subsumption-with-retrospective-re-baseline).
- **Q5 check 26 substrate-aware branch** (CHKD-1 substrate-required vs CHKD-2 substrate-preferred-with-fallback vs CHKD-3 defer-to-post-γ).
- **Q6 engine-v cadence** (EVD-1 single-substantive-bump vs EVD-2 two-step-bump vs EVD-3 multi-step-bump).
- **Q7 reviewer-prompt-template extension scope** (minimum-viable extension vs full extension; per (z7) lock-in-after-n=2).
- **Q8 bundle-vs-defer EF-068-read-write-rebalance** per S069 D-255 operator-discretionary reopen warrant — should the four-record bundle be opened at S073 phase-2 MAD execution per aggregate-budget pressure, or preserved as separate-scope at S074++ per intake-deferral discipline?
- **Q9 implementation-locus session-shape** (Path L single-orchestrator vs Path-AS at S074+).
- **Q10 cross-spec interaction depth** (minor amendments vs substantive bump vs new spec class).

**Aggregate-budget pressure at S073**: aggregate 91,571 / 90K soft (1,571 over). Per `read-contract.md` v6 §2b: S073 MUST include aggregate-reducing action. Close-rotation S067 OUT discharges mechanically; structural restructure scope (EF-068-read-write-rebalance four-record-bundle) preserved as standing operator-discretionary reopen warrant.

## §3 Design-space brief-extension (condensed from S072 `design-space.md` §3-§7)

The S072 phase-3 design-space surveys the choice surface jointly. Read this section as your primary input.

### §3a Workspace state at S073 (β-phase substrate-use observation)

| Session | Substrate calls at session-open | β-phase compliance | Adjudication |
|---------|----------------------------------|---------------------|---------------|
| S071 | non-zero (forward_references + 3 resolve_id) | adoption session | awareness-driven by definition |
| S072 | non-zero (forward_references('S072') = 117 hits) | first observation point post-codification | n=1 in observation window |
| S073 | non-zero (forward_references('S073') = 157 hits) | n=2 observation point | insufficient for adjudication |

n=4-5 across S074-S076 will provide first triangulation between durable behavior change and design-space-salience compliance (Hawthorne effect).

### §3b Capture mechanism trade-offs (CM1/CM2/CM3; CM4 explicitly rejected per S071 D-263)

| Mechanism | Authority | Portability | Implementation cost | Cross-workspace deployment |
|-----------|-----------|-------------|----------------------|------------------------------|
| **CM1 Claude Code hooks** (PreToolUse + PostToolUse emit `provenance/<NNN-session>/harness-telemetry-digest.yaml`) | primary (harness-emitted) | medium (Claude Code only) | low (hook config + emit-to-yaml) | per-workspace `.claude/settings.json` setup |
| **CM2 External wrapper** (shell wraps Claude Code session; intercepts via stdio multiplex or process-tree introspection) | primary (external-process-emitted) | high (cross-harness-tool) | medium (wrapper script + protocol) | per-workspace wrapper invocation discipline |
| **CM3 Post-hoc transcript-reconstruction** (extension to `tools/build_retrieval_index.py` parses Claude Code transcript) | secondary (post-hoc-reconstructed) | highest (offline reconstruction) | medium-high (transcript parsing + reconstruction script) | per-workspace tool-script setup |

S071 D-263 framing: **CM1 preferred** / CM2 acceptable / CM3 acceptable as bridge.

### §3c Cross-product implementation candidates (γ-1) through (γ-5)

| Candidate | Engine-v bumps | Spec-files touched | Tools touched | Resolution sessions | producer_kind coverage | Risk profile |
|-----------|----------------|--------------------|--------------|----------------------|---------------------------|--------------|
| **(γ-1) Maximal scope** (CMD-4 CM1+CM3 + SCD-3 + RAD-3 + REVD-3 + CHKD-1 + EVD-1) | 1 substantive | validation-approach + read-contract + retrieval-contract | tools/validate.sh + new harness-integration | 3-4 | harness-measured + post-hoc + agent-declared | medium-high |
| **(γ-2) Default per (ε) hybrid** (CMD-1 + SCD-3 + RAD-2 + REVD-2 + CHKD-2 + EVD-2) | 1 minor + 1 substantive | validation-approach + minor read-contract | tools/validate.sh + new harness-integration | 2-3 | harness-measured + agent-declared | medium |
| **(γ-3) Minimum-viable γ scope** (CMD-3 + SCD-2 + RAD-2 + REVD-2 + CHKD-3 + EVD-2-smaller) | 1 minor + 1 substantive (smaller) | validation-approach (smaller) | tools/validate.sh (minor) | 2 | post-hoc-reconstructed + agent-declared | low-medium |
| **(γ-4) Capture-mechanism-first staged** (CMD-1 phase-3.1 + SCD-3 phase-3.2 + RAD-2 + REVD-2) | 1 minor + 1 minor + 1 substantive | validation-approach (staged) | tools/validate.sh (staged) + new harness-integration | 3-4 | harness-measured + agent-declared | medium |
| **(γ-5) Hybrid CMD-4 staged** (CMD-4 + SCD-2→SCD-3 staged + RAD-3 + REVD-2→REVD-3 + CHKD-2) | 1 minor + 1 minor + 1 substantive | validation-approach (staged) + read-contract | tools/validate.sh (staged) + new harness-integration | 4 | harness-measured + post-hoc + agent-declared | medium |

### §3d Schema candidate (starting-point; phase-2 MAD finalises)

```yaml
session: <NNN>
captured_at: <ISO-8601>
producer_kind: harness-measured | post-hoc-reconstructed | agent-declared  # NEW per §10.4-M28
authority_level: primary | secondary | tertiary  # NEW per §10.4-M28
tool_calls:
  - tool: <name>
    invocations: <integer>
    failures: <integer>
    failure_modes: [<reason1>, <reason2>, ...]
    routed_around_via: [<alternative-tool>, ...]
read_invocations:
  - path: <workspace-relative-path>
    count: <integer>
    cached_after_first: true | false
unavailable_tools:
  - tool: <name>
    workaround: <description>
anomalous_patterns:
  - pattern: <description>
    instances: <count>
substrate_calls:
  - tool: <mcp__selvedge-retrieval__forward_references | resolve_id | search>
    invocations: <integer>
    arguments_summary: <string>
    invoked_at_session_open: true | false
files_read_at_session_open:
  - path: <workspace-relative-path>
    bytes_read: <integer>
    full_or_partial: full | partial
decision_claims_with_evidence_pointers:
  - decision_id: <D-NNN>
    evidence_pointer: <spec-section | ledger-row-id | minority-warrant | archive-pack>
reviewer_invocation_wall_clock_seconds: <integer>
reviewer_invocation_token_count: <integer>
```

Schema scope sub-questions: SCD-1 (original-EF-059-only) vs SCD-2 (substrate_calls extension only) vs SCD-3 (full extended schema with EF-068 D2 + EF-067 Direction B subsumption) vs SCD-4 (SCD-3 + records-substrate phase-2 promotion; deferred per S062 §10.4-M18 maturity gate).

### §3e Reviewer availability scope

- **RAD-1 D2.1 always-available-always-read**: digest is hard precondition for Layer 2 (γ) reviewer invocation. If digest unavailable, reviewer audit deferred (or explicit honest-limit recording).
- **RAD-2 D2.2 available-at-best-effort**: digest is reviewer input when available; absent-digest sessions fall back to current Layer 2 audit shape.
- **RAD-3 D2.1 with bridged-D2.2 transition window**: D2.1 target end-state; D2.2 deployment-window default during (γ) rollout; D2.1 hard-precondition activates at named gating session.

### §3f Reviewer self-report disposition (post-S071 D-264)

- **REVD-1 Direction B full subsumption now**: deprecate `duration_minutes` + `reviewer_cost` self-report; replace with harness-measured. §10.4-M25 P1 audit-cost-budget threshold arithmetic re-activates against harness-measured.
- **REVD-2 Direction B partial-deprecation**: preserve self-report fields with `producer_kind: agent-declared` annotation; harness-measured fields added as parallel; cross-session pattern observation continues against harness-measured trajectory.
- **REVD-3 Direction B + retrospective re-baseline**: REVD-1 + post-(γ) harness-measured value as new baseline; current S063 self-report baseline retired.

### §3g Preserved minorities relevant to S073 deliberation

- **§10.4-M16 P2 minimum-viable-response precedent** (S062) — informs (γ-3) candidate.
- **§10.4-M22 P1 two-session-arc minority** (S064) — honored by multi-session arc (S072+S073+S074+).
- **§10.4-M23 P3 substrate-led reviewer-judged frame** (S064; substantively adopted at v7).
- **§10.4-M25 P1 audit-cost-budget reopen-warrant** (S064; threshold arithmetic suspended at S071 D-264 pending harness-measurement).
- **§10.4-M26 P1 full-(γ)-immediate position** (S071) — preserved at S071; tracked at S072+ observation window.
- **§10.4-M27 P2 (γ)-deferral-criteria position** (S071; partly absorbed by (ε) hybrid).
- **§10.4-M28 P3 measurement-authority-separation position** (S071; substantively adopted; load-bearing for §3d schema).
- **§10.4-M29 P4 bundling-by-laundering audit position** (S071; substantively adopted; per-direction disposition discipline).

## §4 Response format

Return your response as a single markdown file with the following structure:

```markdown
---
session: 073
title: <Perspective name> — Session 073 phase-2 MAD response
date: 2026-04-26
status: complete
perspective: <perspective name>
committed_at: <ISO-8601>
---

# <Perspective name>

## Frame critique
<2-4 paragraphs: any framing concerns about the brief itself; missing axes; reframes you would push back on or surface (z-prefix per S058+S062+S064+S071 reframe-architecture pattern). Optional but encouraged for P3 + P4.>

## Q1 — capture mechanism preferred end-state
<position + reasoning>

## Q2 — schema scope
<position + reasoning>

## Q3 — reviewer availability discipline
<position + reasoning>

## Q4 — reviewer self-report disposition
<position + reasoning>

## Q5 — check 26 substrate-aware branch
<position + reasoning>

## Q6 — engine-v cadence
<position + reasoning>

## Q7 — reviewer-prompt-template extension scope
<position + reasoning>

## Q8 — bundle-vs-defer EF-068-read-write-rebalance
<position + reasoning>

## Q9 — implementation-locus session-shape
<position + reasoning>

## Q10 — cross-spec interaction depth
<position + reasoning>

## Cross-product candidate position
<which of (γ-1) through (γ-5) you advocate, OR (γ-6)+ if you surface a new candidate; reasoning>

## Honest limits
<3-7 specific limitations of your reasoning here: areas of uncertainty, dependencies on other perspectives' inputs, claims you would want to verify with substrate or harness data>

## Dissent-preservation
<if synthesis adopts a direction other than yours, what minority warrant should preserve your position? activation triggers + reopen warrants>
```

Target length: 1,500-3,000 words total. Be concrete; cite design-space §X or §10.4-MN where load-bearing.

## §5 Constraint on external imports

Reason primarily from this brief. If you draw on pretraining knowledge (e.g., specific Claude Code hook API surfaces; specific MCP protocol details; engineering practice from outside this workspace), flag it explicitly as **[external import]** with the justification (e.g., "the PreToolUse hook surface I'm citing is from Claude Code documentation external to this brief; I include it because the brief's §3b mentions hooks but does not enumerate the surface"). Do not commit external ideas as if they were workspace-internal reasoning.

The brief's §3 brief-extension condenses S072 design-space.md §3-§7 (the canonical full source). If you find the condensation insufficient for a particular question, flag it as honest-limit; do not attempt to read workspace files during your independent phase.

## §6 Decision-procedure pre-ratification

Per S072 D-272 + design-space §9: cross-family weighted convergence per S058 + S062 + S064 + S071 precedent. Threshold: 3-of-4 across families adoption signal triggers same-session-bounded direction-adoption per S071 D-263 (ε) hybrid β-phase precedent OR phase-3 adoption deferred to S074+ per S062 D-220 multi-session phase-3 precedent depending on direction adopted; below threshold preserves design-space + names follow-on phase-2 MAD or phase-3 shape.

The synthesis at S073 close will produce `01-deliberation.md` (cross-family weighted convergence + dissent preservation + minority warrants) + `02-decisions.md` (substantive decisions + minority preservation per §10.4-M30+ candidates if surfaced) + `03-close.md` + Tier 2.5 (γ) reviewer audit at close per Layer 2 trigger (b) substantive-arc-class + likely (a) engine-definition-touching (Google Gemini reviewer per cross-family rule satisfaction).
