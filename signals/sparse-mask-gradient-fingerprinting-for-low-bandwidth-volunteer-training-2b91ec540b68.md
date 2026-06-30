# Sparse-Mask Gradient Fingerprinting for Low-Bandwidth Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sparse-mask-gradient-fingerprinting-for-low-bandwidth-volunteer-training-2b91ec540b68`
Run ID: `sparse-mask-gradient-fingerprinting-for-low-bandwidth-volunteer-training-2b91ec540b68-20260526T054210896845+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fcaeefd6eeab

## What looked useful

Sparse gradient coordinate support can leak persistent client identity at very low bandwidth in a controlled federated proxy. IID fixed-client data also produced strong fingerprints, suggesting finite local sample idiosyncrasies may be enough for attribution, not only label skew.

## Boundaries and scale limits

Synthetic data only; 32 clients; 48 rounds; small linear model; no real volunteer benchmark, secure aggregation, client dropout, local epochs, clipping, DP noise, or larger neural network validation.

## Claim scope

In a fixed-client synthetic federated multiclass proxy with a 970-parameter linear classifier, top-k sparse gradient coordinate masks are stable enough to re-identify clients across held-out rounds at 1-5% sparsity, with 0.790-1.000 attribution accuracy versus approximately 0.032 chance/random-mask control.

## Why it stopped

Closed as a no-paper useful synthetic signal: the mechanism is supported locally, but direct real-volunteer or benchmark evidence is still missing.

## Recommended next action

Run the same held-out-round mask-attribution protocol on a real federated benchmark with client subsampling/dropout and mitigation baselines before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-benchmark sparse gradient mask attribution under client subsampling
- Success threshold: At least 5x chance top-1 attribution accuracy at 1-5% sparsity on real benchmark clients while preserving training utility within 2 percentage points of the dense or standard sparse baseline.
- Stop condition: Stop if attribution falls below 2x chance across two real benchmark/client-partition settings or only appears when training utility collapses.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-mask-gradient-fingerprinting-for-low-bandwidth-volunteer-training-2b91ec540b68`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
