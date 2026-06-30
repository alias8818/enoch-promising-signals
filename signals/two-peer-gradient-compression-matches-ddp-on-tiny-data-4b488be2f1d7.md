# Two-peer gradient compression matches DDP on tiny data

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `two-peer-gradient-compression-matches-ddp-on-tiny-data-4b488be2f1d7`
Run ID: `two-peer-gradient-compression-matches-ddp-on-tiny-data-4b488be2f1d7-20260607T124059961027+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ed5c7ff6fa8c

## What looked useful

Error feedback is the deciding mechanism: at 1% top-k it kept mean loss delta versus exact averaging at -0.001593 with max positive loss delta 0.000919 and mean accuracy delta 0.000313, while no-error-feedback 1% top-k had mean loss delta 0.031135 and mean relative parameter L2 drift 0.3482.

## Boundaries and scale limits

Tiny synthetic data, 1,218-parameter MLP, 50 seeds, 200 steps, simulated two-peer update only; no real distributed process group, network transport, large model, real vision/language dataset, optimizer ablation, or long-horizon training.

## Claim scope

In a single-host simulation of two-peer synchronous training on a tiny 2D classification dataset, top-k gradient sparsification with error-feedback residuals matched exact DDP-style averaging on final loss and accuracy across 50 seeds while reducing transmitted gradient values by up to 93.69x; top-k without error feedback did not match exact averaging at aggressive sparsity on loss or parameter trajectory.

## Why it stopped

The result is direct for a tiny simulated update rule but only proxy evidence for real DDP systems, so it is not publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up with a real two-process PyTorch DDP communication hook on MNIST or CIFAR to test whether error-feedback top-k preserves convergence while reducing communicated bytes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-process DDP top-k error-feedback hook on a real small dataset
- Success threshold: Error-feedback top-k at 10% or lower transmitted values maintains validation accuracy within 1% and validation loss within 0.02 of exact DDP over at least 5 seeds while achieving at least 10x lower communicated gradient values.
- Stop condition: Stop if error-feedback top-k fails the validation loss/accuracy tolerance at 10% transmitted values or if the measured communication reduction is below 10x.

## Evidence references

- Artifact root: `<local-path>/projects/two-peer-gradient-compression-matches-ddp-on-tiny-data-4b488be2f1d7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
