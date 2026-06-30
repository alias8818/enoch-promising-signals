# KV-Cache Aware Cascade Fallback

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `kv-cache-aware-cascade-fallback-4733bb6f795f`
Run ID: `kv-cache-aware-cascade-fallback-4733bb6f795f-20260523T160135934610+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/72c532193db4

## What looked useful

Naive KV-cache-aware cascade fallback is compute-negative in this bounded probe because preserving a large-model cache requires paying large-model work before fallback; stateless fallback won all 15 calibrated scenarios and all 81 break-even sweep scenarios.

## Boundaries and scale limits

Synthetic transformer-like kernels and Monte Carlo policy simulation only; no real LLM quality, confidence calibration, serving scheduler, batching, PagedAttention, or trained cross-model KV projection was evaluated.

## Claim scope

On a GB10 toy transformer proxy with prompt lengths 128-1024, generation length 128, and fallback probabilities 0.001-0.05 per token, straightforward large-model KV preservation via shadowing or periodic checkpointing did not reduce expected latency versus stateless fallback.

## Why it stopped

Moderate proxy evidence falsified the straightforward implementation path: KV-aware shadow/checkpoint policies produced no latency wins and up to 1.397x slowdown versus stateless fallback in the calibrated grid.

## Recommended next action

Stop this naive KV-preservation path as no-paper evidence; the only bounded next test worth running is a separate cross-model KV projection/reuse probe that avoids shadow-running the large model.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Cross-Model KV Projection for Cascade Fallback
- Success threshold: At least 10% lower fallback latency than stateless prefill at matched output quality, with next-token KL divergence or task metric degradation within a predeclared tolerance.
- Stop condition: Stop if projection quality is unstable across prompt domains or if projection cost plus correction work is not at least 10% faster than stateless prefill.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-aware-cascade-fallback-4733bb6f795f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
