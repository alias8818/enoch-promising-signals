# Bounded CPU-only ZeRO-style optimizer state sharding for tiny GPT-2-class training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-cpu-only-zero-style-optimizer-state-sharding-for-tiny-gpt-2-class-training-e53a60ef20d3`
Run ID: `bounded-cpu-only-zero-style-optimizer-state-sharding-for-tiny-gpt-2-class-training-e53a60ef20d3-20260620T061622238735+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a4517dea9a45

## What looked useful

The bounded control confirms the core ZeRO-1 optimizer-state mechanism for AdamW: state is per-parameter, so sharding parameter ownership across optimizers can preserve updates exactly while lowering the largest local optimizer-state shard to about one quarter of baseline in this setup. Process RSS did not improve in single-process simulation.

## Boundaries and scale limits

This run used synthetic data, 1.06M parameters, 25 training steps, and a single process. It did not test multi-process collectives, rank-local RSS isolation, parameter broadcast/all-gather costs, sharded checkpoint restart, real corpora, GPT-2-small scale, or convergence over long training.

## Claim scope

On a CPU-only single-process tiny GPT-2-style causal transformer, partitioning AdamW parameters across four disjoint optimizer shards preserved the exact loss trace and final parameter hash while reducing the maximum local optimizer-state tensor bytes by 74.59% versus a single AdamW optimizer.

## Why it stopped

No-paper closure: useful bounded mechanism evidence was produced, but the experiment is a single-process proxy and not a full distributed training validation.

## Recommended next action

Run a bounded multi-process CPU follow-up with separate rank processes, explicit parameter synchronization after shard-local AdamW updates, and rank-local RSS measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-process CPU ZeRO-1 rank-local RSS validation for tiny GPT training
- Success threshold: For a 1M-10M parameter GPT-style CPU model over at least 100 steps, max rank-local optimizer-state bytes are reduced by at least 60%, loss trace max absolute delta is below 1e-6 or parameter delta is explained by deterministic communication order, and synchronization overhead is below 2x baseline wall time.
- Stop condition: Stop if multi-process synchronization cannot preserve training within tolerance after debugging deterministic ordering, or if rank-local RSS reduction is below 40% despite correct state sharding.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-cpu-only-zero-style-optimizer-state-sharding-for-tiny-gpt-2-class-training-e53a60ef20d3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
