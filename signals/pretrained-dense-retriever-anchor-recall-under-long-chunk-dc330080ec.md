# Pretrained Dense Retriever Anchor Recall Under Long-Chunk Dilution

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `pretrained-dense-retriever-anchor-recall-under-long-chunk-dc330080ec`
Run ID: `pretrained-dense-retriever-anchor-recall-under-long-chunk-dc330080ec-20260629T204348741762+0000`

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

- Parent run decision: Exact-Anchor Retrieval Beats Dense at Extreme Context: enoch://control-plane/projects/exact-anchor-retrieval-beats-dense-at-extreme-context-dc355d3e3e20/runs/exact-anchor-retrieval-beats-dense-at-extreme-context-dc355d3e3e20-20260629T183200606789+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d384553fe35e

## What looked useful

Across three max-length-512 seed runs, anchor-only chunks reached mean recall@1 0.902. With 4 distractors and no truncation, recall@1 fell to 0.702 for front anchors, 0.220 for middle anchors, and 0.178 for end anchors. With 16 distractors and no truncation, recall@1 was 0.574 front, 0.241 middle, and 0.134 end. At 64+ distractors, front anchors stayed partially retrievable while middle/end anchors collapsed near zero as truncation removed the anchor.

## Boundaries and scale limits

One pretrained dense retriever, one synthetic fact/query template family, 256 anchors, exact cosine search, and no public-corpus, multi-model, overlap, reranking, or production retrieval validation.

## Claim scope

In a controlled synthetic anchor-fact retrieval probe using sentence-transformers/all-MiniLM-L6-v2, recall@1 drops substantially as unrelated distractor sentences are added to the embedded chunk; the drop appears before truncation and becomes near-total for middle/end anchors once long chunks exceed the encoder window.

## Why it stopped

Synthetic medium probe supports the mechanism but is not direct public-benchmark evidence or publication-grade validation.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded action is a public-corpus deepen test with multiple retrievers, lexical controls, and overlapping short-chunk baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Public-Corpus Dense Retriever Anchor Recall Under Chunk Length and Position
- Success threshold: Reproduce a minimum 20 percentage point recall@1 drop from short chunks to long non-truncated chunks for at least one dense retriever, while a short-overlap or lexical control preserves materially higher anchor recall.
- Stop condition: Stop if public-corpus dense recall does not degrade by at least 10 percentage points under matched non-truncated long chunks or if lexical/overlap controls fail similarly, indicating this synthetic mechanism does not transfer cleanly.

## Evidence references

- Artifact root: `<local-path>/projects/pretrained-dense-retriever-anchor-recall-under-long-chunk-dc330080ec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
