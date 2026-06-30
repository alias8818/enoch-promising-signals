# Real CPU model cascade for local serving latency-quality tradeoff

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-cpu-model-cascade-for-local-serving-latency-quality-t-a08fe1e783`
Run ID: `real-cpu-model-cascade-for-local-serving-latency-quality-t-a08fe1e783-20260605T072944187952+0000`

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

- Parent run decision: Tiny router cascade for CPU-bound local model serving: enoch://control-plane/projects/tiny-router-cascade-for-cpu-bound-local-model-serving-83692cf95b70/runs/tiny-router-cascade-for-cpu-bound-local-model-serving-83692cf95b70-20260604T205909105081+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/48518d91158f

## What looked useful

The 200-example run found a feasible cascade at threshold 0.95 with 7.0% fallback, 92.5% accuracy, 69.90 ms mean latency, and 38.52% lower mean latency than the 113.69 ms large-model baseline. The 500-example confirmation found a feasible cascade at threshold 0.98 with 10.6% fallback, 93.2% accuracy, 74.11 ms mean latency, and 35.80% lower mean latency than the 115.44 ms large-model baseline.

## Boundaries and scale limits

One binary classification task, one model pair, one CPU host, fixed 4-thread local serving, no concurrency, no quantization baseline, no repeated confidence intervals, and offline threshold sweep reconstructed from per-example measured timings rather than a deployed router benchmark.

## Claim scope

On one CPU worker using batch-size-one PyTorch inference for SST-2 validation examples, a confidence-gated cascade from distilbert-base-uncased-finetuned-sst-2-english to textattack/bert-base-uncased-SST-2 reduced mean latency versus always using the larger model while staying within 1 accuracy point on 200-example and 500-example direct tests.

## Why it stopped

Closed as no-paper useful signal: the direct CPU tests support the mechanism, but the evidence is too narrow for publication readiness.

## Recommended next action

Run a bounded deepen follow-up with held-out threshold selection on the full SST-2 validation set, repeated latency trials, and baselines against cheap-only, large-only, and an available quantized/distilled single-model alternative.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out calibrated CPU cascade validation against quantized single-model baselines
- Success threshold: Held-out cascade achieves at least 25% mean-latency reduction versus large-only with no more than 1.0 accuracy point loss, and is not dominated by the quantized/distilled single-model baseline on both accuracy and p95 latency.
- Stop condition: Stop if held-out accuracy loss exceeds 1.0 point at every threshold that provides at least 25% mean-latency reduction, or if a quantized/distilled single-model baseline strictly dominates the cascade on accuracy, mean latency, and p95 latency.

## Evidence references

- Artifact root: `<local-path>/projects/real-cpu-model-cascade-for-local-serving-latency-quality-t-a08fe1e783`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
