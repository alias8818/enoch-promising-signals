# Netem-shaped multi-process delta-compressed synchronization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `netem-shaped-multi-process-delta-compressed-synchronizatio-1b7cc247cd`
Run ID: `netem-shaped-multi-process-delta-compressed-synchronizatio-1b7cc247cd-20260522T123936017582+0000`

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

- Parent run decision: Network-Emulated Delta-Compressed Distributed Training: enoch://control-plane/projects/network-emulated-delta-compressed-distributed-training-76302dce52/runs/network-emulated-delta-compressed-distributed-training-76302dce52-20260522T111401428149+0000
- Parent run decision: Home Delta-Compressed Distributed: enoch://control-plane/projects/home-delta-compressed-distributed-2615551bb97b/runs/home-delta-compressed-distributed-2615551bb97b-20260522T110504893596+0000

## What looked useful

Delta encoding is the primary mechanism: delta_zlib averaged 95.11% fewer payload bytes and 16.18x faster virtual sync than full_raw, and 90.30% fewer bytes and 6.63x faster sync than full_zlib. Compression should be entropy-aware because delta_raw beat delta_zlib in the high-entropy aggregate groups.

## Boundaries and scale limits

State size was 256 KiB per worker for 20 rounds, workloads were synthetic, the network was a deterministic user-space virtual shaper rather than kernel tc/netem, and no real distributed application or failure recovery path was tested.

## Claim scope

In a fixed-seed synthetic 4-process state synchronization benchmark with deterministic virtual netem shaping, delta-first synchronization substantially reduced bytes and shaped-link sync latency versus full-state baselines across sparse-to-moderately-dense mutations. Compression helped compressible deltas but did not help high-entropy deltas.

## Why it stopped

Tier 2 evidence supports a narrowed mechanism but does not provide paper-positive direct network evidence, and the compression component is mixed rather than universally beneficial.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded step is a real socket transport under kernel tc/netem or a container network emulator using the same seeds and application-derived traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Kernel-netem socket validation for entropy-aware delta synchronization
- Success threshold: Across at least 3 fixed seeds and 2 shaped-link profiles, entropy-gated delta synchronization achieves at least 5x p95 sync-latency speedup and at least 80% byte reduction versus full_zlib on sparse application-derived traces, with no more than 5% latency regression versus delta_raw on high-entropy traces.
- Stop condition: Stop if real netem p95 speedup versus full_zlib is below 2x on sparse traces, if correctness hashes diverge, or if compression-gate overhead exceeds the latency saved by compression.

## Evidence references

- Artifact root: `<local-path>/projects/netem-shaped-multi-process-delta-compressed-synchronizatio-1b7cc247cd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
