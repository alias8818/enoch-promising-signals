# LoRA-Style Low-Rank Adaptation for Memory-Bounded Fine-Tuning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lora-style-low-rank-adaptation-for-memory-bounded-fine-tuning-d2be62b18cad`
Run ID: `lora-style-low-rank-adaptation-for-memory-bounded-fine-tuning-d2be62b18cad-20260610T015845035050+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/9e213a0d0d2c

## What looked useful

LoRA r4 reached 0.6774 mean validation accuracy versus dense 0.6624 on a rank-4 target shift while using 1,088 trainable parameters versus dense 12,352 and 66,560 B versus dense 246,784 B estimated fp32 training state. On the high-rank control, LoRA r16 reached only 0.1131 accuracy versus dense 0.5443, showing the expected capacity limit.

## Boundaries and scale limits

Synthetic linear classifier only; no transformer, no real language-model data, no measured activation memory, no quantization/offload stack, and no 7B or datacenter-scale training. The result should not be read as publication-grade evidence for full memory-bounded LLM fine-tuning.

## Claim scope

In a controlled NumPy linear-classifier adaptation benchmark, LoRA-style low-rank updates recover dense-update validation accuracy when the target shift is rank-4, while using substantially fewer trainable parameters and less estimated fp32 optimizer training state; the same adapters fail to match dense adaptation on a high-rank target-shift control.

## Why it stopped

Controlled synthetic evidence supports the mechanism and exposes a failure mode, but it is not direct transformer fine-tuning evidence and does not establish novelty over existing LoRA.

## Recommended next action

Stop this run as no-paper useful signal; next run should test a small transformer language-model task with dense and LoRA baselines, measured peak memory, and perplexity/accuracy under a fixed memory budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Transformer LoRA Memory-Budget Confirmation
- Success threshold: LoRA should reach at least 95% of dense baseline validation improvement over frozen base while using at most 40% of dense measured training memory on the small transformer task.
- Stop condition: Stop if dense fine-tuning cannot beat the frozen baseline, if memory cannot be measured reproducibly, or if LoRA remains below 80% of dense improvement at ranks using at least 40% of dense memory.

## Evidence references

- Artifact root: `<local-path>/projects/lora-style-low-rank-adaptation-for-memory-bounded-fine-tuning-d2be62b18cad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
