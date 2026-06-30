# Dynamic Batch Sizing Based on Queue Depth for Bounded CPU Work

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `dynamic-batch-sizing-based-on-queue-depth-for-bounded-cpu-work-49f7d80eda4d`
Run ID: `dynamic-batch-sizing-based-on-queue-depth-for-bounded-cpu-work-49f7d80eda4d-20260610T133100306065+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7ed7bd294395

## What looked useful

Adaptive batching is worth implementation-level testing when per-batch overhead is material and queue depth varies; it is not useful when batch overhead is zero, and fixed larger batches can still win near saturation under high overhead.

## Boundaries and scale limits

Synthetic/proxy evidence only: no real CPU worker implementation, OS scheduler effects, cache behavior, allocator pressure, heterogeneous service times, multi-worker contention, or production traces were tested. Full-scale service validation remains untested.

## Claim scope

In a deterministic single-worker FIFO queueing model for bounded CPU work, queue-depth adaptive batch sizing preserved throughput within 2% of the best fixed policy while keeping p95 latency within 25% of best in 4 of 4 default-overhead scenarios; the effect depends on nonzero per-batch overhead and policy thresholds.

## Why it stopped

Closed as no-paper useful signal because evidence is bounded synthetic/proxy evidence, not direct deployment-grade validation.

## Recommended next action

Implement a real CPU worker microbenchmark with controlled arrivals and measured bounded CPU tasks to validate whether the simulated latency/throughput tradeoff persists outside the queueing model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU Worker Benchmark for Queue-Depth Adaptive Batching
- Success threshold: Adaptive policy is within 2% of best fixed-policy throughput and improves p95 latency by at least 10% versus the best high-throughput fixed policy in at least 3 of 4 real-worker scenarios.
- Stop condition: Stop if adaptive misses the throughput threshold or fails to improve p95 latency in 2 or more scenarios, or if measured overhead is too small for batching to matter.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-batch-sizing-based-on-queue-depth-for-bounded-cpu-work-49f7d80eda4d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
