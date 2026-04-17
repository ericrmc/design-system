---
session: 001
title: Landscape Survey of Design Methodologies
date: 2026-04-17
status: complete
---

# Landscape Survey: How People Have Designed Complex Things

This survey was conducted as the first act of a new design methodology that intends to be domain-general, AI-participatory, self-hosting, and provenance-preserving. The goal is not an exhaustive catalog but a usable map of what exists, organized by what each tradition contributes to our thinking and where each breaks down.

## 1. Sequential Stage Models

**Waterfall** (Royce, 1970) and **Stage-Gate** (Cooper, 1990) impose a linear progression: requirements, then design, then build, then test, then deploy. Each stage produces documents that gate entry to the next.

*What they get right:* Clear milestones. Traceability from requirements to artifacts. Forced completeness — you must think about the whole before building any part.

*Where they fail:* They assume the problem is knowable upfront. Change is punished rather than accommodated. The documents they produce tend to describe intentions rather than reality, and the gap between the two widens as the project proceeds. In domains with genuine uncertainty, they produce false confidence.

*What to take:* The idea that transitions between stages should be explicit and gated — not by documents, but by demonstrated understanding.

## 2. Agile and Iterative Approaches

The **Agile** family (Scrum, XP, Kanban, and the 2001 Manifesto that unified them) arose as a reaction to sequential models. Work proceeds in short iterations. Working artifacts are the primary measure of progress. Plans are adjusted continuously based on what is learned.

*What they get right:* Short feedback loops. Preference for working output over comprehensive documentation. Acknowledgment that requirements evolve. The principle that the people doing the work should organize it.

*Where they fail:* "Working software" as the primary measure of progress is too domain-specific. Agile can devolve into a series of disconnected sprints with no architectural coherence. The oral-tradition culture of many Agile teams (standups, retros, conversations) means reasoning is lost when people leave. Velocity metrics create perverse incentives.

*What to take:* Iterative refinement. The principle that artifacts should demonstrate their own correctness rather than asserting it through documents. The idea that process should serve the work, not the other way around.

*What to reject:* Time-boxing (sprints are an organizational convenience, not a design principle). Fixed roles (Scrum Master, Product Owner) that don't generalize across domains.

## 3. Systems Engineering

**Classical Systems Engineering** (INCOSE, NASA NPR 7123, DoD MIL-STD-498) was built for domains where failure is catastrophic: aerospace, defense, nuclear, medical devices. It emphasizes requirements decomposition, traceability matrices, interface control documents, verification and validation at every level.

*What they get right:* Requirements traceability — every specification traces to a need, every test traces to a specification. Interface management — explicit agreements about how components interact. Verification matrices — a systematic way to demonstrate that what was built matches what was specified.

*Where they fail:* Crushing ceremony. The documents become an end in themselves. The cost of maintaining traceability across thousands of requirements makes change prohibitively expensive. The culture tends to be risk-averse to the point of paralysis.

*What to take:* Traceability as a concept (though not necessarily in matrix form). The discipline of interface specification. The principle that verification should be planned at the same time as the thing being verified, not after.

## 4. Design Thinking and Human-Centered Design

**Design Thinking** (d.school, IDEO) and the broader **Human-Centered Design** tradition structure work as: empathize with users, define the problem, ideate solutions, prototype, test. The **Double Diamond** (Design Council, 2004) frames this as two diverge-converge cycles: one for the problem, one for the solution.

*What they get right:* Starting with the problem, not the solution. Divergent thinking before convergent thinking — generating options before choosing. Rapid prototyping as a thinking tool, not just a validation tool. The recognition that who you design for shapes what you design.

*Where they fail:* The empathy phase can become superficial ("innovation theater"). The framework assumes human users as the primary stakeholders, which doesn't generalize to all domains. The process doesn't scale to highly technical or deeply constrained design problems.

*What to take:* The diverge-converge rhythm. The principle that understanding the problem precedes solving it. Prototyping as thinking, not just building.

## 5. Christopher Alexander's Pattern Language

Alexander's **Pattern Language** (1977) proposed that good design emerges from applying well-understood patterns in combination. Each pattern names a recurring problem, describes its context, proposes a solution, and connects to related patterns at larger and smaller scales.

*What it gets right:* Named patterns create a shared vocabulary. The compositional structure (patterns refer to other patterns) mirrors how complex things actually work. Context is explicit — a pattern doesn't claim to be universal, it claims to work in specific situations.

*Where it fails:* Patterns can calcify. Once named, they resist evolution. Quality criteria ("the quality without a name") are subjective and hard to operationalize. The approach is better at capturing what works than at discovering what might work.

*What to take:* Named, composable solutions with explicit context. The idea that design knowledge should be transmissible through structured descriptions, not just apprenticeship.

## 6. Architecture Decision Records

**ADRs** (Nygard, 2011) are lightweight documents that capture a single architectural decision: context, decision, status, consequences. They accumulate over time into a decision log.

*What they get right:* Lightweight enough to actually get written. Decision-centric rather than document-centric. Immutable — old decisions aren't edited, they're superseded. The format is simple enough to be adopted without training.

*Where they fail:* They record decisions but not the deliberation that led to them. "Context" is usually a paragraph, not a reconstruction of the reasoning. They're disconnected from the artifacts they govern — the ADR says "we chose X" but doesn't link to where X is implemented or how to verify it.

*What to take:* The principle of recording decisions as immutable, supersedable artifacts. The lightweight format. The status lifecycle (proposed → accepted → deprecated → superseded).

*What to improve on:* Richer provenance — not just the decision, but the alternatives considered, the arguments for and against each, and who (or what perspective) advocated for what.

## 7. Domain-Driven Design

**DDD** (Evans, 2003) organizes software design around the domain it models. Key concepts: ubiquitous language (a shared vocabulary between developers and domain experts), bounded contexts (clear boundaries around areas of the model), strategic design (deciding which parts of the domain deserve deep modeling).

*What it gets right:* Language as a design tool — agreeing on terminology reduces ambiguity and exposes conceptual gaps. Bounded contexts prevent modeling everything the same way. The distinction between strategic and tactical design.

*Where it fails:* Heavily software-specific vocabulary. Assumes domain experts are available and engaged. The strategic/tactical split can discourage deep modeling where it's actually needed.

*What to take:* The emphasis on shared vocabulary as a design artifact. Bounded contexts as a way to manage complexity by drawing boundaries. The principle that the language used to describe a system shapes the system itself.

## 8. Axiomatic Design

**Axiomatic Design** (Suh, 1990) proposes two axioms: the Independence Axiom (maintain independence of functional requirements) and the Information Axiom (minimize the information content — i.e., choose the simplest design that satisfies the requirements).

*What it gets right:* A formal framework for decomposition. The independence axiom is a powerful heuristic — coupling between functional requirements signals a design problem. The information axiom provides a criterion for choosing among alternatives.

*Where it fails:* Requires precise functional decomposition upfront, which is often the hardest part. The axioms are more useful as diagnostic tools ("is this design coupled?") than as generative ones ("what should I design?").

*What to take:* Coupling as a diagnostic signal. Simplicity as a design criterion, not just an aesthetic preference.

## 9. TRIZ (Theory of Inventive Problem Solving)

**TRIZ** (Altshuller, 1946-1985) systematized invention by analyzing thousands of patents. Key concepts: contradictions (the real design problem is often a contradiction between competing requirements), inventive principles (40 standard ways to resolve contradictions), evolution patterns (technologies evolve along predictable trajectories).

*What it gets right:* Contradictions as the unit of creative work — instead of compromising, find a way to satisfy both sides. The abstraction of solutions from specific domains to general principles. The idea that evolution has patterns.

*Where it fails:* Steep learning curve. Heavy taxonomy. Primarily developed for physical systems, though practitioners have extended it. Can feel mechanical in domains where the design space is poorly understood.

*What to take:* The concept of contradiction as productive tension. The principle that good solutions resolve contradictions rather than trading them off. Evolution patterns as something to look for as the methodology matures.

## 10. Cynefin and Sense-Making Frameworks

**Cynefin** (Snowden, 1999) distinguishes five domains: clear (cause and effect are obvious), complicated (cause and effect are discoverable by expertise), complex (cause and effect are only coherent in retrospect), chaotic (no perceivable cause and effect), and confused (not yet categorized). Each domain requires a different approach.

*What it gets right:* Not all problems are the same kind of problem. A methodology that works for complicated problems (analyzable, decomposable) fails in complex ones (emergent, irreducible). The framework prevents the dangerous mistake of applying certainty-based methods to uncertainty-laden domains.

*Where it fails:* Descriptive, not prescriptive — it tells you what domain you're in, but not what to do once you know. Categorization itself can be contested. The framework is hard to operationalize.

*What to take:* Domain-sensitivity. The methodology should have different modes for different kinds of problems, or at minimum should diagnose which kind of problem it's facing before prescribing an approach.

## 11. Zettelkasten and Networked Knowledge

**Zettelkasten** (Luhmann) is a method of knowledge management built on atomic notes connected by links. Knowledge emerges from the network of connections rather than from hierarchical organization.

*What it gets right:* Atomic units (one idea per note) are easy to create, link, and reorganize. The network structure mirrors how knowledge actually relates — not as a tree but as a graph. Surprise comes from unexpected connections.

*Where it fails:* It's an individual practice with no collaboration model. There's no validation mechanism — bad ideas persist alongside good ones. No built-in way to distinguish settled knowledge from speculation.

*What to take:* Atomic, linkable units of knowledge. The principle that structure should emerge from connections, not be imposed top-down.

## 12. Viable System Model and Cybernetics

The **Viable System Model** (Beer, 1972) applies cybernetic principles to organizational design. A viable system has five subsystems: operations, coordination, operational management, strategic management, and identity/purpose. The model is recursive — each viable system contains viable systems.

*What it gets right:* Recursion as a structural principle — the methodology should work at any scale. Requisite variety — a system's regulatory mechanisms must match the complexity of what they regulate. Self-regulation through feedback loops rather than external control.

*Where it fails:* Highly abstract. Difficult to apply directly without significant interpretation. The cybernetic language is unfamiliar to most practitioners.

*What to take:* Recursion (the methodology should work at different scales). Feedback loops as a regulatory mechanism. The principle that the methodology's complexity should match the complexity of what it designs, and no more.

## 13. Design Science Research

**Design Science Research** (Hevner et al., 2004; Peffers et al., 2007) provides a framework for rigorous design in academic contexts. The core cycle is: identify problem → define objectives → design and develop → demonstrate → evaluate → communicate.

*What it gets right:* The build-evaluate cycle. Insistence that a designed artifact must be evaluated, not just described. Contribution to a knowledge base — what was learned has value beyond the specific project.

*Where it fails:* Academic overhead. The communication step is oriented toward journals and conferences, not practitioners. The framework can make simple work ponderous.

*What to take:* The build-evaluate cycle as a core rhythm. The idea that the methodology should contribute to its own knowledge base over time.

## 14. Theory of Change and Logic Models

**Theory of Change** (Weiss, 1995) works backward from desired outcomes to identify necessary preconditions and interventions. **Logic Models** map inputs → activities → outputs → outcomes → impact.

*What they get right:* Making causal assumptions explicit. Working backward from goals forces clarity about what you actually need. The distinction between outputs (what you produce) and outcomes (what changes as a result).

*Where they fail:* Can become compliance theater — a diagram that satisfies funders but doesn't guide work. Hard to update when assumptions prove wrong. Linear causal chains misrepresent complex systems.

*What to take:* Making assumptions explicit and testable. The output/outcome distinction (did we produce the artifact, and did it achieve what it was supposed to?).

---

## Cross-Cutting Themes

Several patterns emerge across these traditions:

**What the best methodologies share:**
- They make reasoning explicit and preservable
- They have a rhythm — propose, challenge, decide, build, validate
- They handle uncertainty rather than assuming it away
- They produce artifacts that outlive the process that created them

**Common failure modes:**
- Ceremony overtakes substance (the process becomes an end in itself)
- Artifacts become stale because updating them is too expensive
- Single-perspective bias (whoever is loudest or most senior wins)
- Loss of provenance (decisions survive but reasoning doesn't)
- Rigidity (the process can't adapt to what it discovers)

**What AI participation changes:**
- Reading the full history of a project's reasoning becomes cheap — AI can process everything in seconds, making provenance more valuable because it will actually be read
- Multiple genuine perspectives can be convened without assembling a team of people
- Specifications can be checked against reality continuously, not just at milestones
- The ceremony problem is inverted — the expensive part is no longer writing documents but ensuring the documents say something true
- Institutional memory is only as good as what's written down; there's no tribal knowledge to fall back on
