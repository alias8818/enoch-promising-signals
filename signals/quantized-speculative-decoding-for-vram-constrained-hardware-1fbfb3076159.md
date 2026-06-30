# Quantized Speculative Decoding for VRAM-Constrained Hardware

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-speculative-decoding-for-vram-constrained-hardware-1fbfb3076159`
Run ID: `quantized-speculative-decoding-for-vram-constrained-hardware-1fbfb3076159-20260619T062902312978+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/224517be825a

## What looked useful

Int8 draft-side quantization noise was compatible with speculative acceptance in this bounded probe (0.438 vs 0.442 fp16 acceptance), but int4 was not (0.165 acceptance). Target-call reductions did not translate into wall-clock speedup because draft overhead dominated.

## Boundaries and scale limits

Small GPT-2/distilgpt2 models, 24 fixed prompts, 768 generated tokens per variant, greedy decoding, no optimized INT kernels, no real quantized VRAM allocation reduction, no KV-cache-aware serving runtime, and no long-context memory-pressure sweep.

## Claim scope

On a GB10 host with a Python/Hugging Face GPT-2-family greedy speculative decoding harness, fake int8 draft-weight quantization preserved acceptance nearly exactly versus fp16 draft, while fake int4 quantization sharply reduced acceptance. No end-to-end speedup was demonstrated.

## Why it stopped

No-paper useful signal: this was a bounded proxy/early mechanism test, not full validation; fake int8 preserved acceptance but did not improve wall-clock throughput, and fake int4 failed acceptance.

## Recommended next action

Run one bounded follow-up using real quantized draft kernels and KV-cache-aware decoding under a fixed memory cap; stop if int8 still fails to beat target-only wall-clock throughput by at least 10%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-kernel int8 draft speculative decoding under a fixed memory cap
- Success threshold: Int8 quantized-draft speculative decoding preserves at least 95% of fp16 draft acceptance and improves wall-clock throughput by at least 10% versus target-only under the same memory cap.
- Stop condition: Stop if real int8 kernels reduce acceptance below 95% of fp16 draft or if wall-clock throughput remains at or below target-only after warmup-controlled measurement.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-speculative-decoding-for-vram-constrained-hardware-1fbfb3076159`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
