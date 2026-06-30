# Local cascade router: int4 vs fp16 model split on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-cascade-router-int4-vs-fp16-model-split-on-cpu-2dbc77c6454e`
Run ID: `local-cascade-router-int4-vs-fp16-model-split-on-cpu-2dbc77c6454e-20260619T094342875961+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2aca5cca4c60

## What looked useful

The cascade mechanism is locally useful, but the standalone INT4 first stage was slower than the same small FP16 linear model in this NumPy implementation despite using fewer weight bytes. The observed gain came from avoiding FP16 expert calls, not from proving INT4 CPU math is faster.

## Boundaries and scale limits

Synthetic distilled linear router and synthetic FP16 MLP expert only; no real LLM, tokenizer, public task benchmark, optimized INT4 CPU kernel, or generation workload. Quality metric is agreement with the synthetic FP16 expert, not real task accuracy.

## Claim scope

On a bounded synthetic CPU proxy, a confidence-routed small weight-only INT4 first stage can reduce average latency versus an all-FP16 expert while preserving high agreement with that FP16 expert when enough uncertain cases are routed. Across three seeds, 75% expert routing preserved at least 99.52% expert agreement with at least 1.34x speedup; 50% routing preserved at least 97.36% agreement with at least 1.99x speedup.

## Why it stopped

No-paper closure: this is a synthetic proxy useful signal, not full validation; it also found a local negative kernel-speed signal for the naive INT4 path.

## Recommended next action

Run a bounded direct follow-up with a real CPU inference backend that supports optimized INT4 and FP16 variants, measuring latency, memory, and task quality on a small public eval set.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU backend cascade router with optimized INT4 and FP16 model variants
- Success threshold: At a predeclared threshold, cascade latency is at least 1.25x faster than all-FP16 expert inference while preserving at least 99% of the all-FP16 task metric and showing the INT4 first stage is not slower than an equivalent small FP16 first stage.
- Stop condition: Stop as negative if optimized INT4 first-stage latency is not faster than the equivalent small FP16 first stage, or if no threshold reaches both 1.25x latency speedup and 99% task-quality retention.

## Evidence references

- Artifact root: `<local-path>/projects/local-cascade-router-int4-vs-fp16-model-split-on-cpu-2dbc77c6454e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
