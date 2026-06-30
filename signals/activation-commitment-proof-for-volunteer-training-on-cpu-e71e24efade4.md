# Activation-Commitment Proof for Volunteer Training on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-commitment-proof-for-volunteer-training-on-cpu-e71e24efade4`
Run ID: `activation-commitment-proof-for-volunteer-training-on-cpu-e71e24efade4-20260529T060950940000+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8c22d69b4c8e

## What looked useful

The mechanism is locally viable for deterministic audit binding: honest sampled audits had 0 mismatches, while skip-update and corrupt-gradient traces produced 70 sampled field mismatches each. The naive full activation-commitment implementation had substantial overhead, averaging 2.08x per training step on this tiny CPU model.

## Boundaries and scale limits

Only a toy synthetic CPU task was tested: 3 seeds, 400 SGD steps per seed, batch size 128, hidden layers 64 and 32. No real volunteer network, large model, nondeterministic framework kernels, checkpoint custody protocol, privacy constraint, storage/bandwidth accounting, or sophisticated adversary was evaluated.

## Claim scope

In a deterministic NumPy CPU MLP on synthetic classification data, per-step BLAKE2b commitments to batch indices, forward activations, and post-update model parameters replay exactly for honest traces and detect sampled skipped-update or corrupted-gradient traces.

## Why it stopped

Bounded deterministic mechanism evidence is positive, but the result is proxy-only and naive full activation hashing roughly doubles tiny-model CPU step time, so it is not a deployable volunteer-training proof or paper-ready validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should reduce commitment overhead with sparse or Merkle activation commitments while preserving sampled cheat detection on a harder real dataset.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sparse Activation-Commitment Audit for CPU Volunteer Training
- Success threshold: At least 95% segment-level detection for skipped or corrupted updates with 0 honest false positives in the tested seeds, under 25% mean training-step overhead versus no commitments, and verifier replay cost below 10% of worker training cost for the audited segment.
- Stop condition: Stop if sparse commitments exceed 50% mean overhead, create any honest false positives under deterministic replay, or fail to detect more than 80% of adversarial segments at the planned audit budget.

## Evidence references

- Artifact root: `<local-path>/projects/activation-commitment-proof-for-volunteer-training-on-cpu-e71e24efade4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
