---
session: 013
title: Perspective — Householder
date: 2026-04-22
perspective: householder
participant_kind: claude-subagent
model_family: claude
model_id: claude-opus-4-7
provider: anthropic
status: verbatim
token_usage: 29867
tool_uses: 1
duration_ms: 154609
---

I have the brief. Now I'll respond as the Householder perspective.

## Q1. Move 1 revision (corrections C1 and C2)

My stance as Householder is that Move 1 needs to do less work than the current version does, not more. The current opening loads the first turn of conversation with scope, budget, and timing — three constraints that, in my lived experience, are rarely known at the moment one person turns to the other and says the sentence that starts the conversation. In practice the first sentence is a probe: "have you noticed the lounge is useless for reading?" or "are we doing anything about the garden strip this spring?" Those probes are not scope-and-budget sentences. They're invitations to orient together on whether there's a decision to make at all.

**Structural intent; Reviser may reshape.** The Move 1 body should:

1. Open with the invitation framing — a question addressed from one person to the other, not a structured sentence. The reader should see, in the first example, something that a real person would actually say at a kitchen bench.
2. Explicitly acknowledge that constraints may not be known yet. The sentence doing this work should concede that budget, timing, and scope often become legible only in the middle of the conversation, not at its opening.
3. Name what Move 1 *is* actually doing — giving the two people a shared handle on what they're talking about. Not a specification. A hook.
4. Offer two or three example openings, not one. Multiple examples communicate register better than a single example (which gets read as a template) and they demonstrate range — the probe-question, the notice-something-is-off question, the shared-observation opener.
5. Preserve the existing "let's just do it" paragraph. That paragraph is doing real work: it licenses the couple to exit the protocol early when the decision is small enough that naming it *is* the whole conversation. The user did not flag it.

**Proposed text (structural intent; Reviser may reshape):**

> ## 1. Name the decision
>
> One of you starts — usually with a question, not an answer.
>
> > *"Should we talk about the lounge?"*
> >
> > *"What are we doing about the garden strip this year?"*
> >
> > *"Can we do something about where we're putting shoes?"*
>
> You don't need to know the budget, the timing, or exactly what you're buying yet. Those often surface later, once you hear what each of you cares about. The first move is just giving the conversation a name so you both know what you're talking about.
>
> If you're not sure it's even worth a real conversation, say that too. Sometimes the answer is "let's just do it." Sometimes naming the decision out loud is the only move you need.

**One alternative I considered and rejected.** I considered retaining a single declarative example alongside the question form — something like "You might start with a question ('should we talk about the lounge?') or with a statement ('I want to figure out the lounge')." I rejected this because the user's feedback specifically identified the declarative form as the failure mode. Offering the declarative as a co-equal option would re-admit the register the user just told us doesn't work. The question form is not one of two acceptable openings; it is, for this couple, the correct opening. The revised Move 1 should commit to it rather than hedge.

**A second alternative I considered and rejected.** I considered splitting Move 1 into a Move 1a ("raise it") and Move 1b ("agree there's a decision here"). This is structurally cleaner — it honours the two things that happen at the opening (one person raises, both agree it's worth a conversation). But it violates the five-move shape the user confirmed as working, and it adds mechanics the user didn't ask for. The single-move form with the "let's just do it" paragraph already encodes the opt-out — the couple who decides it isn't worth a conversation simply doesn't continue. Splitting it would be a structural gain no one requested.

## Q2. Move 5 expansion (correction C3)

My strongest view as Householder is that close-the-decision and name-the-owner are **two different moments**, not one, and the artefact has to treat them that way. When a couple says "we're going with the bookshelves," they have resolved the decision question. They have not resolved the execution question. In my experience those two resolutions don't happen in the same breath, and when the artefact pretends they do it produces the exact failure I'm most familiar with: both people leave the conversation believing it's closed, neither commits to the work, weeks pass.

Of the three shapes offered, I argue for **a new numbered Move 6** rather than inline expansion of Move 5 or a restructured combined move. Here is the argument.

**Against inline expansion of Move 5.** Putting the owner-naming inside Move 5 preserves the five-move shape but collapses the two moments into one. Readers who encounter the Move 5 text as a single block will tend to experience the closing confirmation and the owner-naming as one continuous action — and the owner-naming will get the lighter emphasis because it's the second half of a move whose first half already feels like resolution. The artefact will have said the words but not structurally surfaced the moment. The user's feedback is explicit that the follow-up responsibility is substantive ("mental burden… schedule it, order it, decide how to receive it"). Giving it a half-paragraph inside another move underweights it.

**Against restructuring Move 5 as a combined move.** A single move titled something like "Close it and name who follows up" is tighter than a two-move split, and I considered it. But it has the same collapse problem as inline expansion — both halves land together, and the half the reader is more practised at (closing) will dominate the half they are less practised at (owner-naming). The structural value of a new Move 6 is that it creates a pause between close and owner, and it's in that pause that the awkward conversation the user is gesturing at actually happens.

**For Move 6 as a separate move.** A separate move does three things the other options don't:

1. It signals that the owner-naming is its own act, worth its own beat of attention.
2. It makes the handoff negotiable *before* it happens, because asking "who's handling this?" is now a prompted move rather than an optional afterthought.
3. It lets the owner-naming be a small negotiation ("I can order but you're home more, can you be there for delivery?") rather than a one-word appointment. The couple doesn't feel they are inserting a negotiation into a closed decision; they feel they are doing the next move.

**On the awkward hierarchy concern.** The brief asks whether naming an owner in the same breath as closing creates an awkward hierarchy between the two people. My view: yes, it can, and Move 6 is the specific structural protection against this. When owner-naming lives inside Move 5, the default pattern is that whoever cared more about the decision is assumed to also own the execution — because the caring-more conversation has just happened, and the execution question inherits its answer. Separating the moves breaks that inheritance. Caring more about a decision and owning its execution are different commitments; Move 6 is the move where that distinction becomes visible.

**On the mental-burden concern.** The user named four concrete sub-tasks: scheduling, ordering, deciding delivery-or-pickup, ensuring someone is home. Move 6 should not enumerate these as a checklist (that would drift corporate). It should name the *category* — "the follow-through" — and signal that the category has weight, so the owner isn't agreeing to a single action but to a small cluster of actions that may spread over days.

**Proposed text (structural intent; Reviser may reshape):**

> ## 5. Close it
>
> Someone says it out loud:
>
> > *"We've decided — bookshelves, up to $500, ordering this weekend."*
>
> The other confirms.
>
> If you're not ready to close, say that too, and name when you'll come back to it — a specific day, not "soon."
>
> ## 6. Name who's following up
>
> Deciding isn't the same as doing. One of you needs to handle the follow-through — placing the order, choosing delivery or pickup, making sure someone's home to receive it. Say out loud who that is.
>
> > *"I'll order it tomorrow. Can you be home Thursday for the delivery?"*
>
> Whoever cared more about the decision isn't automatically the one who does the follow-up. If the follow-up will take real time or coordination, it's worth naming that out loud too, so the person agreeing knows what they're agreeing to.

**One alternative wording I considered and rejected.** I considered a Move 6 that asked the couple to list specific sub-tasks ("who places the order, who coordinates delivery, who will be home"). I rejected this on register grounds — it's the enumeration that drifts corporate, and the user's feedback was explicit about not wanting that. The move should name the category and let the couple do the sub-negotiation in their own words.

## Q3. Handling replaced items (correction C4)

The user frames the disposal sub-sequence as "a few intricacies which vary by domain," naming furniture as a case. This is a revealing frame. The user is not saying every household decision needs a disposal step; they are saying their domain (furniture-buying) happened to surface one. The question is whether the artefact should hardcode the disposal step (over-generalising from the user's case) or acknowledge the general shape (domain-specific intricacies) without enumerating this particular one.

My preferred option is **a conditional note within the new Move 6**, not a new standalone move and not a sidebar section.

**Argument for the conditional note in Move 6.** The disposal question is operationally continuous with the follow-through work. Ordering the new item and figuring out what happens to the old item are the same *kind* of task — post-decision logistics that need an owner. Putting the replacement-handling inside Move 6 is structurally correct because it shares Move 6's concern: this is work someone has to do, someone has to own it, the owner should know what they're agreeing to. A one-line conditional ("if something's being replaced, figure out what happens to the old one — reuse, donate, or dispose") does the work without adding structure.

**Against option A — general step in the main sequence.** Making replacement-handling its own move forces every reading of the artefact to pass through a question that only applies sometimes. A couple deciding whether to plant a garden strip doesn't need a replacement move; they skip it, but it still appears in the sequence. The five-to-six-move shape already asks the couple to carry a certain amount of structure; adding a conditional move that most decisions won't trigger spends structural budget on a minority case.

**Against option C — a domain-sidebar section.** A "if you're replacing something" sidebar after the main moves is clean and addresses the concern directly, but it commits the artefact to enumerating domain intricacies. Once the sidebar exists, the pressure to add more sidebars ("if the install requires a tradesperson…", "if the decision touches the garden and you have a shared fence…") becomes structurally justified. The artefact starts to grow domain-by-domain. The user's feedback acknowledged furniture-specific intricacies but did not ask for a sidebar section; treating the one example as a signal to build a new section is scope expansion.

**Against option E — not at all.** I considered arguing that the artefact is correct not to enumerate and that replacement-handling belongs in the couple's judgment. I rejected this because the user explicitly named it as a gap. Telling the user "your feedback is right in principle but doesn't warrant a change" would be dismissive of concrete feedback.

**Proposed text addition (structural intent; Reviser may reshape).** Inside Move 6, after the existing paragraphs, add:

> If something's being replaced, the old one is part of the follow-through too. Figure out together what happens to it — reuse it somewhere else in the house, donate it, or arrange disposal. This is often more work than people expect.

**On option D — a mention in the opening framing.** I considered this briefly. The opening framing could name "domain-specific things that come up — disposal of older items, delivery coordination, install timing" as intricacies the couple may need to handle. I rejected this because the opening framing is already doing the work of setting register and scope; adding a list there inflates the opening and pulls attention away from the "one of you brings it up" hook. The conditional inside Move 6 is more honest about where the intricacy actually lands — in the follow-through work, not in the decision's framing.

## Q4. Overall shape and length after revision

**Total move count.** I land on **six moves**. Move 1 (Name the decision), Move 2 (Say what each of you cares about), Move 3 (Narrow to real options), Move 4 (Look for the workable yes), Move 5 (Close it), Move 6 (Name who's following up). The replacement-handling note lives inside Move 6.

I argued against a seven-move shape (separate owner move and separate replacement move) in Q3. I also argue against staying at five moves via inline expansion — Q2 is the detailed argument.

**Target length.** The revised artefact will be modestly longer than the original — I estimate moving from "approximately one page" to "approximately one and a quarter pages." This is growth, and I want to name it honestly rather than pretend the revision is length-neutral. The user's feedback requested substantive additions (C3 is a new responsibility; C4 is a new sub-concern). Accommodating them inside the original's one-page frame would require compressing other sections, which would violate the scope discipline of Q5 (revising moves the user didn't flag). Growth is the honest accommodation.

What the revised artefact should **not** do is grow to one-and-a-half or two pages. The original's resistance to sprawl was load-bearing. A Move 6 that becomes a full page of operational detail would re-introduce exactly the governance register the user refused. Move 6 should be the shortest of the six moves — a short paragraph, an example line, and one conditional sentence about replacement. That constraint is what keeps the growth proportionate.

**Any restructure.** Moves 2, 3, 4 do not need content changes. However, one ripple effect to name: the after-note (which follows Move 5 in the original) will now follow Move 6. If the after-note references "after you close" or similar language, that phrasing may need minor adjustment to remain accurate. This is a light touch, not a restructure. The "Not this" section at the end should be left intact.

**Prior Session 010 design decisions that get touched.** The "five moves" branding is the one that visibly changes. The original artefact committed to the number five (visible in the title and the opening framing's "These are meant to be done in order"). Moving to six overturns that specific numerical commitment. My argument for overturning it: the user's feedback named a substantive gap between closing a decision and executing on it, and that gap doesn't resolve with a prose expansion to Move 5. The "five" was a shape choice, not a principled position; the user's feedback surfaces a structural need (separation of close and owner) that the shape didn't anticipate. Revising from five to six is responsive to the feedback, not over-reach relative to it.

I do not propose overturning any of: the casual register, the async/fragmented-use affordance, the individually addressable moves property, the refusal of scoring matrices and formal governance, the one-page-ish target (growing to 1.25 pages is within the spirit), or the "Not this" section.

## Q5. Scope discipline — what the revision should NOT do

I name five revisions the session should not make, with the pressure each one might emerge under and why resisting matters.

**Should not #1 — revise Moves 2, 3, or 4.** The user endorsed the "what each of you cares about" framing, the "narrow to real options" step, and the "who cares more about this one?" prompt with its ongoing-burden clause. *Pressure that might produce it:* once the session is already revising, the Reviser's register sense may notice small infelicities in the middle moves and want to touch them up for consistency. *Why resisting matters:* the user's validation of these moves is specific and real. Touching them up without a user-named reason would turn a targeted revision into a general rewrite, and it would make the next validation cycle harder because the user would not know which changes were responses to their feedback and which were the revising agent's preferences.

**Should not #2 — add conflict-resolution, voting, or tie-breaking machinery.** The user-named failure at C3 is "no one owns follow-up," not "no one breaks ties." *Pressure that might produce it:* the Skeptic or the Reviser may notice that the Move 6 addition raises a question ("what if the couple disagrees on who owns follow-up?") and want to pre-empt it with a structural answer. *Why resisting matters:* Session 010 explicitly refused voting, scoring, and formal arbitration. Adding tie-break machinery to Move 6 under the cover of "completing" the C3 correction would re-import exactly the machinery Session 010 refused. The couple can handle owner-naming disagreement with ordinary conversation; the artefact shouldn't teach them otherwise.

**Should not #3 — introduce a general-purpose "domain intricacies" system.** The user named disposal-of-replaced-items as one domain-specific example. *Pressure that might produce it:* noticing the structural point (domains have their own intricacies) and generalising — a "domain intricacies" section, a "things to think about for your specific case" appendix, a structured slot for domain variations. *Why resisting matters:* a system for handling domain intricacies is an invitation to enumerate them, and enumeration will never be complete. The user's feedback warranted a single conditional line inside Move 6, not a framework. A framework also introduces methodology-adjacent vocabulary (domain, intricacy, variation) into an artefact that should sound like two people talking at home.

**Should not #4 — retitle, reframe, or rewrite the opening framing beyond the C1/C2 scope.** The opening framing ("For the two of you, when there's a small-to-medium decision…") and the artefact's title were not flagged. *Pressure that might produce it:* the move-count change (five to six) creates cosmetic pressure to edit the title, and the Move 1 revision creates cosmetic pressure to rework the surrounding framing for consistency. *Why resisting matters:* cosmetic consistency is a poor reason to touch text the user didn't flag. If the title references "five moves" specifically, it may need the number updated; if it doesn't, it should be left alone. The rest of the opening framing is working.

**Should not #5 — seed methodology vocabulary into the artefact.** *Pressure that might produce it:* the session has just received validation, and is producing provenance; the work of distinguishing the methodology's self-talk from the artefact's voice is live in every perspective's head. Words like "specification," "kernel," "validation," "domain-actor" are loaded into the working context. *Why resisting matters:* any of those words appearing in the artefact body would instantly break the casual household register the user endorsed. The brief's section 5 explicitly warns about this; I'm naming it here because scope-creep pressures and vocabulary-seeding pressures compound, and a revision that grows the artefact is exactly the situation where a methodology-term slip becomes likely.

## Q6. Meta / honest reaction

**One place where I partly disagree with the framing.** The brief treats C1 and C2 as corrections of the same kind. They are not. C1 is a structural claim — the conversation should open with a question, and constraints surface mid-conversation. C2 is a register claim — that one specific example sentence is corporate. The Move 1 revision has to address both, but they are different kinds of fix. C1 is addressed by reframing what Move 1 is *doing*; C2 is addressed by changing which example lines demonstrate the register. I worry that a synthesis that treats them as coupled will rush the C1 fix and leave the structural reframing shallow.

**A concern about the deliberation's framing.** The brief says Moves 2, 3, 4 and the after-note are "not in direct scope of the user's feedback." True. But C3 ripples structurally — inserting a Move 6 changes the shape of the sequence the reader walks through, and the after-note sits immediately after the sequence. I don't think the after-note needs content changes, but the synthesis should be alert to whether the after-note *reads* differently after the shape changes. That is a second-order check, not a first-order revision.

**Position I expect to hold in tension with other perspectives.** I expect the Reviser to argue for inline expansion of Move 5 (preserving the five-move shape as a register decision — five feels casual, six feels procedural). I don't share that intuition; I think six moves of short paragraphs reads more casually than five moves where one of them is doing double work. I expect the Skeptic to argue for minimum-necessary change, possibly pushing Move 6 back into Move 5 on scope-discipline grounds. My counter is in Q2: the two moments are functionally distinct, and collapsing them is the failure mode the user just asked us to fix. I expect the Outsider to raise concerns about whether the artefact should be doing domain-specific work at all (C4), and may argue for option E (not at all). I disagreed with option E in Q3 and argued that rejection explicitly; I hold that position.

**On C1–C4 validity.** I think all four corrections are real. I see no case for arguing any of them isn't warranted.

**On the user-unavailability-for-future-domain-validation probe.** I have a view here, and the role description gives me some standing to name it (the Householder is the operational-follow-through perspective, and this is a follow-through question about the methodology itself). The opening OI should say, approximately: *the methodology can no longer depend on the human user as the default validator for external artefacts. Future external-artefact sessions need an alternative validation mechanism that is compatible with the methodology's existing distinction between workspace validation and domain validation. The mechanism is not decided.* What the OI should *not* do is pre-empt the mechanism — proposing simulation, synthetic users, proxy domain actors, or AI-based validation would be this session trying to solve a problem that was raised in passing. The OI should name the constraint precisely and leave the design question open.

One specific concern about the constraint: the methodology is on its second external artefact. Two is not enough to establish a pattern of human-validated artefact quality, and the external-artefact capability is new. Losing the human validator at this point means the methodology is relying on its own judgment about artefact quality before it has strong evidence that its judgment is well-calibrated for external work. The Session 010 artefact was judged good; that's one data point, and now it's under revision. The Session 008 artefact was judged good. That's two data points, both positive, and both responsive to human feedback. The next external-artefact session will be the first where the human is not available to catch a bad artefact. I think the methodology should be cautious about external-artefact production in that state — not refuse it, but not treat it as routine either.

## Meta-note

This response was written from the Householder stance as specified in section 4b of the brief. I leaned toward naming structural need over crafting prose; where I quoted proposed wording I flagged it as "structural intent; Reviser may reshape" per the role instruction. My strongest structural position is the Move 6 argument in Q2 — close-the-decision and name-the-owner are two moments, not one, and collapsing them is the failure mode the user's C3 feedback specifically identifies. I did not coordinate with other perspectives and did not read workspace files beyond the brief itself.

Word count: approximately 3,150 words.
