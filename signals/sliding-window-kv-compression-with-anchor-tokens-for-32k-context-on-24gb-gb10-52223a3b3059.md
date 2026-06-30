# Sliding-Window KV Compression with Anchor Tokens for 32k Context on 24GB GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sliding-window-kv-compression-with-anchor-tokens-for-32k-context-on-24gb-gb10-52223a3b3059`
Run ID: `sliding-window-kv-compression-with-anchor-tokens-for-32k-context-on-24gb-gb10-52223a3b3059-20260629T043704810519+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1af9aa073b79

## What looked useful

The memory/latency motivation is credible and the anchor mechanism works when old context is redundant and multiplicity-corrected, but static anchor compression is insufficient for rare-token long-context retrieval. Future work should combine anchors with salient-token retention or trained/query-aware anchor construction.

## Boundaries and scale limits

No trained LLM was evaluated, no perplexity or downstream task score was measured, and the benchmark uses synthetic q/k/v tensors rather than a full model. The results do not validate learned anchor tokens, production kernels, batching behavior, or full 24GB deployment with model weights and real prompts.

## Claim scope

On a GB10 CUDA proxy benchmark at 32k context, a 2048-token sliding window plus one anchor per 128 old tokens reduces retained KV slots from 32768 to 2288 and cuts decode-attention proxy latency by roughly 10-12x. Block-mean anchors with a log(block_size) attention correction preserve full-attention outputs on redundant block-repeated synthetic context, but static anchors fail rare high-logit old-token recall.

## Why it stopped

Stopped after a direct local proxy produced a mixed useful signal but not paper-ready evidence: memory and latency improve, redundant-context fidelity is strong with corrected anchors, and rare-token recall is an early falsification for static anchors.

## Recommended next action

Run a bounded trained small-transformer follow-up with explicit log-count anchors plus salient-token retention, measuring perplexity and rare-needle accuracy against full KV and sliding-window baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train small anchor-cache transformer with salient-token retention
- Success threshold: At 32k context, anchor-plus-salient-retention should keep rare-needle retrieval accuracy at least 90% of full KV, keep redundant-summary loss within 5% of full KV, and retain at least an 8x KV-slot reduction versus full cache.
- Stop condition: Stop if the trained anchor-plus-salient method remains below 60% of full-KV rare-needle accuracy after a matched small-model training budget, or if its KV-slot reduction falls below 4x.

## Evidence references

- Artifact root: `<local-path>/projects/sliding-window-kv-compression-with-anchor-tokens-for-32k-context-on-24gb-gb10-52223a3b3059`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
