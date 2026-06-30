# Baseline-controlled CPU hierarchical memory retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `baseline-controlled-cpu-hierarchical-memory-retrieval-13b82b6703`
Run ID: `baseline-controlled-cpu-hierarchical-memory-retrieval-13b82b6703-20260604T062714098782+0000`

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

- Parent run decision: Hierarchical Memory for Long Context on CPU: enoch://control-plane/projects/hierarchical-memory-for-long-context-on-cpu-413e6c1abec8/runs/hierarchical-memory-for-long-context-on-cpu-413e6c1abec8-20260604T033638501172+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/06693430aed3

## What looked useful

Mechanism support is present: clustered hierarchy achieved 0.971 mean recall@1 at probe 1 on 100k vectors while random partitions achieved 0.012 mean recall@1. The latency threshold failed: that point was only 0.915x flat speed, and 500k checks showed either >2x speed with recall below threshold or recall above threshold with speed below 2x.

## Boundaries and scale limits

Synthetic vector data only; no real model memory traces, semantic embedding corpus, production ANN implementation, or end-to-end model-quality evaluation. Largest check was one seed at 500k vectors; primary controlled run was three seeds at 100k vectors.

## Claim scope

On synthetic clustered vector memories up to 500k entries, learned CPU hierarchical retrieval preserves recall far better than a random-partition control, but the tested NumPy/Python routed implementation does not achieve recall@1 >= 0.95 and >= 2x speedup over an optimized flat exact NumPy baseline at the same time.

## Why it stopped

Controlled direct small test plus scale checks failed the combined recall and 2x CPU latency threshold; this is not a full real-corpus validation, but it is sufficient to reject the tested implementation path as paper-ready.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded action is to test a compiled or batched hierarchy implementation against the same optimized flat CPU baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compiled batched CPU hierarchy versus optimized flat retrieval
- Success threshold: For clustered memories, at one probe setting across at least three seeds: mean recall@1 >= 0.95, mean speedup_vs_flat >= 2.0, and mean recall gap versus random partition control >= 0.5 absolute.
- Stop condition: Stop if no compiled/batched configuration reaches both recall@1 >= 0.95 and speedup_vs_flat >= 2.0 at 500k vectors, or if the random control explains most of the recall at the same candidate budget.

## Evidence references

- Artifact root: `<local-path>/projects/baseline-controlled-cpu-hierarchical-memory-retrieval-13b82b6703`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
