# Public-Corpus Dense Retriever Anchor Recall Under Chunk Length and Position

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `public-corpus-dense-retriever-anchor-recall-under-chunk-le-8522f45d22`
Run ID: `public-corpus-dense-retriever-anchor-recall-under-chunk-le-8522f45d22-20260629T215208884692+0000`

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

- Parent run decision: Pretrained Dense Retriever Anchor Recall Under Long-Chunk Dilution: enoch://control-plane/projects/pretrained-dense-retriever-anchor-recall-under-long-chunk-dc330080ec/runs/pretrained-dense-retriever-anchor-recall-under-long-chunk-dc330080ec-20260629T204348741762+0000
- Parent run decision: Exact-Anchor Retrieval Beats Dense at Extreme Context: enoch://control-plane/projects/exact-anchor-retrieval-beats-dense-at-extreme-context-dc355d3e3e20/runs/exact-anchor-retrieval-beats-dense-at-extreme-context-dc355d3e3e20-20260629T183200606789+0000

## What looked useful

Dense recall@10 averaged 0.181 for phrased queries and 0.227 for exact-anchor queries across 12 medium conditions, versus TF-IDF recall@10 of 0.840 and 0.889. Dense recall@10 fell from 0.295 at 128-word chunks to 0.108 at 768-word chunks for phrased queries, and from 0.294 for start anchors to 0.096 for end anchors. The encoder reported max_seq_length 256, consistent with truncation of late anchors in longer chunks.

## Boundaries and scale limits

Synthetic anchor facts, one dense encoder, one public filler corpus, 96 anchors and 192 distractors per condition in the medium grid, CPU-local inference only, no natural QA benchmark and no multi-encoder robustness sweep.

## Claim scope

In a controlled public-corpus-backed injection test using 20 Newsgroups filler and sentence-transformers/all-MiniLM-L6-v2, dense retrieval of short anchor facts degrades as chunk length increases and as anchors move later in the chunk; TF-IDF remains much higher on the same corpora.

## Why it stopped

Moderate controlled evidence supports the mechanism, but the result is synthetic-injection and single-encoder rather than publication-grade direct evidence.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded action is a multi-encoder confirmation on natural answer-bearing public documents before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-encoder natural-document anchor recall under chunk length and position
- Success threshold: Across at least three dense encoders, late anchors in chunks at or above 512 words have recall@10 at least 30 percentage points below start anchors or below a lexical/hybrid control, with the same direction on natural public documents.
- Stop condition: Stop if the effect disappears for stronger dense encoders on natural documents, if lexical controls also fail similarly, or if failures are explained entirely by an avoidable preprocessing bug rather than retriever behavior.

## Evidence references

- Artifact root: `<local-path>/projects/public-corpus-dense-retriever-anchor-recall-under-chunk-le-8522f45d22`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
