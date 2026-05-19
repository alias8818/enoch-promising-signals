# KV-Cache Offload Router for Multi-Turn Local Serving

Status: `useful_signal`
Project ID: `kv-cache-offload-router-for-multi-turn-local-serving-639041a0dcc9`
Run ID: `kv-cache-offload-router-for-multi-turn-local-serving-639041a0dcc9-20260519T033502616796+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4a1d9380147a

## What looked useful

KV offload strongly reduces recompute latency versus discard/no-cache, but the tested online EWMA router is consistently 2.18%-3.37% slower than simple LRU-offload. A future-aware oracle beats capped LRU-offload by 2.04%-7.52% mean latency and uses up to 30.45% less host KV, showing headroom only if reuse prediction improves.

## Boundaries and scale limits

No real model execution, no production serving traces, no vLLM/llama.cpp scheduler integration, no measured CUDA transfer overlap, and no validation beyond synthetic traces on one GB10-class local machine.

## Claim scope

Bounded synthetic trace-driven simulator for Llama-3-8B-class fp16 KV-cache residency in multi-turn local serving; tested an online EWMA reuse router against no-cache, LRU-discard, LRU-offload, capped LRU-offload, and an oracle upper bound.

## Why it stopped

Proxy/synthetic evidence falsified the implementable EWMA router against the strongest simple baseline; this is not a full serving validation and not paper-ready.

## Recommended next action

Stop this run as a proxy early falsification of the tested router; run one bounded follow-up that replaces EWMA admission with a learned or trace-calibrated reuse predictor and tests it against capped LRU-offload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Reuse Prediction for KV-Cache Offload Admission
- Success threshold: Beat capped LRU-offload by at least 2% mean latency or 10% host KV peak at no worse than 1% p95 latency regression, and recover at least 50% of the oracle improvement on held-out traces.
- Stop condition: Stop if the learned predictor fails to beat capped LRU-offload on held-out traces or if gains vanish under a real serving replay.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-offload-router-for-multi-turn-local-serving-639041a0dcc9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
