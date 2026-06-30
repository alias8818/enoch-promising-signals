# Ring Attention Blockwise Scan for 8K Context on 10GB VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ring-attention-blockwise-scan-for-8k-context-on-10gb-vram-f3b6f57ec49e`
Run ID: `ring-attention-blockwise-scan-for-8k-context-on-10gb-vram-f3b6f57ec49e-20260522T114559842052+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/60fbf69a39be

## What looked useful

Blockwise online attention matched dense attention within fp16 tolerance and completed an 8K high-pressure case whose dense score tensor alone would be 8 GiB fp16 or 16 GiB fp32. However, dense attention was faster and fit for the smaller B=1 8K case, so the result supports only a bounded memory mechanism, not a broad performance or paper-ready claim.

## Boundaries and scale limits

Not a strict 10 GiB discrete VRAM proof; not a fused kernel; no multi-GPU ring communication, backward pass, training integration, model-quality measurement, or production SDPA/FlashAttention comparison. PyTorch cached allocator reserved large UMA pools, so reserved memory is not used as the claim metric.

## Claim scope

Single-GPU GB10 PyTorch evidence shows exact blockwise/ring-order online softmax can compute 8K attention with fp16 dense-equivalent outputs and under 5 GiB peak live CUDA allocation for B=4,H=16,D=64,block=512.

## Why it stopped

Bounded local evidence supports the memory mechanism but is proxy-limited for the 10 GiB claim and mixed on performance, so it is not publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should implement a fused Triton/CUDA blockwise kernel and test forward/backward on a strict 10 GiB device against SDPA or FlashAttention-style baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused 8K Blockwise Attention on Strict 10 GiB VRAM
- Success threshold: For an 8K transformer-layer-equivalent case under a hard 10 GiB limit, blockwise forward/backward completes with peak allocated memory below 9.5 GiB, dense baseline OOMs or exceeds the cap, correctness error remains within fp16 tolerance on comparable smaller shapes, and throughput is at least 25% of the optimized SDPA baseline.
- Stop condition: Stop if the fused implementation cannot keep peak allocation below 9.5 GiB, fails correctness beyond fp16 tolerance, or remains below 25% of optimized SDPA throughput after one focused kernel optimization pass.

## Evidence references

- Artifact root: `<local-path>/projects/ring-attention-blockwise-scan-for-8k-context-on-10gb-vram-f3b6f57ec49e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
