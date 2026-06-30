# Sliding-Window Cascade with Streaming Long-Context Reranking

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sliding-window-cascade-with-streaming-long-context-reranking-6f523110546a`
Run ID: `sliding-window-cascade-with-streaming-long-context-reranking-6f523110546a-20260528T051443336096+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b47b93fd62bd

## What looked useful

A narrow streaming shortlist is insufficient: shortlist 2 per 16-window block reached only 65.97% recall and 30.69% hard-case recall. A wider shortlist, 8 per 16-window block, averaged 98.95% recall and 97.88% hard-case recall across five seeds while passing 6.25% of windows to the downstream answerer, but it required scoring 50% of windows with the reranker.

## Boundaries and scale limits

Synthetic data only; deterministic hand-coded reranker; no neural reranker, real LLM answerer, natural long-context QA dataset, tokenizer-specific accounting, GPU/UMA memory measurement, or end-to-end latency measurement.

## Claim scope

In a deterministic synthetic long-context window-selection benchmark, streaming reranking can recover near-full answer-window recall while sending only 8 of 128 windows to the downstream answerer, but only when the first-stage streaming shortlist keeps 8 of every 16 windows for reranking.

## Why it stopped

Closed as no-paper useful signal because the supporting evidence is synthetic/proxy-only; it supports the mechanism but not a publication-grade long-context reranking claim.

## Recommended next action

Run a bounded real-model follow-up with a local lightweight reranker or embedding model plus a local LLM answerer on real long-context QA traces, measuring answer correctness, downstream token reduction, reranker cost, and end-to-end latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model streaming reranker for sliding-window long-context QA
- Success threshold: At least 95% answer correctness or answer-window recall, at least 75% downstream token reduction, and lower end-to-end latency than full-context answering on the same local stack.
- Stop condition: Stop if real-model recall falls below 90% at 75% downstream token reduction, or if reranker cost eliminates latency gains versus full-context answering.

## Evidence references

- Artifact root: `<local-path>/projects/sliding-window-cascade-with-streaming-long-context-reranking-6f523110546a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
