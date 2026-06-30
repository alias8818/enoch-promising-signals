# CPU Speculative Decoding via Suffix-Array N-gram Drafts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-speculative-decoding-via-suffix-array-n-gram-drafts-ededfad7b919`
Run ID: `cpu-speculative-decoding-via-suffix-array-n-gram-drafts-ededfad7b919-20260620T091302549658+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ef9e9a368dd1

## What looked useful

Suffix-array lookup averaged 200 us/query with 93.65% nonempty drafts, but accepted only 0.096 exact future tokens/query and matched all 4 draft tokens in 0.05% of queries. This is above controls but below a practical speedup signal.

## Boundaries and scale limits

Single corpus, 48k train tokens, 12k held-out tokens, word/punctuation tokenization, 2,000 sampled queries, no verifier model, no transformer decode loop, no prompt-local or model-scored drafting.

## Claim scope

On a 60k-token Tiny Shakespeare exact-match proxy, a CPU suffix-array longest-context n-gram drafter is cheap to query and outperforms hash/shuffled controls, but its absolute accepted-token yield is too low to claim practical speculative decoding speedup.

## Why it stopped

Proxy/local evidence is useful but not paper-ready; exact-match draft acceptance is too low for a practical speculative decoding claim.

## Recommended next action

Run one bounded direct verifier-loop test with GPT-2-small-class CPU decoding and compare wall-clock tokens/second against vanilla decoding plus hash n-gram drafts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Verifier-loop CPU test for suffix-array n-gram drafts
- Success threshold: At least 5% repeatable wall-clock tokens/second improvement over vanilla decoding on the same prompts while preserving identical greedy output.
- Stop condition: Stop if suffix-array speculative decoding is slower than vanilla or improves throughput by less than 5% across the bounded prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-speculative-decoding-via-suffix-array-n-gram-drafts-ededfad7b919`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
