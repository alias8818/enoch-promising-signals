# Difficulty-Routed Local Cascade Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `difficulty-routed-local-cascade-serving-069840b52db1`
Run ID: `difficulty-routed-local-cascade-serving-069840b52db1-20260610T210411767161+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7322411afbae

## What looked useful

The mechanism produces a real speed/quality frontier but simple confidence routing is not near-lossless here: tiny model 0.8303 accuracy, fallback 0.9106 accuracy, best speedup policy with smallest accuracy loss routed 46.3% to the small model for 0.8991 accuracy and 1.51x expected speedup.

## Boundaries and scale limits

This is a bounded classification-serving proxy on 872 examples, not autoregressive LLM serving. It does not measure generation quality, KV-cache pressure, multi-request scheduling, production batching, or broader task distributions.

## Claim scope

On GLUE/SST-2 validation using M-FAC/bert-tiny-finetuned-sst2 as the local small classifier, distilbert-base-uncased-finetuned-sst-2-english as fallback, and max-softmax confidence thresholding as the difficulty router, no threshold achieved near-lossless accuracy within 0.5 percentage points of the fallback model while also improving expected latency. The best speedup with any accuracy improvement constraint was 1.51x at 1.15 percentage points accuracy loss.

## Why it stopped

Bounded proxy evidence did not support the near-lossless difficulty-routing hypothesis; the result is useful but insufficient for a paper and is not a full LLM-serving validation.

## Recommended next action

Stop this run as no-paper useful signal; if continuing, run a bounded learned-router follow-up using separate calibration/test splits and direct end-to-end local LLM generation metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Difficulty Router for Local Cascade Serving
- Success threshold: On held-out data, achieve at least 1.3x expected end-to-end speedup versus large-only with quality within 0.5 percentage points or equivalent task metric tolerance of the large-only fallback.
- Stop condition: Stop if the learned router cannot beat the max-softmax tradeoff or if high-confidence small-model errors keep near-lossless routing infeasible on held-out data.

## Evidence references

- Artifact root: `<local-path>/projects/difficulty-routed-local-cascade-serving-069840b52db1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
