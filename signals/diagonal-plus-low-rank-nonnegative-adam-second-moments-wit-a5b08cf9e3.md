# Diagonal-plus-low-rank nonnegative Adam second moments with rank-floor selection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `diagonal-plus-low-rank-nonnegative-adam-second-moments-wit-a5b08cf9e3`
Run ID: `diagonal-plus-low-rank-nonnegative-adam-second-moments-wit-a5b08cf9e3-20260516T070152902556+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6eeb1383b126

## What looked useful

Rank 2-4 projected DPLR/floor Adam matched Adam on classification and regression within the predeclared 5% validation-loss threshold; rank 4 classification had loss ratio 0.9998 and accuracy delta 0.0000, while rank 2 regression had loss ratio 0.9702. Moment relative L2 dropped from about 0.84-0.87 for rank 0 to about 0.07-0.10 for rank 2-4.

## Boundaries and scale limits

The optimizer kept full second moments and used per-step SVD projection, so this does not validate memory savings, streaming low-rank state updates, large language-model training, long-horizon stability, or production throughput.

## Claim scope

Tier 1 small direct neural-network training test: projected nonnegative low-rank plus scalar-floor Adam second-moment denominators at ranks 2-4 matched Adam validation behavior on two synthetic tasks over 3 seeds, with moment approximation error decreasing strongly with rank.

## Why it stopped

No-paper closure: the Tier 1 direct test supports the preconditioner mechanism but is not publication-grade because it relies on an oracle/projected full-moment implementation and small synthetic tasks.

## Recommended next action

Run a bounded deepen follow-up implementing a true storage-saving DPLR/floor optimizer without full exp_avg_sq, then compare against Adam and Adafactor on a medium direct training task with memory and wall-clock metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Streaming storage-saving DPLR/floor Adam versus Adam and Adafactor
- Success threshold: Storage-saving DPLR/floor optimizer achieves validation loss within 5% of Adam, is not worse than Adafactor on the target metric, and reduces 2D second-moment state memory by at least 2x without instability.
- Stop condition: Stop if the storage-saving variant diverges or is more than 5% worse than both Adam and Adafactor on validation loss in two independent seeds, or if memory savings disappear after accounting for required optimizer state.

## Evidence references

- Artifact root: `<local-path>/projects/diagonal-plus-low-rank-nonnegative-adam-second-moments-wit-a5b08cf9e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
