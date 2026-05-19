# Anchor-Indexed KV Compression with Exact Recall Positions

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-indexed-kv-compression-with-exact-recall-positions-ab2f6cd34ec6`
Run ID: `anchor-indexed-kv-compression-with-exact-recall-positions-ab2f6cd34ec6-20260518T060423398003+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/aad9d2ebdfff

## What looked useful

Anchor-indexed exact-position postings separated sparse exact recall from dense KV retention: 36 sparse/moderate scenarios had 1.000 anchor-indexed top-1 with 4.57x to 111.24x compression, while sliding-window and anchor-only controls averaged 0.060 and 0.009 top-1. Dense stress showed compression collapses to about 0.98x at 100% exact-recall density.

## Boundaries and scale limits

Tested only synthetic embeddings at 1k and 8k sequence lengths with oracle index construction; no trained transformer, natural-language task, real hidden-state routing, GPU cache implementation, latency measurement, or full-scale serving validation was run.

## Claim scope

In a deterministic synthetic KV retrieval benchmark with oracle exact-recall postings, anchor-indexed sparse KV retention recovered exact target positions at 100% top-1 accuracy while reducing modeled KV storage when exact-recall positions were sparse.

## Why it stopped

Synthetic/oracle-index evidence supports the mechanism but is insufficient for paper-grade validation of a real KV-compression method.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is an end-to-end small-transformer cache experiment with learned or computed anchor routing instead of oracle postings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-Transformer Anchor-Indexed KV Cache Evaluation
- Success threshold: Exact-recall accuracy within 1 percentage point of full KV and at least 4x measured KV memory reduction on sparse retrieval tasks across at least three seeds.
- Stop condition: Stop if learned/computed anchor routing loses more than 5 percentage points of exact recall versus full KV at target densities where the oracle-index synthetic model predicts at least 4x compression.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-indexed-kv-compression-with-exact-recall-positions-ab2f6cd34ec6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
