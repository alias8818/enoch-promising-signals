# Exact Anchor Ledger for Compressed Agent Episodic Memory

Status: `useful_signal`
Project ID: `exact-anchor-ledger-for-compressed-agent-episodic-memory-880ec5c31eee`
Run ID: `exact-anchor-ledger-for-compressed-agent-episodic-memory-880ec5c31eee-20260516T000040498468+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/908298541335

## What looked useful

The anchor-ledger mechanism consistently preserves selected exact commitments/constraints/provenance better than matched-budget controls and detects ledger mutation, but it trades off general all-fact recall because hashes and provenance consume budget.

## Boundaries and scale limits

Synthetic facts only; no real agent transcripts, no LLM summarization or retrieval QA, no noisy-anchor labeling study, and no integration with a live agent memory system. All runs were local CPU-scale proxy evaluations with 40 seeds and 7,200 facts per seed.

## Claim scope

In a deterministic synthetic episodic-memory benchmark with pre-labeled exact anchors, a hash-chained exact-anchor ledger improves exact recall of anchor-labeled facts by about 3.9x over recency-first extractive compression and about 4.5x over random anchoring at matched byte budgets from 2% to 20% of the full log.

## Why it stopped

Synthetic proxy supports the mechanism but is not direct/full validation of compressed agent episodic memory in real deployments.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should test EAL on real or semi-real agent traces with LLM compression and retrieval QA at matched storage budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact-anchor ledger on real agent traces with LLM compression
- Success threshold: EAL achieves at least 2x exact anchor recall over the strongest matched-budget baseline, retains at least 95% ledger tamper detection on injected corruptions, and adds less than 20% retrieval latency overhead in the tested prototype.
- Stop condition: Stop if EAL fails to beat the strongest matched-budget baseline by 25% relative anchor recall on real/semi-real traces or if latency/storage overhead makes the mechanism dominated by simpler extractive retention.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-ledger-for-compressed-agent-episodic-memory-880ec5c31eee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
