# Causal Non-Oracle Anchor Selection for Real-KV Landmark Pooling

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `causal-non-oracle-anchor-selection-for-real-kv-landmark-po-09956cac81`
Run ID: `causal-non-oracle-anchor-selection-for-real-kv-landmark-po-09956cac81-20260517T024003318188+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Causal Non-Oracle Anchor Selection for Real-KV Landmark Pooling: internal_generated:causal-non-oracle-anchor-selection-for-real-kv-landmark-po-09956cac81

## What looked useful

Fixed-seed Tier 2 runs over 432 cases per method showed causal_received mean MSE of 0.05340 at block size 16 versus centroid 0.04261 and mean_pool 0.04525; block-size ablations at 8 and 32 also favored centroid/mean-pool. The failure is concentrated in late-layer tail errors, while an oracle diagnostic shows remaining selectable headroom.

## Boundaries and scale limits

No end-to-end perplexity, retrieval, generation-quality, multi-model, or sequence lengths above 512 were tested. Evidence is direct mechanism evidence for KV attention approximation, not publication-grade deployment evidence.

## Claim scope

For pretrained distilgpt2 real Q/K/V tensors at sequence length 512, keeping 64 recent tokens and compressing older context into one landmark per 8, 16, or 32-token block, a causal received-attention anchor selector does not outperform simple centroid or mean-pool baselines on attention-context reconstruction MSE.

## Why it stopped

Tier 2 direct real-KV evidence with fixed seeds, baselines, controls, and block-size ablations does not support the proposed causal non-oracle selector as superior to simple real baselines.

## Recommended next action

Stop this branch as no-paper evidence; the only worthwhile continuation is a bounded deepen test adding a tail-risk stabilizer and measuring both end-to-end LM loss and attention-context error.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tail-Stabilized Causal Anchor Selection for Real-KV Landmark Pooling
- Success threshold: The stabilized selector must beat centroid and mean_pool on mean attention-context MSE by at least 5% and reduce late-layer p95 MSE by at least 10% at two of three block sizes, with no end-to-end LM loss regression versus centroid beyond 1%.
- Stop condition: Stop if the stabilized selector fails to beat centroid or mean_pool on mean MSE at block size 16, or if end-to-end LM loss regresses by more than 1% versus centroid.

## Evidence references

- Artifact root: `<local-path>/projects/causal-non-oracle-anchor-selection-for-real-kv-landmark-po-09956cac81`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
