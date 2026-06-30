# Compute-Aware Selective Gradient Checkpointing via Pareto Optimization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compute-aware-selective-gradient-checkpointing-via-pareto-optimization-c0c9fc52f789`
Run ID: `compute-aware-selective-gradient-checkpointing-via-pareto-optimization-c0c9fc52f789-20260525T013621576066+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/54be85ff558a

## What looked useful

Compute cost is useful in checkpoint selection, but optimizing total estimated activation bytes is an insufficient proxy for actual CUDA peak memory. Peak placement/liveness matters: uniform checkpointing saved 22.60% memory at 10.74% overhead and dominated pareto_dp at target 0.35, while pareto_dp saved 27.99% at 18.20% overhead at target 0.65 and beat largest_activation but was not clearly best versus ratio/uniform policies.

## Boundaries and scale limits

Single GB10, one synthetic 12-block MLP stack, batch 4, 512 tokens, width 512, bfloat16, five measured repeats per policy. No GPT-2-small-class transformer validation, no real training corpus, no allocator/liveness-aware optimizer, and no multi-seed robustness sweep.

## Claim scope

On a bounded GB10/CUDA synthetic heterogeneous MLP stack, a total-activation-byte Pareto/knapsack checkpoint selector reduced peak memory versus no checkpointing and beat the largest-activation heuristic, but it did not reliably define the measured memory/time frontier against simple uniform or bytes-per-ms heuristics.

## Why it stopped

Early bounded falsification of the stronger proxy claim: the simple total-byte Pareto selector was often matched or dominated by simpler heuristics on measured peak memory and step time, so evidence is insufficient for a paper-positive result.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should replace total-byte savings with a liveness-aware peak-memory objective and evaluate it on GPT-2-small-class transformer blocks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Liveness-Aware Pareto Checkpoint Selection on GPT-2-Small-Class Blocks
- Success threshold: At two or more memory-pressure targets, liveness-aware Pareto must be non-dominated and save at least 10% more peak memory than the best simple heuristic at equal or lower step-time overhead, or reduce step overhead by at least 10% at equal or better peak memory.
- Stop condition: Stop if liveness-aware selection is dominated by a simple heuristic in two consecutive transformer configurations or if measured peak memory does not correlate with the liveness objective.

## Evidence references

- Artifact root: `<local-path>/projects/compute-aware-selective-gradient-checkpointing-via-pareto-optimization-c0c9fc52f789`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
