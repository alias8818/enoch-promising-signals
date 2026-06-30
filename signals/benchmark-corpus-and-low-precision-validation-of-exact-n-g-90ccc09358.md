# Benchmark-corpus and low-precision validation of exact n-gram speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `benchmark-corpus-and-low-precision-validation-of-exact-n-g-90ccc09358`
Run ID: `benchmark-corpus-and-low-precision-validation-of-exact-n-g-90ccc09358-20260522T062542546746+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Medium corpus validation of KV-cache n-gram speculative decoding on repeated code and text: enoch://control-plane/projects/medium-corpus-validation-of-kv-cache-n-gram-speculative-de-9798d03e0d/runs/medium-corpus-validation-of-kv-cache-n-gram-speculative-de-9798d03e0d-20260522T041204344138+0000
- Parent run decision: Optimized KV-cache n-gram speculative decoding latency test: enoch://control-plane/projects/optimized-kv-cache-n-gram-speculative-decoding-latency-tes-6ae376d828/runs/optimized-kv-cache-n-gram-speculative-decoding-latency-tes-6ae376d828-20260522T032104481187+0000

## What looked useful

Exact n-gram speculation is not a broad paper-ready win here, but the benchmark found a reproducible narrow signal: n=2/K=4-8 can give about 8 percent time-adjusted gain on distilgpt2/WikiText-2; fp16 validation mostly preserves acceptance decisions; int4 logit validation is unsafe.

## Boundaries and scale limits

Not tested on 7B+ models, production serving stacks, broad web-scale corpora, sampling-mode acceptance, batched multi-user inference, or optimized compressed n-gram lookup. The timing estimate excludes n-gram lookup overhead and full serving-system effects.

## Claim scope

On local GB10 validation with distilgpt2, WikiText-2, greedy target validation, and a 1M-token exact n-gram table, low-order exact n=2 drafting produced a small but real speculative decoding signal: 1.244x forward-count speedup and about 1.08x cached-validation time-adjusted speedup at K=8, while n=3/n=4 were weak and held-out tiny Shakespeare n=4 was near baseline.

## Why it stopped

Bounded validation found only a small scoped gain and mixed low-precision behavior, not enough for publication-grade support of exact n-gram speculative decoding.

## Recommended next action

Stop this run as no-paper useful evidence; only deepen if testing the same n=2/K=4-8 method on GPT-2-small-or-larger targets and at least one broader held-out corpus with measured end-to-end lookup plus cached validation latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end exact n=2 n-gram speculation on larger target models and broader corpora
- Success threshold: Across at least two broader corpora and one larger target model, n=2/K=4-8 must achieve at least 1.15x measured end-to-end latency speedup versus cached greedy decoding, with fp16 acceptance-decision disagreement below 0.5 percent and random control at or below 1.01x.
- Stop condition: Stop if end-to-end measured speedup is below 1.10x on either broader corpus, if lookup overhead erases the gain, or if fp16 validation disagreement exceeds 0.5 percent.

## Evidence references

- Artifact root: `<local-path>/projects/benchmark-corpus-and-low-precision-validation-of-exact-n-g-90ccc09358`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
