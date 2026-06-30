# Transformer Speculative Decoding With Suffix Retrieval Drafts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `transformer-speculative-decoding-with-suffix-retrieval-dra-ea0f941a5c`
Run ID: `transformer-speculative-decoding-with-suffix-retrieval-dra-ea0f941a5c-20260602T132000452896+0000`

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

- Parent run decision: Direct Small-LM Speculative Decoding With Suffix Retrieval Drafts: enoch://control-plane/projects/direct-small-lm-speculative-decoding-with-suffix-retrieval-32ba99342c/runs/direct-small-lm-speculative-decoding-with-suffix-retrieval-32ba99342c-20260601T091000918895+0000
- Parent run decision: Suffix-Array Speculative Decoding for Zero-VRAM Drafting: enoch://control-plane/projects/suffix-array-speculative-decoding-for-zero-vram-drafting-ecdf3e2731f0/runs/suffix-array-speculative-decoding-for-zero-vram-drafting-ecdf3e2731f0-20260531T204900866624+0000

## What looked useful

Across five fixed held-out Tiny Shakespeare segments, suffix_12 achieved 4.4566 tokens per target call versus 2.2746 for the ngram_4 drafter and 1.0663 for shuffled retrieval control. Acceptance was 0.8646 for suffix_12 versus 0.3188 for ngram_4, and suffix length ablations showed that too-long suffixes lose coverage.

## Boundaries and scale limits

The target model is not a transformer; throughput is measured by target-call accounting rather than end-to-end transformer serving latency; draft lookup overhead and GPU/KV-cache behavior were not validated.

## Claim scope

On real-text byte-token speculative decoding with a high-order n-gram target surrogate, suffix-retrieval drafts can nearly double target-call efficiency versus a low-order n-gram drafter baseline when suffix length balances precision and coverage.

## Why it stopped

No-paper closure: the mechanism is supported in a bounded surrogate, but transformer-target and serving-stack evidence are missing.

## Recommended next action

Run the same fixed-seed protocol against an actual causal transformer target and report both acceptance and end-to-end latency before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-target validation of suffix-retrieval speculative drafts
- Success threshold: Best suffix-retrieval configuration achieves at least 1.25x target-call efficiency versus the n-gram drafter baseline and at least 1.10x end-to-end tokens-per-second versus the same baseline across fixed seeds.
- Stop condition: Stop as negative if suffix retrieval fails to beat the n-gram drafter by 10% in target-call efficiency or if lookup overhead erases end-to-end speedup on the transformer target.

## Evidence references

- Artifact root: `<local-path>/projects/transformer-speculative-decoding-with-suffix-retrieval-dra-ea0f941a5c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
