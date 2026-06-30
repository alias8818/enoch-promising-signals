# N-gram CPU cache self-speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-cpu-cache-self-speculative-decoding-eb46ad182dd1`
Run ID: `n-gram-cpu-cache-self-speculative-decoding-eb46ad182dd1-20260607T114348515193+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/03ec92883942

## What looked useful

CPU n-gram cache drafting can produce exact accepted greedy tokens often enough to reduce forward calls in a bounded small-model proxy. Best mean configuration was n=2, max_draft=4 with 1.110x mean speedup, 72.25 accepted tokens per 768-token run, and 6.72% accepted/proposed-token rate. Correctness check passed 16/16 equivalence cases.

## Boundaries and scale limits

Small model only; 12 prompts x 64 generated tokens per seed; full-prefix forward path rather than production KV-cache verification; no 7B+ model, batching, sampling, live-serving CPU contention, or cross-corpus robustness validation.

## Claim scope

On a distilgpt2 CUDA full-prefix greedy-decoding proxy with WikiText-derived CPU n-gram caches, exact speculative verification preserved greedy output and reduced target forward calls, yielding 1.036x to 1.110x mean speedup across tested n-gram/draft configurations over four seeds.

## Why it stopped

This run produced useful bounded proxy evidence but not a paper-ready validation; the remaining question is production KV-cache behavior rather than another full-prefix proxy.

## Recommended next action

Run a bounded deepen follow-up with a production-style KV-cache verifier on GPT-2-small or similar local model, using repeated prompts and a success threshold of at least 1.15x median tokens/sec without output divergence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache n-gram speculative decoding serving probe
- Success threshold: Median tokens/sec at least 1.15x greedy baseline with zero output mismatches and p50/p95 latency not worse than baseline by more than 5%.
- Stop condition: Stop if acceptance stays below 5% or median tokens/sec is below 1.05x baseline after two n-gram orders and two draft lengths with verified output equivalence.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cpu-cache-self-speculative-decoding-eb46ad182dd1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
