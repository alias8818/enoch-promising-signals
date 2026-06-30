# Tiny Router Cascade for Local CPU Inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-router-cascade-for-local-cpu-inference-eab320b675c4`
Run ID: `tiny-router-cascade-for-local-cpu-inference-eab320b675c4-20260604T073219408888+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4f69b55a54be

## What looked useful

The mechanism is locally supported: routing overhead did not erase savings, only 22.98% of test examples reached the large model, and measured cascade speedup was 2.105x with a 0.34 percentage-point test accuracy drop.

## Boundaries and scale limits

Single dataset, single seed, toy image classifiers, NumPy/Python batch-1 inference, no LLM token generation, no quantized production runtime, no multi-domain robustness or calibration study.

## Claim scope

On MNIST with small NumPy CPU classifiers, a confidence-margin tiny/medium/large cascade reduced batch-1 CPU inference latency from 0.1853 ms/sample for the large model to 0.0880 ms/sample while retaining 95.76% test accuracy versus 96.10% for the large model.

## Why it stopped

The result is positive for the small mechanism test but too toy and narrow for publication-grade claims about local CPU language-model inference.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should repeat the cascade on a CPU text-classification or tiny language-model task with a real local inference runtime.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU Text Router Cascade With Real Local Runtime
- Success threshold: At least 1.5x measured batch-1 CPU speedup versus always-large with no more than 1 percentage-point accuracy or task-score loss on held-out text examples.
- Stop condition: Stop if router overhead plus escalation yields less than 1.2x speedup or if matching the quality threshold sends more than 70% of examples to the largest model.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-router-cascade-for-local-cpu-inference-eab320b675c4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
