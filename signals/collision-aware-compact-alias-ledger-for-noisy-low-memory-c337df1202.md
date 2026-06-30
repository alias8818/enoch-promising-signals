# Collision-Aware Compact Alias Ledger for Noisy Low-Memory Agent Consistency

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `collision-aware-compact-alias-ledger-for-noisy-low-memory-c337df1202`
Run ID: `collision-aware-compact-alias-ledger-for-noisy-low-memory-c337df1202-20260519T204656388970+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: N-Gram KV Suffix Ledger for Low-Memory Agent Consistency: enoch://control-plane/projects/n-gram-kv-suffix-ledger-for-low-memory-agent-consistency-822c01664f0f/runs/n-gram-kv-suffix-ledger-for-low-memory-agent-consistency-822c01664f0f-20260519T202818718270+0000
- Parent run decision: Alias-Robust Suffix Ledger for Low-Memory Agent Consistency: enoch://control-plane/projects/alias-robust-suffix-ledger-for-low-memory-agent-consistenc-a5bf24e296/runs/alias-robust-suffix-ledger-for-low-memory-agent-consistenc-a5bf24e296-20260519T204150438842+0000

## What looked useful

Collision awareness is useful as a mechanism when collisions are frequent and a small stash is available, but the proposed ledger does not show a broad enough advantage over a simpler compact hash baseline to justify paper writing.

## Boundaries and scale limits

Synthetic aliases only; no real LLM agent traces, no natural-language ambiguity, no measured per-method runtime memory beyond estimated bytes, and no publication-grade robustness beyond fixed-seed medium grids.

## Claim scope

On a synthetic fixed-seed low-memory alias/fact stream, a collision-aware ledger with a bounded stash consistently improves over exact LRU and over its no-stash ablation; it is near-parity with compact hash on the main Tier 2 grid and modestly better only under collision stress.

## Why it stopped

Medium synthetic evidence is mixed: the ledger beats exact LRU and its no-stash ablation, but main-grid accuracy is effectively tied with compact hash, so this is useful no-paper evidence rather than paper-positive support.

## Recommended next action

Stop paper escalation for this run; run one bounded trace-based follow-up only if real or realistic alias-heavy agent memory transcripts can be evaluated against compact hash at matched memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Based Alias Ledger Evaluation Against Compact Hash
- Success threshold: At least +5 percentage points mean consistency accuracy over compact hash at matched memory, no increase in wrong-answer rate, and positive paired deltas on at least 80% of fixed splits.
- Stop condition: Stop if the ledger is within 1 percentage point of compact hash or has a higher wrong-answer rate on the primary trace benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/collision-aware-compact-alias-ledger-for-noisy-low-memory-c337df1202`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
