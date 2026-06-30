# Bounded Work-Stealing Queue for GPU Worker Saturation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `bounded-work-stealing-queue-for-gpu-worker-saturation-b71e0dd51e17`
Run ID: `bounded-work-stealing-queue-for-gpu-worker-saturation-b71e0dd51e17-20260605T013444379161+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/eb58a872501e

## What looked useful

The bounded owner-queue stealing mechanism processed the same task set as controls but achieved only 0.24x-0.40x static throughput and 0.27x-0.36x global atomic-one throughput across random, sorted, hotspot, and chunk-sensitivity runs. Chunked global atomic scheduling was the strongest simple baseline.

## Boundaries and scale limits

Synthetic/proxy workload only; no real application trace, persistent production runtime, cooperative-groups deque, multi-kernel pipeline, model-training workload, or datacenter-scale validation. The owner queues are preloaded immutable task lists with atomic heads, not fully concurrent deques.

## Claim scope

On NVIDIA GB10, for a synthetic block-level irregular-task CUDA microbenchmark with 65,536 tasks, 512 blocks, and repeated medians, the implemented bounded owner-queue stealing scheduler reduces block-cycle imbalance but does not improve throughput versus static scheduling or chunked global atomic scheduling.

## Why it stopped

Proxy-scale early falsification: the directly tested bounded owner-queue stealing scheduler lowered imbalance but lost substantial throughput to probing and atomic overhead, so it is not paper-ready and not viable as implemented.

## Recommended next action

Stop this branch as no-paper useful-signal evidence; any follow-up must implement a lower-overhead persistent/shared-memory stealing design and beat global_atomic_chunk on direct throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Persistent shared-memory GPU work stealing versus chunked global atomic baseline
- Success threshold: Median work_per_s at least 1.10x global_atomic_chunk on two irregular patterns or one real trace while keeping checksum parity and p95/mean worker time no worse than 1.10.
- Stop condition: Stop if the lower-overhead scheduler remains below 0.95x global_atomic_chunk after chunk/probe tuning or if correctness diverges under repeated checksums.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-work-stealing-queue-for-gpu-worker-saturation-b71e0dd51e17`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
