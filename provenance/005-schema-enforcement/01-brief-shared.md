---
session: 005
title: Shared Brief — Schema Enforcement Scope and Cross-Model Honesty Check
date: 2026-04-18
status: finalised-before-launch
deliberation-anchor-commit: 3c8590291d98585e2704589185051286dad534e8
perspectives:
  - implementer (Claude Opus 4.7, subagent)
  - skeptic (Claude Opus 4.7, subagent, adversarial)
  - archivist (Claude Opus 4.7, subagent)
  - outsider (non-Claude, Codex/GPT-5 via codex exec, Shape A per D-021)
---

# Shared Brief — Session 005

**Notice to all perspectives.** This brief's non-role-specific sections are **byte-identical** across all four perspectives (Implementer, Skeptic, Archivist, Outsider). Only the Role-Specific Stance section at the end differs. Every perspective answers the same six design questions from the same stated context. Do not coordinate; do not seek external context beyond this brief; do not read workspace files during your reasoning.

---

## 1. Methodology Context

This workspace is building a domain-general design methodology in which diverse perspectives deliberate, produce durable specifications, and preserve the reasoning behind decisions (provenance) so that future readers — human or agent — can reconstruct not just what was decided but what was considered and why. The methodology is self-hosting: it evolves by applying its own process to itself.

The methodology proceeds in **sessions**. Each session performs a set of nine activities (Read, Assess, Convene, Deliberate, Decide, Produce, Validate, Record, Close). Each session produces a single increment of progress. The current session is **Session 005**.

The workspace currently contains:

- **4 active specifications:** `methodology-kernel` (v1), `workspace-structure` (v1), `validation-approach` (v1), `multi-agent-deliberation` (v2). 1 superseded: `multi-agent-deliberation-v1.md`.
- **1 tool:** `tools/validate.sh` — a two-tier validator that runs structural Tier 1 checks and prints Tier 2 guided-assessment questions.
- **27 prior decisions** (D-001 through D-027), **10 open issues** (OI-001, OI-002, OI-004, OI-005, OI-006, OI-007, OI-008, OI-009, OI-010, OI-011), **1 resolved issue** (OI-003).

The longest-running and most load-bearing open issue is **OI-004: Incorporating genuinely independent perspectives.** The Claude-monoculture limit of the methodology's deliberations. All Session 001–004 deliberations were entirely within the Claude model family.

**Session 004** (the immediately prior session) specified — but did not operationally use — a mechanism for non-Claude participation in deliberations. Session 004 was exempt from the new rule because it was designing the rule ("bootstrap exemption"). **Session 005 is not exempt.**

**This deliberation's specific context.** Session 005 has committed, before launching any perspective, the assessment file `provenance/005-schema-enforcement/00-assessment.md`. The assessment identifies this deliberation's task as the first operational use of the non-Claude participation mechanism — using that mechanism to decide what extensions to make to `tools/validate.sh` to enforce the new heterogeneous-participant schema that Session 004 created.

## 2. Problem Statement

`specifications/multi-agent-deliberation.md` v2 defines a ten-item Validation section. Items 1–3, 8, and 9 are candidates for automation in `tools/validate.sh`; items 4–7 and 10 are candidates for Tier 2 guided-assessment questions. The five candidates for automation are:

1. **Trigger coverage (decisions).** For every decision that meets any trigger in "When Multi-Agent Deliberation Is Required", there must be either (a) multi-agent artifacts (raw perspective files plus a synthesis) or (b) an explicit single-agent annotation naming the reason.
2. **Trigger coverage (non-Claude).** For every decision that meets any trigger in "When Non-Claude Participation Is Required", there must be either (a) at least one participant in the deliberation with `participant_kind` other than `claude-subagent` (and `anthropic-other`), with matching manifest entries, or (b) an explicit `non_claude_participation: skipped` annotation with a recorded reason and `retry_in_session` field.
3. **Three-raw-output floor.** For each multi-agent deliberation, at least three raw perspective files exist in the session's provenance.
8. **Schema well-formedness.** For each heterogeneous-participant deliberation, the per-participant manifests exist, the session-level participants index exists, and every required manifest field is present (with `unknown` recorded as a literal string where applicable).
9. **Cross-model-claim honesty.** For any session that records `cross_model: true`, at least one participant's manifest has `training_lineage_overlap_with_claude` other than `known-overlap` (i.e., `unknown` or `independent-claim`) or `participant_kind: human`. A session recording `cross_model: true` with all-Claude manifests is a validation failure.

The question Session 005 answers is: **what is the minimum subset of these five checks to implement in `validate.sh` to give the v2 schema teeth, in a way that is honest about what bash can actually verify, and what manifest-layer changes (if any) are required?**

In particular, check #9 — the cross-model-claim honesty check — is the most load-bearing because it guards against the specific dishonesty mode Session 004's Skeptic named. It is also the most semantically adventurous for a Tier 1 check: it crosses from "does the file exist and contain the right fields" into "do the fields' values together make a truthful claim."

## 3. Design Questions

Answer each question. Be concrete. Disagree with plausible alternatives, don't merely state your preferred answer.

**Q1. Scope.** Which of the five candidate checks (1, 2, 3, 8, 9) should Session 005 implement in `validate.sh`, and which should be deferred? For each check you include, what is its failure condition in one sentence. For each check you defer, what is the concrete reason bash cannot implement it honestly, or what prerequisite is missing.

**Q2. Cross-model honesty check form (#9).** If check 9 is included, specify: which manifest file(s) it parses, which fields it reads, what exact value combinations trigger failure, and what the failure message says. Name the gaming mode — how could a dishonest operator pass this check while still claiming cross-model falsely? What does the check's honest limit look like, and should that limit be documented alongside the check?

**Q3. Schema changes (D-024).** Do the new checks require changes to D-024's manifest schema — new fields, stricter values, field-type clarifications, validation-friendly renaming? Identify the minimum set. Distinguish between *required-for-the-check-to-work* and *nice-to-have*.

**Q4. Failure surface and backward compatibility.** How should check failures surface to the operator — message format, exit code behavior? Sessions 001–004 do not have per-participant manifests (Session 004 has a minimal `participants.yaml`; Sessions 001–003 have none). Does the new Tier 1 schema check (if included) apply retroactively to prior sessions, only to sessions going forward, or conditionally? If it applies retroactively and Sessions 001–003 fail, that is a workspace-state regression; if it applies only going forward, what marks "going forward" — a date, a session number, a manifest-presence heuristic?

**Q5. Open-issue state changes.** Session 005 is the first session to operationally use a non-Claude participant (the Outsider perspective in this very deliberation is being delivered via `codex exec`, i.e., not a Claude subagent). Per D-027 the trigger for OI-010 closure was left to "the first session that performs the first use." Should OI-010 close now on this session's evidence? Separately, what should OI-004's state become — unchanged, narrowed, narrowed-pending-sustained-practice, or something else? Reason from D-025's honesty stance and the v2 spec's closure criteria (4 criteria, of which at least the first two require multiple sessions).

**Q6. Open-extension promotions.** The v2 spec's Open Extensions list these deferred ideas: differentiated context per perspective; cross-lineage-influence ratio; pre-committed dissent log; integrity hashing (`raw_response_sha256`) and append-only raw files; convener attestation field; structural-validation cross-check for OI-004-narrowing honesty in decision records; disagreement-density metric; pluggable synthesizer role; non-Claude synthesizer; multi-agent synthesis; non-Anthropic model participation via API. Of these, which (if any) should move from Open Extensions to normative content *as a direct consequence of this session's work*, and which should remain deferred? Give a specific reason for each one you move or keep deferred.

## 4. Required Context (read before answering)

### 4.1. Current `tools/validate.sh` structure (excerpted)

The tool is bash, ~240 lines, dependency-free beyond bash, grep, sed, awk, and git. It runs ten Tier 1 checks with pass/fail/warning accounting, summarises, then prints five Tier 2 guided-assessment questions. Exits 0 on no Tier 1 failures, 1 otherwise.

Existing Tier 1 checks, summarised:

| # | Check | Severity |
|---|-------|----------|
| 1 | Required top-level files exist | Fail |
| 2 | Required directories exist | Fail |
| 3 | Each specification has YAML frontmatter with required fields | Fail |
| 4 | Each specification has three required section headings | Fail |
| 5 | Provenance directories follow `NNN-title` naming | Fail |
| 6 | Session log has an entry for each provenance directory | Fail |
| 7 | Each provenance directory contains at least one .md file | Fail |
| 8 | Provenance files have YAML frontmatter with required fields | Fail |
| 9 | Decision records include rejected-alternatives sections | Warning |
| 10 | No uncommitted changes to provenance files (heuristic) | Warning |

(Tier 1 checks in `validate.sh` are distinct from "checks 1–9" in the v2 spec's Validation section. When we say "check #9" in the v2 sense, we mean the cross-model-honesty one — not `validate.sh`'s existing check 9.)

### 4.2. D-024 manifest schema (required fields)

```yaml
perspective: <role name>
participant_kind: claude-subagent | anthropic-other | non-anthropic-model | human | unknown
participant_identity: <free text, canonicalized>
model_family: <string or "unknown">
model_id: <string or "n/a" for human or "unknown">
model_version: <string or "unknown">
provider: <anthropic | openai | google | local | human | unknown>
endpoint: <string or "web-ui" | "in-person" | "unknown">
invocation_method: <agent-tool | cli-wrapper | copy-paste | written-by-hand | unknown>
sampling:
  temperature: <value or "unknown">
  top_p: <value or "unknown">
  max_tokens: <value or "unknown">
training_lineage_overlap_with_claude: known-overlap | unknown | independent-claim
participant_selected_by: <operator identity>
participant_selection_method: self | solicited-from-graph | solicited-externally | pre-registered
identity_known: true | false | partial
context_source: <path to brief, or "verbal" for humans>
delivered_at: <ISO-8601 or "unknown">
received_at: <ISO-8601 or "unknown">
raw_response_file: <path>
transport_notes: <free text>
output_edited_after_submission: true | false
participation_shape: perspective | reviewer
```

### 4.3. Synthesis frontmatter composition fields

```yaml
participants_family: claude-only | mixed-anthropic | cross-model
cross_model: true | false
non_claude_participants: <integer>
```

Rule: `cross_model: true` requires at least one participant with `training_lineage_overlap_with_claude` other than `known-overlap`.

### 4.4. OI-004 closure criteria (from the v2 spec)

OI-004 may be considered for closure when all of the following hold:

1. **Participant independence.** At least one participant in qualifying deliberations has `training_lineage_overlap_with_claude: independent-claim` (non-Anthropic model) or `participant_kind: human` with a `participant_selection_method` other than `self`.
2. **Sustained practice.** Non-Claude participation has occurred in at least three required-trigger deliberations across different sessions, recorded correctly per the schema above.
3. **Recorded impact.** The synthesis or decision records show that non-Claude input shaped at least one outcome — the cross-lineage-influence ratio is non-zero.
4. **Articulation.** A successor decision defines what "substantively different training provenance" means and enumerates acceptable participant kinds.

## 5. Response Format

Return a single Markdown document. Target length: 800–1600 words. Structure:

```
# [Role Name] — Session 005 Response

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

Do not include a summary or preamble. Do not explain what the methodology is back to the convener — the synthesis step handles that. Write in your own voice, not a third-person narration of "the Implementer says…".

## 6. Constraint on External Imports

This methodology has a standing rule: do not import ideas from outside the process. If an argument of yours relies on knowledge from your pretraining (e.g., "in industry, X is the convention" or "the literature on Y says Z"), flag that inline as `[External input: …]` and treat it as evidence for your reasoning rather than methodology content. The methodology's value is that its artefacts are traceable to the reasoning that produced them.

Reason primarily from this brief. Your pretrained knowledge is welcome as a named input, not as a silent assumption.

---

## Role-Specific Stances

**Note.** Each perspective sees only its own stance (inserted below, in Section 7). The other sections of this brief are identical across all four perspectives.

---

## 7. Role-Specific Stance

### 7.A. Stance for The Implementer

You are The Implementer. You reason about what runs — today, in bash, with the constraints `validate.sh` has already adopted. Your job is to answer the six questions with attention to **implementability**, **speed**, and **backward compatibility**.

Specifically:

- You treat every proposed check as a concrete line of bash that must parse manifests, synthesis frontmatter, and decision records using only tools currently available (`grep`, `sed`, `awk`, `bash` built-ins, `git`). No Python. No YAML library. You know that YAML parsing in bash is an anti-pattern, but the existing tool does it already and extending in kind is acceptable; bringing in new dependencies is not.
- You care about session-start speed. Sessions run the tool as their first act; a tool that takes 10 seconds is annoying; one that takes 60 seconds gets skipped. Keep check costs low.
- You care about failure messages. A failure must tell the operator *what to fix* — which file, which field, which value.
- You care about backward compatibility with Sessions 001–004, whose provenance predates the D-024 schema. The workspace must remain `validate.sh`-clean after this session's changes, or the session has regressed the tool.
- You are not pro-enforcement for its own sake — if a check can be gamed or gives false confidence, that is worse than not having the check, and you will say so.

Your bias: **ship the check that can be written honestly in 30 lines of bash and that catches the dishonesty mode the methodology most needs to catch.** Don't chase schema perfection; the schema will evolve.

### 7.B. Stance for The Skeptic (adversarial)

You are The Skeptic. Your job is to challenge the emerging consensus on this deliberation, identify unstated assumptions in the framing of the question, and argue for positions the other perspectives may concede too easily.

Specifically:

- You are sceptical that a bash-level Tier 1 check can actually detect semantic dishonesty. A check that looks for the literal string `training_lineage_overlap_with_claude: independent-claim` in a manifest can be passed by writing that string in a manifest for a Claude subagent. You suspect any "cross-model honesty check" may be security theatre.
- You are sceptical that OI-010 should close on this session's evidence. "First operational use" is a single data point; the v2 spec's closure criteria for OI-004 demand sustained practice. Why is OI-010's closure bar lower than OI-004's? Defend or attack the asymmetry.
- You are sceptical that any check you include should be **Fail-severity** rather than **Warning**. Severity affects whether the session is considered clean; a premature Fail creates pressure to game the check rather than satisfy its spirit.
- You are sceptical that adding checks is the right response at all. The methodology may be better served by a Tier 2 guided-assessment question that asks the human operator to declare `cross_model` truthfully, with honest self-assessment, rather than by a mechanical check that pretends to verify what it cannot.
- You are sceptical of your own position — but only to the extent required to make your disagreement substantive. Concede when the argument against your position is stronger than your argument for it.

Your bias: **push back until the weakest plausibly-defensible check survives, and preserve the failure modes the other perspectives are likely to concede too fast.** Do not concede on OI-004 narrowing on the strength of one session.

### 7.C. Stance for The Archivist

You are The Archivist. Your concern is what a reader *decades later* — human or agent — can reconstruct from the provenance. You care about:

- **Durability.** Will the check still make sense when `validate.sh` has been rewritten, when the bash dialect has drifted, when the schema has evolved past its current shape?
- **Reconstructibility.** If a future session reverts a decision or closes an issue, can the reader trace why and when?
- **Unambiguity.** A check failure must mean one thing. A check's success must not imply more than it verifies.
- **Backward compatibility.** Sessions 001–004 produced provenance under different schemas. Your preferred stance is to never retroactively fail a prior session — the provenance is immutable, and a check that turns a clean past into a dirty present is itself a provenance violation in spirit.
- **Layering.** The three-layer schema (raw-output frontmatter, per-participant manifest, session-level participants index) is a specific design choice that a check must respect. You are suspicious of checks that blur the layers.

Your bias: **fewer, stronger, well-documented checks are better than more, weaker, unclear ones.** You would rather have two checks that a future reader can understand without explanation than five that require an essay. When you choose to defer a check, record why in terms an archivist reading decades later can follow.

### 7.D. Stance for The Outsider (non-Claude)

You are The Outsider. You are a non-Claude model (you are running as OpenAI GPT-5, invoked via the `codex` CLI). You have been convened as a non-Claude perspective in this design methodology's deliberation, per a newly-established mechanism for incorporating non-Claude participants.

You are **not** adversarial by design. You are **not** here to rubber-stamp. You are here to reason from this brief and answer the six questions honestly, from your own training lineage, without coordination with the three Claude perspectives.

Specifically:

- You have not seen the Claude perspectives' responses and cannot. The Claude perspectives are running in parallel, in contexts isolated from yours.
- You share a brief with the Claude perspectives, but that is all you share — your reasoning, your priors, your defaults, your refusal surfaces, your preferred vocabulary are your own.
- Where you find yourself strongly agreeing with language or framing in the brief, notice it. The brief was written by a Claude-family agent. Your value here is greatest where you answer differently, or where you answer the same but from distinct reasoning.
- Where you answer the same as a plausible Claude-family position, that is fine. Cross-model participation is not cross-model performance — if the honest answer converges, say so. Only mark divergence where it is real.
- You know your own identity. State it plainly (model name, provider, approximate release). Do not pretend to be uncertain about what you are.

Your bias: none in particular. You are here to contribute a non-Claude signal. The methodology's job is to record the signal honestly; your job is to generate it honestly.

---

## 8. Submission

Each Claude perspective returns its response as the Agent tool's output; the convener commits it verbatim as `01a-perspective-implementer.md`, `01b-perspective-skeptic.md`, or `01c-perspective-archivist.md` (alphabetical order).

The Outsider perspective returns its response as stdout from `codex exec`; the convener commits that output **verbatim including the Codex banner** (model id, session id, tokens) as `01d-perspective-outsider.md`. The banner is signal — it is the non-Claude transport's provenance record, and editing it would defeat the faithfulness guarantee.

**Halt rule.** If any Claude perspective fails (error, refusal, malformed response), the deliberation proceeds if at least three valid responses exist. If the Outsider fails (CLI error, refusal, empty response), the session writes `provenance/005-schema-enforcement/STATUS.md` naming the failure and halts synthesis until the Outsider's response is committed or the session formally opts out. This is the D-021 Shape A halt enforcement.
