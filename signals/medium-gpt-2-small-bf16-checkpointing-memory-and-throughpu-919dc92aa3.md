# Medium GPT-2-small bf16 checkpointing memory and throughput sweep

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-gpt-2-small-bf16-checkpointing-memory-and-throughpu-919dc92aa3`
Run ID: `medium-gpt-2-small-bf16-checkpointing-memory-and-throughpu-919dc92aa3-20260608T013742786268+0000`

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

- Parent run decision: Real-data GPT-2-small confirmation of bf16 checkpointing memory reduction: enoch://control-plane/projects/real-data-gpt-2-small-confirmation-of-bf16-checkpointing-m-ec57190492/runs/real-data-gpt-2-small-confirmation-of-bf16-checkpointing-m-ec57190492-20260607T211530589479+0000
- Parent run decision: Gradient Checkpointing + Mixed Precision for 60% VRAM Reduction: enoch://control-plane/projects/gradient-checkpointing-mixed-precision-for-60-vram-reduction-a3afc381745a/runs/gradient-checkpointing-mixed-precision-for-60-vram-reduction-a3afc381745a-20260607T170532278631+0000

## What looked useful

Gradient checkpointing gives a stable, activation-pressure-dependent memory/throughput tradeoff for GPT-2-small bf16 on GB10: larger batch/sequence shapes save more memory but consistently pay recompute throughput cost.

## Boundaries and scale limits

Single GPU, one GPT-2-small implementation, synthetic tokens, short fixed-step runs, no real dataloader, no convergence or time-to-quality validation, no multi-GPU or larger-model evidence.

## Claim scope

On a single NVIDIA GB10, GPT-2-small-class bf16 training with AdamW and synthetic token batches showed full gradient checkpointing reduced CUDA peak allocated memory by 26.3% to 43.5% across batch sizes 2-16 and sequence lengths 512-1024, while reducing training throughput by 10.3% to 17.6%.

## Why it stopped

Medium direct local evidence supports the mechanism but is not paper-ready because it is synthetic-token, single-host, short-horizon evidence without convergence or end-to-end training validation.

## Recommended next action

Run a bounded deepen follow-up with a real tokenized dataset/input pipeline and include max-fit batch-size plus time-to-fixed-token-budget comparisons; stop if checkpointing does not enable at least a 1.3x larger batch or if end-to-end throughput loss exceeds 25%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small bf16 checkpointing with real dataloader and max-fit batch comparison
- Success threshold: Checkpointing must reduce peak allocated CUDA memory by at least 25%, enable at least 1.3x larger max-fit batch at sequence length 1024, and keep end-to-end tokens/sec loss at or below 25% for the same fixed sequence-item budget.
- Stop condition: Stop as no-paper negative if memory savings fall below 25%, max-fit batch improves by less than 1.3x, or end-to-end throughput loss exceeds 25% after dataloader overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/medium-gpt-2-small-bf16-checkpointing-memory-and-throughpu-919dc92aa3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
