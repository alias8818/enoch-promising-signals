# PoW-Staked Gradient Updates

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `pow-staked-gradient-updates-a53f868501f2`
Run ID: `pow-staked-gradient-updates-a53f868501f2-20260525T145841431028+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4c49dab1e186

## What looked useful

PoW/stake weighting is useful as a scarce-resource Sybil cap, not as a standalone robust gradient aggregator. The decisive boundary is attacker total work share: low attacker work preserves honest updates even with many attacker identities; equal or higher attacker work makes the weighted aggregate point opposite the honest gradient.

## Boundaries and scale limits

Synthetic convex task only: 40 clients, 96 examples per client, 30 dimensions, 8 seeds, 120 rounds. No real PoW verification, networking, cryptoeconomic behavior, nonconvex neural model, GPT-scale training, adaptive attacker, clipping, slashing, or production federated data was tested.

## Claim scope

In a synthetic federated logistic-regression simulation with coherent Byzantine gradients, PoW/stake-weighted averaging suppresses Sybil amplification when attacker total work is capped at 0.1x honest total work, but fails catastrophically when attacker work/stake reaches parity or higher.

## Why it stopped

Bounded synthetic evidence gives an early no-paper falsification of PoW/stake weighting as a standalone robust-gradient method, while preserving a useful scoped signal for Sybil-budget resistance.

## Recommended next action

Stop this standalone claim; the bounded next action is to test PoW/stake weighting combined with gradient clipping or a robust aggregator on a small neural/federated benchmark and require robustness to equal-budget attackers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PoW-Staked Clipped Robust Aggregation on Small Neural Federated Benchmarks
- Success threshold: A combined PoW/stake plus clipping/robust aggregation variant should stay within 5 accuracy points of the honest baseline and keep mean update cosine positive at 30% attacker identities with 1.0x attacker/honest work budget, while outperforming either PoW weighting or robust aggregation alone.
- Stop condition: Stop if equal-budget attackers still drive negative update cosine for more than 25% of rounds or cause more than a 10 point accuracy drop versus the honest baseline across at least 3 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/pow-staked-gradient-updates-a53f868501f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
