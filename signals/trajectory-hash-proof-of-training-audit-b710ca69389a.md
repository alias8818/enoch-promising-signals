# Trajectory Hash Proof-of-Training Audit

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trajectory-hash-proof-of-training-audit-b710ca69389a`
Run ID: `trajectory-hash-proof-of-training-audit-b710ca69389a-20260525T184201071244+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/01c5be3baed4

## What looked useful

Full replay matched the honest final hash and rejected 1% label-flip and 1% learning-rate tampering. Sparse audit over 20 intervals detected single-boundary tampering only 6.7% with 1 sampled interval, 45.0% with 5 sampled intervals, 68.3% with 10 sampled intervals, and 100% only when all 20 intervals were sampled.

## Boundaries and scale limits

Tested only a 64-feature logistic model on synthetic data for 5000 CPU steps with deterministic NumPy arithmetic. It did not test large neural networks, GPU nondeterminism, distributed training, privacy constraints, online time-binding, public commitments, or adaptive adversaries.

## Claim scope

Toy deterministic NumPy logistic-regression training shows trajectory hashes can verify full replay of a declared training run and detect changed data or optimizer settings, while sparse sampled-interval replay has miss probability proportional to unaudited intervals.

## Why it stopped

Proxy/toy evidence supports audit mechanics but not a full proof-of-training claim; sparse verification leaves clear localized-tamper miss probability unless coverage is high.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should add an online or externally timestamped commitment layer and evaluate sampled challenge verification on a small neural network.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Timestamped Challenge Commitments for Sparse Trajectory-Hash Audits
- Success threshold: For at least a small MLP training task, honest runs verify reproducibly, post-hoc fabricated or modified trajectories fail under committed challenges, and sparse audit detection matches a predeclared probability model with verifier cost below 25% of full replay for the chosen challenge budget.
- Stop condition: Stop if timestamped commitments cannot prevent post-hoc fabrication in the toy protocol, if deterministic replay cannot be achieved for the selected model, or if sparse verification cost approaches full replay while still missing localized tampering.

## Evidence references

- Artifact root: `<local-path>/projects/trajectory-hash-proof-of-training-audit-b710ca69389a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
