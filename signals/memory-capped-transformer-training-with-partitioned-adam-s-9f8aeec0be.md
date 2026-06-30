# Memory-capped transformer training with partitioned Adam state

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `memory-capped-transformer-training-with-partitioned-adam-s-9f8aeec0be`
Run ID: `memory-capped-transformer-training-with-partitioned-adam-s-9f8aeec0be-20260612T221632113886+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Optimizer State Partitioning for Tiny VRAM: enoch://control-plane/projects/optimizer-state-partitioning-for-tiny-vram-a980e93919a1/runs/optimizer-state-partitioning-for-tiny-vram-a980e93919a1-20260612T215600756260+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/8016a2027f8b

## What looked useful

Partitioned AdamW state is a real memory-capping mechanism in direct CUDA transformer training: peak allocation fell from 890,950,144 to 554,398,720 bytes and persistent GPU optimizer state fell from 336,289,792 bytes to 0, at a throughput ratio of 0.390x baseline.

## Boundaries and scale limits

Synthetic data only; 16 training steps; one model shape; naive synchronous CPU-GPU state copies; no GPT-2-small-class baseline, real corpus, long convergence, distributed training, activation checkpointing, or partition-size ablation.

## Claim scope

On a small direct GB10 CUDA transformer LM test with 84.1M parameters, CPU-resident partitioned AdamW removed persistent GPU optimizer state and reduced peak CUDA allocation by 37.77% versus PyTorch AdamW, while preserving short-run loss behavior.

## Why it stopped

Tier 1 direct evidence supports the memory mechanism, but the current naive implementation is a short synthetic run and is too slow for a paper-ready practical claim.

## Recommended next action

Run a bounded deepen follow-up that sweeps partition size and pinned/asynchronous CPU-state transfer on this same 84M-parameter transformer, requiring at least 30% peak CUDA memory reduction with at least 0.70x baseline throughput over 100 real-data steps.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Partition-size and pinned-transfer sweep for CPU-state AdamW on an 84M-parameter transformer
- Success threshold: At least 30% lower peak CUDA allocation than baseline AdamW, 0 persistent GPU optimizer-state bytes after step, throughput at least 0.70x baseline, and final loss within 2% of baseline after 100 matched steps.
- Stop condition: Stop if every tested partition/transfer setting remains below 0.50x baseline throughput or if the loss trajectory diverges by more than 5% from baseline while preserving the memory cap.

## Evidence references

- Artifact root: `<local-path>/projects/memory-capped-transformer-training-with-partitioned-adam-s-9f8aeec0be`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
