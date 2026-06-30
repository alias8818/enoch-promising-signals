# Multi-seed GPT-2-small shard watermark survival under longer public-corpus fine-tuning

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `83`
Project ID: `multi-seed-gpt-2-small-shard-watermark-survival-under-long-aa69a046fd`
Run ID: `multi-seed-gpt-2-small-shard-watermark-survival-under-long-aa69a046fd-20260620T015212226917+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: GPT-2-small shard watermark survival under realistic fine-tuning and evasion controls: enoch://control-plane/projects/gpt-2-small-shard-watermark-survival-under-realistic-fine-9a0ba3c7db/runs/gpt-2-small-shard-watermark-survival-under-realistic-fine-9a0ba3c7db-20260620T005402747930+0000
- Parent run decision: Embedded Shard Watermarks for Free-Rider Detection in Volunteer Training: enoch://control-plane/projects/embedded-shard-watermarks-for-free-rider-detection-in-volunteer-training-ee5a014a1d89/runs/embedded-shard-watermarks-for-free-rider-detection-in-volunteer-training-ee5a014a1d89-20260620T003112160616+0000

## What looked useful

Watermarked survival ratios were 0.9943, 1.0099, and 1.0035 with mean 1.0026. Baseline final keyed detector projection over expected watermark had mean 0.0027. Mean absolute wrong-key z-like statistic across all records was 0.7086.

## Boundaries and scale limits

This was not full-model fine-tuning and not a long public-corpus training schedule. All non-target parameters were frozen. The CPU-only host had no visible CUDA device, so longer full-model GPT-2-small fine-tuning was outside the local resource-efficiency contract.

## Claim scope

A deterministic sign watermark embedded in GPT-2-small transformer.h.0.mlp.c_fc.weight survived 36 target-shard-only Wikitext fine-tuning updates across fixed seeds 17, 29, and 43; unwatermarked baseline detector response remained near zero and wrong-key controls were noise-like.

## Why it stopped

Local evidence supports shard-level watermark persistence, but the original longer full fine-tuning claim remains unvalidated because the host is CPU-only and full-model longer GPT-2-small fine-tuning would exceed the deployment resource contract.

## Recommended next action

Stop this worker run as no-paper useful signal; the next meaningful validation is a GPU-backed full-model GPT-2-small run with the same fixed seeds, a longer public-corpus schedule, and the same baseline/wrong-key controls.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/multi-seed-gpt-2-small-shard-watermark-survival-under-long-aa69a046fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
