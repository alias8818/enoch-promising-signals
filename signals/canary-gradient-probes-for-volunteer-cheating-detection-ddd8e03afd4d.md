# Canary Gradient Probes for Volunteer Cheating Detection

Status: `useful_signal`
Project ID: `canary-gradient-probes-for-volunteer-cheating-detection-ddd8e03afd4d`
Run ID: `canary-gradient-probes-for-volunteer-cheating-detection-ddd8e03afd4d-20260515T030932273302+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/37d210749f4c

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Synthetic logistic proxy supports the canary-gradient mechanism at higher canary budgets, but low-overhead settings are weak or borderline and no real volunteer/federated/deep-model evidence was produced.

## Recommended next action

Stop this run as a proxy-only mixed result; run one bounded direct federated-learning benchmark before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Federated Benchmark for Hidden Canary Gradient Audits
- Success threshold: TPR >= 0.80 at FPR <= 0.05 for skip/replay cheating with <= 2% extra training examples or tokens and <= 1% final task metric degradation across at least 5 seeds.
- Stop condition: Stop if skip/replay TPR remains below 0.70 at 5% FPR at <= 2% overhead, or if utility degradation exceeds 1% in the lowest-overhead setting that reaches the detection threshold.

## Evidence references

- Artifact root: `<local-path>/projects/canary-gradient-probes-for-volunteer-cheating-detection-ddd8e03afd4d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
