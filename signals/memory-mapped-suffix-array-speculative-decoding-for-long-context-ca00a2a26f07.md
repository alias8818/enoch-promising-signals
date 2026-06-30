# Memory-Mapped Suffix Array Speculative Decoding for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `memory-mapped-suffix-array-speculative-decoding-for-long-context-ca00a2a26f07`
Run ID: `memory-mapped-suffix-array-speculative-decoding-for-long-context-ca00a2a26f07-20260629T010742183345+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/520493da9a0d

## What looked useful

Suffix-array variable-length matching accepted 2032 tokens versus 1994 for 8-gram and 1712 for 16-gram controls, but mean lookup latency was 3.54 ms versus 0.019 ms for 8-gram. The mechanism works, but this implementation is not practically compelling.

## Boundaries and scale limits

Synthetic corpus only; 60k indexed tokens; 213 query points; no real LLM verifier, tokenizer, KV-cache, concurrent serving, cold-page-cache, or multi-GB mmap validation; suffix-array lookup implemented in Python rather than optimized systems code.

## Claim scope

Bounded synthetic proxy: a Python/NumPy read-only memory-mapped suffix array over 60k indexed tokens can draft oracle-accepted continuations from repeated long-context spans, slightly improving accepted tokens/query over fixed 8-token and 16-token hash retrieval controls, but with much higher lookup latency.

## Why it stopped

Proxy evidence is mixed: useful accepted-token signal, but small gain and severe latency disadvantage versus simple hash retrieval prevent paper-positive closure.

## Recommended next action

Stop this run as no-paper useful signal; only pursue a follow-up if implementing an optimized Rust/C++ suffix/LCP interval lookup and testing real tokenized long-context traces against optimized hash baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized suffix/LCP interval speculative decoding on real token traces
- Success threshold: At 1M+ indexed tokens on real traces, suffix/LCP retrieval must improve accepted tokens per query by at least 10% over the best optimized k-gram baseline while keeping p95 lookup latency under 2x that baseline or improving latency-adjusted accepted-token throughput.
- Stop condition: Stop if optimized lookup remains more than 5x slower than the best k-gram baseline without at least 10% accepted-token/query gain on real traces.

## Evidence references

- Artifact root: `<local-path>/projects/memory-mapped-suffix-array-speculative-decoding-for-long-context-ca00a2a26f07`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
