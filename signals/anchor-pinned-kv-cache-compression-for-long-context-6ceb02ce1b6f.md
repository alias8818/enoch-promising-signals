# Anchor-Pinned KV-Cache Compression for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-pinned-kv-cache-compression-for-long-context-6ceb02ce1b6f`
Run ID: `anchor-pinned-kv-cache-compression-for-long-context-6ceb02ce1b6f-20260620T030235560256+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2b41b650352d

## What looked useful

Anchor pinning achieved 1.000 anchor hit rate across three seeds and budgets 256/512/1024 on 32768-token caches, while recent and sink+recent baselines had 0.000 anchor hit. The same policy failed unknown far non-anchor retrieval and reduced local hit rate versus recency policies, showing a narrow mechanism with a clear tradeoff.

## Boundaries and scale limits

Synthetic single-layer attention proxy only; no real LLM, natural task, per-head/layer analysis, or production serving kernel was tested. Broad novelty is limited by close related work on retrieval-head and anchor-token-aware KV-cache compression.

## Claim scope

In a synthetic 32768-token attention-cache probe with explicitly known sparse anchor tokens, anchor-pinned retention preserved far-anchor retrieval under 32x to 128x token-count compression better than equal-budget recent, sink+recent, stride+recent, and key-norm+recent baselines.

## Why it stopped

The local evidence supports only a synthetic mechanism claim and exposes tradeoffs; it is not direct publication-grade evidence for long-context LLM KV-cache compression.

## Recommended next action

Stop this run as no-paper useful signal; the next concrete test is a bounded real-model evaluation on long-context anchor-fact retrieval with matched KV budgets and strong KV-compression baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model anchor-pinned KV retention on long-context fact retrieval
- Success threshold: At 4x or greater KV token reduction, anchor-pinned retention should recover at least 90% of full-cache anchor-fact accuracy and outperform sink+recent by at least 10 percentage points while losing no more than 5 percentage points on local-control prompts.
- Stop condition: Stop if anchor-pinned retention fails to beat sink+recent by 5 percentage points on anchor-fact accuracy at matched budget or causes more than 10 percentage points local-control degradation.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-pinned-kv-cache-compression-for-long-context-6ceb02ce1b6f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
