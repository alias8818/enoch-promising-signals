# Queue-Pressure Adaptive Dynamic Batcher

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `queue-pressure-adaptive-dynamic-batcher-cefe431c63d5`
Run ID: `queue-pressure-adaptive-dynamic-batcher-cefe431c63d5-20260621T122812217339+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6677ab870bb4

## What looked useful

Adaptive pressure-based batch sizing is a plausible serving scheduler mechanism: low queue pressure preserves low wait, while high pressure increases effective batch size enough to drain bursts without the steady latency cost of always-large batches.

## Boundaries and scale limits

No real model, CUDA kernel, KV-cache, variable token length, production scheduler, admission control, multi-GPU, or real traffic trace was tested. The main run used 20 synthetic seeds and completed in 55.34 seconds on one CPU process.

## Claim scope

In a deterministic single-worker discrete-event proxy with bursty synthetic arrivals and accelerator-like sublinear batch service time, queue-pressure adaptive batching matched the throughput of a large fixed batcher while reducing p95 latency by 36-49% on bursty traces, and avoided the catastrophic backlog of a small fixed batcher under burst pressure.

## Why it stopped

Proxy simulation produced useful mechanism evidence but not direct serving-system evidence; this is not a full validation or paper-ready result.

## Recommended next action

Run a bounded deepen experiment in a real inference-serving harness with token-length-aware traces, comparing adaptive pressure batching against fixed small and fixed large batch controls on throughput, p95/p99 latency, GPU utilization, and timeout rate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-Length-Aware Real Serving Test for Queue-Pressure Adaptive Batching
- Success threshold: Adaptive policy matches fixed-large throughput within 3%, reduces p95 latency by at least 20% on bursty traces, and has timeout/error rate no higher than both fixed controls.
- Stop condition: Stop if adaptive throughput is more than 5% below fixed-large throughput or p95 latency is not at least 10% better than fixed-large on two of three bursty traces.

## Evidence references

- Artifact root: `<local-path>/projects/queue-pressure-adaptive-dynamic-batcher-cefe431c63d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
