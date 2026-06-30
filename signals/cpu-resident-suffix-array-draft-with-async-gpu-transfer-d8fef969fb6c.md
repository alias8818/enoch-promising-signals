# CPU-Resident Suffix-Array Draft with Async GPU Transfer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-resident-suffix-array-draft-with-async-gpu-transfer-d8fef969fb6c`
Run ID: `cpu-resident-suffix-array-draft-with-async-gpu-transfer-d8fef969fb6c-20260602T193553561194+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/97c40ffa75b4

## What looked useful

The CPU-resident async-transfer idea is not generally viable as a streamed scan replacement for GPU-resident suffix arrays, but it may be worth a bounded follow-up for sparse/random suffix-array query workloads where irregular GPU work masks transfer overhead. Mapped zero-copy is competitive for sequential GB10 UMA scans but weaker on 256 MiB random probes.

## Boundaries and scale limits

Tested only 4-256 MiB synthetic SA-entry arrays and checksum kernels on one GB10. Did not test full suffix-array construction, real text/pattern search, CPU draft construction overlap, multi-query distributions, or larger corpora.

## Claim scope

On GB10, synthetic 32-bit suffix-array-like entries in pinned CPU memory can be streamed asynchronously to a GPU at about 43 GiB/s for 64-256 MiB sequential scans, but that is about 5x slower than a GPU-resident scan; for full-array random-permutation probe kernels, async transfer plus compute is about 1.25-1.29x slower than GPU-resident.

## Why it stopped

Synthetic/proxy benchmark supports a mixed mechanism signal but is not direct end-to-end suffix-array evidence or publication-grade validation.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded action is a real suffix-array search benchmark over generated text comparing GPU-resident, pinned async full/chunk transfer, and mapped zero-copy under identical query distributions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real suffix-array query benchmark for CPU-resident async transfer
- Success threshold: At 256 MiB or larger, CPU-resident async or zero-copy mode remains within 1.5x of GPU-resident query throughput for sparse/random real suffix-array searches while using less persistent device allocation, with all query results matching CPU reference.
- Stop condition: Stop as negative if either CPU-resident mode is more than 2x slower than GPU-resident on real sparse/random queries at 256 MiB, or if correctness diverges from CPU reference.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-resident-suffix-array-draft-with-async-gpu-transfer-d8fef969fb6c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
