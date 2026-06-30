# Frozen INT2 base + FP4 LoRA adapter for CPU continual pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `frozen-int2-base-fp4-lora-adapter-for-cpu-continual-pretraining-cbacebf4bd79`
Run ID: `frozen-int2-base-fp4-lora-adapter-for-cpu-continual-pretraining-cbacebf4bd79-20260630T021851986193+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1ff1ce5b8c3a

## What looked useful

The mechanism is plausible but rank-sensitive: rank 4/8 recovered little dense improvement, while rank 16/24 recovered substantially more. Across three rank-24 seeds, FP4 LoRA improved target loss over frozen INT2 by 0.519 nats on average but remained 0.355 nats worse than dense continual training and 0.470 nats worse than FP32 LoRA.

## Boundaries and scale limits

Not a transformer, not GPT-2-small-class, not real text, not packed low-bit CPU kernels, and not a throughput benchmark. Computation used dequantized NumPy arrays. FP4 LoRA trailed dense FP32 and FP32 LoRA controls and increased source-domain loss, so this does not validate broad CPU continual pretraining.

## Claim scope

In a NumPy CPU 64-token Markov next-token toy task with fake/storage INT2 base quantization and fake/storage FP4 LoRA quantization, a frozen INT2 base plus FP4-style LoRA can adapt to a target-domain shift and recover a mean 59.5% of dense FP32 continual-training target-loss improvement at rank 24 across three seeds, with a mean 5.82x storage advantage over dense FP32 weights.

## Why it stopped

Bounded toy evidence supports the adaptation mechanism but is proxy-only and mixed, so it is insufficient for a paper-ready CPU continual-pretraining claim.

## Recommended next action

Stop this run as no-paper useful signal; next concrete step is a bounded tiny-transformer follow-up with real text, block-scaled FP4 adapters, packed or explicitly simulated INT2 base storage, and CPU wall-clock/memory metrics against dense and standard LoRA controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-transformer CPU continual pretraining with block-scaled FP4 LoRA over frozen INT2 base
- Success threshold: FP4 LoRA over frozen INT2 recovers at least 70% of the dense or standard-LoRA target validation-loss improvement, stays within 0.15 nats of the best LoRA control, retains at least 4x storage reduction, and does not exceed 1.5x CPU time per token versus the closest low-bit control.
- Stop condition: Stop as negative if FP4 LoRA recovers less than 50% of target validation-loss improvement, has more than 0.3 nats gap to FP32 LoRA at matched rank, or loses the storage/CPU advantage after honest packing and timing.

## Evidence references

- Artifact root: `<local-path>/projects/frozen-int2-base-fp4-lora-adapter-for-cpu-continual-pretraining-cbacebf4bd79`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
