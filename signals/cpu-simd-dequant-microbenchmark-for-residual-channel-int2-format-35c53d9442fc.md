# CPU SIMD dequant microbenchmark for residual-channel int2 format

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-simd-dequant-microbenchmark-for-residual-channel-int2-format-35c53d9442fc`
Run ID: `cpu-simd-dequant-microbenchmark-for-residual-channel-int2-format-35c53d9442fc-20260621T171937072825+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/408262a02f5a

## What looked useful

SIMD dequantization is worthwhile for the tested int2 format, but residual channel tails reduced throughput by about 27.6% for AVX2 and 17.0% for AVX-512 on average versus the preceding vector-friendly channel count.

## Boundaries and scale limits

Single CPU host, one compiler, one synthetic layout, single-thread execution, random data, no production kernel baseline, no end-to-end inference, and no cross-architecture validation.

## Claim scope

On this Xeon Silver 4114 CPU, for a synthetic row-major residual-channel int2 dequant layout with per-channel scale and bias, single-thread AVX2 and AVX-512 kernels were about 3.23x faster than scalar on average, but residual channel counts introduced material tail penalties.

## Why it stopped

Bounded local microbenchmark produced useful residual-tail evidence, but the result is synthetic and lacks production baselines or multi-host validation.

## Recommended next action

Stop this run as no-paper useful signal; next concrete step would be a bounded production-kernel comparison against FBGEMM/oneDNN/XNNPACK-style tail handling on two CPU generations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production-kernel residual-channel int2 dequant comparison
- Success threshold: Residual-specialized path reduces average residual-tail throughput loss by at least 50% versus the baseline SIMD tail path with max_abs_error equal to 0.
- Stop condition: Stop if the specialized path fails to reduce average residual-tail loss by at least 20% on either CPU generation or introduces any correctness mismatch.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-simd-dequant-microbenchmark-for-residual-channel-int2-format-35c53d9442fc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
