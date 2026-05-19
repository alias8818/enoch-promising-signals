# True FEMNIST Writer-Partition and Longer CIFAR-10 Lottery Gradient Audit

Status: `useful_signal`
Project ID: `true-femnist-writer-partition-and-longer-cifar-10-lottery-276241cd81`
Run ID: `true-femnist-writer-partition-and-longer-cifar-10-lottery-276241cd81-20260517T052203362256+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: True FEMNIST Writer-Partition and Longer CIFAR-10 Lottery Gradient Audit: internal_generated:true-femnist-writer-partition-and-longer-cifar-10-lottery-276241cd81

## What looked useful

SNIP beat random by 4.69 percentage points on CIFAR-10 and 4.02 points on true writer-partition FED-EMNIST, but trailed dense by 7.10 and 3.41 points respectively. Magnitude-at-initialization collapsed on both targets.

## Boundaries and scale limits

FED-EMNIST used 800 of 3,400 real writer clients with a 200-example/client cap; CIFAR-10 used 20 epochs rather than a high-accuracy production schedule; only one 10% sparsity point and one-shot initial masks were tested.

## Claim scope

At 10% kept weights, one-shot initial gradient pruning gives reproducibly better sparse subnetworks than random masks on full CIFAR-10 over 20 epochs and on an 800-client true writer-partition FED-EMNIST subset over 10 epochs, but it does not match dense training.

## Why it stopped

Bounded direct validation supports a useful mechanism over random controls but fails the paper gate because sparse gradient masks remain materially below the dense baseline and robustness across sparsity/rewinding/full-writer scale is untested.

## Recommended next action

Stop as no-paper useful evidence unless the controller permits one final depth-4 deepen run with full 3,400-client FED-EMNIST, a 10/20/30% sparsity sweep, and one-shot versus rewinding masks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Full-Writer FEMNIST Sparsity and Rewinding Gradient Audit
- Success threshold: SNIP or rewound-gradient masks beat random by at least 3 accuracy points at all tested sparsities and reduce the dense-baseline gap to under 2 points at 20% or 30% kept weights on full writer-partition FED-EMNIST.
- Stop condition: Stop if gradient masks fail to beat random by 3 points on the first full-writer sparsity setting or if rewinding/higher keep fractions do not reduce the dense gap below 2 points.

## Evidence references

- Artifact root: `<local-path>/projects/true-femnist-writer-partition-and-longer-cifar-10-lottery-276241cd81`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
