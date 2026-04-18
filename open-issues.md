# Open Issues

Issues identified during sessions that remain unresolved. Each entry records the issue, the session that surfaced it, and its current status.

---

### OI-001: Naming the methodology
**Surfaced:** Session 001
**Status:** Open
The methodology does not yet have a name. A name should emerge when the methodology has developed enough identity to be named meaningfully. See deliberation in `provenance/001-genesis/01-deliberation.md`, Question 6.

### OI-002: Threshold for substantive revision vs. minor correction
**Surfaced:** Session 001
**Status:** Open (data points added Sessions 002, 003, 004, 005)
Decision D-004 established that substantive revisions trigger file-level version preservation while minor corrections do not. No formal criteria for distinguishing the two have been defined. Session 002 (D-014): adding `tools/` to workspace-structure was minor — change *anticipated by* the specification's own language. Session 003 (D-020): adding a pointer to `multi-agent-deliberation.md` in methodology-kernel.md was minor — kernel's Convene/Deliberate language was already mechanism-neutral. Session 004 (D-026): revising `multi-agent-deliberation.md` v1 → v2 was **substantive** — adds new normative content (new trigger rules, new required fields, new mechanism shapes) not anticipated structurally in v1. Session 005 (D-034): a pair of simultaneous revisions resolved differently — revising `validation-approach.md` v1 → v2 was **substantive** (added three new Tier 1 checks with gating, severity, sequencing, and a new Tier 2 question; new normative content); annotating each Open Extensions entry in `multi-agent-deliberation.md` v2 with an activation precondition was **minor** (elaboration within the section's explicit purpose of naming future candidates; no rules, required fields, triggers, or required artefacts changed). The four-point heuristic: **minor** if the change makes explicit what the specification's existing language already contains or explicitly anticipates as a category of extension, OR annotates existing candidate entries with descriptive metadata within the section's stated purpose; **substantive** if the change adds new normative content (rules, required fields, severity decisions, gating rules, triggers, required artefacts) beyond what the existing language contains.

### OI-004: Incorporating genuinely independent perspectives
**Surfaced:** Session 001
**Status:** Open — narrowed-pending-sustained-practice after Session 005 (phrased as tally, not endorsement)
When a single AI agent plays all perspectives, disagreement is simulated. Session 003 built parallel context-isolated Claude subagents as the first real mechanism, closing the single-context simulation gap but leaving the Claude-monoculture gap. Session 004 specified a non-Claude participation mechanism (in `multi-agent-deliberation.md` v2, see D-021/D-023/D-024) but explicitly chose **not** to claim any narrowing of OI-004 (D-025), because no non-Claude participant was in Session 004's deliberation. Narrowing requires operational use.

**Session 005 tally (per D-033):** One session of non-Claude participation has occurred (Session 005, Outsider perspective via `codex exec` to OpenAI GPT-5). Per v2 closure criteria: criterion 1 (participant independence) plausibly met conditional on the Outsider manifest's `training_lineage_overlap_with_claude: independent-claim` being truthful; criteria 2 (sustained practice, ≥3 required-trigger deliberations across different sessions — current count: **1 of 3**), 3 (recorded impact — Session 005 recorded three concrete non-Claude influences on outcomes in D-033), and 4 (articulation of "substantively different training provenance") remain unmet. No closure on single-session evidence.

Closure criteria are specified in the v2 specification's Closure Criteria section: (1) participant independence; (2) sustained practice across ≥3 required-trigger deliberations; (3) recorded impact on outcomes; (4) articulated definition of "substantively different training provenance." "Closable" and "closed" remain distinct states; closure requires explicit deliberation by a future session.

### OI-005: Sub-activities and work-type variants
**Surfaced:** Session 001
**Status:** Open
The nine core activities may need sub-activities, and different types of work (research, design decisions, validation, implementation) may warrant different subsets or emphases. To be explored as the methodology is applied to different kinds of work — premature to address until the methodology has been applied to a non-self problem.

### OI-006: Cross-references between specifications
**Surfaced:** Session 001
**Status:** Open
The current specification format does not mandate cross-references between related specifications or links to the provenance that produced them. As the number of specifications grows, navigability may require explicit linking. Deferred until the need arises.

### OI-007: Scaling the open issues format
**Surfaced:** Session 001
**Status:** Open
Open issues are currently a single file. After Session 005 the count is 9 open issues (OI-010 closed) and the file remains readable, but this format may become unwieldy. Consider migrating to a directory of individual issue files, or developing a categorization system, when the need arises.

### OI-008: Persisting validation reports
**Surfaced:** Session 002
**Status:** Open
Should the output of `tools/validate.sh` be saved as part of session provenance? Currently the output is ephemeral — run during Read, consumed, not saved. If validation history proves useful for tracking methodology health over time, a future session should design a persistence mechanism. See D-010 for context.

### OI-009: Monitor for drift-to-ritual in multi-agent deliberation
**Surfaced:** Session 003
**Status:** Open (Session 004 audit: no drift; Session 005 audit: no drift; audit found a brief-priming small-finding on Session 004)
Session 003's Skeptic argued that multi-agent deliberation will drift to ritual within five sessions. Session 004's audit of Session 003's pattern application (in `provenance/004-participation-mechanisms/00-assessment.md`) found the Skeptic's demands materially shaped the specification, dissent was preserved, and the pattern was applied to maximally load-bearing work — no drift signal. Session 004 itself applied multi-agent to OI-010, which meets multiple D-016 triggers and is the most load-bearing candidate for the session — also no drift. Session 005's audit (in `provenance/005-schema-enforcement/00-assessment.md`) surfaced one small-finding: the Session 004 brief seeded the phrase "training-distribution theatre" at Q2, and all three perspectives picked it up — "total convergence" on the phrase is partially lexical echo not independent coinage. The *conclusion* (Claude-only is not cross-model) remained genuinely convergent. This is the failure-mode the v2 spec's Limitations section explicitly acknowledges ("brief-writing has no adversary"); Session 005 took care in its own brief to avoid loaded vocabulary in the design questions. Session 005's own pattern application showed no drift — the deliberation was tightly scoped to a load-bearing question meeting multiple D-023 required triggers, and the non-Claude perspective materially shaped outcomes. Continue monitoring. Drift would appear as: multi-agent applied to typos, renames, reordering, or decisions with no genuinely articulable alternative positions.

### OI-010: Cross-model or human participation mechanism
**Surfaced:** Session 003
**Status:** CLOSED in Session 005 (per D-032) — see Resolved Issues table below.
Session 004 produced a concrete specification (in `multi-agent-deliberation.md` v2): two participation shapes (perspective and reviewer), a three-layer recording schema, explicit trigger rules, and closure criteria. Session 005 performed the first operational use: Outsider perspective delivered via `codex exec` to OpenAI GPT-5, recorded per the v2 schema with full D-024 manifest. D-027 set the closure trigger to "first session that performs the first use." Session 005 is that session. OI-010 closed. Narrowing of OI-004 begins (but does not complete) per D-033 — see OI-004 above.

### OI-011: Intra-family model mixing as a deliberation-quality lever
**Surfaced:** Session 004
**Status:** Open
Per D-022, mixing Anthropic models (Opus + Sonnet + Haiku) does **not** constitute cross-model participation for OI-004. But all three Session 004 perspectives noted that intra-family mixing has residual utility — capability stratification (Haiku surfaces what a weak reasoner catches; Opus explores longer tails), cost-scaled deliberation, and validation-band variance. This is a separate concern that should not be conflated with OI-004 progress in future sessions. A future session may deliberate whether to specify guidance for *when* intra-family mixing is worth doing and *how* to record it honestly (`participants_family: mixed-anthropic`) without inadvertently claiming OI-004 movement.

---

## Resolved Issues

| Issue | Resolved | Session | Notes |
|-------|----------|---------|-------|
| OI-003: Automated validation | 2026-04-17 | 002 | Built two-tier validation: `tools/validate.sh` + guided questions. See `specifications/validation-approach.md` and decisions D-010 through D-014. |
| OI-010: Cross-model or human participation mechanism | 2026-04-18 | 005 | Session 004 specified the mechanism (D-021/D-023/D-024). Session 005 performed the first operational use: Outsider perspective (OpenAI GPT-5 via `codex exec`, Shape A per D-021) with full D-024 per-participant manifest. Per D-027, closure trigger was "first session that performs the first use." Session 005 is that session. See D-032. Narrowing of OI-004 begins (but does not complete) per D-033. |
