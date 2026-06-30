# GB10 Transformer Training Stability With Checkpoint Resume

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gb10-transformer-training-stability-with-checkpoint-resume-b708cd69c2`
Run ID: `gb10-transformer-training-stability-with-checkpoint-resume-b708cd69c2-20260613T001128590575+0000`

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

- Parent run decision: Canary-MiniTask Validation for Volunteer GB10 Training: enoch://control-plane/projects/canary-minitask-validation-for-volunteer-gb10-training-c4359dae7013/runs/canary-minitask-validation-for-volunteer-gb10-training-c4359dae7013-20260612T232441057400+0000
- Parent run decision: Bounded Real-Workload GB10 Training Stability Check: enoch://control-plane/projects/bounded-real-workload-gb10-training-stability-check-cebd15ea12/runs/bounded-real-workload-gb10-training-stability-check-cebd15ea12-20260612T233458646267+0000

## What looked useful

Full-state checkpoint resume was trajectory-identical to continuous training across seeds 101, 202, and 303: zero final loss delta and zero parameter delta. Ablations produced nonzero relative parameter L2 deltas: mean 0.0439 without optimizer state, 0.0781 without torch RNG state, and 0.1191 without batch RNG state. Missing batch RNG also caused the largest mean final loss absolute delta at 0.00484.

## Boundaries and scale limits

The completed Tier 2 run used a resized 4-layer, 256-width Transformer for 300 steps with three seeds after a larger 6-layer, 512-width, 600-step command was externally terminated. It did not test real datasets, GPT-2-small scale, mixed precision scaler state, learning-rate schedulers, dataloader worker processes, distributed training, crash consistency under process kill, or multi-node checkpoint I/O.

## Claim scope

On a single NVIDIA GB10 with PyTorch 2.12.0+cu130, a small dense GPT-style Transformer trained on a synthetic autoregressive token stream resumed exactly from checkpoint across three fixed seeds when model, AdamW optimizer, PyTorch RNG, and batch-generator state were restored. Incomplete checkpoints diverged from an uninterrupted continuous baseline in parameter space and, for missing batch RNG, in scalar loss trajectory.

## Why it stopped

Moderate direct local evidence supports the checkpoint-state mechanism, but the completed validation remains small-to-medium and synthetic, so it is not paper-positive.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded deepen test should use a real text corpus, GPT-2-small-class or parameter-matched model, process-level restart, and additional checkpoint fields such as scheduler and AMP scaler state.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus GPT-2-Small Checkpoint Resume State Ablation
- Success threshold: Full-state resume has zero or numerically negligible trajectory delta versus continuous baseline across all seeds, while at least two incomplete-state ablations produce consistent parameter relative L2 delta above 1e-3 or validation-loss delta above 1e-4 after resume.
- Stop condition: Stop if full-state resume is not reproducible under process-level restart, if ablations do not separate from baseline across fixed seeds, or if the run cannot complete within the local GB10 execution budget with durable partial metrics.

## Evidence references

- Artifact root: `<local-path>/projects/gb10-transformer-training-stability-with-checkpoint-resume-b708cd69c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
