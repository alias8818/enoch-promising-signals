# KV cache INT2 with per-head FP8 residual

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `kv-cache-int2-with-per-head-fp8-residual-d3ad6ecf5586`
Run ID: `kv-cache-int2-with-per-head-fp8-residual-d3ad6ecf5586-20260628T202453191959+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ba6eef76f325

## What looked useful

Dense FP8 residuals repair most plain INT2 error but produce an unattractive point: 10.0036 bits/element and 0.095486 mean attention-output relative RMSE versus INT8 at 8.0018 bits/element and 0.038696 mean attention-output relative RMSE.

## Boundaries and scale limits

No CUDA kernel, paged-attention serving stack, real model KV traces, perplexity, or long-context generation quality was tested. Results falsify the dense residual storage point, not all possible sparse/adaptive residual variants.

## Claim scope

CPU-only synthetic KV-cache attention probe of per-head affine INT2 K/V plus dense per-element FP8 E4M3 residuals with per-head residual scales; sequence lengths 128, 512, and 1024; 8 heads; head dimension 64; gaussian, Student-t, and outlier-mixture distributions.

## Why it stopped

Early bounded falsification: the tested dense INT2+FP8 residual is larger and less accurate than INT8/FP8 on direct synthetic KV attention metrics, so it is not a practical compression mechanism in this form.

## Recommended next action

Stop this dense-residual formulation as no-paper; the only bounded next test worth running is a sparse/adaptive FP8 residual variant that must stay below the INT8 bit budget while matching INT8 attention-output error.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Sparse per-head FP8 residuals for INT2 KV cache
- Success threshold: Total storage below 8 bits/element and mean attention-output relative RMSE no more than 1.10x INT8 on the same synthetic matrix, with no p95 error blow-up above 1.25x INT8.
- Stop condition: Stop if mask/index overhead pushes storage to 8 bits/element or higher, or if sparse residual attention-output error remains above 1.10x INT8 after a bounded sweep.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-int2-with-per-head-fp8-residual-d3ad6ecf5586`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
