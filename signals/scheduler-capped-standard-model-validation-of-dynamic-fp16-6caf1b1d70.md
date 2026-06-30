# Scheduler-capped standard-model validation of dynamic FP16 loss scaling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `scheduler-capped-standard-model-validation-of-dynamic-fp16-6caf1b1d70`
Run ID: `scheduler-capped-standard-model-validation-of-dynamic-fp16-6caf1b1d70-20260614T082459338211+0000`

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

- Parent run decision: Memory-capped real-task validation of dynamic FP16 loss scaling: enoch://control-plane/projects/memory-capped-real-task-validation-of-dynamic-fp16-loss-sc-7417e718d9/runs/memory-capped-real-task-validation-of-dynamic-fp16-loss-sc-7417e718d9-20260614T080359316213+0000
- Parent run decision: Dynamic loss scaling with mixed precision for tiny-VRAM stable training: enoch://control-plane/projects/dynamic-loss-scaling-with-mixed-precision-for-tiny-vram-stable-training-17c266387675/runs/dynamic-loss-scaling-with-mixed-precision-for-tiny-vram-stable-training-17c266387675-20260614T073801270226+0000

## What looked useful

Scheduler-capping is a viable mechanism for preventing FP16 loss-scale overflow skips, but this standard-model validation suggests skipped-step removal alone is insufficient evidence of quality improvement and a simple static cap is a strong control.

## Boundaries and scale limits

Single GB10 GPU, small character-level Transformer, 1,500-step runs, Tiny Shakespeare only; not GPT-2-small scale, not multi-GPU, not long-horizon language-model pretraining.

## Claim scope

On a 826k-parameter Tiny Shakespeare causal Transformer trained for 1,500 CUDA AMP FP16 steps across seeds 13, 17, and 23, scheduler-capped dynamic loss scaling eliminated GradScaler overflow skips but did not improve validation loss versus default dynamic AMP and did not outperform a static conservative cap.

## Why it stopped

Tier 2 fixed-seed validation found mechanism support but no scheduler-specific validation-loss benefit over default dynamic AMP or a static cap ablation.

## Recommended next action

Stop this branch as no-paper useful evidence unless a bounded follow-up specifically tests scheduler caps against static caps in a regime where static low scales cause measurable gradient underflow or quality loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Underflow-sensitive scheduler caps versus static caps on a larger tokenized Transformer
- Success threshold: Scheduler-capped AMP must reduce skipped steps by at least 90% versus uncapped dynamic AMP and improve mean validation loss by at least 0.02 nats/token versus the best static-cap control across three seeds.
- Stop condition: Stop if any static cap matches scheduler-capped validation loss within 0.01 nats/token while also keeping overflow skips below 0.5%, or if scheduler-capped loss is not better than default dynamic AMP.

## Evidence references

- Artifact root: `<local-path>/projects/scheduler-capped-standard-model-validation-of-dynamic-fp16-6caf1b1d70`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
