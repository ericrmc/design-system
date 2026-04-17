# Open Issues

Issues identified during sessions that remain unresolved. Each entry records the issue, the session that surfaced it, and its current status.

---

### OI-001: Naming the methodology
**Surfaced:** Session 001
**Status:** Open
The methodology does not yet have a name. A name should emerge when the methodology has developed enough identity to be named meaningfully. See deliberation in `provenance/001-genesis/01-deliberation.md`, Question 6.

### OI-002: Threshold for substantive revision vs. minor correction
**Surfaced:** Session 001
**Status:** Open (data points added Sessions 002, 003, 004)
Decision D-004 established that substantive revisions trigger file-level version preservation while minor corrections do not. No formal criteria for distinguishing the two have been defined. Session 002 (D-014): adding `tools/` to workspace-structure was minor — change *anticipated by* the specification's own language. Session 003 (D-020): adding a pointer to `multi-agent-deliberation.md` in methodology-kernel.md was minor — kernel's Convene/Deliberate language was already mechanism-neutral. Session 004 (D-026): revising `multi-agent-deliberation.md` v1 → v2 was **substantive** — adds new normative content (new trigger rules, new required fields, new mechanism shapes) not anticipated structurally in v1. The three-point heuristic: **minor** if the change makes explicit what the specification's existing language already contains or explicitly anticipates as a category of extension; **substantive** if the change adds new normative content (rules, required fields, triggers, required artefacts) beyond what the existing language contains.

### OI-004: Incorporating genuinely independent perspectives
**Surfaced:** Session 001
**Status:** Open (unchanged scope after Session 004)
When a single AI agent plays all perspectives, disagreement is simulated. Session 003 built parallel context-isolated Claude subagents as the first real mechanism, closing the single-context simulation gap but leaving the Claude-monoculture gap. Session 004 specified a non-Claude participation mechanism (in `multi-agent-deliberation.md` v2, see D-021/D-023/D-024) but explicitly chose **not** to claim any narrowing of OI-004 (D-025), because no non-Claude participant was in Session 004's deliberation. Narrowing requires operational use. Closure criteria are now specified in the v2 specification's Closure Criteria section: (1) participant independence; (2) sustained practice across ≥3 required-trigger deliberations; (3) recorded impact on outcomes; (4) articulated definition of "substantively different training provenance." "Closable" and "closed" remain distinct states; closure requires explicit deliberation by a future session.

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
Open issues are currently a single file. With Session 004 the count is 8 open issues and the file remains readable, but this format may become unwieldy. Consider migrating to a directory of individual issue files, or developing a categorization system, when the need arises.

### OI-008: Persisting validation reports
**Surfaced:** Session 002
**Status:** Open
Should the output of `tools/validate.sh` be saved as part of session provenance? Currently the output is ephemeral — run during Read, consumed, not saved. If validation history proves useful for tracking methodology health over time, a future session should design a persistence mechanism. See D-010 for context.

### OI-009: Monitor for drift-to-ritual in multi-agent deliberation
**Surfaced:** Session 003
**Status:** Open (Session 004 audit: no drift observed)
Session 003's Skeptic argued that multi-agent deliberation will drift to ritual within five sessions. Session 004's audit of Session 003's pattern application (in `provenance/004-participation-mechanisms/00-assessment.md`) found the Skeptic's demands materially shaped the specification, dissent was preserved, and the pattern was applied to maximally load-bearing work — no drift signal. Session 004 itself applied multi-agent to OI-010, which meets multiple D-016 triggers and is the most load-bearing candidate for the session — also no drift. Continue monitoring. Drift would appear as: multi-agent applied to typos, renames, reordering, or decisions with no genuinely articulable alternative positions.

### OI-010: Cross-model or human participation mechanism
**Surfaced:** Session 003
**Status:** Open, narrowed. Mechanism specified; awaiting first operational use.
Session 004 produced a concrete specification (in `multi-agent-deliberation.md` v2): two participation shapes (perspective and reviewer), a three-layer recording schema, explicit trigger rules, and closure criteria. OI-010 is not closed because the mechanism has not yet been used. Closure: the first session that successfully uses the mechanism on a required-trigger deliberation and records it per the new schema may close this issue (and begin — but not complete — the narrowing of OI-004 per D-025).

### OI-011: Intra-family model mixing as a deliberation-quality lever
**Surfaced:** Session 004
**Status:** Open
Per D-022, mixing Anthropic models (Opus + Sonnet + Haiku) does **not** constitute cross-model participation for OI-004. But all three Session 004 perspectives noted that intra-family mixing has residual utility — capability stratification (Haiku surfaces what a weak reasoner catches; Opus explores longer tails), cost-scaled deliberation, and validation-band variance. This is a separate concern that should not be conflated with OI-004 progress in future sessions. A future session may deliberate whether to specify guidance for *when* intra-family mixing is worth doing and *how* to record it honestly (`participants_family: mixed-anthropic`) without inadvertently claiming OI-004 movement.

---

## Resolved Issues

| Issue | Resolved | Session | Notes |
|-------|----------|---------|-------|
| OI-003: Automated validation | 2026-04-17 | 002 | Built two-tier validation: `tools/validate.sh` + guided questions. See `specifications/validation-approach.md` and decisions D-010 through D-014. |
