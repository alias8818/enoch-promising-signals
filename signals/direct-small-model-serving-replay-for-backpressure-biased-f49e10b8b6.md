# Direct Small-Model Serving Replay for Backpressure-Biased Cascade Routing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-small-model-serving-replay-for-backpressure-biased-f49e10b8b6`
Run ID: `direct-small-model-serving-replay-for-backpressure-biased-f49e10b8b6-20260611T130700502770+0000`

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

- Parent run decision: Queue-Aware Adaptive Cascade: Using Backpressure to Bias Local Cascade Routing: enoch://control-plane/projects/queue-aware-adaptive-cascade-using-backpressure-to-bias-local-cascade-routing-316e3478426d/runs/queue-aware-adaptive-cascade-using-backpressure-to-bias-local-cascade-routing-316e3478426d-20260611T120045972849+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c2e658f144b9

## What looked useful

Backpressure bias has a measurable latency-protection mechanism, but quality-preserving benefit is narrow. Aggressive settings cut deadline misses by up to nearly 100% but exceeded the quality budget; the narrow setting achieved a 47.16% deadline-miss reduction with -0.019 expected-quality delta at 8 qps only.

## Boundaries and scale limits

The larger model service times were proxied by a multiplier, quality was score-modeled rather than label-measured, arrivals were synthetic Poisson streams, and the threshold was met only at 8 qps onset overload, not across heavier overload levels.

## Claim scope

In a Tier-1 local replay using direct CUDA distilgpt2 small-model serving latencies and a controlled large-model service multiplier, a narrow backpressure-biased cascade policy reduced deadline misses at onset overload while staying within a 0.02 expected-quality loss budget.

## Why it stopped

Tier-1 direct small-model replay produced a useful but mixed mechanism signal; it is not paper-positive because the quality-preserving effect appeared only at onset overload and key large-model and quality measurements were proxied.

## Recommended next action

Run a bounded paired-model replay with direct service measurements for both small and larger local models plus labeled task accuracy before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Paired Small/Large Direct Cascade Replay With Labeled Quality
- Success threshold: At least 25% relative deadline-miss reduction at two or more controlled overload levels with actual labeled quality no worse than 2 percentage points below confidence-only routing.
- Stop condition: Stop if no policy setting meets both the deadline-miss and actual-quality thresholds, or if the effect appears only under proxied quality or proxied large-model service.

## Evidence references

- Artifact root: `<local-path>/projects/direct-small-model-serving-replay-for-backpressure-biased-f49e10b8b6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
