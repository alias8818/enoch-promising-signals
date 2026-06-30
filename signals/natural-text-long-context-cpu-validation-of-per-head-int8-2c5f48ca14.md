# Natural-text long-context CPU validation of per-head int8 KV cache

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `natural-text-long-context-cpu-validation-of-per-head-int8-2c5f48ca14`
Run ID: `natural-text-long-context-cpu-validation-of-per-head-int8-2c5f48ca14-20260605T095744012656+0000`

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
- Parent run decision: Real-model CPU validation of per-head int8 KV cache: enoch://control-plane/projects/real-model-cpu-validation-of-per-head-int8-kv-cache-6e23fdfd95/runs/real-model-cpu-validation-of-per-head-int8-kv-cache-6e23fdfd95-20260605T051944433397+0000

## What looked useful

Medium grid produced 162 checkpointed rows. Per-head int8 averaged 0.01865 context rel-L2 and 0.01111 attention-projection rel-L2 versus per-tensor int8 at 0.02778 and 0.01637, a 32.9% and 32.1% reduction respectively. Mean NLL delta stayed near zero and top-1 match was 1.0 for both int8 modes. Per-head int4 control degraded strongly, with 13.2x higher context rel-L2 than per-head int8 and a top-1 mismatch.

## Boundaries and scale limits

Single small GPT-2-family model, two-source natural-text corpus mixture, three fixed seeds, context lengths below 1024, and one-layer-at-a-time replay. This is not all-layer persistent KV-cache autoregressive serving, not a throughput/RSS benchmark, and not validated on 7B-class or million-token settings.

## Claim scope

On distilgpt2 natural-text windows of 256, 512, and 768 tokens, injecting one quantized attention layer at a time, symmetric per-head int8 KV scaling reduces local attention approximation error versus per-tensor int8 while preserving downstream next-token top-1 and near-zero NLL/logit drift.

## Why it stopped

Tier 2 bounded mechanism evidence was obtained, but it is one-layer replay evidence rather than direct full-cache serving validation, so it should remain a no-paper useful signal.

## Recommended next action

Run a bounded deepen validation with full all-layer KV-cache quantization during autoregressive decode, measuring NLL/perplexity, top-k drift, decode latency, and RSS versus fp32/fp16 cache on at least two small-to-medium pretrained models.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: All-layer autoregressive CPU decode validation of per-head int8 KV cache
- Success threshold: Per-head int8 should reduce KV memory by at least 45% versus fp16/fp32 cache, keep mean NLL delta below 0.01 and top-1 mismatch below 1% versus the real fp32/fp16 decode baseline, and beat per-tensor int8 by at least 20% on local KV/attention error or downstream drift.
- Stop condition: Stop if per-head int8 all-layer decode causes mean NLL delta above 0.02, top-1 mismatch above 3%, or fails to improve materially over per-tensor int8 on both quality and memory/latency metrics.

## Evidence references

- Artifact root: `<local-path>/projects/natural-text-long-context-cpu-validation-of-per-head-int8-2c5f48ca14`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
