# Full GPT-2-small causal-LM mmap q4 LoRA CPU benchmark on real text

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `full-gpt-2-small-causal-lm-mmap-q4-lora-cpu-benchmark-on-r-2be4b7841e`
Run ID: `full-gpt-2-small-causal-lm-mmap-q4-lora-cpu-benchmark-on-r-2be4b7841e-20260609T095242530053+0000`

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

- Parent run decision: Memory-Mapped 4-bit LoRA Fine-Tuning on CPU: enoch://control-plane/projects/memory-mapped-4-bit-lora-fine-tuning-on-cpu-6cd38e7ebe15/runs/memory-mapped-4-bit-lora-fine-tuning-on-cpu-6cd38e7ebe15-20260609T010615273581+0000
- Parent run decision: GPT-2-small-class mmap q4 LoRA CPU fine-tuning benchmark: enoch://control-plane/projects/gpt-2-small-class-mmap-q4-lora-cpu-fine-tuning-benchmark-5c30358d4a/runs/gpt-2-small-class-mmap-q4-lora-cpu-fine-tuning-benchmark-5c30358d4a-20260609T035800703147+0000

## What looked useful

Naive mmap q4 plus LoRA is not practically competitive as implemented: dense baseline reached 183.95 tok/s and PPL 80.57; q4_body reached 46.62 tok/s and PPL 116.32; full q4 reached 42.70 tok/s and PPL 402592.72; full q4 LoRA reached 37.61 tok/s and PPL 406335.36. Dense lm_head ablation localizes most of the quality failure to output-head quantization.

## Boundaries and scale limits

Medium local CPU confirmation only: 2,048 scored tokens at sequence length 64 for the main run, one dense baseline seed and a second shorter LoRA seed check. LoRA deltas were deterministic synthetic matrices, not trained adapters. The q4 path dequantizes into torch matmuls and is not an optimized int4 GEMM implementation.

## Claim scope

On GPT-2-small CPU inference over a fixed Wikitext real-text shard, a literal mmap-backed per-column q4 projection implementation with synthetic rank-8 LoRA support compressed projected matrix storage by 7.93x but was slower than dense PyTorch CPU and full q4 including lm_head catastrophically degraded perplexity.

## Why it stopped

Tier 2 direct benchmark produced a useful negative/mixed result: compression worked, but full q4 quality failed badly and mmap q4 execution was about 4x slower than the dense CPU baseline.

## Recommended next action

Stop this line as no-paper evidence unless a follow-up specifically replaces naive lm_head q4 and dequantizing matmuls with an optimized groupwise or activation-aware q4 scheme and a real int4 CPU kernel.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized GPT-2-small q4 output-head and int4 CPU kernel benchmark
- Success threshold: Perplexity no worse than 1.5x dense baseline and throughput at least 1.0x dense baseline on the same CPU worker for q4_body or full q4 with documented memory savings.
- Stop condition: Stop if lm_head quantization remains above 2x dense perplexity or the optimized q4 path remains below 0.75x dense CPU throughput on 2,048 or more real-text scored tokens.

## Evidence references

- Artifact root: `<local-path>/projects/full-gpt-2-small-causal-lm-mmap-q4-lora-cpu-benchmark-on-r-2be4b7841e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
