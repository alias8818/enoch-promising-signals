# Quantized Draft Head: Auxiliary LoRA Exit for Speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-draft-head-auxiliary-lora-exit-for-speculation-533e460a6f24`
Run ID: `quantized-draft-head-auxiliary-lora-exit-for-speculation-533e460a6f24-20260607T201502410394+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/d2bef7faee6b

## What looked useful

Across three seeds, LoRA improved target top-1 agreement by 1.40 percentage points and reduced KL to target by 5.0% versus a linear early exit; int8 head quantization was effectively lossless. The acceptance proxy fell by 2.74 percentage points, so better imitation did not imply better speculative acceptance in this setup.

## Boundaries and scale limits

No real-corpus GPT-2-small-class model, no full draft-verify decoding loop, no optimized int8 kernel, and no long-context or multi-model serving benchmark. Speculative decoding is measured by per-token top-1 agreement and min(1, p_target(draft) / p_draft(draft)) proxies only.

## Claim scope

Toy GPU experiment with a 4-layer 686k-parameter transformer on synthetic autoregressive sequences: an auxiliary LoRA early exit from layer 2 improves target-logit imitation metrics versus a plain linear exit and survives row-wise int8 vocabulary-head quantization, but does not improve the speculative acceptance proxy.

## Why it stopped

No-paper mixed result: the core quantized LoRA exit mechanism worked for imitation and quantization robustness, but the speculation acceptance proxy worsened in this toy experiment.

## Recommended next action

Run a bounded calibration follow-up that adds draft temperature/scaling or acceptance-aware distillation to the LoRA exit and requires both improved top-1 agreement and non-degraded acceptance proxy versus the linear exit.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Acceptance-Calibrated LoRA Draft Exit
- Success threshold: Calibrated LoRA int8 exit must improve target top-1 agreement by at least 1.0 percentage point over the linear exit while matching or exceeding the linear exit acceptance proxy across at least two of three seeds.
- Stop condition: Stop if calibration cannot recover the linear exit acceptance proxy or if top-1 agreement gains disappear after calibration.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-draft-head-auxiliary-lora-exit-for-speculation-533e460a6f24`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
