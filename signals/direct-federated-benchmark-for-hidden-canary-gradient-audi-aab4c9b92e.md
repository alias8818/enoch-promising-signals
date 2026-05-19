# Direct Federated Benchmark for Hidden Canary Gradient Audits

Status: `compute_scale_blocked`
Project ID: `direct-federated-benchmark-for-hidden-canary-gradient-audi-aab4c9b92e`
Run ID: `direct-federated-benchmark-for-hidden-canary-gradient-audi-aab4c9b92e-20260515T031856726636+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/37d210749f4c

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 1 direct evidence supports the hidden-canary gradient-audit mechanism in several controlled MNIST federated aggregate-gradient runs, but one target seed missed the threshold and the 50-client single-canary condition failed; this is mechanism support, not publication-grade validation.

## Recommended next action

Run a bounded medium confirmation with 5-10 seeds, multiple datasets/models, client counts 20/50/100, FedSGD versus FedAvg, and clipping/noise sweeps before considering this publishable.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium-Scale Robustness Benchmark for Hidden Canary Gradient Audits
- Success threshold: For the 20-client, batch-32, one-canary condition, lower 95% confidence bound AUC >= 0.90 and TPR@5%FPR >= 0.50 across seeds, while controls remain near chance; larger-client failures must be characterized rather than ignored.
- Stop condition: Stop if the 20-client single-canary condition fails the lower-bound threshold in two datasets/models or if controls show comparable separation to the true canary score.

## Evidence references

- Artifact root: `<local-path>/projects/direct-federated-benchmark-for-hidden-canary-gradient-audi-aab4c9b92e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
