# Queue-depth adaptive batching for gpu_worker

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `queue-depth-adaptive-batching-for-gpu-worker-5858c26ea014`
Run ID: `queue-depth-adaptive-batching-for-gpu-worker-5858c26ea014-20260607T053339411880+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2b828dab0d6c

## What looked useful

Adaptive batching avoided fixed-batch wait overhead at shallow queue depth while still using larger batches during bursts; the p95/best-fixed ratio ranged from 0.611 to 0.628 across five seeds with throughput ratio 1.0.

## Boundaries and scale limits

Synthetic arrivals, synthetic matmul service curve with scaling, no production gpu_worker integration, no real inference trace, no multi-worker or multi-GPU validation.

## Claim scope

On a GB10-calibrated synthetic single-worker queue model, queue-depth adaptive batching reduced p95 latency by about 37-39% versus the best fixed batch-size control across five bursty arrival seeds while preserving completed-request throughput.

## Why it stopped

Closed as no-paper useful signal because evidence is a GPU-calibrated synthetic queue proxy, not direct production-worker validation.

## Recommended next action

Implement the adaptive policy in a real gpu_worker loop and replay representative request traces against fixed batch-size controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace replay validation of queue-depth adaptive batching in a real gpu_worker
- Success threshold: Adaptive p95 latency at least 20% lower than the best fixed batch-size control with throughput at least 98% of the best fixed policy across at least three traces.
- Stop condition: Stop if adaptive batching fails to beat the best fixed p95 by 10% on two representative traces or reduces throughput below 95%.

## Evidence references

- Artifact root: `<local-path>/projects/queue-depth-adaptive-batching-for-gpu-worker-5858c26ea014`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
