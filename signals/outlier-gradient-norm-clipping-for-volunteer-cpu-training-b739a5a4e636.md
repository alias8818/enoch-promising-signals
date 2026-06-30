# Outlier Gradient Norm Clipping for Volunteer CPU Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `outlier-gradient-norm-clipping-for-volunteer-cpu-training-b739a5a4e636`
Run ID: `outlier-gradient-norm-clipping-for-volunteer-cpu-training-b739a5a4e636-20260524T070113585375+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/27bbaca74165

## What looked useful

Robust norm-outlier clipping is useful when high gradient norms correlate with corrupted volunteers, but norm-only detection has a clear failure mode on honest rare high-norm clients. Medium run: corrupted/outlier_clip vs none improved val loss by -0.2126, val accuracy by +0.0704, and clean-aggregate cosine by +0.2267 mean over 12 seeds; rare_honest/outlier_clip clipped 5,929 honest/rare updates and worsened loss by +0.00037 mean with near unchanged accuracy.

## Boundaries and scale limits

Proxy-only convex synthetic workload; no real neural network, no real volunteer hardware heterogeneity, no asynchronous/stale updates, no real non-IID corpus, and no long/full-scale training. Results are useful mechanism evidence but not publication-grade validation for volunteer CPU training.

## Claim scope

In a dependency-free synthetic volunteer/federated logistic-regression simulation with 25% high-norm corrupted clients, per-round median/MAD norm-outlier clipping improved validation loss, accuracy, and aggregate-gradient alignment versus no clipping across 12/12 seeds; in a matched rare-honest high-norm scenario it clipped many honest rare updates and slightly worsened loss/alignment.

## Why it stopped

No-paper closure: this is moderate synthetic/proxy evidence with a mixed mechanism result, not direct publication-grade evidence for volunteer CPU training.

## Recommended next action

Run a bounded deepen follow-up on a tiny real neural workload with injected bad workers and honest rare shards, comparing norm-only outlier clipping against per-layer clipping and a loss-consistency filter.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny neural volunteer clipping with bad-worker and rare-shard controls
- Success threshold: Across at least 8 seeds, an augmented clipping method improves corrupted-worker validation loss by at least 5% versus no clipping while keeping honest rare-shard validation loss within 1% of no clipping and reducing honest rare clip rate by at least 50% versus norm-only outlier clipping.
- Stop condition: Stop if norm-only and augmented clipping both suppress honest rare shards enough to worsen rare-shard loss by more than 1% without a compensating corrupted-worker gain of at least 5%.

## Evidence references

- Artifact root: `<local-path>/projects/outlier-gradient-norm-clipping-for-volunteer-cpu-training-b739a5a4e636`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
