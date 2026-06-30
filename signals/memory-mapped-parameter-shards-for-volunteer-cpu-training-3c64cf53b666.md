# Memory-mapped parameter shards for volunteer CPU training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `memory-mapped-parameter-shards-for-volunteer-cpu-training-3c64cf53b666`
Run ID: `memory-mapped-parameter-shards-for-volunteer-cpu-training-3c64cf53b666-20260604T025716027560+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/91e01e9fca96

## What looked useful

Lazy mmap grew RSS by only 4.6 MiB and ran at 0.68x RAM when touching 1% of rows, but random sparse access touched 54.2% of rows, grew RSS by 259.2 MiB, incurred 183 major faults, and ran at 0.22x RAM.

## Boundaries and scale limits

No real neural model, optimizer state, multi-worker coordination, network transfer, restart recovery, or long-running checkpoint cadence was tested. Table size was 256 MiB and runtime was seconds, not hours.

## Claim scope

Single-worker CPU microbenchmark of a 256 MiB fp32 parameter table with SGD-style row updates shows lazy mmap shards preserve memory only under hot shard-local sparse access; random or broad-sweep access loses the memory advantage and is slower than resident RAM.

## Why it stopped

Proxy systems microbenchmark supports the locality-dependent mechanism but early-falsifies mmap shards as a general drop-in volunteer CPU training solution; full validation would require real model training with optimizer state and scheduler controls.

## Recommended next action

Stop this run as no-paper useful signal; only pursue a bounded follow-up if it tests an explicitly shard-local scheduler with real optimizer state against a resident baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Shard-local optimizer scheduling for mmap-backed CPU training
- Success threshold: For at least a 4x larger-than-hot-working-set parameter table, shard-local mmap keeps peak RSS at least 2x lower than resident RAM while achieving at least 0.75x RAM throughput and matching loss trend within noise over a bounded run.
- Stop condition: Stop if shard-local scheduling still touches more than 25% of parameter pages per checkpoint window, peak RSS approaches resident RAM, or throughput remains below 0.5x RAM after basic batching/vectorization.

## Evidence references

- Artifact root: `<local-path>/projects/memory-mapped-parameter-shards-for-volunteer-cpu-training-3c64cf53b666`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
