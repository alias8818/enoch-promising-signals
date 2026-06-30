# Residual-Summary KV Cache for Extreme Context on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-summary-kv-cache-for-extreme-context-on-cpu-8f6b642bd423`
Run ID: `residual-summary-kv-cache-for-extreme-context-on-cpu-8f6b642bd423-20260603T190943743834+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5bb884061b8a

## What looked useful

At 65,536 tokens with d=64, 128 queries, residual=1024, block=512, mean summaries compressed cache tokens by 56.99x and reduced attention time by 62.78x on the smooth task with cosine 0.8947 vs full attention. On needle retrieval, full attention recovered the target at cosine about 0.99999, while the summary cache target cosine was -0.0065, essentially the same failure as residual-only eviction.

## Boundaries and scale limits

Synthetic attention-only experiment; no trained transformer, real corpus, learned summarizer, long-context QA, perplexity, production serving, or 7B+ validation was tested.

## Claim scope

A CPU synthetic KV-cache probe up to 65,536 tokens shows that residual-window plus query-independent block-mean K/V summaries can approximate full attention on smooth block-structured old context with large cache and attention-time reductions, but fails sparse old-token needle retrieval.

## Why it stopped

No-paper closure: the bounded proxy directly falsified the broad simple-summary claim for sparse old-token retrieval, while preserving a useful smooth-context mechanism signal.

## Recommended next action

Do not write a paper from this run; run a bounded deepen follow-up testing multi-prototype or learned block summaries against the same smooth and needle controls before any larger model evaluation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-prototype residual-summary KV cache under sparse retrieval controls
- Success threshold: At 65,536 tokens, maintain at least 20x cache-token compression, smooth-task cosine versus full attention at least 0.85, and needle target cosine at least 0.50 while remaining at least 10x faster than full attention for the measured query batch.
- Stop condition: Stop if no tested multi-summary policy reaches needle target cosine 0.20 at 16,384 tokens under at least 8x compression, because that would indicate the approach still cannot preserve sparse retrieval.

## Evidence references

- Artifact root: `<local-path>/projects/residual-summary-kv-cache-for-extreme-context-on-cpu-8f6b642bd423`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
