# Exact-Anchor Episodic Memory for Small Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-episodic-memory-for-small-agents-38b3219c09d4`
Run ID: `exact-anchor-episodic-memory-for-small-agents-38b3219c09d4-20260525T035831395822+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7a13d09d61dc

## What looked useful

Exact-anchor memory is a cheap guard for small-agent memory stacks that strip or smooth opaque IDs, but the evidence shows an engineering pattern rather than a paper-ready novel result because ordinary lexical exact-match retrieval is an equally strong baseline on this task.

## Boundaries and scale limits

Synthetic CPU-only benchmark only; no end-to-end LLM agent, learned embedding model, production vector database, natural trace corpus, typo robustness, collision handling, or long-horizon memory writing was tested. A lexical all-token TF-IDF baseline also solved the task perfectly.

## Claim scope

On a deterministic synthetic episodic recall benchmark with 1000 near-duplicate ID-keyed memories per trial and 30 trials, preserving an exact anchor side index prevents the recall failures seen when a semantic retriever drops ID-like tokens.

## Why it stopped

The local evidence supports the narrow mechanism but is synthetic/proxy-only and does not beat a simple lexical exact-match baseline, so it is not publication-grade validation.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should evaluate exact-anchor hybrid memory inside an actual small-agent loop against embedding, BM25, and hybrid retrieval baselines on semi-natural ID-bearing traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact-anchor hybrid memory in a real small-agent trace loop
- Success threshold: Exact-anchor hybrid retrieval reduces wrong-episode recall by at least 50% relative to embedding-only retrieval and is not worse than BM25/hybrid retrieval by more than 2 percentage points on clean-anchor queries, while preserving useful fallback accuracy when no anchor is present.
- Stop condition: Stop if exact-anchor hybrid fails to outperform embedding-only retrieval on clean-anchor wrong-episode rate, or if BM25/hybrid retrieval fully matches it without requiring anchor-specific machinery across clean, typo, and missing-anchor splits.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-episodic-memory-for-small-agents-38b3219c09d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
