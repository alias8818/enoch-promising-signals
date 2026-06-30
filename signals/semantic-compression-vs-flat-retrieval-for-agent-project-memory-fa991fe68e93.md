# Semantic Compression vs Flat Retrieval for Agent Project Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `semantic-compression-vs-flat-retrieval-for-agent-project-memory-fa991fe68e93`
Run ID: `semantic-compression-vs-flat-retrieval-for-agent-project-memory-fa991fe68e93-20260611T142526143749+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/4ab3cbe94cf3

## What looked useful

Compression was neutral at a generous 260-token budget (0.9960 vs 0.9954 exact), strongly better at an 80-token budget where summaries fit (0.9960 vs 0.8185), and worse at a 40-token budget below summary size (0.0922 compact and 0.0000 verbose vs 0.4778 flat).

## Boundaries and scale limits

Synthetic structured facts only; deterministic lossless compression for retained fields; lexical BM25 retrieval; deterministic regex reader; no real agent traces, no embedding retriever, no LLM-generated summaries, no natural-language omission audit, and no end-to-end agent task completion.

## Claim scope

On a deterministic synthetic current-state project-memory benchmark with 7,560 raw events, 360 compressed entity summaries, and 1,758 queries, structured semantic compression improves answer accuracy over flat raw-event retrieval only when the context budget is tight but large enough to fit a compressed summary.

## Why it stopped

Bounded synthetic evidence supports a budget-dependent mechanism but is not direct or realistic enough for a paper-ready claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the observed budget boundary on realistic agent traces with embedding retrieval and LLM-generated summaries plus omission audits.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic Trace Test for Semantic Project-Memory Compression
- Success threshold: At least a 10 percentage point exact-answer improvement over the best flat baseline in the scarce-but-summary-fits budget regime, with less than 2 percentage points degradation in generous budgets and audited summary omission rate below 5%.
- Stop condition: Stop if compression fails to beat the best flat baseline by 5 percentage points in the scarce-but-summary-fits regime or if summary omissions exceed 10% on audited facts.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-compression-vs-flat-retrieval-for-agent-project-memory-fa991fe68e93`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
