# LLM-agent layered memory replay on natural-language household traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-agent-layered-memory-replay-on-natural-language-househ-098e82f6a1`
Run ID: `llm-agent-layered-memory-replay-on-natural-language-househ-098e82f6a1-20260629T224509471008+0000`

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

- Parent run decision: Layered Memory for Multi-Step Household Tasks: enoch://control-plane/projects/layered-memory-for-multi-step-household-tasks-b5f963b0da1a/runs/layered-memory-for-multi-step-household-tasks-b5f963b0da1a-20260629T221302309776+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fa338371aaca

## What looked useful

Layered source/recency structure produced a large bounded mechanism signal: 1.000 accuracy versus 0.517 for flat retrieval, 0.250 for transcript search, and 0.250 for no memory. Across 200 generated corpora, the layered-minus-flat mean accuracy improvement was 0.527 with a 95% interval of [0.476, 0.590].

## Boundaries and scale limits

Synthetic templated traces only; no LLM agent, learned embedding retriever, real household corpus, independent annotation, adversarial paraphrase, latency measurement, or full-scale deployment validation was tested.

## Claim scope

On a deterministic synthetic benchmark of 48 natural-language household traces with stale corrections and invalid distractors, explicit layered memory with source filtering and latest-write-wins conflict resolution answered all 288 replay questions correctly and outperformed no-memory, transcript-search, and flat-retrieval baselines.

## Why it stopped

Bounded synthetic/proxy evidence supports the mechanism but is insufficient for publication-grade LLM-agent claims.

## Recommended next action

Stop this run as no-paper useful evidence; next run should test the same layered-vs-flat claim on independently authored household traces with paraphrased questions and a local embedding or LLM retrieval baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layered memory replay with paraphrased household traces and retrieval baselines
- Success threshold: Layered retrieval improves exact-answer accuracy by at least 10 percentage points over the strongest flat baseline on at least 200 held-out questions, with bootstrap confidence interval lower bound above 0.
- Stop condition: Stop as unsupported if layered retrieval improves by less than 5 percentage points or the bootstrap interval includes zero after 200 held-out questions.

## Evidence references

- Artifact root: `<local-path>/projects/llm-agent-layered-memory-replay-on-natural-language-househ-098e82f6a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
