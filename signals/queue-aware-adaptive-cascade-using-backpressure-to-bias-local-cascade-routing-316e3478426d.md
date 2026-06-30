# Queue-Aware Adaptive Cascade: Using Backpressure to Bias Local Cascade Routing

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `queue-aware-adaptive-cascade-using-backpressure-to-bias-local-cascade-routing-316e3478426d`
Run ID: `queue-aware-adaptive-cascade-using-backpressure-to-bias-local-cascade-routing-316e3478426d-20260611T120045972849+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c2e658f144b9

## What looked useful

Backpressure was a useful bias term in the local cascade router: it avoided overload of the slow high-skill branch and cut timeout rate by about 0.58 absolute in overload scenarios, with about 0.028-0.030 absolute expected-quality loss versus quality-only. The latency-only control was faster but lost about 0.055-0.061 expected quality.

## Boundaries and scale limits

No real model inference, no calibrated confidence estimator, no production traces, synthetic expected-quality model, exponential service times, single-process CPU simulation, and 60 paired seeds for the main run.

## Claim scope

In a bounded synthetic discrete-event simulation of a two-stage local cascade with heterogeneous branch speed/quality, queue-backpressure-biased routing reduced queue collapse, p95 latency, and timeout rate versus quality-only routing while preserving more expected quality than shortest-work routing.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but is not direct/full validation of queue-aware cascade routing in an actual model-serving system.

## Recommended next action

Stop this run as no-paper useful signal; next run should replay a small real cascaded model stack with calibrated confidence and measured task accuracy under controlled bursty load.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Small-Model Serving Replay for Backpressure-Biased Cascade Routing
- Success threshold: Backpressure reduces p95 latency by at least 30% and timeout rate by at least 50% versus quality-only under bursty overload, while retaining at least 98% of quality-only measured accuracy and outperforming shortest-work on accuracy.
- Stop condition: Stop if measured accuracy loss exceeds 2% absolute at the backpressure setting needed for a material latency/timeout improvement, or if quality-only does not create measurable queue pressure in the direct stack.

## Evidence references

- Artifact root: `<local-path>/projects/queue-aware-adaptive-cascade-using-backpressure-to-bias-local-cascade-routing-316e3478426d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
