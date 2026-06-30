# Anchor-Indexed Sparse KV Retrieval for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-indexed-sparse-kv-retrieval-for-long-context-09386c4044e5`
Run ID: `anchor-indexed-sparse-kv-retrieval-for-long-context-09386c4044e5-20260525T220515546818+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b6629cf0c69c

## What looked useful

Coarse anchor-indexed sparse KV retrieval is weak in sparse needle-like retrieval: best 256-token block recall was only 5.2% to 7.4% at a 3.125% token budget and 19% to 23% at a 12.5% token budget. Finer anchors produce a concrete mechanism signal but require much higher index granularity.

## Boundaries and scale limits

No transformer integration, no language-model perplexity or QA metric, no learned anchors, no GPU kernel measurement, and no real corpus KV cache traces. Fine-grained anchor result uses an anchor count equal to 25% of token count, so compute overhead may erase the intended sparsity benefit.

## Claim scope

Synthetic long-context vector retrieval over 32,768 keys and 256 queries: compact 256-token block anchors are too lossy for dense top-16 KV target recovery, while much finer 16-token/four-subblock anchors recover 46% to 81% of dense top-16 targets at a 3.125% token candidate budget.

## Why it stopped

No-paper closure: this was a synthetic retrieval probe that early-falsified the compact coarse-anchor version, while identifying a bounded fine-grained-anchor follow-up rather than producing publication-grade model evidence.

## Recommended next action

Run a bounded transformer-level follow-up on a small long-context retrieval task comparing dense KV, coarse anchors, and fine learned/local anchors with both accuracy/perplexity and measured attention-step cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-level validation of fine-grained anchor KV routing
- Success threshold: At least 95% of dense baseline retrieval accuracy or no more than 5% perplexity degradation with at least 2x measured attention-step speedup or memory-bandwidth reduction versus dense KV at the tested context length.
- Stop condition: Stop if fine-grained anchors require scoring at least 25% as many anchors as tokens without a measured end-to-end speed or memory benefit, or if accuracy remains below 90% of dense at a 12.5% token candidate budget.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-indexed-sparse-kv-retrieval-for-long-context-09386c4044e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
