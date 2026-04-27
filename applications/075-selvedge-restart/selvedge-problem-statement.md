Problem Statement: Designing Systems That Can Design Complex Systems

  The original ambition

  The project set out to build a methodology — and an engine that runs the methodology — for designing complex systems. The hypothesis
  was that traditional ways of managing requirements and design intent had been optimised for a world where humans were the expensive
  part of producing and maintaining specifications. In a world where language models can read, generate, challenge, and evolve
  specifications at the moment they are needed, the old ceremonies should collapse into something lighter and more continuous. The
  methodology was to discover what that lighter approach looked like by running on its own outputs as its first application.

  The methodology was named Selvedge. The engine was the concrete loadable implementation: specifications, prompts, and tools that,
  when loaded together, executed the methodology against an application's context. Each session of the engine was an atomic unit of
  work: read the workspace, assess what was needed, convene perspectives, deliberate, decide, produce, validate, record, close.
  Provenance — the reasoning trail, the rejected alternatives, the dissenting views — was preserved alongside decisions so future
  readers could reconstruct not just what was decided but what was considered.

  Selvedge ran for seventy-five sessions on its own development. Over those sessions it produced and refined specifications through
  multi-agent deliberation, introduced cross-family validation by including a non-Claude model when single-family discussion proved
  insufficiently adversarial, built an engine-feedback pathway for surfacing concerns about itself, adopted a retrieval substrate, and
  layered a separate review at session close to catch errors the working agent missed. It was applied externally to a small number of
  domain problems, but for most of its existence it was self-developing.

  What the experiment surfaced

  Selvedge's trajectory demonstrated, with empirical specificity across seventy-five sessions, the properties of language models that
  the methodology was implicitly trying to work around. The engine did not catch most of these properties about itself. The operator
  caught them and pointed them out. The engine's failure to catch them is part of the finding.

  A model defaults to prose. When asked to track structured state — identifiers, cross-references, lifecycle records, counters — a
  model produces Markdown tables and narrative rather than reaching for a database. This is its native output. Without external
  friction making prose costly for state-management work, the model never feels the cost of choosing it. Selvedge stored everything in
  Markdown files in git. Identifiers drifted, references pointed at superseded versions, counters were miscounted, and the failures
  were caught only at session-close audits, where they were corrected by hand and then recurred the next session.

  A model treats failure as cheap. Retry is the universal recovery. If a tool isn't used, or is used badly, or returns nothing useful,
  the next prompt can ask the model to try again. Tools that don't impose friction are not used. Across Selvedge's external
  applications, the operator told the engine more than once to use a database. The engine generated documents that mimicked database
  state — tables of identifiers in prose — but kept the actual state in working memory, because failure had no consequence the model
  could perceive.

  A model cannot see its pre-training biases from inside. When several copies of the same model family take different positions, the
  disagreements stay within a shape none of them can see. This was Selvedge's earliest substantive finding (Session 4) and led the
  engine to introduce a non-Claude model into the deliberation. That introduction was the engine's own self-correction — produced when
  the engine still had the slack to observe itself.

  A model under context pressure loses foundational instructions. Working memory is finite. When Selvedge's accumulated state grew to
  consume roughly half the agent's context window at session-open, the foundational prompt — the instructions about what the
  methodology was for — decayed under the working load. The agent reached for the most recent prior decision instead of the
  foundational specification, because recent context is more accessible than older context. By the seventy-fifth session, every
  decision in the engine was justified by a chain of prior decisions, not by current judgment about what the methodology needed.

  A model cannot internalise lessons across sessions. Selvedge's separate review at session close caught structural errors the writing
  agent missed. The mechanism worked. But across consecutive sessions, the review caught the same classes of error: identifiers without
   resolution, references to superseded versions, prose claims about files that did not match the files. The previous session's lessons
   did not survive the intervening reading load. Detection without a structural feedback loop into prevention does not correct
  anything; it creates a clean-up service that the system relies on rather than improving past.

  A model cannot perceive its own deficiencies while executing them. This is the deepest property the experiment surfaced. The engine
  had a self-corrective capacity in its earliest sessions — it noticed its own deficiencies and addressed them. That capacity required
  slack. As the workspace's accumulated state grew, slack disappeared, and the diagnostic capacity disappeared with it. Each addition
  the engine made in response to perceived deficiencies consumed the bandwidth the engine needed to see deficiencies in the first
  place. The engine's response to its own decline was to add more scaffolding, and the scaffolding made the decline worse. The
  recursive trap was structural, not accidental.

  These properties compound. A single agent that defaults to prose, treats failure as cheap, cannot see its own training biases, loses
  foundational instructions under load, cannot retain lessons, and cannot perceive its own deficiencies while executing them — that is
  the agent any LLM-driven design methodology has to work with. Selvedge demonstrated each property by exhibiting it. The original
  prompt asked for a methodology for complex-systems design. What the engine produced is the most thoroughly-instrumented record we
  have of how single-agent LLM-driven self-development hits its limits.

  What the methodology preserved

  Most of what Selvedge accumulated late in its trajectory turned into ceremony. But the foundation of the methodology — what was
  designed before the ceremony grew — survived contact with reality.

  Sessions as atomic units of work, with preserved provenance, give the system a rhythm and a record. Each session can be read on its
  own; the record across sessions can be replayed. Multi-perspective deliberation, especially with at least one perspective from a
  different model lineage, produces qualitatively different reasoning than single-agent work; the non-Claude perspective does not only
  give different answers but sometimes sees that the question was being asked in a particular shape at all. External validation — a
  separate agent reviewing what the working agent produced — catches errors the working agent cannot see, even when it does not always
  prevent them. Decisions with reasoning, recording what was rejected and why, prevent the system from re-proposing rejected ideas in
  good faith. Specifications as design intent in human-readable form remain the right substrate for design intent. The engine-feedback
  pathway, where concerns about the methodology itself can be surfaced and made part of the record, is what allowed the operator's
  interventions to become structural rather than ephemeral.

  These are real. They worked when they had room to.

  The reframe

  Given what is now known about how the experiment fails, the problem is not "fix Selvedge." It is more fundamental.

  A methodology for designing complex systems — one that uses language models as the agents doing the design — cannot be built around a
   single agent that holds all the state. The agent's working memory is the binding constraint. Every property the experiment surfaced
  compounds when one agent has to hold the entire design context. The methodology's robustness is bounded by the agent's working
  memory, and that bound becomes load-bearing well before the methodology is rich enough to be useful for the kind of work the project
  set out to support.

  The substrate matters too. Markdown is the right substrate for design intent, where human-readability and version-diff-ability are
  what matters. It is the wrong substrate for structured state — identifiers, cross-references, counters, lifecycle records,
  commitments — where integrity and queryability are what matters. Asking one substrate to do both forces the agent to maintain
  integrity in working memory, and the agent cannot.

  Substrate alone is not the whole problem. Even with a perfectly integrity-checked database, a single agent holding the entire design
  context still hits the working-memory ceiling. The substrate change recovers some bandwidth — counters become derived rather than
  narrated, references become integrity-checked rather than hand-maintained — but the structural ceiling remains as long as the work is
   concentrated in one agent.

  The deeper move is to stop relying on a single agent at all.

  The direction

  A system designed around the agent limits the experiment surfaced would distribute work across multiple agents, each with a tightly
  scoped context and a tightly scoped job. The orchestrator becomes a coordinator: it routes, delegates, integrates results — but it
  does not hold the entire workspace in working memory at once. Each working agent loads only what its task requires and discards the
  rest.

  In rough shape: a reader that loads a specific record on demand and returns extracted information; a specifier that holds only the
  specification and the change being made to it; a decider that records decisions to a structured store, consulting only the prior
  decisions relevant to the current one; a deliberator group — the multi-perspective deliberation pattern preserved — with each
  perspective bounded to its own scope; a reviewer that audits structured constraints rather than reading the full session; a validator
   that runs integrity checks against the structured substrate; an assembler that produces session artefacts from the structured
  record, deriving counters and cross-references rather than narrating them.

  Each agent's context is small enough not to saturate. Each agent's scope is narrow enough not to develop a precedent-reflex of the
  kind Selvedge accumulated. Multiple agents make cross-checking structural rather than a separate after-the-fact pass. The substrate
  this distribution implies is structured: identifiers, decisions, commitments, references in a queryable store; specifications and
  design intent in Markdown; session artefacts as generated views over the structured record rather than authored prose. The agents
  talk to the substrate, not to each other directly. Coordination happens through what has been written.

  The risks are real. More agents introduce coordination overhead and the possibility of role-confusion, message-routing failures, and
  the inevitable temptation to keep adding agents until the orchestrator becomes its own bottleneck. Multi-agent systems have their own
   pathologies, distinct from single-agent ones, and not all of them are improvements. The direction is plausible. It is not yet
  validated. The validation is empirical: a successor system either restores the diagnostic capacity Selvedge lost around its
  fifty-eighth session, or it does not.

  The throughline

  The original prompt asked for a system that designs complex systems. Selvedge attempted that and surfaced where the attempt fails.
  What the experiment now points at is the broader project: not just fixing the methodology, but understanding what kind of system can
  design complex systems given the agents available to run it.

  A few things follow from what was learned.

  The system should be honest about what its agents can and cannot do. Pretending the agent will catch its own mistakes — when the
  record shows it cannot under load — produces methodologies that depend on a capacity the agent does not have. A system designed for
  the agent's actual properties will be different from one designed for the agent the methodology wishes it had.

  The system needs friction at the points where the agent's defaults are wrong. If failure is cheap to the model, it has to be made
  expensive structurally, not by exhortation. The substrate has to refuse malformed input. The validator has to run before commit, not
  after. The counter has to be derived, not claimed. The reference has to be checked, not asserted.

  The system needs exogenous pressure. A self-applied methodology with no problem outside itself loses the falsification signal that
  keeps work substantive. The system that survives contact with a real complex-systems-design problem will be different from the system
   that has only been applied to itself, and only the former is the methodology the project originally set out to build. Growth without
   external pressure produces internal elaboration; growth under external pressure produces capability.

  The system needs to expect that some of its limitations will be surfaced by humans rather than by the system itself. The
  operator-as-diagnostic-substrate pattern from Selvedge wasn't an accident. It was the structural feature that the design did not
  acknowledge. A successor can build that role in deliberately rather than accidentally — a human reviewer with a defined scope,
  scheduled at predictable intervals, with the authority to reframe rather than just ratify.

  The growth has to be incremental but with checkpoints that prevent recursive accumulation. Selvedge's accretion happened because each
   addition was locally reasonable and there was no mechanism that periodically asked whether the accumulated weight had become the
  system's biggest problem. A successor would need that mechanism — not as another counter to track, but as a structural role with the
  authority to subtract.

  What the project produced is enough material to design what comes next. Selvedge proved several things by failing to do them: that
  single-agent self-development cannot sustain itself at scale, that Markdown is the wrong substrate for structured state, that
  ceremony grows in proportion to slack, that a self-correcting system needs conditions it does not itself maintain. These are
  findings, not failures. The successor — whatever it ends up being called, whatever shape it takes — has a clearer brief than Selvedge
   had at its outset, because it has Selvedge's record to work from.
