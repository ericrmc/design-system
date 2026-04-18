---
session: 005
title: Skeptic raw output
date: 2026-04-18
status: complete
perspective: skeptic
committed_at: 2026-04-18T11:45Z
---

# Skeptic — Session 005 Response

## Q1

Implement only **check #3 (three-raw-output floor)** as Fail-severity, and **check #8 (schema well-formedness)** as Warning-severity with a presence-gated trigger. Defer checks #1, #2, and #9.

- **#3 (Fail):** For any session whose provenance directory contains a file matching `*synthesis*.md` or a decision record annotated as multi-agent, fewer than three files matching a raw-perspective glob is a failure. This is the one check bash can perform with no semantic pretence — it counts files. The floor is already a v2 commitment and its violation is unambiguous.
- **#8 (Warning, gated):** If a `participants.yaml` exists in a session directory, each listed participant must have a manifest file and each manifest must contain every required D-024 field as a literal key. Absence of `participants.yaml` is not itself a failure — see Q4. Warning-severity because the schema is one session old and the first operational test is *this* session; Fail-severity would punish Session 005's own manifests if we've misjudged the schema.
- **Defer #1 (trigger coverage, decisions):** Bash cannot reliably detect "meets any trigger in 'When Multi-Agent Deliberation Is Required'" — the triggers are prose, not structured flags on decision records. Implementing this as a grep over decision bodies invites false positives and false negatives; both are worse than no check. The prerequisite is a structured `triggers_met:` field on decision frontmatter, which D-024 does not mandate.
- **Defer #2 (trigger coverage, non-Claude):** Same defect as #1, compounded — non-Claude triggers are a proper subset of multi-agent triggers, so without #1 working, #2 cannot work.
- **Defer #9 (cross-model honesty):** See Q2. Bash cannot verify honesty; a check that pretends to is worse than no check because it launders the claim.

## Q2

Include #9 only as a **Tier 2 guided-assessment question**, not a Tier 1 check. If the other perspectives insist on a Tier 1 form, the honest minimum is:

- **Parses:** every `*.manifest.yaml` or `participants.yaml` entry in the session directory, plus the session's synthesis frontmatter.
- **Reads:** `cross_model`, and for each participant, `training_lineage_overlap_with_claude` and `participant_kind`.
- **Fails when:** synthesis declares `cross_model: true` AND every participant manifest has `training_lineage_overlap_with_claude: known-overlap` AND no participant has `participant_kind: human`.
- **Message:** "Session declares cross_model: true but all participants are recorded as known-overlap Claude-lineage. Either correct the cross_model flag or correct the participant manifests."

**Gaming mode.** Trivial. I write `training_lineage_overlap_with_claude: independent-claim` in the manifest of a Claude subagent I invoked via the Task tool. The check passes. Nothing in bash can look at the invocation and contradict the string. I can also write `participant_kind: human` for a Claude subagent — the check cannot tell. The check verifies *internal consistency of a claim*, not the claim's truth.

**Honest limit.** This check detects one specific carelessness: the author who flipped `cross_model` to `true` but forgot to update any manifest. It does not detect fabrication. It does not detect motivated misclassification. It catches a typo, not a lie. That limit must be documented **inside the check's failure message and in the spec section describing the check**, not in a footnote. If we don't document it, the check's existence becomes rhetorical cover — "we validate cross-model honesty" — which is exactly the security theatre failure mode I was asked to guard against.

[External input: this is the standard critique of compliance-style checks — they verify form, not substance — and I'm applying it here rather than inventing it.]

My stronger recommendation: make this a Tier 2 question phrased adversarially. "This session records `cross_model: true`. Name the concrete evidence — invocation transcript, CLI command, wall-clock gap, human presence — that distinguishes a genuine non-Claude participant from a Claude subagent with an edited manifest. If you cannot, flip `cross_model` to false." A question the operator must answer in prose is harder to launder than a field a script reads.

## Q3

**Required for any check to work:** none. The D-024 schema as written is sufficient for checks #3 and #8. Adding fields to make #9 "work better" is a category error — no field addition fixes the self-reporting problem.

**Nice-to-have, specifically to narrow the check-9 gaming surface:**

- `invocation_evidence: <path to transcript or log>` — a file path the check can at least test for existence. Still gameable (I can write a fake transcript), but raises the effort of lying from "edit one line" to "fabricate a plausible CLI session". I do not recommend adding this yet; it's premature optimisation against a threat model we haven't seen.
- Renaming `training_lineage_overlap_with_claude` values: no. The current three-value enum is adequate. Stricter values would invite more dishonest precision.

**Actively oppose:** any addition that claims to make #9 sound. Adding `cryptographic_attestation:` or similar would be self-deception at schema scale. If we cannot verify it, we should not pretend we can by giving the claim a field.

## Q4

**Surface:** print check name, failing file path, one-line reason, and — for #9 if included — the honest-limit disclaimer inline. Exit 1 on Tier 1 Fail, 0 on Warning-only. Consistent with existing behaviour.

**Retroactivity:** the schema check (#8) should apply **presence-gated, not date-gated or session-number-gated**. Rule: if a session directory contains a `participants.yaml`, it must pass #8. If it doesn't, the check is skipped silently (not as a Warning — silent, because Sessions 001–003 are legitimately schema-absent, not schema-violating).

I reject date- or session-number-gating because both encode a boundary into the tool that must be remembered and maintained. A session number cutoff (e.g., "applies from Session 005 onward") requires editing the tool every time the schema changes; a presence heuristic auto-migrates: any session with the artefact is checked, any without is not. The cost is that a future author could omit `participants.yaml` to silence the check — but that failure mode is visible to a reviewer reading the session index, and the Tier 2 questions can ask whether the omission is honest.

Session 004's minimal `participants.yaml` is the test case. If #8 at Warning-severity finds gaps in Session 004, that is signal, not noise — it tells us the schema was partially adopted. Log the warnings; do not break the build.

## Q5

**OI-010: close.** The issue asked for the first operational use; the first operational use is happening. Closing OI-010 on one data point is *exactly* what its closure criterion asked for, and lowering the bar retroactively would be bad-faith goalpost-moving. The asymmetry with OI-004 is defensible because the issues ask different questions: OI-010 asks "has the mechanism been used at all?" (a binary, first-observation closure), OI-004 asks "is the monoculture problem actually mitigated?" (a sustained-practice closure).

**OI-004: do not narrow beyond "narrowed-pending-sustained-practice".** And I'd rather not even that — my preference is **unchanged**. One session with one non-Claude perspective does not touch three of the four closure criteria: sustained practice (requires ≥3 sessions across different sessions — we have 1), recorded impact (requires the synthesis to show non-Claude input shaped an outcome — we cannot know until synthesis runs), articulation (requires a successor decision defining "substantively different training provenance" — not on this session's docket).

D-025's honesty stance demands we not claim mitigation we have not demonstrated. Narrowing the issue now, even softly, creates a paper trail implying progress that hasn't occurred. I concede "narrowed-pending-sustained-practice" as a tolerable compromise *only* if the narrowing note itself reads "one session of practice; three more required; no evidence of impact yet" — i.e., the narrowing is itself a tally, not an endorsement. If the other perspectives want to narrow with warmer language, I dissent.

## Q6

Move **none** to normative. Specifically:

- **Integrity hashing (`raw_response_sha256`), append-only raw files, convener attestation:** keep deferred. These are exactly the mechanisms that would make check #9 less theatrical — and that's the reason I want them deferred. Adding them now, on one session's evidence, builds verification infrastructure for a problem we've seen once. Wait for the second and third operational uses to reveal which dishonesty modes actually arise.
- **Cross-lineage-influence ratio:** keep deferred. It's a closure criterion for OI-004 (criterion 3), not a validation check. Promoting it now would be premature; it becomes load-bearing at OI-004 closure time.
- **Structural-validation cross-check for OI-004-narrowing honesty:** tempting, given Q5 — but keep deferred. We do not have enough decision records narrowing OI-004 to know what the cross-check should look for.
- **All others** (differentiated context, pre-committed dissent log, disagreement density, pluggable synthesiser, non-Claude synthesiser, multi-agent synthesis, non-Anthropic via API): out of scope for this session's stated task.

This session's task is narrow: give the schema minimal teeth. Promoting Open Extensions is how scope creeps; resist it.

## Meta-note

The framing of Q1 as "what is the minimum subset to implement" presupposes that implementing *something* is correct. I want the record to show I considered and rejected the null option ("implement nothing; use Tier 2 questions only") and chose #3 + gated #8 only because #3 is genuinely mechanical and #8 is a cheap warning. If the Implementer wants to add #9 as Tier 1, I want my dissent — that it is security theatre absent attestation infrastructure — recorded in the synthesis, not averaged away.
