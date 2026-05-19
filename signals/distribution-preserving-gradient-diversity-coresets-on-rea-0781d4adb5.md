# Distribution-Preserving Gradient Diversity Coresets on Real Tiny Text

Status: `useful_signal`
Project ID: `distribution-preserving-gradient-diversity-coresets-on-rea-0781d4adb5`
Run ID: `distribution-preserving-gradient-diversity-coresets-on-rea-0781d4adb5-20260516T040152921932+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3920ac4291bd

## What looked useful

The selector exactly matched distribution-random JS divergence while raising mean gradient pairwise cosine distance by 0.00699-0.00871 and improving accuracy versus distribution-random by +2.00 points at 5% and +1.93 points at 10%; the effect vanished at 20% and log-loss was worse than distribution-random at all tested fractions.

## Boundaries and scale limits

Evidence is limited to a shallow TF-IDF/SVD logistic classifier, one real text dataset subset, five seeds, and coreset selection from a full observed training pool. It does not validate token-level language-model training, transformer gradients, large corpora, acquisition cost, or robustness across datasets and stronger coreset baselines.

## Claim scope

On a controlled 20 Newsgroups four-class real-text classification task with 1200 train and 600 test examples, class/length distribution-preserving farthest-first selection in per-example logistic-gradient space improved mean accuracy over distribution-random selection at 5% and 10% coreset sizes while preserving the same distribution quotas.

## Why it stopped

No-paper closure: Tier-1 direct evidence supports a mechanism signal but is mixed and too narrow for publication readiness.

## Recommended next action

Run a bounded medium confirmation with neural text gradient embeddings on multiple real datasets and compare against BADGE, k-center, herding, uncertainty, distribution-random, and random baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Neural Gradient Confirmation for Distribution-Preserving Text Coresets
- Success threshold: Mean accuracy and macro-F1 at least 1 percentage point above the strongest non-proposed baseline on at least two of three datasets at 5% or 10%, with distribution JS no worse than distribution-random and log-loss degradation no greater than 0.01.
- Stop condition: Stop as unsupported if the proposed selector fails to beat distribution-random or BADGE-style selection by 1 point on at least two datasets, or if accuracy gains consistently come with log-loss degradation greater than 0.01.

## Evidence references

- Artifact root: `<local-path>/projects/distribution-preserving-gradient-diversity-coresets-on-rea-0781d4adb5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
