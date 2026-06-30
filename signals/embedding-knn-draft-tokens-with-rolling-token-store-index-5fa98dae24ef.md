# Embedding-kNN draft tokens with rolling token-store index

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `embedding-knn-draft-tokens-with-rolling-token-store-index-5fa98dae24ef`
Run ID: `embedding-knn-draft-tokens-with-rolling-token-store-index-5fa98dae24ef-20260620T045513505010+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1ff5a6bb3738

## What looked useful

Best Tiny Shakespeare kNN accuracy was 10.03% versus 14.06% for rolling bigram, with draft-2 rate 1.65% and draft-4 rate 0.085%. A repeated-template control reached 89.62% kNN accuracy and 80.23% draft-2 rate, showing the mechanism works only under high context repetition in this setup.

## Boundaries and scale limits

CPU-only local proxy over 30k-token word/punctuation streams; no transformer verifier, learned hidden-state embeddings, approximate nearest-neighbor serving path, or GPT-2-class baseline.

## Claim scope

A simple rolling store of random-vector context embeddings with cosine kNN can recover draftable tokens in highly repeated template streams, but did not beat a rolling bigram baseline or produce useful multi-token draft rates on a 30k-token Tiny Shakespeare proxy.

## Why it stopped

Proxy-scale early falsification for practical real-text drafting: the simple embedding-kNN store did not beat a cheap bigram baseline and produced rare multi-token drafts, although a repeated-template control was positive.

## Recommended next action

Stop this simple random-embedding version as no-paper; if continuing, run a bounded learned-hidden-state follow-up against rolling n-gram/cache baselines with verifier acceptance and tokens/sec metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned hidden-state rolling kNN draft tokens versus n-gram cache baselines
- Success threshold: At least 20% relative improvement over the best cheap rolling baseline in accepted draft tokens per position, with no end-to-end throughput regression in the local benchmark.
- Stop condition: Stop if learned embeddings fail to beat the best rolling n-gram/cache baseline on accepted draft tokens per position or if index latency erases the draft-token speedup.

## Evidence references

- Artifact root: `<local-path>/projects/embedding-knn-draft-tokens-with-rolling-token-store-index-5fa98dae24ef`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
