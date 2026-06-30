# Self-Speculative Decoding via Layer Skipping for GLM-5.1

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-decoding-via-layer-skipping-for-glm-5-1-4064c16601c8`
Run ID: `self-speculative-decoding-via-layer-skipping-for-glm-5-1-4064c16601c8-20260527T043943052505+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f8722ba9e610

## What looked useful

For distilgpt2 over 8 prompts and 96 next-token positions per skip setting, keeping 1, 2, 3, or 5 of 6 layers yielded top-1 match rates of 0.229, 0.313, 0.323, and 0.385; distribution-overlap acceptance of 0.182, 0.266, 0.265, and 0.363; and best estimated speculative speedups of 0.740, 0.761, 0.719, and 0.706 respectively. Naive layer skipping is therefore a slowdown in this proxy.

## Boundaries and scale limits

This does not directly validate GLM-5.1. The run did not test GLM architecture, GLM tokenizer/data, KV-cache-aware serving, GPU kernels, or parallel verification on production hardware.

## Claim scope

On a small distilgpt2 proxy, naive self-speculative decoding that uses logits after skipping later transformer layers is not promising: skipped-layer drafts have low agreement with the full model and no estimated speedup under measured CPU costs.

## Why it stopped

Proxy early falsification, not full GLM-5.1 validation: the directly tested small-model mechanism produced low acceptance and estimated slowdown.

## Recommended next action

Stop this naive layer-skipping path as no-paper proxy evidence; a bounded follow-up should test whether a trained intermediate draft head or calibration loss can raise overlap acceptance above a useful threshold on the same proxy before spending GLM-5.1 serving resources.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated intermediate draft heads for self-speculative layer skipping
- Success threshold: At least one intermediate draft configuration must achieve estimated speedup greater than 1.10 with distribution-overlap acceptance at or above 0.65 on held-out prompts.
- Stop condition: Stop if calibrated heads remain below 0.50 overlap acceptance or estimated speedup remains at or below 1.0 after a bounded CPU/GPU-local training run.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-layer-skipping-for-glm-5-1-4064c16601c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
