# Anchor-Addressed Compressed Memory for Long-Context Agent Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-addressed-compressed-memory-for-long-context-agent-tasks-fdad5942473e`
Run ID: `anchor-addressed-compressed-memory-for-long-context-agent-tasks-fdad5942473e-20260629T051255721799+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/084f73bed7c6

## What looked useful

Anchor-addressed compressed memory reached 1.0000 accuracy versus 0.7281 for transcript_search_top8 and 0.4746 for flat_compressed_latest_alias. The failure cases show flat compression loses old aliases or returns stale facts after updates, while anchor mappings preserve identity.

## Boundaries and scale limits

Synthetic CPU-only proxy run: 160 anchors, 4,825 events, 1,140 queries, simple deterministic retrievers, no LLM-in-the-loop, no real operator traces, and simple lexical token estimates.

## Claim scope

In a deterministic synthetic repeated-agent memory benchmark with explicit anchors, alias changes, fact updates, and noisy distractors, anchor-addressed compressed memory preserved current entity facts better than flat compressed alias memory and lexical transcript search while using 14.55% of the estimated full-transcript memory.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic/proxy mechanism test, not direct full validation on real long-context agent tasks.

## Recommended next action

Run a bounded real-trace or LLM-in-the-loop follow-up that measures anchor creation/extraction errors, stale fact rate, answer accuracy, and memory footprint against transcript and flat-memory baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace anchor-addressed memory validation
- Success threshold: At least +0.20 absolute answer accuracy or stale-error reduction versus flat compressed memory at no more than 1.25x its memory footprint, with no worse than -0.05 accuracy versus full transcript search.
- Stop condition: Stop if anchor extraction accuracy is below 0.90 or if anchor-addressed memory fails to beat flat compressed memory by at least +0.10 absolute accuracy on the first 500 real-trace queries.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-addressed-compressed-memory-for-long-context-agent-tasks-fdad5942473e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
