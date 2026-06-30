# Adaptive Queue-Aware Model Cascade Routing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-queue-aware-model-cascade-routing-5e99b3263a8b`
Run ID: `adaptive-queue-aware-model-cascade-routing-5e99b3263a8b-20260613T171132342000+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/a566b6ed4483

## What looked useful

Queue delay and remaining SLO budget are useful routing signals under bursty overload: queue-aware routing cut p95 latency by 54.3% to 93.4%, SLO misses by 21.18 to 32.12 percentage points, and cost by 12.6% to 21.5% versus static cascade, while losing 1.45 to 3.25 accuracy percentage points.

## Boundaries and scale limits

Synthetic proxy only: no real LLM serving traces, token distributions, GPU batching, live queue telemetry, or production model quality measurements. Runs used 8 seeds, 3 load levels, 2500 requests per seed/load/policy, and a simplified one-server large tier.

## Claim scope

In a deterministic synthetic bursty-serving simulator with small/medium/large model tiers, queue-aware cascade routing reduced p95 latency, SLO misses, cost, and large-model calls versus a static confidence cascade, but with a measurable accuracy tradeoff.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic/proxy-only and the adaptive policy improves latency/cost by trading away some accuracy rather than preserving the static baseline exactly.

## Recommended next action

Run a bounded trace-replay follow-up with calibrated model latency/quality profiles and an explicit maximum 1 percentage point accuracy-loss constraint.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Trace Replay for Queue-Aware Cascade Routing Under an Accuracy Floor
- Success threshold: At least 20% p95 latency reduction and 10 percentage point SLO-miss reduction versus tuned static cascade at <=1 percentage point accuracy loss across at least two load regimes.
- Stop condition: Stop if the accuracy-constrained queue-aware policy cannot beat static cascade p95 latency by 10% in two calibrated load regimes, or if calibrated traces show the large-tier queue is not a bottleneck.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-queue-aware-model-cascade-routing-5e99b3263a8b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
