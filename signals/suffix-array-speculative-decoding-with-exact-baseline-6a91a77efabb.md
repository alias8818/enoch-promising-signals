# Suffix-Array Speculative Decoding with Exact Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-decoding-with-exact-baseline-6a91a77efabb`
Run ID: `suffix-array-speculative-decoding-with-exact-baseline-6a91a77efabb-20260620T015213635896+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a20ab1ddc3ea

## What looked useful

The exact baseline mechanism works in the controlled target, but practical speedup depends on proposal quality. In the neural smoke, suffix-array proposals were poorly aligned with the target and reduced verifier-call proxy by only about 4%, before proposer overhead.

## Boundaries and scale limits

Toy exactness uses a bigram target and 100,000 one-step samples. Neural evidence is a 96-token top-k-truncated distilgpt2 smoke test with a small synthetic/repeated corpus, not full-vocabulary GPT sampling or optimized serving latency.

## Claim scope

A small reproducible probe shows exact speculative correction preserves a known bigram target distribution within finite-sample error, but a naive suffix-array proposer over a small repeated corpus has only 4.17% acceptance against a distilgpt2 top-k neural target smoke.

## Why it stopped

Bounded local evidence supports exact correction but early neural smoke falsifies practical speedup for the naive small-corpus suffix-array drafter; this is not a full validation.

## Recommended next action

Stop this run as no-paper evidence; next work should test a domain-matched suffix corpus with batched full-vocabulary or top-p verifier correction and require at least 35% accepted drafted tokens after proposer overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Domain-matched suffix-array drafter with batched neural verifier
- Success threshold: At least 35% accepted drafted tokens and at least 20% end-to-end latency reduction versus autoregressive decoding on the matched corpus, with no detectable distributional regression in the bounded exactness check.
- Stop condition: Stop if matched-corpus acceptance remains below 20% or end-to-end latency is not better than autoregressive decoding after suffix lookup overhead.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decoding-with-exact-baseline-6a91a77efabb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
