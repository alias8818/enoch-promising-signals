# Memory-capped real-task validation of dynamic FP16 loss scaling

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `memory-capped-real-task-validation-of-dynamic-fp16-loss-sc-7417e718d9`
Run ID: `memory-capped-real-task-validation-of-dynamic-fp16-loss-sc-7417e718d9-20260614T080359316213+0000`

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

- Parent run decision: Dynamic loss scaling with mixed precision for tiny-VRAM stable training: enoch://control-plane/projects/dynamic-loss-scaling-with-mixed-precision-for-tiny-vram-stable-training-17c266387675/runs/dynamic-loss-scaling-with-mixed-precision-for-tiny-vram-stable-training-17c266387675-20260614T073801270226+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5687ed737c89

## What looked useful

Dynamic FP16 averaged 0.9363 validation accuracy and 0.9152 finite-step rate versus FP32 at 0.9444 accuracy and fixed static FP16 at 0.6830 accuracy with 0.2394 finite-step rate. The mechanism is supported for this bounded Tier 1 direct test, but it is not paper-ready.

## Boundaries and scale limits

Three seeds, 10 epochs, small MLP, scikit-learn digits dataset, single GB10 GPU, reserve-based memory cap rather than scheduler-enforced quota, SGD optimizer, deliberately high initial loss scale; no transformer/CNN benchmark breadth, no long run, no distributed setting, no production memory allocator study.

## Claim scope

On a small real handwritten-digit classification task under a CUDA/UMA reserve-based memory cap leaving about 2 GiB free, dynamic FP16 loss scaling recovered from an aggressively high initial loss scale and reached validation accuracy close to FP32 while fixed static scaling at the same initial scale skipped most updates.

## Why it stopped

Tier 1 direct validation completed; result is a no-paper useful signal because the evidence is small-scale and intentionally stress-calibrated, not publication-grade broad validation.

## Recommended next action

Run a bounded deepen follow-up on a standard small transformer or CNN task with FP32-master optimizer controls and a scheduler- or container-enforced memory cap before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Scheduler-capped standard-model validation of dynamic FP16 loss scaling
- Success threshold: Dynamic FP16 must reach at least 95% of the FP32/BF16 validation metric with at least 90% finite optimizer steps, while fixed static FP16 at the same initial scale either loses at least 25 percentage points of finite-step rate or at least 5% relative validation quality.
- Stop condition: Stop if dynamic FP16 fails to recover finite updates on two seeds, if static FP16 can match dynamic quality and finite-step rate without retuning, or if scheduler memory enforcement cannot be made reproducible locally.

## Evidence references

- Artifact root: `<local-path>/projects/memory-capped-real-task-validation-of-dynamic-fp16-loss-sc-7417e718d9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
