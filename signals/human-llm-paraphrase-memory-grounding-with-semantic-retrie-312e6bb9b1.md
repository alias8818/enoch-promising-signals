# Human/LLM Paraphrase Memory Grounding With Semantic Retrieval Baselines

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `human-llm-paraphrase-memory-grounding-with-semantic-retrie-312e6bb9b1`
Run ID: `human-llm-paraphrase-memory-grounding-with-semantic-retrie-312e6bb9b1-20260519T122606557307+0000`

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

- Internal Enoch project: Human/LLM Paraphrase Memory Grounding With Semantic Retrieval Baselines: internal_generated:human-llm-paraphrase-memory-grounding-with-semantic-retrie-312e6bb9b1

## What looked useful

Semantic retrieval beat BM25 by +14.76 top-1 points on ChatGPT/Quora paraphrases and +3.00 points on Redis LLM paraphrases, with shuffled-label ablations at chance. On human MRPC, semantic retrieval was only +0.24 points over BM25 with mixed seed-level signs, so the broad human/LLM claim is not supported.

## Boundaries and scale limits

The evaluation used 3 public pair datasets, 5 fixed seeds, 500 queries per source per seed, 101-candidate query-specific banks, and one small pretrained embedding model. It did not test downstream generation, real agent memory traces, multilingual data, long-context memories, larger embedding models, cross-encoder reranking, or production vector stores.

## Claim scope

In a local retrieval-only benchmark with public English paraphrase pairs, MiniLM semantic retrieval materially improves top-1 paraphrase-to-memory retrieval for LLM-generated paraphrases under TF-IDF hard distractors, especially low lexical-overlap queries, but does not materially improve over BM25/TF-IDF on human MRPC paraphrases.

## Why it stopped

Medium fixed-seed evidence supports a useful LLM-paraphrase retrieval mechanism but gives mixed support for the stated human/LLM grounding claim and is retrieval-only, so it is not paper-ready.

## Recommended next action

Stop this paper path; run a bounded deepen follow-up only if using naturalistic memory traces and end-to-end grounded answer metrics rather than pair-only retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Naturalistic Paraphrase Memory Grounding With End-to-End Answer Metrics
- Success threshold: Semantic or semantic-plus-rerank retrieval improves top-1 by at least 10 absolute points over BM25 on both human-style and LLM-style low-overlap queries, or improves grounded answer F1 by at least 5 absolute points with no unsupported-answer increase.
- Stop condition: Stop if BM25 remains within 3 top-1 points of semantic retrieval on human-style low-overlap memory queries or if retrieval gains do not improve end-to-end grounded answers.

## Evidence references

- Artifact root: `<local-path>/projects/human-llm-paraphrase-memory-grounding-with-semantic-retrie-312e6bb9b1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
