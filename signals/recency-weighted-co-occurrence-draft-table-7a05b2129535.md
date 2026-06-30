# Recency-Weighted Co-occurrence Draft Table

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `recency-weighted-co-occurrence-draft-table-7a05b2129535`
Run ID: `recency-weighted-co-occurrence-draft-table-7a05b2129535-20260522T175004441374+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/77a8ea6ac213

## What looked useful

Across 10 seeds, best recency weighting improved drift top-4 recall by mean +0.321 absolute and drift MRR by mean +0.453 absolute versus global co-occurrence; stationary recall delta was near zero at mean -0.00044.

## Boundaries and scale limits

Synthetic table-level evaluation only: 256-token vocabulary, 64 recurring context tokens, 8 segments of 4000 tokens, 10 random seeds. No real corpus, tokenizer, language model, speculative decoding acceptance, latency, or large-vocabulary memory validation was performed.

## Claim scope

In controlled synthetic token streams with explicit pair-association drift, an exponential recency-weighted co-occurrence draft table improves top-4 next-token candidate recall and MRR versus a global unweighted co-occurrence table while remaining essentially tied on a stationary control stream.

## Why it stopped

Closed as a no-paper useful signal: the mechanism is supported in a controlled synthetic table-level test, but this is not full validation of end-to-end draft generation.

## Recommended next action

Run a bounded deepen follow-up that plugs the recency-weighted table into a small language-model or n-gram draft/verification loop on chronological real text and measures acceptance rate, latency, memory, and candidate recall against cache and unweighted co-occurrence baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Recency-weighted co-occurrence draft table on chronological real text
- Success threshold: At least +5% relative candidate recall or draft acceptance improvement over the strongest equal-memory baseline after detected shifts, with no more than 2% relative degradation on stationary/no-shift windows.
- Stop condition: Stop if recency weighting fails to beat the strongest equal-memory baseline on both candidate recall and draft acceptance in two independent chronological shards, or if table maintenance overhead erases throughput gains.

## Evidence references

- Artifact root: `<local-path>/projects/recency-weighted-co-occurrence-draft-table-7a05b2129535`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
