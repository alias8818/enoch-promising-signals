# Exact-Anchor KV Cache Compression via Tiered Summarization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-cache-compression-via-tiered-summarization-32a35f931905`
Run ID: `exact-anchor-kv-cache-compression-via-tiered-summarization-32a35f931905-20260518T193950545527+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/13ecdec67f00

## What looked useful

Exact-anchor tiering preserved anchor argmax accuracy at 1.0 for 4096-token b16 and 0.9987 for b32, while uniform and random-anchor controls were near zero. Log-count correction was critical: without it, 4096-token b16 relative output MSE worsened from 0.7080 to 4.2304 despite perfect anchor argmax. Overall output fidelity remained mixed and sometimes worse than recent-window controls.

## Boundaries and scale limits

Tested synthetic tensors at sequence lengths 1024, 4096, and 16384 on one GB10 with PyTorch CUDA; no pretrained model, no real KV-cache intervention, no perplexity, no generation, and oracle synthetic anchors.

## Claim scope

Synthetic clustered-KV attention proxy only: exact true anchors plus log-counted tier summaries preserve anchor-target retrieval under 12x-20x compression, but do not establish practical LLM KV-cache quality.

## Why it stopped

This run produced only synthetic proxy evidence with mixed output-fidelity results, so it is no-paper useful signal rather than full validation.

## Recommended next action

Run a bounded direct pretrained-LM KV-cache intervention on a small causal model, measuring loss/perplexity and needle retrieval against sliding-window, quantized KV, and pooling baselines before reconsidering paper readiness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM Direct KV Intervention for Exact Anchors plus Log-Count Summaries
- Success threshold: At 8x or greater KV-slot compression, improve needle retrieval by at least 20 percentage points over sliding-window or uniform pooling at matched budget while keeping perplexity/loss degradation within 10% of the best compressed baseline.
- Stop condition: Stop if exact-anchor summarized KV fails to beat both sliding-window and uniform/random-anchor controls on either retrieval or loss at matched budget in two context lengths.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-cache-compression-via-tiered-summarization-32a35f931905`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
