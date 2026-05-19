# Commit-Reveal Spot-Check Gradient Verification for Volunteer Training

Status: `useful_signal`
Project ID: `commit-reveal-spot-check-gradient-verification-for-volunteer-training-c7bbf4bdc595`
Run ID: `commit-reveal-spot-check-gradient-verification-for-volunteer-training-c7bbf4bdc595-20260517T161247368346+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/211406be87da

## What looked useful

512 sampled coordinates detected 1% random coordinate corruption in 99.5% of 400 trials with about 3.71 ms prototype verification and 290 KiB proof traffic, but the same sample detected only 20.5% of 100-coordinate sparse attacks and effectively missed single-coordinate attacks.

## Boundaries and scale limits

Single-machine toy MLP gradient only; no large-model volunteer training, no distributed workers, no direct per-coordinate gradient recomputation benchmark, and no evaluation of stale-gradient, collusion, poisoned-data, or semantic Byzantine attacks.

## Claim scope

Local prototype evidence shows that Merkle commit-reveal spot checks bind gradient submissions before challenge selection and detect dense coordinate corruption at rates predicted by hypergeometric sampling on a 201,377-coordinate toy PyTorch gradient.

## Why it stopped

Prototype evidence supports the bounded mechanism but also shows sparse-attack weakness; this is not a full validation of volunteer training integrity.

## Recommended next action

Stop this run as no-paper useful signal; next, test direct sampled-gradient recomputation cost and attack detection inside a small real distributed-training loop.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end sampled-gradient recomputation for volunteer spot checks
- Success threshold: At least 95% detection for 1% dense coordinate corruption and stale-gradient submissions with under 10% throughput overhead on a small training loop, while explicitly quantifying sparse-attack miss probability.
- Stop condition: Stop if sampled-coordinate recomputation requires near-full-gradient cost or exceeds 25% throughput overhead before meeting the detection threshold.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-spot-check-gradient-verification-for-volunteer-training-c7bbf4bdc595`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
