---
session: 028
title: Perspective — Outsider
date: 2026-04-23
status: complete
perspective: Outsider
committed_at: 2026-04-23T09:34:55+10:00
---

## Q1

Convert §5.3 into active specification now, but do **not** convert it by simply copying its original 90K/80K numbers into the spec. The preferred revision direction fired for a reason: the engine now has direct evidence that per-file control is insufficient against default-read accretion. Continuing preservation-only after the activation threshold has been crossed would turn §2a into a siren that everybody hears and nobody is required to act on.

I do not think the right move is “record activation and wait for more evidence.” The evidence is already sufficient. The aggregate moved from about 83K at Session 023 close to 105,399 at Session 028 open, without any single-file hard breach. That is the exact failure mode aggregate control was introduced to catch. Waiting longer would not be principled restraint; it would be declining to complete a control loop the engine deliberately designed.

But I also do not think the right move is “the minority said 90K/80K, therefore 90K/80K must now be adopted literally.” That would confuse activation with auto-enactment. Activation says the direction is now preferred. It does not erase the right to revise the exact shape in light of the trajectory observed since Session 023.

So my answer is: **adopt, and revise §5.3 in light of post-activation information.** The right revision is an aggregate hard budget, but at values and with a remediation mechanism fitted to what is now known about the workspace’s actual growth pattern.

## Q2

Adopt **100K hard / 90K soft**.

Those numbers are the cleanest choice for three reasons.

First, they are already field-tested thresholds. Session 023 named 90K as advisory and 100K as activation. The system then produced actual trajectory data against those values across Sessions 024–028. The thresholds were not arbitrary paper numbers anymore; they were exercised. The engine learned that 90K is “pressure is real” and 100K is “the surface has crossed into structural-revision territory.” Reusing those numbers as soft/hard budget values is the least ad hoc move available.

Second, 90K/80K is too low **for adoption at this stage**. I understand the original §5.3 argument: named budgets create forcing function. That was right. But the observed state matters. The default-read surface is now 105,399 words across 39 files. Setting hard at 90K after the surface has stabilized above 100K does not just create forcing function; it demands an immediate large-scale carve-out without first deciding which content classes deserve removal from default-read. That is not disciplined pressure. It is a blunt retrospective overcorrection.

Third, 110K/100K or 120K/110K would launder the activation. If the engine crosses a pre-named 100K threshold and then answers by putting the new hard ceiling above the current state, it is effectively saying: “the trigger fired, so we moved the trigger.” That is exactly the kind of self-protective drift this methodology is supposed to resist.

I would therefore set the budget at:

- **Soft:** 90,000 words aggregate default-read surface.
- **Hard:** 100,000 words aggregate default-read surface.

And I would not grandfather the current overage. If the engine adopts the budget, it should pair adoption with real remediation sufficient to get back under hard. Otherwise the “budget” is only narrative.

## Q3

When the aggregate approaches or exceeds ceiling, the response should target the **retention structure** of the default-read surface, not randomly attack coherent files.

I would specify a two-stage mechanism.

At **soft threshold** (≥90K):
- The session close must report aggregate total, delta from prior close, and the main growth driver.
- The session must name a concrete remediation candidate for the next crossing, chosen from a closed list.
- This remains warning-level, not failure-level.

At **hard threshold** (≥100K):
- The session cannot close cleanly unless it also executes a restructuring that returns the default-read surface below hard.
- The remediation must be structural, not summarising. Archive-pack discipline and explicit-reference discipline still apply.
- The preferred remediation order should be stated in the spec so the engine does not improvise under pressure.

My recommended remediation order is:

1. **Rotate aged `03-close.md` files to archive surface first.**  
   This is the main monotone-growth class. Every close currently remains default-read forever. That is manageable at small scale and eventually untenable at large scale. If aggregate control exists for any reason, it is largely for this class.

2. **Keep only a bounded recent close window on default-read.**  
   I recommend the most recent **6** session closes, plus any older close that is explicitly cited by an active specification or open issue for currently load-bearing governance. Older closes remain preserved and referenceable, but they stop being compulsory rereads every session.

3. **Only after that, trim other monotone-history structures.**  
   The obvious secondary candidate is long-form history in `engine-manifest.md` §7. If that section keeps growing, it should eventually become pointer-backed rather than endlessly elaborated in the live manifest.

4. **Use prompt-level close-size guidance as inflow control, not primary remediation.**  
   This matters, but it is secondary. It reduces future growth; it does not solve the current structural fact that aged closes remain mandatory reads forever.

What I would *not* do is use aggregate pressure as the main reason to split `multi-agent-deliberation.md` or other coherent normative specs. That would misdiagnose the problem. The current breach was reached with only one persistent soft-warn file and no per-file hard breaches. The engine is not being crushed by one oversized spec. It is being crushed by accumulation rules.

## Q4

Aggregate and per-file budgets should be **supplementary and orthogonal**.

Per-file budgets answer one question: can any single default-read file become too large to read coherently in one pass?

Aggregate budget answers a different question: can the total default-read surface become too large by accretion even when every individual file remains locally “fine”?

This session exists because the answer to the second question is yes.

So the aggregate budget should not override the per-file budget, and the per-file budget should not be treated as evidence that aggregate control is unnecessary. They guard different failure modes. The Session 027/028 state is the proof: per-file control largely held, but aggregate control fired.

The practical consequence is important. When aggregate pressure appears without per-file breaches, the default presumption should be: **fix the enumeration or retention policy first**, not the stable normative documents. If a future session sees both kinds of pressure at once, then both controls may need action. But they are not substitutes.

One more point: §5.2’s retroactive vindication matters here. It shows that the per-file recalibration dispute and the aggregate-growth dispute are separable. The fact that no restructure-for-budget event occurred under the per-file regime does **not** weaken the aggregate case. It strengthens it, because it demonstrates that aggregate accretion is a distinct phenomenon rather than a disguised single-file problem.

## Q5

Treat engine-version cadence as a **separate issue per OI-018**, not as a co-decided question inside this deliberation.

A substantive `read-contract.md` revision here would properly bump `engine-v4` to `engine-v5`. That should be recorded plainly and justified plainly. But I would not reopen `engine-manifest.md` §5 bump-trigger criteria in the same session unless the operator explicitly broadens scope.

Reason: the current deliberation has a clean subject. The aggregate mechanism fired. The engine needs to decide whether to enact an aggregate budget and how. That is already enough. Folding OI-018 into the same decision risks turning a concrete scaling repair into a meta-argument about whether engine versions mean enough.

The cadence minority should still be acknowledged. My recommendation is to record, in the decision and close, that:

- this bump is content-driven rather than ceremonial,
- it responds to a pre-named activation condition,
- and it does not by itself settle OI-018 one way or the other.

In other words: **do not let §5.4 veto a necessary repair, but do not ignore it either.** Note the interaction and defer the cadence-rule question to its own agenda unless separately activated on present facts.

## Q6

This is **mechanism working**, with one revealed gap: the sensing worked, but the actuation was deferred.

The important thing to notice is that §2a did what it was supposed to do. It surfaced a load-bearing scaling problem that per-file budgets could not surface. That is success. If the aggregate had continued to rise without any special note until the workspace became plainly unreadable, that would have been mechanism failure. That did not happen. The system named a threshold, tracked it, crossed it, and brought the question forward.

The gap is that §2a was an informational reporter with no committed remediation policy behind it. That was acceptable while the threshold had not fired. It is no longer acceptable now that it has. The engine now needs to move from detector-only to detector-plus-response.

So my formulation is: **the mechanism was correct, but incomplete by design.** Session 028 should complete it. I would resist framing the activation itself as evidence the prior design failed. Warning systems are supposed to warn. The right lesson is not “the watchpoint was inadequate.” The right lesson is “the watchpoint has done its job; now bind it to an enforcement path.”

A control-systems framing is useful here. The engine already had a sensor. It did not yet have a controller. This deliberation should add the controller.

## Q7

The new information since Session 023 is substantial, and it is enough to justify action without laundering.

The most important new facts are:

1. **Observed trajectory, not imagined trajectory.**  
   At Session 023 close the aggregate was about 83K. At Session 024 close it was about 92.5K. At Session 025 close it was 95,675. At Session 026 close it was 99,532. At Session 028 open it was 105,399. That is not a speculative risk anymore. It is an observed curve.

2. **Aggregate growth persisted without single-file hard pressure.**  
   That validates the original aggregate concern. The engine now knows, empirically, that local file ceilings do not solve surface-wide accretion.

3. **The growth was not only one noisy spike.**  
   The >10% clause mattered in Session 024, but the actually decisive pattern was repeated moderate growth across multiple sessions, culminating in the absolute-threshold crossing. That matters for calibration. It argues for an absolute hard budget more than for a growth-rate-only watchpoint.

4. **The dominant growth driver is structural retention of closes.**  
   Every `03-close.md` stays default-read. That is a rule, not an accident. Once the engine sees that the append-only class is the main pressure source, the response should target the rule.

5. **§5.2 vindicated separately.**  
   That is new information too. It tells the engine that the earlier per-file revision dispute should not be conflated with the aggregate-budget question. The aggregate problem survived even though the per-file crisis did not materialize in the way one minority feared.

Does activation-firing itself count as new information? **Yes, but only procedurally.** It tells you that a pre-named condition has now occurred. It does **not** by itself prove that the original minority’s exact numbers were correct. Treating activation as automatic proof of 90K/80K would be a laundering move in the opposite direction: turning “reconsider now” into “adopt literally.”

The coherent continuation of preservation discipline is this:

- Preserve the Session 023 minority text as historical witness.
- Acknowledge that its direction was vindicated by later evidence.
- Convert the direction into active spec using the now-available empirical trajectory, rather than pretending the original text must be copied unchanged.

The incoherent options are the two extremes:
- saying “the threshold fired but let’s preserve-only anyway,” which empties activation of force;
- or saying “the threshold fired so the minority’s exact numeric shape must be enacted unchanged,” which treats activation as an oracle.

My answer is between those. The direction was right. The exact shape should now be decided on present evidence. That is not reversal of preservation discipline. It is its intended use.

## Honest Limits

I performed workspace reads to ground this position. Specifically I read `specifications/read-contract.md`, `specifications/engine-manifest.md`, `open-issues/OI-018.md`, the aggregate-report section of `tools/validate.sh`, `provenance/027-session-assessment/03-close.md`, and `provenance/028-session-assessment/00-assessment.md`. The concrete numeric claims above rely on those reads plus the shared brief.

I did **not** read archive-surface records, the Session 024 Outsider archive-pack, or the full close-file corpus beyond Sessions 023 and 027. I also did not recompute aggregate counts from scratch independently of the validator state reported in Session 028 assessment. The main gap this leaves is that my recommendation about rotating aged `03-close.md` files is inferred from the active spec, validator behavior, and trajectory evidence, not from a full fresh audit of every close file’s marginal usefulness.
