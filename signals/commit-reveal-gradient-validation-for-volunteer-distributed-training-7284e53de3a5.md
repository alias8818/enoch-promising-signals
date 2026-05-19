# Commit-Reveal Gradient Validation for Volunteer Distributed Training

Status: `useful_signal`
Project ID: `commit-reveal-gradient-validation-for-volunteer-distributed-training-7284e53de3a5`
Run ID: `commit-reveal-gradient-validation-for-volunteer-distributed-training-7284e53de3a5-20260518T123745314536+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/bad98d7e7975

## What looked useful

Commit-reveal is useful as an ordering/binding primitive, not as a standalone gradient validator. In the main run, adaptive cancellation kept reveal-only at loss 0.6931 and accuracy 0.1228, while commit-only reached loss 0.2323 and accuracy 0.9036. Precommitted sign-flips destroyed commit-only training with loss 33.5833 and accuracy 0.1095. Commit plus redundant validation recovered sign-flip training to loss 0.3730 and accuracy 0.8577 at default coverage, and a validation-budget ablation recovered near-honest performance around loss 0.232 and accuracy 0.901 at high coverage.

## Boundaries and scale limits

Evidence is limited to synthetic logistic regression, controlled attack models, local execution, and deterministic same-shard recomputation. It does not test neural networks, non-IID volunteer data, real network timing, Sybil/economic incentives, privacy-preserving aggregation, or production distributed-training overhead.

## Claim scope

In a deterministic synthetic logistic-regression simulation with 20 volunteers and 30% malicious workers, commit-reveal prevents post-reveal adaptive cancellation but does not validate precommitted bad gradients; redundant same-shard recomputation can reject clear sign-flip gradients when validation coverage is high enough.

## Why it stopped

No-paper closure: this local synthetic run supports a useful mechanism distinction but also falsifies the stronger idea that commit-reveal alone validates volunteer gradients.

## Recommended next action

Run a bounded deepen follow-up using a small neural network, non-IID shards, commit withholding/timeouts, and robust aggregation baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commit-Reveal Gradient Validation Under Non-IID Neural Volunteer Training
- Success threshold: Across at least 5 seeds, commit-validate must match or beat robust aggregation on final validation loss/accuracy under adaptive and sign-flip attacks with false rejects below 2% and measured overhead below 2x honest reveal-only training.
- Stop condition: Stop as a negative result if commit-validate fails to improve over robust aggregation or requires near-full redundant recomputation to remain stable.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-gradient-validation-for-volunteer-distributed-training-7284e53de3a5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
