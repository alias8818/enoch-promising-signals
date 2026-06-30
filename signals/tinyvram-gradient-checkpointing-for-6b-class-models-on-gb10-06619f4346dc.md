# TinyVRAM gradient checkpointing for 6B-class models on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tinyvram-gradient-checkpointing-for-6b-class-models-on-gb10-06619f4346dc`
Run ID: `tinyvram-gradient-checkpointing-for-6b-class-models-on-gb10-06619f4346dc-20260611T005751947752+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d8ae7b0184f5

## What looked useful

Checkpointing saved 1.97 GB peak CUDA allocation in a frozen-parameter activation diagnostic, but full-gradient peaks were unchanged across 4-layer, 8-layer, 16-layer, and 40-layer probes because weights plus gradients dominated memory. The direct 6.29B block-parameter run stayed at 25.303 GB peak with or without checkpointing, while throughput fell from 966 to 637 tokens/s.

## Boundaries and scale limits

Synthetic random input/loss only; no embeddings, LM head, optimizer state, dataloader, multi-step update, long-run fragmentation study, or full corpus training. Sequence length was bounded to 2048 for 16 layers and 1024 for the direct 40-layer 6B-class stack.

## Claim scope

On NVIDIA GB10 with PyTorch 2.12 CUDA bf16, activation checkpointing reduced activation-path memory in a frozen-parameter 16-layer 6B-class block-shape diagnostic, but did not reduce peak CUDA allocation for matched full-gradient transformer stacks up to a direct 40-layer 6.29B block-parameter probe at sequence length 1024.

## Why it stopped

Proxy/full-gradient early falsification: direct 6B-class full-gradient GB10 evidence showed no peak-memory benefit from checkpointing alone, though activation-only diagnostics confirmed the mechanism under frozen parameters.

## Recommended next action

Stop this run as an early bounded negative for checkpointing-alone TinyVRAM full-gradient training; a useful follow-up is to test the adjacent case where activations can dominate, such as LoRA/frozen-base or optimizer-sharded long-context training with a real optimizer step.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-dominated TinyVRAM checkpointing with LoRA or sharded optimizer state on GB10
- Success threshold: At least 20% lower peak CUDA allocation from checkpointing with no more than 60% throughput loss in an activation-dominated 6B-class training or adaptation step.
- Stop condition: Stop if full training/adaptation peaks remain dominated by weights, gradients, or optimizer state and checkpointing saves less than 10% peak CUDA allocation in two activation-targeted configurations.

## Evidence references

- Artifact root: `<local-path>/projects/tinyvram-gradient-checkpointing-for-6b-class-models-on-gb10-06619f4346dc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
