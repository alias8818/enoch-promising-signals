# LoRA + 8-bit AdamW for Sub-4GB VRAM Fine-tuning

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `lora-8-bit-adamw-for-sub-4gb-vram-fine-tuning-b100bd0e32f0`
Run ID: `lora-8-bit-adamw-for-sub-4gb-vram-fine-tuning-b100bd0e32f0-20260621T052142131213+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/41fa2e2055c3

## What looked useful

LoRA reduced trainable parameters from 124.4M to 0.811M, and AdamW8bit reduced measured LoRA optimizer state from 3.09 MiB to 1.71 MiB with uint8 state tensors. Bfloat16 LoRA+AdamW8bit stayed under 4GB peak allocated at batch=1 seq=128, batch=2 seq=512, and batch=4 seq=512; the strict reserved-cache-safe larger setting was batch=2 seq=512.

## Boundaries and scale limits

Synthetic token data only; randomly initialized GPT-2-small-class model only; three-step runs only; no pretrained checkpoint, real dataset, validation loss, long-run convergence, gradient checkpointing sweep, or larger-model test. PyTorch reserved memory exceeded 4GB for batch=4 sequence=512 even though live allocation stayed under 4GB.

## Claim scope

LoRA plus bitsandbytes AdamW8bit executed short synthetic GPT-2-small-class CUDA training steps on GB10 below a 4GB live CUDA allocation budget, with lower LoRA optimizer-state memory than torch AdamW.

## Why it stopped

No-paper useful signal: this was a synthetic/proxy memory and optimizer-state probe, not a full validation of fine-tuning quality or convergence.

## Recommended next action

Run a bounded direct follow-up on a pretrained GPT-2-small checkpoint and a small real text dataset, requiring validation loss to decrease while peak allocated and reserved CUDA memory remain under 4GB.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2-small LoRA+AdamW8bit under strict 4GB memory
- Success threshold: Validation loss decreases by at least 2% over the bounded run, LoRA+AdamW8bit uses less optimizer-state memory than LoRA torch AdamW, and peak allocated plus reserved CUDA memory both remain below 4096 MiB.
- Stop condition: Stop as negative if validation loss does not improve, if memory exceeds 4096 MiB under reserved-cache accounting at the smallest practical microbatch, or if AdamW8bit fails on the target CUDA backend.

## Evidence references

- Artifact root: `<local-path>/projects/lora-8-bit-adamw-for-sub-4gb-vram-fine-tuning-b100bd0e32f0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
