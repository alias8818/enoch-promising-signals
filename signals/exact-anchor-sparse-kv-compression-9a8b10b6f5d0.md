# Exact-Anchor Sparse KV Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-sparse-kv-compression-9a8b10b6f5d0`
Run ID: `exact-anchor-sparse-kv-compression-9a8b10b6f5d0-20260605T081643874941+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a52a6c210eec

## What looked useful

At budget 64/2048, exact-anchor reduced mean relative attention-output error on anchor-structured traces from 0.5744 for recent-only to 0.0580 and retained 0.9593 dense attention mass, but on adversarial old-token traces it was consistently worse than recent-only and random-old controls.

## Boundaries and scale limits

Sequence length 2048, dim/value_dim 64, 3 trials per condition, synthetic Q/K/V only, oracle anchor identities, no pretrained language model, no perplexity/task metric, and no production sparse-attention kernel benchmark.

## Claim scope

Synthetic single-head causal attention traces show exact-anchor plus recent KV retention can approximate dense attention well only when important long-range tokens are known stable anchors; it is not supported as a general sparse KV compression policy.

## Why it stopped

Synthetic proxy evidence supports the mechanism only under oracle stable anchors and early-falsifies the broader general sparse KV compression claim; this is not a full validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should evaluate learned or calibration-derived anchors inside a small pretrained causal LM with perplexity and per-layer dense-attention error.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LM Calibration Anchors for Sparse KV Compression
- Success threshold: At 6.25% to 12.5% retained KV budget, calibration-derived exact anchors improve perplexity delta and mean per-layer attention-output error by at least 25% versus recent-only on anchor-heavy prompts without regressing neutral/random prompts by more than 5%.
- Stop condition: Stop if calibration-derived anchors fail to beat recent-only on both perplexity delta and attention-output error at two KV budgets, or if benefits appear only with oracle labels.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-sparse-kv-compression-9a8b10b6f5d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
