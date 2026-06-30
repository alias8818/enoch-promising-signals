# Hadamard-rotated 2-bit weights with FP16 outlier buffer for GB10 memory-bound inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hadamard-rotated-2-bit-weights-with-fp16-outlier-buffer-for-gb10-memory-bound-inference-36de97684010`
Run ID: `hadamard-rotated-2-bit-weights-with-fp16-outlier-buffer-for-gb10-memory-bound-inference-36de97684010-20260629T034001887868+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b3da86e28ed9

## What looked useful

Packed Q2 GEMV was 2.5-2.9x faster than a simple FP16 GEMV when activations were already rotated, and Hadamard rotation greatly reduced error versus the unrotated control. However, measured activation Hadamard cost erased the gain at 4096x4096 and left only 1-3% end-to-end speedup at M=16384,K=4096, while relative RMSE remained high at 0.61-0.65 even with 64-256 FP16 residual outliers per row.

## Boundaries and scale limits

No trained LLM weights, no perplexity/task metrics, no fused production Hadamard kernel, no multi-layer serving stack, no long-context/KV-cache interaction. Results are bounded to synthetic heavy-column-outlier matrices and a simple custom CUDA GEMV.

## Claim scope

Synthetic batch-1 GB10 GEMV proxy for Hadamard-rotated packed 2-bit weights with per-row scale and sparse FP16 residual outlier buffer; tested M=4096,K=4096 and M=16384,K=4096.

## Why it stopped

Early GB10 proxy falsification for the practical recipe: kernel-only bandwidth benefit exists, but end-to-end speed/fidelity is not compelling once activation rotation and FP16 residual buffer cost are included.

## Recommended next action

Stop this run as a no-paper useful signal; only reopen with a bounded follow-up that fuses or amortizes the Hadamard transform and demonstrates relative RMSE below 0.10 on real model linear weights.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused or persistent-rotation Q2 Hadamard GEMV on real model linear weights
- Success threshold: At least 1.25x end-to-end latency speedup versus optimized FP16 GEMV at batch-1 with output relative RMSE below 0.10 or no worse than 1% relative degradation on the selected model-level metric.
- Stop condition: Stop if fused/persistent rotation cannot exceed 1.10x end-to-end speedup or if error remains above 0.20 relative RMSE at compression ratio above 3x.

## Evidence references

- Artifact root: `<local-path>/projects/hadamard-rotated-2-bit-weights-with-fp16-outlier-buffer-for-gb10-memory-bound-inference-36de9768`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
