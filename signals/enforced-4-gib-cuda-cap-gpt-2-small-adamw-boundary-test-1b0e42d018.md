# Enforced 4 GiB CUDA cap GPT-2-small AdamW boundary test

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `83`
Project ID: `enforced-4-gib-cuda-cap-gpt-2-small-adamw-boundary-test-1b0e42d018`
Run ID: `enforced-4-gib-cuda-cap-gpt-2-small-adamw-boundary-test-1b0e42d018-20260519T051934241609+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Enforced 4 GiB CUDA cap GPT-2-small AdamW boundary test: internal_generated:enforced-4-gib-cuda-cap-gpt-2-small-adamw-boundary-test-1b0e42d018

## What looked useful

The 4 GiB cap is a real boundary for standard fp32-state AdamW GPT-2-small at seq1024: capped batch 2 succeeded for seeds 1-3 with mean 3.431 GiB allocated, capped direct batch 4 OOMed for seeds 1-3, uncapped batch 4 succeeded with mean 5.224 GiB allocated, and capped microbatch 2 accumulation achieved effective batch 4 with mean 3.895 GiB allocated.

## Boundaries and scale limits

Synthetic-token boundary test only; five optimizer steps per fixed-seed Tier 2 condition; no real dataset quality validation, no long-run stability test, no dataloader memory, no multi-hardware replication, and no fused or low-bit optimizer variants beyond the bf16-state ablation.

## Claim scope

On this GB10/PyTorch 2.11 CUDA 13 setup, a GPT-2-small-class 124.4M parameter model at sequence length 1024 under an enforced 4 GiB PyTorch CUDA allocator cap can run fp32-state AdamW with bf16 autocast at direct batch 2, cannot run direct batch 4, and can run effective batch 4 via microbatch 2 gradient accumulation or by switching parameters/AdamW state to bf16.

## Why it stopped

Tier 2 boundary evidence is direct and reproducible for memory feasibility, but the result is not publication-grade because it uses synthetic batches and demonstrates an expected cap boundary/workaround rather than a novel training result.

## Recommended next action

Stop as no-paper useful evidence; use the measured boundary as an engineering reference, and only reopen if the claim changes to real-data long-run stability or a specific optimizer-compression mechanism.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/enforced-4-gib-cuda-cap-gpt-2-small-adamw-boundary-test-1b0e42d018`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
