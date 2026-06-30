# Trace replay validation of queue-depth adaptive batching in a real gpu_worker

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-replay-validation-of-queue-depth-adaptive-batching-i-cc30b2a4d4`
Run ID: `trace-replay-validation-of-queue-depth-adaptive-batching-i-cc30b2a4d4-20260607T072258585829+0000`

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

- Parent run decision: Queue-depth adaptive batching for gpu_worker: enoch://control-plane/projects/queue-depth-adaptive-batching-for-gpu-worker-5858c26ea014/runs/queue-depth-adaptive-batching-for-gpu-worker-5858c26ea014-20260607T053339411880+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2b828dab0d6c

## What looked useful

The tuned adaptive policy reached 7616.5 rps on the heavier-kernel replay versus 7618.9 rps fixed64 and 7628.1 rps fixed16, while reducing p95 latency to 1.651 ms versus 2.663 ms fixed64 and 2.579 ms fixed16. Single-request dispatch backlogged badly at 2408.9 rps and 483.676 ms p95.

## Boundaries and scale limits

Single worker, one deterministic trace family, synthetic FP16 matrix workload, no production model, no real payload transfer path, no multi-seed or long-duration robustness, and no multi-worker scheduling.

## Claim scope

On one GB10 gpu_worker replaying a deterministic 3000-request burst trace into a real CUDA FP16 matrix workload, queue-depth adaptive batching with a 0.5 ms wait window preserved fixed-batch offered-load throughput and reduced p95 latency versus fixed64 and fixed16 controls.

## Why it stopped

Tier 1 direct validation produced a useful mechanism signal, but evidence is not paper-ready because it is one local worker, one deterministic trace family, and a synthetic CUDA workload.

## Recommended next action

Run a bounded deepen follow-up with multi-seed burst traces and a production-like inference kernel, requiring adaptive05 to keep p95 at least 20% below fixed64 at matched throughput across most seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-seed production-kernel validation of queue-depth adaptive batching
- Success threshold: Adaptive 0.5 ms or a predeclared adaptive wait policy must match fixed64 throughput within 5% and reduce p95 latency by at least 20% in at least 8 of 10 seeds without exceeding fixed16 p95 by more than 10%.
- Stop condition: Stop if adaptive fails the p95 threshold in 3 or more seeds, if throughput falls more than 5% below fixed64 in 3 or more seeds, or if production-kernel integration cannot run on the local gpu_worker.

## Evidence references

- Artifact root: `<local-path>/projects/trace-replay-validation-of-queue-depth-adaptive-batching-i-cc30b2a4d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
