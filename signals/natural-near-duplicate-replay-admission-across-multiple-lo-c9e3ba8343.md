# Natural near-duplicate replay admission across multiple local transformer routing tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `natural-near-duplicate-replay-admission-across-multiple-lo-c9e3ba8343`
Run ID: `natural-near-duplicate-replay-admission-across-multiple-lo-c9e3ba8343-20260519T193616637630+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-runtime VRAM-aware cascade replay with small local models: enoch://control-plane/projects/real-runtime-vram-aware-cascade-replay-with-small-local-mo-2f77d39ff5/runs/real-runtime-vram-aware-cascade-replay-with-small-local-mo-2f77d39ff5-20260519T191108433551+0000
- Parent run decision: Live-memory replay admission for real small local transformer cascades: enoch://control-plane/projects/live-memory-replay-admission-for-real-small-local-transfor-85eecba84d/runs/live-memory-replay-admission-for-real-small-local-transfor-85eecba84d-20260519T191844352029+0000

## What looked useful

Semantic near duplicates are common and useful compared with exact matching, but using near-duplicate admission as the sole replacement rule collapses buffer coverage and loses to random reservoir replay by 0.216 mean macro-F1 over 12 paired task/seed comparisons.

## Boundaries and scale limits

This bounded validation did not fine-tune transformer weights, use private production router traces, test larger model families, or run datacenter-scale workloads. The natural routing benchmark is public 20 Newsgroups text rather than deployed router traffic.

## Claim scope

On four public 20 Newsgroups-derived local transformer routing tasks with frozen all-MiniLM-L6-v2 embeddings, online linear router heads, label-blocked continual streams, 256-example replay buffers, and three fixed seeds, standalone natural near-duplicate replay admission improves over no replay and exact-duplicate-only replay but does not beat random reservoir replay.

## Why it stopped

Bounded direct validation found a mixed but no-paper result: near-duplicate admission beat no replay and exact-only controls, but was consistently and significantly worse than the real random reservoir replay baseline.

## Recommended next action

Stop this standalone near-duplicate-admission claim; if continuing, test a class-balanced near-duplicate-prioritized reservoir that preserves route coverage while using near-duplicate scores only as an admission priority.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Class-balanced near-duplicate-prioritized replay for local transformer routers
- Success threshold: Class-balanced near-duplicate-prioritized replay must beat both random reservoir and class-balanced reservoir by at least +0.02 mean macro-F1, with no task worse by more than -0.01 macro-F1 over the same 12 task/seed pairs.
- Stop condition: Stop if the prioritized policy fails to beat random or class-balanced reservoir on mean macro-F1, or if gains come only from one task while degrading two or more tasks.

## Evidence references

- Artifact root: `<local-path>/projects/natural-near-duplicate-replay-admission-across-multiple-lo-c9e3ba8343`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
