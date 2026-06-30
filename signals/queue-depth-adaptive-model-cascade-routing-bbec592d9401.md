# Queue-Depth Adaptive Model Cascade Routing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `queue-depth-adaptive-model-cascade-routing-bbec592d9401`
Run ID: `queue-depth-adaptive-model-cascade-routing-bbec592d9401-20260531T195814908914+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8d9d476b9342

## What looked useful

Queue-depth-aware cascade thresholds are a plausible overload-control mechanism: they reduce downstream saturation and deadline misses in moderate overload, but become an explicit latency-quality tradeoff under severe overload.

## Boundaries and scale limits

No real LLM serving traces, logits, task labels, batching scheduler, cancellation behavior, concurrency pools, or measured model latencies were used. At 10-18 requests/s the latency gains came with quality losses from 0.0267 to 0.0853 for the mild policy, so the result does not support a broad quality-preserving overload claim.

## Claim scope

Synthetic single-server FCFS three-model cascade with generated confidence, quality, and service-time distributions. Mild queue-depth threshold adaptation improved p95 latency by 22.2% at 6 requests/s and 49.9% at 8 requests/s while keeping quality loss within 0.02 absolute versus static confidence-threshold cascade.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only and severe-overload results violate the quality-preservation threshold.

## Recommended next action

Run a medium trace-driven confirmation using real or production-like request difficulty, confidence, quality, and per-model latency measurements before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-driven queue-depth adaptive cascade validation
- Success threshold: Across at least three moderate-overload settings, queue-depth adaptive cascade reduces p95 latency by >=20% and deadline miss rate by >=25% with <=0.02 absolute quality loss versus static cascade; it must not rely on simply suppressing large-model usage below the quality-preserving threshold.
- Stop condition: Stop if trace-driven validation shows quality loss >0.02 at the loads where p95 latency improves >=20%, or if a simpler deadline/admission baseline dominates the queue-depth policy on both latency and quality.

## Evidence references

- Artifact root: `<local-path>/projects/queue-depth-adaptive-model-cascade-routing-bbec592d9401`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
