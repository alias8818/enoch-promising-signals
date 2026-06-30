# Exact Anchor Retrieval with Compressed Context Skipping

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-retrieval-with-compressed-context-skipping-7ddaba965edc`
Run ID: `exact-anchor-retrieval-with-compressed-context-skipping-7ddaba965edc-20260603T190022009087+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3b9552bce518

## What looked useful

Exact anchor retrieval under compressed context skipping requires explicit preservation of anchor membership. Bloom-style compressed membership supports exact retrieval with low read cost, while generic lossy summaries are not viable for exact anchors unless paired with fallback scanning.

## Boundaries and scale limits

Algorithmic synthetic benchmark only; no transformer attention, learned compression, real document corpus, serving latency, or large-model validation was tested.

## Claim scope

In deterministic synthetic anchor-block corpora up to 1024 blocks and 8192 anchors, exact compressed membership summaries can preserve 100% anchor payload retrieval while reading about 3.29% to 7.91% of full context on average; lossy fixed-budget summaries fail exact retrieval in proportion to omitted anchors.

## Why it stopped

Synthetic mechanism evidence is useful but not direct model evidence or full validation; stopping as no-paper useful signal rather than claiming publication readiness.

## Recommended next action

Run a bounded deepen test with a small transformer or LLM prompt/runtime that uses compressed anchor summaries to select blocks, comparing exact answer rate and token/latency cost against dense long-context retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-facing compressed anchor skip retrieval
- Success threshold: At least 99% exact-match retrieval, no more than 1 percentage point below dense baseline, with mean consumed tokens at or below 10% of dense context on held-out synthetic and semi-real text corpora.
- Stop condition: Stop if exact-match accuracy is below 95%, if the method requires fallback scanning for more than 5% of queries, or if mean consumed tokens exceed 20% of dense context.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-retrieval-with-compressed-context-skipping-7ddaba965edc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
