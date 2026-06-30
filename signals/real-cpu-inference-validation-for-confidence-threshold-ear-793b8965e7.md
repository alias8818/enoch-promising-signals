# Real CPU inference validation for confidence-threshold early-exit cascades

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-cpu-inference-validation-for-confidence-threshold-ear-793b8965e7`
Run ID: `real-cpu-inference-validation-for-confidence-threshold-ear-793b8965e7-20260523T111602758948+0000`

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

- Parent run decision: Early-exit cascade router for CPU serving: enoch://control-plane/projects/early-exit-cascade-router-for-cpu-serving-545c67795e74/runs/early-exit-cascade-router-for-cpu-serving-545c67795e74-20260523T110636121032+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/29f7362601bb

## What looked useful

Full SST-2 dev direct CPU inference supported the cascade mechanism: threshold 0.99 accepted 84.4% of requests, fell back on 15.6%, matched fallback accuracy at 0.9243, and reduced mean model inference latency from 112.61 ms to 74.32 ms per example.

## Boundaries and scale limits

Single text-classification dataset, one model pair, sequential unbatched PyTorch CPU inference, model forward timing only after tokenization, no production server concurrency, no ONNX/int8 optimization, no held-out threshold tuning split, and no internal transformer early-exit heads.

## Claim scope

A two-model confidence-threshold CPU cascade using DistilBERT SST-2 as the first stage and BERT-base SST-2 as fallback preserved BERT-base accuracy on the full SST-2 validation split at threshold 0.99 while reducing mean sequential per-example model inference latency by 34.0%.

## Why it stopped

Tier 1 direct validation produced a useful bounded mechanism signal, but one dataset/model pair is not publication-grade evidence.

## Recommended next action

Run a medium confirmation across at least three text-classification datasets/model pairs with held-out threshold selection and bootstrap confidence intervals before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium multi-dataset CPU validation for confidence-threshold cascades
- Success threshold: Across a majority of tested dataset/model-pair settings, the selected threshold keeps accuracy within 1 percentage point of fallback-only accuracy and reduces mean CPU latency by at least 20%, with bootstrap intervals excluding zero latency gain.
- Stop condition: Stop as negative if fewer than half of settings meet the accuracy-preservation and latency-reduction thresholds, or if threshold tuning is unstable enough that held-out selection fails on final evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/real-cpu-inference-validation-for-confidence-threshold-ear-793b8965e7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
