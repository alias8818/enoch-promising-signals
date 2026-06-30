# GPT-2-small-class memory-cap sweep for CPU-evicted AdamW

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gpt-2-small-class-memory-cap-sweep-for-cpu-evicted-adamw-259edd479c`
Run ID: `gpt-2-small-class-memory-cap-sweep-for-cpu-evicted-adamw-259edd479c-20260604T014631093545+0000`

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

- Parent run decision: Dynamic Optimizer State Eviction for Tiny-VRAM Training: enoch://control-plane/projects/dynamic-optimizer-state-eviction-for-tiny-vram-training-31fe34674533/runs/dynamic-optimizer-state-eviction-for-tiny-vram-training-31fe34674533-20260602T211743804112+0000
- Parent run decision: Transformer Memory-Cap Test for CPU-Evicted AdamW: enoch://control-plane/projects/transformer-memory-cap-test-for-cpu-evicted-adamw-a39e23a211/runs/transformer-memory-cap-test-for-cpu-evicted-adamw-a39e23a211-20260603T180813988443+0000

## What looked useful

Cap 0 MiB moved about 0.922 GiB of AdamW moment tensors to CPU and reduced CUDA peak allocation by about 1.096 GiB versus stock AdamW, but slowed mean step time to 2.17x baseline. Cap 256 MiB moved about 0.675 GiB to CPU, saved about 0.848 GiB CUDA peak, and slowed to 1.83x baseline. Caps at 1024 MiB or unlimited retained all moments on CUDA for this model.

## Boundaries and scale limits

Three fixed seeds, synthetic fixed-token batches, block size 128, batch size 1, 20 steps per variant, one GB10 CUDA host, no real corpus perplexity, no long-horizon stability test, and no hard device-memory OOM/larger-batch enablement test.

## Claim scope

On a GPT-2-small-class 123.8M-parameter CUDA training microbenchmark, explicit CPU eviction of AdamW FP32 moment state reduces measured CUDA peak allocation in proportion to evicted state bytes, but low caps slow training steps materially.

## Why it stopped

Tier 2 medium confirmation produced a reproducible memory-throughput tradeoff but not publication-grade evidence: the mechanism works locally, yet quality, long-horizon stability, and real memory-pressure enablement remain unproven.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded test should verify whether CPU-evicted AdamW enables a larger batch/sequence/model under an actual constrained CUDA memory budget while keeping slowdown below a predefined threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard-memory-budget GPT-2-small CPU-evicted AdamW enablement test
- Success threshold: CPU-evicted AdamW fits and trains a configuration with at least 25% more tokens per step or parameters than the largest fitting stock AdamW baseline while keeping mean step-time slowdown below 2.0x and showing non-increasing training loss over 50 steps.
- Stop condition: Stop as negative if CPU-evicted AdamW cannot fit a larger configuration than stock AdamW, or if the larger fitting configuration requires 2.0x or greater slowdown without a compensating tokens-per-step or model-size gain.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-memory-cap-sweep-for-cpu-evicted-adamw-259edd479c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
