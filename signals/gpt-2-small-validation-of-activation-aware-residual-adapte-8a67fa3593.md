# GPT-2-small validation of activation-aware residual adapter calibration

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `gpt-2-small-validation-of-activation-aware-residual-adapte-8a67fa3593`
Run ID: `gpt-2-small-validation-of-activation-aware-residual-adapte-8a67fa3593-20260519T032104266097+0000`

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

- Internal Enoch project: GPT-2-small validation of activation-aware residual adapter calibration: internal_generated:gpt-2-small-validation-of-activation-aware-residual-adapte-8a67fa3593

## What looked useful

Activation-aware calibration achieved the intended 1% per-layer initial residual perturbation, but the uncalibrated adapter baseline achieved lower NLL in all three seeds. Mean final NLL: activation-aware 8.2739, global control 8.2756, uncalibrated 8.2503; mean uncalibrated minus activation-aware NLL was -0.02366.

## Boundaries and scale limits

Not a paper-readiness validation: no longer training schedule, no target-ratio sweep, no multiple corpora/tasks, no full fine-tuning baseline, and no larger-model replication. Completed runs were split per seed/condition because a longer combined foreground run was SIGTERM'd by the local controller.

## Claim scope

GPT-2-small frozen rank-8 residual adapters on WikiText-2 with 3 fixed seeds, 80 adapter-only training steps, and 32,768 validation tokens. Activation-aware per-layer RMS calibration controls initial residual perturbation and is slightly better than a global-scale calibration control, but it does not outperform an uncalibrated residual-adapter baseline on validation NLL.

## Why it stopped

Direct GPT-2-small validation did not support the activation-aware calibration claim against a real uncalibrated adapter baseline; evidence is bounded and useful but not paper-ready.

## Recommended next action

Stop this follow-up at depth 4: record the bounded negative/useful signal rather than chaining another automatic follow-up.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-validation-of-activation-aware-residual-adapte-8a67fa3593`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
