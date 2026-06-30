# Confidence-gated dual-model cascade for CPU local serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-gated-dual-model-cascade-for-cpu-local-serving-27bd30802cbe`
Run ID: `confidence-gated-dual-model-cascade-for-cpu-local-serving-27bd30802cbe-20260610T165928064279+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7b7f6e596e3d

## What looked useful

Accuracy-biased gating reached 0.630 held-out accuracy versus 0.633 for always-expensive and 0.609 for cheap-only, with 17.8% fallback, 3.00x mean latency speedup, and 1.51x p95 latency speedup versus always-expensive. A latency-biased threshold collapsed to cheap-only behavior and missed the expensive model's gains.

## Boundaries and scale limits

Synthetic data only; no LLM/token generation, real prompt distribution, batching, quantization, concurrent serving, or production CPU runtime was tested.

## Claim scope

On a synthetic CPU-local classification serving benchmark with a cheap linear softmax model and an expensive exact kNN fallback, an accuracy-selected confidence threshold recovered most expensive-model accuracy while reducing mean per-query latency.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only, despite showing a concrete speed-quality tradeoff and an important threshold-selection failure mode.

## Recommended next action

Do not write a paper from this synthetic proxy; run a bounded real CPU-local text classification, reranking, or small/large LLM serving benchmark with the same min-fallback and max-accuracy threshold policies.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU-local confidence cascade on text serving workload
- Success threshold: Cascade quality within 1 percentage point of expensive-only, at least 2x mean latency speedup, p95 latency speedup above 1.2x, and no calibration-to-test collapse.
- Stop condition: Stop if the confidence gate either improves quality by less than 0.5 percentage points over cheap-only or needs more than 50% fallback to stay within 1 percentage point of expensive-only.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-dual-model-cascade-for-cpu-local-serving-27bd30802cbe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
