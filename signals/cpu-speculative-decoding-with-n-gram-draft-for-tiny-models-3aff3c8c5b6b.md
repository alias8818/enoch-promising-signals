# CPU Speculative Decoding with N-gram Draft for Tiny Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-speculative-decoding-with-n-gram-draft-for-tiny-models-3aff3c8c5b6b`
Run ID: `cpu-speculative-decoding-with-n-gram-draft-for-tiny-models-3aff3c8c5b6b-20260604T082651023670+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0efddd0f401e

## What looked useful

N-gram speculative decoding exactly matched baseline and reduced target calls, but wall-clock speedup appeared only with perfect acceptance and nontrivial verifier cost; corrupted/stale drafts were consistently slower despite fewer target calls.

## Boundaries and scale limits

Synthetic corpora, synthetic deterministic n-gram target oracle, no real transformer/KV-cache/tokenizer, single-process CPU run, short generated sequences of 512 tokens, Python 3.14/NumPy environment only.

## Claim scope

Bounded NumPy CPU proxy for exact greedy decoding with an n-gram draft and configurable tiny-model-like verifier cost; not a real transformer serving benchmark.

## Why it stopped

Proxy evidence is mixed: it supports the mechanism only under high acceptance and sufficient target cost, and falsifies broad tiny-CPU speedup claims for low-quality drafts in this local harness.

## Recommended next action

Stop as no-paper useful-signal evidence; the next bounded test should use a real CPU transformer/KV-cache implementation and natural prompt traces before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real tiny-transformer CPU n-gram speculative decoding threshold test
- Success threshold: At least 1.15x median tokens/s or latency improvement over baseline on real tiny-transformer CPU decoding with exact greedy equivalence and acceptance rate >= 0.8 across at least two natural prompt sets.
- Stop condition: Stop if acceptance is below 0.7 or median speedup is below 1.05x after controlling for model, tokenizer, KV-cache, generated length, and CPU thread count.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-speculative-decoding-with-n-gram-draft-for-tiny-models-3aff3c8c5b6b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
