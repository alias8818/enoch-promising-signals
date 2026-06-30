# Structural Anchor Mixed-Precision KV Cache

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `structural-anchor-mixed-precision-kv-cache-b8c195870477`
Run ID: `structural-anchor-mixed-precision-kv-cache-b8c195870477-20260602T185730991724+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/bbe37b6af998

## What looked useful

Structural high-precision KV rows helped only when the synthetic anchors actually carried attention mass: no-anchor control showed no structural-over-random benefit, default anchors improved rel-L2 by 13.6% over random mixed precision in 47/48 seeds, and strong anchors improved rel-L2 by 86.6% over random in 48/48 seeds. All-int8 remained more accurate at roughly double the memory.

## Boundaries and scale limits

No trained transformer, real KV activations, perplexity, logit drift, generation quality, decode latency, or GPU kernel throughput was tested. Anchor positions were known by construction. Results should not be treated as LLM-serving validation.

## Claim scope

Synthetic NumPy attention reconstruction proxy with known structural anchor rows every 64 tokens, seq_len 4096, dim 128, 128 queries, and 48 seeds for default and strong anchor regimes. Mixed structural fp16-anchor/int4-rest KV reduced relative L2 attention-output error versus all-int4 and random mixed-row controls at about 26.17% of fp16 KV footprint when anchors carried persistent attention mass.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic proxy, not real model or serving validation.

## Recommended next action

Run a bounded direct follow-up on a small pretrained transformer by compressing recorded per-layer KV activations with structural, random, key-norm, int4, and int8 policies, then measure logit drift/perplexity and decode cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained Transformer KV-Activation Test for Structural Anchor Mixed Precision
- Success threshold: At the same KV byte budget, structural-anchor mixed precision reduces mean logit drift or perplexity degradation by at least 10% versus random mixed precision across most tested layers/heads, without losing to a simple adaptive selector.
- Stop condition: Stop if structural anchors fail to beat random mixed precision by 5% on logit drift/perplexity in two model/dataset settings, or if adaptive selectors dominate structural anchors at the same memory budget.

## Evidence references

- Artifact root: `<local-path>/projects/structural-anchor-mixed-precision-kv-cache-b8c195870477`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
