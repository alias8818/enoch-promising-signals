# Hierarchical Memory for Long Context on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hierarchical-memory-for-long-context-on-cpu-413e6c1abec8`
Run ID: `hierarchical-memory-for-long-context-on-cpu-413e6c1abec8-20260604T033638501172+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/06693430aed3

## What looked useful

Hierarchical chunk summaries with exact local verification are a plausible CPU mechanism for long-context exact recall: slower at small contexts, but consistently faster at 1M records with exact recall and small summary-memory overhead.

## Boundaries and scale limits

Synthetic uint64 key-value retrieval only; no language model, no semantic retrieval, no transformer KV-cache integration, no production index baselines, and maximum tested context was 1,048,576 records with 2,048 queries per run on one CPU worker.

## Claim scope

On a synthetic exact key-value recall task over CPU-resident long contexts, Bloom-routed hierarchical chunk memory preserved exact recall and reduced query time versus dense full-context scan after a crossover between 65k and 262k records; at 1,048,576 records it achieved at least 13.7x query-time speedup across three seeds, excluding separately reported build cost.

## Why it stopped

No paper-positive closure: this was a bounded synthetic mechanism test, not direct evidence for LLM long-context modeling or a full validation.

## Recommended next action

Run a bounded deepen follow-up that compares the hierarchical chunk memory against sorted-array, hash-index, and ANN-style CPU baselines on exact and simple semantic long-context retrieval tasks before attempting transformer integration.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Baseline-controlled CPU hierarchical memory retrieval
- Success threshold: At 1M records, hierarchical memory must keep recall at or above 0.99 and beat at least one strong non-dense CPU baseline by 2x on query latency or by 2x on append/update cost at comparable latency and memory.
- Stop condition: Stop as a hard negative if standard hash or sorted indexes dominate hierarchical memory on latency, memory, and update cost across exact and document retrieval tasks.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-memory-for-long-context-on-cpu-413e6c1abec8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
