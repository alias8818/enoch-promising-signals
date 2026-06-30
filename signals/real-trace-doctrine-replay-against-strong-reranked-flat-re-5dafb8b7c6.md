# Real-trace doctrine replay against strong reranked flat retrieval

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `53`
Project ID: `real-trace-doctrine-replay-against-strong-reranked-flat-re-5dafb8b7c6`
Run ID: `real-trace-doctrine-replay-against-strong-reranked-flat-re-5dafb8b7c6-20260630T044052498954+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 10, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- weak evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Direct Trace Doctrine Memory vs Reranked Flat Retrieval: enoch://control-plane/projects/direct-trace-doctrine-memory-vs-reranked-flat-retrieval-f4fb26d64d/runs/direct-trace-doctrine-memory-vs-reranked-flat-retrieval-f4fb26d64d-20260630T034314249898+0000
- Parent run decision: Operator-Doctrine Memory Beats Flat Vector Retrieval on Repeated Multi-Turn Tasks: enoch://control-plane/projects/operator-doctrine-memory-beats-flat-vector-retrieval-on-repeated-multi-turn-tasks-7b99d40be8c8/runs/operator-doctrine-memory-beats-flat-vector-retrieval-on-repeated-multi-turn-tasks-7b99d40be8c8-20260629T152901995504+0000

## What looked useful

A strong reranked flat retriever with heading metadata matched doctrine-section memory on all-terms recall (0.80 vs 0.80) and expected-section recall (0.90 vs 0.90), while doctrine memory improved mean term coverage by only 0.0458.

## Boundaries and scale limits

Proxy-only local corpus: no sanitized multi-session real traces, no temporal memory snapshots, no noisy metadata replay, no operator private payloads, and no LLM answer-quality judge.

## Claim scope

On a 20-query doctrine-replay proxy derived from the local controller prompt and project doctrine files, doctrine-section retrieval slightly improved mean anchor-term coverage but did not improve all-anchor recall or expected-section recall over a strengthened reranked flat baseline.

## Why it stopped

Early proxy result did not show a material doctrine-memory win over a strengthened flat baseline; decisive real-trace evidence is absent from this workspace.

## Recommended next action

Stop this scaffold as no-paper proxy evidence; only reopen with a sanitized real repeated-agent trace corpus and predeclared answer-quality scoring.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-doctrine-replay-against-strong-reranked-flat-re-5dafb8b7c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
