# Actual DFlash/Qwen per-token prefix-label survival prediction

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `actual-dflash-qwen-per-token-prefix-label-survival-predict-d07c3fd83e`
Run ID: `actual-dflash-qwen-per-token-prefix-label-survival-predict-d07c3fd83e-20260520T020947052621+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-trace DFlash prefix labels for SSD-lite verification prediction: enoch://control-plane/projects/real-trace-dflash-prefix-labels-for-ssd-lite-verification-4d58f0064e/runs/real-trace-dflash-prefix-labels-for-ssd-lite-verification-4d58f0064e-20260520T015907859479+0000
- Parent run decision: Per-token DFlash outcome labels for SSD-lite verification prediction: enoch://control-plane/projects/per-token-dflash-outcome-labels-for-ssd-lite-verification-4d769e7131/runs/per-token-dflash-outcome-labels-for-ssd-lite-verification-4d769e7131-20260520T015407832810+0000

## What looked useful

Survival prediction is a real target, but the tested deployable feature expansion is not novel against confidence/margin baselines: aggregate no-gold ROC-AUC was 0.780 +/- 0.025 versus 0.795 +/- 0.006 for confidence-only, while permuted-label control was 0.440 +/- 0.062.

## Boundaries and scale limits

80 train and 80 validation examples per seed, 8 prefix positions, seeds 17/23/42, CPU inference, Qwen2.5-0.5B-Instruct only; no larger Qwen models, hidden-state probes, DFlash implementation internals, distribution-shift tasks, or end-to-end early-exit utility validation.

## Claim scope

On SST-2 sentiment prompts using Qwen/Qwen2.5-0.5B-Instruct, prefix-label survival is measurable and separable from random/permuted controls, but deployable prefix/logprob features do not outperform a simple confidence-only baseline across three fixed-seed bounded replications.

## Why it stopped

Tier-4 paper-readiness threshold was not met because the deployable predictor did not improve over a real confidence-only baseline, despite direct actual-Qwen evidence and fixed-seed replications.

## Recommended next action

Stop this follow-up at depth 4: record the negative no-paper result that actual Qwen survival is predictable but the deployable DFlash-style features fail to beat confidence-only baselines.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/actual-dflash-qwen-per-token-prefix-label-survival-predict-d07c3fd83e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
