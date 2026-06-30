# Stacked Residual-Quantized Weights with Rate-Distortion Bound

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `stacked-residual-quantized-weights-with-rate-distortion-bound-52d6d8563f46`
Run ID: `stacked-residual-quantized-weights-with-rate-distortion-bound-52d6d8563f46-20260629T002720915147+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/640fda8882d3

## What looked useful

The tested scalar stacked residual formulation reduces error with more stages but remains far from the Gaussian rate-distortion bound and underperforms simpler same-rate quantizers. At 8 bits per scalar, trained MLP weights had NMSE 0.013953 for stacked residual 2x16 versus 0.002055 for single Lloyd and 0.000156 for uniform min/max; whole-model 8-bit stacked binary quantization lost 6.93 accuracy points while uniform lost 0.05 points.

## Boundaries and scale limits

No transformer-scale, vector/product quantization, entropy coding, quantization-aware training, GPT-2-small-class perplexity, or hardware decode throughput was tested.

## Claim scope

Greedy stacked residual scalar Lloyd quantization of weight values was tested on synthetic weight distributions and a small trained MLP, with fixed-rate comparisons to single Lloyd and uniform min/max quantization plus a Gaussian rate-distortion benchmark.

## Why it stopped

Proxy/local early falsification, not full-scale validation: the directly tested scalar formulation was far from the rate-distortion benchmark and worse than simpler same-rate baselines on distortion and small-model accuracy.

## Recommended next action

Stop this scalar greedy rate-distortion-bound claim; only revisit as a distinct vector/product residual quantization hypothesis with per-layer scaling, entropy-coded rates, and GPT-2-small-class perplexity baselines.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/stacked-residual-quantized-weights-with-rate-distortion-bound-52d6d8563f46`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
