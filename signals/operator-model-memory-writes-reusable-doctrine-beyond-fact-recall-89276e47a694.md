# Operator-Model Memory Writes Reusable Doctrine Beyond Fact Recall

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-model-memory-writes-reusable-doctrine-beyond-fact-recall-89276e47a694`
Run ID: `operator-model-memory-writes-reusable-doctrine-beyond-fact-recall-89276e47a694-20260628T112833606333+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c6936620b079

## What looked useful

Doctrine memory achieved 0.9678 mean novel-query accuracy in the main run and 0.9674 with no repeated queries, while exact fact recall matched no-memory at about 0.316 and 0.312 respectively. Exemplar memory was also strong but lower, about 0.871 and 0.866 novel accuracy.

## Boundaries and scale limits

Synthetic transformations only; deterministic solver instead of a trained LLM/operator; family-scoped retrieval is assumed; no natural-language memory writing, retrieval noise, or large-scale agent deployment was tested.

## Claim scope

In a deterministic synthetic task-stream benchmark with sparse ambiguous supports, operator-written reusable doctrine memories improved novel-query accuracy over literal exact fact recall and reduced ambiguity versus raw exemplar memory.

## Why it stopped

Closed as a no-paper useful signal because the positive evidence is synthetic and deterministic, not direct publication-grade evidence for real operator-model memory systems.

## Recommended next action

Run a bounded real-operator follow-up using a small LLM or API-backed agent that writes natural-language doctrine memories, with exact-fact and exemplar baselines plus retrieval-noise controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Operator Doctrine Memory Under Retrieval Noise
- Success threshold: Doctrine memory improves novel-query accuracy by at least 10 percentage points over exact fact recall and at least 5 points over raw exemplar memory under nonzero retrieval noise, without increasing memory-token footprint above exemplar memory.
- Stop condition: Stop if doctrine memory fails to beat exact fact recall by 5 percentage points on novel queries in a smoke run with at least 200 queries, or if retrieval noise collapses doctrine performance to no-memory levels.

## Evidence references

- Artifact root: `<local-path>/projects/operator-model-memory-writes-reusable-doctrine-beyond-fact-recall-89276e47a694`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
