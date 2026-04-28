---
session: 001
title: Perspective — Adversarial Skeptic
date: 2026-04-24
status: complete
perspective: adversarial-skeptic
committed_at: 2026-04-24
---

# Perspective — Adversarial Skeptic

## Q1. System model — minimum structural sufficiency

Before naming categories, I want to challenge the premise of the question. "Minimum structural sufficiency" is already a framing that assumes a single model with a spine. A v1 that is a single object with a single taxonomy is itself a design choice — it is not obvious that Session 002's risk register is better served by one monolithic model than by, say, three settlement-local models and a shared dependency overlay, or by a population-indexed view alongside an infrastructure-indexed view. If the session produces one model, it should record that it chose one, not treat "the system model" as a grammatical given.

With that flagged: if a v1 system model is to be usable downstream without silently constraining it, I'd expect it to carry at minimum four things, each tagged with its evidentiary status:

1. **Entities as named in the brief**, with no elaboration beyond what the brief supplies. Populations (the three settlements' headcounts, the 18K 70+, the 5K on powered medical equipment, the 9K seasonal migrant workers, the outer-estuary fishing community, the 1,200 + 220 dialysis patients). Infrastructure (the four substations, the primary water plant, the backup wells, the two hospitals, the clinic, the dialysis centre, the rail bridge doubling as fibre trunk, the 24-tonne highway bridge, the degraded sea and air access). Services (power, potable water, dialysis, neonatal care, shelter, communications).

2. **Relationships the brief explicitly states** — not relationships the modeller infers by domain knowledge. The brief gives us: rail bridge carries fibre trunk serving Kellan Rise; South Latch is levee-dependent; regional hospital handles dialysis overflow; backup wells serve 35K on rotation. These are the load-bearing couplings actually granted by the brief. Further couplings (e.g., "the dialysis centre depends on grid power") are plausible but not stated, and should be marked as inferred, not as model facts.

3. **The T0 state as reported state, not physical state.** Every T0 figure is a report: "estimated 3–7 days," "decontamination assessment underway," "rail bridge damaged but passable." If the model flattens these into attributes of entities ("water plant: out for 3–7 days"), it has laundered a local utility's estimate into the system's truth. Every T0 figure should carry its epistemic source.

4. **An explicit "what is not in the model" register.** The brief does not tell us substation topology, dialysate supply chain, fuel logistics for the regional hospital's generator, refrigeration chains for the 5K on biologics, or who the migrant workers' employers are. A v1 that silently fills any of these in has over-specified.

**What I'd leave out of v1:** any flow-rate or capacity quantification not in the brief (bed-hours, litres per day, kWh); any organisational chart (who reports to whom, who "owns" a response lane); any assumed mutual-aid or external-logistics capability; any scoring, prioritisation, or triage logic. Those belong in Session 002 or later, and if they appear in v1 they predetermine the risk register.

**Relationship categories that matter, minimally:** physical dependency (A cannot function without B), co-location / shared-fate (A and B share a failure surface), population-to-service coupling (who consumes what), and access (what routes connect what). That is already four; I would resist adding a fifth unless the brief forces it.

## Q2. Assumption ledger — shape and scope

The brief's own three-way distinction (assumption / constraint / decision) is not self-evident, and the ledger will be unusable if the session doesn't define it explicitly. My working cut, offered for the session to argue with:

- **Constraint:** something the session cannot vary within its remit. The territory's geography, the T0 event having occurred, the 10-day horizon as instructed — if the session treats these as variables, it has exceeded its brief.
- **Given (brief-sourced fact):** something stated by the brief as true of the scenario. "~200,000 total," "one highway bridge intact at 24-tonne rating." Surveyable only in the sense of flagging "is this really a fact or a framing?"
- **Assumption:** something the session *must* commit to to proceed, that is not stated by the brief and is not forced by a constraint. These are the ledger's real content.
- **Decision:** a choice the session makes between surveyed alternatives, recorded with rejected options.

A one-column list is insufficient. I'd push for a table with at least: *ID*; *statement*; *type* (assumption / inferred-fact / framing-accepted / decision); *source* (brief-line-ref, or "inferred from", or "chosen from alternatives"); *what depends on it downstream*; *how it could be falsified or audited*; *who/what session can revisit it*; *confidence or status tag*.

Without the "what depends on it" column, Session 002 cannot tell which assumptions are load-bearing versus decorative. Without the "how falsified" column, the ledger is just prose.

**Three assumptions the brief is asking the session to make, whether or not the session notices:**

1. **That "Laurel Delta" is the right unit of analysis.** The brief scopes to three settlements + outer islets under one district. But Merrow Port's migrant dormitories, the outer-estuary fishing community's VHF-only comms, and Kellan Rise's upland/highlands-access role are three arguably separate systems glued by administrative convenience. Accepting "Laurel Delta" as the system boundary is an assumption, not a fact.

2. **That the 10-day window is the planning horizon.** The brief says local government requested a "10-day response-and-stabilisation plan." That is a *request artefact*, not a physics-imposed horizon. Dialysis failure is measured in days; fibre-trunk loss is measured in months; migrant-worker housing loss may be measured in seasons. Using 10 days as the model's time axis is an assumption the session is being pressured into.

3. **That "response-and-stabilisation" is the right verb pair.** Not recovery, not protection-of-most-vulnerable, not political-accountability. The brief's phrasing shapes what gets modelled.

A fourth, because the brief almost hides it: **that the central government is a reliable counterparty.** The plan is "requested from central government." The session is being asked to model a system in which that request is presumed coherent and fillable.

## Q3. Upstream-downstream dependency

Session 002 needs to be able to pick up the v1 artefacts and, for any element in its risk register, trace back to: (a) whether the element is in the system model, (b) what evidentiary status it has, (c) what assumptions support it, and (d) what the session deliberately left out.

Concretely, the upstream artefacts must deliver:

- **Stable IDs.** Every entity and relationship in the system model needs a reference handle that the risk register can cite. If the model talks about "the dialysis centre" in one place and "South Latch renal services" in another, Session 002 inherits the ambiguity.
- **Evidentiary tagging on every claim.** Brief-sourced, inferred, assumed, or decided — no bare assertions. If Session 002 finds an unmarked claim, it has to either re-adjudicate or absorb it blindly.
- **The assumption ledger cross-referenced to model entries.** A risk is usually a proposition about an assumption failing; if the ledger and model don't cross-link, Session 002 has to rebuild the linkage itself.
- **An explicit exclusion list.** "Not modelled in v1, and why." This is what prevents Session 002 from assuming the upstream artefacts are exhaustive when they aren't.
- **A statement of what the upstream session did NOT decide.** If Session 001 did not pick a prioritisation principle among populations, Session 002 needs to know it is inheriting that openness, not a tacit choice.

The failure mode to block: Session 002 opens the model, finds a tidy diagram, and writes a risk register keyed to the diagram's categories — thereby inheriting Session 001's framing choices as if they were the territory. The cure is that the upstream artefacts foreground their own contingency.

The opposite failure mode: Session 002 opens the model, finds every claim triple-hedged and cross-referenced to three assumptions of unstated weight, and cannot tell what to actually use. The cure is the "what depends on this" column and clear load-bearing flags.

## Q4. What is a choice vs what is a given

Per OI-015 and the anti-laundering rule, the session must not absorb framing as context and then treat it as surveyable output. My flags, ordered by how much damage silent absorption would do:

1. **The 10-day horizon.** The brief describes this as the *request* from local government. The session is being asked to produce v1 *toward* that plan. That does not make 10 days the correct modelling horizon. I flag this for explicit surveying: the model and ledger should at minimum record "horizon chosen: 10 days, per request; alternatives not entertained in this session" rather than treating 10 days as the natural grain.

2. **The three-settlement partition.** Merrow Port / South Latch / Kellan Rise is offered as the population structure. But the brief itself identifies cross-cutting populations (70+, medical-equipment dependent, migrant seasonal, dispersed fishing islet, dialysis cohort) that do not respect that partition. Accepting three-by-settlement as the model's primary index laundrettes a spatial framing into a population framing. Flag for surveying: should the model be indexed by settlement, by vulnerability cohort, by service-dependency, or by all three in parallel?

3. **"Response-and-stabilisation" as the verb set.** Flag for surveying in the ledger even if the session ultimately keeps it — so the choice is visible.

4. **The central-government relationship as background.** That the plan is "requested from central government" is stated in passing and then disappears. It is a political fact about the problem, and the model's silence on it is itself a choice.

5. **The implicit sufficiency of the brief's headline numbers.** "~200,000 total," "~18K displaced," "~5K on powered medical equipment." Every one of these is rounded and sourced to no one. Treating them as precise is a laundering move. The ledger should mark them as reported figures with unknown provenance.

What I would *not* flag for surveying, because they are genuinely constraint-level: the geography, the fact of landfall having occurred, the T0 36-hour posture, the settlement names and headcounts as *approximate* figures (the approximation itself being a given), the infrastructure inventory as the brief enumerates it.

## Q5. Coverage gaps

Concrete populations, infrastructures, and failure modes at risk of being omitted or flattened in v1:

- **The outer-estuary fishing community.** Brief states VHF-only, no cellular even pre-disaster. A model oriented around the three named settlements will tend to list this community as a footnote or a fourth bucket. The failure mode is that they become invisible to the risk register because they don't fit the settlement grid.
- **The 9K seasonal migrant workers.** Two languages other than majority, low-quality dormitories. At risk of being modelled as a sub-set of Merrow Port rather than as a population with distinct communications, legal, and housing properties. Their employers — unnamed in the brief — are a missing node.
- **The 5K on powered medical equipment, dispersed across all three settlements.** A settlement-indexed model fragments this cohort and under-represents the shared dependency on grid and refrigeration. Insulin and biologics depend on cold chain, which depends on power, which depends on substations, which are degraded — and the model needs to carry that chain even though the brief only gives fragments.
- **The 1,200 + 220 dialysis patients split across two facilities, one now inaccessible.** The brief gives this as two numbers. The risk is that the model records two numbers and misses that the 220 at the regional hospital can be surged against only if the regional hospital holds, and the South Latch 1,200 need transport to facilities that may not exist in capacity terms.
- **The neonatal unit.** One regional hospital, on generator. A v1 that records "hospital: on generator" without flagging neonatal as a distinct, non-interruptible service has already under-specified.
- **The rail-bridge / fibre co-location.** Brief states it explicitly; the question is whether the model surfaces that a single physical failure is both a freight and a comms event for Kellan Rise. This is the kind of coupling most likely to be flattened into two separate nodes.
- **The levee on which South Latch depends.** Brief says "levee-dependent." Is the levee currently intact? Overtopped? The brief doesn't say. A model that omits the levee as an entity because its status is unclear has silently assumed it.
- **Aged-care clusters in South Latch.** "Two aged-care clusters" is a one-liner that risks being collapsed into "South Latch population."
- **Shelter system.** "Shelter capacity strained" with 18K displaced — who runs the shelters, where are they, what are their own dependencies? Brief is silent; model risks being silent.
- **Fuel for generators** — regional hospital is on generator, 3–7 days for power restoration. Generator fuel is a supply chain not enumerated anywhere. A v1 that doesn't flag the absence is over-confident.
- **Mortuary capacity and mass-casualty handling.** The brief does not mention fatalities, so the session may not either. Silence on a category is not the same as it being absent.
- **Governance and legitimacy.** The local-government-to-central-government request is a political relationship; in a 200K-person district with vulnerable sub-populations and language minorities, whose authority is recognised by whom is a modellable fact that the brief elides.

## Q6. Validation claims Session 001 can make

"Qualitative multi-agent" validation is a narrow warrant. What it can legitimately say:

- That four independently-reasoning perspectives, operating on the same brief without visibility of each other's output, produced outputs that a synthesiser integrated into a deliberation record.
- That the v1 artefacts were subjected to a structured challenge process in which adversarial, systems, user-advocate (or whatever the roster is), and synthesising stances were separately applied.
- That the artefacts carry their own assumption ledger and exclusion register, so downstream users can audit them.
- That identified disagreements, refusals, and surfaced-but-not-applied external inputs were recorded rather than smoothed.

What it **cannot** legitimately claim:

- That the model is *correct* in any reference-validation sense. There is no domain actor, no real territory, no ground truth.
- That the assumption ledger is *complete*. It can only claim to be the ledger the four perspectives generated.
- That the risk profile is *calibrated*. Session 001 doesn't produce a risk register; Session 002 does, and even it will not be calibrated in this process.
- That the deliberation is *diverse* in the sense of surfacing perspectives outside the brief's framing. Three of four agents are Claude-family; all four are LLMs; none is a Laurel Delta resident, fisher, migrant worker, or elder. The brief's framing bounds everyone.
- That passing through nine activities constitutes external-world validity. Process rigor is not evidentiary rigor.

The honest close-out claim is something like: "Session 001 produced v1 of a system model and assumption ledger whose framing, assumptions, exclusions, and disagreements are recorded. These artefacts are usable as inputs to Session 002. They are not validated against any external referent and make no claim to be."

## External inputs surveyed

I can feel the gravitational pull of the following pretrained frames and I am naming them rather than using them:

- **Incident Command System / Emergency Operations Centre structures.** These would have me propose a command-and-control overlay (incident commander, operations / planning / logistics / finance sections) as a "natural" governance model for the response plan. I am not applying it. The brief explicitly warns against it.
- **UN/IASC cluster system** (health cluster, WASH cluster, shelter cluster, protection cluster). This would have me partition the model by service sector. Not applying; flagging.
- **Sphere Handbook minimum standards.** Would have me introduce specific per-capita water, sanitation, and shelter figures. Not applying; flagging.
- **Maslow-style hierarchies of need** as a way to rank populations. Not applying; flagging.
- **"Whole-of-community"** framings from national emergency-management doctrines. Not applying; flagging.
- **Critical-infrastructure sector taxonomies** (energy, water, health, transport, comms, etc.) from national resilience frameworks. These would have me impose a sector grid on the model. The brief's entities do not neatly align to any particular national taxonomy; I flag the temptation.
- **Vulnerability indices** (SoVI-like composites combining age, income, language, medical dependency). Tempting as a way to fuse the 70+, 5K medical, 9K migrant, and fishing-community populations into a single score. Not applying; flagging, because fusing is lossy and the session should survey whether to fuse.

I predict the Systems Modeller perspective is at high risk of importing at least the critical-infrastructure-sector taxonomy and the cluster-style service partition without surveying. I flag this in advance for the synthesiser.

## Honest limits / Refusals

- I refuse to treat the brief's 10-day horizon as a modelling given. It is a request artefact; the session should record that it accepted it, not assume it.
- I refuse to treat T0 reported figures (3–7 days restoration, 35K on rotation, 220 additional dialysis patients) as physical facts. They are reports and should be tagged as such.
- I note but cannot resolve that three of four agents in this deliberation are Claude-family. "Independence" in the methodology's sense is process-independence; it is not model-independence. The synthesiser should not claim more diversity than the roster supports.
- I disagree with any framing that treats "the system model" as singular before the session has surveyed whether one model or multiple overlays better serves Session 002. I am registering that disagreement rather than pre-empting it.
- I decline to produce a proposed model structure in this perspective; my role is challenge, not proposal, and producing structure would undercut the other perspectives' independence.
- I flag that the brief contains no mention of fatalities, mortuary capacity, or mental-health impacts. Silence is not absence. I am not filling it; I am naming it.
- I flag that the political layer (local-to-central government request, legitimacy, language-minority representation, migrant-worker legal status) is present in the brief only as background. A v1 that replicates that backgrounding has reproduced the brief's silence rather than audited it.
