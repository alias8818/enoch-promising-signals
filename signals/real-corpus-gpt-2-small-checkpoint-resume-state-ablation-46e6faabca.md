# Real-Corpus GPT-2-Small Checkpoint Resume State Ablation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `real-corpus-gpt-2-small-checkpoint-resume-state-ablation-46e6faabca`
Run ID: `real-corpus-gpt-2-small-checkpoint-resume-state-ablation-46e6faabca-20260613T011053646664+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: GB10 Transformer Training Stability With Checkpoint Resume: enoch://control-plane/projects/gb10-transformer-training-stability-with-checkpoint-resume-b708cd69c2/runs/gb10-transformer-training-stability-with-checkpoint-resume-b708cd69c2-20260613T001128590575+0000
- Parent run decision: Bounded Real-Workload GB10 Training Stability Check: enoch://control-plane/projects/bounded-real-workload-gb10-training-stability-check-cebd15ea12/runs/bounded-real-workload-gb10-training-stability-check-cebd15ea12-20260612T233458646267+0000

## What looked useful

Full-state resume matched continuous training exactly at every common post-split eval step for all three seeds. Dropping optimizer state modestly worsened mean eval loss by +0.0194 (+0.296%). Dropping RNG was negligible in this deterministic-order setup. Dropping scheduler state improved mean eval loss by -0.0618 (-0.941%) because the cosine schedule restarted to a higher post-split learning rate; model-only resume showed a similar schedule-driven improvement.

## Boundaries and scale limits

The run used GPT-2 config initialized from scratch, WikiText-2 raw text, 128-token blocks, effective batch size 8, deterministic batch order, and 1,000 optimizer steps. It does not establish behavior for pretrained GPT-2 fine-tuning, full-scale pretraining corpora, stochastic dataloader resume, longer convergence, or alternative LR schedules.

## Claim scope

In a three-seed, 1,000-step from-scratch GPT-2-small-class training run on WikiText-2, full checkpoint resume exactly reproduced continuous training, while dropping optimizer, scheduler, RNG, or all non-model state changed final held-out loss by variant-specific amounts.

## Why it stopped

The bounded validation produced a reproducible useful mechanism signal, but the claim is too scoped and schedule-dependent for publication readiness.

## Recommended next action

Stop paper escalation for this run; the next bounded test should repeat the ablation on pretrained GPT-2 fine-tuning with both cosine and constant-LR controls to separate resume-state effects from scheduler-phase effects.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2 Resume-State Ablation with LR-Schedule Controls
- Success threshold: Show a consistent variant effect of at least 0.2% held-out loss delta versus full resume, or demonstrate that scheduler control eliminates the model-only/no-scheduler advantage across at least three seeds.
- Stop condition: Stop if full-state resume fails to exactly replay continuous training, if scheduler-controlled variants show less than 0.05% loss delta across all seeds, or if the run cannot complete pretrained fine-tuning locally within the bounded worker budget.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-gpt-2-small-checkpoint-resume-state-ablation-46e6faabca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
