# Production-style copy-on-write KV suffix-history speculation with deterministic fp16 acceptance

Status: `useful_signal`
Project ID: `production-style-copy-on-write-kv-suffix-history-speculati-3ee4d280af`
Run ID: `production-style-copy-on-write-kv-suffix-history-speculati-3ee4d280af-20260519T101253572889+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Production-style copy-on-write KV suffix-history speculation with deterministic fp16 acceptance: internal_generated:production-style-copy-on-write-kv-suffix-history-speculati-3ee4d280af

## What looked useful

At calibrated medium branch=4 rounds=24 over 3 seeds, COW matched eager final-cache digests exactly, improved ops/sec by 33.28x, used 0.597x torch peak allocation, and reduced estimated copy traffic to 0.0131x of eager. Naive fp16 acceptance falsely accepted 26.61% of adversarial near-tie trials while widened deterministic acceptance made 20000/20000 correct decisions.

## Boundaries and scale limits

No real transformer serving integration, draft/target model, paged-attention kernel, scheduler, natural text workload, or long-running fragmentation test. Uncalibrated medium, branch-8 medium, longer medium persistence, and large-local eager attempts were terminated before metrics.

## Claim scope

Bounded torch/CUDA KV-cache-shaped tensor benchmark: copy-on-write suffix-history sharing reduces prefix-copy traffic and preserves final accepted cache contents versus eager full-prefix copying at small and calibrated medium branch-4 scale; deterministic widened acceptance avoids adversarial fp16 near-tie false accepts.

## Why it stopped

Strict Tier-4 paper-readiness was not met: evidence supports the mechanism but remains a bounded synthetic/local benchmark, and larger branchier attempts were terminated before metrics.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful evidence; a separate non-chained effort would need integrated real-model serving metrics before any paper claim.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/production-style-copy-on-write-kv-suffix-history-speculati-3ee4d280af`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
