# Residual Codebook KV-Cache for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-codebook-kv-cache-for-long-context-0d26ea9f929e`
Run ID: `residual-codebook-kv-cache-for-long-context-0d26ea9f929e-20260523T225943196964+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/71075af61b6a

## What looked useful

RVQ_3x256 reached 4.74x compression with attention-output relative L2 0.073 on smooth_lowrank versus scalar_int4 0.082, and 0.015 on outlier_mixed versus scalar_int4 0.267 at 1024 tokens. At 4096 tokens it reached 14.22x compression and beat scalar_int4 on outlier_mixed attention-output error, 0.218 versus 0.302, but failed on iid_gaussian with attention-output relative L2 near 0.99.

## Boundaries and scale limits

No real model KV traces, no generation or perplexity evaluation, no GPU serving kernel, no multi-layer transformer cache, and no GPT-2-small-class baseline. The largest proxy used 4096 tokens, 4 heads, dim 64, and synthetic distributions.

## Claim scope

Whole-vector residual codebook KV-cache compression was tested on synthetic 4-head KV tensors at 1024 and 4096 cached tokens. It showed useful attention-output error behavior on structured smooth and outlier-heavy proxy caches, but failed on iid high-entropy KV and is not validated on real transformer activations.

## Why it stopped

Proxy evidence is mixed: it supports a niche mechanism on structured or outlier-heavy cache tensors but early-falsifies a broad general RVQ KV-cache claim, especially on unstructured high-entropy KV. This is not a full validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use real GPT-2-small-class KV activations with grouped/product RVQ and scalar baselines at matched byte budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Activation Grouped RVQ KV-Cache Probe
- Success threshold: At matched byte budget near or above int4 compression, grouped/product RVQ reduces attention-output relative L2 by at least 25% versus scalar int4 on real activations without increasing next-token loss by more than 5% relative.
- Stop condition: Stop if real-activation RVQ fails to beat scalar int4 attention-output error on both structured and high-entropy prompt sets, or if loss degradation exceeds 5% at matched byte budgets.

## Evidence references

- Artifact root: `<local-path>/projects/residual-codebook-kv-cache-for-long-context-0d26ea9f929e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
