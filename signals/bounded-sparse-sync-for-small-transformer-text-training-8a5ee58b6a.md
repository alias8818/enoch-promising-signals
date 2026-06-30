# Bounded Sparse Sync for Small-Transformer Text Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-sparse-sync-for-small-transformer-text-training-8a5ee58b6a`
Run ID: `bounded-sparse-sync-for-small-transformer-text-training-8a5ee58b6a-20260608T213343015974+0000`

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

- Parent run decision: Volunteer Distributed Training with Bounded Parameter Sync: enoch://control-plane/projects/volunteer-distributed-training-with-bounded-parameter-sync-e84677f0a7cd/runs/volunteer-distributed-training-with-bounded-parameter-sync-e84677f0a7cd-20260608T192642715729+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/69b8a2ecfe2c

## What looked useful

10% bounded sparse sync met the Tier-1 threshold in both seeds: mean final val loss 2.5335 versus dense 2.5216, mean relative degradation 0.47%, communication fraction 0.1000. 2% sparse sync failed with mean final val loss 3.2337 and 28.24% degradation, with residuals pinned at the 2.0 bound.

## Boundaries and scale limits

Small character-level model, Tiny Shakespeare only, two seeds, 300 steps, simulated workers on one GB10 GPU, coordinate-count communication metric rather than measured distributed network traffic.

## Claim scope

In a two-worker sequential GPU simulation training a 2-layer character-level causal transformer on Tiny Shakespeare for 300 steps, bounded sparse parameter-delta synchronization at 10% coordinates preserved dense-sync validation loss within about 0.5% while reducing communicated coordinates by about 90%; 2% sparsity failed.

## Why it stopped

Tier-1 direct evidence supports the mechanism at 10% sparsity but remains too small and simulated for a paper-ready claim.

## Recommended next action

Run a bounded medium direct follow-up with a larger tokenizer-level transformer, at least 4 seeds, longer training, and real multi-process or multi-node communication timing to test whether the 10% sparse-sync signal persists beyond coordinate-count savings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium tokenizer-level validation of 10% bounded sparse sync
- Success threshold: Sparse 10% final validation loss remains within 10% of dense sync and measured synchronization traffic or time is reduced by at least 50% without persistent residual-bound saturation.
- Stop condition: Stop if sparse 10% exceeds 10% validation-loss degradation in two seeds, diverges, or measured synchronization savings are below 50%.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-sparse-sync-for-small-transformer-text-training-8a5ee58b6a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
