# Anchor-Exact KV Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-exact-kv-compression-c92b808ecdf7`
Run ID: `anchor-exact-kv-compression-c92b808ecdf7-20260523T224914556399+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/032903e20ec6

## What looked useful

Keeping true high-impact KV entries exact while pooling the rest can reduce synthetic attention-output error by about 4.9x on an anchored distribution and about 2.0x when high-value outliers should be isolated from pools. Without pooled-count bias, exact anchors distort softmax mass and are worse than pooled-only.

## Boundaries and scale limits

No real transformer, real prompt distribution, multi-layer/head KV cache, generation-quality metric, production attention kernel, or latency/memory-bandwidth benchmark was tested. The positive mechanism depends on log(pool_size) count correction; the naive no-count-bias form failed in smoke tests.

## Claim scope

Synthetic attention-only probe at T=4096, d=128, 12.5% compressed KV slots, 8 seeds per scenario: count-aware anchor-exact compression reduces attention-output relative L2 error versus pooled-only when high-impact anchor tokens exist, and is neutral on IID KV.

## Why it stopped

Evidence is synthetic/proxy-only and not sufficient for a paper; it supports a mechanism and falsifies the naive no-count-bias variant, but not an end-to-end KV compression claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should test count-aware anchor-exact compression on recorded KV caches from a small real transformer with logit drift or perplexity and decode latency at matched memory budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transformer KV cache test for count-aware anchor-exact compression
- Success threshold: At 4x to 8x KV slot reduction, count-aware anchor-exact must reduce mean logit drift or perplexity degradation by at least 25% versus pooled-only and random/uniform controls while keeping decode latency within 10% of the compressed baseline.
- Stop condition: Stop if anchor-exact does not beat pooled-only by at least 10% on logit drift/perplexity in two prompt sets, or if count-bias correction causes decode latency overhead above 25% at matched memory budget.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-exact-kv-compression-c92b808ecdf7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
