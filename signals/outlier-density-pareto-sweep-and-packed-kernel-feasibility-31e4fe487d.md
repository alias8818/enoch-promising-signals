# Outlier-density Pareto sweep and packed-kernel feasibility for GPT-2-small W4 residual quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `outlier-density-pareto-sweep-and-packed-kernel-feasibility-31e4fe487d`
Run ID: `outlier-density-pareto-sweep-and-packed-kernel-feasibility-31e4fe487d-20260629T222332055696+0000`

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

- Parent run decision: Outlier-Aware 4-bit Weight-Only Quant on GPT-2-Small: enoch://control-plane/projects/outlier-aware-4-bit-weight-only-quant-on-gpt-2-small-240d984ab9d6/runs/outlier-aware-4-bit-weight-only-quant-on-gpt-2-small-240d984ab9d6-20260629T220208679674+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6c14b3140ece

## What looked useful

At 5% residual density, estimated storage was 2.738x smaller than fp16 for targeted weights and WikiText-2 probe PPL was 29.474 versus fp16 28.079. At 1-2% residual density, compression was 3.50x to 3.28x but PPL degradation remained +3.34 to +2.42. The dequantize-plus-matmul proxy was 11.13x to 13.55x slower than fp16 dense matmul on the four largest GPT-2 MLP matrices.

## Boundaries and scale limits

Perplexity probe used 32 contiguous 1024-token WikiText-2 validation chunks, not the full validation set. Packed-kernel evidence is a PyTorch proxy, not a fused int4 CUDA kernel. Embeddings, layer norms, and biases remained at model precision.

## Claim scope

On GPT-2-small 2D non-embedding weights, groupwise W4 with sparse per-row fp16 residual outliers gives a monotonic reconstruction and bounded WikiText-2 perplexity Pareto signal; naive PyTorch unpack/dequantize-plus-matmul is not a viable packed execution path on GB10.

## Why it stopped

Bounded direct evidence supports an outlier-density Pareto mechanism, but packed-kernel feasibility was only tested through a slow PyTorch proxy and is not validated.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is a single representative fused int4+scale+residual CUDA kernel for GPT-2 MLP c_fc/c_proj and a latency comparison against fp16.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused GB10 int4 plus sparse residual kernel for one GPT-2 MLP projection
- Success threshold: For at least one GPT-2-small MLP projection and token batch size, fused W4+residual matmul is at least 1.2x faster than fp16 torch matmul while keeping max output error consistent with the dequantized W4+residual reference.
- Stop condition: Stop if the fused kernel remains slower than fp16 by more than 20% after a minimal coalesced-load implementation, or if residual overlay cost dominates enough to erase the int4 bandwidth benefit.

## Evidence references

- Artifact root: `<local-path>/projects/outlier-density-pareto-sweep-and-packed-kernel-feasibility-31e4fe487d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
