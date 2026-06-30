# Real-agent validation of validation-before-use operational memory

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-agent-validation-of-validation-before-use-operational-2328ad8238`
Run ID: `real-agent-validation-of-validation-before-use-operational-2328ad8238-20260630T055521427616+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: OpMemory: Doctrine Update for Repeating Local Agents: enoch://control-plane/projects/opmemory-doctrine-update-for-repeating-local-agents-475c4350655f/runs/opmemory-doctrine-update-for-repeating-local-agents-475c4350655f-20260630T052839001761+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/dc6ddb85ba8b

## What looked useful

The trust-memory Codex agents still inspected tests and source files, detected stale memory conflicts, edited the evidence-supported files, and passed all evaluator tests. This suggests prompt-level trust-memory controls can be too weak for modern coding agents because default verification behavior may swamp the intended contrast.

## Boundaries and scale limits

Only three generated tasks, one Codex version, local MEMORY.md files, short single-step Python fixes, and no true persistent memory store or production repository workload.

## Claim scope

In a six-trial local benchmark using nested noninteractive Codex agents on tiny Python workspaces, explicit validation-before-use instructions did not improve stale operational-memory task success over a trust-memory prompt.

## Why it stopped

Bounded real-agent evidence did not support a measurable benefit from explicit validation-before-use; the result is an early scoped falsification of the prompt-level effect, not a full validation or refutation of persistent operational memory systems.

## Recommended next action

Stop this run as a bounded no-paper negative; if continuing, run a stronger 20+ task follow-up with a control agent/model that demonstrably follows stale memory without implicit local validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stronger stale-memory control for validation-before-use agents
- Success threshold: Validation-before-use pass rate is at least 30 percentage points higher than trust-memory on stale-memory tasks, with clean-memory pass rate no more than 5 percentage points lower.
- Stop condition: Stop if the control agent continues to validate local evidence despite trust-memory instructions, because the benchmark cannot isolate the mechanism.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-validation-of-validation-before-use-operational-2328ad8238`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
