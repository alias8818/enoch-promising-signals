# Cross-layer KV sharing for GPT-2-small

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cross-layer-kv-sharing-for-gpt-2-small-3e2946fc0222`
Run ID: `cross-layer-kv-sharing-for-gpt-2-small-3e2946fc0222-20260525T052952251612+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/11a49bfa7e02

## What looked useful

Adjacent K/V tensors in pretrained GPT-2-small were nearly orthogonal on WikiText-2 (mean adjacent key cosine 0.00743, value cosine -0.00053). Replacing a single layer's K/V with the previous layer worsened loss by +0.052 to +0.594; sharing layers 1,3,5,7,9,11 from previous layers raised loss from 4.10168 to 6.78017, and sharing all layers 1-11 raised loss to 8.85693.

## Boundaries and scale limits

Inference-only probe on pretrained GPT-2-small using 64 WikiText-2 test texts at max length 128 plus a fallback smoke test. It did not retrain or fine-tune with K/V sharing, did not test learned K/V alignment adapters, non-adjacent source search, larger corpora, long-context decoding throughput, or parameter-matched training baselines.

## Claim scope

Pretrained GPT-2-small does not tolerate naive inference-time adjacent-layer K/V sharing where layer l keeps its own queries but consumes key/value tensors from layer l-1; every single-layer replacement increased WikiText-2 loss and pairwise/all-layer sharing caused large perplexity degradation.

## Why it stopped

Moderate local evidence directly tested the naive inference-time hypothesis and found large loss/perplexity degradation; this is not a full training-time architecture validation.

## Recommended next action

Stop this run as an early, direct falsification of naive pretrained K/V sharing; only pursue a new bounded deepen test if it trains or learns an explicit alignment mechanism rather than directly substituting adjacent pretrained K/V tensors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned alignment for adjacent-layer K/V sharing in GPT-2-small
- Success threshold: Adapter-aligned pairwise sharing should recover at least 80% of the loss gap between naive pairwise sharing and baseline on held-out WikiText-2 while adding less than 5% of GPT-2-small parameters and preserving a reduced K/V cache footprint.
- Stop condition: Stop if learned alignment recovers less than half of the naive-sharing loss gap or requires enough per-layer state that cache/parameter savings become negligible.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-kv-sharing-for-gpt-2-small-3e2946fc0222`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
