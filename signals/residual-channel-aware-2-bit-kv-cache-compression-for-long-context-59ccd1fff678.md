# Residual-Channel-Aware 2-bit KV Cache Compression for Long Context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-channel-aware-2-bit-kv-cache-compression-for-long-context-59ccd1fff678`
Run ID: `residual-channel-aware-2-bit-kv-cache-compression-for-long-context-59ccd1fff678-20260524T161925398195+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5c558e37ba4a

## What looked useful

Across two prompt-sampling seeds and 192 layer/sample/context comparisons, residual-aware average-2-bit allocation reduced attention relative MSE by 37.7% mean / 40.1% median versus uniform 2-bit and won every comparison. Magnitude-aware mixed allocation was weaker at 20.6% mean reduction and 83.3% win rate; random mixed was near neutral.

## Boundaries and scale limits

No end-to-end perplexity, retrieval, serving latency, packed-kernel bandwidth, larger model, or context beyond GPT-2's 1024-token window was tested.

## Claim scope

Layer-local distilgpt2 activation probe: residual/sensitivity-ranked average-2-bit KV channel allocation reduces causal attention-output distortion versus uniform 2-bit quantization for contexts from 128 to 768 tokens.

## Why it stopped

This run produced useful direct layer-local evidence but not enough end-to-end or hardware evidence for a paper; closure is no-paper useful signal rather than full validation.

## Recommended next action

Implement a bounded end-to-end GPT-2/OPT-style cache wrapper using the same residual-aware average-2-bit allocation, then compare logit drift/perplexity and decode throughput against uniform 2-bit on 512-1024 token contexts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end residual-aware average-2-bit KV cache decoding probe
- Success threshold: At least 20% lower logit drift or perplexity degradation than uniform 2-bit at equal average bit budget, with no worse than 10% decode throughput regression in the bounded implementation.
- Stop condition: Stop if residual-aware allocation fails to beat uniform 2-bit by 20% on logit/perplexity drift, if benefits disappear across two seeds, or if implementation overhead removes practical cache benefit.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-aware-2-bit-kv-cache-compression-for-long-context-59ccd1fff678`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
