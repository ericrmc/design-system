---
session: 006
title: Raw Perspective — Archivist
date: 2026-04-19
status: complete
perspective: archivist
committed_at: 2026-04-19
---

# The Archivist — Session 006 Response

## Q1

The shape must survive the trigger rules themselves changing. A map of booleans keyed by current trigger identifier (`{d016_1: false, d016_3: true, ...}`) couples the record permanently to the rule set in force when it was written; if D-016 later reorders or retires triggers, every old record either silently lies or requires backfilling. The single-prose field is legible now but opaque to bash and ambiguous to future parsers. Two separate fields bifurcate what is logically one concept (which triggers fired). A pure list loses the distinction between "evaluated and empty" and "unevaluated."

I choose the **combined form: a machine-readable list of stable trigger identifiers plus a narrative `triggers_rationale` prose field**, with an explicit enumeration for the empty case.

Concretely, per decision:

```yaml
triggers_met:
  multi_agent: [D-016.2, D-016.3]   # or: none | unevaluated
  non_claude:  [D-023.2]            # or: none | unevaluated
triggers_rationale: "Substantively revises multi-agent-deliberation.md (D-016.2, D-023.2); reasonable practitioners could disagree on field shape (D-016.3)."
triggers_ruleset: "D-016@S004, D-023@S005"
```

Allowed-value set: each list element is a dotted identifier `D-NNN.K` where N is the decision number that defined the trigger rule and K is the ordinal of the clause within that rule as originally numbered. The tokens `none` and `unevaluated` are reserved and mutually exclusive with any list content. `none` means "author evaluated and no triggers fired"; `unevaluated` means "field present for schema reasons, author did not classify" (this is a Warning, not a Fail, for reasons in Q4).

The `triggers_ruleset` field pins the version of the rule set the author was reasoning against. If a future D-040 adds a trigger, old records remain valid because they reference the ruleset that existed at their writing. New records written after D-040 include `D-040.K` tokens as appropriate and bump their `triggers_ruleset` stamp. No retroactive rewrite is implied: a future reader seeing `triggers_ruleset: "D-016@S004, D-023@S005"` understands the record was evaluated before D-040 existed, and can look up what the rules were at that time.

Rejected alternatives: the map-of-booleans (brittle under rule evolution, forces either lies or rewrites when triggers retire); pure prose (unparseable); separate `triggers_met_d016` / `triggers_met_d023` (splits a unified concept and doesn't generalise to D-040). A combined form preserves both machine-readability and the narrative a decades-later reader needs to understand what the author thought they were doing.

## Q2

**Option B: inline with each `D-NNN:` decision entry as per-decision frontmatter**, expressed as a fenced YAML block immediately following the `## D-NNN:` heading and preceding the `**Decision:**` line.

The aggregation question (document-level vs per-decision) resolves in favour of per-decision because the field is fundamentally about a specific decision's classification. A document-level map (`decisions: {D-037: {triggers_met: ...}, D-038: {...}}`) works for a bash parser but is a provenance hazard: it physically separates the classification from the text it classifies, making silent drift between the two possible and likely. A decades-later reader opening `02-decisions.md` and reading `D-037` linearly should see the trigger classification adjacent to the reasoning it applies to.

Option C (separate `decisions.manifest.yaml`) is worse on the same grounds plus it creates a new file type for every session; Option D (participants.yaml) conflates decision-provenance with participant-provenance, which are orthogonal axes.

Per-decision inline requires the bash validator to do light structural parsing: find each `## D-NNN:` heading and look for a YAML fence in the following lines until the next heading or the `**Decision:**` marker. This is well-scoped and checkable — it's the same class of parsing check 12 already does against manifest files. The failure mode (fence missing, malformed) becomes check 14's Fail condition.

The placement choice forces a corresponding update to the decision-record template shown in §4.5 of the brief; Session 006's Produce activity must emit v3 of that template.

## Q3

I hold the strict position: **prospective-only, with the migration itself recorded as a visible event**.

Full backfill rewrites 36 closed-session files. D-017 and workspace-structure §provenance treat those files as immutable. A migration argument can be made — "the schema changed, and records must reflect the new schema" — but that argument proves too much: any future schema addition could retroactively invalidate all prior records, and provenance becomes a rolling edit rather than a durable trail. The archivist's position is that the correct response to schema evolution is *to date-stamp the schema*, not to rewrite history to pretend the old records always had the new shape.

Conditional backfill (only D-023-relevant decisions) has the same immutability problem on a smaller surface and adds a judgement call about which old decisions qualify — exactly the semantic classification the brief says bash cannot honestly perform.

The mechanism: Session 006 records D-NNN "adopt `triggers_met:` schema, effective S006+". `validate.sh` check 14 and 15 are gated on `session_number >= 6`. For sessions 001–005, the checks are skipped with an explanatory inline comment; the log line reads "check 14: SKIP (pre-adoption, S001–S005)". The gating rule is a numeric comparison against a constant defined near the top of the script so a decades-later reader can see `readonly TRIGGERS_MET_ADOPTION_SESSION=6` and understand the history in one line.

Presence-gating (evaluate only records where the field is present) is tempting but fails on unambiguity: a field's absence then means either "pre-adoption" or "author forgot," and the validator can't distinguish. Explicit numeric gating keeps absence unambiguous: in pre-adoption sessions, absence is expected; in post-adoption sessions, absence is a Fail.

If a future session's authors believe backfill is essential — for example, to run a cross-historical audit — the correct path is a new session that proposes backfill as its own decision with its own deliberation, preserves v1 of each affected file before the edit (per D-004 supersession mechanics), and stamps the migration prominently. This session should not quietly do that work as a side effect.

## Q4

**Check 14: Multi-agent trigger coverage.**

- Failure condition: Post-adoption decision record lacks per-decision `triggers_met:` block, or block is malformed YAML, or `multi_agent` list is non-empty and non-`none` but session has fewer than three `*-perspective-*.md` raw outputs and lacks a `single_agent_reason` annotation field on the decision.
- Gating: session number >= 6 AND session has at least one decision record (`D-NNN:` heading).
- Severity: Fail for missing/malformed block; Fail for trigger-fires-but-no-artefact-and-no-annotation; Warning for `unevaluated` value.
- Sequencing: BLOCKED if check 12 (manifest well-formedness) fails on any manifest, because the three-raw-output floor (check 11) depends on artefacts check 14 also references.
- Failure message: `FAIL [check 14]: D-NNN in session S0NN declares triggers_met.multi_agent=[D-016.3] but session has 1 perspective file and no single_agent_reason annotation. Either add raw-perspective outputs or annotate with reason (D-016 trigger 3 applies; see multi-agent-deliberation.md §When Required).`
- Honest-limit inline comment: `# NOTE: This check verifies structural consistency between declared triggers and session artefacts. It does not verify that the declaration itself is honest — whether the author correctly classified their decision against D-016 is a Tier 2 judgement.`

**Check 15: Non-Claude trigger coverage.**

- Failure condition: Post-adoption decision record has non-empty `triggers_met.non_claude` list AND session manifests lack a participant with `participant_kind` other than `claude-subagent`/`anthropic-other` AND there is no `non_claude_participation: skipped` annotation with both `reason` and `retry_in_session` fields populated.
- Gating: session number >= 6 AND check 12 passed.
- Severity: Fail.
- Sequencing: BLOCKED if check 12 fails. Independent of check 14 — a decision can fail 15 while passing 14.
- Failure message: `FAIL [check 15]: D-NNN declares triggers_met.non_claude=[D-023.2] but no non-Claude participant appears in session manifests and no non_claude_participation:skipped annotation present. Either include a non-Claude participant per D-023 or record an explicit skip with reason and retry_in_session.`
- Honest-limit inline comment: same structural-not-semantic framing as check 13 and check 14.

Checks 14 and 15 reinforce — not replicate — check 13. Check 13 asks "if you claimed cross-model, did you in fact run cross-model?" Check 14/15 ask "given the decision's declared trigger coverage, do the artefacts match?" They are orthogonal consistency checks.

## Q5

The exploitable false-compliance surface, enumerated:

1. **Under-declaration.** Author writes `triggers_met.multi_agent: none` when a trigger in fact applied. Validator cannot detect this without semantic classification.
2. **Over-declaration.** Author writes `triggers_met.non_claude: [D-023.2]` then annotates `non_claude_participation: skipped` with a vacuous reason ("not available") — producing a formally-compliant record that defeats the rule's purpose.
3. **Mismatched rationale.** `triggers_met` list says D-016.3, `triggers_rationale` prose says something unrelated. Both parse; the inconsistency is semantic.
4. **Bogus `retry_in_session`.** Skip annotation cites `retry_in_session: S099` with no intention of following through; the deferral is a Tier 1 timestamp, not a Tier 1 commitment.
5. **Ruleset-stamp gaming.** Author pins `triggers_ruleset: D-016@S001` to invoke an earlier version of the rules that didn't cover the decision.

Every one of these is a Tier 2 concern. The check framing must carry an honest-limit comment in the exact register of D-029: "This check verifies that the record's declared triggers are structurally consistent with the session's artefacts. It does not verify that the declaration itself is a truthful classification of the decision against D-016 and D-023." Place this in three locations per the check-13 precedent: a comment block above the implementation, the failure message's NOTE line, and a subsection of `validation-approach.md` v3.

A paired Tier 2 question is required. Proposed Q7 and Q8 for `validate.sh` Tier 2:

- Q7: "For each decision in this session, does the declared `triggers_met` classification match your own reading of D-016 and D-023 against the decision's content?"
- Q8: "For any `non_claude_participation: skipped` annotation, is the stated reason substantive and the `retry_in_session` commitment credible?"

## Q6

The v2 spec's Open Extensions include the "structural-validation cross-check for OI-004-narrowing honesty" whose precondition this session satisfies. I recommend **promoting it to normative but deferring implementation to Session 007**. Rationale: Session 006 is already substantively revising two specs and adding a new frontmatter schema plus two validator checks. Session 005's D-033 narrowing gives us exactly one test case, which is enough to design against but thin to validate against — a second data point in Session 007 or later would harden the check. The promotion is a schedule commitment; the implementation is the next session's Produce activity.

Other Open Extensions in v2 should retain their current preconditions unless this brief's Section 4 demonstrates they are now unblocked; I see no evidence of that. Do not revise preconditions merely because the session is open and could.

## Meta-note

One durability concern worth flagging: the dotted-identifier scheme `D-NNN.K` depends on D-016 and D-023's internal clause numbering being stable. If a future session renumbers clauses within D-016 (adds "0. preamble trigger" shifting the rest), every extant `triggers_met` token points to the wrong clause. The ruleset-stamp field partially mitigates this (a reader can look up what D-016.3 meant "@S005") but the mitigation is a lookup, not a self-contained record. An alternative is to give each trigger clause a permanent sub-identifier on first introduction (`D-016 trigger "kernel-modification"`) rather than a positional one. I raise it here for the synthesist's consideration without taking a position — the brief asks for `triggers_met:` shape, and I have given my answer; the clause-identifier-stability question is a separate issue that Session 007 or later should address, possibly as a new open issue OI-012.
