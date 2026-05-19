# Robust Aggregation for Low-Cost Verifiable Gradient Lottery

Status: `useful_signal`
Project ID: `robust-aggregation-for-low-cost-verifiable-gradient-lotter-5aa4c01151`
Run ID: `robust-aggregation-for-low-cost-verifiable-gradient-lotter-5aa4c01151-20260518T081542775338+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/124efa13c452

## What looked useful

At 20% Byzantine and 64 audited coordinates (3.125% coordinate audit cost), lottery-gated trimmed mean improved relative L2 error versus naive mean by 1.46x to 14.60x across four attack modes and reached cosine about 0.894-0.898. Dense attacks were fully detected with 8 audited coordinates, while sparse 5% coordinate spikes required 64-128 audited coordinates for high recall. However, mean-after-lottery was better after complete dense-attack rejection, and plain trimmed mean was best for sparse spikes, so the combined robust-after-lottery policy is conditionally useful rather than uniformly dominant.

## Boundaries and scale limits

No end-to-end training convergence, neural-network gradients, adaptive attacker, cryptographic commit/reveal implementation, production verifier cost model, or distributed runtime overhead was tested.

## Claim scope

Controlled synthetic logistic-regression gradient aggregation with 31 workers, 2048-dimensional gradients, 50 trials per condition, Byzantine fractions up to 30%, and randomized coordinate audits up to 128 coordinates per worker.

## Why it stopped

Tier-1 direct synthetic gradient evidence supports the mechanism but is mixed and not paper-ready; stronger direct training-loop evidence is needed before any publication claim.

## Recommended next action

Run a bounded end-to-end SGD follow-up comparing mean-after-clean-audit, robust-after-suspect-audit, and fixed robust aggregation under adaptive sparse/dense Byzantine attacks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Training-Loop Validation for Conditional Lottery Aggregation
- Success threshold: At 20-30% Byzantine workers and <=3.125% coordinate audit cost, the conditional policy should keep final validation loss within 5% of all-honest training and improve mean gradient relative L2 by at least 2x over naive mean in every attack mode.
- Stop condition: Stop as negative if the conditional policy fails the validation-loss threshold or does not beat naive mean by 2x relative L2 in at least three of four attack modes across three random seeds.

## Evidence references

- Artifact root: `<local-path>/projects/robust-aggregation-for-low-cost-verifiable-gradient-lotter-5aa4c01151`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
