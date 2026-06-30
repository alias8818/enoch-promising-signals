# Anchor-Pinned KV with Compressed Tail

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-pinned-kv-with-compressed-tail-08ed7351f86c`
Run ID: `anchor-pinned-kv-with-compressed-tail-08ed7351f86c-20260620T032346445492+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a49c4c28f6c4

## What looked useful

Weighted anchor-pinned KV compression maintained 99.9-100% target top-1 retrieval for anchor targets across 2048-8192 token synthetic contexts, while comparable weighted block-mean compression reached only 14.1-31.2%. The same method failed on non-anchor old-token targets at about 0.3-1.7%, so the mechanism depends on reliable anchor placement or promotion of important tokens.

## Boundaries and scale limits

No trained language model, no real-text perplexity or QA evaluation, no learned/semantic anchor placement, no optimized serving kernel, and no multi-layer/multi-head decode integration. Latency metrics include Python cache construction overhead and are not serving-speed evidence.

## Claim scope

Synthetic single-head attention retrieval on random KV tensors with periodic exact anchors, compressed non-anchor tail blocks, and exact recent-window KV. Weighted anchor-pinned compression preserved anchor-aligned old-token retrieval at 5.17x-9.35x effective-cache-record compression.

## Why it stopped

Closed as no-paper useful signal: this was a direct synthetic attention-quality probe, not full model validation; it supports the anchor-aligned mechanism and falsifies arbitrary old-token retrieval under simple tail compression.

## Recommended next action

Run a bounded transformer-level follow-up that implements weighted anchor-pinned KV during decode on a small causal model and evaluates real-text perplexity plus retrieval accuracy against full KV, sliding-window, and block-compressed controls at matched memory budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer decode validation for weighted anchor-pinned KV compression
- Success threshold: At matched KV memory budget, recover at least 95% of full-KV anchor-aligned retrieval accuracy and keep perplexity degradation below 5% relative to full KV, while outperforming sliding-window and block-mean controls.
- Stop condition: Stop if anchor-pinned KV does not outperform both sliding-window and block-mean controls on real-text retrieval/perplexity at matched memory, or if the implementation requires nonlocal model changes that invalidate a KV-cache-only claim.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-pinned-kv-with-compressed-tail-08ed7351f86c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
