# Learned Residual Channels for Ternary-Plus-Correction Quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `learned-residual-channels-for-ternary-plus-correction-quantization-329e57a71a01`
Run ID: `learned-residual-channels-for-ternary-plus-correction-quantization-329e57a71a01-20260520T145805882509+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/97eb668fc02a

## What looked useful

Across 16 seeds, rank-1 correction reduced synthetic teacher logit NMSE by 58.1% and improved dense-teacher agreement from 0.4304 to 0.6079 at 15.1% FP16 bit fraction; rank-8 reduced activation NMSE by 67.4% and logit NMSE by 75.6% at about one third FP16 bit fraction.

## Boundaries and scale limits

No real pretrained model, real dataset, quantization-aware training, optimized kernel, latency, or perplexity/accuracy validation was run. SVD residual fitting proxies learned residual channels.

## Claim scope

In NumPy synthetic matrix and synthetic two-layer teacher probes, ternary post-training quantization plus low-rank residual correction channels consistently reduced reconstruction and logit error versus ternary-only at 15-34% of an FP16 dense storage-bit proxy.

## Why it stopped

This run produced proxy/synthetic mechanism evidence only; it is useful but not a full validation or paper-ready result.

## Recommended next action

Run a bounded direct model follow-up on a real small network or pretrained layer trace, comparing ternary-only, low-rank-only, and ternary-plus-learned-residual at matched bit budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Small-Model Validation of Ternary Plus Learned Residual Channels
- Success threshold: At <=35% FP16-equivalent bit budget, ternary-plus-learned-residual recovers at least 50% of the ternary-only task-metric loss and beats matched low-rank-only correction on the direct validation metric.
- Stop condition: Stop if residual correction fails to beat ternary-only by at least 20% relative loss recovery or fails to beat matched low-rank-only on the direct task metric.

## Evidence references

- Artifact root: `<local-path>/projects/learned-residual-channels-for-ternary-plus-correction-quantization-329e57a71a01`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
