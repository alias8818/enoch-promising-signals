# Medium Lottery Gradient Audit Confirmation on FEMNIST and CIFAR-10

Status: `useful_signal`
Project ID: `medium-lottery-gradient-audit-confirmation-on-femnist-and-690ec03534`
Run ID: `medium-lottery-gradient-audit-confirmation-on-femnist-and-690ec03534-20260517T051123310333+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Medium Lottery Gradient Audit Confirmation on FEMNIST and CIFAR-10: internal_generated:medium-lottery-gradient-audit-confirmation-on-femnist-and-690ec03534

## What looked useful

Gradient masking showed a robust FEMNIST-source mechanism signal (+5.08 percentage points over random, +3.43 points over shuffled-gradient) but CIFAR-10 failed the label-specific shuffled-gradient control (gradient was -0.13 points below shuffled-gradient).

## Boundaries and scale limits

Not a true LEAF FEMNIST federated writer/client split; 15k train and 3k test examples per dataset, three seeds, four epochs, one compact CNN, one sparsity level, one optimizer, and one one-shot audit scoring rule.

## Claim scope

A local medium-scale CNN test on CIFAR-10 and EMNIST ByClass as the FEMNIST image/classification source found that a one-shot SNIP-style abs(weight * gradient) audit mask at 80% sparsity consistently improves over random pruning on both datasets, but only the EMNIST/FEMNIST-source result also beats the shuffled-label gradient-mask ablation.

## Why it stopped

Medium direct evidence is mixed: EMNIST/FEMNIST-source supports the mechanism, but CIFAR-10 does not beat the shuffled-label gradient ablation, so the stated cross-dataset lottery-gradient audit confirmation is not closed.

## Recommended next action

Stop paper escalation for this run; run one bounded deepen follow-up using true LEAF FEMNIST writer partitions and a longer CIFAR-10 confirmation before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: True FEMNIST Writer-Partition and Longer CIFAR-10 Lottery Gradient Audit
- Success threshold: Real-label gradient masks improve final accuracy by at least 2 percentage points over both random and shuffled-label gradient masks on both true FEMNIST and CIFAR-10, with positive paired deltas in at least 4 of 5 seeds per dataset.
- Stop condition: Stop as no-paper if either dataset fails to beat the shuffled-label gradient ablation or if the advantage over random pruning drops below 2 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/medium-lottery-gradient-audit-confirmation-on-femnist-and-690ec03534`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
