# KV-cache-aware routed n-gram speculative decoding on realistic mixed-domain prompts

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `kv-cache-aware-routed-n-gram-speculative-decoding-on-reali-a1bbc74443`
Run ID: `kv-cache-aware-routed-n-gram-speculative-decoding-on-reali-a1bbc74443-20260526T205631366256+0000`

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

- Parent run decision: Context-Aware N-gram Speculative Decoding: enoch://control-plane/projects/context-aware-n-gram-speculative-decoding-cfd239152dc8/runs/context-aware-n-gram-speculative-decoding-cfd239152dc8-20260526T020851382698+0000
- Parent run decision: Small-LM serving test for context-routed n-gram speculative decoding: enoch://control-plane/projects/small-lm-serving-test-for-context-routed-n-gram-speculativ-d86d93eca2/runs/small-lm-serving-test-for-context-routed-n-gram-speculativ-d86d93eca2-20260526T143011288696+0000

## What looked useful

Global n-gram speculation reduced target verification calls by about 86.34% versus no speculation. Domain routing was slightly worse than global, random routing was much worse, and cache-aware routing collapsed to global when cache-load cost was charged.

## Boundaries and scale limits

Offline static corpus; exact next-token trace verification rather than real LLM logits or GPU serving latency; public dataset/tokenizer loading was attempted but stopped to keep the CPU-only worker run bounded.

## Claim scope

On a deterministic offline mixed-domain trace suite with fixed seeds, cache-aware routed n-gram speculative decoding did not meaningfully improve over a strong global n-gram baseline after route/cache overhead; zero-cost routing produced only a tiny 0.085% estimated speedup gain.

## Why it stopped

Medium trace-level validation failed to show a meaningful advantage for KV-cache-aware routing over the global n-gram baseline; this is not a full serving validation but is enough to reject the local mechanism claim under tested conditions.

## Recommended next action

Stop this branch as no-paper useful-signal evidence; only revisit with a real small-LLM serving harness that measures wall-clock latency and cache movement over a public mixed-domain prompt suite.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LLM serving validation for routed n-gram speculation
- Success threshold: Cache-aware routing must improve median tokens/sec by at least 5% over global n-gram at equal output tokens and no worse than 1% p95 latency regression across three fixed seeds.
- Stop condition: Stop if global n-gram remains within 2% of cache-aware routing on median tokens/sec after route/cache overhead is measured, or if route overhead exceeds the accepted-token gain.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-aware-routed-n-gram-speculative-decoding-on-reali-a1bbc74443`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
