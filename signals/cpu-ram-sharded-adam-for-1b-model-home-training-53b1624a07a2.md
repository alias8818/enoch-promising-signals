# CPU-RAM Sharded Adam for 1B Model Home Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-ram-sharded-adam-for-1b-model-home-training-53b1624a07a2`
Run ID: `cpu-ram-sharded-adam-for-1b-model-home-training-53b1624a07a2-20260525T134731009315+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7cb06f40219f

## What looked useful

Direct 1B BF16 vector benchmark: CPU-RAM sharded AdamW with 64M shards averaged 0.914 s/step, median 0.913 s, peak CUDA allocation 3.96 GiB, and MemAvailable 115.38 -> 99.64 GiB. Direct GPU fused AdamW baseline averaged 0.116 s/step, median 0.095 s, peak CUDA allocation 9.31 GiB. The offload mechanism works at 1B optimizer scale but is about 7.9x slower for optimizer work alone.

## Boundaries and scale limits

The evidence is an optimizer microbenchmark with synthetic gradients only. It does not include transformer forward/backward, activation memory, convergence, data loading, checkpoint I/O, multi-hour stability, or a real 1B model training run.

## Claim scope

On a GB10-class host, a synthetic 1B-parameter BF16 optimizer step can keep Adam FP32 moments in CPU RAM and update GPU parameters shard-by-shard, reducing optimizer CUDA allocation versus GPU-resident AdamW at the cost of a large optimizer-step slowdown.

## Why it stopped

Bounded optimizer evidence supports the memory-offload mechanism but is insufficient for a 1B home-training claim or paper-positive result because real model training and convergence were not tested.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should integrate the optimizer into a small transformer training loop and compare tokens/sec, memory, and loss against GPU AdamW at matched parameter count.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU-RAM Adam Offload in a Real Transformer Training Loop
- Success threshold: A real transformer run completes at least 100 optimizer steps with stable loss, reduces peak CUDA allocation by at least 30% versus GPU AdamW, and keeps end-to-end throughput slowdown at or below 3x for a setting where memory headroom matters.
- Stop condition: Stop if the integrated optimizer causes loss divergence, cannot complete 100 steps, or end-to-end throughput is slower than GPU AdamW by more than 5x without enabling a materially larger model or batch.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-ram-sharded-adam-for-1b-model-home-training-53b1624a07a2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
