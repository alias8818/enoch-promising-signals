# GPT-2-small bf16 checkpointing with real dataloader and max-fit batch comparison

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `gpt-2-small-bf16-checkpointing-with-real-dataloader-and-ma-2e375d14ef`
Run ID: `gpt-2-small-bf16-checkpointing-with-real-dataloader-and-ma-2e375d14ef-20260608T054607602215+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Medium GPT-2-small bf16 checkpointing memory and throughput sweep: enoch://control-plane/projects/medium-gpt-2-small-bf16-checkpointing-memory-and-throughpu-919dc92aa3/runs/medium-gpt-2-small-bf16-checkpointing-memory-and-throughpu-919dc92aa3-20260608T013742786268+0000
- Parent run decision: Real-data GPT-2-small confirmation of bf16 checkpointing memory reduction: enoch://control-plane/projects/real-data-gpt-2-small-confirmation-of-bf16-checkpointing-m-ec57190492/runs/real-data-gpt-2-small-confirmation-of-bf16-checkpointing-m-ec57190492-20260607T211530589479+0000

## What looked useful

Checkpointing at batch 8 used 0.51x the PyTorch peak allocation but only 0.76x the no-checkpoint throughput over 10 measured steps. In short max-fit probes, no-checkpoint completed batch 32 with only 5.08 GiB MemAvailable, while checkpointing completed batch 64 with 24.92 GiB MemAvailable; checkpoint batch 96 and longer high-batch confirmations terminated.

## Boundaries and scale limits

Single host, one dataset, one GPT-2-small random-initialized model shape, short high-batch probes, and several SIGTERM resource-limit events rather than clean OOM thresholds. No pretrained convergence or multi-hour sustained-training evidence.

## Claim scope

On one GB10 host with PyTorch 2.12.0+cu130, GPT-2-small-shape bf16 training over a real WikiText-2 GPT-2-tokenized dataloader at sequence length 1024, activation checkpointing reduced matched-batch memory and enabled a larger completed short-run microbatch, but it slowed matched-batch throughput and was not robustly confirmed in sustained high-batch runs.

## Why it stopped

No-paper useful systems signal: direct GPT-2-small bf16 dataloader evidence supports the memory mechanism and a short-run max-batch advantage, but matched-batch throughput regresses and sustained high-batch validation was not stable enough for a paper claim.

## Recommended next action

Run one final deepen pass with a pre-tokenized/memmap dataloader and per-step metric flushing to cleanly classify sustained batch 32/64/80 behavior without losing partial high-batch evidence to process termination.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sustained GPT-2-small checkpointing max-batch confirmation with pre-tokenized dataloader
- Success threshold: Checkpointing sustains at least 1.5x the largest no-checkpoint microbatch for 50 measured steps with at least 80% of the no-checkpoint max-batch tokens/s and at least 10 GiB MemAvailable headroom.
- Stop condition: Stop if checkpoint batch 64 cannot complete 50 measured steps, if throughput falls below 70% of the no-checkpoint max-batch tokens/s, or if MemAvailable drops below 8 GiB before a clean result is written.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-bf16-checkpointing-with-real-dataloader-and-ma-2e375d14ef`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
