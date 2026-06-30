# Bounded Speculative Decoding with N-gram Draft Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-speculative-decoding-with-n-gram-draft-baseline-7ee185af4456`
Run ID: `bounded-speculative-decoding-with-n-gram-draft-baseline-7ee185af4456-20260608T200225731011+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/69b8a2ecfe2c

## What looked useful

The n-gram draft baseline is mechanically viable as an exact speculative draft and gives nontrivial target-call upper-bound gains, but acceptance is workload-dependent and draft-8 accepts only about 15% of proposed tokens, so systems overhead could erase the apparent benefit.

## Boundaries and scale limits

No optimized KV-cache-aware wall-clock serving benchmark; only GPT-2-small, greedy argmax, Wikitext-2, 128-token prompts, 48 generated tokens, and in-context suffix-copy drafts were tested.

## Claim scope

On GPT-2-small greedy decoding over 24 Wikitext-2 prompts per configuration, an in-context suffix-matching n-gram draft preserves exact greedy output and reduces target forward calls by 1.42x-1.62x in a proxy speculative decoding harness.

## Why it stopped

Bounded local proxy supports the mechanism but does not provide direct production throughput evidence, so it is not sufficient for a paper-positive decision.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement a KV-cache-aware wall-clock benchmark and require at least 1.2x measured tokens/s over greedy on Wikitext-2 plus one non-repetitive corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache wall-clock validation for n-gram speculative decoding
- Success threshold: At least 1.2x measured tokens/s over greedy with exact output match on both corpora and no material latency regression for 48-128 token generations.
- Stop condition: Stop if measured throughput is below 1.05x on either corpus or exact output equivalence fails.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-speculative-decoding-with-n-gram-draft-baseline-7ee185af4456`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
