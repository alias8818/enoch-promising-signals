# Asymmetric Residual Quantization: 4-bit Residuals with 2-bit Weights for CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `asymmetric-residual-quantization-4-bit-residuals-with-2-bit-weights-for-cpu-e4c07a973056`
Run ID: `asymmetric-residual-quantization-4-bit-residuals-with-2-bit-weights-for-cpu-e4c07a973056-20260529T151313570543+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/730f4b282d3d

## What looked useful

The residual mechanism is useful for error reduction, but the proposed 2+4 design behaves like an inefficient 6-bit scheme for CPU: it uses two metadata streams, is less accurate than direct q6, and was 4% to 8% slower than q4 in scalar dequant-on-the-fly matvec.

## Boundaries and scale limits

No real transformer weights, calibration sets, perplexity, packed bit kernels, SIMD intrinsics, multithreaded serving, or end-to-end LLM generation were tested. CPU benchmark uses scalar unpacked uint8 codes and is directional for decode overhead only.

## Claim scope

On synthetic row-wise asymmetric quantized CPU matvec probes, 2-bit base plus 4-bit residual quantization reduces matvec relative L2 error by about 2.9x to 3.3x versus direct 4-bit quantization, but direct 6-bit quantization is consistently more accurate with slightly lower estimated row-wise payload.

## Why it stopped

Bounded proxy/direct CPU evidence found no paper-ready advantage: ARQ 2+4 improves q4 error but is inferior to direct q6 on accuracy/storage and adds decode overhead versus q4.

## Recommended next action

Stop this run as no-paper evidence; the only concrete next test worth doing is a packed AVX2/AVX-512 real-layer benchmark against mature int4/int8 and direct q6 baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed AVX-512 ARQ 2+4 on real transformer layers
- Success threshold: ARQ 2+4 must be at least 10% faster than direct q6 at matched or lower layer-output error, or at least 20% lower error than q4 with no more than 5% throughput loss on real packed CPU kernels.
- Stop condition: Stop if packed ARQ remains slower than q6 or fails to beat q6 accuracy/storage on two representative transformer layers.

## Evidence references

- Artifact root: `<local-path>/projects/asymmetric-residual-quantization-4-bit-residuals-with-2-bit-weights-for-cpu-e4c07a973056`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
