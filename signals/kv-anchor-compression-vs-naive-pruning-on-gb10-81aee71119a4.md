# KV Anchor Compression vs Naive Pruning on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-anchor-compression-vs-naive-pruning-on-gb10-81aee71119a4`
Run ID: `kv-anchor-compression-vs-naive-pruning-on-gb10-81aee71119a4-20260611T190941889667+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2dbc57aa11d0

## What looked useful

Anchor compression is worth deeper testing only where old tokens form high-mass reusable anchors; naive recency pruning predictably fails there, but synthetic oracle compression does not establish a production method.

## Boundaries and scale limits

No real LLM KV traces, no learned/online anchor selector, no perplexity or task metric, no optimized decode kernel, and calibrated sequence length was 8192 with 96 synthetic trials per condition.

## Claim scope

On synthetic single-query GB10 attention traces with planted old anchors, oracle query-weighted anchor compression can preserve full-attention output far better than equal-budget recency pruning when attention is anchor-dominated; the advantage is weak or mixed when attention is diffuse.

## Why it stopped

Closed as no-paper useful signal because current evidence is synthetic and oracle-assisted, not a direct/full validation.

## Recommended next action

Run a bounded deepen follow-up on real GPT-2-small-class KV traces with non-oracle anchor selection, matched KV budgets, and perplexity plus decode-error metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transformer KV anchor compression against recency and heavy-hitter pruning
- Success threshold: At least 20% lower attention-output MSE than the best pruning baseline at the same KV budget with no more than 1% perplexity degradation and a documented throughput cost.
- Stop condition: Stop if non-oracle anchor compression fails to beat the best pruning baseline on both attention-output error and perplexity at two KV budgets.

## Evidence references

- Artifact root: `<local-path>/projects/kv-anchor-compression-vs-naive-pruning-on-gb10-81aee71119a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
