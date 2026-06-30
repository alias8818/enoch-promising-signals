# 1.58-bit Ternary Draft Model in CPU RAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-58-bit-ternary-draft-model-in-cpu-ram-b435e17841df`
Run ID: `1-58-bit-ternary-draft-model-in-cpu-ram-b435e17841df-20260529T010914188389+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f12390d6958e

## What looked useful

Largest tested shape 16384x8192 used 25.6 MiB for 1.6-bit base3 ternary versus 512 MiB FP32 and 128 MiB int8, but base3 ternary reached only 738.9 Mweights/s, 0.155x dense int8 throughput. Across larger shapes, base3 ternary was 0.155x-0.256x int8 and 0.146x-0.371x FP32.

## Boundaries and scale limits

Synthetic GEMV only; no trained language model, no speculative decoding acceptance-rate measurement, no end-to-end target-model verification, and no hand-optimized SIMD/AMX/VNNI ternary kernel.

## Claim scope

On this CPU worker, packed 2-bit and 1.6-bit ternary GEMV gives the expected RAM compression for synthetic decoding-shaped matrices, but a straightforward scalar unpacking CPU path is substantially slower than dense int8 and FP32 baselines.

## Why it stopped

Proxy early falsification, not full validation: memory compression was confirmed, but straightforward packed ternary CPU GEMV was far below int8 throughput on out-of-cache synthetic decoding-shaped matrices.

## Recommended next action

Stop this run as a proxy early falsification of the simple CPU-RAM packed-ternary draft-model claim; a bounded follow-up should test a specialized SIMD bitplane/LUT ternary GEMV against dense int8.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: SIMD bitplane ternary GEMV for CPU-RAM draft models
- Success threshold: For 16384x8192 and at least one other out-of-cache shape, packed ternary throughput is >=0.8x dense int8 throughput while storage remains <=0.25 bytes/weight.
- Stop condition: Stop as negative if the optimized packed ternary kernel remains below 0.5x dense int8 throughput on 16384x8192 or requires unpacking to >=1 byte/weight.

## Evidence references

- Artifact root: `<local-path>/projects/1-58-bit-ternary-draft-model-in-cpu-ram-b435e17841df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
