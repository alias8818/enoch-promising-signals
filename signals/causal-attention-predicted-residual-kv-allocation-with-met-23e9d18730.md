# Causal attention-predicted residual KV allocation with metadata-inclusive bit budget

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `causal-attention-predicted-residual-kv-allocation-with-met-23e9d18730`
Run ID: `causal-attention-predicted-residual-kv-allocation-with-met-23e9d18730-20260522T205711963114+0000`

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

- Parent run decision: Attention-aware residual codebooks with per-channel scaling for sub-2-bit KV cache: enoch://control-plane/projects/attention-aware-residual-codebooks-with-per-channel-scalin-0c15c7b71f/runs/attention-aware-residual-codebooks-with-per-channel-scalin-0c15c7b71f-20260522T204150870196+0000
- Parent run decision: Sub-2-bit KV cache via residual codebook channels: enoch://control-plane/projects/sub-2-bit-kv-cache-via-residual-codebook-channels-f0e454110abe/runs/sub-2-bit-kv-cache-via-residual-codebook-channels-f0e454110abe-20260522T190047637252+0000

## What looked useful

Attention prediction alone is insufficient; residual/KV magnitude is a strong driver of quantization sensitivity. Metadata overhead changes the apparent budget and must be included. The strongest cheap norm control beat causal attention x residual allocation at 2.75, 3.25, and 4.25 bits/scalar.

## Boundaries and scale limits

Synthetic traces only; no real LM K/V cache, perplexity, generation, or serving-latency validation. Uniform fixed-width baseline cannot spend fractional leftover budget, so random and norm variable-allocation controls are the stricter budget-matched comparisons.

## Claim scope

On fixed-seed synthetic transformer-like causal attention traces, metadata-inclusive causal attention x residual KV allocation improves future attention-output reconstruction error versus uniform, random, recency, and attention-only controls, but does not beat a simple K/V norm allocation baseline.

## Why it stopped

Medium synthetic validation produced a useful but mixed result: the mechanism beats weak baselines but fails against the strongest simple control, so it is no-paper evidence rather than paper-positive support.

## Recommended next action

Do not write a paper from this run; next bounded test should use real GPT-2-small-class KV traces and require causal attention x residual allocation to beat a tuned norm baseline under exact metadata-inclusive budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real GPT-2 KV-trace test of causal attention x residual allocation against norm allocation
- Success threshold: Causal attention x residual allocation must beat tuned norm-only allocation by at least 10% relative future attention-output MSE at two of three budgets without exceeding storage budget, and must not worsen perplexity versus norm at the matched budget.
- Stop condition: Stop negative if tuned norm-only matches or beats causal attention x residual allocation on real traces at two or more budgets, or if metadata-inclusive accounting removes the apparent gain.

## Evidence references

- Artifact root: `<local-path>/projects/causal-attention-predicted-residual-kv-allocation-with-met-23e9d18730`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
