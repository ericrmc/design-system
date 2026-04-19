---
session: 008
title: Raw Perspective — The Skeptic (adversarial)
date: 2026-04-19
status: complete
perspective: skeptic
committed_at: 2026-04-19T03:18Z
---

## Q1

Three candidates, deliberately spanning different domains. I am holding the third candidate to the fire as my adversarial entry — it is the one a success-biased agent would quietly leave off.

**Candidate A — Personal reading-and-retention protocol design.** Domain: personal-knowledge practice. Problem: design a reproducible protocol by which the user processes a non-fiction book (or a small corpus of articles on one topic) from first encounter through durable retention and later retrieval, with an explicit reviewer/validator mechanism. Illustrative shapes: (i) a protocol for processing one specific book the user is currently reading, producing a spec that a second reader could execute and compare results; (ii) a protocol for a topic-cluster (three articles on one subject), with a comprehension-validation artefact the user could attempt two weeks later. Strongest fit: criterion 3 (Validate is native — a comprehension attempt or second-reader trial is a genuine test). Weakest: criterion 4 — the vocabulary overlaps heavily with methodology-talk (protocols, specifications, reviewers) and may fail the "mid distance" requirement. Risk of confounded success is high.

**Candidate B — Recipe or cooking-process design for a specific dietary constraint.** Domain: culinary practice. Problem: design a menu-and-preparation-sequence artefact for a bounded culinary task — say, a week of weeknight dinners under a stated constraint (budget, time, allergen, or nutritional target) the user cares about. Illustrative shapes: (i) five weeknight dinners under forty-five minutes meeting a stated macro target, with a cook-through validation; (ii) a three-course dinner-party menu executable in a home kitchen with a stated ingredient-cost ceiling, validated by actually cooking one course. Strongest fit: criterion 5 (externally legible — anyone can read a recipe). Weakest: criterion 3 at scale — cook-through validation requires the user's time and kitchen, which is accessible but slow.

**Candidate C (adversarial entry) — A governance or dispute-resolution protocol for a real interpersonal or small-group situation in the user's life.** Domain: human-process design outside software. Problem: design a written deliberation-and-decision protocol for a specific recurring decision-making situation the user is part of — a household decision, a small club or volunteer-group choice, a collaborative project with one or two other humans. Illustrative shapes: (i) a protocol for how a household of two decides on a non-trivial shared purchase above a stated threshold; (ii) a protocol for how a three-person hobby project decides when to abandon a direction. Strongest fit: criterion 6 (this is genuinely *hard* — the agent does not know the social texture, cannot quietly succeed). Weakest: criterion 2 — edges close to real stakes; must be kept strictly advisory.

I reject as Q1 entries: physical-training programmes (validation timeline too long), investment policy design (ruled out by criterion 2 stakes), and any curriculum for software topics (ruled out by criterion 8). I specifically reject multiple variants of personal-knowledge practice as the whole shortlist because that is adjacent sub-domains, forbidden by Q1's framing.

## Q2

My recommended pick is **Candidate C** — the human-process protocol for a real small-group decision in the user's life. This is the adversarial recommendation; I hold it because criterion 6 is the criterion most likely to be quietly violated by an orchestrating agent, and C is the only one of the three where success is not overdetermined.

Criteria C handles best: 6 (the agent cannot comfortably predict success because the domain knowledge is not in the agent's training distribution for this specific social context); 4 (vocabulary distance is real — "motion," "concurrence," "deferred decision," "quorum-of-two" do not map onto methodology-talk without effort); 5 (a household or small-group member can read the output and judge whether it would actually be followed).

The property I expect to be challenging — and where the risk is serious — is **Validate**. A social-protocol artefact is only truly validated by being used in a real decision, and the user cannot manufacture a real contested decision to order. The fallback — a walk-through by the user and a second participant imagining how the protocol would have worked on a past decision — is a weaker test than the methodology wants. The honest statement: Validate here is thinner than Validate would be in, say, Candidate B where you can actually cook the meal.

Proceeding nonetheless is the right call because: (i) criterion 6's counter-weight role is explicit in the brief — criterion 7 is a floor, not a ceiling, and C is the candidate that most visibly resists the agent's expected-to-succeed bias; (ii) a thin but real Validate is more informative for a first external application than a thick Validate on a target where the vocabulary barely moves; (iii) the methodology's claim is about durable specifications and preserved reasoning — a family-decision protocol is the kind of artefact where that claim has bite (real-world protocols drift, are forgotten, are re-litigated), so the methodology has something distinctive to offer rather than merely a place to perform.

I held Candidate A (reading protocol) longer than I should have. I demote it because its vocabulary overlap with methodology-talk is precisely the confounding condition criterion 4 was written to prevent, and the agent's attraction to it is itself suspicious. Candidate B is my fallback if the user judges C too risky on criterion 2 stakes — B clears Validate cleanly but fails criterion 6 (an agent predicts success on a recipe exercise too easily).

If I am wrong and C's Validate gap proves load-bearing, the correct move is to run C with the explicit caveat that Validate will be a walk-through rather than a live deployment, and accept that as a session-level limitation rather than switching candidates. Switching to B to escape the Validate problem would be the agent-bias move criterion 6 exists to prevent.

## Q3

Two failure modes specific to Candidate C, with distinguishing evidence.

**Failure mode 1: The social texture the protocol is supposed to govern turns out to be illegible from the available materials.** The user can describe a household or small-group decision process, but the actual friction lives in implicit priorities, unstated loyalties, history of past disagreements, and tacit power — none of which compress into a brief a deliberation can work from. The resulting protocol reads as generic "here is how a reasonable small group could decide things" — fluent, publishable, and useless because it does not bind on *this* group's actual friction points.

Evidence distinguishing this from methodology failure: the artefact is coherent and domain-idiomatic (it does not read as methodology-talk), but when the user reads it against the specific decision-shape it was designed for, the user can point to real friction points the protocol does not name or address. Contrast: a methodology failure would produce something that uses methodology vocabulary ("activities," "deliberations," "provenance") inside the protocol; this target failure produces something that sounds like a civic-textbook protocol and is flat against the specific case. If the user says "this is a fine generic protocol but it would not have prevented the disagreement we had in March," that is target failure, not methodology failure.

**Failure mode 2: Stakes collapse inward during execution.** The protocol is ostensibly advisory — a sandboxed design artefact — but the mere act of drafting it exposes something about the group's decision-making the user did not want surfaced, or the user and other participants start negotiating over the protocol as if it were binding. The session then either (a) produces a deliberately thin protocol that avoids the real questions, or (b) produces a protocol the user cannot share with the group without social cost. Either way the external artefact ceases to be external — it becomes internal to the user's situation and fails criterion 5 retroactively because the user will not allow an outside reader to see it.

Evidence distinguishing this from methodology failure: the session produces something, but the user declines to treat it as the external artefact, or the user requests that the provenance be sanitised before commit. The methodology would be working correctly; the target would have failed the reversibility-stake test the session tried to hold. A methodology failure looks different — it looks like the deliberation producing text but the user judging the text hollow.

A third, weaker failure mode worth naming: the user's Validate walk-through with a second participant ends up being a conversation about the methodology rather than about the protocol. If the user finds themselves explaining what a Validate activity *is* before the other participant can evaluate the protocol, the target has forced methodology-talk to leak into validation, and Q4's external-legibility test has already failed.

## Q4

A reader who has never read this methodology's specifications will receive, for Candidate C, a document that describes: a named decision situation (e.g., "shared-purchase decisions in household H of two members, for items above a stated threshold"); the actors and their roles in that situation; the sequence of steps by which a decision is proposed, considered, and resolved; the handling of disagreement, deferral, and reversal; and a written record of what the protocol was designed against and what it is *not* trying to solve.

What the reader should *not* see, if the artefact is real domain work: the words "activity," "deliberation," "provenance-record," "specification," "trigger," or "manifest" as the protocol's load-bearing vocabulary. Those are methodology-talk. They may appear in a clearly-separated section describing how the protocol was produced, but the protocol itself should use the vocabulary the reader's domain actually uses — "proposal," "objection," "standing decision," "review period," "fallback," "quiet consent," or whatever the specific case calls for.

The reader's judgement test is whether they can answer two questions from the artefact alone: (1) "If a concrete decision arose in this situation, could I follow this protocol step by step without needing to ask the authors anything?" and (2) "Does the protocol address the friction points I would expect in this situation, or does it read as if it was designed for some idealised version of this situation?" If yes to both, it reads as real design work. If the reader finds themselves asking "what does 'deliberation' mean here — is that a specific thing?" the artefact has failed external legibility.

A stronger test: show the artefact to a second household or small-group analogue — a different pair in a different living situation — and ask whether they can adapt it to their own case by changing parameters, or whether they would need to start over. Real domain work adapts; methodology-talk-in-disguise does not, because the load-bearing structure was never about the domain.

Concrete markers I would look for in the final artefact: named steps rather than named activities; domain-specific edge cases (what happens on a weekend when one party is travelling; what happens when a decision was made under one assumption and the assumption changed); an explicit scope statement in domain terms ("this applies to purchases above £X, does not apply to routine household consumables"); and a change-log in the protocol's own terms ("amended after the March disagreement") not the methodology's.

Rejected framing: "the artefact is legible if it is well-written." Legibility is not prose quality; it is the absence of methodology-vocabulary doing load-bearing work and the presence of domain-vocabulary doing real work. A beautifully-written document that keeps slipping into methodology-talk is worse than a rougher document that stays in the domain — the former reads as a performance, the latter as design.

## Q5

The non-obvious agent bias: **the agent prefers targets whose domain artefact shape is textual, structured, and author-led — a single document produced by a single author for a cooperative reader.** The methodology was built in that shape. The agent will gravitate to targets whose deliverable looks like "a specification" because specifications are what the agent has practised producing. This is distinct from software-adjacency (criterion 8) and distinct from expected-to-succeed (criterion 6); it is a bias about the *shape of the artefact*, not the domain.

Under this scrutiny, Candidate A (reading protocol) looks suspicious for reasons beyond vocabulary-overlap: it produces a document. Candidate B (menu) produces a document. Candidate C produces a document. All three candidates I offered share the bias. That is a real admission.

The candidate a more honest selection would include, which I do not add to my Q1 shortlist because I do not want to pretend I can execute it well within the criteria, is: **a target whose artefact is not primarily textual** — for example, a designed schedule (a calendar-shaped artefact where the layout carries meaning), a designed physical-space arrangement (a floor plan for a specific room reconfiguration), or a designed visual reference (a chart, a legend, a colour system for some real categorisation task the user has). These force the methodology to produce provenance about a non-textual deliverable, and expose whether the methodology can record reasoning about something other than prose.

A candidate to rule out as obvious-looking: **any "policy document" target** (personal financial policy, household media policy, personal AI-use policy). These are the agent's home turf — textual, specification-shaped, reader-cooperative — and criterion 6 should bite hard against them precisely because they will feel easiest. If the next session's target, or the follow-on session after Session 008, lands on "design a personal AI-use policy" or similar, that is the bias re-asserting itself and should be treated with suspicion even if it clears all eight criteria on paper.

The concrete proposal: in Session 008 we proceed with Candidate C as recommended, and the provenance should flag that C, too, is document-shaped — we have not escaped the shape-of-artefact bias, only the domain bias. Session 009 or a later session should deliberately test a non-textual artefact target. The methodology does not get to claim generality until it has produced a provenance-record for something that is not a document.

I hold this position against my own shortlist. I do not retract C — within document-shaped targets, C is still the most honest choice — but I refuse to let the shortlist conceal that all three entries share a shape the methodology has never been stressed against.

## Meta-note

I expect the Pragmatist to recommend Candidate B or an equivalent recipe/protocol-with-easy-Validate target, arguing that first external application should clear Validate cleanly. I expect the Explorer to range wider than my three candidates and possibly propose a non-textual artefact I ruled out of my own shortlist for executability reasons. The position I hold in tension with my role is that I do think Candidate C carries real Validate risk; a non-adversarial version of me would probably pick B. I am recording the C recommendation at full strength because my role exists to resist the shortlist being three comfortable options.

Assumption I flag as suspect: the brief treats criterion 7 (accessibility) as a floor and criterion 6 as the counter-weight, but in practice criterion 7's bounded-brief requirement narrows the domain far more than criterion 6 widens it. The real floor is higher than the brief admits.
