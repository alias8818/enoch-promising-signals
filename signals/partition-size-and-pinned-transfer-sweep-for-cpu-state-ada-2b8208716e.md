# Partition-size and pinned-transfer sweep for CPU-state AdamW on an 84M-parameter transformer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `partition-size-and-pinned-transfer-sweep-for-cpu-state-ada-2b8208716e`
Run ID: `partition-size-and-pinned-transfer-sweep-for-cpu-state-ada-2b8208716e-20260612T223757853775+0000`

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

- Parent run decision: Optimizer State Partitioning for Tiny VRAM: enoch://control-plane/projects/optimizer-state-partitioning-for-tiny-vram-a980e93919a1/runs/optimizer-state-partitioning-for-tiny-vram-a980e93919a1-20260612T215600756260+0000
- Parent run decision: Memory-capped transformer training with partitioned Adam state: enoch://control-plane/projects/memory-capped-transformer-training-with-partitioned-adam-s-9f8aeec0be/runs/memory-capped-transformer-training-with-partitioned-adam-s-9f8aeec0be-20260612T221632113886+0000

## What looked useful

Pinned CPU buffers and partition size changed CPU-state AdamW optimizer time by up to about 18% in the confirmation sweep, with 16 MiB pinned best among tested CPU-state settings. However, best CPU-state AdamW was 1.73x slower per step and 2.04x slower in optimizer time than the GPU AdamW baseline.

## Boundaries and scale limits

Single host, one 84M-class model shape, synthetic fixed-token batches, short fixed-seed throughput runs, straightforward non-overlapped flattened CPU-state AdamW implementation; no real-corpus convergence or production fused optimizer.

## Claim scope

On a single GB10 worker using PyTorch 2.12/CUDA 13, an 84,167,424-parameter GPT-style transformer with synthetic fixed batches showed measurable partition-size and pinned-buffer effects for CPU-state AdamW, but the best tested CPU-state setting remained slower than GPU AdamW.

## Why it stopped

Tier 2 fixed-seed direct target benchmark with a real GPU AdamW baseline did not support a paper-ready speed result; the result is a useful mechanism signal rather than full validation.

## Recommended next action

Stop this branch as no-paper evidence; a bounded follow-up should test double-buffered overlapped pinned transfers plus a fused CPU update before any larger training claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Double-buffered overlapped pinned CPU-state AdamW for 84M transformer steps
- Success threshold: The overlapped CPU-state optimizer reduces median optimizer time by at least 30% versus the synchronous pinned CPU-state baseline and reaches within 1.5x of GPU AdamW optimizer time on the same host.
- Stop condition: Stop if the overlapped implementation cannot reduce optimizer time by at least 15% in a smoke plus 3-seed confirmation, or if correctness/loss parity fails.

## Evidence references

- Artifact root: `<local-path>/projects/partition-size-and-pinned-transfer-sweep-for-cpu-state-ada-2b8208716e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
