---
session: 007
title: Shared Brief — External Application Re-examination
date: 2026-04-19
status: finalised-before-launch
deliberation-anchor-commit: d1d6908897600ff9a137e66e5715786b4a746cc8
perspectives:
  - generalist (Claude Opus 4.7, subagent)
  - steward (Claude Opus 4.7, subagent)
  - skeptic (Claude Opus 4.7, subagent, adversarial)
  - outsider (non-Claude, Codex/GPT-5 via codex exec, Shape A per D-021)
---

# Shared Brief — Session 007

**Notice to all perspectives.** This brief's non-role-specific sections (1–6) are **byte-identical** across all four perspectives (Generalist, Steward, Skeptic, Outsider). Only the Role-Specific Stance section at the end differs. Every perspective answers the same six design questions from the same stated context. Do not coordinate; do not seek external context beyond this brief; do not read workspace files during your reasoning.

---

## 1. Methodology Context

This workspace is building a domain-general design methodology in which diverse perspectives deliberate, produce durable specifications, and preserve the reasoning behind decisions (provenance) so that future readers — human or agent — can reconstruct not just what was decided but what was considered and why. The methodology is self-hosting: it evolves by applying its own process to itself.

The methodology proceeds in **sessions**. Each session performs a set of nine activities (Read, Assess, Convene, Deliberate, Decide, Produce, Validate, Record, Close). Each session produces a single increment of progress. The current session is **Session 007**.

The workspace currently contains:

- **4 active specifications:** `methodology-kernel` (v1), `workspace-structure` (v1), `validation-approach` (v3), `multi-agent-deliberation` (v3). 4 superseded preserved.
- **1 tool:** `tools/validate.sh` — a two-tier validator (15 Tier 1 checks, 7 Tier 2 guided questions).
- **43 prior decisions** (D-001 through D-043). **9 open issues** (OI-001 naming the methodology; OI-002 substantive-vs-minor revision threshold, five data points; OI-004 genuinely independent perspectives, narrowed-pending-sustained-practice with tally 2 of 3; OI-005 sub-activities and work-type variants; OI-006 cross-references between specifications; OI-007 scaling the open-issues format; OI-008 persisting validation reports; OI-009 monitor for drift-to-ritual; OI-011 intra-family model mixing). 2 resolved (OI-003 automated validation; OI-010 cross-model participation mechanism).

**Sessions 001 through 006** have all been self-work on the methodology's own infrastructure:

- Session 001 (Genesis): bootstrap, nine activities, workspace structure, methodology kernel.
- Session 002 (Self-Validation): built `tools/validate.sh` (13 checks, 6 questions at that time), first validation-approach spec.
- Session 003 (Multi-Agent Deliberation): first non-simulated parallel-subagent deliberation; specified the multi-agent deliberation pattern.
- Session 004 (Participation Mechanisms): specified the non-Claude participation mechanism (D-021), trigger rules for required non-Claude participation (D-023), per-participant manifest schema (D-024). Used bootstrap exemption (no non-Claude participant in-session).
- Session 005 (Schema Enforcement): first operational non-Claude participation (Outsider = OpenAI GPT-5 via `codex exec`). Added three Tier 1 checks (11 three-raw-output floor, 12 manifest well-formedness, 13 cross-model-claim honesty). OI-010 closed.
- Session 006 (Triggers-Met Schema): second heterogeneous-participant deliberation. Added per-decision `**Triggers met:**` annotation schema, two new Tier 1 checks (14 multi-agent trigger coverage, 15 non-Claude trigger coverage), session-number-gated at ≥006. Advanced OI-004 tally 1→2 of 3.

**The methodology has not yet been applied to any non-self problem.**

## 2. Problem Statement

PROMPT.md frames the methodology explicitly as domain-general: *"The methodology is not specific to any domain. It may be used to design software, research programmes, physical systems, policy interventions, curricula, organisations, or anything else where a complex thing must be brought into being and evolved over time."* The domain-generality is stated as an asserted property. It has not been tested.

Session 004's close ranked non-self application as priority #6. Session 005's close reframed it as "increasingly overdue." Session 006's assessment made it priority #2 and deferred it explicitly, giving as reason: *selecting a non-self problem on unilateral authority is heavy-handed without explicit user direction.* Session 006's close flagged that a third consecutive session of self-work without external application approaches the ceremony-accumulation pattern OI-009 exists to catch. Session 006's close explicitly instructed Session 007 to re-examine.

Session 007 is session three. OI-009's drift-to-ritual monitor is at its most sensitive. The orchestrating agent has not received new user direction on a target domain; the Session 006 rationale's load-bearing claim therefore has not been directly invalidated, but neither has it been re-defended against a session further along in the deferral pattern.

The question Session 007 answers is: **given the methodology's current maturity and the deferral history, should Session 007 begin the methodology's first non-self application (or explicitly prepare for it in Session 008), or is continued self-work justified at this point? If continued self-work is justified, what is the specific new justification that is not a re-statement of Session 006's deferral rationale, and what self-increment does this session produce? If external application is warranted, by what mechanism is the first problem selected, what are the criteria for a well-scoped first target, and does first external application require any specification or kernel change before first use?**

## 3. Design Questions

Answer each question. Be concrete. Name and argue against plausible alternatives. Do not only state your preferred answer.

**Q1. Overdueness versus readiness.** Is external application now overdue, or is the methodology better served by one or more further self-increments first? The opposing positions to address in your answer:

- Position A: *Three consecutive sessions of self-work after the methodology has mechanisms for multi-agent deliberation, non-Claude participation, two operational heterogeneous sessions, and machine-readable trigger coverage is the definition of the drift OI-009 exists to catch. Domain-generality is the methodology's central untested claim; testing it is the most load-bearing work available.*
- Position B: *Self-work has produced real evolution at every recent session — each increment has had concrete load-bearing motivation (not ritual). Nothing in the deferral history suggests the self-work is ceremony. Forcing an external pivot without explicit user direction on domain is itself the drift-signal: reactive motion to placate an open issue.*

State which position you find more load-bearing, and why. Be concrete about what evidence would change your position.

**Q2. Selection mechanism.** If external application is warranted, by what mechanism is the first target selected? Candidate mechanisms:

- **User-direction:** the orchestrating agent asks the user for a target domain and problem before proceeding. The user's input becomes the brief for Session 008.
- **Multi-agent selection:** convene a multi-agent deliberation (possibly later in this session, possibly as Session 008's primary work) specifically on "what is the right first target." The deliberation produces criteria plus a shortlist plus a recommended pick.
- **Unilateral proposal for user ratification:** the orchestrating agent proposes one target (chosen by reasonable judgment from available context) and records the user's accept/reject before proceeding.
- **Criteria-first, target-later:** this session produces selection criteria only, and defers target selection to a later session or to user direction.
- **Some combination:** e.g., criteria-first + user-direction + multi-agent validation of the chosen target.

Specify the mechanism, its cost, its accountability properties (who owns the choice, and how is that ownership recorded), and how it handles the load-bearing concern Session 006 named (that unilateral selection is heavy-handed).

**Q3. Criteria for a good first target.** What makes a domain and problem suitable as first external application? Consider:

- **Domain type.** Software, research, curriculum design, policy, physical system, organisational design, creative work, other. Is any domain particularly good or bad as first test?
- **Scope.** One-session-executable, multi-session, or explicitly open-ended?
- **Reversibility.** Does the target have low- or high-stakes consequences? Should first external be reversible (a sandbox design exercise) or externally-consequential (real decision)?
- **Validation accessibility.** Can the methodology's Validate activity be exercised? Is there a "test" in PROMPT.md's domain-general sense — reproducibility, pilot study, qualification campaign, automated test, or analogue — that applies?
- **Vocabulary distance.** Is the domain's vocabulary native to the methodology's existing specs and provenance, or genuinely external? Too-close domains risk confirmation bias; too-far domains risk the methodology's abstractions not translating.
- **Accessibility.** Does the orchestrating agent and the workspace have the tools, permissions, and context to do the work?

Specify what a well-scoped first target looks like. Do not pick one.

**Q4. Specification and kernel changes.** Does first external application require any specification or kernel change before first use? Consider:

- **Methodology kernel.** Do the nine activities translate cleanly to external work? Is any activity under-specified for non-self application (e.g., Read: the workspace has finite prior provenance; an external domain may have none or too much)?
- **Workspace structure.** Does `specifications/` and `provenance/` translate? Would external application need a new top-level directory (`domains/`, `applications/`, or similar)?
- **Multi-agent deliberation and validation specs.** Are they written in a way that assumes self-work? Would they need clarifications to avoid self-referential phrasing in an external domain?

If changes are required, specify them minimally. If no changes are required, argue why the existing specs are sufficient and what stress-test would surface hidden assumptions.

**Q5. Alternative self-increment.** If the re-examination's outcome is continued self-work, what specific self-increment does Session 007 produce, and what is the justification distinct from Session 006's deferral rationale?

Candidate self-increments (not exhaustive):

- **OI-001** — naming the methodology. The methodology is now mature enough to be named meaningfully; external reference to it will be easier when it has a name.
- **OI-004 criterion 4** — articulating what "substantively different training provenance" means. This advances OI-004 closure irrespective of the 2-of-3 tally.
- **OI-007** — open-issues scaling format; at 9 open issues this is not pressing but is a candidate.
- **OI-011** — intra-family model mixing guidance.
- **OI-005** — sub-activities and work-type variants. Explicitly blocked on non-self application per Session 005's deferral; cannot be addressed honestly without first external application.
- **Something not previously surfaced** — a specific methodology weakness the re-examination exposes.

State the increment, its load-bearing justification, and why its justification is distinct from a deferral of the re-examination (not just a re-statement of "we need more time").

**Q6. OI-009 drift-to-ritual implications.** Whichever outcome the session reaches, does it activate the OI-009 drift-to-ritual signal? Consider:

- OI-009 was opened after Session 003 (*"multi-agent deliberation will drift to ritual within five sessions"*, the adversary's argument). Sessions 004, 005, 006 audits found no drift signal. Session 006 close named the third consecutive self-session specifically as the signal OI-009 monitors for.
- Drift is characterised in OI-009 as: multi-agent applied to typos, renames, reordering, or decisions with no genuinely articulable alternative positions. The Session 007 deliberation has genuinely articulable alternative positions (A and B in Q1 are genuine); the deliberation is not applied to a typo.
- But drift could also take the form of: load-bearing self-work that is nevertheless another session of self-work when external application is the actual structural need.

State whether Session 007's chosen outcome activates the drift signal, and what specific criterion distinguishes "load-bearing self-work" from "ritual-tracking self-work" at this point in the methodology's maturity. If your Q1 answer is Position A, describe what the methodology should do if Session 007 nevertheless concludes "one more self-session." If your Q1 answer is Position B, describe the concrete criterion that would make the next self-deferral unacceptable.

## 4. Response format

Produce a single Markdown response. Use H2 headings matching `## Q1` through `## Q6`. Under each heading, provide your answer, the arguments you considered, and the rejected alternatives. Target length: 250–500 words per question, reader judgment.

At the end of your response, include a short section `## Meta-note` of up to 150 words noting: (a) any position you hold that you expect to differ from what other perspectives will say, and why it is load-bearing; (b) any assumption in the brief you flag as suspect; (c) any concern about the deliberation's scoping or framing.

## 5. Constraint on external imports

Reason primarily from this brief. Do not open workspace files. If an idea you want to use arrived through your pretraining, a real-world example, or an analogue from outside the methodology, flag it explicitly (e.g., "[external analogue: ...]") and argue why the analogue applies; do not silently commit external ideas as if generated from within the brief.

## 6. Closing note

Your response will be committed verbatim as provenance. It will be read by synthesis in conjunction with three other perspective responses. Your positions — including positions you hold reluctantly or conditionally — are load-bearing. Do not soften them to anticipate synthesis; record them at their strongest. If you hold a position in tension with your role-specific stance, record that tension explicitly; the synthesis prefers honest tension to performed alignment.

---

## 7. Role-Specific Stance

*(This is the only section that differs across the four briefs.)*
