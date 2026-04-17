---
session: 001
title: Foundational Decisions
date: 2026-04-17
status: complete
---

# Decisions — Session 001: Genesis

## D-001: The methodology's core rhythm

**Decision:** The methodology operates through nine named activities: Read, Assess, Convene, Deliberate, Decide, Produce, Validate, Record, Close. These are a vocabulary, not a strict sequence. They have a general flow but permit recursion.

**Rationale:** Fine-grained activities (nine rather than three) make each step's stance explicit, which matters both for AI agents adopting the right mode and for provenance that distinguishes observation from argument from decision.

**Rejected alternatives:**
- Three coarse phases (understand, reason, produce) — rejected because they hide critical transitions, particularly the decide-to-produce and produce-to-validate boundaries.
- Strictly sequential stages — rejected because real work is recursive; reading may resume during deliberation, deliberation may reveal the need for more assessment.

**What remains open:** Whether the nine activities need sub-activities, and whether certain work types (pure research vs. design decisions vs. validation) warrant different subsets of the nine.

---

## D-002: Provenance structure

**Decision:** Provenance is organized by session in numbered directories (`provenance/NNN-title/`). Each session produces Markdown files with YAML frontmatter. Records are immutable once the session closes; corrections are made in subsequent sessions.

**Rationale:** Per-session directories group related records. Markdown with frontmatter is both human-readable and machine-parseable. Immutability ensures the reasoning trail is trustworthy.

**Rejected alternatives:**
- Single-file provenance (one growing document) — rejected because it becomes unwieldy and makes it hard to find specific deliberations.
- Per-topic provenance (one file per decision across sessions) — rejected because it breaks the temporal coherence of a session's reasoning.
- Provenance without frontmatter — rejected because metadata (session number, date, status) is necessary for automated processing.

**What remains open:** The exact frontmatter schema beyond the minimum (session, title, date, status). Future sessions may identify additional metadata needs.

---

## D-003: Specification format

**Decision:** Specifications live in `specifications/` as Markdown files with YAML frontmatter (title, version, status, created, last-updated, supersedes). Each has three sections: Purpose, Specification, Validation. Status lifecycle: draft → active → superseded | deprecated.

**Rationale:** This format balances completeness with simplicity. Purpose explains why the specification exists. The specification itself is the normative content. Validation makes the specification testable.

**Rejected alternatives:**
- Specifications without validation sections — rejected because untestable specifications drift from reality.
- Specifications as structured data (YAML/JSON throughout) — rejected because the specification body needs to be readable prose, not just structured fields.
- Inline version history — rejected in favor of git-based version control with file-level preservation for substantive revisions.

**What remains open:** Whether specifications need cross-references (links to related specifications, links to provenance that produced them). The current format doesn't mandate this but doesn't prevent it.

---

## D-004: Specification versioning

**Decision:** Git provides the primary version control. When a specification undergoes substantive revision (not minor corrections), the prior version is preserved by renaming it with a version suffix (e.g., `methodology-kernel-v1.md`), and the new version takes the canonical filename. The new version's `supersedes` field links to the old.

**Rationale:** This makes succession visible in the directory listing without requiring git archaeology, while avoiding the overhead of preserving every minor edit as a separate file.

**Rejected alternatives:**
- Git-only versioning (no file-level preservation) — rejected because it makes succession invisible to casual readers.
- File-level preservation for every change — rejected as excessive; minor corrections don't warrant separate files.

**What remains open:** The threshold between "minor correction" and "substantive revision." Future sessions should develop criteria.

---

## D-005: Perspectives are work-specific, not fixed

**Decision:** Perspectives are chosen for the work at hand, not prescribed as a standing committee. The Convene activity selects and documents them. Deliberative work (where decisions are made) must include at least one adversarial perspective.

**Rationale:** Different work requires different viewpoints. Forcing irrelevant perspectives adds noise. But all decision-making benefits from challenge.

**Rejected alternatives:**
- Fixed roster of perspectives for all sessions — rejected because different work demands different expertise.
- No adversarial requirement — rejected because unchallenged consensus is the methodology's most dangerous failure mode.
- Always including a specific set (e.g., always include the Historian) — rejected as overly prescriptive, though in practice many perspectives will recur.

**What remains open:** How to select perspectives well. The methodology currently relies on the judgment of whoever (or whatever) performs the Assess activity. Over time, patterns will emerge about which perspectives are valuable for which kinds of work — these patterns should be documented when they become clear.

---

## D-006: Workspace structure

**Decision:** The workspace has four top-level elements: `PROMPT.md` (the bootstrap prompt), `SESSION-LOG.md` (running session index), `specifications/` (living specifications), `provenance/` (historical reasoning), and `open-issues.md` (known unknowns). Additional directories may be created by future sessions as needed.

**Rationale:** Minimal structure that covers the three essential kinds of content: current truth (specifications), historical reasoning (provenance), and known gaps (open issues). The session log provides quick orientation without requiring a full read of all provenance.

**Rejected alternatives:**
- Open issues as a directory of individual files — rejected for now as excessive for a small list. May be revisited.
- An `implementations/` directory — rejected as premature. Created when needed.
- Subdirectories within `specifications/` — rejected as premature. The current number of specifications doesn't warrant hierarchy.

**What remains open:** At what scale the structure needs hierarchy. When specifications or open issues become numerous, the flat structure may need revision.

---

## D-007: No name yet

**Decision:** The methodology does not have a name. It refers to itself as "the methodology" until it has developed enough identity to be named meaningfully.

**Rationale:** Names create attachment and resist evolution. The methodology is too nascent to name well.

**Rejected alternatives:**
- Adopting a provisional working name — rejected because "provisional" names tend to stick.
- Naming it now based on its principles — rejected because the principles themselves may evolve.

**What remains open:** Naming, explicitly. This is an open issue for future sessions.

---

## D-008: Validation is specification-level

**Decision:** Each specification includes its own validation criteria. The methodology's overall health is assessed heuristically during each session's Assess activity, not through a separate validation framework.

**Rationale:** Specification-level validation is concrete and actionable. Methodology-level validation is currently too abstract to formalize.

**Rejected alternatives:**
- Automated methodology-level validation — rejected as premature. The methodology doesn't yet have enough structure to automate validation.
- No formal validation — rejected because "just trust the process" is the failure mode of every methodology that stops evolving.

**What remains open:** Whether and when to develop automated validation. As the methodology matures, patterns of healthy and unhealthy sessions will emerge, and these could be formalized.

---

## D-009: Acknowledgment of simulated disagreement

**Decision:** The methodology explicitly acknowledges that when a single AI agent plays all perspectives, the disagreement is simulated, not genuinely independent. This is a known limitation, mitigated by structural requirements (positions stated before hearing others, disagreements preserved, adversarial perspectives required).

**Rationale:** Honesty about limitations is preferable to pretending the process is something it isn't. The structural mitigations reduce (but don't eliminate) the convergence bias.

**Rejected alternatives:**
- Ignoring the limitation — rejected as dishonest.
- Refusing to use multi-perspective deliberation because it's simulated — rejected because even simulated disagreement produces better outcomes than no deliberation, and the structural mitigations are meaningful.

**What remains open:** How to incorporate genuinely independent perspectives (different AI agents, different models, human participants) as the methodology matures. This is both a technical and a process design question.
