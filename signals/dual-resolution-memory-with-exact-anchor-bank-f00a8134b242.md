# Dual-Resolution Memory with Exact Anchor Bank

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `dual-resolution-memory-with-exact-anchor-bank-f00a8134b242`
Run ID: `dual-resolution-memory-with-exact-anchor-bank-f00a8134b242-20260525T033811119411+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/94d9ebb9dd35

## What looked useful

Across 20 seeds and 120,000 synthetic memories per seed, dual_anchor reached anchor accuracy 0.149/0.320/0.661/1.000 at 32/64/128/256 KiB while uniform_sketch reached 0.068/0.073/0.086/0.111 and exact_lru reached 0.009/0.017/0.034/0.068. All dual_anchor topic accuracies were 1.0.

## Boundaries and scale limits

No natural-language retrieval, learned salience, transformer integration, GPT-2-small-class training, long-context serving, or large-scale corpus validation was performed. Synthetic salience is oracle-like, and the baseline set is limited.

## Claim scope

Synthetic structured-memory benchmark only: under equal byte budgets, an exact bank for generated high-salience anchors plus coarse topic counts improves rare key-value anchor recall over recency-only exact storage and, except at the smallest 16 KiB budget, over uniform count-min-style compression while preserving topic majority recall.

## Why it stopped

Synthetic mechanism evidence is useful but not paper-ready; the run directly tested structured anchor recall and only proxied real model memory behavior.

## Recommended next action

Run one bounded deepen experiment with non-oracle salience on a small natural-language retrieval or GPT-2-small-class memory task using the same equal-budget controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-oracle anchor selection for dual-resolution memory on a small language-memory task
- Success threshold: At a matched memory budget, dual-resolution memory improves exact fact recall by at least 20% relative over the best baseline while keeping coarse retrieval quality or perplexity within 2% of the best baseline.
- Stop condition: Stop if non-oracle anchor selection fails to beat the best equal-budget baseline on exact recall in two independent seeds or if coarse quality regresses by more than 5%.

## Evidence references

- Artifact root: `<local-path>/projects/dual-resolution-memory-with-exact-anchor-bank-f00a8134b242`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
