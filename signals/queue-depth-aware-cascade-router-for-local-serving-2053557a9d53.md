# Queue-depth-aware cascade router for local serving

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `queue-depth-aware-cascade-router-for-local-serving-2053557a9d53`
Run ID: `queue-depth-aware-cascade-router-for-local-serving-2053557a9d53-20260611T042928789806+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2cab43e8fd26

## What looked useful

Across 20 seeds and 8,000 requests per seed, queue-aware routing reduced p95 latency versus static threshold 0.46 by 18.0% under light load, 99.2% near capacity, and 99.3% under overload. It reduced SLO misses by 1.21, 30.52, and 24.32 percentage points respectively, while reducing simulated quality by 0.70, 3.48, and 5.51 percentage points.

## Boundaries and scale limits

No real LLMs, GPUs, batching scheduler, tokenizer, KV-cache pressure, prefill/decode split, or production request traces were tested. The evidence is mechanism-level simulator evidence only, not deployment or paper-grade validation.

## Claim scope

In a deterministic two-stage local-serving simulator with synthetic confidence, quality, and service-time distributions, lowering the escalation threshold as large-model queue depth grows prevents runaway large-stage queues and improves tail latency/SLO behavior versus a high-quality fixed threshold, at a measurable quality cost.

## Why it stopped

Closed as no-paper useful signal because the bounded simulator supports the queue-depth mechanism but lacks direct real-model serving evidence.

## Recommended next action

Run a bounded deepen follow-up in a real local serving stack with measured small/large model latencies, confidence signals, quality labels, and GPU utilization; do not write a paper from this simulator-only result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real local-serving trace test of queue-depth-aware cascade routing
- Success threshold: Queue-aware policy improves p95 latency by at least 25% or reduces SLO misses by at least 10 percentage points versus a quality-matched static threshold, with no more than 2 percentage points quality loss and no new stability regressions.
- Stop condition: Stop if real-serving confidence/quality signals are unavailable, if queue-depth policy cannot be integrated without changing the serving workload, or if two replicated workloads show less than 10% p95 improvement at matched quality.

## Evidence references

- Artifact root: `<local-path>/projects/queue-depth-aware-cascade-router-for-local-serving-2053557a9d53`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
