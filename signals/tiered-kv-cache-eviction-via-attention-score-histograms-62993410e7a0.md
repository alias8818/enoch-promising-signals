# Tiered KV Cache Eviction via Attention-Score Histograms

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiered-kv-cache-eviction-via-attention-score-histograms-62993410e7a0`
Run ID: `tiered-kv-cache-eviction-via-attention-score-histograms-62993410e7a0-20260608T214407893081+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7b7a88ab66bb

## What looked useful

Histogram-tail eviction improved retained dense attention mass over recency by 33.78%, 18.67%, and 9.88% at 12.5%, 25%, and 50% cache budgets; it also beat observed cumulative attention by 0.98%, 1.75%, and 1.71%.

## Boundaries and scale limits

Trace-only, short sequence length 128, built-in fallback text snippets, no end-to-end KV-cache implementation, no latency, no perplexity/task quality, no compression-tier movement costs, and no long-context benchmark coverage.

## Claim scope

On a bounded distilgpt2 dense-attention trace probe with 12 short built-in natural-language samples, histogram-tail scoring retained more dense attention mass than sliding-window recency and slightly more than observed cumulative-attention scoring at equal token budgets.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a bounded trace proxy, not a full validation of tiered KV-cache eviction.

## Recommended next action

Run a bounded deepen test that implements actual decode-time KV eviction for distilgpt2 or GPT-2 small and measures perplexity plus latency/memory against recency and cumulative-attention controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Decode-time KV eviction quality and latency check
- Success threshold: At a 25% KV budget, histogram-tail should reduce perplexity degradation by at least 10% relative to sliding-window recency and be no worse than observed cumulative attention, while preserving a measurable active-KV memory reduction.
- Stop condition: Stop if histogram-tail is not better than recency on perplexity/next-token loss or if its bookkeeping overhead erases the practical memory/latency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-kv-cache-eviction-via-attention-score-histograms-62993410e7a0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
