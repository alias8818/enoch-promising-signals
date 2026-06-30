# INT8 Weight-Only Quantization With Per-Channel Calibration on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-weight-only-quantization-with-per-channel-calibration-on-cpu-43f92f6c2f7c`
Run ID: `int8-weight-only-quantization-with-per-channel-calibration-on-cpu-43f92f6c2f7c-20260629T202249182918+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/64cd9e1e824e

## What looked useful

Per-channel calibration improved output relative RMSE by a median 6.92x and at least 1.44x across six local cases, with 3.98x-3.99x weight storage compression. A naive NumPy weight-only proxy was 2.44x-13.72x slower than fp32, so the run supports calibration and memory benefit but not a CPU speedup claim.

## Boundaries and scale limits

Synthetic linear layers only; no real transformer checkpoint, perplexity/task metric, activation calibration, native fused INT8 GEMM kernel, production inference library, or long-run serving benchmark was tested.

## Claim scope

On deterministic synthetic CPU linear layers, symmetric INT8 weight-only quantization with per-output-channel calibration reduces output relative RMSE versus per-tensor calibration and gives approximately 4x weight storage compression after scale overhead.

## Why it stopped

Bounded proxy evidence supports per-channel calibration accuracy and storage benefit, but runtime evidence is an early falsification of naive NumPy CPU implementation viability rather than full validation of optimized INT8 kernels.

## Recommended next action

Stop this run as no-paper useful signal; the next concrete test is a native AVX2/AVX512 fused INT8 weight-only GEMM microkernel compared against fp32 BLAS on the same shapes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Native CPU fused INT8 weight-only GEMM for per-channel scales
- Success threshold: Per-channel relative output RMSE remains below 0.01 on outlier cases, weight storage compression remains at least 3.8x, and fused INT8 weight-only latency is no slower than 1.05x fp32 BLAS for at least four of six benchmark cases.
- Stop condition: Stop if the fused kernel remains more than 1.25x slower than fp32 BLAS on four or more cases, or if output relative RMSE exceeds 0.02 on outlier cases.

## Evidence references

- Artifact root: `<local-path>/projects/int8-weight-only-quantization-with-per-channel-calibration-on-cpu-43f92f6c2f7c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
