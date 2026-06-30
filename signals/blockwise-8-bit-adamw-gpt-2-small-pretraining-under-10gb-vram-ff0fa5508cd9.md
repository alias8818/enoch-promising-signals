# Blockwise 8-bit AdamW GPT-2-small pretraining under 10GB VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `blockwise-8-bit-adamw-gpt-2-small-pretraining-under-10gb-vram-ff0fa5508cd9`
Run ID: `blockwise-8-bit-adamw-gpt-2-small-pretraining-under-10gb-vram-ff0fa5508cd9-20260604T213313437566+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/33ebd991a77f

## What looked useful

Blockwise 8-bit moment storage works mechanically and halves persistent optimizer state for GPT-2-small, but activation/backward memory dominates the tested under-10GB boundary. PyTorch bf16 AdamW was already memory-lean because its moment tensors were bf16 in this environment. Batch 8 seq 1024 without checkpointing peaked at 10.778 GB allocated for both optimizers; with checkpointing, AdamW fit at 6.250 GB allocated / 8.007 GB reserved and block8 fit at 6.250 GB allocated / 9.051 GB reserved.

## Boundaries and scale limits

Synthetic data only; 1-3 training steps; no real corpus convergence; reference non-fused block8 optimizer; GB10 UMA memory with nvidia-smi memory reporting unsupported, so PyTorch allocated/reserved memory and process telemetry are used as proxies.

## Claim scope

On GB10 with PyTorch 2.12, Transformers 4.57.6, bf16 GPT-2-small-class synthetic CUDA training, a reference blockwise 8-bit AdamW reduces persistent optimizer state from about 498 MB to about 250 MB but does not lower the observed peak CUDA allocation boundary versus PyTorch AdamW; gradient checkpointing, not optimizer quantization, gets batch 8 sequence 1024 under 10GB allocated/reserved in this setup.

## Why it stopped

Bounded proxy/direct memory test falsified the enabling claim for this implementation and environment: blockwise 8-bit state reduced persistent optimizer bytes but did not reduce the peak memory boundary versus the standard bf16 AdamW baseline.

## Recommended next action

Stop this run as a no-paper useful signal; if deepening locally, implement or use a production fused/tiled 8-bit AdamW that avoids full-moment dequantization and retest the batch 8 seq 1024 no-checkpoint boundary against bf16 AdamW.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused blockwise 8-bit AdamW peak-memory boundary for GPT-2-small
- Success threshold: At batch 8 sequence 1024 without checkpointing, fused/tiled blockwise 8-bit AdamW must keep peak CUDA allocated below 10.0 GB and at least 5% lower than PyTorch bf16 AdamW while preserving finite 3-step loss and no more than 20% throughput regression.
- Stop condition: Stop if the optimized 8-bit update still peaks within 5% of PyTorch AdamW, exceeds 10GB allocated at batch 8 sequence 1024, has non-finite loss, or requires changes outside optimizer implementation/checkpointing controls.

## Evidence references

- Artifact root: `<local-path>/projects/blockwise-8-bit-adamw-gpt-2-small-pretraining-under-10gb-vram-ff0fa5508cd9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
