tion.md` | Defines multi-perspective deliberation triggers, non-Claude participation, recording schema. |
| `specifications/validation-approach.md` | Two-tier validation: structural checks and guided-assessment questions. |
| `specifications/workspace-structure.md` | Defines file classes, top-level structure, provenance conventions. |
| `specifications/identity.md` | Records the name Selvedge and the three-layer denotation. |
| `specifications/reference-validation.md` | Defines reference-validation as the third sense of validation. |
| `specifications/engine-manifest.md` | **This file.** |
| `tools/validate.sh` | Executable: runs the Tier 1 structural checks from `validation-approach.md`. |

An external-application workspace that clones the engine should copy (or reference) these files and nothing else from the source workspace.

### 4. What is explicitly NOT part of the engine

The following are development-provenance or application-scope; they are **not** loaded when an external application initialises:

- `SESSION-LOG.md` (development-provenance)
- `open-issues.md` (development-provenance)
- `provenance/` (development-provenance: all session records)
- `applications/NNN-*/` (application-scope: prior application outputs, not reusable as engine load)
- `specifications/*-v1.md`, `*-v2.md`, `*-v3.md` (superseded spec versions: preserved in the workspace but not active engine definition)

This manifest's own version history is also not part of the engine load; the current `engine-manifest.md` is what counts.

### 5. Versioning discipline

The engine version (`engine-v1`, `engine-v2`, ...) increments when any file in §3 changes in substance. "In substance" means:

- A new engine-definition file is added to §3.
- An existing engine-definition file receives a substantive revision (v-bump per the spec-revision discipline in `workspace-structure.md`).
- An engine-definition file is removed or superseded.

The engine version does **not** increment on:
- Typo corrections or formatting adjustments.
- Minor elaborations within an existing spec's scope (per the OI-002 substantive-vs-minor heuristic).
- Updates to development-provenance or application-scope files.
- Changes to `SESSION-LOG.md`, `open-issues.md`, or `provenance/`.

Engine-version increments are declared by a decision record in the session that executes the increment. The decision names the file(s) changed and the new engine version.

### 6. Loading the engine / minimal external-application initialisation contract

An external application workspace is initialised by:

1. **Copy the engine-definition file set** (§3) into a fresh directory (or reference them from a canonical engine repository). The copy is flat: maintain the same paths (`PROMPT.md`, `prompts/`, `specifications/`, `tools/`).
2. **Create fresh development-provenance files** in the new workspace:
   - Empty `SESSION-LOG.md` (header only).
   - Empty `open-issues.md` (header only).
   - Empty `provenance/` directory.
3. **Create the first application directory** `applications/001-<slug>/` containing at minimum a `brief.md` carrying:
   - The problem statement.
   - Constraints (domain constraints; time constraints; stakeholder constraints).
   - Stakeholders (who holds the problem; who will receive the artefact; who validates).
   - Success condition (what the artefact must do for the application to be considered successful).
4. **Select the execution prompt.** For an external-problem application, copy `prompts/application.md` to the workspace's `PROMPT.md` (or reference it), then fill in the template slots with the application-specific content from `brief.md`. For a self-development application (like this workspace), use `prompts/development.md`.
5. **Record the engine version loaded.** The first session's provenance (e.g., `provenance/001-*/00-assessment.md`) should name the engine version (`engine-v1` or later) the workspace was initialised from.
6. **Run Session 001** per the loaded execution prompt. The session Reads the application's initial state (the `brief.md` + the engine specifications), Assesses what the application's first increment should be, Convenes perspectives, Deliberates, Decides, Produces the first artefact or design fragment, Validates, Records, and Closes.

The critical rule per Outsider [Session 017 01d Q6]: **external application workspaces inherit the engine, not the engine's autobiography.** The development-provenance of the Selvedge engine's own development is preserved in this source workspace; it does not travel with the engine to an external application.

### 7. Engine version history

- **`engine-v1`** — established Session 017 via D-074. First versioned engine definition. File set per §3. Corresponds to the post-Session-017 state of the workspace: `methodology-kernel.md` v4 + scope-clarification sentence; `multi-agent-deliberation.md` v3 + minor scope-applicability sentence; `validation-approach.md` v3 + minor scope-applicability sentence; `workspace-structure.md` v3; `identity.md` v2; `reference-validation.md` v1; `tools/validate.sh` as of Session 005/006 last substantive change; `PROMPT.md` as thin dispatcher; `prompts/development.md` and `prompts/application.md` as created by D-074. Subsequent intra-engine-v1 changes (Session 019: `reference-validation.md` v1 → v2; Session 020: `workspace-structure.md` v3 minor amendment) did not bump the engine version because v3 minor amendments do not trigger §5 bump per OI-002 heuristic.

- **`engine-v2`** — established Session 021 via D-082. Substantive revisions to three engine-definition files: `multi-agent-deliberation.md` v3 → v4 (added §Criterion-4 Articulation for OI-004; §Acceptable Participant Kinds for OI-004; six new Layer 2 manifest fields; one new synthesis frontmatter field; one new session-level participants.yaml block; four-state OI-004 lifecycle with §Closure Procedure for OI-004); `validation-approach.md` v3 → v4 (added §Tier 2 Q8; documented gating conventions for new checks 16-19); `tools/validate.sh` substantive update (added checks 16, 17, 18, 19; added CRITERION4_ARTICULATION_SESSION constant; added PARTICIPANT_ORGANISATION_CLOSED_SET constant; added Tier 2 Q8 print-out). v3 of the two specs preserved as `multi-agent-deliberation-v3.md` and `validation-approach-v3.md` (both `status: superseded`). All other engine-definition files unchanged at engine-v2 boundary: `PROMPT.md`, `prompts/development.md`, `prompts/application.md`, `methodology-kernel.md` v4, `workspace-structure.md` v3, `identity.md` v2, `reference-validation.md` v2, `engine-manifest.md` (this file, frontmatter `last-updated: 2026-04-22` + `updated-by-session: 021`).

Future engine-version increments will extend this history in this section.

## Validation

To validate this specification:

1. Confirm the files enumerated in §3 all exist at the declared paths.
2. Confirm that any file NOT enumerated in §3 but present in the workspace is either (a) in §4's explicit exclusion list, or (b) a superseded spec version, or (c) clearly out-of-scope (e.g., `.git`, `.gitignore`, `.claude`, `.serena`).
3. Confirm that `identity.md` v2 references this manifest as the definition of the engine at the current version.
4. Confirm that `workspace-structure.md` v3 references the same three file-class distinction this manifest implies (engine-definition / development-provenance / application-scope).
5. When a session executes a substantive revision to an engine-definition file, confirm the session's decision record declares a new engine version in this manifest's §2 and §7.
6. When an external application workspace is first initialised, confirm its Session 001 provenance records the engine version loaded per §6.5.
7. Confirm that no engine-version increment has occurred without a decision record authorising it (guard against silent engine-version drift).

 succeeded in 0ms:
#!/usr/bin/env bash
# Methodology workspace validation tool
# Two-tier validation: automated structural checks + guided semantic questions
# Read-only: this script never modifies any files

set -euo pipefail

# Session from which the triggers_met schema is enforced (D-039, Session 006).
# Checks 14 and 15 apply only to sessions numbered >= this constant.
# See specifications/validation-approach.md v3 "Gating Conventions (checks 14, 15)".
readonly TRIGGERS_MET_ADOPTION_SESSION=6

# Session from which OI-004 criterion-4 schema is enforced (D-082, Session 021).
# Checks 16, 17, 19 apply only to sessions numbered >= this constant.
# Check 18 is presence-gated (fires only when oi-004-retrospective.md exists).
# See specifications/validation-approach.md v4 "Gating Conventions (checks 16-19)".
readonly CRITERION4_ARTICULATION_SESSION=21

# Closed set of acceptable participant_organisation values (D-082 R3, Session 021).
# Extensible by named decision per multi-agent-deliberation.md v4 §Acceptable
# Participant Kinds. Membership check used by check 19.
readonly PARTICIPANT_ORGANISATION_CLOSED_SET="anthropic openai google meta xai mistral deepseek cohere local human-individual other-named"

WORKSPACE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PASS=0
FAIL=0
WARN=0

pass() { PASS=$((PASS + 1)); echo "  ✓ $1"; }
fail() { FAIL=$((FAIL + 1)); echo "  ✗ $1"; }
warn() { WARN=$((WARN + 1)); echo "  ⚠ $1"; }

echo "=== Methodology Validation Report ==="
echo "Workspace: $WORKSPACE_ROOT"
echo "Date: $(date +%Y-%m-%d)"
echo ""
echo "--- Tier 1: Structural Checks ---"
echo ""

# [1] Required top-level files
echo "[1] Required files"
for f in PROMPT.md SESSION-LOG.md open-issues.md; do
  if [[ -f "$WORKSPACE_ROOT/$f" ]]; then
    pass "$f exists"
  else
    fail "$f missing"
  fi
done
echo ""

# [2] Required directories
echo "[2] Required directories"
for d in specifications provenance; do
  if [[ -d "$WORKSPACE_ROOT/$d" ]]; then
    pass "$d/ exists"
  else
    fail "$d/ missing"
  fi
done
echo ""

# [3] Specification frontmatter
echo "[3] Specification frontmatter"
shopt -s nullglob
specs=("$WORKSPACE_ROOT"/specifications/*.md)
shopt -u nullglob
if [[ ${#specs[@]} -eq 0 ]]; then
  warn "No specifications found"
else
  for spec in "${specs[@]}"; do
    name=$(basename "$spec")
    if ! head -1 "$spec" | grep -q '^---$'; then
      fail "$name — no YAML frontmatter"
      continue
    fi
    frontmatter=$(awk 'BEGIN{n=0} /^---$/{n++; next} n==1{print}' "$spec")
    missing=""
    for field in title version status created last-updated supersedes; do
      if ! echo "$frontmatter" | grep -q "^${field}:"; then
        missing="${missing} ${field}"
      fi
    done
    if [[ -z "$missing" ]]; then
      pass "$name — all required fields present"
    else
      fail "$name — missing:${missing}"
    fi
  done
fi
echo ""

# [4] Specification sections
echo "[4] Specification sections"
for spec in "${specs[@]}"; do
  name=$(basename "$spec")
  missing=""
  for section in Purpose Specification Validation; do
    if ! grep -q "^## ${section}" "$spec"; then
      missing="${missing} ${section}"
    fi
  done
  if [[ -z "$missing" ]]; then
    pass "$name — all required sections present"
  else
    fail "$name — missing sections:${missing}"
  fi
done
echo ""

# [5] Provenance directory naming
echo "[5] Provenance directory naming"
shopt -s nullglob
provdirs=("$WORKSPACE_ROOT"/provenance/*/)
shopt -u nullglob
if [[ ${#provdirs[@]} -eq 0 ]]; then
  warn "No provenance directories found"
else
  for dir in "${provdirs[@]}"; do
    dirname=$(basename "$dir")
    if [[ "$dirname" =~ ^[0-9]{3}-.+ ]]; then
      pass "$dirname"
    else
      fail "$dirname — does not match NNN-title pattern"
    fi
  done
fi
echo ""

# [6] Session log completeness
echo "[6] Session log completeness"
for dir in "${provdirs[@]}"; do
  dirname=$(basename "$dir")
  session_num=$(echo "$dirname" | grep -o '^[0-9]\{3\}')
  session_int=$((10#$session_num))
  if grep -qE "\|[[:space:]]*0*${session_int}[[:space:]]*\|" "$WORKSPACE_ROOT/SESSION-LOG.md" 2>/dev/null; then
    pass "Session ${session_num} in SESSION-LOG.md"
  else
    fail "Session ${session_num} missing from SESSION-LOG.md"
  fi
done
echo ""

# [7] Provenance directories non-empty
echo "[7] Provenance directory contents"
for dir in "${provdirs[@]}"; do
  dirname=$(basename "$dir")
  shopt -s nullglob
  files=("$dir"*.md)
  shopt -u nullglob
  if [[ ${#files[@]} -gt 0 ]]; then
    pass "$dirname — ${#files[@]} file(s)"
  else
    fail "$dirname — empty (no .md files)"
  fi
done
echo ""

# [8] Provenance frontmatter
echo "[8] Provenance frontmatter"
for dir in "${provdirs[@]}"; do
  for prov in "$dir"*.md; do
    [[ -f "$prov" ]] || continue
    relpath="$(basename "$(dirname "$prov")")/$(basename "$prov")"
    if ! head -1 "$prov" | grep -q '^---$'; then
      fail "$relpath — no YAML frontmatter"
      continue
    fi
    frontmatter=$(awk 'BEGIN{n=0} /^---$/{n++; next} n==1{print}' "$prov")
    missing=""
    for field in session title date status; do
      if ! echo "$frontmatter" | grep -q "^${field}:"; then
        missing="${missing} ${field}"
      fi
    done
    if [[ -z "$missing" ]]; then
      pass "$relpath"
    else
      fail "$relpath — missing:${missing}"
    fi
  done
done
echo ""

# [9] Decision record quality
echo "[9] Decision record quality"
found_decisions=false
for dir in "${provdirs[@]}"; do
  for f in "$dir"*decision*.md "$dir"*decisions*.md; do
    [[ -f "$f" ]] || continue
    found_decisions=true
    relpath="$(basename "$(dirname "$f")")/$(basename "$f")"
    if grep -qi "rejected alternative" "$f"; then
      pass "$relpath — includes rejected alternatives"
    else
      warn "$relpath — no rejected alternatives found"
    fi
  done
done
if ! $found_decisions; then
  warn "No decision records found"
fi
echo ""

# [10] Provenance immutability (basic heuristic)
echo "[10] Provenance immutability"
if command -v git &>/dev/null && git -C "$WORKSPACE_ROOT" rev-parse --git-dir &>/dev/null 2>&1; then
  uncommitted=$(git -C "$WORKSPACE_ROOT" diff --name-only -- provenance/ 2>/dev/null || true)
  staged=$(git -C "$WORKSPACE_ROOT" diff --cached --name-only -- provenance/ 2>/dev/null || true)
  if [[ -z "$uncommitted" && -z "$staged" ]]; then
    pass "No uncommitted changes to provenance/"
  else
    warn "Uncommitted changes in provenance/ (may be current session's work-in-progress)"
  fi
else
  warn "Git not available — skipping immutability check"
fi
echo ""

# [11] Multi-agent three-raw-output floor (D-028, D-030)
# Gate: a session directory containing at least one file matching *-perspective-*.md
# is multi-agent; verify ≥3 such files exist.
echo "[11] Multi-agent three-raw-output floor"
for dir in "${provdirs[@]}"; do
  dirname=$(basename "$dir")
  shopt -s nullglob
  perspective_files=("$dir"*-perspective-*.md)
  shopt -u nullglob
  if [[ ${#perspective_files[@]} -eq 0 ]]; then
    continue  # not a multi-agent session; out-of-scope
  fi
  if [[ ${#perspective_files[@]} -ge 3 ]]; then
    pass "$dirname — ${#perspective_files[@]} raw perspective files"
  else
    fail "$dirname — only ${#perspective_files[@]} raw perspective file(s); multi-agent requires ≥3"
  fi
done
echo ""

# [12] Heterogeneous-participant schema well-formedness (D-028, D-030)
# Gate: a session directory containing a manifests/ subdirectory.
# For each *.manifest.yaml in manifests/, verify D-024 required fields are present as literal keys.
# Stores per-session fail state in BLOCKED_SESSIONS (space-separated) for the sequencing
# rule (D-030 §3). Uses a flat string rather than associative array for bash 3.2 compatibility.
BLOCKED_SESSIONS=""
echo "[12] Heterogeneous-participant schema well-formedness"
D024_REQUIRED_FIELDS=(
  perspective participant_kind participant_identity
  model_family model_id model_version provider endpoint invocation_method
  sampling training_lineage_overlap_with_claude
  participant_selected_by participant_selection_method
  identity_known context_source delivered_at received_at
  raw_response_file transport_notes output_edited_after_submission
  participation_shape
)
D024_SAMPLING_SUBFIELDS=(temperature top_p max_tokens)
for dir in "${provdirs[@]}"; do
  dirname=$(basename "$dir")
  manifests_dir="${dir}manifests"
  if [[ ! -d "$manifests_dir" ]]; then
    continue  # no manifests/ directory; out-of-scope (D-030 §1)

exec
/bin/zsh -lc "sed -n '1,220p' specifications/workspace-structure.md" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
---
title: Workspace Structure
version: 3
status: active
created: 2026-04-17
last-updated: 2026-04-22
updated-by-session: 020
supersedes: workspace-structure-v2.md
---

# Workspace Structure

## Purpose

This specification defines how the workspace is organized: what directories and files exist, what each contains, and how they relate. It ensures that any agent or person reading the workspace can orient themselves quickly and knows where to find — and where to put — each kind of content.

Version 3 (Session 017, D-074) adds the three file-class distinction (engine-definition / development-provenance / application-scope) and documents `prompts/` as a new directory created by the PROMPT.md split. v2 preserved as `workspace-structure-v2.md`.

## Specification

### File classes (added v3)

Under the three-layer denotation established in `identity.md` v2 (Selvedge methodology / Selvedge engine / application), workspace files fall into one of three classes:

- **Engine-definition files** — the loadable Selvedge engine. An external application workspace may (and should) clone this set without inheriting development-provenance. Enumerated canonically by `specifications/engine-manifest.md`. At `engine-v1`: `PROMPT.md`, `prompts/development.md`, `prompts/application.md`, `specifications/*.md` (all active files in the `specifications/` directory), `tools/validate.sh`.
- **Development-provenance files** — the self-development application's own accumulated history. Not part of the engine load; not inherited by external-application workspaces by default. Includes `SESSION-LOG.md`, `open-issues.md`, and `provenance/`.
- **Application-scope files** — per-application content (inputs, outputs, application-specific briefs and notes). Mutable per the `applications/` directory rules below. Organised as `applications/NNN-<slug>/`.

The normative rule: an external application workspace may load the engine-definition set as a read-only unit (or a cloned starting point) without inheriting development-provenance. The self-development application (this workspace) carries all three classes by construction (the engine is being developed here; the provenance is the development record; the applications are the by-products).

### Top-level structure

The workspace has the following top-level structure:

```
/PROMPT.md
/prompts/
  development.md
  application.md
/SESSION-LOG.md
/open-issues.md
/specifications/
/provenance/
/tools/
/applications/
```

### PROMPT.md

The bootstrap prompt. Under v3 (D-074, Session 017) `PROMPT.md` is a thin **dispatcher**: it names the three layers (methodology / engine / application), names the two operating modes (self-development and external-problem), and points to the two mode-specific executable prompts in `prompts/`. It is part of the engine-definition file class. It may be revised, but any revision is a significant event and recorded in provenance (as it was when the v3 split occurred in Session 017). The self-development application's executable content was moved to `prompts/development.md`; the template for external-problem applications lives at `prompts/application.md`.

### prompts/

Contains the two mode-specific executable prompts created by the D-074 split. Part of the engine-definition file class.

- `prompts/development.md` — the self-development application's executable prompt. Carries the content that was in the pre-split `PROMPT.md` (minus the high-level framing moved up into the dispatcher), reframed as the engine's own self-development. This workspace's current application loads this file.
- `prompts/application.md` — the template for external-problem applications. Loads the engine by reference (engine-manifest), names the slots an external application fills (problem statement, constraints, stakeholders, success condition, initial state), and declares that development-provenance is NOT part of the application's context unless explicitly imported. An external application workspace copies this file (typically renamed to `PROMPT.md` in the new workspace, or loaded from its canonical location here) and fills in the slots.

Both files are revisable under the methodology's spec-revision discipline (significant revisions recorded in provenance; v-suffix preservation if substantive changes accumulate).

### SESSION-LOG.md

A running index of sessions for quick orientation. Each entry is one line (one Markdown table row) containing the session number, date, title, and a summary of what was accomplished. The summary length scales to session complexity: planning-only, single-perspective, or assessment-only sessions produce shorter summaries; deliberation sessions producing substantive spec revisions, cross-model influences, or external artefacts produce longer summaries calibrated to record the decision surface and load-bearing influences. The canonical detail for each session lives in its provenance `03-close.md` file; the SESSION-LOG entry is an index over that detail, not a replacement. This file is updated at the close of each session.

### open-issues.md

A list of known questions, gaps, uncertainties, and unresolved disagreements. Each entry has a brief description, the session that identified it, and its current status. Issues are removed when resolved (with a reference to the session that resolved them). This is a single file, not a directory, unless the number of issues makes a single file unwieldy.

### specifications/

Contains the living specifications that describe the methodology's current state. Each specification is a Markdown file with YAML frontmatter:

```yaml
---
title: [what this specifies]
version: [integer, starting at 1]
status: draft | active | superseded | deprecated
created: [date]
last-updated: [date]
supersedes: [path to prior version, or "none"]
---
```

The body of each specification has three sections:

1. **Purpose** — What this specification governs and why it exists
2. **Specification** — The normative content
3. **Validation** — How to verify this specification still describes reality

When a specification undergoes substantive revision, the prior version is preserved with a version suffix (e.g., `workspace-structure-v1.md`) and the new version takes the canonical filename. Minor corrections are committed through git without file-level versioning.

Status lifecycle:
- **draft** — Proposed but not yet deliberated and accepted
- **active** — Deliberated, accepted, and governing
- **superseded** — Replaced by a newer version (the `supersedes` chain connects them)
- **deprecated** — No longer relevant because the thing it governed no longer exists

### provenance/

Contains the historical reasoning records. Organized by session:

```
/provenance/
  /001-genesis/
    00-survey.md
    01-deliberation.md
    02-decisions.md
  /002-[title]/
    ...
```

Each session's provenance is a numbered directory. Files within are numbered for reading order. All provenance files use Markdown with YAML frontmatter:

```yaml
---
session: [number]
title: [title]
date: [date]
status: complete | in-progress
---
```

Provenance records are **immutable** once the session closes. Errors or retractions are recorded in subsequent sessions, not by editing past records.

### tools/

Contains tooling that supports the methodology's operations. Tools are executable scripts or programs that automate aspects of the methodology (e.g., validation, reporting). Each tool should have a corresponding specification in `specifications/`.

Current contents:
- `validate.sh` — Two-tier validation tool (see `specifications/validation-approach.md`)

### applications/

Contains **external artefacts** — work-products the methodology has produced for use outside the workspace (specifications, sequences, templates, design fragments, and the like). Organized by the session that originally produced the artefact:

```
/applications/
  /NNN-[slug]/
    [artefact-files]
```

`NNN` is the producing session's number; `[slug]` is a short descriptive name. Filenames within the directory are descriptive (not numbered for reading order) — the numbered-reading-order convention applies to provenance records only.

External artefacts are **mutable**: they may be revised by later sessions in response to domain validation (see `methodology-kernel.md` §7 Domain validation) or other feedback. Revisions update the artefact in place; the revising session's provenance records what changed and why. When an artefact is revised, any corresponding copies in the originating session's provenance directory and in prior revising sessions' provenance remain untouched (per the provenance immutability rule) and serve as historical witnesses to earlier versions.

Each external artefact file includes in its frontmatter the fields `originating_session` (the session that first produced the artefact) and, when applicable, `regularized_in_session` (the session that moved the artefact into `applications/` after the fact) and `provenance_witness_path` (the path to the frozen provenance copy, if one exists). Subsequent revisions update `last-revised-session` in the frontmatter.

**Regularization of pre-existing external artefacts.** When an external artefact was placed in a producing session's provenance directory before `applications/` existed as a defined top-level directory, the artefact is regularized into `applications/` by **copy-plus-reference**: a copy is made to `applications/NNN-[slug]/[filename]` with the frontmatter fields above; the provenance copy is not moved, modified, or deleted. The regularizing session's decision record is the authoritative cross-reference.

### Additional directories

New top-level directories may be created by future sessions when the work demands them (e.g., `implementations/`, `examples/`). Any new directory should be documented by updating this specification. `applications/` was defined by Session 009 (D-054) for external artefacts and is no longer a hypothetical example.

## Validation

To validate this specification:

1. Check that all top-level elements listed above exist in the workspace
2. Check that each specification in `specifications/` has the required frontmatter fields and three body sections
3. Check that each provenance directory follows the naming convention `NNN-title/`
4. Check that `SESSION-LOG.md` has an entry for every provenance directory
5. Check that no provenance record dated before the current session has been modified since its session closed (immutability check via git)
6. Check that each directory in `applications/` corresponds to an external artefact produced or regularized in a session whose decision record in provenance authorises its presence
7. Check that every external artefact file in `applications/` carries the `originating_session` frontmatter field; for regularized artefacts, also `regularized_in_session` and `provenance_witness_path`

exec
/bin/zsh -lc "sed -n '1,220p' specifications/methodology-kernel.md" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
---
title: Methodology Kernel
version: 4
status: active
created: 2026-04-17
last-updated: 2026-04-22
updated-by-session: 014
supersedes: methodology-kernel-v3.md
---

# Methodology Kernel

## Purpose

This specification defines the core process of the methodology: what happens during each application of the prompt, in what order, and to what standard. It is the minimum viable process — the kernel that every session follows. As the methodology matures, additional specifications may elaborate on individual activities, but this kernel defines the overall shape.

This specification defines the Selvedge methodology kernel: the abstract execution semantics that a conforming engine must realise. `specifications/engine-manifest.md` enumerates the files that constitute the current engine; `specifications/identity.md` establishes the denotation layering (Selvedge names the methodology; "Selvedge engine" denotes the current executable implementation; each session is an application of that engine). The kernel applies equally to the self-development application and to external-problem applications.

## Specification

### Application Model

The methodology advances by **sessions**. Each session is one application of PROMPT.md to the workspace. A session reads the full workspace state, determines what work is needed, does that work through multi-perspective deliberation, produces artifacts, and closes cleanly.

Each session advances the workspace by **one increment** — a coherent unit of progress that leaves the workspace in a better state than it found it. The size of an increment is a judgment call informed by the work at hand; it is not time-boxed.

### The Nine Activities

Each session performs nine activities. These are a **vocabulary, not a strict sequence**. They have a general flow (you cannot decide before you deliberate) but permit recursion (deliberation may reveal the need for more reading).

#### 1. Read

Absorb what the session will reason from before changing anything. In every session this includes **workspace reading**: the full current state of the workspace — every file, every specification, every provenance record, and, where relevant, recent version-control history. Build a complete picture of the workspace's own state.

When the session produces or revises an artefact intended for use outside the workspace, it also includes **domain reading**: the domain constraints the session operates under (stated by the user or operator in-session), cited external materials introduced into the session, and domain knowledge that the orchestrating agent surfaces explicitly as input to the work. Domain reading enlarges what must be understood; it does not permit silent import of outside ideas. Knowledge not already present in the workspace or in the session's explicit domain inputs must still be introduced through an explicit surveying or hypothesising step (per PROMPT.md). Perspective pretraining enters the session via stance briefs and perspective responses, not via §1 Read.

This is a receptive activity. Its output is understanding, not artifacts.

#### 2. Assess

Determine what state the methodology is in and what this session should address. State the determination explicitly so future sessions have a record of what was inferred.

Assessment questions:
- What is the most important work the workspace needs right now?
- Are existing specifications consistent with each other and with reality?
- Are there open issues that should be addressed?
- Is there work from a prior session that needs continuation?
- Is the methodology itself showing signs of strain (stale specifications, unaddressed issues, loss of coherence)?

This activity produces the session's **agenda**: a statement of what will be worked on and why.

#### 3. Convene

Assemble perspectives suited to the work at hand. Name each perspective, describe its stance, and record why it was chosen.

For deliberative work (where decisions will be made), at least one perspective must be **adversarial** — its role is to challenge the emerging consensus, identify unstated assumptions, and argue for alternatives.

The choice of perspectives shapes outcomes and should be treated as a design decision, not an afterthought.

When a decision meets the triggers defined in `specifications/multi-agent-deliberation.md`, perspectives must be instantiated as independent agents whose outputs are synthesised rather than as multiple voices produced within a single context. Decisions that meet those triggers but are made single-perspective anyway must record the reason.

#### 4. Deliberate

Reason together from multiple perspectives. Each perspective contributes its genuine position on the questions at hand.

Requirements:
- Perspectives state positions before hearing others (to prevent anchoring)
- Disagreements are preserved in the record, even when resolved
- Alternatives are articulated, not just dismissed
- Uncertainty is flagged explicitly

This activity produces the richest provenance. The record should capture not just conclusions but the reasoning that led to them.

#### 5. Decide

Make concrete decisions with rationale. Each decision records:
- What was decided
- Why (the key arguments that carried it)
- What was rejected and why
- What remains open

Decisions are distinct from deliberations. A deliberation explores options; a decision commits to one.

#### 6. Produce

Create or update the artifacts that the decisions warrant. This may include:
- New specifications
- Revisions to existing specifications
- Updates to open issues
- New workspace structure

Artifacts should be produced to the standard defined in their respective specifications (e.g., specifications have the required frontmatter and three sections).

#### 7. Validate

Validate the session's output at each level on which it makes claims. Three senses apply.

**Workspace validation** applies to every session. Check that:
- New specifications don't contradict existing ones
- Specifications describe the workspace as it actually is
- Provenance records are complete and well-formed
- Open issues reflect the actual state of uncertainty

**Domain validation** applies when a session produces or revises an artefact intended for use outside the workspace and a domain-actor is available. Obtain evidence from the domain-actor who holds the problem the artefact addresses — the user of a sequence, the reader of a specification, the participant in a process, or an equivalent — that the artefact functioned for its intended use. Record who performed the validation, what was tried, what happened, and whether modifications were requested. Domain validation may complete out-of-session; when it does, the receiving session records the report and decides whether it triggers revision.

**Reference validation** applies when a session produces an external-intent artefact and no domain-actor is available. A reference-validation exercise pairs the methodology's Produce step (run blind against a staged constraint tranche set whose emergent constraints surface during the run) with comparison against a pre-selected documented proven solution the Produce agents do not see. The exercise runs across a small number of sessions in a sealed three-cell protocol (Curation, Produce, Validation) specified in `specifications/reference-validation.md`. The exercise records constraint-satisfaction, structural correspondence, cross-model divergence, and a contamination audit.

**Reference validation supplies evidence about the methodology's capacity to derive artefacts under stated constraints. It does not establish that the artefact functioned in its intended use. It does not substitute for Domain validation when a domain-actor is available.** Artefacts passing reference-validation carry the label `validation: reference-validated` in frontmatter and retain that scoping in any later citation.

If any validation reveals problems, they are either fixed in this session (return to Produce) or recorded as open issues for subsequent sessions.

#### 8. Record

Commit provenance to the workspace. Ensure all deliberations, decisions, and the reasoning behind them are captured in the session's provenance directory.

This activity is about completeness and permanence. Nothing decided or considered in this session should be lost.

#### 9. Close

Verify the workspace is in a coherent state:
- All new and modified files are committed to version control
- SESSION-LOG.md is updated with this session's entry
- open-issues.md reflects any new issues or resolved issues
- A statement of what the next session should address is included in the session log or provenance

### Continuity Rules

- **Read prior provenance before proposing.** If an idea was considered and rejected in a prior session, do not silently re-propose it. Cite the prior rejection and explain what has changed.
- **Do not overwrite silently.** When a specification is revised, preserve the prior version and make the succession traceable.
- **Preserve all provenance.** Do not delete historical records, even when they feel outdated.
- **Leave coherent state.** If work cannot complete, commit what was produced, document the blocker, and close cleanly.

### Self-Hosting

The methodology is self-hosting: it evolves by applying its own process to itself. This means:
- The methodology's specifications are subject to the same deliberation, decision, and versioning processes as any other artifact
- The methodology can revise its own kernel (this specification) through a regular session
- Changes to the kernel are recorded in provenance like any other decision
- The kernel should be revised when the process it describes no longer matches the process actually followed, or when a better process is discovered

## Validation

To validate this specification:

1. Review the most recent session's provenance and check that all nine activities were performed (or that their omission was explained — e.g., Convene is not needed for pure validation work)
2. Check that deliberative sessions included at least one adversarial perspective
3. Check that decisions record rejected alternatives, not just the chosen option
4. Check that SESSION-LOG.md is up to date
5. Check that no provenance from closed sessions has been modified
6. Ask: did the session's Read activity successfully use prior provenance to understand past decisions? If not, the provenance format or depth may need revision

codex
The live files match the brief’s core tension: `prompts/development.md` still says “read the workspace completely,” the kernel still says “every file,” `CLAUDE.md` still carries the mempalace paragraph, and the validator has no size-budget notion yet. I’m checking the deliberation/validation specs and a few concrete workspace facts next so the stance can make specific operational claims.
exec
/bin/zsh -lc "nl -ba prompts/development.md | sed -n '17,45p'" in /Users/ericmccowan/Development/complex-systems-engine
exec
/bin/zsh -lc "nl -ba specifications/methodology-kernel.md | sed -n '28,42p'" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
    28	
    29	Each session performs nine activities. These are a **vocabulary, not a strict sequence**. They have a general flow (you cannot decide before you deliberate) but permit recursion (deliberation may reveal the need for more reading).
    30	
    31	#### 1. Read
    32	
    33	Absorb what the session will reason from before changing anything. In every session this includes **workspace reading**: the full current state of the workspace — every file, every specification, every provenance record, and, where relevant, recent version-control history. Build a complete picture of the workspace's own state.
    34	
    35	When the session produces or revises an artefact intended for use outside the workspace, it also includes **domain reading**: the domain constraints the session operates under (stated by the user or operator in-session), cited external materials introduced into the session, and domain knowledge that the orchestrating agent surfaces explicitly as input to the work. Domain reading enlarges what must be understood; it does not permit silent import of outside ideas. Knowledge not already present in the workspace or in the session's explicit domain inputs must still be introduced through an explicit surveying or hypothesising step (per PROMPT.md). Perspective pretraining enters the session via stance briefs and perspective responses, not via §1 Read.
    36	
    37	This is a receptive activity. Its output is understanding, not artifacts.
    38	
    39	#### 2. Assess
    40	
    41	Determine what state the methodology is in and what this session should address. State the determination explicitly so future sessions have a record of what was inferred.
    42	

 succeeded in 0ms:
    17	## How to operate
    18	
    19	Begin by reading the workspace completely. Every file, every document, every historical record, every commit message if the workspace is under version control. Build a full picture of what exists before changing anything.
    20	
    21	From that reading, determine what state the methodology is in and what should happen next. If the workspace has not yet defined its own structure, the first work is to do so — by surveying prior approaches, reasoning about what this methodology needs, and committing a proposed shape along with the reasoning that led to it. If the workspace has defined a structure but not yet applied it, the next work is to begin applying it. If the structure has been applied but produces artefacts that have not been validated, the next work is validation. If everything has been exercised at least once, the methodology is in evolution mode — identify the weakest aspect of the current system and do whatever work addresses it.
    22	
    23	State your determination explicitly at the start of each session, so the next application of this prompt has a clear record of what you inferred and why.
    24	
    25	Before doing any substantive work, read everything the workspace has preserved about prior decisions. If an idea was considered and rejected earlier, do not silently re-propose it. If you believe a rejected idea deserves reconsideration, cite the prior rejection and explain what has changed. Continuity of reasoning is the whole point of preserving provenance.
    26	
    27	Substantive work in this methodology should not be done by a single perspective. Convene a group of AI agents with genuinely different viewpoints suited to the work at hand. Some perspectives generate options, some challenge them, some attend to what is unknown, some attend to what has been ignored, some reason about how the work will be received by those who must live with it. The specific perspectives, their number, and how they collaborate are for you to develop. Over repeated applications, patterns will emerge — document them when they do, so future applications can build on what worked.
    28	
    29	The work should produce a concrete output: a structured record of what was proposed, what was decided, what was rejected with reasoning, and what remains uncertain. This record is the provenance. Commit it to the workspace in a way that preserves it permanently and makes it findable by future applications. Alongside the provenance, update or create whichever artefacts the work warrants. If the work produced a new specification, write the specification. If it produced an implementation, build it. If it surfaced problems, record them where subsequent work will find them. The structure of the workspace should evolve to serve the methodology, not the other way around.
    30	
    31	Before ending the session, verify the workspace is in a coherent state. Specifications describe the engine as it currently is. Validations pass against those specifications, or their failures are documented as open issues for subsequent work to address. Any human-facing summary of the workspace accurately reflects its current state. Every piece of work done in this session has committed its provenance.
    32	
    33	## Rules that hold across applications
    34	
    35	These rules apply to both the self-development application and to external-problem applications of the engine.
    36	
    37	Do not import ideas from outside the process. If an insight arrived through reading something unrelated, a conversation with a human, or your own pretraining, introduce it as an input to an explicit surveying or hypothesising step rather than committing it directly. The value of this methodology is that its artefacts are traceable to the reasoning that produced them.
    38	
    39	Do not skip steps. Each piece of work's output is the next piece's input, and skipping breaks the chain of reasoning that makes the methodology evolveable.
    40	
    41	Do not overwrite prior specifications silently. When a specification is revised, preserve the prior version and make the succession traceable. The form of that preservation — filenames, directory structure, supersession markers, or something else — is for you to develop. Whatever you choose, be consistent so future readers can follow the thread.
    42	
    43	Preserve all provenance. Do not delete historical records, even when they feel embarrassing or outdated. A rejected idea from long ago may be the key to understanding a decision made today.
    44	
    45	Leave the workspace in a coherent state at the end of every application. If a piece of work cannot complete, commit what was produced, document the blocker, and end cleanly rather than leaving work in an indeterminate state.

exec
/bin/zsh -lc "sed -n '1,260p' specifications/validation-approach.md" in /Users/ericmccowan/Development/complex-systems-engine
exec
/bin/zsh -lc "sed -n '1,220p' prompts/application.md" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
You are operating on an **external-problem application** of the **Selvedge engine**. This application runs the engine against a specific problem that is not the engine's own development. You have loaded the engine definition (the files enumerated in `specifications/engine-manifest.md` §3) and are now executing the engine against this application's context.

Selvedge is the methodology (abstract approach). The Selvedge engine is its current loadable implementation. This application is one specific run of that engine; it has its own inputs, its own artefacts, its own validation pathway, and its own provenance. The engine's development-provenance (the `SESSION-LOG.md`, `open-issues.md`, and `provenance/` of the source workspace where the engine was developed) is NOT part of this application's context unless explicitly imported by a decision in this workspace.

## This application's context

The orchestrator filling this template should replace each `<<slot>>` with the application's concrete content before the first session runs. The slots are named; their content is the application's scope.

### Problem statement

<<Problem statement. What is being designed, for whom, under what constraints. One to three paragraphs. This is the primary input to every session's Read activity for this application.>>

### Constraints

<<Constraints on the design: domain constraints (what the physical, social, or procedural domain permits or forbids), time constraints (when the artefact must exist and in what progression), stakeholder constraints (who must find it usable, who must approve it, who must live with its consequences). Enumerate concretely.>>

### Stakeholders

<<Who holds the problem. Who will receive the artefact. Who will validate that the artefact worked (the domain-actor for Domain validation per `methodology-kernel.md` §7). If no domain-actor is available, Reference validation (per `specifications/reference-validation.md`) may substitute — the initialising session should determine.>>

### Success condition

<<What the artefact must do for this application to be considered successful. State as observable evidence, not as internal properties. Example: "a practitioner reads the artefact once and produces a usable attempt within five minutes" vs. "the artefact is clear" — the former is observable, the latter is not. Concrete success conditions make Validate possible.>>

### Initial state

<<Any materials, references, partial work, or prior context the application starts with. If starting from scratch, state "no prior materials; starting from the problem statement." If building on prior work, identify it explicitly and include references or copies in `applications/001-<slug>/` (or whichever numbered directory is first in this workspace).>>

### Engine version loaded

<<The engine version under which this application is running (e.g., `engine-v1`). Record this in every session's provenance so future readers know which engine behaviour applies. See `specifications/engine-manifest.md` §2 and §7.>>

---

## How to operate

All rules and activities from `prompts/development.md` §How to operate and §Rules that hold across applications apply to this application with the following application-specific adjustments.

### Read

The session's Read activity covers:

- **Workspace reading** — the full current state of this application's workspace (this workspace, not the engine's source workspace). Every file, every prior session's provenance, every prior artefact in `applications/`.
- **Domain reading** — this application's problem statement, constraints, stakeholders, success condition, initial state (the slots above), plus any domain materials introduced into the session.
- **Engine reading** — the loaded engine-definition files (`specifications/` + `tools/validate.sh` + `PROMPT.md` + this file). These are the normative rules the session executes under. They are not up for revision within this application's sessions unless a kernel-revision is explicitly authorised by the engine's source workspace.

### Convene and Deliberate

Per `specifications/methodology-kernel.md` §3 and `specifications/multi-agent-deliberation.md` v3, substantive work requires multi-perspective deliberation with adversarial coverage. For this application, perspectives are selected to surface the problem's specific contested dimensions. Domain perspectives (a perspective whose stance is grounded in domain knowledge — a practitioner, 