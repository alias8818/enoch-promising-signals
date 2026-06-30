# Tiny Router for CPU Model Cascade Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-router-for-cpu-model-cascade-serving-c707f3986dfb`
Run ID: `tiny-router-for-cpu-model-cascade-serving-c707f3986dfb-20260602T154645261244+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6d97d8ae3df8

## What looked useful

Tiny confidence-feature routers can preserve large-model accuracy and cut mean CPU serving latency in a sequential cascade, but the same design may hurt p95 tail latency when more than a small fraction of requests route to the large model.

## Boundaries and scale limits

Toy dataset and classical sklearn models only; no transformer/LLM inference, no production traces, no concurrency, no batching, no queueing, and no workload drift. Calibrated p95 latency was slightly worse than always-large because routed requests pay small-plus-large sequential cost.

## Claim scope

On a local sklearn digits single-request CPU cascade, a logistic-regression router over small-model confidence features matched the calibrated large-model test accuracy while improving mean latency by 4.57x and routing 15.28 percent of requests to the large model.

## Why it stopped

Bounded local evidence supports the mean-latency mechanism but is toy-scale and mixed on tail latency, so it is not publication-grade direct evidence.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up on real CPU text classifiers or small transformer inference with concurrency and p95 SLO measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny router cascade on real CPU text inference with tail-latency SLOs
- Success threshold: At matched large-model accuracy within 0.5 percentage points, show at least 2x mean latency or CPU-cost improvement on both tasks; for p95 claims, show p95 improvement on both tasks under the stated serving policy.
- Stop condition: Stop if matched-accuracy mean latency speedup is below 1.5x on either task, or if p95 is worse and the claim requires tail-latency improvement.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-router-for-cpu-model-cascade-serving-c707f3986dfb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
