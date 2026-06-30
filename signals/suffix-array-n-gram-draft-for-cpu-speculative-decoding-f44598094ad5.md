# Suffix-Array N-gram Draft for CPU Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-n-gram-draft-for-cpu-speculative-decoding-f44598094ad5`
Run ID: `suffix-array-n-gram-draft-for-cpu-speculative-decoding-f44598094ad5-20260609T051839831344+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/93e550780a82

## What looked useful

The suffix-array mechanism is feasible and can reduce build-time traced allocations versus a Counter-heavy hash table in this prototype, but it did not improve prediction quality and was substantially slower at the CPU lookup operation that matters for a draft model. Exact n-gram reuse also had too little held-out acceptance to be useful on this text at n=3 or n=5.

## Boundaries and scale limits

Single-process Python implementation; bounded suffix prefixes rather than a compressed production suffix array; Tiny Shakespeare only; no BPE tokenizer, target language model, KV-cache integration, or end-to-end speculative decoding acceptance measurement.

## Claim scope

On Tiny Shakespeare word/punctuation tokens with 20k-100k-token training prefixes and 5,000 held-out queries per case, a bounded suffix-array n-gram index reproduced hash n-gram predictions but was 2.7x-5.0x slower for lookup; both exact-context methods produced near-zero short-draft acceptance on the held-out continuation.

## Why it stopped

Moderate proxy/direct data-structure evidence does not support the suffix-array n-gram index as a practical standalone CPU draft model: lookup is slower than the hash baseline and draft acceptance is near zero in the held-out text probe.

## Recommended next action

Stop this as no-paper evidence; only revisit with an end-to-end small-LM speculative decoding harness using real tokenizer traces and a rolling prompt/history cache.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Rolling-cache suffix n-gram draft in a small-LM speculative decoding loop
- Success threshold: Suffix-array draft must beat no-draft wall-clock throughput by at least 10% and be within 10% of hash n-gram throughput while achieving at least 0.5 mean accepted draft tokens per target step on the bounded prompt suite.
- Stop condition: Stop if mean accepted draft tokens remain below 0.2 or suffix-array p95 draft latency exceeds hash n-gram p95 by more than 2x after implementing context backoff and rolling-cache updates.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-n-gram-draft-for-cpu-speculative-decoding-f44598094ad5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
