# N-gram Speculative Decoding with Suffix-Trie Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-with-suffix-trie-baseline-b9d43feefe86`
Run ID: `n-gram-speculative-decoding-with-suffix-trie-baseline-b9d43feefe86-20260608T143111838062+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/715307f7e303

## What looked useful

The suffix-trie baseline can provide modest verification-call reduction in text replay, but full multi-token draft acceptance is rare below 0.4% for best per-corpus settings and median accepted draft length is zero, so longer suffixes and longer draft blocks do not create strong speculative decoding leverage.

## Boundaries and scale limits

Proxy-only CPU replay: no neural target model, no model tokenizer, no measured serving latency, no GPU kernels, no production draft-overhead accounting, and only three public-domain book corpora.

## Claim scope

In a pure-stdlib replay simulation on held-out Project Gutenberg book text, a suffix-trie n-gram draft model reduced idealized target verification calls by about 18-22% versus one-token decoding, with best results from order-2 contexts.

## Why it stopped

Closed as no-paper useful signal because the local evidence supports only a proxy replay mechanism, not a full speculative decoding validation.

## Recommended next action

Run a bounded direct neural-target follow-up with a real tokenizer and small target model to measure actual greedy acceptance, verification calls, draft overhead, and wall-clock latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural-target validation of suffix-trie n-gram speculative decoding
- Success threshold: At least 10% wall-clock latency reduction and at least 15% verification-call reduction on 500 or more held-out prompts, with confidence intervals excluding zero improvement.
- Stop condition: Stop if verification-call reduction is below 10%, if draft overhead removes wall-clock gains, or if median accepted draft length remains zero across all tested draft lengths.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-with-suffix-trie-baseline-b9d43feefe86`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
