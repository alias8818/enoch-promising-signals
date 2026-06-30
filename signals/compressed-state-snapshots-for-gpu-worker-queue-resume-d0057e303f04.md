# Compressed State Snapshots for GPU Worker Queue Resume

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-state-snapshots-for-gpu-worker-queue-resume-d0057e303f04`
Run ID: `compressed-state-snapshots-for-gpu-worker-queue-resume-d0057e303f04-20260612T011356270755+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f0e02bdbdc90

## What looked useful

Compressed snapshots are correct and can reduce 64-68 MB raw state to 0.02-37.04 MB depending on entropy. For tensor-dominated quantized/random-fp16 state, codec roundtrip overhead creates break-even persistence bandwidths around 190-300 MB/s; above that, raw snapshots are likely faster unless state is highly redundant.

## Boundaries and scale limits

Synthetic single-process benchmark only; no production scheduler, object store, crash injection, distributed workers, or large model optimizer/KV-cache checkpoint validation.

## Claim scope

Local GB10 Python/PyTorch benchmark of compressed mid-queue CUDA worker snapshots with structured, mixed, quantized, zero, and random-fp16-normal synthetic state; all restored continuations matched uninterrupted controls.

## Why it stopped

No-paper closure: this run produced useful bounded synthetic evidence and thresholds, but not direct production crash-recovery or scheduler evidence.

## Recommended next action

Implement an adaptive snapshot policy that samples snapshot entropy and selects raw, lz4, or zstd1, then validate it with local crash-injection against an object-store or filesystem queue.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive compressed GPU queue snapshots under crash injection
- Success threshold: Adaptive policy matches uninterrupted correctness in all trials and is at least 10% faster than the best fixed policy in two of three entropy regimes without more than 5% regression in the third.
- Stop condition: Stop if restored digests diverge, if adaptive selection cannot beat the best fixed policy in any regime, or if recovery latency variance prevents a stable 10% effect after 30 trials per regime.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-snapshots-for-gpu-worker-queue-resume-d0057e303f04`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
