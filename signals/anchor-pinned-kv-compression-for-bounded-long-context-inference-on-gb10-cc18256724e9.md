# Anchor-Pinned KV Compression for Bounded Long-Context Inference on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-pinned-kv-compression-for-bounded-long-context-inference-on-gb10-cc18256724e9`
Run ID: `anchor-pinned-kv-compression-for-bounded-long-context-inference-on-gb10-cc18256724e9-20260619T162350278272+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3b455a7205b0

## What looked useful

Across three 32k-token synthetic GPU benchmark seeds, anchor-pinned chunk compression kept 669/32768 KV entries (2.04% estimated BF16 KV memory) and preserved anchor exact-top1 retrieval at 100%, while chunk-mean without pinned anchors kept 510 entries (1.56%) but had 0% anchor exact-top1. Both methods failed middle non-anchor exact retrieval, so the signal supports exact anchor preservation, not general middle-context recovery.

## Boundaries and scale limits

No pretrained LLM, no tokenizer/doc-task benchmark, no multi-layer cache policy, no generation quality metrics, and no integration with paged-attention serving kernels. Evidence is direct for attention-level anchor retention but only a proxy for end-to-end long-context inference quality.

## Claim scope

Synthetic KV-level GB10 attention benchmark at 32k context, 8 heads, 64 head dimension, 384 query probes, comparing full KV, recent-only, chunk-mean compression, and anchor-pinned chunk-mean compression.

## Why it stopped

No-paper useful signal: the local evidence is a synthetic KV-level mechanism test, not publication-grade end-to-end long-context inference validation.

## Recommended next action

Run a bounded real-model follow-up on a small open LLM with document/needle prompts where anchor positions are semantically meaningful, comparing perplexity or retrieval answer accuracy against StreamingLLM-style sink+recent and SnapKV-like selection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model anchor-pinned KV compression on needle/document prompts
- Success threshold: At the same KV entry budget within +/-10%, anchor-pinned compression improves anchor-addressed retrieval accuracy by at least 20 percentage points over chunk compression and stays within 5 percentage points of full KV on anchor-target prompts.
- Stop condition: Stop if anchor-pinned compression does not beat same-budget chunk compression on anchor-target retrieval or causes unacceptable loss on recent-token prompts.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-pinned-kv-compression-for-bounded-long-context-inference-on-gb10-cc18256724e9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
