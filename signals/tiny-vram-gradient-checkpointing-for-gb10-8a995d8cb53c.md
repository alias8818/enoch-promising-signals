# Tiny-VRAM Gradient Checkpointing for GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-vram-gradient-checkpointing-for-gb10-8a995d8cb53c`
Run ID: `tiny-vram-gradient-checkpointing-for-gb10-8a995d8cb53c-20260613T141302730439+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2cedb9658183

## What looked useful

Activation checkpointing produced a repeatable memory-throughput tradeoff on GB10 UMA: larger activation pressure increased savings from 24.1% to 40.3% CUDA allocation reduction while throughput fell 10-16%. This supports per-block checkpointing as a practical next baseline for small-memory GB10 training experiments, but not a paper-ready claim.

## Boundaries and scale limits

Synthetic random tensors and MSE loss only; no tokenizer, corpus, optimizer schedule, convergence test, replicated statistics, hard VRAM cap, or GPT-2-small-class real training workload. GB10 reports unified memory and nvidia-smi does not expose normal GPU memory usage, so memory evidence is PyTorch allocator peak plus host MemAvailable telemetry.

## Claim scope

On this GB10 host, short synthetic bf16 transformer-style CUDA training steps showed PyTorch non-reentrant activation checkpointing reduced peak CUDA allocator memory by 24.1% at 8 layers/2048 tokens and 40.3% at 12 layers/4096 tokens, with about 10-16% lower throughput and aligned deterministic losses.

## Why it stopped

No-paper closure: this run produced a useful synthetic/proxy mechanism signal, not full validation or publication-grade evidence.

## Recommended next action

Run a bounded GPT-2-small-class training follow-up with real data/objective, fixed memory cap or allocator budget, repeated measurements, and loss parity checks before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class GB10 checkpointing memory-throughput validation
- Success threshold: Checkpointed real training reduces peak allocator or UMA memory by at least 25%, keeps final short-run loss within 2% of no-checkpoint at matched steps, and loses no more than 25% tokens/s.
- Stop condition: Stop if memory savings are below 15%, loss diverges by more than 5% at matched steps, or throughput drops by more than 35% without enabling a larger otherwise-failing configuration.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-vram-gradient-checkpointing-for-gb10-8a995d8cb53c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
