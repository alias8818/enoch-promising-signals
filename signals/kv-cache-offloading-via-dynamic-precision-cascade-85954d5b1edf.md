# KV-Cache Offloading via Dynamic Precision Cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-offloading-via-dynamic-precision-cascade-85954d5b1edf`
Run ID: `kv-cache-offloading-via-dynamic-precision-cascade-85954d5b1edf-20260529T155908768770+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1e8d7bf3cbbd

## What looked useful

A three-tier KV precision cascade is a plausible compression/error tradeoff, but the tested dynamic salience rule is not enough by itself to justify a paper claim. Future work should compare against recency and all-int8 controls in a real inference stack.

## Boundaries and scale limits

No real transformer serving integration, packed int4 kernel, offload transfer path, perplexity measurement, or production long-context workload was tested. Timing reflects a PyTorch microbenchmark implementation, not an optimized inference backend.

## Claim scope

Synthetic GPU attention benchmark over sequence lengths 512, 1024, and 2048 with token-wise KV quantization policies. Precision cascades reduced modeled KV bytes to about one third of FP16 and improved attention-output error versus all-int4, but dynamic attention-EMA precision assignment did not clearly outperform a simpler recency cascade.

## Why it stopped

Proxy/local benchmark only, and the dynamic precision cascade did not produce a strong advantage over simpler controls.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement the best recency and dynamic policies in a small real transformer inference path and measure perplexity plus tokens/s.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV precision cascade validation on small long-context inference
- Success threshold: At least 50% KV byte reduction versus FP16, less than 1% perplexity degradation, and a statistically clear improvement over simple recency at matched byte budget.
- Stop condition: Stop if dynamic salience fails to beat recency at matched byte budget or if quality loss exceeds 1% before achieving 50% KV byte reduction.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-offloading-via-dynamic-precision-cascade-85954d5b1edf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
