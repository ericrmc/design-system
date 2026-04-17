---
session: 002
title: Deliberation — Automated Self-Validation
date: 2026-04-17
status: complete
---

# Deliberation — Session 002: Automated Self-Validation

## Perspectives Convened

Five perspectives were assembled for this deliberation. The work — designing a validation mechanism for the methodology itself — requires implementation skill, methodological awareness, practical restraint, forward-looking design sense, and adversarial challenge.

1. **The Implementer** — Focuses on what is technically buildable with available tools. Thinks in terms of shell commands, file operations, and pattern matching.

2. **The Methodologist** — Cares about whether the validation approach is consistent with the methodology's principles: provenance, traceability, self-hosting, and domain-generality.

3. **The Skeptic** (adversarial) — Challenges whether automated validation is worth building now. Questions whether structural checks provide real assurance or false confidence.

4. **The Pragmatist** — Advocates for the simplest approach that delivers genuine value. Resists scope creep and overengineering.

5. **The Futurist** — Considers how validation will be used by AI agents in future sessions and how it should scale as the methodology grows.

---

## Question 1: Is automated validation worth building at this stage?

**Skeptic (opening position):** The methodology has two specifications and one session of provenance. Building a validation framework for this is like installing a sprinkler system in a tent. The real risk to this methodology isn't structural — it's semantic. The specs could have perfect YAML frontmatter and still be wrong about what the methodology should do. Automated checks give false confidence by focusing on the easy-to-check things while ignoring the hard ones.

**Methodologist (opening position):** The methodology's own principles argue for building validation now. Both existing specifications include Validation sections — they were *designed* to be checkable. Not building the checks means those sections are aspirational rather than operative. A self-hosting methodology that can't verify its own specifications is not yet self-hosting.

**Implementer (opening position):** The checks defined in the specifications are straightforward to implement. File existence, frontmatter validation, naming conventions, cross-referencing the session log — this is a short shell script. The cost is low.

**Pragmatist (opening position):** Low cost and immediate value. Every future session starts with Read. If Read includes a validation step, every session gets a health check for free. This compounds. The first session it catches a real problem, it pays for itself.

**Futurist (opening position):** For AI agents, validation output is structured orientation. An agent reading the workspace for the first time gets: "3 specifications, all well-formed. 2 provenance sessions, complete. Session log up to date." That's useful context before diving into the content.

**Skeptic (rebuttal):** I'll concede the cost argument — if it's truly cheap to build, the bar for value is lower. But I maintain that structural validation creates a false sense of health. You could have perfectly structured specs that contradict each other, or a complete provenance record that doesn't actually capture the real reasoning. The danger is that "validation passes" becomes a proxy for "the methodology is working."

**Methodologist (rebuttal):** Agreed — structural checks are necessary but not sufficient. That's why I propose a two-tier model: automated checks for structure, plus a set of guided questions for semantic assessment that the agent (or human) answers during the Assess activity. The guided questions are the methodology's way of saying "these things matter but can't be automated — pay attention to them."

**Pragmatist:** I like the two-tier model as long as the guided questions are short. Five questions maximum. More than that and they become wallpaper.

**Skeptic (final position):** Two-tier addresses my concern. Build it. But be honest in the specification about what the automated checks do and don't catch. Don't call it "validation" without qualification — call the automated part "structural checks" and reserve "validation" for the full two-tier process.

### Resolution

**Build automated validation now.** The cost is low, the value compounds across sessions, and the methodology's principles call for it. Use a two-tier model: automated structural checks for format and consistency, plus guided semantic questions for judgment-dependent assessment. The automated tier is explicit about its limitations — it checks structure, not meaning.

**What was contested:** Whether building validation now is premature (Skeptic argued it was, but conceded when the cost was shown to be low and the two-tier model addressed the false-confidence concern). Whether the guided questions would actually be used (Pragmatist's constraint: maximum five questions).

---

## Question 2: What form should the validation tool take?

**Implementer (opening position):** Shell script. The checks are all file operations: does this path exist, does this file contain this pattern, what does git log say. No parsing libraries needed. No dependencies. Runs on any Unix system.

**Futurist (opening position):** I'd argue for something more structured. A shell script that greps for patterns is fragile. What if the YAML style changes? What if section headings are formatted slightly differently?

**Implementer (rebuttal):** We're checking *our own* format conventions. We define what the format is. If the format changes, we update the script. That's how validation works — the validator matches the specification. And shell is the right level of tool for file-system checks.

**Pragmatist (opening position):** Shell script. Under 200 lines. Clear output. If it grows beyond that, future sessions can rewrite it in something more powerful. Don't optimize for the future version.

**Skeptic (opening position):** Whatever you build, make it idempotent and safe. It reads files; it never modifies them. That should be an explicit constraint.

**Methodologist:** The script should produce a report, not just exit codes. When an AI agent runs this at the start of a session, the output should be readable and actionable. A structured report with pass/fail/warning counts and clear per-check results.

**Futurist:** Agreed on the report format. Also: the script should be runnable as part of the Read activity. Future sessions should be able to say "I ran `tools/validate.sh` and here's what it found."

### Resolution

**Shell script at `tools/validate.sh`.** Read-only (never modifies files). Produces a clear report with pass/fail/warning counts and a list of guided questions. No external dependencies beyond standard Unix tools and git.

**What was contested:** Whether shell is sufficient or something more robust is needed (Futurist raised fragility concerns; Implementer argued the validator should match the specification, and shell is appropriate for file-structure checks). Whether the output format matters (Methodologist and Futurist agreed it should be a readable report, not just exit codes).

---

## Question 3: What should the automated checks cover?

**Implementer:** Drawing from the Validation sections of both existing specifications, here are the automatable checks:

From workspace-structure:
1. Required top-level files exist (PROMPT.md, SESSION-LOG.md, open-issues.md)
2. Required directories exist (specifications/, provenance/)
3. Each specification has YAML frontmatter with required fields
4. Each specification has Purpose, Specification, and Validation section headings
5. Provenance directories follow NNN-title naming convention
6. Session log has entry for each provenance directory

From methodology-kernel:
7. Decision records include "Rejected alternatives" sections

**Methodologist:** I'd add: check that every provenance directory contains at least one file. An empty provenance directory is a sign of an incomplete session.

**Pragmatist:** And provenance files should have their own frontmatter (session, title, date, status). That's already specified in workspace-structure.

**Skeptic:** What about immutability? The specs say provenance records are immutable after the session closes. Can we check that?

**Implementer:** Partially. We can check for uncommitted changes to provenance files — that catches in-progress violations. Full historical immutability verification (across git commits) is more complex and prone to false positives when provenance files are created across multiple commits within a session. I recommend a simple check for uncommitted changes, reported as a warning.

**Futurist:** The immutability check is valuable even as a basic heuristic. And if the methodology later moves to signed commits or content-addressed storage, the check can be upgraded.

### Resolution

**Ten automated checks**, grouped by what they validate:

*Workspace structure:*
1. Required top-level files exist
2. Required directories exist
3. Each specification has YAML frontmatter with required fields (title, version, status, created, last-updated, supersedes)
4. Each specification has three required section headings (Purpose, Specification, Validation)
5. Provenance directories follow NNN-title naming convention
6. Session log has an entry for each provenance directory

*Provenance integrity:*
7. Each provenance directory contains at least one file
8. Provenance files have YAML frontmatter (session, title, date, status)

*Decision quality:*
9. Decision records include rejected alternatives

*Immutability:*
10. No uncommitted changes to completed provenance files (basic heuristic, reported as warning)

**What was contested:** The scope of the immutability check (Skeptic raised the concern about reliability; Implementer proposed the simpler uncommitted-changes check as a practical first step; Futurist agreed that even a basic check is better than none).

---

## Question 4: What should the guided semantic questions be?

**Methodologist:** These are the checks that require judgment. Drawing from the specification validation criteria:
- Did the Read activity successfully use prior provenance?
- Are specifications semantically consistent with each other?
- Did deliberative sessions include genuinely adversarial challenge?
- Is the methodology producing meaningful progress?

**Pragmatist:** Four questions. Good. Under the five-question limit.

**Skeptic:** "Genuinely adversarial challenge" is hard to assess when the same agent plays all roles. But asking the question forces the agent to at least consider whether the Skeptic was a genuine challenger or a paper tiger.

**Futurist:** I'd add one more: "Are there specifications that describe things that no longer exist, or things that exist without specifications?" This catches both stale specs and undocumented additions.

**Pragmatist:** That's five. Stop there.

### Resolution

**Five guided assessment questions:**

1. Did this session's Read activity use prior provenance to understand past decisions? Were any past decisions re-proposed without acknowledgment?
2. Are the current specifications semantically consistent with each other? Do any contradict or make assumptions that conflict?
3. In deliberative work, did the adversarial perspective provide genuine challenge, or did it concede too easily?
4. Is the methodology producing meaningful progress, or is it accumulating ceremony without advancing?
5. Are there specifications that describe things that no longer exist, or things that exist without being specified?

**What was contested:** The number of questions (Pragmatist enforced a cap of five). Whether the adversarial-quality question is answerable by a single agent (Skeptic raised the concern; the group agreed it's still worth asking as a self-check).

---

## Question 5: Where does the tool live, and does this need a specification?

**Implementer:** `tools/validate.sh`. New directory.

**Methodologist:** The workspace-structure spec says new directories should be documented. So we update that spec. And the validation tool itself should have a specification — it's a substantive artifact of the methodology.

**Skeptic:** A specification for a shell script? Isn't that excessive?

**Methodologist:** It specifies what the tool checks and why, not its implementation details. The specification is the authoritative description of what validation covers. If someone rewrites the tool in Python later, the spec still holds.

**Pragmatist:** That's the right level. One specification, clear scope, obvious validation criteria. Do it.

**Skeptic (conceding):** Fine. But the specification should explicitly state the limitations — what structural checks don't catch.

### Resolution

- Create `tools/` directory
- Place `validate.sh` in `tools/`
- Update `specifications/workspace-structure.md` to document the `tools/` directory
- Create `specifications/validation-approach.md` specifying the two-tier validation model, the ten structural checks, and the five guided questions
- The specification explicitly states the limitations of automated structural checking

**What was contested:** Whether the tool needs its own specification (Skeptic questioned it; Methodologist argued it's consistent with the principle that substantive artifacts get specifications; Pragmatist agreed the spec is lightweight enough to justify).
