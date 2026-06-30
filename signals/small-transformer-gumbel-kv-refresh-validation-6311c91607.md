# Small-Transformer Gumbel KV Refresh Validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-transformer-gumbel-kv-refresh-validation-6311c91607`
Run ID: `small-transformer-gumbel-kv-refresh-validation-6311c91607-20260629T235342409230+0000`

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

- Parent run decision: Sparse-Local KV Cache with Gumbel-Top-K Refresh: enoch://control-plane/projects/sparse-local-kv-cache-with-gumbel-top-k-refresh-b75a1eddef49/runs/sparse-local-kv-cache-with-gumbel-top-k-refresh-b75a1eddef49-20260629T230542449766+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/73e1919ed312

## What looked useful

Across seeds 0-2, final eval accuracy was 93.47% +/- 1.89% for Gumbel refresh, 83.06% +/- 0.19% for random refresh over salient pairs, 25.44% for random all-token refresh, 25.53% for FIFO all-token refresh, 0.98% for no refresh, 99.18% for oracle salient FIFO, and 99.14% for full-context transformer. This supports the bounded mechanism that learned hard refresh can improve compressed KV retention on the proxy.

## Boundaries and scale limits

This is not a language-model KV-cache validation, not GPT-2-small-class evidence, and not a long-context serving benchmark. It uses synthetic salience labels, a tiny memory model, 600-step training runs, and three seeds.

## Claim scope

On a synthetic 16-pair associative-recall proxy with 4 KV memory slots, a learned hard Gumbel refresh policy trained for 600 steps outperformed non-learned refresh controls at the same memory budget and approached oracle/full-context ceilings.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only despite supporting the local mechanism.

## Recommended next action

Do not write a paper from this proxy alone; run a bounded deepen follow-up in a tiny causal language model with real KV cache refresh during streaming evaluation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Causal-LM Gumbel KV Refresh Benchmark
- Success threshold: Gumbel refresh beats the strongest non-oracle fixed/random cache policy by at least 5 percentage points exact recall or at least 5% relative perplexity on the bounded benchmark, without more than 15% extra wall-clock cost.
- Stop condition: Stop if Gumbel refresh is not better than the strongest non-oracle cache policy in at least two of three seeds, or if the implementation requires scale beyond a single local GPU.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-gumbel-kv-refresh-validation-6311c91607`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
