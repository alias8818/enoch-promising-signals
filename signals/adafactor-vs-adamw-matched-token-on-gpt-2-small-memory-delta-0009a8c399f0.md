# Adafactor vs AdamW matched-token on GPT-2-small, memory delta

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adafactor-vs-adamw-matched-token-on-gpt-2-small-memory-delta-0009a8c399f0`
Run ID: `adafactor-vs-adamw-matched-token-on-gpt-2-small-memory-delta-0009a8c399f0-20260610T131611980135+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/021ea2559543

## What looked useful

Adafactor's factorized state representation gives a directly measured optimizer-state memory saving of about 948 MiB on GPT-2-small-class fp32 training, but peak CUDA memory savings shrink when activation memory dominates.

## Boundaries and scale limits

The run used random initialization, synthetic token IDs, one optimizer step per configuration, and no mixed precision, gradient checkpointing, fused optimizers, sharding, distributed training, real corpus, validation loss, or long-run throughput measurement.

## Claim scope

In isolated one-step fp32 GPT-2-small-class synthetic-token training on a single NVIDIA GB10, Transformers Adafactor materialized about 1.2 MiB optimizer state versus about 949.4 MiB for torch AdamW, saving about 948 MiB of post-step CUDA allocation at matched token counts from 128 to 1024 tokens per step.

## Why it stopped

A direct bounded memory result was obtained, but it is a one-step synthetic-token memory probe rather than a full validation of optimizer quality or long-run training behavior.

## Recommended next action

Stop this run as no-paper useful evidence; a bounded follow-up should test real-corpus multi-step GPT-2-small training with tuned learning rates, validation loss, throughput, and fp32/bf16 memory telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus GPT-2-small Adafactor vs AdamW memory-throughput-loss comparison
- Success threshold: Adafactor saves at least 700 MiB CUDA final allocation versus AdamW while achieving validation loss within 2 percent of AdamW at the same token budget and no worse than 10 percent lower tokens per second.
- Stop condition: Stop if Adafactor loses the memory advantage under practical precision settings, fails to approach AdamW validation loss after bounded learning-rate tuning, or the run exceeds the calibrated local budget without checkpointed metrics.

## Evidence references

- Artifact root: `<local-path>/projects/adafactor-vs-adamw-matched-token-on-gpt-2-small-memory-delta-0009a8c399f0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
