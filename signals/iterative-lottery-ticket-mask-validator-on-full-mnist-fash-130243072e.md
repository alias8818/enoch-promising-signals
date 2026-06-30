# Iterative Lottery-Ticket Mask Validator on Full MNIST/Fashion-MNIST CNNs

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `iterative-lottery-ticket-mask-validator-on-full-mnist-fash-130243072e`
Run ID: `iterative-lottery-ticket-mask-validator-on-full-mnist-fash-130243072e-20260525T200320957594+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Lottery Ticket Sparse Mask Validator: enoch://control-plane/projects/lottery-ticket-sparse-mask-validator-cb9cd555f0d4/runs/lottery-ticket-sparse-mask-validator-cb9cd555f0d4-20260525T183150978755+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/01c5be3baed4

## What looked useful

Full-split MNIST/Fashion-MNIST direct evidence supports that IMP-derived rewound masks encode useful structure beyond random masks in this bounded CNN setting; all four dataset/seed cells passed the predefined threshold.

## Boundaries and scale limits

Only one small CNN, one optimizer, one 80% sparsity level, two random seeds, one matched random-mask replicate per seed, and short one-epoch prune/validation training were tested. No train-to-convergence, multi-architecture, multi-sparsity, or confidence-interval study was run.

## Claim scope

In a two-seed Tier 1 direct test on full MNIST and Fashion-MNIST with a small PyTorch CNN, 2-round IMP rewound masks at about 80% global weight sparsity preserved dense accuracy within 1 percentage point and beat layerwise matched random masks by at least 1 percentage point under a one-epoch validation budget.

## Why it stopped

Tier 1 direct validation succeeded as a useful mechanism signal, but the evidence is too narrow for publication readiness.

## Recommended next action

Run a bounded deepen study with at least 5 seeds, 3 random-mask replicates, 60/80/90/95% sparsity levels, and one additional CNN architecture on full MNIST and Fashion-MNIST before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-seed Multi-sparsity IMP Mask Validation on Full MNIST/Fashion-MNIST CNNs
- Success threshold: For both datasets and each tested architecture, IMP mean accuracy is within 1 percentage point of dense at 80% and 90% sparsity and exceeds matched random masks by at least 1 percentage point with non-overlapping 95% confidence intervals or an equivalent paired test.
- Stop condition: Stop as negative if the IMP advantage over matched random masks is below 1 percentage point at 80% sparsity on either dataset in two architectures, or if dense accuracy retention fails by more than 2 percentage points after extending training to a fair convergence budget.

## Evidence references

- Artifact root: `<local-path>/projects/iterative-lottery-ticket-mask-validator-on-full-mnist-fash-130243072e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
