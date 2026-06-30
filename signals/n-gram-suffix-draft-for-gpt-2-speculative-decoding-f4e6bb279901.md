# N-gram Suffix Draft for GPT-2 Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-suffix-draft-for-gpt-2-speculative-decoding-f4e6bb279901`
Run ID: `n-gram-suffix-draft-for-gpt-2-speculative-decoding-f4e6bb279901-20260528T090713419826+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9f6fadd21e81

## What looked useful

The mechanism is not empty: suffix lookup found reusable prompt continuations and accepted enough tokens to reduce target calls by 32.2% for min_ngram=2,draft_len=4 and 37.6% for min_ngram=1,draft_len=4 on 32 x 64-token WikiText-2 GPT-2 runs. Longer drafts increased call reduction but lowered draft-token acceptance, showing a real tradeoff.

## Boundaries and scale limits

This is a bounded local inference harness, not a production serving implementation. It does not validate KV-cache reuse, batched serving throughput, latency under concurrent load, alternate corpora, sampling rather than greedy decoding, larger GPT-2-family targets, or long-context/request distributions. Draft_len=8 wall time was measured during parallel GPU contention and should not be used as a serving speed claim.

## Claim scope

On GPT-2 small greedy decoding over WikiText-2 validation prompts, a prompt-local n-gram suffix lookup drafter can reduce target-model verification calls in an exact speculative decoding harness. The best local setting tested, min_ngram=1 and draft_len=8, generated 2048 tokens with 1212 target calls, a 40.8% target-call reduction, while exactness checks passed on a smaller 4-prompt run.

## Why it stopped

Evidence supports the bounded mechanism but is insufficient for a paper because it is a small local harness and does not prove production speedup or robustness beyond WikiText-2 greedy decoding.

## Recommended next action

Stop this worker run as no-paper useful signal; next run should implement a KV-cache aware verifier and compare end-to-end latency against greedy GPT-2 on repeated and non-repeated prompt strata.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache aware GPT-2 prompt-lookup speculative decoding benchmark
- Success threshold: At least 15% median latency reduction versus greedy GPT-2 on the high-repetition stratum with no exactness failures and no more than 5% regression on the low-repetition stratum.
- Stop condition: Stop if KV-cache aware verification fails exactness, or if high-repetition prompts do not reach 10% median latency reduction after tuning min_ngram and draft_len.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-draft-for-gpt-2-speculative-decoding-f4e6bb279901`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
