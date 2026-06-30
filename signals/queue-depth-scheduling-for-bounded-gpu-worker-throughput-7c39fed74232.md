# Queue Depth Scheduling for Bounded GPU Worker Throughput

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `queue-depth-scheduling-for-bounded-gpu-worker-throughput-7c39fed74232`
Run ID: `queue-depth-scheduling-for-bounded-gpu-worker-throughput-7c39fed74232-20260607T214611877457+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7a12bd32f122

## What looked useful

Across two heavier sweeps in forward and reversed depth order, depth 2 averaged 412.0 req/s, depth 4 averaged 412.0 req/s, and depths 8/16/32 did not improve throughput; mean p95 end-to-end latency rose from 6.43 ms at depth 2 to 10.44/20.12/39.81/79.32 ms at depths 4/8/16/32.

## Boundaries and scale limits

This does not validate production GPU worker throughput, real model serving, network/tokenization overhead, bursty arrival traces, multi-process contention, or long thermal/memory persistence. Evidence is direct for CUDA queue-depth microbenchmark behavior and proxy-only for a bounded serving scheduler.

## Claim scope

On a single GB10 GPU, for a PyTorch CUDA-stream GEMM-burst request microbenchmark with 384 requests per sweep and shapes 2048/3072 in float16, bounding in-flight queue depth at 2 reached peak mean throughput while deeper queues mainly increased p95/p99 latency.

## Why it stopped

The result is useful but microbenchmark-scoped; it supports the queue-depth knee mechanism but is not full validation of bounded GPU worker throughput.

## Recommended next action

Stop this run as no-paper useful signal; the next concrete step is a bounded model-serving follow-up that reuses the queue-depth sweep against a real inference workload and request trace.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Queue-depth knee validation on real single-GPU model serving traces
- Success threshold: Depth selected by the scheduler reaches at least 95% of peak measured throughput and reduces p95 latency by at least 30% versus the deepest queue tested across repeated runs.
- Stop condition: Stop if no bounded depth reaches 95% of peak throughput, or if latency improvement versus deep queue is under 15% in repeated runs.

## Evidence references

- Artifact root: `<local-path>/projects/queue-depth-scheduling-for-bounded-gpu-worker-throughput-7c39fed74232`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
