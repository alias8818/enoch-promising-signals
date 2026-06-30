# Ring Attention Blocks for 4K Context on 6GB VRAM

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `ring-attention-blocks-for-4k-context-on-6gb-vram-82572d0b9b21`
Run ID: `ring-attention-blocks-for-4k-context-on-6gb-vram-82572d0b9b21-20260526T025941462450+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/acd2798a41c2

## What looked useful

At 4K context with batch 3, heads 32, head_dim 128, dense attention failed under the 6 GiB cap while block-online attention completed with 0.565 GiB peak allocated. At batch 2, block-online used 0.387 GiB peak versus dense at 4.301 GiB, with fp16 correctness probes passing at max absolute error 0.001953125.

## Boundaries and scale limits

Forward attention only; synthetic random QKV tensors; single GB10 GPU; no backward pass, optimizer state, full transformer stack, KV cache, model-quality evaluation, optimized custom kernel, or multi-GPU ring communication.

## Claim scope

Exact block-online causal attention, implemented in plain PyTorch, can run 4K sequence attention under a 6 GiB CUDA process allocation cap for fp16 tensors at batch 3, 32 heads, and head dimension 128, while dense materialized attention OOMs under the same cap.

## Why it stopped

Useful local mechanism signal only; not paper-ready because evidence is synthetic, forward-only, and does not validate end-to-end model behavior or distributed ring attention.

## Recommended next action

Run a bounded deepen test by integrating block-online attention into a small GPT-style inference/eval stack and comparing end-to-end memory and tokens/sec against PyTorch SDPA or FlashAttention under the same 6 GiB cap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end 4K GPT-style inference with block-online attention under 6 GiB
- Success threshold: Complete 4K end-to-end forward inference under 6 GiB with peak allocated memory at least 2x below the strongest baseline that fits, or complete when the baseline OOMs; small-sequence logits must match dense within max absolute error below 1e-2.
- Stop condition: Stop if block-online end-to-end inference exceeds 6 GiB, fails correctness tolerance, or is more than 3x slower than the strongest memory-feasible baseline at 4K.

## Evidence references

- Artifact root: `<local-path>/projects/ring-attention-blocks-for-4k-context-on-6gb-vram-82572d0b9b21`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
