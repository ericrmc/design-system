# Open Issues

Issues identified during sessions that remain unresolved. Each entry records the issue, the session that surfaced it, and its current status.

---

### OI-001: Naming the methodology
**Surfaced:** Session 001
**Status:** Open
The methodology does not yet have a name. A name should emerge when the methodology has developed enough identity to be named meaningfully. See deliberation in `provenance/001-genesis/01-deliberation.md`, Question 6.

### OI-002: Threshold for substantive revision vs. minor correction
**Surfaced:** Session 001
**Status:** Open (data points added Sessions 002, 003)
Decision D-004 established that substantive revisions trigger file-level version preservation while minor corrections do not. No formal criteria for distinguishing the two have been defined. Session 002 produced a data point: D-014 treated adding `tools/` to the workspace-structure spec as a minor correction, reasoning that changes *anticipated by* the specification's own language are minor updates, while changes that *alter the meaning or structure* of the specification are substantive. Session 003 added a second data point: D-020 treated adding a pointer to `multi-agent-deliberation.md` in methodology-kernel.md as a minor correction because the kernel's Convene/Deliberate language was already mechanism-neutral and explicitly anticipates elaboration via child specifications. The emerging two-point heuristic: if a change only makes explicit something the specification's existing language already admits, it is minor. Future sessions should continue collecting data points.

### OI-004: Incorporating genuinely independent perspectives
**Surfaced:** Session 001
**Status:** Open (scope narrowed in Session 003)
When a single AI agent plays all perspectives, disagreement is simulated, not genuinely independent. Session 003 built `specifications/multi-agent-deliberation.md` and demonstrated parallel context-isolated Claude subagents as the first real mechanism, which closes the single-context simulation gap. What remains open — and is the issue's narrowed scope — is perspective independence beyond a single model family: different models, human participants, or both. The pattern's specification states plainly that the current mechanism is "a meaningful floor, not a ceiling." Future sessions should address cross-model participation (the lightest path) or human-in-the-loop deliberation (higher value, higher infrastructure cost). OI-004 should not be closed on the basis of Claude-only parallelism.

### OI-005: Sub-activities and work-type variants
**Surfaced:** Session 001
**Status:** Open
The nine core activities may need sub-activities, and different types of work (research, design decisions, validation, implementation) may warrant different subsets or emphases. To be explored as the methodology is applied to different kinds of work.

### OI-006: Cross-references between specifications
**Surfaced:** Session 001
**Status:** Open
The current specification format does not mandate cross-references between related specifications or links to the provenance that produced them. As the number of specifications grows, navigability may require explicit linking. Deferred until the need arises.

### OI-007: Scaling the open issues format
**Surfaced:** Session 001
**Status:** Open
Open issues are currently a single file. If the number of issues grows significantly, this format may become unwieldy. Consider migrating to a directory of individual issue files, or developing a categorization system, when the need arises.

### OI-008: Persisting validation reports
**Surfaced:** Session 002
**Status:** Open
Should the output of `tools/validate.sh` be saved as part of session provenance? Currently the output is ephemeral — run during Read, consumed, not saved. If validation history proves useful for tracking methodology health over time, a future session should design a persistence mechanism. See D-010 for context.

### OI-009: Monitor for drift-to-ritual in multi-agent deliberation
**Surfaced:** Session 003
**Status:** Open
The Session 003 Skeptic argued that multi-agent deliberation will drift to ritual within five sessions — applied to routine decisions because the machinery exists and using it feels rigorous, while the presence of multi-agent becomes a quality proxy rather than a tool of actual inquiry. The specification's selective-use triggers (D-016) and the required single-agent annotation for triggered-but-skipped decisions are both countermeasures. Future sessions should track (a) how often each trigger fires vs. how often single-agent annotation is used, (b) whether synthesis disagreements are genuine or formulaic, (c) whether any session applies multi-agent to clearly routine decisions. If drift is observed, D-016 should be tightened or the kernel substantively revised.

### OI-010: Cross-model or human participation for independence beyond Claude
**Surfaced:** Session 003
**Status:** Open
Distinct from OI-004's narrowed scope, this tracks the concrete infrastructure question: what is the lightest path to incorporating a non-Claude participant (e.g., via API) or a human reviewer into a multi-agent deliberation? Candidate approaches to consider in a future session: a CLI wrapper that calls a second model with the same brief; a provenance-aware review step where a human reads raw outputs before synthesis; an asynchronous pattern that issues a brief and collects a response across sessions. This issue is about mechanism; OI-004 is about the independence gap it would close.

---

## Resolved Issues

| Issue | Resolved | Session | Notes |
|-------|----------|---------|-------|
| OI-003: Automated validation | 2026-04-17 | 002 | Built two-tier validation: `tools/validate.sh` + guided questions. See `specifications/validation-approach.md` and decisions D-010 through D-014. |
