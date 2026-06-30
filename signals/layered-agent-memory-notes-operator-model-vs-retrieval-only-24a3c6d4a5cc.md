# Layered Agent Memory: Notes+Operator-Model vs Retrieval-Only

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-agent-memory-notes-operator-model-vs-retrieval-only-24a3c6d4a5cc`
Run ID: `layered-agent-memory-notes-operator-model-vs-retrieval-only-24a3c6d4a5cc-20260620T012100389486+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/17cd328b4fe6

## What looked useful

Across 5 seeds with 40,800 synthetic notes and 12,000 queries, layered notes+operator-model reached 1.0000 mean accuracy at k=10 while retrieval-only reached 0.33675; at k=120 retrieval-only recovered to 0.9910, showing the main signal is context-budget efficiency under noisy history.

## Boundaries and scale limits

Synthetic only; no real operator traces, no LLM-in-the-loop action generation, no embedding/reranker retrieval baseline, and no privacy-preserving extraction validation. Retrieval-only nearly closed the gap when k=120 recovered the full relevant per-operator history.

## Claim scope

In a deterministic synthetic repeated-agent replay with noisy notes, stale contradicted preferences, and constrained top-k retrieval, a recency-weighted notes+operator-model memory layer selected operator-consistent actions more accurately than naive retrieval-only.

## Why it stopped

Closed as no-paper useful signal: local synthetic evidence supports the context-efficiency mechanism but is not direct/full validation of layered agent memory on real operator behavior.

## Recommended next action

Run a bounded real-trace or human-authored replay with fixed context budget, embedding retrieval plus reranking, and held-out operator preference labels before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human-authored repeated-agent memory replay with embedding retrieval control
- Success threshold: Layered memory improves accuracy by at least 10 percentage points over embedding+reranking retrieval-only at the same context budget on at least 500 held-out labeled queries, without losing to retrieval-only on more than 2 of 8 preference facets.
- Stop condition: Stop if the stronger retrieval-only baseline is within 3 percentage points of layered memory or if labeled human-authored traces cannot be produced without private/operator data exposure.

## Evidence references

- Artifact root: `<local-path>/projects/layered-agent-memory-notes-operator-model-vs-retrieval-only-24a3c6d4a5cc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
