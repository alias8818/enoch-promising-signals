# LoRA fine-tuning with frozen CPU base for tiny-VRAM adaptation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lora-fine-tuning-with-frozen-cpu-base-for-tiny-vram-adaptation-b82995d2ba00`
Run ID: `lora-fine-tuning-with-frozen-cpu-base-for-tiny-vram-adaptation-b82995d2ba00-20260620T153842620446+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9250a8adcc84

## What looked useful

Rank-matched CPU-frozen-base LoRA reached validation MSE 0.000603 versus dense 0.001117, with estimated VRAM 0.941 MiB versus dense 9.750 MiB and GPU-resident LoRA 3.191 MiB. On the full-rank control, CPU-frozen-base LoRA validation MSE was 0.044777 versus dense 0.001259, confirming the expected low-rank capacity limit.

## Boundaries and scale limits

No GPU was visible on this worker, so actual VRAM allocation, CPU-to-GPU transfer overhead, transformer execution, and language-model validation quality were not directly measured. The primary run used 768x768 linear maps, rank 8 adapters, 4096 train samples, 1024 validation samples, and 800 Adam steps.

## Claim scope

On a CPU-only synthetic linear adaptation task, frozen-base LoRA can learn rank-matched low-rank deltas while explicit training-state accounting predicts substantially lower tiny-device memory when frozen base parameters are kept off-device.

## Why it stopped

Closed as no-paper useful-signal evidence: the local proxy supports the mechanism and memory accounting but does not directly validate the tiny-VRAM GPU systems claim.

## Recommended next action

Run the same control structure on a real tiny-VRAM GPU with a small transformer block and measure actual VRAM, transfer time, tokens/s, and validation loss for CPU-frozen-base LoRA versus GPU-resident LoRA.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-VRAM GPU measurement for CPU-frozen-base LoRA
- Success threshold: CPU-frozen-base LoRA fits a transformer adaptation configuration that GPU-resident LoRA cannot fit under the same tiny-VRAM cap, while reaching validation loss within 10% relative of GPU-resident LoRA on a smaller fitting configuration and retaining at least 25% of its throughput.
- Stop condition: Stop if CPU-frozen-base LoRA does not reduce measured peak VRAM versus GPU-resident LoRA, cannot complete a bounded transformer run, or falls below 25% of GPU-resident LoRA throughput without unlocking a previously non-fitting configuration.

## Evidence references

- Artifact root: `<local-path>/projects/lora-fine-tuning-with-frozen-cpu-base-for-tiny-vram-adaptation-b82995d2ba00`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
