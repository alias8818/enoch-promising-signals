# Learnable Anchor Tokens with Compressed KV Buffer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `learnable-anchor-tokens-with-compressed-kv-buffer-7b70966d0206`
Run ID: `learnable-anchor-tokens-with-compressed-kv-buffer-7b70966d0206-20260520T070003438189+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/cd36c05e0d83

## What looked useful

Learned anchors appear to learn a retention policy for predictable salience, especially recency. They do not solve arbitrary pre-query KV compression: uniform recall stayed close to fixed chunks and far below full KV.

## Boundaries and scale limits

CPU-only synthetic probe; sequence length 64; 8 and 16 compressed anchor slots; fixed random key embeddings; no transformer language-model training, no GPT-2-small-class baseline, no 7B-scale inference, and no hardware KV-cache latency or memory benchmark.

## Claim scope

In a synthetic associative-recall probe with 64-token KV buffers compressed before the query is known, learned anchor slots materially improve recall over fixed chunk compression when queries target the most recent 8 positions, but provide almost no advantage for uniformly distributed target positions.

## Why it stopped

The bounded synthetic evidence is mixed: useful mechanism signal for recency-biased recall, but insufficient and too proxy-like for a paper or broad architecture claim.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next test is a small transformer language-model comparison of standard KV, fixed compressed KV, and learned anchor compressed KV under matched cache budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Transformer Validation of Learned Anchor KV Compression
- Success threshold: Learned anchor compression beats fixed chunk compression by at least 10% relative error reduction on retrieval or a statistically consistent perplexity improvement at the same cache budget, with measured cache memory reduction versus full KV.
- Stop condition: Stop if learned anchors fail to beat fixed chunk compression on both retrieval and perplexity under matched cache budgets, or if implementation overhead eliminates the measured cache benefit.

## Evidence references

- Artifact root: `<local-path>/projects/learnable-anchor-tokens-with-compressed-kv-buffer-7b70966d0206`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
