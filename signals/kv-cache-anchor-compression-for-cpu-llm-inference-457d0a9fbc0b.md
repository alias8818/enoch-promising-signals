# KV-Cache Anchor Compression for CPU LLM Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-anchor-compression-for-cpu-llm-inference-457d0a9fbc0b`
Run ID: `kv-cache-anchor-compression-for-cpu-llm-inference-457d0a9fbc0b-20260621T113523229996+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/55f35adcd078

## What looked useful

Mean-anchor compression gave median 53.56x speedup at 64x KV length reduction with mean relative L2 error 0.000314 on block-redundant synthetic KV; hybrid recent-window anchors gave median 24.75x speedup with mean relative L2 error 0.000127 on recent-sensitive redundant KV. Random KV remained high-error, with mean-anchor relative L2 error 0.7983.

## Boundaries and scale limits

Tested only NumPy fp32 synthetic KV caches up to 16384 tokens, 8 heads, 64 head dimension, one CPU process/thread, and no real model, tokenizer, perplexity, answer-quality, quantized-KV, or serving-runtime integration.

## Claim scope

Synthetic CPU decode-attention proxy: block-mean KV anchors with softmax multiplicity preserve output on locally redundant old KV blocks while reducing attention length and latency; the method fails on nonredundant/random KV.

## Why it stopped

Proxy-only mixed result: mechanism supported under redundant synthetic KV, falsified as a general method under random/nonredundant KV, and not sufficient for a paper or CPU LLM serving claim.

## Recommended next action

Run a bounded real-model CPU follow-up that captures per-layer KV tensors from a small transformer or llama.cpp-class runtime and compares latency, memory, perplexity, and decode output drift for weighted mean anchors versus full KV.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU KV anchor compression validation
- Success threshold: At least 1.5x CPU decode-attention speedup and 2x KV memory reduction at 4096 or more tokens while keeping next-token KL or perplexity drift below 1 percent on the bounded prompt set.
- Stop condition: Stop if real-model KV shows mean output drift above 5 percent or token changes on more than 10 percent of tested decode steps at block sizes that provide at least 2x memory reduction.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-anchor-compression-for-cpu-llm-inference-457d0a9fbc0b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
