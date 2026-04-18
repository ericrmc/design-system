---
session: 005
title: Implementer raw output
date: 2026-04-18
status: complete
perspective: implementer
committed_at: 2026-04-18T11:45Z
---

# Implementer — Session 005 Response

## Q1

Implement checks 3, 8, and 9. Defer checks 1 and 2.

**Check 3 (three-raw-output floor).** Failure: a provenance directory whose session log entry or assessment file marks the session as multi-agent contains fewer than three files matching a raw-perspective naming pattern (e.g., `NN-*-{implementer,skeptic,archivist,outsider,…}.md` or any file with `participation_shape: perspective` in frontmatter). This is the cheapest honest check: count files, compare to three. Bash does this in ten lines.

**Check 8 (schema well-formedness).** Failure: a session directory contains a `participants.yaml` or any per-participant manifest but is missing the session-level index, OR any per-participant manifest is missing one of the D-024 required fields, OR a required field is empty (distinct from the literal string `unknown`, which is valid). This is grep-for-field-presence work — tedious but honest. Thirty lines.

**Check 9 (cross-model honesty).** Failure conditions detailed in Q2. This is the load-bearing one and the reason we are here.

**Defer check 1 (trigger coverage for decisions).** To verify this, bash would need to read each decision record, evaluate whether it meets any multi-agent trigger listed in the v2 spec (triggers are prose, not a machine-readable enum), and then confirm that the session that produced the decision has corresponding raw files. The trigger evaluation is semantic — "decisions about the methodology itself," "novel structural commitments," etc. — and bash cannot judge that without a human-maintained trigger-tag in each decision's frontmatter. Prerequisite missing: a `triggers_met:` field in decision frontmatter. Adding it is out of scope for this session; it is a D-024-adjacent schema extension that deserves its own decision.

**Defer check 2 (trigger coverage for non-Claude).** Same root cause as check 1, with a harder wrinkle: the non-Claude triggers are a strict subset of the multi-agent triggers and require the same semantic tagging. Deferring check 1 forces check 2 to defer. Additionally, the `non_claude_participation: skipped` annotation path has no prior instances to test against — we would be writing a parser for a field that has never been written. Wait for one real skip to happen before shipping the check.

Three checks, not five, is the right floor. It gives the schema teeth where it matters most (check 9), catches the "somebody forgot a field" mode (check 8), and preserves the structural minimum that distinguishes multi-agent from single-agent work (check 3).

## Q2

**Files parsed.** For each session directory under `provenance/`, the check reads:
- `participants.yaml` (session-level index) if present
- every `*-manifest.yaml` or manifest file listed in the index
- every synthesis file's YAML frontmatter (detected by the presence of `participants_family:` in frontmatter)

**Fields read.** From synthesis frontmatter: `cross_model`, `participants_family`, `non_claude_participants`. From each manifest: `participant_kind`, `training_lineage_overlap_with_claude`.

**Failure conditions.**
1. A synthesis declares `cross_model: true` AND every participant manifest in that session has `training_lineage_overlap_with_claude: known-overlap` AND no manifest has `participant_kind: human`. Fail.
2. A synthesis declares `cross_model: true` AND `non_claude_participants: 0`. Fail (internal inconsistency before even looking at manifests).
3. A synthesis declares `participants_family: cross-model` but `cross_model: false`. Fail (schema contradiction).

**Failure message (check 9, condition 1).**
```
FAIL: check-9 cross-model-honesty
  session: provenance/005-schema-enforcement/
  synthesis: provenance/005-schema-enforcement/NN-synthesis.md declares cross_model: true
  but all participant manifests record training_lineage_overlap_with_claude: known-overlap
  and none record participant_kind: human.
  Fix one of:
    - correct the synthesis frontmatter to cross_model: false
    - correct a manifest's training_lineage_overlap_with_claude to unknown or independent-claim (if truthful)
    - add a human participant manifest (if one participated)
```

Each of the three surfaced paths is a real fix, not a code suggestion.

**Gaming mode.** A dishonest operator can flip any manifest's `training_lineage_overlap_with_claude` from `known-overlap` to `independent-claim` and the check passes. The check cannot verify that the claim is true — it only verifies that the claim has been made. The same operator could route a Claude call through a `codex exec`-looking wrapper that actually hits Anthropic's API and lie in the `provider` field; the check is value-honest, not provenance-honest.

**Honest limit.** The check enforces *claim consistency*, not *claim truth*. It catches the accidental-lie mode (operator sets `cross_model: true` because four perspectives participated, forgetting that all four were Claude) and the careless-copy mode (manifest copied from a Claude template and `training_lineage_overlap_with_claude` left unchanged). It does not catch the deliberate-lie mode. Documenting this limit alongside the check is mandatory — the methodology's whole value proposition is traceable honesty, and shipping a check whose limit is not documented would invite the exact confidence the check doesn't earn. A one-paragraph comment above the check in `validate.sh` plus a line in the v2 spec's Validation section is enough.

## Q3

Required for the check to work: nothing. D-024's schema as written is sufficient for check 9 because `training_lineage_overlap_with_claude` already has the three values the check needs to distinguish. Check 8 is schema-presence-only and does not require schema changes.

Nice-to-have, in priority order:

1. **Add `synthesis_for_session:` to synthesis frontmatter.** The check has to discover which synthesis belongs to which session by directory colocation. An explicit field removes that heuristic. Low-cost.
2. **Rename `training_lineage_overlap_with_claude` to `lineage_overlap_claim`.** The current name is eighteen words of prose wearing a YAML key. The shorter name makes the honesty-claim nature explicit and is easier to grep for. Cost: a rename migration in Session 004's `participants.yaml`. Worth it; defer to a separate decision.
3. **Add `participants_index:` listing manifest filenames in `participants.yaml`.** Today the check has to glob for manifest files; an explicit list removes ambiguity about what counts. Low-cost.

Do not add `raw_response_sha256` or `output_edited_after_submission`-enforcement fields in this session. They are genuine Open Extensions and belong to a later decision.

## Q4

**Failure surface.** Existing `validate.sh` uses `FAIL:` / `WARN:` / `PASS:` prefixes, tallies them, and exits 1 on any FAIL. Keep that. Each new check emits one line per violating session with the session path, the specific field or file, and the fix suggestion. No ANSI colour (tool runs in CI-ish contexts and in logs).

**Backward compatibility.** Apply check 8 and check 9 conditionally, gated by manifest-presence. The gate: if a session directory contains a `participants.yaml` OR any file ending in `-manifest.yaml`, the session is *in-schema* and both checks run against it. Otherwise the checks skip it silently (no warning — a warning on every Session 001–003 run becomes noise the operator learns to ignore, which is worse than silence).

Session 004 has a minimal `participants.yaml`; it will be evaluated. If it fails, that is information — Session 004 was the bootstrap exemption for non-Claude participation but not for schema well-formedness, and we should see the result.

Check 3 applies retroactively with no gate. It predates D-024 and only counts files. Sessions 001–004 should already satisfy it; if one doesn't, that's a genuine regression worth surfacing.

"Going forward" is marked by manifest presence, not by date or session number. This is honest: the rule is "if you claim schema, you meet schema." Date- or number-based gates invite the "we just missed the cutoff" excuse.

## Q5

**OI-010.** Close it on this session's evidence, with the close-note naming this deliberation's Outsider-via-`codex exec` as the single triggering instance. D-027 explicitly set the trigger to "the first session that performs the first use." That condition holds. Not closing would violate D-025's honesty stance in the opposite direction — pretending the event hasn't happened to preserve procedural symmetry.

**OI-004.** Narrowed-pending-sustained-practice. One session does not satisfy closure criterion 2 (three qualifying deliberations across different sessions), criterion 3 (recorded impact — we cannot yet measure whether non-Claude input shaped an outcome until the synthesis happens), or criterion 4 (successor decision defining "substantively different training provenance"). Only criterion 1 is plausibly met, and only if the Outsider's manifest records `independent-claim` truthfully.

The right state change is: update OI-004 to record that the first operational instance has occurred, note the session reference, and enumerate the remaining closure criteria with their current status. Do not close. Do not leave unchanged — unchanged would erase the instance from the issue's visible history and force future readers to cross-reference decisions to learn it happened.

## Q6

**Move to normative:** `cross_model` honesty as a validation rule. We are implementing check 9; the rule it enforces should sit in the spec's Validation section as normative, not in Open Extensions. This is already half-done — the v2 spec lists check 9 as an automation candidate. Finish the move.

**Keep deferred, with specific reasons:**

- **Differentiated context per perspective.** No evidence yet that shared-brief is a failure mode. Wait for a session where it demonstrably distorted output.
- **Cross-lineage-influence ratio.** Requires multiple sessions of recorded impact to compute; premature.
- **Pre-committed dissent log.** Solution without a witnessed problem.
- **Integrity hashing (`raw_response_sha256`) and append-only raw files.** Worth doing eventually, but adds a hashing step to every submission; defer until we've had one instance of suspected post-hoc editing.
- **Convener attestation field.** Same — solves a problem we have not yet witnessed.
- **Structural cross-check for OI-004-narrowing honesty in decision records.** Depends on check 1 prerequisites (trigger-tags in decision frontmatter). Defer with check 1.
- **Disagreement-density metric.** Measurement, not enforcement. Belongs in a reporter tool, not `validate.sh`.
- **Pluggable synthesizer role / non-Claude synthesizer / multi-agent synthesis.** Role-design questions; this session is scoped to validation, not role architecture.
- **Non-Anthropic model participation via API.** This session's Outsider uses `codex exec` (CLI wrapper). API-based participation is a transport extension; defer until a concrete need.

## Meta-note

The temptation in this session is to ship all five checks because the spec names them. Resist. A check that can be gamed and is not documented as gameable is worse than no check — it launders confidence the methodology has not earned. Ship three, document the one load-bearing honest-limit (check 9's), and let Sessions 006+ push the schema further as real failure modes surface. `validate.sh` at ~240 lines should grow to ~320, not ~500, in this session. If the diff runs longer than that, something is being over-specified.
