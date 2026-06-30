# Layered memory vs flat retrieval on repeated agent tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-memory-vs-flat-retrieval-on-repeated-agent-tasks-b65ff39fa88d`
Run ID: `layered-memory-vs-flat-retrieval-on-repeated-agent-tasks-b65ff39fa88d-20260611T163801785554+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/17d687b72f1b

## What looked useful

Layered consolidated memory achieved 1.000 mean accuracy with about 5 context tokens/query. Flat BM25 at top_k=8 achieved 0.603 overall and 0.283 multi-slot accuracy with about 184 context tokens/query; top_k=32 improved flat multi-slot accuracy to 0.714 but used about 737 context tokens/query and still trailed layered memory.

## Boundaries and scale limits

No production traces, no LLM generation, no embedding model, no metadata-filtered vector database, and no realistic natural-language paraphrase distribution. CPU-only benchmark ran 5 seeds with 2,000 events and 800 queries per seed.

## Claim scope

Bounded synthetic repeated-agent-task benchmark where tasks require exact current user state after chronological slot updates; layered consolidated semantic memory is compared with flat BM25 raw-event retrieval at top_k=8 and top_k=32.

## Why it stopped

Closed as a no-paper useful signal because evidence is synthetic and proxy-level, not full validation on real agent workloads.

## Recommended next action

Run a bounded direct follow-up with natural-language repeated-agent traces, embedding retrieval, metadata-aware flat baselines, and LLM answer generation before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language repeated-agent memory benchmark with metadata-aware flat baselines
- Success threshold: Layered memory improves multi-slot current-state accuracy by at least 10 percentage points over the strongest metadata-aware flat baseline while using no more than half the context tokens.
- Stop condition: Stop if metadata-aware flat retrieval matches layered accuracy within 3 percentage points at comparable context cost, or if generated traces do not produce reliable ground-truth current-state labels.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-vs-flat-retrieval-on-repeated-agent-tasks-b65ff39fa88d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
