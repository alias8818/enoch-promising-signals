# Gradient-Norm Verification for Volunteer Training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `gradient-norm-verification-for-volunteer-training-e283cd851f4b`
Run ID: `gradient-norm-verification-for-volunteer-training-e283cd851f4b-20260602T182700771533+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b67010670af1

## What looked useful

Same-norm sign-flipped gradients passed the norm verifier and reversed training direction. In IID shards, 50% sign-flip attackers had 100% malicious acceptance and dropped test accuracy from 0.942 to 0.419; 75% attackers dropped accuracy to 0.079. In non-IID shards, the same norm envelope accepted only 0.412 of honest updates and still allowed destructive sign-flip attacks.

## Boundaries and scale limits

The result is synthetic and small-model only. It does not test large neural networks, real volunteer hardware, network behavior, cryptographic protocols, or verifiers that combine norm checks with direction, loss-improvement, redundancy, or robust aggregation.

## Claim scope

In a deterministic small federated logistic-regression simulation with 10 clients, 160 rounds, 8 seeds, IID and non-IID shards, and a 20% L2-norm acceptance envelope, norm-only gradient verification failed to reliably distinguish useful volunteer updates from same-norm harmful updates.

## Why it stopped

Bounded early falsification: a scalar norm check cannot bind gradient direction, and the local simulations show both accepted same-norm harmful updates and false rejection of honest heterogeneous updates.

## Recommended next action

Stop pursuing standalone gradient-norm verification; any next protocol should add directional, loss-improvement, redundant recomputation, or robust aggregation checks before larger training experiments.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-verification-for-volunteer-training-e283cd851f4b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
