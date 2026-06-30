# INT2 Base with FP32 LoRA Residual Fine-Tuning on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `int2-base-with-fp32-lora-residual-fine-tuning-on-cpu-cd0f1562f7e1`
Run ID: `int2-base-with-fp32-lora-residual-fine-tuning-on-cpu-cd0f1562f7e1-20260525T234650898737+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/23d032b8c77b

## What looked useful

Across five corrected main seeds, INT2+FP32 LoRA improved target test accuracy over frozen INT2 by mean +0.1643 (stdev 0.0693), while remaining mean 0.0170 below FP32-base LoRA and mean 0.0640 below full FP32 fine-tuning.

## Boundaries and scale limits

Synthetic classification only; no transformer, no language modeling corpus, no packed INT2 kernel, no GPT-2-small-class baseline, and no rank/alpha ablation beyond rank 8 alpha 16 in the main run.

## Claim scope

On a small NumPy two-layer ReLU classifier with per-row simulated INT2 frozen base weights, FP32 LoRA residual training consistently improves target-task accuracy over the frozen INT2 base across five synthetic source-to-target drift seeds.

## Why it stopped

Proxy-only CPU evidence supports trainability but does not validate the claim for real transformer language models or packed INT2 training/inference.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use a small transformer language-model task with dense, FP32-LoRA, INT2-frozen, and INT2+FP32-LoRA controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Transformer INT2 Frozen Base with FP32 LoRA Residual Adaptation
- Success threshold: INT2+FP32 LoRA recovers at least 50 percent of the frozen INT2 validation perplexity/loss degradation versus frozen FP32 and finishes within 10 percent relative validation loss of FP32-base LoRA on at least two of three repeats.
- Stop condition: Stop if INT2+FP32 LoRA fails to recover at least 25 percent of quantization-induced validation loss degradation on two repeats or is more than 20 percent worse than FP32-base LoRA after matched tuning.

## Evidence references

- Artifact root: `<local-path>/projects/int2-base-with-fp32-lora-residual-fine-tuning-on-cpu-cd0f1562f7e1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
