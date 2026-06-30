# Volunteer Distributed Training with Bounded Parameter Sync

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `volunteer-distributed-training-with-bounded-parameter-sync-e84677f0a7cd`
Run ID: `volunteer-distributed-training-with-bounded-parameter-sync-e84677f0a7cd-20260608T192642715729+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/69b8a2ecfe2c

## What looked useful

Bounded top-magnitude delta sync with residual feedback matched full synchronization in the tested proxy while enforcing residual ratios near 0.20 or 0.10 and reducing communication. Ultra-sparse 2% controls saved more bytes but carried or discarded much larger update mass and showed worse loss in the stress probe.

## Boundaries and scale limits

Synthetic classification proxy only; no real volunteer network, no transformer or GPT-2-small-class language-model training, no WAN latency/bandwidth measurement, no optimizer-state sharding, no fault/security/adversarial validation.

## Claim scope

In a local CUDA PyTorch simulation with a small MLP, synthetic non-IID worker shards, intermittent participation, and sparse delta synchronization with residual/error feedback, bounded residual sync preserved full-sync final accuracy/loss while reducing observed communication by about 50-67%.

## Why it stopped

The result is a synthetic proxy mechanism validation, not direct/full evidence for volunteer distributed language-model training.

## Recommended next action

Stop this run as no-paper useful signal; deepen with a bounded small-transformer text-corpus experiment comparing full sync, bounded residual sync, fixed sparse error-feedback sync, and fixed sparse no-feedback sync on perplexity per communicated byte.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded Sparse Sync for Small-Transformer Text Training
- Success threshold: Bounded sync reaches validation perplexity within 2% of full sync while reducing communicated bytes by at least 40%, with residual ratios staying at configured bounds and no instability across seeds.
- Stop condition: Stop as negative if bounded sync fails to reach within 5% of full-sync perplexity at comparable training budget or if communication savings fall below 25% after enforcing the residual bound.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-distributed-training-with-bounded-parameter-sync-e84677f0a7cd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
