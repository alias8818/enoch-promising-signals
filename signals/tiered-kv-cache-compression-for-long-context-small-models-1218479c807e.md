# Tiered KV-cache compression for long-context small models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiered-kv-cache-compression-for-long-context-small-models-1218479c807e`
Run ID: `tiered-kv-cache-compression-for-long-context-small-models-1218479c807e-20260607T235810306031+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/698d11b7d1cb

## What looked useful

Tiered KV precision at 37.4% of fp16 cache bytes achieved mean relative attention-output MSE 0.00424, versus 0.01482 for uniform int4 at 26.6% bytes and 0.46958 for same-byte sliding eviction. Retrieval-query error matched uniform int4, while recent-query error was much lower. Uniform int8 remained far more accurate at 51.6% bytes.

## Boundaries and scale limits

No model-level perplexity, downstream retrieval task, real prompt distribution, layer-wise accumulation, generation drift, or inference-kernel throughput was tested. Evidence is synthetic and attention-level only.

## Claim scope

In a synthetic 8192-token attention probe with 8 heads, head dimension 64, and a 30/70 old-retrieval versus recent-query mixture, a tiered recent-fp16/mid-int8/old-int4 KV cache preserved attention outputs much better than same-byte fp16 sliding-window eviction and reduced mean relative MSE versus uniform int4, mainly by protecting recent-token queries.

## Why it stopped

Stopped after a calibrated CPU-only proxy because it produced a useful mechanism signal but not direct model-level evidence; the result is not a full validation or paper-positive claim.

## Recommended next action

Run a bounded real-model follow-up that implements compressed KV in a small long-context transformer and measures perplexity, retrieval accuracy, cache memory, and decode latency against uniform int4, uniform int8, and sliding-window baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-transformer evaluation of tiered KV-cache compression
- Success threshold: Tiered KV must use no more than 40% of fp16 cache bytes, beat uniform int4 and same-byte sliding eviction on perplexity and retrieval accuracy, and stay within 10% decode latency overhead versus the closest compressed baseline.
- Stop condition: Stop if tiered KV fails to beat uniform int4 on both perplexity and retrieval accuracy at matched or lower byte budget, or if decode overhead exceeds 25% without a compensating quality gain.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-kv-cache-compression-for-long-context-small-models-1218479c807e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
