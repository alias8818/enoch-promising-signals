# Residual Channel Quantization for Home Fine-Tuning: VRAM-Efficient LoRA on Quantized Base

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-channel-quantization-for-home-fine-tuning-vram-efficient-lora-on-quantized-base-6521d0dcaf1a`
Run ID: `residual-channel-quantization-for-home-fine-tuning-vram-efficient-lora-on-quantized-base-6521d0dcaf1a-20260528T020513233565+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/93bf42d03423

## What looked useful

At 1024x1024 over three seeds, q4+LoRA mean test MSE was 0.097418 versus 0.076596 for fp-base+LoRA. RCQ with 20% residual rows reduced q4+LoRA MSE to 0.091709, recovering 27.4% of the q4 quality gap while using an estimated 46.0% of fp-base+LoRA storage. Smaller residual budgets improved monotonically but weakly.

## Boundaries and scale limits

No real transformer, tokenizer, language-model loss, optimizer-state VRAM, quantized kernel implementation, or end-task fine-tuning was tested. Memory values are analytical storage estimates plus recorded PyTorch allocation for the probe, not full training VRAM.

## Claim scope

Synthetic single-projection mechanism probe: for a 1024x1024 frozen linear mapping with a low-rank target delta and fixed rank-8 LoRA, adding frozen fp32 residual rows for high quantization-error output channels monotonically reduced held-out MSE versus naive q4+LoRA across three seeds.

## Why it stopped

Synthetic proxy supports the mechanism but does not provide direct language-model fine-tuning evidence, so it is not paper-ready.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next bounded test should implement RCQ row residuals in a small transformer LoRA fine-tune and measure validation loss plus peak memory against q4+LoRA and fp/bf16+LoRA.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer RCQ LoRA validation
- Success threshold: At least 10% recovery of the q4+LoRA validation-loss gap to fp/bf16+LoRA at no more than 60% of fp/bf16-base storage or measured peak training memory, reproduced across at least two seeds or data shards.
- Stop condition: Stop if RCQ fails to improve validation loss over q4+LoRA by at least 3% of the q4 gap at 20% residual rows, or if measured memory exceeds 70% of fp/bf16-base LoRA with no quality gain.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-quantization-for-home-fine-tuning-vram-efficient-lora-on-quantized-base-6521d0d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
