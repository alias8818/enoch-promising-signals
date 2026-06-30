# CPU-draft speculative decoding with suffix-cache draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-draft-speculative-decoding-with-suffix-cache-draft-85ddbab76f6d`
Run ID: `cpu-draft-speculative-decoding-with-suffix-cache-draft-85ddbab76f6d-20260621T022906572424+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/736bfc6bce23

## What looked useful

Suffix-cache draft reuse is mechanically viable and lossless in the tested abstraction, but speedup is bounded by exact suffix recurrence. With cache capacity 4096, high_reuse reached 13.45% cache hit rate and 1.0456x incremental speedup versus no-cache CPU draft; mixed_reuse reached 5.75% and 1.0190x; low_reuse was effectively zero. Acceptance-rate delta was 0.0 in all scenarios.

## Boundaries and scale limits

No real transformer draft model, GPU verifier, production serving traces, tokenizer/KV-cache effects, or batching dynamics were tested. Main evidence is 96,000 generated tokens per scenario in a local CPU simulator.

## Claim scope

Synthetic n-gram mechanism probe of suffix-keyed CPU draft continuation reuse for speculative decoding; cached continuations were acceptance-equivalent to recomputed draft continuations and saved CPU draft compute only in traces with exact suffix recurrence.

## Why it stopped

Bounded synthetic evidence supports the mechanism but not a publication-grade claim; result is workload-sensitive and lacks direct real-model serving validation.

## Recommended next action

Stop this run as no-paper useful signal; only pursue a follow-up if real serving traces or a small real-model harness can measure exact suffix recurrence and end-to-end latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model suffix-cache draft latency probe
- Success threshold: At least 5% p50 and p95 latency improvement versus no-cache CPU draft speculative decoding on a trace with measured exact suffix recurrence above 10%, with no acceptance-rate degradation beyond measurement noise.
- Stop condition: Stop if exact suffix recurrence at active decode positions is below 5% or if end-to-end latency gain versus no-cache CPU draft is below 2% after controlling for cache overhead.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-draft-speculative-decoding-with-suffix-cache-draft-85ddbab76f6d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
