# Multi-encoder natural-document anchor recall under chunk length and position

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `multi-encoder-natural-document-anchor-recall-under-chunk-l-d4b842fe28`
Run ID: `multi-encoder-natural-document-anchor-recall-under-chunk-l-d4b842fe28-20260629T220743536301+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Pretrained Dense Retriever Anchor Recall Under Long-Chunk Dilution: enoch://control-plane/projects/pretrained-dense-retriever-anchor-recall-under-long-chunk-dc330080ec/runs/pretrained-dense-retriever-anchor-recall-under-long-chunk-dc330080ec-20260629T204348741762+0000
- Parent run decision: Public-Corpus Dense Retriever Anchor Recall Under Chunk Length and Position: enoch://control-plane/projects/public-corpus-dense-retriever-anchor-recall-under-chunk-le-8522f45d22/runs/public-corpus-dense-retriever-anchor-recall-under-chunk-le-8522f45d22-20260629T215208884692+0000

## What looked useful

Lexical TF-IDF reached 0.972 Recall@1 overall, while e5-small-v2 reached 0.514, bge-small-en-v1.5 reached 0.271, and all-MiniLM-L6-v2 reached 0.250. E5 degraded from 0.806 Recall@1 at 128-word chunks to 0.278-0.306 at 512-768-word chunks, indicating chunk length and position can strongly affect dense anchor recall.

## Boundaries and scale limits

Small controlled benchmark only: inserted anchors rather than naturally occurring gold facts, 144 medium-run queries, same-document candidate pools, and simple mean-pooled transformer embeddings rather than exhaustive model-specific retrieval wrappers.

## Claim scope

In a controlled benchmark using three Project Gutenberg books, four inserted natural-language anchor facts, three anchor positions, four chunk lengths, and same-document retrieval pools, dense neural encoders showed materially lower anchor Recall@1 than a local lexical TF-IDF baseline, especially at 512-768 word chunks.

## Why it stopped

The local benchmark produced a reproducible mixed/useful signal, but the evidence is controlled and bounded rather than publication-grade direct validation.

## Recommended next action

Stop this run as no-paper useful evidence; deepen with a larger natural-anchor benchmark using official encoder wrappers and heterogeneous retrieval pools.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-anchor dense retrieval degradation under chunk length and position
- Success threshold: Dense encoders show a statistically clear Recall@1 drop of at least 15 percentage points from short to long chunks or from middle to edge positions, with lexical or hybrid retrieval reducing the drop by at least half.
- Stop condition: Stop if official-wrapper dense encoders maintain Recall@1 within 5 percentage points across chunk lengths and positions or if lexical/hybrid baselines do not outperform dense retrieval on anchor localization.

## Evidence references

- Artifact root: `<local-path>/projects/multi-encoder-natural-document-anchor-recall-under-chunk-l-d4b842fe28`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
