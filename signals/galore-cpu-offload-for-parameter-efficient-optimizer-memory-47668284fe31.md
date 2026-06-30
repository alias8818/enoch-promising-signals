# GaLore CPU-Offload for Parameter-Efficient Optimizer Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `galore-cpu-offload-for-parameter-efficient-optimizer-memory-47668284fe31`
Run ID: `galore-cpu-offload-for-parameter-efficient-optimizer-memory-47668284fe31-20260521T215754324217+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/0d8a4806b8d2

## What looked useful

GaLore-style low-rank optimizer state reduced optimizer-state bytes by 128x to 256x in tested rank/shape settings, and CPU offload can make device optimizer-state bytes zero. However, dense gradient/update transfer bytes remain the same as Adam CPU offload, and naive host-side projection/reconstruction was 3.36x slower than dense Adam at 2048x2048 rank 8 and 6.10x slower at 4096x4096 rank 16.

## Boundaries and scale limits

No GPU was available, so GPU memory, PCIe/NVLink/UMA latency, overlap with backward compute, and real transformer convergence were not directly tested. The GaLore implementation is a naive host-side projection/reconstruction microbenchmark, not a fused production kernel.

## Claim scope

CPU-only microbenchmark and exact tensor byte accounting for dense Adam, Adam CPU-offload proxy, GaLore-style low-rank optimizer state, and GaLore CPU-offload proxy on synthetic matrix gradients up to 4096x4096.

## Why it stopped

No-paper useful signal: memory mechanism is supported, but the practical systems claim is not validated because this run is a CPU proxy and the naive projected update is too slow at larger matrix sizes.

## Recommended next action

Stop this CPU-only run; the next concrete test is a bounded GPU implementation that measures peak device memory, tokens/sec, transfer utilization, and loss against Adam CPU offload and GaLore resident controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded GPU validation of GaLore CPU-offload transfer and throughput
- Success threshold: At least 2x lower total optimizer-state memory than Adam CPU offload host state, zero or near-zero device optimizer state, and no more than 20% throughput loss versus Adam CPU offload while matching short-run loss trend.
- Stop condition: Stop if GaLore CPU offload is more than 50% slower than Adam CPU offload after basic overlap/fusion, or if loss diverges relative to the dense Adam control at practical ranks.

## Evidence references

- Artifact root: `<local-path>/projects/galore-cpu-offload-for-parameter-efficient-optimizer-memory-47668284fe31`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
