# Anchor-Preserved KV Compression with Entropy-Gated Exact Retention

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `anchor-preserved-kv-compression-with-entropy-gated-exact-retention-aa555ccfc2bb`
Run ID: `anchor-preserved-kv-compression-with-entropy-gated-exact-retention-aa555ccfc2bb-20260518T180316129001+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/add4f502ddf1

## What looked useful

In the tested synthetic fixed-budget setting, entropy-gated exact retention worsened relative MSE versus anchor+recent by 1.098x to 1.397x and versus recent-only by 1.781x to 5.149x; a retention-fraction sweep found the best entropy extra fraction was 0.00.

## Boundaries and scale limits

No real pretrained transformer KV traces, no end-to-end LLM perplexity or task accuracy, no throughput/kernel measurement, and no multi-layer/head production-cache dynamics were tested.

## Claim scope

Synthetic KV-cache attention-output replay with seq_len 1024, periodic anchors, held-out anchor/needle/local/diffuse queries, fixed budgets 64/96/128, and entropy-gated exact retention selected from calibration attention.

## Why it stopped

Synthetic/proxy evidence directly tested the fixed-budget attention-output mechanism and found entropy-selected exact retention hurt rather than helped; this is not full LLM validation.

## Recommended next action

Stop this run as a proxy early falsification; only revisit with real small-transformer KV trace replay against equal-budget summary-only and recent-only baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer KV trace replay for entropy-gated exact retention
- Success threshold: Entropy-gated exact retention reduces mean attention-output error by at least 15% versus both anchor+recent and block-summary-only baselines at the same budget, and improves retrieval/logit accuracy on held-out prompts.
- Stop condition: Stop if entropy-gated retention fails to beat the best equal-budget baseline on either attention-output error or held-out retrieval/logit accuracy across at least three budgets.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserved-kv-compression-with-entropy-gated-exact-retention-aa555ccfc2bb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
