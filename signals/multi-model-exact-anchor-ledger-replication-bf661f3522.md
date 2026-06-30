# Multi-Model Exact Anchor Ledger Replication

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `multi-model-exact-anchor-ledger-replication-bf661f3522`
Run ID: `multi-model-exact-anchor-ledger-replication-bf661f3522-20260529T035751217222+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Exact Anchor Evidence Ledger for Tiny Agents: enoch://control-plane/projects/exact-anchor-evidence-ledger-for-tiny-agents-36d47913c507/runs/exact-anchor-evidence-ledger-for-tiny-agents-36d47913c507-20260527T154913869242+0000
- Parent run decision: Real-LLM Exact Anchor Ledger Benchmark: enoch://control-plane/projects/real-llm-exact-anchor-ledger-benchmark-49bd42e7fe/runs/real-llm-exact-anchor-ledger-benchmark-49bd42e7fe-20260528T224713331607+0000

## What looked useful

The exact-ledger mechanism behaves as expected for exact surviving anchors, but in this Tier-2 bounded test it provides no observed recovery advantage over a real BM25 baseline and is brittle to anchor corruption/drop. The collision ablation confirms uniqueness is required.

## Boundaries and scale limits

Multi-model behavior was proxied by deterministic text transformations rather than actual independently trained or hosted LLMs; records retained unique entity/context text, which made no-anchor BM25 retrieval strong; no large-model, long-context, or real deployment validation was run.

## Claim scope

On a deterministic synthetic exact-payload recovery task with 6000 records, 3 fixed seeds, 5 text-output channels, BM25 baselines, anchor-drop/corrupt controls, and collision ablation, exact anchor ledgers only match retrieval baselines when exact unique anchors survive and fail when anchors are corrupted or absent.

## Why it stopped

Tier-2 synthetic validation with fixed seeds, ablations, and a real baseline did not support the claimed advantage of exact anchor ledger replication over standard retrieval.

## Recommended next action

Stop this branch as no-paper useful negative evidence unless a new direct test removes ordinary lexical identifiers and uses actual independently trained models.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/multi-model-exact-anchor-ledger-replication-bf661f3522`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
