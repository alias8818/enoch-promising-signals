# Gradient Checkpointing with Chunked Forward: 4GB VRAM Training

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `gradient-checkpointing-with-chunked-forward-4gb-vram-training-f00d7d2095eb`
Run ID: `gradient-checkpointing-with-chunked-forward-4gb-vram-training-f00d7d2095eb-20260613T193122031935+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5d0558a2f703

## What looked useful

Checkpointing reduced batch-2 peak allocation from 3.150 GiB to 2.698 GiB and shifted batch-4 from OOM to fit. Chunking alone still OOMed at batch 4, and checkpoint+chunking had the same 3.239 GiB peak allocation as checkpoint-only while lowering throughput at smaller chunk sizes.

## Boundaries and scale limits

Synthetic data, 1-3 optimizer steps, allocator-cap proxy rather than physical 4 GB GPU, single GPT-style model shape, fp32 AdamW optimizer state, no convergence or real-corpus validation.

## Claim scope

Under a PyTorch CUDA allocator cap approximating 4 GiB on GB10, block-level activation checkpointing enabled a 135M-parameter GPT-style synthetic bf16 training step at batch 4 where the standard and chunked-only variants OOMed. Naive MLP chunked-forward did not reduce peak allocated memory beyond checkpointing in this setup.

## Why it stopped

Bounded proxy evidence supports checkpointing but does not support the combined chunked-forward hypothesis as a distinct memory-saving method.

## Recommended next action

Stop this line as a paper candidate; use checkpoint-only as the practical 4 GB training baseline and only revisit chunked-forward if profiling identifies MLP activations as the dominant peak in a different architecture.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/gradient-checkpointing-with-chunked-forward-4gb-vram-training-f00d7d2095eb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
