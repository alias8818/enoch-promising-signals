# Codebook INT3 + Sparse FP16 Residual on GPT-2-small CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `codebook-int3-sparse-fp16-residual-on-gpt-2-small-cpu-587832128c34`
Run ID: `codebook-int3-sparse-fp16-residual-on-gpt-2-small-cpu-587832128c34-20260614T034652737792+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/59cbdc3df83e

## What looked useful

Across 48 GPT-2-small projection tensors with 64 sampled rows each, INT3-only mean relative RMSE was 0.2409 at estimated 5.15x compression vs dense FP16. Adding 1%, 2%, 5%, and 10% sparse FP16 residuals reduced RMSE by 25.3%, 30.0%, 38.1%, and 47.0% respectively, with estimated compression ratios of 4.46x, 3.93x, 2.91x, and 2.02x. Naive CPU dequantize-plus-matmul averaged 10.75x slowdown vs dense matmul.

## Boundaries and scale limits

No full perplexity evaluation, no token-generation benchmark, no packed INT3 storage implementation, no fused sparse-residual matmul kernel, and sampled rows rather than every row in every tensor. CPU-only local runs were kept under the 15-minute budget.

## Claim scope

On sampled rows from all 48 GPT-2-small attention/MLP projection tensors, row-wise INT3 codebooks plus sparse FP16 top-error residuals improve weight reconstruction at useful byte ratios, but a naive CPU dequantize-plus-matmul implementation is much slower than dense NumPy matmul.

## Why it stopped

Early bounded CPU evidence supports the reconstruction mechanism but falsifies practical viability for a straightforward dequantize-before-matmul CPU implementation; this is not a full validation of optimized kernels or model quality.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up implementing a fused packed INT3 codebook plus sparse-residual CPU kernel and measure GPT-2-small perplexity and token latency against FP16/INT8 baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused CPU Kernel and Perplexity Test for INT3 Codebook Sparse Residual GPT-2-small
- Success threshold: At least 2x memory reduction vs dense FP16, less than 5% relative perplexity degradation on the validation subset, and no worse than 1.25x token-latency slowdown vs the strongest local INT8/dense baseline.
- Stop condition: Stop if the fused kernel remains more than 2x slower than dense/INT8 baseline at 2% or lower residual density, or if perplexity degradation exceeds 5% at the minimum density that meets the latency target.

## Evidence references

- Artifact root: `<local-path>/projects/codebook-int3-sparse-fp16-residual-on-gpt-2-small-cpu-587832128c34`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
