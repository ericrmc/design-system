---
session: 043
title: Shared brief for five-perspective Path PSD deliberation
date: 2026-04-24
status: brief-authored
---

# Shared Brief — Session 043 Path PSD Deliberation

This brief is read in common by all five perspectives. Each perspective additionally receives a role-specific prompt wrapper when convened. The brief is the **neutral ground**: shared question set, shared reading guidance, shared output format, shared reminders. Role-specific framing (what lens to apply) lives in the wrapper, not here.

## 1. What this deliberation is

The operator has surfaced a question at Session 043 open. The question is verbatim in `00-assessment.md` §2 of this session's provenance folder. In short: **six of the last ten sessions have been Path A (Watch); default-agent path recommendation produces Path A whenever no activation warrant fires; warrant-firing is sparse by design; the resulting observational sessions generate metrics that read as positive outcomes and confirm restraint as the right discipline; is there a structural gap in path selection that the current machinery doesn't surface, and if so, what should change?**

The operator has explicitly said this is **a question for the engine to deliberate, not a directive to implement**. The output may be a specification change, a new convention, a new open issue, or a reasoned rejection of the operator's framing. The operator is not pre-deciding the answer.

The assessment has identified this session as a substantive-revision candidate requiring multi-perspective deliberation per `multi-agent-deliberation.md` v4 §When Multi-Agent Deliberation Is Required, with cross-family participation. Closed-state OI-004 means `d023_4` does not fire; other MAD v4 clauses apply.

## 2. The question set (Q1–Q7)

Each perspective is asked to answer all seven questions to the extent its role allows. A perspective MAY decline to answer a question if the question is outside its role — declining explicitly is acceptable and preferable to answering out-of-role.

- **Q1.** Is warrant-firing genuinely sparse **by design**, or is it under-articulated? If by design, name the design intent. If under-articulated, name what is missing.
- **Q2.** Do observational-session metrics (no-growth streaks; preservation depths; zero-event watchpoint windows) constitute (a) evidence of discipline working, (b) evidence of discipline deferring, (c) neither, or (d) both simultaneously? Cite specific sessions if possible.
- **Q3.** Are there engine-internal work-shapes the current default-agent reasoning does not generate? Name them concretely. For each, state whether the absence is a defect, a feature, or indeterminate.
- **Q4.** Should default-agent path recommendation be required to surface non-Path-A alternatives **with evidence** (analogous to the Rejected-alternatives convention in decision records)? If yes, what form? If no, why not?
- **Q5.** Is a periodic self-audit at some cadence — reading further back than the `read-contract.md` §2c 6-session window — a net-positive mechanism or a laundering risk? If net-positive, what cadence and what scope? If laundering risk, what specifically makes it one?
- **Q6.** Does the §5.3 S041 strong-vindication (Session 041 is exactly the 20-successor-session "indefinitely movable finish line" pattern §5.3 warned against) imply any revision to the path-selection mechanism specifically, beyond the discharge already recorded? Or is discharge-as-vindicated complete closure?
- **Q7.** Overall verdict on the operator's framing: correct, partially correct (specify what is kept and what is adjusted), or wrong (specify where the reasoning breaks)?

## 3. Reading guidance

All perspectives are expected to read:

- `provenance/043-session-assessment/00-assessment.md` — this session's assessment including §2 operator framing verbatim.
- `specifications/methodology-kernel.md` (v6).
- `specifications/multi-agent-deliberation.md` (v4).
- `specifications/read-contract.md` (v4) — especially §2c close-rotation rule and §5.3 aggregate-hard-budget minority.
- `SESSION-LOG.md` full 42-row thin-index — the timeline of what has happened.
- `open-issues/index.md` — current issue surface.

Perspectives 3 (Long-Baseline Auditor) and 4 (Outsider) are additionally expected to read:

- `provenance/021-oi004-criterion4-articulation/03-close.md` — where §5.3 "indefinitely movable finish line" originated.
- `provenance/027-session-assessment/03-close.md` — where §5.2 was retroactively vindicated and §5.3 aggregate-hard-budget activation warrant first fired.
- `provenance/028-session-assessment/03-close.md` — where §5.3 was converted to specification and the Outsider "laundering the activation" critique landed.
- `provenance/036-session-assessment/03-close.md` — the one non-Path-A operator-surfaced-agenda session in the engine-v6+ window.
- `provenance/041-session-assessment/03-close.md` — where §5.3 was discharged-as-vindicated and §5.6 was preserved.
- `provenance/041-session-assessment/oi-004-retrospective.md` — the closure retrospective containing the §5.3 vindication finding (NB: this is a load-bearing cross-model data point; read in full if citing).

Perspectives 1 (Work-Shape Proposer), 2 (Path-Selection Defender), and 5 (non-Claude) MAY read those archive files if needed, but are not required to — the thin-index rows in SESSION-LOG.md should provide sufficient timeline context. If a perspective reads archive-surface files, it should cite them.

## 4. Required output format

Each perspective produces one markdown file at `provenance/043-session-assessment/01X-perspective-<role>.md` (X = a/b/c/d/e matching perspective 1..5). Required structure:

```markdown
---
session: 043
perspective: <role name>
perspective_index: <1-5>
lineage: <claude / gemini / other>
---

# Perspective <n>: <role name>

## Reading performed
<list of files actually read during this perspective's work>

## Q1 through Q7
<one subsection per question; the perspective may decline explicitly>

## Independent claim
<one or two sentences: what this perspective contributes that the other four cannot — this is the MAD v4 §16 manifest-schema "independent_claim" field substance>

## Confidence and limits
<what the perspective is confident in; what it is NOT confident in; anything it could not resolve given its scope>
```

Length guidance: perspectives should aim for roughly 800–2,000 words total. Compress where possible. The deliberation synthesis is more useful than any individual perspective; contribute a sharp position, not an exhaustive treatise.

## 5. What this deliberation is not

Anti-laundering reminders relevant to this session specifically:

- **Do not retrofit a spec in the same session that surfaces the motivating pattern without cross-family convergence.** The MAD v4 warning applies directly. If perspectives converge on spec change, convergence must be genuine, not manufactured.
- **Do not paper over the §5.3 S041 vindication.** The vindication is a data point; the operator is asking whether it should change the forward mechanism. Saying "we already discharged it" is insufficient — the question is what follows from the discharge.
- **Do not pre-decide in favour of any of the operator's four listed output shapes.** They are seed candidates, not a menu to pick from. A sixth option may be the right answer. "The framing is wrong" is a first-class outcome.
- **Do not use observational-metric vindications as evidence that discipline is working** when the question itself is whether observational-metric vindications are structurally guaranteed to look positive. That is the self-referential trap the operator has named.
- **If the deliberation concludes the operator's framing is wrong, the operator's framing must be preserved as a first-class minority**, per the operator's explicit request in §2 of the assessment. The preservation reason must be operational (what would cause the framing to be re-examined), not ceremonial.

## 6. Cross-family convergence and minority preservation

Convergence threshold per MAD v4 §Convergence: for substantive moves, 3-of-5 cross-family convergence suffices if at least one non-Claude perspective is on the prevailing side. If the non-Claude perspective dissents, the prevailing side must be 4-of-5 (all Claude plus explicit acknowledgement of non-Claude dissent), OR the move must be downgraded to non-substantive OR deferred.

Minority preservation: any perspective that does not prevail and whose position has distinctive operational content is preserved as a first-class §5-series minority in this session's provenance, with reopen warrants stated.

## 7. Non-Claude operational notes (Perspective 5 only, others skip)

Perspective 5 is invoked via `gemini` CLI with `--approval-mode plan` (read-only). Invocation pattern is analogous to the established `codex exec --sandbox read-only` convention for GPT. This is the first non-GPT non-Claude lineage exercise in the workspace's history and generates the §5.6 reopen-warrant (ii) data point on the **vindication side** — meaning Session 047 close no longer fires reopen-warrant (ii) if this session succeeds, regardless of which side this perspective lands on substantively. §5.6's concern is about cross-family exercise of the engine, not about which side wins.
