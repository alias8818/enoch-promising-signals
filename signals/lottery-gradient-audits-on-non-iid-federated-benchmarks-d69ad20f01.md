# Lottery Gradient Audits on Non-IID Federated Benchmarks

Status: `useful_signal`
Project ID: `lottery-gradient-audits-on-non-iid-federated-benchmarks-d69ad20f01`
Run ID: `lottery-gradient-audits-on-non-iid-federated-benchmarks-d69ad20f01-20260517T050614145515+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/87ce680fc6cc

## What looked useful

Across 12 seeds at 5 percent sparsity, non-IID post-training top-k gradient masks achieved 1.000 nearest-neighbor same-majority recovery and 0.962 mask/label-histogram correlation, versus 0.051 and -0.007 for matched random masks; sensitivity runs at 1 percent and 10 percent top-k preserved 1.000 non-IID nearest-neighbor recovery over 6 seeds each.

## Boundaries and scale limits

One small dataset, one MLP architecture, deliberately strong label skew, full-batch visible client gradients, no secure aggregation, no differential privacy, no partial participation, no feature-skew/quantity-skew variants, and no larger CNN/FEMNIST/CIFAR validation.

## Claim scope

In a controlled small federated sklearn-digits benchmark with a 64-64-10 MLP, 20 clients, explicit 80 percent label-majority non-IID partitions, and full-batch per-client gradients, top-k absolute gradient masks recover client label-skew structure far above random sparse-mask controls.

## Why it stopped

Tier 1 controlled small direct test supports the mechanism but remains no-paper evidence because it is limited to one small dataset, one model, and strong label skew.

## Recommended next action

Run a medium direct confirmation on FEMNIST and CIFAR-10 using a small CNN, partial client participation, IID/non-IID controls, and matched random-mask controls before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Lottery Gradient Audit Confirmation on FEMNIST and CIFAR-10
- Success threshold: On both datasets, post-training sparse masks should exceed random-mask nearest-neighbor same-majority recovery by at least 0.35 absolute and exceed IID by at least 0.20 absolute, with mask/histogram correlation at least 0.50 in non-IID and stable across two top-k sparsities.
- Stop condition: Stop as unsupported if either dataset fails to beat random masks by 0.20 absolute in nearest-neighbor same-majority recovery or if the signal appears only under the strongest label-skew condition.

## Evidence references

- Artifact root: `<local-path>/projects/lottery-gradient-audits-on-non-iid-federated-benchmarks-d69ad20f01`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
