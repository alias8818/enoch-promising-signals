# Tiny router cascade for CPU-bound local model serving

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-router-cascade-for-cpu-bound-local-model-serving-83692cf95b70`
Run ID: `tiny-router-cascade-for-cpu-bound-local-model-serving-83692cf95b70-20260604T205909105081+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/48518d91158f

## What looked useful

The mechanism is supported in a bounded proxy: confidence thresholds routed most easy examples to cheap tiers, sent about 2.9% of requests to the large tier on average, and achieved 5.49x mean direct latency speedup with -0.0046 mean absolute accuracy loss versus large-only.

## Boundaries and scale limits

Not tested on actual local LLMs, token generation, batching, streaming, KV cache behavior, realistic prompt mixes, memory pressure, or production queueing. Model-tier cost differences were synthetic dense NumPy CPU kernels rather than real model forward passes.

## Claim scope

On a CPU-only SMS text-classification proxy with real confidence-gated tiny/medium/large Naive Bayes classifiers and calibrated dense CPU work per tier, a cascade preserved large-only accuracy within 0.5 percentage points while reducing direct mean per-request latency by 3.89x to 6.86x across five deterministic splits.

## Why it stopped

Proxy evidence supports the cascade mechanism, but the result is not a full validation of local model serving because model costs were synthetic and the task was SMS classification rather than real LLM serving.

## Recommended next action

Stop this run as no-paper useful signal; next, run a bounded deepen test on actual CPU-served small language or encoder models with real inference latency and a fixed quality tolerance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU model cascade for local serving latency-quality tradeoff
- Success threshold: At least 2x mean latency speedup and improved p95 latency versus large-only while quality loss remains at or below 1 percentage point across two deterministic splits or task subsets.
- Stop condition: Stop if real model routing yields less than 1.5x speedup at the required quality tolerance or if confidence calibration cannot separate easy from hard requests better than a single small-model baseline.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-router-cascade-for-cpu-bound-local-model-serving-83692cf95b70`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
