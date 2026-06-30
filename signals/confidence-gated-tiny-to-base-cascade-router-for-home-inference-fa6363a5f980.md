# Confidence-Gated Tiny-to-Base Cascade Router for Home Inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `confidence-gated-tiny-to-base-cascade-router-for-home-inference-fa6363a5f980`
Run ID: `confidence-gated-tiny-to-base-cascade-router-for-home-inference-fa6363a5f980-20260609T111646871077+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/153d62b5b21c

## What looked useful

At threshold 0.46, the tiny classifier handled 57.14% of test examples with 92.86% accuracy on accepted examples; the cascade reached 0.8257 accuracy versus 0.8340 for always-base, called base on 42.86% of examples, and achieved 1.5106x measured speedup versus always-base. Bootstrap 95% CI: accuracy [0.8081, 0.8423], speedup [1.4822, 1.5422].

## Boundaries and scale limits

This run used CPU linear text classifiers, batch prediction, one real classification dataset, and 1,814 held-out test examples. It did not test generative LLMs, token latency, quantization, KV-cache behavior, batching policy, real home prompts, or user-facing quality labels.

## Claim scope

On a bounded 20 Newsgroups text-classification proxy, a confidence-gated tiny-to-base cascade can preserve base-model accuracy within 1 percentage point while reducing measured per-item inference cost by about 1.51x.

## Why it stopped

No-paper closure: the mechanism worked in a reproducible classifier proxy, but this is not direct evidence for home generative inference or publication-grade validation.

## Recommended next action

Run a direct small-LM follow-up with locally runnable tiny/base generative models, token-level latency, confidence calibration, and human- or benchmark-derived quality labels before making home-inference claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Small-LM Confidence Cascade for Home Prompt Inference
- Success threshold: Cascade routes at least 40% of prompts to tiny-only, improves measured end-to-end latency by at least 1.25x versus always-base, and keeps quality within 2 percentage points of always-base on the same prompt set.
- Stop condition: Stop if tiny confidence is poorly calibrated enough that no threshold achieves both at least 25% tiny-only routing and quality within 3 percentage points of always-base, or if local generative-model latency measurements cannot be made reproducibly.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-tiny-to-base-cascade-router-for-home-inference-fa6363a5f980`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
