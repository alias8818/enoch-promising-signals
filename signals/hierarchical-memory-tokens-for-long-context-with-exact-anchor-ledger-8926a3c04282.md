# Hierarchical Memory Tokens for Long Context with Exact Anchor Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hierarchical-memory-tokens-for-long-context-with-exact-anchor-ledger-8926a3c04282`
Run ID: `hierarchical-memory-tokens-for-long-context-with-exact-anchor-ledger-8926a3c04282-20260517T034006482875+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b9524683d7e6

## What looked useful

Exact anchor ledger achieved 100% exact retrieval through 200k facts with 3-6 query reads, while 512-entry tail/sample controls fell to about 0.2% at 200k and lossy hierarchical memory stayed near 6-7% recall.

## Boundaries and scale limits

No neural model was trained; memory tokens were deterministic summaries; anchors were clean synthetic IDs; exact ledger storage scales linearly with number of facts; largest run was 200k facts on local CPU/Python.

## Claim scope

Synthetic deterministic anchor-value retrieval up to 200k generated facts: an exact anchor ledger paired with hierarchical memory summaries preserves exact lookup accuracy with small query-time read counts.

## Why it stopped

No-paper closure: this run is a synthetic retrieval mechanism result, not direct neural architecture validation or publication-grade evidence.

## Recommended next action

Run a bounded deepen study with a small transformer/GPT-2-small-class synthetic QA task comparing equal-parameter baseline, lossy memory, and exact-ledger retrieval on end-to-end answer accuracy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Transformer QA Test for Exact Anchor Ledger Retrieval
- Success threshold: At 32k-token-equivalent synthetic contexts, exact-ledger retrieval improves exact answer accuracy by at least 20 absolute percentage points over the best equal-budget baseline while preserving at least 95% ledger retrieval recall.
- Stop condition: Stop if the exact ledger improves retrieval recall but fails to improve end-to-end answer accuracy by 10 absolute points over the best equal-budget baseline after controlled training/evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-memory-tokens-for-long-context-with-exact-anchor-ledger-8926a3c04282`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
