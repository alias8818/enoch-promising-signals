# Sparse Anchor Attention via N-Grams

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sparse-anchor-attention-via-n-grams-010b635aff5f`
Run ID: `sparse-anchor-attention-via-n-grams-010b635aff5f-20260604T101514832957+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/2322373383a0

## What looked useful

For 2-gram keys with local window 32, n-gram anchors matched dense retrieval accuracy at 0.997 on 32,000 long-gap retrieval positions while using 0.2389 dense-edge density; local-only reached 0.1703. A grid showed unigram anchors are ambiguous, while 2-gram and 3-gram anchors recover dense-level retrieval on this probe.

## Boundaries and scale limits

Proxy-only evidence: no trained transformer, no real language modeling perplexity, no pretrained model evaluation, no sparse kernel implementation, and no end-to-end latency measurement. Sequence length was 256 with synthetic facts and CPU-only deterministic oracle retrieval.

## Claim scope

On a deterministic synthetic repeated n-gram key/value retrieval probe, causal local-plus-n-gram-anchor masks expose the same retrieval evidence as dense attention for 2-gram and 3-gram keys while using substantially fewer causal edges.

## Why it stopped

This run produced a useful proxy mechanism signal but not direct model-training, perplexity, or runtime evidence; it is not paper-ready.

## Recommended next action

Run a bounded trained-transformer follow-up on the same synthetic retrieval distribution to verify that a learned model can use the exposed anchor edges, then only move to a small real-token LM benchmark if dense-level retrieval persists.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer Validation of N-Gram Anchor Sparse Attention
- Success threshold: Anchor transformer retrieval accuracy within 2 percentage points of dense and at least 20 percentage points above local-only, with <= 0.30 dense-edge density on held-out synthetic examples.
- Stop condition: Stop as negative if the anchor transformer fails to beat local-only by 10 percentage points after a calibrated short training run or if realized mask overhead erases the intended sparsity benefit in the tiny implementation.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-anchor-attention-via-n-grams-010b635aff5f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
