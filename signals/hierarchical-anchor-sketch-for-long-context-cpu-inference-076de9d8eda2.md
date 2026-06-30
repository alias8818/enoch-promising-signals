# Hierarchical Anchor Sketch for Long-Context CPU Inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `hierarchical-anchor-sketch-for-long-context-cpu-inference-076de9d8eda2`
Run ID: `hierarchical-anchor-sketch-for-long-context-cpu-inference-076de9d8eda2-20260605T024614224351+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ce76442746ef

## What looked useful

Simple two-level mean-anchor sketches reduced dot-product work only by losing target recall. No approximate method met the threshold of target_recall>=0.95, exact_match>=0.95, and dot_product_fraction<=0.35; flat leaf anchors usually beat the hierarchy at matched candidate budgets.

## Boundaries and scale limits

Does not test a real transformer decoder, natural language tasks, learned anchors, product quantization, native SIMD kernels, multi-batch serving, or 7B-plus model KV-cache behavior.

## Claim scope

Bounded CPU/NumPy synthetic retrieval benchmark for simple mean-anchor flat and two-level hierarchical candidate selection at 8192 to 65536 tokens, 64-dimensional keys, and 256 queries per main condition.

## Why it stopped

Proxy early falsification: the directly tested candidate selector failed the predeclared recall/work threshold on synthetic retrieval, and hierarchy usually underperformed flat anchors.

## Recommended next action

Stop this run as a proxy early falsification of simple hierarchical mean anchors; the next bounded test should replace mean anchors with richer multi-prototype or learned sketches before any model-integration work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-Prototype Leaf Sketches for CPU Long-Context Retrieval
- Success threshold: At N>=32768, achieve target_recall>=0.95, exact_match>=0.95, dot_product_fraction<=0.35, and wall-clock speedup>=1.2x in clustered and clustered_needle regimes without catastrophic random-regime degradation.
- Stop condition: Stop if multi-prototype anchors still require more than 35% of exact dot products for 0.95 exact_match, or if wall-clock speedup remains below 1.0x after vectorized batched scoring.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-anchor-sketch-for-long-context-cpu-inference-076de9d8eda2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
