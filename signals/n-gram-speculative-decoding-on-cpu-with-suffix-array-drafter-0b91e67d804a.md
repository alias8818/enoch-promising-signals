# N-gram speculative decoding on CPU with suffix-array drafter

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `n-gram-speculative-decoding-on-cpu-with-suffix-array-drafter-0b91e67d804a`
Run ID: `n-gram-speculative-decoding-on-cpu-with-suffix-array-drafter-0b91e67d804a-20260528T190600987305+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c8ad9af5b056

## What looked useful

Suffix-array drafting can recover multi-token continuations on highly repetitive streams, but on natural held-out text it accepted only about 0.106 tokens per draft call, and a variable-length hash backoff baseline matched acceptance while reducing p95 lookup latency by roughly 14x-47x on Shakespeare and 38x-131x on synthetic repeated motifs.

## Boundaries and scale limits

No real language model verifier or serving loop was run; implementation is Python; natural-text evidence is one small public-domain-style corpus; synthetic evidence only demonstrates a favorable repeated-pattern regime.

## Claim scope

Bounded CPU proxy benchmark of suffix-array n-gram drafting versus fixed and variable-length hash n-gram baselines on tiny Shakespeare word tokens and a deterministic repeated-motif corpus.

## Why it stopped

Proxy benchmark early-falsified the practical CPU suffix-array drafter claim at this scale: natural-text acceptance was too low and hash backoff dominated suffix-array lookup latency while matching acceptance.

## Recommended next action

Stop this project as no-paper evidence; only revisit with an optimized compressed suffix-array/FM-index implementation if the next claim is explicitly about memory scaling versus hash backoff.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compressed suffix-array/FM-index memory-latency comparison for n-gram drafting
- Success threshold: At equal accepted tokens per call within 5%, compressed suffix/FM-index uses at least 4x less peak memory than hash backoff with p95 draft lookup latency below 50 us for context lengths up to 32 on 1M-token histories.
- Stop condition: Stop if optimized suffix/FM-index p95 latency exceeds hash backoff by more than 10x without at least 4x memory reduction, or if natural-corpus acceptance remains below 0.5 accepted tokens per draft call.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-on-cpu-with-suffix-array-drafter-0b91e67d804a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
