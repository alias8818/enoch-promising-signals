# GPT-2-small heavy-hitter KV eviction budget and retrieval robustness sweep

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `gpt-2-small-heavy-hitter-kv-eviction-budget-and-retrieval-fee3a3acba`
Run ID: `gpt-2-small-heavy-hitter-kv-eviction-budget-and-retrieval-fee3a3acba-20260524T185202292567+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: GPT-2-small perplexity and retrieval validation for heavy-hitter KV eviction: enoch://control-plane/projects/gpt-2-small-perplexity-and-retrieval-validation-for-heavy-50f0feee0d/runs/gpt-2-small-perplexity-and-retrieval-validation-for-heavy-50f0feee0d-20260524T175331440513+0000
- Parent run decision: Public benchmark GPT-2-small perplexity and retrieval check for heavy-hitter KV eviction: enoch://control-plane/projects/public-benchmark-gpt-2-small-perplexity-and-retrieval-chec-079beb43e0/runs/public-benchmark-gpt-2-small-perplexity-and-retrieval-chec-079beb43e0-20260524T180855818474+0000

## What looked useful

Heavy-hitter retention beat recency at every tested budget. At budget 32, heavy-hitter accuracy was 0.455 versus recency 0.205, mean target log-probability delta versus full was -0.415 versus -2.099, and answer retention was 1.000 versus 0.182. At budget 64, heavy-hitter accuracy was 0.641 versus recency 0.188, with delta -0.077 versus -2.413. Random controls were also worse than heavy-hitter across budgets.

## Boundaries and scale limits

The run used masked full-sequence attention as a proxy for KV eviction, not an actual autoregressive KV-cache eviction implementation. It used synthetic single-token answers, 96 examples, one cached GPT-2-small model, and CPU-only bounded validation under 10 minutes; no real retrieval benchmark, multi-token generation, latency, or memory-serving metrics were measured.

## Claim scope

On 96 fixed-seed synthetic one-token retrieval prompts evaluated with GPT-2-small, attention-derived heavy-hitter token retention preserved answer-token probability and candidate accuracy substantially better than recency and random controls at equal retained-token budgets.

## Why it stopped

Closed as no-paper useful signal: the direct GPT-2-small synthetic sweep supports the mechanism, but the current masked-attention approximation is not sufficient for publication-grade KV-cache eviction claims.

## Recommended next action

Run a true GPT-2-small autoregressive KV-cache eviction implementation on a bounded needle/retrieval benchmark, comparing heavy-hitter, recency, random, and full-cache policies with memory and latency measurements.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: True GPT-2-small KV-cache heavy-hitter eviction on bounded retrieval generation
- Success threshold: Heavy-hitter or hybrid eviction improves retrieval exact-match by at least 20 percentage points over recency at two or more cache budgets while retaining at least 90% of full-cache target log-probability on full-cache-correct examples.
- Stop condition: Stop if true KV-cache heavy-hitter eviction fails to beat recency by at least 5 percentage points at all tested budgets or if implementation overhead eliminates any retained-cache memory/latency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-heavy-hitter-kv-eviction-budget-and-retrieval-fee3a3acba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
