# NVLink-C2C Optimizer Offload vs In-GPU 8-bit on Grace Blackwell

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `nvlink-c2c-optimizer-offload-vs-in-gpu-8-bit-on-grace-blackwell-8f1be0eac746`
Run ID: `nvlink-c2c-optimizer-offload-vs-in-gpu-8-bit-on-grace-blackwell-8f1be0eac746-20260621T050729497913+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/41fa2e2055c3

## What looked useful

Mapped host optimizer state is viable and near FP32-device parity on GB10 for a streaming Adam-style update, but it did not outperform compact in-GPU int8 optimizer state in the local benchmark.

## Boundaries and scale limits

Microbenchmark only; no production optimizer, no real model training, no convergence measurement, no multi-GPU or datacenter-scale memory-pressure validation. The int8 path uses fixed scales and is only a throughput and one-step-drift proxy.

## Claim scope

On this GB10 host, a CUDA Adam-style streaming update with FP32 optimizer moments in cudaHostAllocMapped memory reaches near parity with FP32 moments in cudaMalloc memory at 4M-33M parameters, but a toy in-GPU int8 moment representation is consistently faster, including 1.80x faster than mapped-host FP32 at 33M parameters.

## Why it stopped

Local proxy evidence does not support a paper claim that NVLink-C2C-style FP32 optimizer offload beats in-GPU 8-bit state; the result is an early bounded falsification of the throughput side of the hypothesis, not a full training validation.

## Recommended next action

Stop this run as a no-paper useful signal; run one bounded follow-up with a production-like 8-bit optimizer kernel and a small transformer training step under memory pressure on GB10.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production-like optimizer offload vs 8-bit optimizer in a small transformer step on GB10
- Success threshold: Offload must either match or beat 8-bit optimizer tokens/s within 10% while enabling a materially larger batch/model footprint, or produce a clear memory-capacity advantage that the 8-bit path cannot reach locally.
- Stop condition: Stop if the production-like offload path is more than 25% slower than 8-bit at the same footprint and does not enable a larger feasible batch/model, or if convergence proxies diverge materially.

## Evidence references

- Artifact root: `<local-path>/projects/nvlink-c2c-optimizer-offload-vs-in-gpu-8-bit-on-grace-blackwell-8f1be0eac746`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
