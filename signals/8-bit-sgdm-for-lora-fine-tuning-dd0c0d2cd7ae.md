# 8-bit SGDM for LoRA Fine-tuning

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `8-bit-sgdm-for-lora-fine-tuning-dd0c0d2cd7ae`
Run ID: `8-bit-sgdm-for-lora-fine-tuning-dd0c0d2cd7ae-20260525T142810930123+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/51320b64bd65

## What looked useful

8-bit momentum quantization appears viable for LoRA-only SGDM state compression in controlled proxy tasks, with mean final-loss ratios of 0.9983 and 1.000016 versus FP32 SGDM, but the naive implementation ran at about 49-50% of FP32 SGDM throughput.

## Boundaries and scale limits

No pretrained transformer, no real text dataset, no downstream language-model metric, only 400-step synthetic proxy tasks, and no fused or foreach optimizer kernel. Results should not be treated as full LLM LoRA validation.

## Claim scope

On small synthetic frozen-base LoRA regression tasks, blockwise 8-bit SGDM momentum matched FP32 SGDM final validation loss across five seeds per task and reduced persistent momentum-state memory by 74.61%; the implementation tested was a compact unfused PyTorch optimizer.

## Why it stopped

Proxy-only useful signal; not a full validation and not paper-ready.

## Recommended next action

Run a bounded GPT-2-small-class LoRA fine-tuning follow-up on a real text dataset with the same FP32 SGDM versus 8-bit SGDM comparison and a fused or foreach optimizer path if throughput is part of the claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small LoRA validation for 8-bit SGDM momentum
- Success threshold: 8-bit SGDM reaches validation loss or perplexity within 1% of FP32 SGDM across seeds, reduces persistent optimizer-state memory by at least 70%, and does not reduce throughput by more than 15% if using an optimized implementation.
- Stop condition: Stop as negative if 8-bit SGDM is more than 3% worse in validation loss or perplexity at matched compute, or if optimized throughput remains more than 25% slower without a compensating memory-pressure benefit.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-sgdm-for-lora-fine-tuning-dd0c0d2cd7ae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
