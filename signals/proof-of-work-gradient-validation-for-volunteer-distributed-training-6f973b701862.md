# Proof-of-Work Gradient Validation for Volunteer Distributed Training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `proof-of-work-gradient-validation-for-volunteer-distributed-training-6f973b701862`
Run ID: `proof-of-work-gradient-validation-for-volunteer-distributed-training-6f973b701862-20260607T071248897568+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/db5a96a6c4fc

## What looked useful

PoW reduced accepted cheap-random poisoned gradients at moderate simulated cost, but did not change the poisoned fraction for full-cost sign-flip attackers and sharply reduced accepted training updates. Locally, even a 12-bit SHA-256 puzzle cost about 108x one toy minibatch gradient, making throughput collapse the main failure mode.

## Boundaries and scale limits

Synthetic data, logistic regression, analytical acceptance simulation, local SHA-256 benchmark, no real volunteer network, no GPU training, no large-model optimizer state, no real data heterogeneity, and no multi-node wall-clock validation.

## Claim scope

Bounded local synthetic proxy evidence for logistic-regression volunteer training: PoW attached to gradients does not semantically validate gradient correctness and only helps as a rate limiter when invalid gradients are much cheaper than honest gradients.

## Why it stopped

Proxy early falsification: the run directly tested cost ratios and simulated poisoned-gradient acceptance, but did not perform full distributed-training validation. The evidence shows PoW is a rate limiter, not gradient validation.

## Recommended next action

Stop this validation-only PoW line as no-paper evidence; if continuing, run a bounded hybrid PoW plus random recomputation or robust aggregation test against the same attacker models.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid PoW and Semantic Spot-Check Gradient Defense
- Success threshold: Hybrid defense reaches at least 0.86 mean accuracy in the 25% cheap-random attacker scenario, keeps accepted poisoned fraction below 0.35, and retains at least 60% of the accepted honest updates of the undefended no-attack baseline.
- Stop condition: Stop if hybrid validation cost reduces accepted honest updates below 40% of baseline or fails to improve over semantic-check-only control in the cheap-random attacker regime.

## Evidence references

- Artifact root: `<local-path>/projects/proof-of-work-gradient-validation-for-volunteer-distributed-training-6f973b701862`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
