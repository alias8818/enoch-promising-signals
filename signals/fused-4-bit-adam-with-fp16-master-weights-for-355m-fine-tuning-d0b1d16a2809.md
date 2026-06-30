# Fused 4-bit Adam with FP16 master weights for 355M fine-tuning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `fused-4-bit-adam-with-fp16-master-weights-for-355m-fine-tuning-d0b1d16a2809`
Run ID: `fused-4-bit-adam-with-fp16-master-weights-for-355m-fine-tuning-d0b1d16a2809-20260609T023514074555+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/846f49dced2e

## What looked useful

Packed 4-bit moments reduce persistent optimizer state at 355M scale from 4.26 GB for FP32 master/m/v to 1.087 GB when counting quantized moments plus FP16 master/parameter storage, but the naive second-moment quantization is unstable at eps 1e-8 and 1e-6, is 12.45x worse loss at eps 1e-4, and remains 1.74x worse loss at eps 1e-3 on the 1M convex proxy. The unfused prototype is also 2.46x slower than the FP32-state reference at 355M.

## Boundaries and scale limits

No fused CUDA kernel, no real 355M language-model fine-tuning, no validation-loss measurement, and only one synthetic 355M optimizer-step repeat. Timing reflects a PyTorch prototype with full dequantization temporaries.

## Claim scope

Local GB10 PyTorch prototype evidence for packed 4-bit Adam moments with FP16 parameter/master storage on synthetic optimizer-state benchmarks up to 355M parameters and a 1M-parameter convex convergence proxy.

## Why it stopped

Proxy and direct optimizer-state evidence show memory savings but early falsify the naive 4-bit moment design as a viable 355M fine-tuning optimizer without further second-moment stabilization and a fused kernel.

## Recommended next action

Stop this run as no-paper useful signal; next implement a bounded second-moment stabilization variant and rerun the same convergence proxy before any GPT-2-small fine-tuning.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilized 4-bit Adam second moments for FP16-master fine-tuning
- Success threshold: No NaNs for 60 proxy steps, final proxy loss within 10% of FP32-state Adam at eps <= 1e-4, and at least 3x persistent optimizer-state reduction at 355M scale.
- Stop condition: Stop if stabilized 4-bit moments still require eps > 1e-4, exceed 1.10x reference loss on the proxy, or lose the 3x persistent-state memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/fused-4-bit-adam-with-fp16-master-weights-for-355m-fine-tuning-d0b1d16a2809`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
