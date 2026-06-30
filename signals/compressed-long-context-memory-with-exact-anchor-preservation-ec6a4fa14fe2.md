# Compressed Long-Context Memory with Exact Anchor Preservation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-long-context-memory-with-exact-anchor-preservation-ec6a4fa14fe2`
Run ID: `compressed-long-context-memory-with-exact-anchor-preservation-ec6a4fa14fe2-20260607T225425346990+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/4965522b9dfe

## What looked useful

Marked anchor-preserving compression reached mean exact anchor recall of 0.789, 0.912, 0.961, and 1.000 at 1%, 2%, 5%, and 10% byte budgets, while the best generic marked-anchor baseline reached 0.005, 0.021, 0.043, and 0.085. The method failed on unmarked anchors and degraded when exact anchor spans exceeded tiny budgets.

## Boundaries and scale limits

Documents were generated synthetic texts up to 256k filler tokens with 16-256 anchors; no neural model was trained or evaluated; anchors were either explicitly regex-marked or unmarked; the result does not validate real-document anchor detection, downstream model use, or full long-context training.

## Claim scope

In a synthetic long-document key-value retrieval benchmark, exact preservation of explicitly marked anchor spans recovers anchors far better than generic head/tail, uniform-window, or random-window retention at the same byte budget when the exact anchor spans fit the budget.

## Why it stopped

This run produced a synthetic/proxy useful signal, not full validation: the mechanism works for detectable budget-fitting anchors but does not establish learned detection, real-corpus robustness, or neural model answer quality.

## Recommended next action

Run a bounded direct follow-up where a small local language model answers real or semi-real long-context QA from compressed memories produced by exact anchor preservation versus retrieval and truncation baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-read QA from anchor-preserving compressed memory
- Success threshold: At least 20 percentage points absolute exact-match improvement over the best equal-byte baseline, with no more than 5 percentage points degradation on non-anchor questions and detector recall above 0.95.
- Stop condition: Stop if anchor detector recall is below 0.8 on the dataset or if model exact-match improvement over the best equal-byte baseline is below 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-long-context-memory-with-exact-anchor-preservation-ec6a4fa14fe2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
