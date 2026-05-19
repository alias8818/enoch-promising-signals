# Sparse Activation Replay for Byzantine Volunteer Gradient Verification

Status: `useful_signal`
Project ID: `sparse-activation-replay-for-byzantine-volunteer-gradient-verification-764c8c457dca`
Run ID: `sparse-activation-replay-for-byzantine-volunteer-gradient-verification-764c8c457dca-20260517T175834714268+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2d019a3fa381

## What looked useful

Sparse replay is a plausible verifier component for broad or random corruptions, but it is not sufficient alone at low hidden-unit sampling rates against structured neuron-aligned Byzantine gradients; activation-weighted sampling is especially weak for low-activation targeted corruption.

## Boundaries and scale limits

Tested only a synthetic batch and single-step gradient verification on a 64x256x10 MLP; no real volunteer execution, cryptographic commitment protocol, multi-step training, adaptive adversary, transformer model, or distributed system was validated.

## Claim scope

Local proxy evidence on a deterministic one-hidden-layer ReLU MLP shows sparse activation replay detects dense, sign-flip, and random 1% scalar gradient corruption, but low-budget hidden-unit replay has only sampling-coverage-level detection against structured 5% hidden-neuron corruption.

## Why it stopped

Proxy evidence is mixed: useful detection signal exists, but structured attacks expose a coverage weakness and the run is not a full validation.

## Recommended next action

Run a bounded direct volunteer-training simulation with adaptive structured Byzantine workers and equal-cost baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Equal-cost adaptive verifier test for sparse activation replay
- Success threshold: At matched verification cost, the combined verifier detects at least 95% of structured Byzantine updates or keeps final validation loss within 5% of an all-honest baseline across at least three seeds.
- Stop condition: Stop if sparse replay plus an orthogonal check fails to outperform equal-cost random coordinate checking or robust aggregation on structured adaptive attacks.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-activation-replay-for-byzantine-volunteer-gradient-verification-764c8c457dca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
