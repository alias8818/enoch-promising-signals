# CPU-Offloaded 8-bit Optimizer with Gradient Bucketing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-offloaded-8-bit-optimizer-with-gradient-bucketing-da1fa695201a`
Run ID: `cpu-offloaded-8-bit-optimizer-with-gradient-bucketing-da1fa695201a-20260524T172851006534+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7fced0aef310

## What looked useful

Memory savings are real in the proxy implementation, but CPU quantize/dequantize and rescaling passes dominate update time. Bucketing removes scale metadata overhead but did not improve throughput at fixed 8.39M-parameter scale across 64, 256, and 4096 element tensor granularities.

## Boundaries and scale limits

No GPU, no PCIe/NVLink transfer, no asynchronous overlap, no real model training loss, and no fused/vectorized production optimizer kernel were tested. Evidence is limited to single-process CPU C++ microbenchmarks with deterministic synthetic gradients.

## Claim scope

On a CPU-only synthetic optimizer-step benchmark with 8.39M parameters, 8-bit Adam moment state reduces optimizer-state memory by about 4x but is about 2.1x-2.5x slower than fp32 Adam; larger gradient/update buckets do not improve throughput versus per-tensor 8-bit updates.

## Why it stopped

Proxy CPU-only falsification of the bucketing-performance mechanism: 8-bit state saved memory, but bucketed CPU updates remained slower than fp32 and did not beat per-tensor 8-bit updates consistently.

## Recommended next action

Stop this run as a no-paper useful negative signal; only revisit with a GPU-integrated prototype that measures overlapped gradient copy, CPU update, and end-to-end training throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPU-overlapped bucketed 8-bit CPU optimizer prototype
- Success threshold: At least 3x optimizer-state GPU memory reduction with <=10% end-to-end throughput regression and no material loss divergence over a bounded real training run.
- Stop condition: Stop if CPU update plus transfer overhead remains visible on the critical path with >25% throughput regression after basic overlap and bucket-size tuning.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-8-bit-optimizer-with-gradient-bucketing-da1fa695201a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
