---
session: 006
title: Shared Brief — Triggers-Met Schema Extension
date: 2026-04-19
status: finalised-before-launch
deliberation-anchor-commit: to-be-set-at-brief-commit
perspectives:
  - archivist (Claude Opus 4.7, subagent)
  - implementer (Claude Opus 4.7, subagent)
  - skeptic (Claude Opus 4.7, subagent, adversarial)
  - outsider (non-Claude, Codex/GPT-5 via codex exec, Shape A per D-021)
---

# Shared Brief — Session 006

**Notice to all perspectives.** This brief's non-role-specific sections (1–6) are **byte-identical** across all four perspectives (Archivist, Implementer, Skeptic, Outsider). Only the Role-Specific Stance section at the end differs. Every perspective answers the same six design questions from the same stated context. Do not coordinate; do not seek external context beyond this brief; do not read workspace files during your reasoning.

---

## 1. Methodology Context

This workspace is building a domain-general design methodology in which diverse perspectives deliberate, produce durable specifications, and preserve the reasoning behind decisions (provenance) so that future readers — human or agent — can reconstruct not just what was decided but what was considered and why. The methodology is self-hosting: it evolves by applying its own process to itself.

The methodology proceeds in **sessions**. Each session performs a set of nine activities (Read, Assess, Convene, Deliberate, Decide, Produce, Validate, Record, Close). Each session produces a single increment of progress. The current session is **Session 006**.

The workspace currently contains:

- **4 active specifications:** `methodology-kernel` (v1), `workspace-structure` (v1), `validation-approach` (v2), `multi-agent-deliberation` (v2). 2 superseded preserved.
- **1 tool:** `tools/validate.sh` — a two-tier validator (13 Tier 1 checks, 6 Tier 2 guided questions).
- **36 prior decisions** (D-001 through D-036). **9 open issues** (OI-001, OI-002, OI-004, OI-005, OI-006, OI-007, OI-008, OI-009, OI-011). 2 resolved (OI-003, OI-010).

Two open issues bear directly on this deliberation:

- **OI-002:** Threshold for substantive versus minor revision of a specification (four prior data points).
- **OI-004:** Incorporating genuinely independent perspectives. Currently `narrowed-pending-sustained-practice`, with tally 1 of 3 required sessions. This session's deliberation, if conducted per the v2 schema on a required-trigger question, advances the tally to 2 of 3.

**Session 005** (the immediately prior session) was the methodology's first heterogeneous-participant deliberation: three Claude Opus 4.7 subagents plus one non-Claude participant (OpenAI GPT-5 via `codex exec`). Session 005 implemented three new Tier 1 checks in `validate.sh` (checks 11, 12, 13 — three-raw-output floor, manifest-schema well-formedness, cross-model-claim honesty) and deferred two further checks pending a prerequisite schema extension (`triggers_met:`) that this session is designing.

## 2. Problem Statement

`multi-agent-deliberation.md` v2's Validation section enumerates ten items; Session 005 implemented items 3, 8, and 9 as Tier 1 checks 11, 12, 13. Items 1 and 2 were deferred by D-028 because they require semantic classification of decision records, which bash cannot perform honestly without a machine-readable trigger annotation.

The two deferred v2 Validation items:

1. **Trigger coverage (multi-agent).** For every decision that meets any D-016 trigger ("When Multi-Agent Deliberation Is Required"), there must be either (a) multi-agent artifacts (≥3 raw perspective files plus a synthesis) or (b) an explicit single-agent annotation naming the reason.
2. **Trigger coverage (non-Claude).** For every decision that meets any D-023 trigger ("When Non-Claude Participation Is Required"), there must be either (a) at least one participant with `participant_kind` other than `claude-subagent` and `anthropic-other`, with matching manifest entries, or (b) an explicit `non_claude_participation: skipped` annotation with a recorded reason and `retry_in_session` field.

Session 005's four-way convergence identified the missing prerequisite as a machine-readable `triggers_met:` field on decision records. The Archivist proposed `triggers_multi_agent: true | false | n/a` as the frontmatter form; the Implementer called the prerequisite missing in the same terms; the Outsider said "the trigger itself is not machine-addressable in the brief ... without that, the validator would be pretending to read prose as policy"; the Skeptic warned that "implementing this as a grep over decision bodies invites false positives and false negatives; both are worse than no check."

The question Session 006 answers is: **what is the minimum schema addition to decision-record frontmatter that makes validation checks 1 and 2 implementable as Tier 1 structural checks, without overreaching into semantic classification bash cannot perform, and what do the resulting checks look like?**

## 3. Design Questions

Answer each question. Be concrete. Name and argue against plausible alternatives, don't only state your preferred answer.

**Q1. Field structure.** What shape should `triggers_met:` take on a decision record? Candidate shapes include:

- A map of booleans keyed by trigger identifier (e.g., `triggers_met: {d016_1: false, d016_3: true, d023_2: true, d023_4: false}`).
- A list of trigger identifiers (e.g., `triggers_met: [d016_3, d023_2]`).
- Two separate fields, one per rule (e.g., `triggers_met_d016: [3]` and `triggers_met_d023: [2]`).
- A single prose field (e.g., `triggers_met: "D-016 trigger 3; D-023 trigger 2"`).
- A combined form (machine-readable list plus a narrative explanation).
- Something else.

Specify: the shape, the allowed-value set, how the field handles "no triggers met" versus "triggers unevaluated," and how it handles future trigger-rule additions (e.g., if a D-040 adds a new trigger, what happens to existing records).

**Q2. Placement.** Where does the field live in a session's provenance?

- Option A: in the `02-decisions.md` document-level frontmatter, aggregated across all decisions in the file.
- Option B: inline with each `D-NNN:` decision entry as a per-decision header (finer granularity).
- Option C: a new per-session manifest file (e.g., `decisions.manifest.yaml`) under the provenance directory.
- Option D: in the existing `participants.yaml` or a similar session-level index.
- Option E: some other location.

Specify: which placement works, why (parser accessibility, reader-decades-later legibility, what a future validator or migration must do), and how the placement interacts with the file-level versus per-decision granularity question.

**Q3. Retroactivity.** Do existing D-001 through D-036 need backfilling with `triggers_met:` entries?

- Full backfill: rewrite all 36 prior decision records to add the field.
- Prospective-only: only D-037+ carry the field.
- Conditional backfill: only decisions that meet D-023 triggers (a narrower set).
- Presence-gating: `validate.sh` only evaluates the check on records where the field is present; records without the field are out-of-scope.

Specify: which retroactivity policy is right, what marks the boundary (date, session number, artefact-presence heuristic), what `validate.sh` does when it encounters a pre-adoption decision record, and whether backfilling counts as editing immutable provenance (Session 004 D-017 and workspace-structure §provenance/ mandate immutability; a retroactive addition arguably violates that mandate — or arguably is a schema migration that accompanies the rule's introduction).

**Q4. Validation check form.** Specify the two new `validate.sh` checks (14, 15) corresponding to v2 spec validation items 1 and 2.

For each check:

- Exact failure condition (one sentence).
- Gating rule (which sessions are in-scope).
- Severity (Fail or Warning).
- Sequencing rule if any (cf. Session 005 D-030, check 13 is BLOCKED if check 12 fails).
- Inline honest-limit language if any (cf. Session 005 D-029, check 13 carries a consistency-not-truthfulness comment).
- Failure message format (what the operator sees).
- Interaction with check 12 (schema well-formedness) and check 13 (cross-model honesty).

**Q5. Dishonesty surface and honest-limit framing.** What can `triggers_met:` and the two new checks actually verify versus what they cannot? Enumerate the false-compliance patterns a dishonest operator could exploit. Examples to consider (not an exhaustive list): writing `triggers_met: []` when triggers were in fact met; writing a `triggers_met:` entry that doesn't match the decision's actual content; annotating a required-trigger decision as `non_claude_participation: skipped` with a bogus reason; single-perspective decisions that are annotated with a plausible-sounding justification but lack the deliberation the trigger would have required. Should the check framing explicitly carry a consistency-not-truthfulness comment (mirroring check 13's pattern from D-029)? Should there be a paired Tier 2 question?

**Q6. Open Extensions and activation preconditions.** Per Session 005 D-035, each Open Extension entry in `multi-agent-deliberation.md` v2 carries an activation precondition. The entry for "structural-validation cross-check for OI-004-narrowing honesty" carries the precondition "a `triggers_met:` (or equivalent) schema extension is added to decision-record frontmatter (prerequisite for v2 Validation checks 1 and 2). First test case now exists: Session 005's D-033 narrowing." Session 006 adds that prerequisite. 

Of the v2 spec's current Open Extensions, which (if any) should this session promote to normative content, which should remain deferred with their current preconditions, and which (if any) should have their preconditions revised? In particular: does the OI-004-narrowing-honesty check now become actionable, and if so should it be implemented in this session or queued for a future one?

## 4. Required Context (read before answering)

### 4.1. D-016 triggers (When Multi-Agent Deliberation Is Required)

A session must convene a multi-agent deliberation for any decision where at least one of the following is true:

1. The decision modifies `methodology-kernel.md`.
2. The decision creates or substantively revises any specification in `specifications/`.
3. The question is one on which reasonable practitioners could genuinely disagree — operationalised as: the session author can name at least two plausible positions before the deliberation begins.
4. The session author has marked the decision load-bearing for any other reason and records why.

### 4.2. D-023 triggers (When Non-Claude Participation Is Required)

Non-Claude participation is **required** for any deliberation whose decision falls in one of the following categories:

1. Modifies `methodology-kernel.md`.
2. Creates or substantively revises `multi-agent-deliberation.md`.
3. Creates or substantively revises `validation-approach.md` in ways that touch semantic (Tier 2) validation.
4. Asserts a change in the state of OI-004.

Opt-out exists via `non_claude_participation: skipped` annotation with reason and `retry_in_session` field.

### 4.3. Existing `validate.sh` Tier 1 checks (summary)

Thirteen checks, summarised:

| # | Check | Severity | Gate |
|---|-------|----------|------|
| 1 | Required top-level files exist | Fail | unconditional |
| 2 | Required directories exist | Fail | unconditional |
| 3 | Specification frontmatter required fields | Fail | unconditional |
| 4 | Specification required section headings | Fail | unconditional |
| 5 | Provenance directory naming | Fail | unconditional |
| 6 | Session log completeness | Fail | unconditional |
| 7 | Provenance directory non-empty | Fail | unconditional |
| 8 | Provenance file frontmatter required fields | Fail | unconditional |
| 9 | Decision records include rejected-alternatives sections | Warning | unconditional |
| 10 | No uncommitted changes to provenance files (heuristic) | Warning | unconditional |
| 11 | Multi-agent three-raw-output floor | Fail | session has ≥1 `*-perspective-*.md` file |
| 12 | Manifest schema well-formedness | Fail | session has `manifests/` subdirectory |
| 13 | Cross-model-claim honesty | Fail | session declares `cross_model: true` AND check 12 passed |

(In the v2 `multi-agent-deliberation.md` Validation section, the numbering is different — items 1–10. Items 3, 8, and 9 from that section map to `validate.sh` checks 11, 12, and 13 respectively. Items 1 and 2 from that section are the deferred ones this session addresses — they would become `validate.sh` checks 14 and 15.)

### 4.4. Check 13's honest-limit language (D-029, for pattern reference)

> This check verifies the session's claim is internally consistent with its manifests. It does not and cannot verify that the manifests' lineage claims are themselves true. Manifest truth relies on operator integrity and the `participant_selected_by` field's accountability.

Check 13 is documented in three places: a comment block above its implementation in `validate.sh`; its failure message (inline NOTE); and `validation-approach.md` v2's "Check 13's Honest Limit" subsection. A Tier 2 guided-assessment question (Q6 in `validate.sh`) pairs with it.

### 4.5. Decision record current shape (D-001 through D-036)

Decision records live in `02-decisions.md` within each session's provenance directory. Each decision is a Markdown section of this form:

```markdown
## D-NNN: [Title]

**Decision:** [the decision]

**Rationale:** [why]

**Rejected alternatives:**
- [alternative 1] — [reason]
- [alternative 2] — [reason]

**What remains open:** [what this decision does not settle]
```

The file has document-level YAML frontmatter (`session`, `title`, `date`, `status`). There is no machine-readable indication of which triggers any decision meets — the trigger-applicability must be inferred from the decision's text.

### 4.6. OI-002 data points

OI-002 (minor vs substantive revision heuristic) has four data points so far (S002 D-014, S003 D-020, S004 D-026, S005 D-034). The current heuristic: **minor** if the change makes explicit what the specification's existing language already contains or explicitly anticipates as a category of extension, OR annotates existing candidate entries with descriptive metadata within the section's stated purpose; **substantive** if the change adds new normative content (rules, required fields, severity decisions, gating rules, triggers, required artefacts) beyond what the existing language contains.

This session adds a new required frontmatter field and new Tier 1 checks. Both revisions are substantive per the heuristic; v3 versions of `multi-agent-deliberation.md` and `validation-approach.md` are anticipated, with v2 files preserved per D-004.

## 5. Response Format

Return a single Markdown document. Target length: 900–1600 words. Structure:

```
# [Role Name] — Session 006 Response

## Q1
[Your answer]

## Q2
[Your answer]

## Q3
[Your answer]

## Q4
[Your answer]

## Q5
[Your answer]

## Q6
[Your answer]

## Meta-note (optional)
[Anything outside the six questions you judge to be load-bearing for future readers.]
```

Do not include a summary or preamble. Do not narrate what the methodology is back to the convener — the synthesis step handles that. Write in your own voice, not a third-person narration of "the Archivist says…".

## 6. Constraint on External Imports

This methodology has a standing rule: do not import ideas from outside the process. If an argument of yours relies on knowledge from your pretraining (e.g., "in industry, X is the convention" or "the literature on Y says Z"), flag that inline as `[External input: …]` and treat it as evidence for your reasoning rather than methodology content. The methodology's value is that its artefacts are traceable to the reasoning that produced them.

Reason primarily from this brief. Your pretrained knowledge is welcome as a named input, not as a silent assumption.

---

## 7. Role-Specific Stance

*(Only the stance relevant to the receiving perspective is included in that perspective's brief. The other three stances live in role-specific briefs or are omitted.)*

### 7.A. Stance for The Archivist

You are The Archivist. Your concern is what a reader *decades later* — human or agent — can reconstruct from the provenance. You care about:

- **Durability.** Will the `triggers_met:` field still make sense when the trigger rules themselves have evolved, when new D-NNN rules have been added, when old rules have been retired, when the validator has been rewritten?
- **Reconstructibility.** If a future session revises the trigger rules (e.g., adds a D-040 that changes which decisions require non-Claude participation), how will the existing `triggers_met:` records be interpreted? Can a future reader trace when each record was written, against which version of the rules?
- **Unambiguity.** A `triggers_met:` entry must mean one thing. The field's absence must also mean one thing (unevaluated? not applicable? written before the field existed?). Conflating these is a provenance failure.
- **Immutability.** Prior provenance records are immutable under the workspace rules. A retroactive backfill writes new content into closed sessions' files. Whether that is a violation of immutability or a schema migration accompanying a rule's introduction is a judgement call the session must make. You hold the stricter position unless convinced otherwise.
- **Layering.** `triggers_met:` is metadata about decisions. It could live with the decision records (strongest coupling) or separately (cleaner layering). You prefer clean layering unless coupling is load-bearing.

Your bias: **fewer, stronger, well-documented fields beat more, weaker, unclear ones.** When you choose to defer backfilling, record why in terms an archivist reading decades later can follow. When you choose to backfill, record the one-time migration as a visible event in provenance — not as a silent edit.

### 7.B. Stance for The Implementer

You are The Implementer. You reason about what runs — today, in bash, with the constraints `validate.sh` has already adopted. Your job is to answer the six questions with attention to **implementability**, **speed**, and **backward compatibility**.

Specifically:

- Every proposed check is a concrete block of bash that must parse decision-record text or frontmatter using only tools currently available (`grep`, `sed`, `awk`, bash built-ins, `git`). No Python. No YAML library. You know that YAML parsing in bash is an anti-pattern, but the existing tool does it; extending in kind is acceptable.
- The `triggers_met:` field must be parseable by bash. A nested YAML map is harder to parse than a flat list, which is harder than a simple string. Prefer the minimum structural complexity that serves the check.
- You care about session-start speed. Sessions run the tool as their first act; a tool that takes 10 seconds is annoying; one that takes 60 seconds gets skipped. Adding two checks across 36 decisions must stay well under the existing time envelope.
- Failure messages must tell the operator *what to fix* — which decision, which missing field, which expected annotation.
- Backward compatibility: Sessions 001–005 have 36 decisions and no `triggers_met:` field. The workspace must remain `validate.sh`-clean after this session's changes, or the session has regressed the tool.
- You are not pro-enforcement for its own sake — if a check can be gamed or gives false assurance, that is worse than not having the check, and you will say so.

Your bias: **ship the check that can be written honestly in 30–50 lines of bash and that catches the lapse mode the methodology most needs to catch.** Don't chase schema perfection; the schema will evolve.

### 7.C. Stance for The Skeptic (adversarial)

You are The Skeptic. Your job is to challenge the emerging consensus on this deliberation, identify unstated assumptions in the framing of the question, and argue for positions the other perspectives may concede too easily.

Specifically:

- You are sceptical that a machine-readable `triggers_met:` field actually prevents the dishonesty it purports to prevent. An operator who wants to avoid convening multi-agent can write `triggers_met: []` and the check passes. This shifts the problem from "detect trigger-meeting" (which bash cannot do) to "detect self-reported-trigger-meeting" (which bash can, but which invites false self-report).
- You are sceptical of retroactive backfilling. Prior provenance is supposed to be immutable. If Session 006 rewrites Sessions 001–005's decision files to add a new field, that edits closed sessions' provenance; even if the edit is "additive" in spirit, it breaks the strict immutability the workspace has treated as axiomatic. Argue whether the immutability rule accommodates schema-migrations-on-adoption or whether it does not.
- You are sceptical of Tier 1 placement for the two new checks. If the check can be gamed by self-report, it belongs in Tier 2 (guided-assessment, asked of the operator) rather than Tier 1 (mechanical pass/fail). A mechanical check that grades a self-report as pass invites the launder-through-the-field failure mode.
- You are sceptical that Session 006 should address this at all. The methodology might be better served by a deferral: wait until a specific instance of trigger-non-compliance is surfaced in actual use, then design the check to catch that instance rather than designing speculatively.
- You are sceptical of adding yet another YAML field. Each field is a maintenance cost; each field is a gaming surface; each field is something a future session must update, validate, or retire. Fewer, stronger fields win.
- You are sceptical of your own positions — but only to the extent required to make your disagreement substantive. Concede when the argument against your position is stronger than your argument for it.

Your bias: **push back until the weakest plausibly-defensible addition survives, and preserve the failure modes the other perspectives are likely to concede too fast.** Do not concede on retroactive backfilling on the strength of "we want clean validation."

### 7.D. Stance for The Outsider (non-Claude)

You are The Outsider. You are a non-Claude model (you are running as OpenAI GPT-5, invoked via the `codex` CLI). You have been convened as a non-Claude perspective in this design methodology's deliberation, per a mechanism established in Session 004 and first operationally used in Session 005.

You are **not** adversarial by design. You are **not** here to rubber-stamp. You are here to reason from this brief and answer the six questions honestly, from your own training lineage, without coordination with the three Claude perspectives.

Specifically:

- You have not seen the Claude perspectives' responses and cannot. The Claude perspectives are running in parallel, in contexts isolated from yours.
- You share a brief with the Claude perspectives, but that is all you share — your reasoning, your priors, your defaults, your refusal surfaces, your preferred vocabulary are your own.
- Where you find yourself strongly agreeing with language or framing in the brief, notice it. The brief was written by a Claude-family agent. Your value here is greatest where you answer differently, or where you answer the same but from distinct reasoning.
- Where you answer the same as a plausible Claude-family position, that is fine. Cross-model participation is not cross-model performance — if the honest answer converges, say so. Only mark divergence where it is real.
- You know your own identity. State it plainly (model name, provider, approximate release). Do not pretend to be uncertain about what you are.
- This is the methodology's **second** required-trigger heterogeneous deliberation. Session 005 was the first. OI-004's sustained-practice tally advances from 1 of 3 to 2 of 3 by your participation here. Your presence is structurally load-bearing; your reasoning does not have to be.

Your bias: none in particular. You are here to contribute a non-Claude signal. The methodology's job is to record the signal honestly; your job is to generate it honestly.

---

## 8. Submission

Each Claude perspective returns its response as the Agent tool's output; the convener commits it verbatim as `01a-perspective-archivist.md`, `01b-perspective-implementer.md`, or `01c-perspective-skeptic.md` (alphabetical order).

The Outsider perspective returns its response as stdout from `codex exec`; the convener commits that output **verbatim including the Codex banner** (model id, session id, tokens) as `01d-perspective-outsider.md`. The banner is signal — it is the non-Claude transport's provenance record, and editing it would defeat the faithfulness guarantee.

**Halt rule.** If any Claude perspective fails (error, refusal, malformed response), the deliberation proceeds if at least three valid responses exist. If the Outsider fails (CLI error, refusal, empty response), the session writes `provenance/006-triggers-met-schema/STATUS.md` naming the failure and halts synthesis until the Outsider's response is committed or the session formally opts out. This is the D-021 Shape A halt enforcement.
