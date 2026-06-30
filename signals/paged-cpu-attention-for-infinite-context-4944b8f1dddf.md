# Paged CPU Attention for Infinite Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `paged-cpu-attention-for-infinite-context-4944b8f1dddf`
Run ID: `paged-cpu-attention-for-infinite-context-4944b8f1dddf-20260601T100040816682+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1969124219c8

## What looked useful

Paged CPU attention is mechanically viable as an exact online-softmax scan over K/V pages, but it is slower than dense in-RAM attention at tested small contexts and does not by itself justify an infinite-context paper claim.

## Boundaries and scale limits

Synthetic single-query benchmark only; no full transformer, multi-head/layer KV cache, batching, concurrency, GPU baseline, eviction policy, cold storage behavior, or end-to-end decode latency. Per-token work remains linear in context length.

## Claim scope

Exact single-query CPU paged attention over synthetic float32 K/V arrays is numerically equivalent to dense attention on small/medium contexts and can scan a 1,048,576-token, dim-64, 512 MiB K/V cache in 0.483 s on this local CPU worker.

## Why it stopped

Proxy/synthetic benchmark supports the core mechanism but does not validate the broader infinite-context serving claim.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should integrate real model KV tensors and measure end-to-end decode latency against a standard KV-cache/offload baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU paged KV decode benchmark
- Success threshold: At 256k or larger context, paged CPU KV attention must produce numerically matching outputs and keep median per-token latency within 3x the strongest local baseline while demonstrating lower resident-memory pressure or larger context capacity.
- Stop condition: Stop if end-to-end per-token latency scales worse than the single-query scan suggests, if numerical agreement fails, or if memory savings disappear once full model-layer KV tensors are included.

## Evidence references

- Artifact root: `<local-path>/projects/paged-cpu-attention-for-infinite-context-4944b8f1dddf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
