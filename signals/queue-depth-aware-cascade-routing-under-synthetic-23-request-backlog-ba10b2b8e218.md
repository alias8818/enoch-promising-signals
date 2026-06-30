# Queue-Depth-Aware Cascade Routing Under Synthetic 23-Request Backlog

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `queue-depth-aware-cascade-routing-under-synthetic-23-request-backlog-ba10b2b8e218`
Run ID: `queue-depth-aware-cascade-routing-under-synthetic-23-request-backlog-ba10b2b8e218-20260610T205403955958+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3d1a388f08f9

## What looked useful

Queue-depth-aware routing produced a reproducible synthetic signal on 11,500 requests: 2050.36 ms mean latency and 14.49% SLO violations versus 2316.54 ms and 19.05% for shortest_queue, 2647.78 ms and 25.83% for static_small_first, and 4539.22 ms and 43.68% for confidence_only. It also showed the expected quality-latency tradeoff against confidence_only.

## Boundaries and scale limits

Synthetic-only evidence: no live LLM serving, real correctness labels, batching, KV-cache effects, GPU utilization, tokenizer overhead, production traffic traces, or datacenter-scale concurrency were measured.

## Claim scope

In a deterministic synthetic discrete-event benchmark with 500 seeds, 23 simultaneous queued requests per seed, and three modeled cascade tiers, queue-depth-aware routing reduced mean latency and SLO violations relative to static small-first and shortest-queue baselines while improving modeled quality relative to those baselines; compared with confidence-only routing it reduced latency, cost, and SLO violations but sacrificed modeled quality.

## Why it stopped

Bounded synthetic simulation supports a mechanism but is proxy-only and not direct validation of real cascade routing.

## Recommended next action

Stop this worker run as no-paper useful signal; next direct test should replay queue-depth-aware, confidence-only, and queue-only policies against measured model-serving traces with real answer correctness labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Replayed Queue-Depth-Aware Cascade Routing With Real Model Latencies
- Success threshold: Queue-depth-aware routing reduces p95 latency by at least 15% and SLO violations by at least 20% versus confidence-only while losing no more than 2 percentage points of real correctness, and beats shortest_queue on correctness at comparable latency.
- Stop condition: Stop if queue-depth-aware routing fails to improve p95 latency or SLO violations versus confidence-only under the quality-loss budget, or if it cannot beat shortest_queue on correctness at comparable latency.

## Evidence references

- Artifact root: `<local-path>/projects/queue-depth-aware-cascade-routing-under-synthetic-23-request-backlog-ba10b2b8e218`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
