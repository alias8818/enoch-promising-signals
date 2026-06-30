# Layered Agent Memory vs Flat Retrieval on Multi-Session Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-agent-memory-vs-flat-retrieval-on-multi-session-tasks-ebdcaffd13d6`
Run ID: `layered-agent-memory-vs-flat-retrieval-on-multi-session-tasks-ebdcaffd13d6-20260619T231801631829+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fbfae992bbdc

## What looked useful

Layered recency-aware slot memory maintained 1.0 exact-answer accuracy with about 29-31 context characters while flat BM25 retrieval degraded as session count increased. At 128 sessions, flat top-k=5 reached 0.3753 accuracy and flat top-k=20 reached 0.4975 accuracy despite returning about 57x more context than the layered memory.

## Boundaries and scale limits

CPU-only local benchmark; 8-128 sessions, 50 seeds per condition, 80 queries per seed; no natural conversations, LLM extraction, dense retrieval, temporal reranking, or end-to-end agent task execution.

## Claim scope

Synthetic multi-session latest-fact recall with generated stale/conflicting notes and oracle typed fact extraction into the layered memory.

## Why it stopped

No-paper closure: the result is a synthetic proxy mechanism signal, not direct publication-grade evidence for real multi-session agents.

## Recommended next action

Run a bounded deepen follow-up that replaces oracle fact tags with an explicit memory extraction step and compares against flat retrieval with temporal reranking on the same generated histories.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layered Memory With Noisy Extraction vs Temporal Flat Retrieval
- Success threshold: Layered memory beats the strongest flat temporal baseline by at least 10 percentage points at 64 and 128 sessions while using at least 5x less answer context, with extraction F1 reported above 0.90.
- Stop condition: Stop if extraction F1 falls below 0.80 or if temporal flat retrieval matches layered accuracy within 5 percentage points at 64 and 128 sessions.

## Evidence references

- Artifact root: `<local-path>/projects/layered-agent-memory-vs-flat-retrieval-on-multi-session-tasks-ebdcaffd13d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
