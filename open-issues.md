# Open Issues

Issues identified during sessions that remain unresolved. Each entry records the issue, the session that surfaced it, and its current status.

---

### OI-001: Naming the methodology
**Surfaced:** Session 001
**Status:** Open
The methodology does not yet have a name. A name should emerge when the methodology has developed enough identity to be named meaningfully. See deliberation in `provenance/001-genesis/01-deliberation.md`, Question 6.

### OI-002: Threshold for substantive revision vs. minor correction
**Surfaced:** Session 001
**Status:** Open (data point added Session 002)
Decision D-004 established that substantive revisions trigger file-level version preservation while minor corrections do not. No formal criteria for distinguishing the two have been defined. Session 002 produced a data point: D-014 treated adding `tools/` to the workspace-structure spec as a minor correction, reasoning that changes *anticipated by* the specification's own language are minor updates, while changes that *alter the meaning or structure* of the specification are substantive. Future sessions should continue collecting data points toward formal criteria.

### OI-004: Incorporating genuinely independent perspectives
**Surfaced:** Session 001
**Status:** Open
When a single AI agent plays all perspectives, disagreement is simulated, not genuinely independent. The methodology should explore ways to incorporate truly independent viewpoints — different agents, different models, human participants. This is both a technical question (how to orchestrate multiple agents) and a process question (how to integrate their contributions into the deliberation format).

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

---

## Resolved Issues

| Issue | Resolved | Session | Notes |
|-------|----------|---------|-------|
| OI-003: Automated validation | 2026-04-17 | 002 | Built two-tier validation: `tools/validate.sh` + guided questions. See `specifications/validation-approach.md` and decisions D-010 through D-014. |
