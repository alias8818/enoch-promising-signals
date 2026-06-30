# Suffix-Array N-Gram Speculation for Zero-Memory Draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-n-gram-speculation-for-zero-memory-draft-e811b88befef`
Run ID: `suffix-array-n-gram-speculation-for-zero-memory-draft-e811b88befef-20260525T001229924959+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/da180e9f4a95

## What looked useful

Suffix-array copying accepted 1.088 bytes/query on Tiny Shakespeare versus 0.391 for fixed 8-gram and 0.156 first-byte unigram. It reached about 7.4 accepted bytes/query on highly repetitive synthetic corpora, but collapsed to 0.063 bytes/query on IID random and 0.141 on Markov text. The mechanism is repetition-dependent and not broadly validated.

## Boundaries and scale limits

Tested on 160k-byte corpora with 100k-byte training prefixes and 3,462 held-out queries per corpus. No LLM tokenizer, no target-model speculative acceptance loop, no online suffix-array updates, and no large-context serving benchmark were tested.

## Claim scope

A byte-level suffix-array copy draft over a 100k-byte prefix can recover exact held-out continuations in repeated text and improves over a fixed 8-byte n-gram table on one real-text Tiny Shakespeare slice, but it is only a local proxy for LLM speculative decoding.

## Why it stopped

Bounded byte-level evidence supports the retrieval mechanism but is proxy-only and insufficient for a paper or deployment claim.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next test is a token-level prompt-lookup speculative decoding benchmark with a small target LM and end-to-end acceptance/tokens-per-second metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-Level Suffix-Array Prompt Lookup with Target-LM Acceptance
- Success threshold: At least 10% end-to-end tokens/sec improvement over no-draft and at least 20% accepted-token improvement over fixed n-gram prompt lookup on one corpus without regression on the other.
- Stop condition: Stop if token-level suffix-array lookup fails to beat fixed n-gram prompt lookup on accepted tokens or adds enough lookup/update overhead to reduce end-to-end throughput.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-n-gram-speculation-for-zero-memory-draft-e811b88befef`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
