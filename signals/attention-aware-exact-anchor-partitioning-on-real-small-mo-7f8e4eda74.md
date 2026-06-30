# Attention-aware exact anchor partitioning on real small-model KV traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `attention-aware-exact-anchor-partitioning-on-real-small-mo-7f8e4eda74`
Run ID: `attention-aware-exact-anchor-partitioning-on-real-small-mo-7f8e4eda74-20260520T043736710025+0000`

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

- Parent run decision: AnchorKV: Exact Anchor Partitioning for Block-wise KV Compression: enoch://control-plane/projects/anchorkv-exact-anchor-partitioning-for-block-wise-kv-compression-9f35f827e683/runs/anchorkv-exact-anchor-partitioning-for-block-wise-kv-compression-9f35f827e683-20260519T223326083038+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b5f6da419786

## What looked useful

Exact attention-aware anchors retained mean attention mass of 0.691/0.813/0.948 for budgets 4/8/16, beating uniform by 0.112/0.146/0.106 absolute and recency by 0.659/0.715/0.671 absolute across 864 prompt-layer-head cases per budget.

## Boundaries and scale limits

Single small GPT-2-family model, 12 prompts, <=64 tokens, trace-level retained-attention metric only; no end-to-end KV-cache eviction, perplexity, generation-quality, latency, or multi-model validation.

## Claim scope

On real distilgpt2 attention/KV traces from 12 real prose prompts, exact attention-aware contiguous anchor partitioning retained more aggregate attention mass than recency, uniform, and random anchor baselines at budgets 4, 8, and 16.

## Why it stopped

Tier 1 direct trace test supports the mechanism but remains a retained-attention proxy, not publication-grade evidence for KV-cache compression or decoding quality.

## Recommended next action

Run a bounded direct KV-retention follow-up that applies the selected anchors during teacher-forced next-token scoring and compares NLL degradation against recency and uniform cache baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct KV-retention quality test for attention-aware anchors on small GPT traces
- Success threshold: At two or more cache budgets, attention-aware anchors reduce mean NLL degradation versus both recency and uniform baselines by at least 10% relative without increasing retained-token count.
- Stop condition: Stop if attention-aware anchors fail to beat either recency or uniform on mean NLL degradation at all tested budgets, or if implementation requires model internals beyond a bounded small-model test.

## Evidence references

- Artifact root: `<local-path>/projects/attention-aware-exact-anchor-partitioning-on-real-small-mo-7f8e4eda74`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
