# Residual KV-Cache: Critical-Head FP16 with Compressed Contextors

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-kv-cache-critical-head-fp16-with-compressed-contextors-fe2b6fedf9f4`
Run ID: `residual-kv-cache-critical-head-fp16-with-compressed-contextors-fe2b6fedf9f4-20260603T192513821459+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/682b9ac9b3c0

## What looked useful

Across five calibrated GB10 CUDA seeds at a 34.375% cache ratio, critical-head exact KV reduced MSE by 54.3% versus uniform block compression and 37.2% versus random exact-head retention, with mean relative RMSE 0.1463 versus 0.2165 and 0.1845 respectively.

## Boundaries and scale limits

No real transformer perplexity, generation quality, or serving throughput was tested; traces are synthetic, contextors are simple block means, sequence length was 4096, head count was 16, and cache/runtime overheads from an integrated paged KV-cache implementation were not measured.

## Claim scope

On synthetic attention-shaped GPU traces with heterogeneous per-head compressibility, retaining the 25% highest calibration-error heads as exact FP16 KV and compressing the remaining heads into block-mean contextors reduced held-out attention-output error versus uniform compression and random exact-head retention at the same cache ratio.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic mechanism probe, not a full validation of real-model quality or serving performance.

## Recommended next action

Run a bounded direct GPT-2-small-class decode/perplexity experiment that applies calibration-selected exact heads plus compressed contextors inside a real transformer KV-cache and compares quality and tokens/sec against full KV, uniform compression, and random exact-head controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GPT-2-Small Critical-Head Residual KV Cache Validation
- Success threshold: At the same cache ratio, critical-head residual KV must reduce perplexity degradation or attention-output error by at least 25% versus random exact-head retention while preserving decode throughput within 10% of the compressed baseline.
- Stop condition: Stop if critical-head retention fails to beat random exact-head retention on held-out text quality metrics or if implementation overhead removes the intended cache/throughput benefit.

## Evidence references

- Artifact root: `<local-path>/projects/residual-kv-cache-critical-head-fp16-with-compressed-contextors-fe2b6fedf9f4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
