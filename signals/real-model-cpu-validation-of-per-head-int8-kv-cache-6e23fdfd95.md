# Real-model CPU validation of per-head int8 KV cache

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-model-cpu-validation-of-per-head-int8-kv-cache-6e23fdfd95`
Run ID: `real-model-cpu-validation-of-per-head-int8-kv-cache-6e23fdfd95-20260605T051944433397+0000`

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

- Parent run decision: Per-head int8 KV-cache for long CPU inference: enoch://control-plane/projects/per-head-int8-kv-cache-for-long-cpu-inference-cfb7269fde0d/runs/per-head-int8-kv-cache-for-long-cpu-inference-cfb7269fde0d-20260604T223104735130+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0b5705bd13e5
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e621841cbccf

## What looked useful

Real pretrained GPT-2 small weights were evaluated with an actual incremental KV cache. Per-head int8 K/V caching caused low logit drift and no top-k decision changes across 50 tested positions, supporting the correctness mechanism but not a paper-ready performance or robustness claim.

## Boundaries and scale limits

Only GPT-2 small, three fixed prompt token sequences, deterministic continuation IDs, short contexts, batch size 1, and a minimal NumPy implementation were tested. No natural-text corpus perplexity, long-context robustness, optimized int8 CPU kernel, production memory allocation, or larger-model evidence was produced.

## Claim scope

On GPT-2 small with 50 short CPU incremental decoding positions, per-token/per-head symmetric int8 K and V caches with separate scales preserved FP32-cache top-1 predictions and top-5 sets while producing mean KL(fp32||int8) 0.000143684 and max KL 0.00121328.

## Why it stopped

Tier 1 direct test completed and produced useful no-paper mechanism evidence; broader validation remains untested.

## Recommended next action

Run a bounded tokenizer-driven natural-text deepen test with longer contexts and an optimized or semi-optimized int8-cache attention path before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-text long-context CPU validation of per-head int8 KV cache
- Success threshold: Mean KL(fp32||int8) <= 0.001, top-1 match rate >= 0.98, top-5 overlap >= 0.95, and no prompt family with systematic divergence above KL 0.01.
- Stop condition: Stop early as unsupported if top-1 match falls below 0.95, mean KL exceeds 0.005, or any repeatable prompt class shows severe distribution drift unexplained by implementation error.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-cpu-validation-of-per-head-int8-kv-cache-6e23fdfd95`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
