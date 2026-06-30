# Per-Head INT8 KV Cache Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-head-int8-kv-cache-compression-a31bbb97940f`
Run ID: `per-head-int8-kv-cache-compression-a31bbb97940f-20260603T233644541501+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/71331c498ab7

## What looked useful

Per-head INT8 scaling improved over a single global INT8 scale, especially with heterogeneous head ranges, but missed the predeclared <1% median relative L2 attention-output error threshold and failed badly under within-head outliers. Per-head-channel scaling reduced outlier-case error substantially with small metadata overhead, suggesting future work should use finer granularity or clipping rather than static per-head scale alone.

## Boundaries and scale limits

No pretrained transformer activations, downstream perplexity, generation quality, optimized INT8 serving kernel, long-context production trace, or GPU/GB10 throughput validation was run. Results are numerical proxy evidence, not full model validation.

## Claim scope

Synthetic NumPy attention-output benchmark for INT8 quantize/dequantize of cached K/V tensors at batch=2, heads=16, context=512, query block=16, head_dim=64, 12 seeds, comparing global, per-head, per-head-channel, and per-token-head scales across balanced, heterogeneous-head, outlier, and combined activation regimes.

## Why it stopped

Bounded synthetic/proxy test showed per-head INT8 has a mechanism benefit over global scaling but failed the local success threshold and exposed a clear within-head outlier failure mode; this is not full validation or paper-ready evidence.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded action is to collect real pretrained-transformer KV activation traces and rerun the same per-head versus per-channel/clipped INT8 comparison with downstream perplexity checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Activation KV Trace Test for INT8 Scale Granularity
- Success threshold: Per-head-channel or clipped INT8 achieves median attention-output relative L2 below 1% and next-token loss within 0.01 of FP16 while preserving at least 1.9x storage reduction versus FP16; static per-head alone must either meet the same threshold or be rejected as insufficient.
- Stop condition: Stop if real activation traces show static per-head INT8 median attention-output relative L2 above 1% or next-token loss degradation above 0.01 without a finer-grained/clipped control recovering the error at similar storage cost.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-int8-kv-cache-compression-a31bbb97940f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
