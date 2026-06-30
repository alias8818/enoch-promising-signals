# Queue-Pressure-Adaptive Model Cascade Router

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `queue-pressure-adaptive-model-cascade-router-0fc986e112dd`
Run ID: `queue-pressure-adaptive-model-cascade-router-0fc986e112dd-20260530T064411139937+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d04a9c2427be

## What looked useful

Queue pressure is a strong control signal for cascaded model routing: lowering the escalation threshold under large-model backlog avoided queue collapse. In near-capacity bursty traffic, pressure-adaptive routing reduced p99 latency from 160.725s to 2.875s and SLA miss rate from 0.6044 to 0.0640 with 1.36 percentage points of accuracy loss.

## Boundaries and scale limits

Synthetic-only evidence over 3 traffic regimes, 10 seeds, 18,000 requests per seed, assumed service-time and quality distributions, no real model inference, no batching, no trace replay, no production traffic, and no deployment-scale validation.

## Claim scope

In a deterministic synthetic discrete-event simulator with small-to-large cascade routing, bursty arrivals, calibrated confidence proxies, and explicit large-model queue workload, pressure-adaptive thresholding reduced p99 latency and SLA misses versus a static confidence cascade while preserving most quality in near-capacity traffic.

## Why it stopped

No-paper closure: the mechanism is supported only by synthetic/proxy evidence, not direct production or real-model serving evidence.

## Recommended next action

Run a bounded trace-replay or local serving microbenchmark with real small and large model calls, measured confidence/utility scores, batching behavior, and matched static-cascade quality thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Replay Validation of Queue-Pressure Adaptive Cascade Routing
- Success threshold: At least 25% reduction in p99 latency or SLA miss rate relative to static cascade with no more than 3 percentage points quality/utility loss across at least two seeds or replay slices.
- Stop condition: Stop if real-model trace replay shows less than 10% p99/SLA improvement at matched quality, or if adaptive routing needs more than 3 percentage points quality loss to stabilize the queue.

## Evidence references

- Artifact root: `<local-path>/projects/queue-pressure-adaptive-model-cascade-router-0fc986e112dd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
