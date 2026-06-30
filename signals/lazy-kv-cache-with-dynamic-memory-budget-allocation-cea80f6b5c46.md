# Lazy KV-Cache with Dynamic Memory Budget Allocation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `lazy-kv-cache-with-dynamic-memory-budget-allocation-cea80f6b5c46`
Run ID: `lazy-kv-cache-with-dynamic-memory-budget-allocation-cea80f6b5c46-20260610T003601833102+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b33d95b272d0

## What looked useful

Lazy cache retention is a plausible mechanism worth deeper testing: in the medium synthetic run, lazy_dynamic reduced relative attention-output error versus recent-window by 35.57% at 6.25% budget, 94.45% at 12.5%, and 97.42% at 25%; in distilgpt2 attention traces, lazy_dynamic retained 0.656 vs 0.279 attention mass at 12.5% budget and 0.750 vs 0.433 at 25%.

## Boundaries and scale limits

Synthetic simulator used seq_len 384, 8 heads, 5 seeds; real trace used distilgpt2, 4 short prompts, max length 96, and retained-attention-mass metrics only. No end-to-end decode quality, real KV allocator, batching, long-context benchmark, or production latency validation was performed.

## Claim scope

Bounded local evidence shows that lazy importance-based KV retention preserves synthetic attention outputs and small pretrained-model attention mass better than recent-window eviction under equal token budgets; dynamic allocation adds value in the synthetic heterogeneous-head setting.

## Why it stopped

This run produced useful bounded mechanism evidence, but the evidence is still synthetic/trace-level and is not sufficient for a paper or broad deployment claim.

## Recommended next action

Implement the lazy_static and lazy_dynamic policies in a real small-model decode loop and evaluate long-context perplexity or answer accuracy plus measured KV memory and latency against recent-window eviction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Decode Evaluation of Lazy KV Budget Policies
- Success threshold: At matched KV budget, lazy_dynamic should reduce quality degradation versus recent-window by at least 20% while adding no more than 10% decode latency overhead, and should beat lazy_static on heterogeneous long-range cases.
- Stop condition: Stop if lazy_static and lazy_dynamic do not beat recent-window on real decode quality at 12.5% and 25% budgets, or if metadata/scoring overhead exceeds 25% latency without compensating quality gains.

## Evidence references

- Artifact root: `<local-path>/projects/lazy-kv-cache-with-dynamic-memory-budget-allocation-cea80f6b5c46`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
