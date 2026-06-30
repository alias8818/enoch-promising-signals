# Exact-Anchor KV Sketching for CPU Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-sketching-for-cpu-long-context-d47999dc6a1e`
Run ID: `exact-anchor-kv-sketching-for-cpu-long-context-d47999dc6a1e-20260531T182443590293+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4e31330fce0a

## What looked useful

Exact anchors plus a recent window preserve synthetic anchor/recent retrieval under large KV compression. Count-aware bucket sketches materially improve non-anchor readout fidelity versus exact anchors alone, reaching 0.922 median output cosine at 7.53x compression on 4k-16k tests and 0.816 mixed-query median cosine at 45.18x compression on the 32k-65k probe, while broad/random queries remain only moderate.

## Boundaries and scale limits

No real transformer decoder, learned anchor policy, perplexity, downstream task metric, production CPU kernel, or 7B+ model validation was run. Evidence is bounded to NumPy synthetic KV distributions.

## Claim scope

Synthetic CPU softmax-attention KV-cache proxy with exact anchor tokens, exact recent window, and deterministic bucket summaries at 4k-65k context lengths.

## Why it stopped

No-paper closure: this run produced a useful synthetic mechanism signal, but it is a proxy validation rather than direct model-serving evidence.

## Recommended next action

Run a bounded model-backed deepen test by inserting anchor_count_sketch into a small autoregressive transformer decode loop and measuring perplexity, needle retrieval, CPU decode speed, and KV memory against full KV and standard eviction baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-backed exact-anchor count-sketch KV decoding
- Success threshold: At least 4x KV memory reduction with no more than 2% relative perplexity degradation, at least 95% of full-KV needle retrieval accuracy, and a measured CPU decode speedup over full KV at matched context length.
- Stop condition: Stop if perplexity degradation exceeds 5% relative or needle retrieval falls below 90% of full KV at 4x KV reduction after tuning only anchor count, recent window, and bucket count.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-sketching-for-cpu-long-context-d47999dc6a1e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
