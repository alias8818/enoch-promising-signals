# Sliding-Window KV Reset for Long Context on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sliding-window-kv-reset-for-long-context-on-cpu-08c4b661c95b`
Run ID: `sliding-window-kv-reset-for-long-context-on-cpu-08c4b661c95b-20260619T074828956263+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8977943e21b7

## What looked useful

Fixed sliding-window KV eviction produced the CPU/cache benefit; periodic reset on top of sliding-window added only about 1.04x-1.05x throughput versus sliding-window while reducing recall by up to 0.0502 absolute accuracy at length 4096 due to reset-boundary losses.

## Boundaries and scale limits

No trained transformer, perplexity, tokenizer, production KV-cache runtime, or 7B+ serving was tested; evidence is mechanism-level and local CPU-only.

## Claim scope

Bounded NumPy CPU proxy for autoregressive attention cost and associative-recall retention at sequence lengths 512-4096 with d_model=64, window=256, reset_period=512.

## Why it stopped

Proxy/local evidence supports sliding-window eviction but does not support periodic KV reset as a general paper-worthy mechanism; reset mainly introduces boundary recall loss with little added throughput.

## Recommended next action

Stop this no-paper line unless there is a concrete production implementation reason to test periodic reset against sliding-window-only in a trained CPU inference engine.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained CPU inference comparison of sliding-window eviction versus periodic reset
- Success threshold: Periodic reset must improve end-to-end CPU throughput or p95 latency by at least 10% versus sliding-window-only while keeping quality within 1% relative degradation and showing no reset-boundary failure spike.
- Stop condition: Stop if periodic reset gives less than 5% latency/throughput gain, increases boundary failures, or degrades quality by more than 1% relative to sliding-window-only.

## Evidence references

- Artifact root: `<local-path>/projects/sliding-window-kv-reset-for-long-context-on-cpu-08c4b661c95b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
