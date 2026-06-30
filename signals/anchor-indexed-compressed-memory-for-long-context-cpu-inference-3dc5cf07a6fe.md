# Anchor-Indexed Compressed Memory for Long-Context CPU Inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-indexed-compressed-memory-for-long-context-cpu-inference-3dc5cf07a6fe`
Run ID: `anchor-indexed-compressed-memory-for-long-context-cpu-inference-3dc5cf07a6fe-20260621T022024140112+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bd2d277891e5

## What looked useful

Stable anchors plus compressed fact records can make long-context replay unnecessary for exact anchored-fact lookup in a bounded local probe. Across five additional seeds, anchor memory matched full-context exact retrieval and averaged +0.441 accuracy over flat lexical retrieval while using about 0.002% of full-context query text.

## Boundaries and scale limits

Evidence is synthetic and retrieval-level only. It does not measure real CPU LLM inference latency, model answer quality, noisy anchor extraction, KV-cache behavior, or natural long-context QA.

## Claim scope

In a deterministic synthetic anchored-fact corpus with 2,500 facts and 400 queries, anchor-indexed compressed memory preserved exact answer retrieval while reducing per-query context by about 99.9979% versus full-context replay and outperforming flat lexical retrieval.

## Why it stopped

Closed as no-paper useful signal because the result is a synthetic retrieval proxy, not direct publication-grade evidence for long-context CPU inference.

## Recommended next action

Run a bounded direct CPU LLM follow-up using noisy naturalistic transcripts, the same memory strategies, and metrics for answer accuracy, prompt tokens, wall-clock latency, and peak RSS.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM Validation of Anchor-Indexed Compressed Memory
- Success threshold: Anchor-indexed compressed memory retains at least 95% of full-context answer accuracy while reducing prompt tokens and median CPU response latency by at least 50% versus full-context replay, and beats flat lexical retrieval accuracy by at least 10 percentage points.
- Stop condition: Stop as negative if noisy anchor extraction drops anchor-memory accuracy below flat lexical retrieval or if prompt reduction does not produce a measurable CPU latency or memory benefit.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-indexed-compressed-memory-for-long-context-cpu-inference-3dc5cf07a6fe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
