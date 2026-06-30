# Home-Hardware Quantization: INT2 on CPU with Vector-Quantized Residual Dictionaries

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `home-hardware-quantization-int2-on-cpu-with-vector-quantized-residual-dictionaries-e592ccd2046e`
Run ID: `home-hardware-quantization-int2-on-cpu-with-vector-quantized-residual-dictionaries-e592ccd2046e-20260613T142832715641+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e939cac20e2f

## What looked useful

VQ residuals cut output RMSE by 82.28% on a VQ-friendly positive control and 16.74% weighted on a tiny real checkpoint, but only 2.50-2.73% on iid/mildly structured synthetic weights. VQ decode-each-batch was 1.15x-1.22x slower than plain INT2 decode and 2.17x-3.25x slower than cached dense FP32 matmul in the reference CPU implementation.

## Boundaries and scale limits

Synthetic 2048 x 2048 linear layers, batch 32, single-process NumPy CPU timings, 7 repeats; tiny random GPT-2 safetensors checkpoint with 109824 evaluated 2D weights. No trained GPT-2-small or larger perplexity, no real token generation, no packed INT2 AVX2/AVX-512 kernel, and no end-to-end home-hardware serving test.

## Claim scope

Bounded CPU reference evidence for INT2 block quantization plus vector-quantized residual dictionaries on synthetic linear layers and a tiny public GPT-2 checkpoint. The mechanism can reduce quantization/output error when residuals are reusable, but the tested naive CPU decode path is slower than plain INT2 decode and no full-model quality or fused-kernel result was produced.

## Why it stopped

Bounded proxy and tiny-checkpoint evidence is mixed and insufficient for a paper or deployment claim; it shows a mechanism but not end-to-end INT2 home-hardware viability.

## Recommended next action

Stop this run as no-paper useful signal; next, implement a packed/fused CPU kernel and evaluate trained GPT-2-small-class weights with perplexity and matched-storage INT2/INT4 baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused CPU INT2 plus residual-dictionary kernel on trained GPT-2-small weights
- Success threshold: At matched storage, INT2 plus VQ residuals improves perplexity or output error by at least 10% versus plain INT2 while retaining at least 90% of the throughput of the packed plain-INT2 CPU baseline.
- Stop condition: Stop if the fused VQ path is more than 15% slower than packed plain INT2 without at least 10% matched-storage quality improvement, or if trained-model quality remains worse than a standard INT4 baseline.

## Evidence references

- Artifact root: `<local-path>/projects/home-hardware-quantization-int2-on-cpu-with-vector-quantized-residual-dictionaries-e592ccd2046e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
