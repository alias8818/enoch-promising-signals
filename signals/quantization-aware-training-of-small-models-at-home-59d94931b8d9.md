# Quantization-Aware Training of Small Models at Home

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantization-aware-training-of-small-models-at-home-59d94931b8d9`
Run ID: `quantization-aware-training-of-small-models-at-home-59d94931b8d9-20260613T061128562010+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/62aab312ff43

## What looked useful

QAT was locally cheap and feasible. The useful signal is bit-width-specific: 8-bit QAT added no value over PTQ, but 4-bit QAT improved best-checkpoint validation accuracy by about 1.0 percentage point over 4-bit PTQ and reduced validation loss on the same seeds.

## Boundaries and scale limits

Synthetic data only; small MLP only; fake quantization only; no real dataset, no transformer, no exported integer kernels, no latency or energy measurement, and no publication-grade robustness ablations.

## Claim scope

On a 3-seed synthetic teacher-student MLP classification task run locally on GB10, 4-bit fake-quantization-aware training recovered a small amount of accuracy and loss versus 4-bit post-training fake quantization, while 8-bit PTQ was already effectively lossless.

## Why it stopped

Closed as a bounded synthetic useful signal, not full validation; the result supports local feasibility and a 4-bit mechanism hint but is not paper-ready.

## Recommended next action

Run the same matched FP32/PTQ/QAT protocol on a real small dataset with true exported quantized inference before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-dataset small-model QAT/PTQ comparison with exported quantized inference
- Success threshold: QAT-4 should recover at least half of the PTQ-4 accuracy drop relative to FP32 on a real dataset while preserving a concrete deployment advantage in size or latency.
- Stop condition: Stop if 8-bit and 4-bit PTQ match QAT within 0.5 percentage points on real-data accuracy or if exported quantized inference eliminates the apparent fake-quant benefit.

## Evidence references

- Artifact root: `<local-path>/projects/quantization-aware-training-of-small-models-at-home-59d94931b8d9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
