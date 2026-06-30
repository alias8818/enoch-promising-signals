# CPU Residual Channel Matmul

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-residual-channel-matmul-59c83b2f5fc1`
Run ID: `cpu-residual-channel-matmul-59c83b2f5fc1-20260529T192341000750+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/03f6686f4884

## What looked useful

Residual-channel matmul is conditionally useful: full-grid results showed wins in 29/45 cases with all 12.5% and 25% active-fraction cases faster, while longer confirmation showed wins in 7/10 representative cases. High active fractions often lost, and an advanced-indexing smoke test showed hidden layout/copy overhead can erase the benefit.

## Boundaries and scale limits

Synthetic inference microbenchmarks only; no trained model, no real checkpoint, no production fused kernel, no quantization, no non-contiguous active-channel optimization, and no end-to-end accuracy or training evidence.

## Claim scope

On this CPU worker with NumPy/OpenBLAS float32 microbenchmarks, a residual-aware decomposition for Y = X @ (I + Delta_block) matched dense output and often improved wall-clock time when the active update block was contiguous and low-to-medium fraction of channels.

## Why it stopped

Evidence is a synthetic CPU microbenchmark that supports the mechanism only in a scoped regime, not a direct model or publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement a fused C or oneDNN-style residual-block kernel and compare it against dense GEMM on the same shape grid.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused CPU residual-block matmul versus dense GEMM
- Success threshold: At least 1.5x median speedup over dense GEMM for 25% active channels and at least 1.2x for 50% active channels on two or more channel sizes, with max relative error below 1e-5.
- Stop condition: Stop if the fused implementation fails to beat dense GEMM by 1.2x in 25% active-channel cases or if layout conversion overhead exceeds the saved matmul time.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-residual-channel-matmul-59c83b2f5fc1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
