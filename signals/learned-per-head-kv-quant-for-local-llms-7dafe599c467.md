# Learned Per-Head KV Quant for Local LLMs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `learned-per-head-kv-quant-for-local-llms-7dafe599c467`
Run ID: `learned-per-head-kv-quant-for-local-llms-7dafe599c467-20260607T194435292528+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/f3795769f29a

## What looked useful

Learned per-head clipping reduced KV tensor MSE and improved over dynamic head-max on NLL/KL, but a simpler per-layer static clipping baseline had substantially better held-out continuation NLL and logit KL despite worse tensor MSE.

## Boundaries and scale limits

No packed integer KV kernel, no latency or bandwidth measurement, no long-context serving, no larger local LLM, no standard corpus benchmark, and only short prompt-list evaluation.

## Claim scope

Small GPT-2 probe of 4-bit dequantized KV-cache clipping schemes on 16 calibration prompts and 10 held-out continuation prompts across three prompt-split seeds.

## Why it stopped

Bounded GPT-2 direct probe did not support tensor-MSE-learned per-head KV quantization as better than a simple layer-static control for held-out continuation quality.

## Recommended next action

Stop this run as no-paper useful evidence; next run should optimize per-head parameters against semantic loss and require beating layer_static on held-out continuation NLL.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Semantic-Loss Per-Head KV Quantization Versus Layer-Static Control
- Success threshold: Semantic-loss learned per-head clipping must reduce held-out delta NLL by at least 10% versus layer_static while not increasing logit KL/token and while preserving a cache MSE advantage.
- Stop condition: Stop if semantic-loss per-head clipping fails to beat layer_static on mean held-out delta NLL across three seeds or only improves tensor MSE without improving NLL/KL.

## Evidence references

- Artifact root: `<local-path>/projects/learned-per-head-kv-quant-for-local-llms-7dafe599c467`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
