# Residual Channel Quantization for Agent Memory Embeddings

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-quantization-for-agent-memory-embeddings-8aca2592a25c`
Run ID: `residual-channel-quantization-for-agent-memory-embeddings-8aca2592a25c-20260619T103029273957+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/38be93e803b3

## What looked useful

Residual-channel quantization is mechanically viable and produced lower reconstruction error plus slightly higher fp32 top-1 agreement in the stress run, but simple channel int8 matched or nearly matched retrieval recall with lower complexity and closer to exact 4x compression.

## Boundaries and scale limits

Synthetic embeddings only; no real agent replay corpus, production embedding model distribution, task-level answer correctness, ANN index integration, or long-horizon memory updates were tested. Runs were CPU-only and completed in seconds.

## Claim scope

On deterministic synthetic clustered memory embeddings up to 8192 stored vectors and 2048 drifted queries, residual-channel int8 quantization preserves cosine retrieval near fp32 and reduces reconstruction error versus simple channel int8, but does not clearly improve target recall at an equal practical storage budget.

## Why it stopped

No-paper useful signal: the local synthetic evidence supports feasibility but is not direct real-agent validation and does not show a decisive recall advantage over simpler int8 baselines.

## Recommended next action

Run a bounded real-embedding follow-up using repeated agent memory traces or a public retrieval corpus, with equal-byte comparisons against fp16, simple int8, and product/residual quantization baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace equal-byte validation of residual channel quantized memory embeddings
- Success threshold: Residual-channel quantization must improve recall@1 or task answer correctness by at least 2 percentage points over the best equal-byte simple int8 baseline without more than 20 percent search-latency regression.
- Stop condition: Stop if residual-channel quantization fails to beat the best equal-byte simple int8 baseline on both retrieval recall and task correctness, or if gains disappear across seeds/confidence intervals.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-quantization-for-agent-memory-embeddings-8aca2592a25c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
