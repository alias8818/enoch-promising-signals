# Layer-Dropping Draft: Skip-Layer Speculation on Single Model

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `layer-dropping-draft-skip-layer-speculation-on-single-model-b39a9fd4bbd9`
Run ID: `layer-dropping-draft-skip-layer-speculation-on-single-model-b39a9fd4bbd9-20260530T040131002010+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e8ab10a9b95e

## What looked useful

Skipping layers creates a cost/acceptance tradeoff that is unfavorable in this setup: low-depth drafts are cheap but rejected often, while high-depth/interleaved drafts are accepted more often but cost too much. The best optimistic bound over tested settings and K=1..8 was 0.91x.

## Boundaries and scale limits

Small-model inference probe only; no full KV-cache speculative decoder, no 7B+ model, no trained auxiliary heads or layerwise distillation, and no broad prompt/task sweep.

## Claim scope

Naive untrained skip-layer draft speculation on a single pretrained GPT-2-family model, using DistilGPT-2 on 64 WikiText validation contexts, does not produce an optimistic speculative decoding speedup for prefix or interleaved retained-layer draft paths.

## Why it stopped

Early negative result from a direct small pretrained-LM proxy: every tested prefix/interleaved skip-layer draft had an optimistic speedup bound below 1x before implementation overhead, so this is not a full-scale validation but is sufficient to reject the naive construction locally.

## Recommended next action

Stop this naive untrained skip-layer draft line; only reopen with a bounded calibration/distillation variant that demonstrates a draft/full cost ratio and acceptance pair capable of exceeding 1.05x in an end-to-end decoder.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Single-Model Layer Draft Heads
- Success threshold: At least 1.05x measured end-to-end tokens/sec versus full-model sampling, with mean acceptance >= 0.5 and no statistically obvious output-distribution drift on held-out prompts.
- Stop condition: Stop if calibrated draft candidates still have best optimistic K-sweep speedup below 1.0x or if end-to-end decoding fails to exceed baseline throughput by 5%.

## Evidence references

- Artifact root: `<local-path>/projects/layer-dropping-draft-skip-layer-speculation-on-single-model-b39a9fd4bbd9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
