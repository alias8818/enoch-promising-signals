# TinyOptimizer: 1-bit Adam for <4GB VRAM Fine-tuning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tinyoptimizer-1-bit-adam-for-4gb-vram-fine-tuning-889a5df686f4`
Run ID: `tinyoptimizer-1-bit-adam-for-4gb-vram-fine-tuning-889a5df686f4-20260613T043421968673+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/4c047a0b25d1

## What looked useful

Optimizer-state memory fell from measured fp32 AdamW 8.0 bytes/parameter in dummy state tests, or about 4.0 bytes/parameter for bf16 AdamW states in the proxy train loop, to about 1.0 byte/parameter for TinySignAdamW. Same-LR TinySignAdamW lagged AdamW badly, but LR tuning recovered comparable three-seed final loss on the synthetic LM proxy: AdamW lr=0.003 mean 1.6459, TinySignAdamW lr=0.01 mean 1.6327.

## Boundaries and scale limits

Not true bit-packed 1-bit storage; not tested on pretrained LLM fine-tuning, real datasets, production 8-bit optimizers, or a hard 4 GiB GPU memory cap. Python implementation is slower than fused AdamW.

## Claim scope

A PyTorch uint8 sign-state Adam-like optimizer can cut optimizer-state tensors to about 1 byte per trainable parameter and, after learning-rate tuning, match AdamW on a small synthetic CUDA language-model proxy.

## Why it stopped

Evidence is a small synthetic proxy and memory-accounting result, not direct validation of <4GB pretrained fine-tuning.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement a bit-packed or production low-bit optimizer and compare against 8-bit AdamW on GPT-2-small-class fine-tuning under an enforced 4 GiB memory budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard-4GiB GPT-2-small low-bit optimizer comparison
- Success threshold: Under the same 4 GiB cap, complete the fine-tuning run without OOM and finish within 5% validation loss of 8-bit AdamW while using less optimizer-state memory.
- Stop condition: Stop if the low-bit optimizer OOMs under the cap, diverges on two learning-rate settings, or is more than 10% worse than 8-bit AdamW validation loss at matched steps.

## Evidence references

- Artifact root: `<local-path>/projects/tinyoptimizer-1-bit-adam-for-4gb-vram-fine-tuning-889a5df686f4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
