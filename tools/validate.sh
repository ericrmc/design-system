#!/usr/bin/env bash
# Methodology workspace validation tool
# Two-tier validation: automated structural checks + guided semantic questions
# Read-only: this script never modifies any files

set -euo pipefail

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
  fi
  shopt -s nullglob
  manifest_files=("$manifests_dir"/*.manifest.yaml "$manifests_dir"/*.manifest.yml)
  shopt -u nullglob
  if [[ ${#manifest_files[@]} -eq 0 ]]; then
    fail "$dirname — manifests/ directory present but no *.manifest.yaml files found"
    BLOCK_CHECK_13[$dirname]=1
    continue
  fi
  session_ok=true
  for mf in "${manifest_files[@]}"; do
    mname=$(basename "$mf")
    missing=""
    for field in "${D024_REQUIRED_FIELDS[@]}"; do
      if ! grep -qE "^${field}:" "$mf"; then
        missing="${missing} ${field}"
      fi
    done
    for sub in "${D024_SAMPLING_SUBFIELDS[@]}"; do
      if ! grep -qE "^[[:space:]]+${sub}:" "$mf"; then
        missing="${missing} sampling.${sub}"
      fi
    done
    if [[ -z "$missing" ]]; then
      pass "$dirname/manifests/$mname — all D-024 required fields present"
    else
      fail "$dirname/manifests/$mname — missing D-024 fields:${missing}"
      session_ok=false
    fi
  done
  if ! $session_ok; then
    BLOCKED_SESSIONS="${BLOCKED_SESSIONS} ${dirname}"
  fi
done
echo ""

# [13] Cross-model-claim honesty (D-028, D-029, D-030)
#
# HONEST LIMIT (document read before touching this check):
# This check verifies the session's claim is internally consistent with its
# manifests. It does not and cannot verify that the manifests' lineage claims
# are themselves true. Manifest truth relies on operator integrity and the
# `participant_selected_by` field's accountability. Known gaming modes recorded
# in D-029: value-flipping (editing training_lineage_overlap_with_claude),
# `unknown` laundering, paper-human classification, wrapper impersonation. A
# failure here is a consistency failure; a pass is not a truth certificate.
#
# Gate: session declares cross_model: true in either participants.yaml or any
# file matching *-deliberation*.md (synthesis) frontmatter. Runs after check 12
# per the sequencing rule; sessions where check 12 failed are reported BLOCKED.
echo "[13] Cross-model-claim honesty"
for dir in "${provdirs[@]}"; do
  dirname=$(basename "$dir")
  # Discover cross_model declaration
  declared_cross_model=false
  shopt -s nullglob
  candidate_declarations=("${dir}participants.yaml" "${dir}participants.yml" "${dir}"*-deliberation*.md "${dir}"*deliberation.md)
  shopt -u nullglob
  for cf in "${candidate_declarations[@]}"; do
    [[ -f "$cf" ]] || continue
    if grep -qE "^cross_model:[[:space:]]*true" "$cf" 2>/dev/null; then
      declared_cross_model=true
      break
    fi
  done
  if ! $declared_cross_model; then
    continue  # no cross-model claim; out-of-scope
  fi
  # Sequencing: if check 12 failed for this session, block check 13
  if [[ " ${BLOCKED_SESSIONS} " == *" ${dirname} "* ]]; then
    echo "  ⊘ $dirname — BLOCKED: check 12 failed for this session; cannot evaluate check 13"
    continue
  fi
  # Consistency check: at least one manifest must have training_lineage_overlap_with_claude
  # other than known-overlap, or participant_kind: human
  manifests_dir="${dir}manifests"
  honest=false
  if [[ -d "$manifests_dir" ]]; then
    if grep -qE "^training_lineage_overlap_with_claude:[[:space:]]*(independent-claim|unknown)" "$manifests_dir"/*.manifest.yaml 2>/dev/null; then
      honest=true
    fi
    if grep -qE "^participant_kind:[[:space:]]*human" "$manifests_dir"/*.manifest.yaml 2>/dev/null; then
      honest=true
    fi
  fi
  if $honest; then
    pass "$dirname — cross_model: true is consistent with participant manifests"
  else
    fail "$dirname — cross_model: true declared but no participant manifest records training_lineage_overlap_with_claude other than known-overlap, and no participant_kind: human. Fix one of: (a) correct cross_model to false; (b) correct a manifest's training_lineage_overlap_with_claude to unknown or independent-claim (if truthful); (c) add a human participant manifest (if one participated). NOTE: this check verifies consistency of self-report, not truthfulness; see honest-limit comment in validate.sh."
  fi
done
echo ""

# --- Summary ---
echo "--- Tier 1 Summary ---"
echo "Passed: $PASS  |  Failed: $FAIL  |  Warnings: $WARN"
if [[ $FAIL -gt 0 ]]; then
  echo "Result: FAIL"
else
  echo "Result: PASS"
fi
echo ""

# --- Tier 2: Guided Assessment ---
echo "--- Tier 2: Guided Assessment ---"
echo ""
echo "The following questions require judgment. Consider each during the session."
echo ""
echo "  Q1. Did this session's Read activity use prior provenance to understand"
echo "      past decisions? Were any past decisions re-proposed without"
echo "      acknowledgment?"
echo ""
echo "  Q2. Are the current specifications semantically consistent with each"
echo "      other? Do any contradict or make assumptions that conflict?"
echo ""
echo "  Q3. In deliberative work, did the adversarial perspective provide genuine"
echo "      challenge, or did it concede too easily?"
echo ""
echo "  Q4. Is the methodology producing meaningful progress, or is it"
echo "      accumulating ceremony without advancing?"
echo ""
echo "  Q5. Are there specifications that describe things that no longer exist,"
echo "      or things that exist without being specified?"
echo ""
echo "  Q6. This session records cross_model: true. Name the concrete evidence —"
echo "      invocation transcript, CLI command, wall-clock gap, human presence —"
echo "      that distinguishes a genuine non-Claude participant from a Claude"
echo "      subagent with an edited manifest. If you cannot, flip cross_model to"
echo "      false. (Skip if this session does not claim cross-model participation.)"
echo ""

if [[ $FAIL -gt 0 ]]; then
  exit 1
else
  exit 0
fi
