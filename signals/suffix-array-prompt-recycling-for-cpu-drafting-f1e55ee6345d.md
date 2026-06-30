# Suffix-Array Prompt Recycling for CPU Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-prompt-recycling-for-cpu-drafting-f1e55ee6345d`
Run ID: `suffix-array-prompt-recycling-for-cpu-drafting-f1e55ee6345d-20260604T082235442724+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4b3dd5e2c185

## What looked useful

Suffix-array prompt recycling detects exact prompt-span reuse and performs well on a synthetic reuse control, but on natural text it gives only marginal accepted-byte gains over an 8-byte n-gram hash baseline while the tested query path is roughly 500x slower.

## Boundaries and scale limits

No LLM tokenizer IDs, no real serving traces, no verifier model, no optimized compiled implementation, and no end-to-end speculative decoding measurement.

## Claim scope

Byte-token offline replay with 65,536-byte prompt indexes and 32,768-byte continuations on three Gutenberg texts plus one synthetic prompt-reuse positive control.

## Why it stopped

Bounded proxy/medium test found mechanism support only for exact reuse and insufficient practical advantage over a simple n-gram hash baseline on natural text; this is not a full serving validation.

## Recommended next action

Stop this suffix-array Python prototype as no-paper evidence; the only worthwhile next test is a compiled tokenizer-level longest-match implementation against real prompt-reuse traces with a strict latency baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compiled tokenizer-level prompt recycling versus n-gram hash baseline
- Success threshold: At least 10% more accepted draft tokens than the best fixed n-gram hash baseline at p95 query latency below 10 microseconds and without materially higher prompt-index memory than the baseline.
- Stop condition: Stop if compiled longest-match query latency exceeds 10 microseconds p95 or accepted draft tokens improve by less than 5% over the n-gram hash baseline on two representative trace sets.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-prompt-recycling-for-cpu-drafting-f1e55ee6345d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
