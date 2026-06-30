# VRAM-Aware Cascade Router with Predictive Model Swapping

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `vram-aware-cascade-router-with-predictive-model-swapping-9026f0ebe315`
Run ID: `vram-aware-cascade-router-with-predictive-model-swapping-9026f0ebe315-20260525T054001817682+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/db3d7bb517ac

## What looked useful

Prediction alone did not make model swapping useful. History and oracle prefetch were effectively flat or worse versus reactive LRU, while a causal Markov predictor substantially increased latency and swap churn by evicting useful tiers and adding blocking prefetch work.

## Boundaries and scale limits

No real LLM weights, CUDA/UMA allocations, production request traces, batching, or framework model-load behavior were tested. Results should be treated as an early mechanism/failure-mode signal, not production-serving validation.

## Claim scope

Bounded synthetic discrete-event serving tests of naive predictive model swapping for a four-tier cascade router under explicit model footprints, load latencies, capacity limits, and queue-aware response latency.

## Why it stopped

Early synthetic falsification of naive predictive model swapping; not a full production validation.

## Recommended next action

Stop this run as a no-paper useful signal; next, test a cost-gated predictive controller that prefetches only when expected saved demand-load time exceeds idle-time and eviction-risk cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cost-Gated Predictive Swapping for Cascade Routers
- Success threshold: At least 10% p95 latency reduction or 25% relative deadline-miss reduction versus reactive LRU in predictable/slack traces, with no more than 5% swap-in increase and no statistically meaningful regression on random or adversarial traces.
- Stop condition: Stop if cost-gated prefetch fails to improve predictable/slack p95 latency by 10%, increases swap-ins by more than 5%, or regresses random/adversarial p95 latency by more than 5%.

## Evidence references

- Artifact root: `<local-path>/projects/vram-aware-cascade-router-with-predictive-model-swapping-9026f0ebe315`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
