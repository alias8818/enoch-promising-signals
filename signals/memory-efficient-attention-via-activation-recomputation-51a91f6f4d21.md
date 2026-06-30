# Memory-Efficient Attention via Activation Recomputation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `memory-efficient-attention-via-activation-recomputation-51a91f6f4d21`
Run ID: `memory-efficient-attention-via-activation-recomputation-51a91f6f4d21-20260609T104013274202+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/befa06f93b7e

## What looked useful

Activation recomputation reduced logical saved attention-forward tensors from 134 MiB to 6 MiB at sequence 2048 for B1 H4 D64 with float32-correct gradients, but the naive recompute backward still materialized full O(N^2) temporaries and raised sampled CPU peak RSS by about 129 MiB while slowing the case by about 1.74x.

## Boundaries and scale limits

No GPU, fused kernel, bf16/fp16, full transformer block, optimizer step, language-model training, long-context serving, or distributed validation was run. CPU RSS measurements are allocator- and temporary-tensor-sensitive and did not show an end-to-end peak memory reduction for the naive recompute implementation.

## Claim scope

CPU PyTorch proxy for dense scaled dot-product attention forward/backward at batch 1, 2-4 heads, head dimension 32-64, sequence lengths 128-2048: custom autograd activation recomputation saves only Q/K/V and substantially reduces retained attention-forward saved tensor bytes versus standard dense autograd.

## Why it stopped

Bounded CPU proxy supports the activation-saving mechanism but falsifies the stronger practical claim for a naive implementation: lower retained autograd state did not translate to lower sampled process peak memory because backward temporaries dominated.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement blockwise recompute backward that avoids full O(N^2) temporaries and compare peak memory/runtime against dense autograd on CPU and, if available, GPU SDPA baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blockwise Attention Recomputation Without Full Backward Temporaries
- Success threshold: At sequence 2048 B1 H4 D64 float32, blockwise recompute peak RSS is at least 20 percent below dense autograd while gradients remain within 1e-5 max absolute error and wall-time overhead is at most 2.5x.
- Stop condition: Stop if blockwise recompute still has peak RSS equal to or above dense autograd at sequence 2048, or if gradient error exceeds 1e-5 after debugging obvious implementation mistakes.

## Evidence references

- Artifact root: `<local-path>/projects/memory-efficient-attention-via-activation-recomputation-51a91f6f4d21`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
