# Compressed Memory Anchors for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-memory-anchors-for-long-context-d2f537bb3038`
Run ID: `compressed-memory-anchors-for-long-context-d2f537bb3038-20260611T113013458341+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/867393ad498c

## What looked useful

Across three seeds, hashed superposition anchors reached >=0.90 top-1 routing for 16-record chunks with 4-8 anchors and for 64-record chunks with 16-32 anchors, but failed to reach 0.90 for 256-record chunks even with 32 anchors; centroid and sampled controls were much weaker while full exact key scan stayed at 1.0.

## Boundaries and scale limits

No end-to-end transformer training, no natural language tasks, no learned slot router, no generation/value reconstruction; tested only random-vector sparse-key routing up to 1024 chunks and 256 records per chunk.

## Claim scope

Synthetic vector key-value chunk routing shows content-addressed compressed anchors can work at moderate compression, but routing accuracy drops sharply under aggressive compression and high records per chunk.

## Why it stopped

This run produced a useful proxy capacity bound, but it is not a full validation of compressed memory anchors for long-context language modeling.

## Recommended next action

Run a bounded end-to-end small-transformer retrieval experiment with learned anchors and a parameter-matched dense baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer learned anchor retrieval validation
- Success threshold: At least +10 percentage points top-1 retrieval accuracy over the parameter-matched baseline at >=4x KV/memory compression, with no worse than 5% relative degradation on short-context control queries.
- Stop condition: Stop if learned anchors fail to beat the parameter-matched baseline by 5 percentage points on a smoke and medium synthetic split, or if routing accuracy collapses below 0.80 at 4x compression.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-memory-anchors-for-long-context-d2f537bb3038`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
