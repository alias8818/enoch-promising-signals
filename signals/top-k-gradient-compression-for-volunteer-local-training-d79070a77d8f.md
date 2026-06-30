# Top-k Gradient Compression for Volunteer Local Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `top-k-gradient-compression-for-volunteer-local-training-d79070a77d8f`
Run ID: `top-k-gradient-compression-for-volunteer-local-training-d79070a77d8f-20260607T203515227595+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b929845421d7

## What looked useful

Moderate sparsity plus error feedback was stable in the proxy: 10% top-k EF averaged 0.6317 accuracy vs dense 0.6337 at 20.1% bytes, and 5% top-k EF averaged 0.6278 at 10.2% bytes. 1% top-k EF and 10% top-k without error feedback failed the all-seed threshold.

## Boundaries and scale limits

This run did not test real volunteer devices, real network transport, large neural models, privacy/secure aggregation, optimizer state beyond FedSGD, or wall-clock distributed throughput. It is a bounded mechanism probe, not full validation.

## Claim scope

In a deterministic NumPy federated logistic-regression simulator with non-IID clients and stochastic volunteer availability, 5% to 10% top-k gradient compression with error feedback preserved dense-baseline accuracy within 2 absolute accuracy points across 5 seeds while using about 10% to 20% of dense transmitted gradient bytes.

## Why it stopped

Closed as no-paper useful signal: the evidence is a simulator-backed mechanism result, not direct/full validation on real volunteer local training.

## Recommended next action

Run a bounded real-model follow-up on a small CNN or tiny transformer with non-IID client partitions, comparing dense FedAvg/FedSGD against 5% and 10% top-k with error feedback on convergence-per-byte and wall-clock metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model validation of 5%-10% top-k error-feedback compression for non-IID local training
- Success threshold: Both 5% and 10% top-k with error feedback finish within 2 absolute accuracy points of dense in at least 3 seeds while using no more than 25% of dense transmitted bytes; at least one variant must reduce wall-clock or estimated network time under a realistic bandwidth model.
- Stop condition: Stop as negative if 10% top-k with error feedback misses the 2-point accuracy threshold in 2 or more seeds, or if compression overhead eliminates any communication-time benefit under the bandwidth model.

## Evidence references

- Artifact root: `<local-path>/projects/top-k-gradient-compression-for-volunteer-local-training-d79070a77d8f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
