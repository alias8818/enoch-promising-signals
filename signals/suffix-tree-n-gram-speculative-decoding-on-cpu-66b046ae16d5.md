# Suffix-Tree N-Gram Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-n-gram-speculative-decoding-on-cpu-66b046ae16d5`
Run ID: `suffix-tree-n-gram-speculative-decoding-on-cpu-66b046ae16d5-20260609T163443428784+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e71c81d1a98c

## What looked useful

The mechanism works and is cheap, but ordinary prose exact-match acceptance is weak. Best real-text gamma=16 rows achieved 5.86-14.11% theoretical target-call reduction with only 0.80-2.01% raw draft-token acceptance; gamma=1 achieved 5.02-10.53% reduction with 10.75-21.94% acceptance. Repetitive text reached 93.88% reduction, supporting use as a gated prompt-repetition optimization rather than a general standalone draft model.

## Boundaries and scale limits

Trace-level simulator only; regex word/punctuation tokens rather than a production LLM tokenizer; no actual LLM target forward passes; corpora limited to three Project Gutenberg prose files plus one deterministic repetitive stress corpus; single-thread CPU harness.

## Claim scope

A causal suffix/ngram prompt-lookup draft predictor has microsecond-level CPU lookup overhead and can reduce trace-level target verification calls by 5.86-14.11% on three public-domain prose streams, with much larger gains only on highly repetitive text.

## Why it stopped

No-paper useful signal: this was a trace-level proxy/early mechanism test, not a full validation with real model verification or serving latency.

## Recommended next action

Run a bounded CPU LLM integration test with the same policy in a llama.cpp-style decoder, comparing no-draft versus suffix-ngram draft on normal and repeated-context prompts using wall-clock tokens/sec and exact output equivalence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU LLM wall-clock test for gated suffix-ngram prompt lookup
- Success threshold: At least 10% wall-clock tokens/sec improvement on repeated-context prompts, normal-prompt slowdown no worse than 2%, and byte-identical greedy outputs relative to no-draft decoding.
- Stop condition: Stop if integration overhead exceeds measured target-call savings or if normal prompts slow down by more than 2% after repetition-density gating.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-n-gram-speculative-decoding-on-cpu-66b046ae16d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
