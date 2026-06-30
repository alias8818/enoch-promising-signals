# End-to-end 4K GPT-style inference with block-online attention under 6 GiB

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `end-to-end-4k-gpt-style-inference-with-block-online-attent-ce2e86cd29`
Run ID: `end-to-end-4k-gpt-style-inference-with-block-online-attent-ce2e86cd29-20260526T125851266730+0000`

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

- Parent run decision: Ring Attention Blocks for 4K Context on 6GB VRAM: enoch://control-plane/projects/ring-attention-blocks-for-4k-context-on-6gb-vram-82572d0b9b21/runs/ring-attention-blocks-for-4k-context-on-6gb-vram-82572d0b9b21-20260526T025941462450+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/acd2798a41c2

## What looked useful

Block-online attention completed the direct 4K GPT-style workload at 0.734 GiB peak allocated and 0.752 GiB peak reserved under both 6 GiB and 1 GiB caps. Dense eager attention also passed under 6 GiB but used 1.146 GiB allocated and 1.877 GiB reserved, and failed under a 1 GiB cap on a 384 MiB score allocation.

## Boundaries and scale limits

Synthetic random weights and inputs only; no trained checkpoint, no quality metric, no KV-cache decode loop, no batching, no FlashAttention/SDPA baseline, no production serving fragmentation, and no larger model scale.

## Claim scope

Single-batch 4096-token bf16 inference for a random-weight GPT-2-small-class decoder-only model on GB10 CUDA: block-online causal attention completed under a 6 GiB allocator cap and used less peak memory than dense eager attention.

## Why it stopped

Tier-1 direct validation produced a useful mechanism signal but not publication-grade evidence; dense eager attention also satisfied the original 6 GiB threshold at GPT-2-small scale.

## Recommended next action

Run a bounded deepen follow-up that sweeps context/model size and includes SDPA or FlashAttention-style baselines to find the actual under-cap pass/fail boundary.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Memory-threshold sweep for 4K block-online attention versus optimized baselines
- Success threshold: Identify a reproducible condition where block-online completes under a fixed memory cap while dense eager and at least one optimized baseline fail or use at least 25% more peak reserved memory, without more than 2x throughput loss versus the best passing baseline.
- Stop condition: Stop if optimized baselines match block-online memory within 10% at all tested feasible settings or if no setting can be tested within local runtime and memory budgets.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-4k-gpt-style-inference-with-block-online-attent-ce2e86cd29`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
