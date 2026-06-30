# Learned Anchor Detection for KV Eviction on Small Long-Context Retrieval

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `learned-anchor-detection-for-kv-eviction-on-small-long-con-e8d275f044`
Run ID: `learned-anchor-detection-for-kv-eviction-on-small-long-con-e8d275f044-20260529T205423494645+0000`

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

- Parent run decision: Anchor-Gated KV Cache Eviction for Long Context: enoch://control-plane/projects/anchor-gated-kv-cache-eviction-for-long-context-d5c5239c8fab/runs/anchor-gated-kv-cache-eviction-for-long-context-d5c5239c8fab-20260529T171148247561+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a781bc0ef3e5

## What looked useful

The learned detector reached 0.778 precision and 0.708 recall on anchor labels and improved mean anchor retention from 0.250 to 0.848 and target-value retention from 0.828 to 0.985 versus recency, but end-task accuracy remained near chance: full 0.1325, recency 0.1250, learned 0.1175. Anchor-retention diagnostics alone are therefore insufficient evidence for KV-eviction retrieval gains.

## Boundaries and scale limits

Single synthetic task, one small transformer architecture, sequence length 164 in the final valid run, 400 evaluation examples, cache budget 48, no pretrained LLMs or natural-language long-context benchmarks.

## Claim scope

In a controlled small synthetic randomized key-value retrieval task using a two-layer causal transformer with actual incremental KV-cache eviction, learned hidden-state anchor detection retained more fact-span and target-value tokens than recency but did not improve retrieval accuracy because full-cache retrieval stayed at chance.

## Why it stopped

The direct controlled test failed the success threshold: learned-minus-recency accuracy was -0.0075 rather than at least +0.20, and the full-cache model itself was only at chance, so the hypothesis is unsupported in this setup.

## Recommended next action

Stop this run as a no-paper useful negative; any next bounded test should first establish a full-cache randomized retrieval model with at least 70% accuracy before comparing eviction policies.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prevalidated Retriever for Learned Anchor KV Eviction
- Success threshold: Full-cache accuracy >= 0.70; learned-anchor cache accuracy - recency cache accuracy >= 0.20; full-cache accuracy - learned-anchor cache accuracy <= 0.15.
- Stop condition: Stop negative if a prevalidated full-cache retriever cannot be obtained locally within the short GPU budget, or if learned-anchor eviction fails to beat recency by 20 percentage points after full-cache accuracy is established.

## Evidence references

- Artifact root: `<local-path>/projects/learned-anchor-detection-for-kv-eviction-on-small-long-con-e8d275f044`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
