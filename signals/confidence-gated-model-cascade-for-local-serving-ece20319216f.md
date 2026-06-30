# Confidence-Gated Model Cascade for Local Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-gated-model-cascade-for-local-serving-ece20319216f`
Run ID: `confidence-gated-model-cascade-for-local-serving-ece20319216f-20260621T231818921198+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/49b19478d320

## What looked useful

Confidence gating is mechanically viable in a bounded proxy and can sharply reduce fallback invocations, but actual local-serving latency savings depend on hardware/runtime overhead and need direct validation on real model pairs.

## Boundaries and scale limits

Synthetic tabular classification only; not tested on real LLMs, tokenization/runtime overhead, production prompts, queueing, concurrent serving, memory pressure, or real distribution drift. Tiny-model GPU latency was noisy and exceeded the 70% latency-ratio target in one repeat.

## Claim scope

On a generated multiclass local-serving proxy with three harder synthetic seeds, a calibrated confidence gate preserved large-model accuracy within 1 percentage point while routing only about 3% of clean and 9% of shifted requests to the large model; measured GPU latency improved on average but not in every repeat.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy-only and the measured latency win was not robust across all repeats, even though the routing/accuracy mechanism was supported.

## Recommended next action

Run a bounded direct local-serving follow-up with two real local models, representative requests, calibrated gate thresholds, and end-to-end latency including runtime and batching overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real local-model confidence cascade with end-to-end serving latency
- Success threshold: Quality no worse than fallback minus 1 percentage point and p50 end-to-end latency at least 25% lower than always-fallback on both clean and shifted subsets.
- Stop condition: Stop if no threshold meets the quality bound, or if feasible thresholds reduce large-model calls but fail to reduce measured end-to-end p50 latency by at least 10%.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-model-cascade-for-local-serving-ece20319216f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
