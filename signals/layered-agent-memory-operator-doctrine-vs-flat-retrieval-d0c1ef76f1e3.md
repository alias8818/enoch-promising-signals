# Layered Agent Memory: Operator-Doctrine vs Flat Retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-agent-memory-operator-doctrine-vs-flat-retrieval-d0c1ef76f1e3`
Run ID: `layered-agent-memory-operator-doctrine-vs-flat-retrieval-d0c1ef76f1e3-20260621T150032247879+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6efb0dc3fabc

## What looked useful

Layer separation directly prevented doctrine memories from being crowded out by many lexically similar entity/episode memories. Main sweep: layered accuracy stayed 1.000 across tested distractor and contradiction settings; flat top-k<=20 fell to 0.000 accuracy and 0.000 doctrine recall at 3+ distractors per incident. Large-top-k probe showed flat retrieval can recover at moderate density with top_k=100, but not at 5 distractors per incident even with top_k=200.

## Boundaries and scale limits

Synthetic corpus, symbolic BM25 retrieval, deterministic decision heuristic, generated rules/facts/episodes, no LLM answer generation, no embedding vector store, no human-authored doctrine, and no multi-turn memory mutation. The result is mechanism evidence, not production-agent or publication-grade validation.

## Claim scope

In a synthetic BM25 benchmark with generated doctrine, entity, and episode memories, layered retrieval that separately resolves entity facts and operator doctrine preserves correct doctrine-derived action selection under distractor-heavy memory, while flat retrieval can lose doctrine recall and action accuracy due to top-k crowding.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is not direct/full validation of real agent memory behavior.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should deepen with a small local LLM or embedding model, human-authored doctrine snippets, and hidden-answer scoring to test whether the same top-k crowding mechanism persists beyond symbolic BM25.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Embedding/LLM Doctrine-Layer Memory Probe
- Success threshold: Layered retrieval improves exact action accuracy by at least 15 percentage points over flat retrieval at matched context budget in two or more distractor-density settings, with doctrine recall improving by at least 20 percentage points.
- Stop condition: Stop as unsupported if layered retrieval fails to improve exact action accuracy by 5 percentage points in the first 200 scored cases or if failures are dominated by LLM reasoning errors unrelated to retrieval.

## Evidence references

- Artifact root: `<local-path>/projects/layered-agent-memory-operator-doctrine-vs-flat-retrieval-d0c1ef76f1e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
