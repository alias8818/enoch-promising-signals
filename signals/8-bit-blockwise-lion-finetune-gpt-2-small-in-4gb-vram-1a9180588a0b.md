# 8-bit blockwise Lion finetune GPT-2-small in 4GB VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-blockwise-lion-finetune-gpt-2-small-in-4gb-vram-1a9180588a0b`
Run ID: `8-bit-blockwise-lion-finetune-gpt-2-small-in-4gb-vram-1a9180588a0b-20260530T083551423124+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3de4fe3a8a0b

## What looked useful

8-bit blockwise Lion reduced optimizer state from about 475 MiB for AdamW to about 119 MiB for GPT-2-small, and successfully trained below 4 GiB peak allocation in the tested settings. However, AdamW also fit under 4 GiB with the same batch-size boundary, so this does not support a unique enabling claim.

## Boundaries and scale limits

Synthetic repeated-text data only; short smoke and stress runs only; GB10 has much more physical unified memory than 4 GiB; no real 4 GB GPU or hard memory cap was enforced; no downstream quality validation; custom optimizer is unfused and not production optimized.

## Claim scope

On GB10, measured by PyTorch CUDA allocation counters rather than a hard 4 GiB hardware cap, full-parameter Hugging Face GPT-2-small can execute short bf16 gradient-checkpointed causal-LM finetuning steps with a simple 8-bit blockwise Lion optimizer below 4 GiB peak allocated memory for batch sizes up to 4 at sequence length 1024.

## Why it stopped

Proxy/local evidence supports feasibility and optimizer-state reduction, but the AdamW control also fits under the measured 4 GiB budget, so the stronger 8-bit-Lion-enables-GPT-2-small-in-4GB claim is not supported by this run.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should enforce a hard 4 GiB memory cap or use a real 4 GB GPU and compare 8-bit Lion, fp32 Lion, and AdamW on a small real finetuning dataset.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard-cap 4 GiB GPT-2-small finetune optimizer comparison
- Success threshold: 8-bit blockwise Lion completes a configuration that AdamW cannot complete under the same hard 4 GiB cap, while validation loss after a fixed sequence-item budget is within 5% of AdamW at AdamW's best fitting configuration.
- Stop condition: Stop if AdamW fits every practically relevant configuration that 8-bit blockwise Lion fits, or if 8-bit blockwise Lion shows more than 5% worse validation loss at matched sequence-item budget.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-blockwise-lion-finetune-gpt-2-small-in-4gb-vram-1a9180588a0b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
