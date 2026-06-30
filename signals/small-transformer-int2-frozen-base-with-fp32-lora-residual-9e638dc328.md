# Small Transformer INT2 Frozen Base with FP32 LoRA Residual Adaptation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-transformer-int2-frozen-base-with-fp32-lora-residual-9e638dc328`
Run ID: `small-transformer-int2-frozen-base-with-fp32-lora-residual-9e638dc328-20260527T034802316685+0000`

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

- Parent run decision: INT2 Base with FP32 LoRA Residual Fine-Tuning on CPU: enoch://control-plane/projects/int2-base-with-fp32-lora-residual-fine-tuning-on-cpu-cd0f1562f7e1/runs/int2-base-with-fp32-lora-residual-fine-tuning-on-cpu-cd0f1562f7e1-20260525T234650898737+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/23d032b8c77b

## What looked useful

INT2 frozen-base plus FP32 LoRA residual adaptation passed the predeclared small direct threshold in two seeds: seed 7 reached loss 0.3045 and accuracy 0.9622 versus frozen INT2 loss 5.6338 and FP32-LoRA loss 0.2945; seed 11 reached loss 0.2950 and accuracy 0.9621 versus frozen INT2 loss 5.3728 and FP32-LoRA loss 0.3069.

## Boundaries and scale limits

Evidence is limited to tiny synthetic modular-sequence language modeling on CPU. The INT2 implementation uses dequantized 4-level tensors rather than packed deployment kernels. No GPT-2-small-class model, natural-language corpus, rank sweep, quantization-granularity sweep, hardware throughput, or memory-saving validation was run.

## Claim scope

In a two-layer synthetic next-token transformer with a frozen 4-level INT2-quantized base, FP32 LoRA rank-4 residuals on linear maps restored adaptation-task accuracy to about 96.2%, matching the FP32 frozen-base LoRA control and strongly outperforming the frozen INT2 no-adaptation control across two full seeds.

## Why it stopped

Tier 1 small direct validation succeeded as useful mechanism evidence, but synthetic tiny-model results are insufficient for a paper or broad viability claim.

## Recommended next action

Run a bounded deepen follow-up on a GPT-2-small-class or parameter-matched real-language baseline with packed or deployment-realistic INT2 weights, the same frozen INT2 and FP32-LoRA controls, and at least three seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class INT2 frozen base with FP32 LoRA residual adaptation
- Success threshold: INT2+LoRA recovers at least 80% of FP32+LoRA perplexity improvement over frozen INT2, final validation perplexity is within 10% of FP32+LoRA, and measured base-weight memory is at least 3x lower than FP32 storage without a catastrophic throughput penalty.
- Stop condition: Stop as negative if INT2+LoRA recovers less than 50% of FP32+LoRA improvement or remains more than 25% worse in validation perplexity after matched adaptation budget in two of three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-int2-frozen-base-with-fp32-lora-residual-9e638dc328`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
