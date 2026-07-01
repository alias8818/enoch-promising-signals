# Prefix-Anchored KV Compression for Bounded Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prefix-anchored-kv-compression-for-bounded-context-d525b93eef72`
Run ID: `prefix-anchored-kv-compression-for-bounded-context-d525b93eef72-20260613T003701108168+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/0070cdeede09

## What looked useful

Prefix-anchored compression was conditionally useful: at 256 slots it reduced relative attention-output error versus uniform compression by 25.8% on prefix-heavy traces and 23.2% on noisy-prefix traces, but it was worse at tight 64-slot budgets and lost to recency compression on recent-heavy traces. Middle compression was necessary; exact prefix+recent with dropped middle had 71-79% higher error than prefix-anchor-with-middle-compression controls.

## Boundaries and scale limits

No real transformer generation, no perplexity/task-quality measurement, no multi-layer KV cache behavior, no RoPE/position-cache interaction, no learned compression, and no serving latency or throughput validation. Results should not be generalized to production LLM inference without direct model tests.

## Claim scope

Synthetic single-layer attention traces with 1024-item KV caches, 64-dimensional K/V, fixed cache budgets of 64/128/256 slots, deterministic contiguous mean compression with log-count attention correction, and controlled prefix-heavy, mixed, recent-heavy, and noisy-prefix query regimes.

## Why it stopped

No-paper closure: this run produced a reproducible synthetic useful signal, but evidence is mixed and proxy-only rather than direct model-quality validation.

## Recommended next action

Run a bounded direct transformer follow-up on a small pretrained or toy transformer with prefix-recall and recent-recall tasks, measuring perplexity/task accuracy plus KV memory and decode latency against uniform and recency compression baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct tiny-transformer validation of prefix-anchored KV compression
- Success threshold: At a moderate cache budget, prefix anchoring should improve prefix-dependent task accuracy or perplexity by at least 10% relative to both uniform and recency compression without more than 5% degradation on recent-dependent controls.
- Stop condition: Stop if prefix anchoring fails to beat both baselines on prefix-dependent direct model metrics at two tested budgets, or if implementation overhead makes latency worse by more than 20% at equal memory.

## Evidence references

- Artifact root: `<local-path>/projects/prefix-anchored-kv-compression-for-bounded-context-d525b93eef72`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
