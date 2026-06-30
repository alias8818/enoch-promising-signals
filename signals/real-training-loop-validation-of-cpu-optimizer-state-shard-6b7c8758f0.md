# Real training-loop validation of CPU optimizer-state sharding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-training-loop-validation-of-cpu-optimizer-state-shard-6b7c8758f0`
Run ID: `real-training-loop-validation-of-cpu-optimizer-state-shard-6b7c8758f0-20260610T212937348620+0000`

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

- Parent run decision: ZeRO-style Partitioning for CPU RAM Reduction via Sharded Optimizer States: enoch://control-plane/projects/zero-style-partitioning-for-cpu-ram-reduction-via-sharded-optimizer-states-0a89d933caec/runs/zero-style-partitioning-for-cpu-ram-reduction-via-sharded-optimizer-states-0a89d933caec-20260610T134951972464+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7ed7bd294395

## What looked useful

CPU optimizer-state sharding is correctness-preserving in this direct small training loop, with 0.0 loss and sampled-weight drift versus dense Adam. It saved 183.07 MiB RSS at initialization but only 0.39 MiB by final RSS after random sparse updates, and was 1.30x slower.

## Boundaries and scale limits

Single-process CPU worker; 1.5M rows x 16 dim embedding table; 120 training steps; synthetic labels; no GPU, distributed training, checkpoint restart, LLM-scale model, asynchronous prefetch, explicit page eviction, or shard-local batch scheduling.

## Claim scope

In a controlled NumPy sparse embedding-bag training loop, sharded memmapped CPU Adam state exactly matched dense Adam training behavior but did not preserve a final RSS memory advantage under random sparse access.

## Why it stopped

Tier 1 direct training-loop validation found exact optimizer correctness parity but early-falsified the persistent memory-saving claim for simple memmapped sharding under random sparse access; this is not a full-scale validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should add explicit mmap page eviction or an LRU shard cache and require at least 25% final RSS reduction while preserving Adam parity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evicting CPU optimizer-state shards during sparse Adam training
- Success threshold: Final RSS at least 25% below dense Adam, final eval loss absolute difference <= 1e-7, sampled weight max absolute difference <= 1e-7, and sharded slowdown <= 2.0x on the controlled workload.
- Stop condition: Stop if explicit eviction/cache policy cannot keep final RSS at least 25% below dense Adam or if correctness parity fails on identical batches.

## Evidence references

- Artifact root: `<local-path>/projects/real-training-loop-validation-of-cpu-optimizer-state-shard-6b7c8758f0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
