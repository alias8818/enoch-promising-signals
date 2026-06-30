# LoRA with Minimal Rank for 2GB VRAM Fine-tuning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lora-with-minimal-rank-for-2gb-vram-fine-tuning-8ea85f203aea`
Run ID: `lora-with-minimal-rank-for-2gb-vram-fine-tuning-8ea85f203aea-20260609T150835245312+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/32992304ea4c

## What looked useful

Lowering LoRA rank from 16 to 1 saves only MiB to low hundreds of MiB depending on target modules, while base precision and activation/runtime memory dominate 2GB feasibility. A LLaMA-like 1.3B estimate misses 2GB with fp16 base weights even at rank 1, but fits the accounting estimate with int4 base weights even at rank 16. The synthetic control shows ranks below the true rank-8 update underfit sharply.

## Boundaries and scale limits

No actual GPU fine-tuning was run; the probe did not measure CUDA allocator overhead, PEFT/bitsandbytes kernels, paged optimizer behavior, tokenizer/dataloader memory, throughput, or downstream language-model validation loss.

## Claim scope

Bounded CPU-local accounting and synthetic rank-control evidence for whether reducing LoRA rank is the binding factor in 2GB-VRAM fine-tuning.

## Why it stopped

Useful proxy/accounting result, not a full validation: minimal rank alone is not supported as the decisive enabler for 2GB fine-tuning, and direct GPU evidence would be required for a stronger claim.

## Recommended next action

Stop this no-paper run; if continuing, run a bounded direct PEFT/QLoRA experiment under a true 2GB GPU memory cap comparing rank 1/2/4/8/16 with peak memory and validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct 2GB-Capped PEFT/QLoRA Rank Sweep
- Success threshold: At least one quantized configuration completes under 2GB with peak reserved memory below 1.9 GiB, and rank-vs-loss curves show whether rank below 4 has an unacceptable validation-loss penalty relative to rank 8 or 16.
- Stop condition: Stop if no rank completes under 2GB after enabling standard QLoRA memory controls, or if all completing ranks have validation loss within 2 percent while rank contributes less than 10 percent of peak-memory variance.

## Evidence references

- Artifact root: `<local-path>/projects/lora-with-minimal-rank-for-2gb-vram-fine-tuning-8ea85f203aea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
