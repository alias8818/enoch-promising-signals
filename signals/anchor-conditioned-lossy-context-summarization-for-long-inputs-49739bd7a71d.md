# Anchor-conditioned lossy context summarization for long inputs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-conditioned-lossy-context-summarization-for-long-inputs-49739bd7a71d`
Run ID: `anchor-conditioned-lossy-context-summarization-for-long-inputs-49739bd7a71d-20260621T195243010660+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9fb28cddb478

## What looked useful

Anchor conditioning is a strong compression control when the anchor is already resolved to text present in the source, but the anchor-only method collapses near random/truncation when the provided alias is absent from the source. The idea needs anchor normalization or query-aware semantic retrieval before it is more than lexical retrieval.

## Boundaries and scale limits

This was a dependency-free CPU synthetic probe with 1,000 cases, 480 sentences per case, and lexical sentence-selection compressors. It did not test trained summarizers, natural corpora, semantic entity linking, downstream LLM answer generation, latency at serving scale, or large-model long-context behavior.

## Claim scope

In a synthetic long-document fact-recovery benchmark with exact source-visible lexical anchors, anchor-conditioned lossy selection preserved the answer-bearing sentence at 100% recovery across 1 to 16 retained-sentence budgets, while unconditioned first-k/random/generic summaries recovered near 0 to 4.5%.

## Why it stopped

The result is a synthetic/proxy mechanism test, not full validation; it supports exact-anchor preservation but early-falsifies the stronger standalone claim under a simple alias-mismatch control.

## Recommended next action

Stop this run as no-paper useful signal; next, run a bounded natural-corpus QA probe with explicit entity linking or embedding-based anchor resolution before compression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Semantic anchor resolution for lossy long-context compression
- Success threshold: At a fixed compression budget of at most 10% of source sentences or tokens, semantic anchor-conditioned compression improves answer-bearing passage recovery by at least 20 absolute percentage points over anchor-only lexical compression and at least 10 points over query-conditioned lexical matching, with no increase in hallucinated downstream answers.
- Stop condition: Stop if semantic anchor resolution improves recovery by less than 5 absolute percentage points over query-conditioned lexical matching or if most errors are caused by unresolved anchors rather than compression.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-conditioned-lossy-context-summarization-for-long-inputs-49739bd7a71d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
