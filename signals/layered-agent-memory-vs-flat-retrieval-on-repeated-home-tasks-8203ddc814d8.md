# Layered Agent Memory vs Flat Retrieval on Repeated Home Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-agent-memory-vs-flat-retrieval-on-repeated-home-tasks-8203ddc814d8`
Run ID: `layered-agent-memory-vs-flat-retrieval-on-repeated-home-tasks-8203ddc814d8-20260629T204332141088+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/64cd9e1e824e

## What looked useful

Layered doctrine memory achieved 1.000 accuracy versus 0.603 for flat retrieval, 0.784 for transcript search, and 0.258 for no memory. The layered-minus-flat paired seed delta was positive for all 10 seeds, mean +0.397.

## Boundaries and scale limits

Synthetic generator only; no live LLM agent, embeddings, real household traces, human preference ambiguity, or tool-execution scoring. Final bounded run covered 2,800 generated query cases across 10 seeds.

## Claim scope

In a deterministic synthetic repeated-home-task replay with preference updates and distractor snippets, layered current-fact memory outperformed flat retrieval without temporal conflict resolution on exact current-value recall.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only, not direct publication-grade validation.

## Recommended next action

Run a medium direct replay on hand-authored or anonymized realistic repeated-task transcripts with embedding retrieval, fair metadata/recency flat baselines, and LLM/action scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium realistic replay for layered home-task memory
- Success threshold: Layered memory improves exact/action-scored current-task accuracy by at least 10 percentage points over the strongest fair flat baseline across at least 500 realistic query cases, with paired improvements positive across seeds or folds.
- Stop condition: Stop if a flat baseline with reasonable metadata and temporal conflict handling closes the layered advantage below 5 percentage points or if realistic traces cannot be obtained without private data exposure.

## Evidence references

- Artifact root: `<local-path>/projects/layered-agent-memory-vs-flat-retrieval-on-repeated-home-tasks-8203ddc814d8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
