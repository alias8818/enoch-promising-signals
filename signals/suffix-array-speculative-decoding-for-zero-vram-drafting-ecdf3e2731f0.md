# Suffix-Array Speculative Decoding for Zero-VRAM Drafting

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `suffix-array-speculative-decoding-for-zero-vram-drafting-ecdf3e2731f0`
Run ID: `suffix-array-speculative-decoding-for-zero-vram-drafting-ecdf3e2731f0-20260531T204900866624+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/435fc4b4d6a3

## What looked useful

The mechanism is real but narrow: natural repeated contexts produce about 2.0-2.6 upper-bound bytes per verifier call, shuffled text collapses near 1.02, and periodic code reaches near-perfect acceptance. This supports further direct serving tests but is not paper-ready.

## Boundaries and scale limits

This run did not execute a transformer target model, did not measure wall-clock serving speed, used byte tokens rather than production tokenizer tokens, and evaluated only small contiguous text splits plus a synthetic periodic sanity corpus. The reported speedup is a free-draft upper bound, not an end-to-end latency claim.

## Claim scope

A CPU suffix/context retrieval index over byte-token text can provide zero-VRAM draft proposals with nontrivial oracle acceptance on small natural-text corpora: 1.02 accepted draft bytes per verifier call on 220k-byte Tiny Shakespeare and 1.57 on Alice, versus about 0.15-0.16 for a unigram draft and 0.025 for shuffled-context control.

## Why it stopped

Closed as no-paper useful signal because this run directly tested retrieval draft acceptance but only with an oracle held-out byte stream; it is proxy evidence rather than full model-serving validation.

## Recommended next action

Run a bounded direct speculative-decoding implementation with a small cached causal LM and production tokenizer, comparing suffix retrieval against no draft and a small neural draft on acceptance, target calls, and actual wall-clock latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Small-LM Speculative Decoding With Suffix Retrieval Drafts
- Success threshold: Suffix retrieval improves end-to-end tokens per second by at least 10% over no-draft decoding on one repeated-domain corpus while not regressing by more than 5% on a second corpus, with zero additional VRAM for a draft model.
- Stop condition: Stop if tokenizer-level acceptance stays below 0.3 accepted tokens per verifier call or CPU lookup overhead eliminates any target-call savings on both corpora.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decoding-for-zero-vram-drafting-ecdf3e2731f0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
