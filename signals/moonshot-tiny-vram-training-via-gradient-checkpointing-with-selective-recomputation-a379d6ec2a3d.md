# Moonshot: Tiny-VRAM Training via Gradient Checkpointing with Selective Recomputation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `moonshot-tiny-vram-training-via-gradient-checkpointing-with-selective-recomputation-a379d6ec2a3d`
Run ID: `moonshot-tiny-vram-training-via-gradient-checkpointing-with-selective-recomputation-a379d6ec2a3d-20260610T044750672739+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/6d2ab989b5e9

## What looked useful

Selective MLP recomputation was the strongest selective strategy in this probe: it saved most of full-block checkpointing's memory while preserving throughput better, and it converted an allocator-capped OOM into a completed training step.

## Boundaries and scale limits

Synthetic data only; short training-step benchmark only; no convergence or perplexity evidence; no real tiny discrete GPU; no GPT-2-small/full-corpus run; no comparison to offload, sharding, quantized finetuning, gradient accumulation, or production FlashAttention tuning.

## Claim scope

On a local GB10 using a synthetic 91.7M-parameter GPT-like BF16 training step, selective MLP recomputation reduced peak CUDA allocation by 24.9% versus no checkpointing with 0.8% step-time overhead, and completed under a roughly 1.03 GiB PyTorch allocator cap where the no-checkpoint baseline OOMed.

## Why it stopped

No-paper useful signal: this was a local synthetic/proxy validation of the mechanism, not a full validation of tiny-VRAM training.

## Recommended next action

Run a bounded deepen follow-up on real tokenized data with sequence-length and batch-size sweeps, reporting memory, throughput, and matched-loss/perplexity against full-block checkpointing and no checkpointing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data selective recomputation sweep for GPT-like tiny-VRAM training
- Success threshold: Selective MLP recomputation completes at least one allocator-budget setting where no-checkpoint OOMs, achieves at least 70% of full-block memory savings, has at least 25% lower overhead than full-block checkpointing, and shows no worse than 2% relative short-run loss degradation versus full-block checkpointing.
- Stop condition: Stop if selective MLP fails to fit any budget where no-checkpoint OOMs, or if its overhead is not meaningfully lower than full-block checkpointing on real data.

## Evidence references

- Artifact root: `<local-path>/projects/moonshot-tiny-vram-training-via-gradient-checkpointing-with-selective-recomputation-a379d6ec2a3d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
