---
session: 130
title: temporal-claim-grounding — deliberation
generated_by: selvedge export
---

# Deliberation

## D-16 — Grounding discipline for temporal claims in submit bodies

sealed_at: 2026-04-29T21:53:20.471Z

### P-1 (anthropic)

**Position.** Apply ground-or-omit to all submit bodies as a hard rule, locating the discipline in prompt-development 8.5 only.

**position.**
- Narrative-driven number-fitting is a general failure mode that can land anywhere prose lives in the substrate.
- The audits one-row finding is a sample-size argument, not a scope argument, so restricting to engine_feedback would miscalibrate.
- Decision supports, alternative rejection reasons, assessment.state, and close summaries are equally porous prose surfaces.
**risk.**
- An unverified-estimate tag normalises uncalibrated numbers and preserves the rhetorical slot where fabrication lives with a fig leaf.
**position.**
- If a duration claim is load-bearing the cheap substrate query takes seconds; if it is not load-bearing it should be omitted.
- Methodology spec should stay small and stable; it describes nine activities, not authoring discipline for one submit kind.
**risk.**
- Duplicating the rule into methodology adds surface without capability and risks future drift between two copies of the same rule.
- The rule is broad relative to a one-row failure and could chill useful approximate temporal language if mis-scoped.
**position.**
- Ground-or-omit is permissive about omission: authors are not forced to include durations, only forbidden from fabricating them.
**what_not.**
- Discipline should not include programmatic citation requirements like queried-at timestamp decoration that invite theatre without grounding.
- Discipline should not require retroactive sweep of pre-S130 rows since bounded contamination is already calibrated.
- Discipline should not include confidence taxonomies or unverified tagging because they preserve the failure surface.
- Discipline should not include substrate-side enforcement; EF-S127-1 named freeform body_md as impractical for static checks.
**migration_path.**
- If contamination recurs after the discipline lands, escalate to the typed sidecar or to a close-time lint as a middle option.
**position.**
- Do not pre-commit to a close-time lint now; the discipline plus operator catch is the cheapest sufficient response.

### P-2 (openai)

**Position.** Apply ground-or-omit to all submit bodies as a hard rule, locating the discipline in both prompt-development 8.5 and the methodology spec.

**position.**
- The substrate premise applies to every row that can later be treated as provenance, not only engine_feedback.
- Assessments, close summaries, decision supports, and EFs can all smuggle narrative-shaped temporal claims into the record.
**risk.**
- Unverified-estimate is better than pretending but still creates a weak provenance object in a system whose value depends on reliable rows.
**position.**
- If the duration is not worth checking against substrate timestamps, it is not worth recording at all.
- Methodology spec answers why temporal provenance matters; prompt-development 8.5 answers how the rule is performed.
- Two-location placement of the rule makes the discipline robust to prompt rewrites.
**risk.**
- Broadening a one-row failure into a system-wide rule adds friction and may make authors avoid useful temporal context.
**position.**
- The rule targets explicit durations, elapsed-time claims, recency claims, and sequence claims used as evidence.
- The rule does not require every row to contain timestamps; only that any temporal claim be read off substrate data.
**what_not.**
- Discipline should not include a full temporal-claim schema yet, nor mandatory citations for every sentence.
- Discipline should not include retroactive re-audits beyond the bounded contamination check or elaborate confidence taxonomies.
- Discipline should not punish approximate human-facing language outside submit bodies.
**risk.**
- The risk to avoid is turning a clean provenance rule into bureaucratic ceremony.
**cli_surface.**
- Add a close-time lint that scans submit bodies for temporal phrases like gap, after, since, months, hours, recent, earlier, elapsed.
- The lint forces an explicit confirm-or-delete step before commit, catching the rhetorical slot where fabrication occurred.
**migration_path.**
- The lint is a small CLI addition, not a schema change, so it does not collide with the operators deferral of the typed sidecar.

### Synthesis

P-1 (anthropic) and P-2 (openai) converge on Q1 (apply to all submit bodies) and Q2 (hard ground-or-omit rule, no unverified-tag escape). They diverge on Q3 (locus) and on whether to take a structural step now. P-1 places the clause only in prompt-development 8.5, arguing methodology should stay small-and-stable and that duplication invites drift; the discipline is procedural-how, not kernel-why. P-2 wants both placements, treating temporal-provenance as kernel-why warranted in methodology. P-2 also proposes a lightweight close-time lint scanning submit bodies for temporal phrases as a structural alternative short of the deferred typed sidecar; P-1 declines structural moves at one-row contamination and escalates only on recurrence. Adopted synthesis: take both convergences (all submits, hard rule); resolve Q3 in favour of P-1 (prompt-development 8.5 only) on small-kernel grounds; defer P-2 lint as conditional follow-up open-issue triggered by recurrence rather than committing now.

### Synthesis points

- **convergence C-1.** Both perspectives converge: discipline applies to all submit bodies that admit free-text prose, not engine_feedback only.
- **convergence C-2.** Both perspectives converge: hard rule ground-or-omit; no unverified-estimate escape valve, since the rhetorical slot is the failure surface.
- **divergence D-1.** P-1 places clause only in prompt-development 8.5; P-2 places it in both prompt-development 8.5 and methodology spec.
- **divergence D-2.** P-2 proposes close-time lint structural alternative short of typed sidecar; P-1 declines structural moves at one-row contamination, escalates only on recurrence.
- **minority M-1.** P-2 minority view: temporal-provenance is kernel-level warranted in methodology, not only procedural in prompt-development.
