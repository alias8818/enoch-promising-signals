# Real GPT-2-small FP16 checkpointing under a 6 GiB cap

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-gpt-2-small-fp16-checkpointing-under-a-6-gib-cap-8d4e50a996`
Run ID: `real-gpt-2-small-fp16-checkpointing-under-a-6-gib-cap-8d4e50a996-20260605T181709489490+0000`

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

- Parent run decision: FP16 Gradient Checkpointing for 6GB VRAM Training on GB10: enoch://control-plane/projects/fp16-gradient-checkpointing-for-6gb-vram-training-on-gb10-3e92e83be93c/runs/fp16-gradient-checkpointing-for-6gb-vram-training-on-gb10-3e92e83be93c-20260605T142008715595+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/4368a712410f

## What looked useful

Activation checkpointing materially changed the feasible GPT-2-small FP16 microbatch under the 6 GiB cap: clean finite-loss runs fit batch 3 without checkpointing and batch 6 with checkpointing; batch 4 without checkpointing and batch 7 with checkpointing OOMed.

## Boundaries and scale limits

Short controlled direct memory test only: random initialization, synthetic tokens, two measured optimizer steps after one warmup step, allocator cap on a larger UMA GB10 device rather than a physical 6 GiB discrete GPU, and no convergence or real-corpus validation.

## Claim scope

On NVIDIA GB10 with PyTorch 2.12.0+cu130 and Transformers GPT2LMHeadModel using GPT-2-small dimensions, FP16 weights/activations, FP32 cross-entropy, AdamW lr=1e-6 eps=1e-4, synthetic sequence-length-1024 token batches, and a 6 GiB PyTorch CUDA allocator cap, activation checkpointing completed batch size 6 while non-checkpointed training OOMed by batch size 4.

## Why it stopped

The controlled small direct test supports the memory mechanism but is too short and synthetic for paper-positive validation.

## Recommended next action

Stop this run as no-paper useful signal; deepen only with a real pretrained GPT-2-small plus real tokenized corpus run of hundreds of optimizer steps under the same 6 GiB cap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2-small real-corpus checkpointing stability under a 6 GiB cap
- Success threshold: At least 300 optimizer steps on real data complete under the 6 GiB cap with finite losses throughout, peak CUDA reserved below 6 GiB, and checkpointing fitting at least 1.5x the non-checkpointed microbatch or matching the batch 6 threshold observed here.
- Stop condition: Stop if checkpointed pretrained real-data training OOMs below batch size 6 under the cap, produces persistent NaN/Inf losses after FP16-safe optimizer settings, or cannot exceed the non-checkpointed feasible microbatch by at least 1.5x.

## Evidence references

- Artifact root: `<local-path>/projects/real-gpt-2-small-fp16-checkpointing-under-a-6-gib-cap-8d4e50a996`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
