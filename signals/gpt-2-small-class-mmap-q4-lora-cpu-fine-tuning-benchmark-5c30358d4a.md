# GPT-2-small-class mmap q4 LoRA CPU fine-tuning benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gpt-2-small-class-mmap-q4-lora-cpu-fine-tuning-benchmark-5c30358d4a`
Run ID: `gpt-2-small-class-mmap-q4-lora-cpu-fine-tuning-benchmark-5c30358d4a-20260609T035800703147+0000`

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

- Parent run decision: Memory-Mapped 4-bit LoRA Fine-Tuning on CPU: enoch://control-plane/projects/memory-mapped-4-bit-lora-fine-tuning-on-cpu-6cd38e7ebe15/runs/memory-mapped-4-bit-lora-fine-tuning-on-cpu-6cd38e7ebe15-20260609T010615273581+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3202d22de330

## What looked useful

Three GPT-2-small projection-shape tests passed the >=10% loss-reduction threshold for both mmap q4 and resident q4 controls, with mmap/resident mean-step ratios of 1.059, 1.018, and 1.019. A high-learning-rate wide-input projection overflowed in both storage modes and passed after lowering LR, pointing to optimizer stability rather than mmap failure.

## Boundaries and scale limits

Synthetic single-projection NumPy benchmark only; no full 12-layer GPT-2-small causal LM, real text corpus, tokenizer, AdamW optimizer, PyTorch/Hugging Face integration, validation perplexity, or optimized int4 GEMM path was tested.

## Claim scope

Tier 1 controlled CPU evidence shows mmap-backed q4 frozen weights can support rank-8 LoRA adapter training on GPT-2-small projection shapes with identical loss behavior to resident q4 controls and about 1.8% to 5.9% mean-step overhead in passing runs.

## Why it stopped

Tier 1 direct mechanism test completed and produced useful no-paper evidence; publication readiness requires end-to-end model and real-data validation.

## Recommended next action

Run a bounded full GPT-2-small causal-LM LoRA benchmark on a small real text corpus with mmap q4, resident q4, and dense frozen-base controls before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Full GPT-2-small causal-LM mmap q4 LoRA CPU benchmark on real text
- Success threshold: mmap q4 LoRA reaches within 10% of resident q4 validation-loss improvement, mmap/resident tokens-per-second ratio is at least 0.85, and peak RSS is lower than dense frozen-base LoRA by at least 25% on the same CPU worker.
- Stop condition: Stop as negative if mmap q4 LoRA cannot reduce validation loss after a tuned smoke run, if mmap overhead exceeds 25% versus resident q4 in repeated runs, or if memory savings versus dense frozen-base LoRA are below 10%.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-mmap-q4-lora-cpu-fine-tuning-benchmark-5c30358d4a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
