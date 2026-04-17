---
session: 001
title: Foundational Deliberation — Shape of the Methodology
date: 2026-04-17
status: complete
---

# Foundational Deliberation

## Bootstrap Acknowledgment

This is the first application of the prompt. No methodology exists yet, so this session cannot fully follow the methodology it is creating. This is an acknowledged bootstrapping problem. The goal is to produce enough structure that the second session has a process to follow and enough substance that the process is worth following. Future sessions will refine what this one roughed in.

## Perspectives Convened

Seven perspectives were assembled for this foundational deliberation. The selection was driven by the nature of the work: establishing a methodology's initial shape requires historical grounding, practical sense, critical examination, systemic awareness, consideration of AI's role, resistance to unnecessary complexity, and attention to how knowledge is preserved and found.

1. **The Historian** — Brings knowledge of what has been tried across design traditions. Guards against reinventing failed approaches. Recognizes when an idea has a lineage worth acknowledging.

2. **The Practitioner** — Focuses on what actually works when people (and agents) sit down to design something. Resists theory that doesn't survive contact with real work.

3. **The Skeptic** — Challenges assumptions, especially those that feel obvious. Asks "what could go wrong?" and "who is this actually for?"

4. **The Systems Thinker** — Attends to feedback loops, emergence, unintended consequences, and the interactions between the methodology's parts.

5. **The Futurist** — Considers what AI participation means for design methodology. Not as speculation, but as present reality — AI agents are the ones applying this prompt.

6. **The Minimalist** — Argues for the least structure that achieves the goals. Opposes premature abstraction, unnecessary ceremony, and features that serve hypothetical future needs.

7. **The Archivist** — Cares about preservation, findability, and the long-term legibility of what is produced. Thinks about how future readers (human or agent) will navigate the workspace.

---

## Question 1: What is the basic rhythm of the methodology?

**Historian:** Every methodology that survives contact with real work has a rhythm. Waterfall's is: specify-build-verify. Agile's is: plan-build-demonstrate. Design thinking's is: diverge-converge. The rhythm is what practitioners internalize; everything else is commentary. Ours needs to be clear enough to internalize.

**Practitioner:** I see nine things that need to happen each session: read the workspace, assess what's needed, convene perspectives, deliberate, decide, produce artifacts, validate them, record provenance, and close cleanly. But calling them "stages" makes it sound sequential. In practice, you read and you discover something that changes your assessment, or you deliberate and realize you need to read more.

**Systems Thinker:** They're not stages, they're activities. They have a general flow — you can't decide before you deliberate, and you can't deliberate before you know what you're deliberating about — but within that general flow, they're recursive. You might read → assess → realize the assessment requires more reading. That's fine. What matters is that all nine activities happen before the session ends.

**Minimalist:** Nine is too many to name individually. Can we group them? I see three phases: understand (read + assess), reason (convene + deliberate + decide), and produce (build artifacts + validate + record + close).

**Skeptic:** Three phases is too few. It hides the most important transitions. The step from "decide" to "produce" is where most methodologies fail — decisions that seem clear in discussion become ambiguous when you actually have to make something. And the step from "produce" to "validate" is where reality intervenes. If you hide those transitions inside a single "produce" phase, you'll lose track of them.

**Futurist:** For AI agents applying this, the granularity matters. An agent needs to know which activity it's performing so it can adopt the appropriate stance — reading is receptive, deliberation is generative, validation is critical. Lumping them together produces muddled work.

**Archivist:** The activities also determine what gets recorded. Reading produces a state assessment. Deliberation produces positions and arguments. Decisions produce decision records. If we collapse these, we lose the ability to distinguish what was observed from what was argued from what was decided.

### Resolution

The methodology has **nine named activities**, understood as a vocabulary rather than a strict sequence. They have a general flow but permit recursion. The nine activities are:

1. **Read** — Absorb the full current state of the workspace
2. **Assess** — Determine what the workspace needs and what this session should address
3. **Convene** — Assemble perspectives suited to the work at hand
4. **Deliberate** — Reason together from multiple perspectives, preserving disagreement
5. **Decide** — Make concrete decisions with rationale and record of alternatives
6. **Produce** — Create or update the artifacts the decisions warrant
7. **Validate** — Check that artifacts are coherent, consistent, and accurate
8. **Record** — Commit provenance so future sessions can reconstruct the reasoning
9. **Close** — Verify the workspace is in a coherent state, document what comes next

**What was contested:** Whether nine was too many (Minimalist), whether they should be strictly ordered (no — Systems Thinker and Practitioner both argued against), and whether "Convene" deserved its own activity or should be folded into "Deliberate" (Historian argued it should be separate because the choice of perspectives shapes outcomes and should be explicit and recorded).

---

## Question 2: How should provenance be structured?

**Archivist:** Provenance is the methodology's institutional memory. Without it, each session starts from zero. It needs to be: (a) complete enough to reconstruct reasoning, (b) organized enough to navigate, (c) machine-readable enough for agents to process, and (d) human-readable enough for people to audit.

**Historian:** ADRs got the right idea — immutable records that accumulate — but they're too thin. A single paragraph of "context" can't reconstruct a real design deliberation. We need richer records.

**Practitioner:** But if the records are too rich, they won't get written. Or they'll be so long that nobody reads them. There's a sweet spot between a one-paragraph ADR and a 50-page design review document.

**Futurist:** The "nobody reads them" problem is different for agents. An agent can read 50 pages in seconds. The constraint isn't length — it's structure. A long but well-structured document is more useful to an agent than a short but ambiguous one.

**Minimalist:** Structure, yes. But not imposed structure — not a template with 20 required fields. The structure should be the minimum needed to make the record navigable. What happened? What was considered? What was decided? What was rejected and why?

**Skeptic:** I want to push on "what was rejected and why." Rejected alternatives are where the real knowledge lives. Anyone can read a decision and understand what was chosen. The value of provenance is understanding what *wasn't* chosen and the reasoning that excluded it. That's what prevents future sessions from re-proposing ideas that were already considered.

**Systems Thinker:** Provenance also needs to capture uncertainty — things that were flagged as unknown or risky but weren't resolved. These are inputs to future sessions. If we don't capture them, they'll be lost until someone re-discovers the uncertainty the hard way.

### Resolution

Provenance is organized by session, numbered sequentially (`001-genesis`, `002-...`, etc.). Each session's provenance is a directory containing:

- A **survey** or **reading record** (what was observed at the start)
- A **deliberation record** (perspectives convened, positions taken, arguments made)
- A **decision record** (what was decided, what was rejected, what remains open)

Records are **immutable** once the session closes. Errors are corrected by new records in subsequent sessions that reference and supersede the originals.

Records use **Markdown with YAML frontmatter** — human-readable body, machine-parseable metadata.

**What was contested:** Whether provenance should be structured as one file per session or one file per deliberation topic. The Archivist argued for per-session directories containing multiple files, since a session may address several topics. This was adopted. The Minimalist argued against YAML frontmatter as unnecessary structure; the Futurist argued for it as the minimum metadata needed for automated processing. Frontmatter was adopted, but kept minimal (session number, title, date, status).

---

## Question 3: How should specifications be structured?

**Practitioner:** Specifications are the durable artifacts. They describe what the methodology has decided, as of right now. They should be the source of truth — if someone asks "how does this work?", the specification is the answer.

**Historian:** The key problem with specifications in traditional systems engineering is that they go stale. They describe what was intended, not what was built. Then nobody trusts them, so nobody reads them, so nobody updates them, and the cycle continues.

**Systems Thinker:** The solution is validation. A specification should have a corresponding way to check whether it still describes reality. In software, that's a test. In other domains, it's whatever demonstration is appropriate. If the specification and reality disagree, that's an open issue for the next session.

**Minimalist:** Each specification should be one Markdown file with clear sections: what this specifies, the specification itself, and how to validate it. No more.

**Archivist:** Each specification also needs metadata: version, status, creation date, what it supersedes (if anything). And a version history — not inline, but traceable through the provenance records.

**Skeptic:** What about the status lifecycle? A specification can be a draft (proposed but not yet deliberated), active (deliberated and accepted), or superseded (replaced by a newer version). Can it also be deprecated without a replacement?

**Historian:** Yes — ADRs have "deprecated" as a status for decisions that are no longer relevant because the thing they governed no longer exists. Specifications need the same.

### Resolution

Specifications live in the `specifications/` directory. Each is a Markdown file with YAML frontmatter:

```
---
title: [what this specifies]
version: [integer, starting at 1]
status: draft | active | superseded | deprecated
created: [date]
last-updated: [date]
supersedes: [path to prior version, or "none"]
---
```

The body has three sections:
1. **Purpose** — What this specification governs and why it exists
2. **Specification** — The normative content
3. **Validation** — How to verify this specification still describes reality

When a specification is revised, the prior version is preserved. The versioning mechanism is: the old file is renamed to include its version number (e.g., `methodology-kernel-v1.md`) and the new version takes the canonical name. The new version's `supersedes` field points to the old one.

**What was contested:** Whether to version through filenames or through a version control system (git). The Futurist argued that git history is sufficient and renaming files is clutter. The Archivist argued that file-level versioning makes succession visible without requiring git knowledge. The Practitioner broke the tie: use git for the actual version control, but when a specification is *substantively* revised (not just corrected), preserve the old version in the filename so the succession is visible in the directory listing. Minor corrections don't trigger this — they're just commits.

---

## Question 4: How should perspectives work?

**Historian:** This is the most novel part of the methodology. Traditional approaches use review boards, peer review, or cross-functional teams. But those are constrained by who's available and willing. AI can instantiate perspectives on demand, chosen for relevance to the specific work.

**Futurist:** This is where AI participation most changes the game. A human team has five to ten people with fixed backgrounds. An AI-based methodology can convene exactly the perspectives needed for each piece of work. A structural engineering question gets different perspectives than a policy design question.

**Skeptic:** But there's a danger. If a single AI agent is playing all the roles, the "disagreement" is simulated, not real. The perspectives may converge too easily because they share the same underlying model. We need to acknowledge this limitation honestly.

**Systems Thinker:** The mitigation is structural. The methodology should require that each perspective states its position before hearing others (to prevent anchoring), that disagreements are recorded even when a resolution is reached, and that the Skeptic perspective is always included regardless of the topic.

**Minimalist:** Not "always." The Skeptic is valuable for decisions. For pure information-gathering (like the survey we just did), forced skepticism is friction without value.

**Practitioner:** I agree with the Minimalist. The perspectives should be chosen for the work, not prescribed. But the methodology should say that deliberative work (where decisions are made) should always include at least one perspective whose job is to challenge assumptions.

**Archivist:** The convening of perspectives should be recorded in provenance — which perspectives were chosen, why, and what each contributed. This is part of the reasoning trail.

### Resolution

Perspectives are **chosen for the work**, not fixed. The methodology does not prescribe a standing committee. Instead:

- Each session's **Assess** activity determines what perspectives are needed
- The **Convene** activity names them, describes their stance, and records why they were chosen
- The **Deliberate** activity gives each perspective voice and preserves disagreements
- For deliberative work (where decisions are made), at least one perspective must be adversarial — its job is to challenge the emerging consensus

The methodology acknowledges that when a single AI agent plays all perspectives, the disagreement is simulated. This is a known limitation. Mitigations: perspectives state positions before hearing others (recorded in the deliberation), disagreements are preserved even when resolved, and the methodology remains open to incorporating genuinely independent perspectives (different agents, different models, human participants) as the methodology matures.

**What was contested:** Whether a fixed roster of perspectives should be prescribed (Historian argued for it, citing the value of consistency; Minimalist and Practitioner argued against, citing the value of tailoring). The resolution was no fixed roster, but the convention that adversarial perspectives are always included in decisions.

---

## Question 5: What should the workspace structure be?

**Archivist:** The workspace needs three kinds of space: one for current truth (specifications), one for historical reasoning (provenance), and one for known unknowns (open issues).

**Minimalist:** Three directories plus the prompt and a session log. That's it.

**Systems Thinker:** What about implementations? If the methodology ever produces things beyond specifications — code, prototypes, validated demonstrations — where do those go?

**Practitioner:** When we need them. Right now, the methodology is designing itself. The artifacts are specifications and provenance. If a future session needs an `implementations/` directory, it can create one. Don't build structure for hypothetical needs.

**Skeptic:** What about the prompt itself? PROMPT.md is the thing that drives the process. It's not a specification (it's not produced by the methodology), and it's not provenance (it's not a record of reasoning). It's the kernel that bootstraps everything.

**Archivist:** It stays at the root. It's the one artifact that precedes the methodology. Everything else is produced by the process.

### Resolution

```
/PROMPT.md                    # The bootstrap prompt (precedes the methodology)
/SESSION-LOG.md               # Running log of sessions for quick orientation
/open-issues.md               # Known questions, gaps, and uncertainties
/specifications/              # Living specifications (current truth)
/provenance/                  # Historical reasoning records
  /001-genesis/               # First session
    00-survey.md
    01-deliberation.md
    02-decisions.md
  /002-.../                   # Subsequent sessions
```

New top-level directories may be created by future sessions when the work demands them. The structure is not fixed — it's a living specification that the methodology can revise.

**What was contested:** Whether `open-issues.md` should be a single file or a directory of individual issues. The Archivist argued for a directory (one file per issue, better for tracking and linking). The Minimalist argued for a single file (simpler, less overhead for what is currently a small list). The Minimalist won for now, with the understanding that this may be revisited when the number of open issues makes a single file unwieldy.

---

## Question 6: Should we name the methodology?

**Historian:** Every serious methodology has a name. It makes it referrable. "The methodology" is awkward.

**Minimalist:** Naming it now is premature. The methodology barely exists. A name should emerge from what it becomes, not be imposed at birth.

**Skeptic:** A name also creates attachment. Once named, it becomes an identity to defend rather than a system to evolve. Early naming ossifies.

**Practitioner:** A *working* name would be useful. Something explicitly provisional. Better than writing "the methodology" in every sentence.

**Futurist:** The name could be one of the things the methodology discovers about itself. Put it on the open issues list and let future sessions decide.

### Resolution

No name yet. The methodology refers to itself as "the methodology" for now. Naming is recorded as an open issue for future sessions to address when the methodology has enough identity to name meaningfully.

**What was contested:** Whether to adopt a provisional working name (Practitioner favored it). The group decided against it because even a "provisional" name tends to stick, and the methodology doesn't yet have enough identity to name well.

---

## Question 7: How should the methodology validate itself?

**Systems Thinker:** The prompt says the methodology should include validation mechanisms. Since the methodology is self-hosting, it must validate *itself*. This is the hardest part.

**Skeptic:** What would a failed validation look like? The methodology can't crash. It can't throw an error. How do we know when it's not working?

**Practitioner:** Indicators of failure: sessions that don't produce meaningful progress. Specifications that contradict each other. Decisions that get revisited without new information. Provenance that doesn't help future sessions understand past reasoning. These are all detectable.

**Futurist:** For an AI agent, "does the provenance help me understand past reasoning?" is testable. If a future session reads the provenance from this session and can reconstruct why we made these decisions, the provenance works. If it can't, it doesn't.

**Archivist:** Validation should be built into the specifications themselves. Each specification's "Validation" section says how to check it. For the workspace structure specification, validation is: does the workspace actually follow this structure? For the methodology kernel, validation is: did the last session actually follow this process?

### Resolution

Validation is specification-level, not methodology-level. Each specification includes a "Validation" section that describes how to check whether the specification still describes reality. The overall health of the methodology is assessed by whether:

1. Sessions produce meaningful progress (assessed during the Assess activity)
2. Specifications are internally consistent (assessed during the Validate activity)
3. Provenance enables future sessions to reconstruct reasoning (assessed by each session's Read activity)
4. Open issues are being addressed, not just accumulated (assessed during Assess)

These are heuristic, not automated. As the methodology matures, it may develop more formal validation mechanisms. For now, the Assess activity at the start of each session serves as the primary health check.

**What was contested:** Whether to attempt automated validation now (Futurist) or defer it (Minimalist). Deferred, since the methodology doesn't yet have enough structure to automate validation meaningfully. Recorded as an open issue.
