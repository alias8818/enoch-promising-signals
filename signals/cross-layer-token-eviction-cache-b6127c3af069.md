# Cross-Layer Token Eviction Cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cross-layer-token-eviction-cache-b6127c3af069`
Run ID: `cross-layer-token-eviction-cache-b6127c3af069-20260604T221541433420+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5938b088e934

## What looked useful

Attention-derived token salience is a strong bounded proxy signal for eviction versus recency, but cross-layer aggregation did not clearly beat a final-layer attention baseline.

## Boundaries and scale limits

Proxy-only test; no real incremental KV-cache eviction, no serving throughput measurement, no long-context corpus, no GPT-2-small-class or larger baseline, and no scoring-overhead accounting.

## Claim scope

On 12 short built-in text prefixes with distilgpt2, cross-layer attention scoring preserved final-position logits far better than recency/random eviction under attention-mask replay, but only marginally matched or improved over final-layer attention.

## Why it stopped

Bounded proxy evidence is mixed: useful mechanism versus naive eviction, insufficient novelty over final-layer attention and not a full KV-cache validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement actual incremental KV eviction and require cross-layer scoring to beat final-layer attention on longer prompts by a meaningful KL/top-token margin.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct incremental KV-cache eviction with final-layer attention control
- Success threshold: Cross-layer scoring reduces mean KL drift by at least 10% versus final-layer attention at two or more cache budgets while preserving or improving top-token agreement and adding less than 5% decode-time overhead.
- Stop condition: Stop if cross-layer scoring fails to beat final-layer attention by at least 5% mean KL on an initial 64-prompt medium run or if scoring overhead exceeds any measured cache benefit.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-token-eviction-cache-b6127c3af069`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
