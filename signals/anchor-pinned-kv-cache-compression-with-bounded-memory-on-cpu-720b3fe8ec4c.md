# Anchor-Pinned KV Cache Compression with Bounded Memory on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-pinned-kv-cache-compression-with-bounded-memory-on-cpu-720b3fe8ec4c`
Run ID: `anchor-pinned-kv-cache-compression-with-bounded-memory-on-cpu-720b3fe8ec4c-20260621T162211124483+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 10, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- weak evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5e9c9627c941

## What looked useful

Anchor-pinned retention is a plausible bounded-memory mechanism for dormant structured values: it achieved 1.000 structured-dormant recall at every tested budget while heavy-hitter scored 0.000 on that task and 1.000 on salient unstructured needles.

## Boundaries and scale limits

Synthetic retention-only evidence; no real transformer KV tensors, generated-answer accuracy, perplexity, optimized inference latency, or long-context benchmark validation.

## Claim scope

In a deterministic CPU retention simulator with 4,096-token contexts, 800 synthetic tasks, and retained-token budgets from 16 to 256, query-aware anchor pinning composed with heavy-hitter selection retained dormant anchor-adjacent values that recency, sink+recent, and attention-only heavy-hitter policies missed.

## Why it stopped

Closed as no-paper useful signal because evidence is simulator-only and does not validate real transformer behavior.

## Recommended next action

Run a bounded direct-LLM follow-up with a small local transformer and real cache eviction, measuring generated retrieval accuracy, memory, and latency against heavy-hitter and sink+recent controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-transformer validation of anchor-pinned KV retention
- Success threshold: At least 20 percentage-point dormant structured retrieval improvement over heavy-hitter at one or more budgets, with unstructured needle accuracy no more than 2 percentage points below heavy-hitter and retained KV entries never exceeding budget.
- Stop condition: Stop if anchor-pinned retention fails to beat heavy-hitter on dormant structured retrieval at all tested budgets or if real-cache instrumentation cannot enforce the budget.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-pinned-kv-cache-compression-with-bounded-memory-on-cpu-720b3fe8ec4c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
