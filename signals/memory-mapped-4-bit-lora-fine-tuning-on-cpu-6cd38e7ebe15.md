# Memory-Mapped 4-bit LoRA Fine-Tuning on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `memory-mapped-4-bit-lora-fine-tuning-on-cpu-6cd38e7ebe15`
Run ID: `memory-mapped-4-bit-lora-fine-tuning-on-cpu-6cd38e7ebe15-20260609T010615273581+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3202d22de330

## What looked useful

Memory mapping a 32768 x 4096 packed q4 base kept current RSS near 31.46 MiB versus 159.59 MiB for copied q4 and 607.84 MiB for dequantized float32. A 4096 x 1024 mmap q4 base with rank-8 LoRA reduced eval MSE from 0.9391 to 0.01058 in 80 CPU steps with about 54 MiB current RSS.

## Boundaries and scale limits

Synthetic linear base only; no transformer, tokenizer, real dataset, perplexity metric, optimizer framework integration, checkpoint/resume test, page-fault analysis, or end-to-end comparison with mature CPU quantized training stacks.

## Claim scope

On a CPU worker with synthetic matrices, a frozen packed 4-bit base can be memory-mapped and streamed through chunked forward passes while rank-8 LoRA adapters train successfully on a controlled low-rank target, with substantially lower current RSS than copied q4 or dequantized float32 base storage.

## Why it stopped

No-paper closure: this run is a controlled synthetic mechanism validation, not a full real-model fine-tuning validation.

## Recommended next action

Run a bounded deepen follow-up in a GPT-2-small-class CPU transformer that measures tokens/s, RSS, page faults, checkpoint/resume correctness, and loss/perplexity against non-mmap quantized and standard LoRA baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class mmap q4 LoRA CPU fine-tuning benchmark
- Success threshold: Mmap q4 LoRA reaches within 10% of the best baseline validation loss/perplexity after the same step budget, uses at least 2x lower current RSS than float32-base LoRA, and has no more than 30% tokens/s slowdown versus copied q4 LoRA.
- Stop condition: Stop if the implementation cannot complete a 100-step real transformer run under 15 minutes on the CPU worker, if loss fails to decrease over the first 50 steps, or if mmap q4 current RSS is not materially lower than copied q4 or float32 baselines.

## Evidence references

- Artifact root: `<local-path>/projects/memory-mapped-4-bit-lora-fine-tuning-on-cpu-6cd38e7ebe15`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
