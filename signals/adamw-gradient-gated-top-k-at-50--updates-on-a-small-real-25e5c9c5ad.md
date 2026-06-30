# AdamW gradient-gated top-k at 50% updates on a small real model task

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adamw-gradient-gated-top-k-at-50--updates-on-a-small-real-25e5c9c5ad`
Run ID: `adamw-gradient-gated-top-k-at-50--updates-on-a-small-real-25e5c9c5ad-20260527T064152266005+0000`

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

- Parent run decision: Gradient-Gated Sparse Optimizer: Train Top-k% Parameters by Gradient Signal: enoch://control-plane/projects/gradient-gated-sparse-optimizer-train-top-k-parameters-by-gradient-signal-7fb674a3e80b/runs/gradient-gated-sparse-optimizer-train-top-k-parameters-by-gradient-signal-7fb674a3e80b-20260526T173311361295+0000
- Parent run decision: AdamW Gradient-Gated Top-k on a Real Small Model Task: enoch://control-plane/projects/adamw-gradient-gated-top-k-on-a-real-small-model-task-4da797c021/runs/adamw-gradient-gated-top-k-on-a-real-small-model-task-4da797c021-20260526T232851382463+0000

## What looked useful

Gradient-gated top-k 50% AdamW reached 0.9855 mean accuracy versus 0.9863 for dense AdamW, 0.9829 for random 50%, and 0.9537 for bottom-gradient 50%. The mechanism is locally supported because top-k preserved dense performance and bottom-k failed, but random 50% was also close enough that the effect is not publication-grade.

## Boundaries and scale limits

Only MNIST and a small CNN were tested; MNIST is saturated, training was short, hyperparameters were not swept, no language model or harder vision dataset was tested, and the PyTorch masking implementation does not demonstrate wall-clock or memory speedups.

## Claim scope

On MNIST with a compact CNN trained for 5 epochs across seeds 17, 23, and 41, per-tensor top-50%-by-gradient AdamW preserved dense AdamW test accuracy within 0.08 percentage points while applying updates to exactly 50% of parameter elements per step.

## Why it stopped

Tier-2 fixed-seed direct evidence produced a bounded useful signal but not paper-positive evidence; closing as no-paper rather than continuing indefinitely.

## Recommended next action

Run the same dense/top-k/random/bottom-k comparison on a less saturated small real task such as CIFAR-10 with a compact ResNet before considering any paper or large-scale follow-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Gradient-gated top-k AdamW on a less saturated small vision benchmark
- Success threshold: Top-k 50% mean accuracy within 1.0 percentage point of dense AdamW and at least 0.5 percentage points above random 50%, with bottom-gradient clearly worse, across at least 3 fixed seeds.
- Stop condition: Stop as unsupported if top-k falls more than 1.0 percentage point below dense or fails to beat random 50% by 0.5 percentage points on the less saturated task.

## Evidence references

- Artifact root: `<local-path>/projects/adamw-gradient-gated-top-k-at-50--updates-on-a-small-real-25e5c9c5ad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
