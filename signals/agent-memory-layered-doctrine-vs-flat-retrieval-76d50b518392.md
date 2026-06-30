# Agent Memory: Layered Doctrine vs. Flat Retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-memory-layered-doctrine-vs-flat-retrieval-76d50b518392`
Run ID: `agent-memory-layered-doctrine-vs-flat-retrieval-76d50b518392-20260621T100134292023+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/92728ff62b1b

## What looked useful

Layered doctrine/key/recency memory reached 1.000 accuracy and 0.000 stale-violation rate over 430 scored tasks; flat retrieval reached 0.907 accuracy with 0.058 stale-violation rate.

## Boundaries and scale limits

Proxy-only evidence: 10 seeds, 10 generated domains per seed, no LLM generation, no embedding model, no real replay corpus, and no deployed agent loop.

## Claim scope

In a deterministic synthetic replay benchmark with explicit memory keys/layers, layered doctrine memory eliminated stale and noisy retrieval errors that remained in flat lexical retrieval.

## Why it stopped

Closed as useful proxy evidence, not full validation; the run did not test real agent traces or LLM-in-the-loop behavior.

## Recommended next action

Run a bounded direct-evidence follow-up using realistically authored multi-session agent traces with an embedding or LLM retriever baseline and ablations for doctrine priority, key extraction, and recency resolution.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layered Doctrine Memory on Realistic Multi-Session Agent Replays
- Success threshold: Layered memory improves accuracy by at least 5 percentage points over flat embedding retrieval and cuts stale/doctrine violations by at least 50% on at least 100 realistic replay tasks.
- Stop condition: Stop if layered memory fails to improve accuracy or violation rate over the stronger flat baseline, or if key/layer extraction errors dominate the claimed mechanism.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-layered-doctrine-vs-flat-retrieval-76d50b518392`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
