---
session: 002
title: Decisions — Automated Self-Validation
date: 2026-04-17
status: complete
---

# Decisions — Session 002: Self-Validation

## D-010: Build automated validation now

**Decision:** Build an automated validation tool for the methodology. The tool checks structural properties of specifications, provenance, and workspace organization. It uses a two-tier model: automated structural checks plus guided semantic questions.

**Rationale:** The cost is low (shell script, under 200 lines), the value compounds across all future sessions (every Read activity can include a health check), and the methodology's own principles call for it — both existing specifications include Validation sections that describe checkable criteria.

**Rejected alternatives:**
- Defer validation until the methodology is more mature — rejected because the specifications were designed with validation in mind and deferring means those Validation sections remain aspirational.
- Build only automated checks without guided questions — rejected because structural checks alone create false confidence by ignoring semantic consistency.
- Build only a guided checklist without automation — rejected because it misses the value of repeatable automated checking.

**What remains open:** Whether validation output should be stored in provenance (currently it's ephemeral — run at the start of a session, consumed, not saved). Tracked as OI-008.

---

## D-011: Create tools/ directory

**Decision:** Create a `tools/` top-level directory for methodology tooling. Update the workspace-structure specification to document it.

**Rationale:** The workspace-structure spec explicitly anticipates new directories: "New top-level directories may be created by future sessions when the work demands them. Any new directory should be documented by updating this specification." The validation script is the first tool; future sessions may produce others.

**Rejected alternatives:**
- Place the script at the workspace root — rejected because `tools/` signals intent and keeps the root clean.
- Defer directory creation until there are multiple tools — rejected because one real tool is sufficient justification, and the spec expects documentation at creation time.

**What remains open:** Nothing specific to this decision.

---

## D-012: Validation specification

**Decision:** Create `specifications/validation-approach.md` specifying the two-tier validation model, including the ten structural checks, five guided questions, and explicit statement of limitations.

**Rationale:** The validation tool is a substantive artifact of the methodology. Following the methodology's own principle, substantive artifacts get specifications. The specification serves as the authoritative description of what validation covers.

**Rejected alternatives:**
- No specification for the validation tool — rejected as inconsistent with the methodology's principle that substantive artifacts are specified.
- Embedding the validation description in the methodology-kernel spec — rejected because validation is a distinct concern and may evolve independently.

**What remains open:** Whether the validation specification should include acceptance criteria for the guided questions (e.g., "if the answer to question 4 is 'no' for three consecutive sessions, the methodology should be revised"). Deferred as premature.

---

## D-013: Two-tier validation model

**Decision:** Validation has two tiers:
- **Tier 1 (Structural):** Ten automated checks covering workspace structure, specification format, provenance integrity, decision quality, and immutability.
- **Tier 2 (Semantic):** Five guided questions covering provenance usefulness, specification consistency, adversarial quality, meaningful progress, and specification-reality alignment.

Tier 1 is run by `tools/validate.sh`. Tier 2 is printed by the tool for the agent or human to assess.

**Rationale:** Structural properties are automatable and cheap to check. Semantic properties require judgment. Combining both tiers provides real assurance without pretending that automation alone is sufficient. The Skeptic's concern about false confidence is addressed by explicitly separating what automation can and cannot check.

**Rejected alternatives:**
- Automated-only validation — rejected because it misses semantic consistency.
- Guided-only validation — rejected because it misses the value of repeatable automated checks.
- More than five guided questions — rejected by the Pragmatist's constraint that more questions produce diminishing attention.

**What remains open:** Whether Tier 2 should eventually be partially automated (e.g., using AI to compare specifications for semantic contradictions). Interesting but beyond the current session's scope.

---

## D-014: Workspace-structure update is a minor correction

**Decision:** Adding the `tools/` directory to the workspace-structure specification is treated as a minor correction (git-only, no file-level version preservation), not a substantive revision.

**Rationale:** The specification explicitly anticipates new directories and instructs future sessions to document them. This is the spec working as designed, not changing its meaning. The prior version is preserved in git history.

**Note on OI-002:** This decision provides a data point for OI-002 (threshold for substantive revision vs. minor correction). The emerging heuristic: if a change is *anticipated by* the specification's own language, it is a minor update. If a change *alters the meaning or structure* of the specification, it is substantive.

**Rejected alternatives:**
- Treating this as a substantive revision (preserving workspace-structure-v1.md) — rejected as excessive for an anticipated extension.

**What remains open:** OI-002 is not resolved by this decision, but gains a data point.
