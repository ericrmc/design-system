---
session: 005
title: Archivist raw output
date: 2026-04-18
status: complete
perspective: archivist
committed_at: 2026-04-18T11:45Z
---

# Archivist — Session 005 Response

## Q1

Implement checks 3 and 8. Defer 1, 2, and 9.

**Check 3 — three-raw-output floor.** Failure: a session directory whose `00-assessment.md` or session-log entry marks the deliberation as multi-agent contains fewer than three files matching a raw-perspective naming pattern. Bash can count files honestly; the semantics are stable across schema drift because "three files exist" will mean the same thing to a reader in 2056 as it does now.

**Check 8 — schema well-formedness.** Failure: a session whose `00-assessment.md` declares heterogeneous participation is missing either the session-level `participants.yaml` index, any per-participant manifest referenced by that index, or any required field from D-024's schema on any manifest. Bash can verify presence of files and presence of field keys. Note this is presence, not value-correctness — the check succeeds if a field literally contains the string `unknown`, because D-024 explicitly admits `unknown` as a truthful value.

**Defer check 1 (trigger coverage for multi-agent).** The triggers in the v2 spec are semantic ("decisions that materially shape the methodology itself", etc.). Bash cannot classify a decision record as trigger-meeting without a human or model judgment. What's missing is a machine-readable trigger annotation on decision records — e.g., a frontmatter field `triggers_multi_agent: true | false | n/a`. Until that field exists and is required, this check can only produce false positives or silent passes. Prerequisite: a schema decision in a future session adding the trigger annotation.

**Defer check 2 (trigger coverage for non-Claude).** Same structural problem as check 1, plus the additional difficulty that the non-Claude triggers are even more semantic ("decisions that depend on assumptions Claude-family models share"). Bash cannot detect assumption-sharing. Prerequisite: same trigger-annotation field, plus explicit operator declaration per decision.

**Defer check 9 (cross-model-claim honesty).** See Q2 — I believe this check should be written, but not in Session 005 and not in bash without a schema amendment first. Deferring it here is a recorded choice, not an omission.

## Q2

If check 9 were implemented in Session 005, it would parse the session-level `participants.yaml` (for the `cross_model` flag) and every per-participant manifest in the same session directory (for `training_lineage_overlap_with_claude` and `participant_kind`). Failure condition: `participants.yaml` has `cross_model: true` AND every manifest has `training_lineage_overlap_with_claude: known-overlap` AND no manifest has `participant_kind: human`. Failure message: `Session NNN claims cross_model: true but no participant manifest records lineage other than known-overlap or kind human. See specifications/multi-agent-deliberation.md §Cross-Model-Claim Honesty.`

**Gaming mode.** An operator can pass this check while lying by setting one manifest's `training_lineage_overlap_with_claude` to `independent-claim` or `unknown` when it is in fact `known-overlap`. The value is a claim, not a measurement. The check verifies that the claim is internally consistent; it does not verify that the claim is true. A bash tool has no route to the ground truth of a model's training corpus.

**Honest limit.** The check enforces *consistency of self-report*, not *truthfulness of self-report*. A reader decades later must be able to tell this apart. If the check is ever added, its documentation must say so in the same file as the check, not in a separate spec a future archivist might lose. The phrase I would record verbatim: "This check verifies the session's claim is internally consistent with its manifests. It does not and cannot verify that the manifests' lineage claims are themselves true. Manifest truth relies on operator integrity and the `participant_selected_by` field's accountability."

**Why defer to a later session.** Check 9 is load-bearing enough that its first implementation should itself be a multi-agent, cross-model deliberation — the check that most matters for honesty should not be authored under the Claude monoculture failure mode it exists to detect. Session 005 is the first cross-model session; using that first-use to decide *which* checks to add is appropriate, but the check most sensitive to cross-model reasoning deserves its own session with the non-Claude participation it will police.

## Q3

**Required for check 8 to work.** No schema changes. D-024 is sufficient as written.

**Required for check 9 to work (when implemented).** One rename and one clarification. Rename `participants_family` to a machine-friendly enum location — either keep it in `participants.yaml` frontmatter or move it, but pick one and record that choice in a decision. Currently Section 4.3 says "synthesis frontmatter composition fields" — a check needs to know which file to parse. Clarification: `training_lineage_overlap_with_claude` values should be documented as *claims*, not measurements, in D-024 itself, so the manifest schema carries its own epistemic status.

**Nice-to-have.** A `raw_response_sha256` field on manifests (currently deferred in Open Extensions) would let a future reader verify the raw output wasn't edited post-hoc. Not required for any Tier 1 check in Session 005, but its absence narrows what any future integrity check can do.

**Not needed.** No new fields for check 3 or check 8. The existing schema carries enough.

## Q4

**Surface.** Use the same format as existing Tier 1 checks: one line per failure, prefixed with `FAIL:` and the session/file path. Exit 1 on any Tier 1 failure, 0 otherwise — unchanged from current behavior. Do not introduce a new severity level; the existing fail/warning split is adequate and a reader in 2056 will not thank us for a three-level system whose boundaries they must reconstruct.

**Backward compatibility.** Check 8 applies only to sessions whose `00-assessment.md` declares heterogeneous participation. Sessions 001–003 declared no such thing and will not be examined by the check. Session 004 was the bootstrap-exemption session and per the brief has only a minimal `participants.yaml` — check 8 should skip it via an explicit exemption list in the check itself, not via a date or session-number threshold.

**Why an exemption list beats a threshold.** A date or session number is a detached fact a future archivist must cross-reference. An exemption list inside `validate.sh` names the exempted sessions verbatim and will survive any rewrite that preserves the check's intent. When Session 004's provenance is read in 2056, the exemption is visible in the same tool that would otherwise fail it. Record the exemption reason inline in the script as a comment pointing to D-027 (bootstrap exemption). This is the archivist's preferred form: the check carries its own history.

Check 3 applies going forward only, marked by the presence of a `multi-agent: true` declaration in `00-assessment.md`. No retroactive failure of Sessions 001–003, which did not claim multi-agent at all.

## Q5

**OI-010.** Close now. Per D-027 the trigger was "first session that performs the first use" and this session is it. The closure record should cite this deliberation's Outsider delivery via `codex exec` and name the manifest that documents it. Closing OI-010 here is a provenance act, not a celebration — a future reader needs to know the rule moved from conditional to active on this date.

**OI-004.** Narrow, do not close. The v2 spec's four closure criteria require sustained practice (criterion 2: "at least three required-trigger deliberations across different sessions"), which one session cannot satisfy. Per D-025's honesty stance, claiming closure on single-session evidence would be the exact dishonesty D-025 forbids. Narrow OI-004 to a state that records: (a) one qualifying session has occurred; (b) remaining criteria are 2, 3, and 4; (c) the next checkpoint is after the second and third qualifying sessions. I would call this state `narrowed-pending-sustained-practice` — the name itself tells a future reader what's still outstanding without requiring them to read the closure criteria.

## Q6

**Move to normative.** None. Session 005's output is two new Tier 1 checks and possibly a schema clarification; none of the Open Extensions become *required* as a consequence. Promoting any of them absent a deliberation specifically about that extension would be gold-plating.

**Keep deferred, with updated reasons.**

- *Integrity hashing (`raw_response_sha256`) and append-only raw files.* Deferred; becomes a prerequisite for any future check-9 integrity dimension. Record this link in the Open Extensions entry so a future session knows why it matters.
- *Convener attestation field.* Deferred; becomes relevant when check 9 is implemented, since the attestation is what operator-integrity gaming-mode depends on. Link these two in the spec.
- *Structural-validation cross-check for OI-004-narrowing honesty in decision records.* Deferred but closer to the surface: this session is the first to narrow OI-004, so the honesty cross-check now has a concrete first instance to test against. Note in the Open Extensions entry that Session 005 provides the first test case.
- *Pre-committed dissent log, disagreement-density metric, differentiated context per perspective, cross-lineage-influence ratio, pluggable synthesizer, non-Claude synthesizer, multi-agent synthesis, non-Anthropic model participation via API.* All deferred; none touched by Session 005's scope.

## Meta-note

Two things for the future reader.

First, the choice to defer check 9 in this session is the archivally interesting decision here. A skeptic-shaped reader will correctly note that the load-bearing check is the one being deferred. The reason deserves to be recorded in the decision record in one sentence the reader can find without context: *the check most designed to police cross-model honesty should not be authored in the session where cross-model participation was first operationalized — it should be authored in a later session where cross-model reasoning is no longer novel.* If a future session disagrees and implements check 9 sooner, that disagreement should cite this reasoning and name why it no longer applies.

Second, the exemption-list approach in Q4 is a general archivist pattern worth naming: *keep the history of a rule inside the artifact that enforces the rule.* Scattering rule-history across dated thresholds, external spec sections, and session logs creates reconstruction debt. A comment in `validate.sh` pointing to D-027 costs nothing now and saves a decade-later reader a half-hour archaeology session.
