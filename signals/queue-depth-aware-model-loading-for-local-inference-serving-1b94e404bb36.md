# Queue-Depth-Aware Model Loading for Local Inference Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `queue-depth-aware-model-loading-for-local-inference-serving-1b94e404bb36`
Run ID: `queue-depth-aware-model-loading-for-local-inference-serving-1b94e404bb36-20260524T034543059661+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d46c994fc477

## What looked useful

Queue depth is useful as an eviction/loading signal for high-mix workloads where LRU thrashes, but queue-depth delay is not universally beneficial and can worsen phase-shift bursts. This is a no-paper synthetic result that motivates a bounded real-serving harness rather than a broad claim.

## Boundaries and scale limits

No real model loading, GPU/UMA allocation, tokenizer/runtime overhead, batching, production traces, or multi-process serving was measured. Thresholds 4 and 5 were stopped as inefficient in this simulator, so the sensitivity study is incomplete above q=3.

## Claim scope

Synthetic discrete-event simulation of six local-inference model classes under a 10 GB simulated model-memory budget. The tested queue-depth-aware policy with q_threshold=1 reduced flat-mix p95 latency and cold-load churn versus on-demand LRU, was nearly neutral for rare bursts, and regressed bursty phase-shift tail latency.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic and mixed: the mechanism helped flat-mix tail latency but hurt bursty phase-shift p95/p99.

## Recommended next action

Build a real local-serving replay harness with three actual models and measured cold-load/GPU-memory telemetry, then compare q=1 queue-depth eviction/loading against on-demand LRU on the same bursty and flat-mix traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real local-serving replay for queue-depth-aware model loading
- Success threshold: At least 10% lower p95 latency than LRU on flat_mix, no more than 3% p95 regression on bursty_shift, and no increase in incomplete/error rate.
- Stop condition: Stop if real measured load/memory behavior removes the flat_mix tail-latency gain or if bursty_shift p95 regression exceeds 3% in two independent seeds.

## Evidence references

- Artifact root: `<local-path>/projects/queue-depth-aware-model-loading-for-local-inference-serving-1b94e404bb36`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
