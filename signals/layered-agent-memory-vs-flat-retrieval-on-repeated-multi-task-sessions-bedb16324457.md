# Layered Agent Memory vs Flat Retrieval on Repeated Multi-Task Sessions

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-agent-memory-vs-flat-retrieval-on-repeated-multi-task-sessions-bedb16324457`
Run ID: `layered-agent-memory-vs-flat-retrieval-on-repeated-multi-task-sessions-bedb16324457-20260613T025230229833+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6e67206aaa6d

## What looked useful

Layered memory and flat retrieval both reached 1.000 mean answer inclusion accuracy, but flat top-k context contamination averaged 0.992 versus 0.250 for layered memory across 180 conditions.

## Boundaries and scale limits

Synthetic slot facts, generated distractors, lexical retrieval baseline, no LLM-in-the-loop generation, no semantic vector database baseline, 6 seeds, 24 sessions, 3-8 tasks, 142560 online queries.

## Claim scope

In a deterministic synthetic repeated-session benchmark with task/slot-routable queries, layered memory preserved answer recall while reducing irrelevant or conflicting retrieved context compared with flat lexical top-k retrieval under a fixed k=4 context budget.

## Why it stopped

No-paper closure: the local result is a useful synthetic mechanism signal, not direct publication-grade evidence for real agent memory systems.

## Recommended next action

Run a bounded LLM-in-the-loop follow-up where retrieved memories are fed to a model and final answer contradiction/error rates are measured against flat semantic retrieval with recency controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop repeated-session memory contamination benchmark
- Success threshold: Layered memory reduces LLM wrong-preference or contradiction rate by at least 25% relative to flat semantic retrieval without reducing answerable-query recall by more than 2 percentage points.
- Stop condition: Stop if flat semantic retrieval with recency controls matches layered contamination and LLM error rates within 5% relative difference, or if both systems show no measurable downstream LLM error from contaminated context.

## Evidence references

- Artifact root: `<local-path>/projects/layered-agent-memory-vs-flat-retrieval-on-repeated-multi-task-sessions-bedb16324457`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
