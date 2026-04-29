---
session: 128
title: fr-null-state-annotation — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **medium**: monitor_external._me_collect_close returns only raw next_session_should text without null_state annotation; cross-workspace transport drops the flag.
  - **adjudicated.** monitor_external transports to a foreign substrate where null-state classification is the consumer concern; out of scope for OI-S126-4 local-queue framing.
- **low**: prompts/development.md section 8.5 step 2 does not mention null-state items as disposition candidates after annotation lands.
  - **adjudicated.** Spec bump prompt-development v7 to v8 for one-line wording is ceremony; the [null-state] tag is self-explanatory at orient time.

## Terminal passes

- **iteration 1** — clean @ `10be688`
  - Iter-1 review surfaced 2 findings (1 medium, 1 low); both adjudicated as out-of-scope spec coherence.
