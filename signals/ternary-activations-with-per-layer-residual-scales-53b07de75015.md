# Ternary Activations with Per-Layer Residual Scales

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-activations-with-per-layer-residual-scales-53b07de75015`
Run ID: `ternary-activations-with-per-layer-residual-scales-53b07de75015-20260603T203231077401+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/156664998da4

## What looked useful

Ternary activations trained without collapse, and learned residual scales moved consistently and slightly improved validation loss versus ternary without scales. The mean improvement was only 0.00347 val-loss points, while ternary remained 0.18739 val-loss points worse than dense GELU, so residual scales recovered only a small fraction of the quality gap.

## Boundaries and scale limits

This is a bounded local proxy, not GPT-2-small-class or large-corpus evidence. It does not validate inference efficiency, fused activation-memory savings, long training stability, or datacenter-scale behavior.

## Claim scope

A 4-layer character-level transformer on Tiny Shakespeare with ternary MLP hidden activations and adaptive ternary thresholds; three seeds, 800 steps each, comparing dense GELU, ternary without residual scales, and ternary with learned per-layer residual branch scales.

## Why it stopped

Bounded proxy evidence showed a consistent but too-small residual-scale benefit and a large remaining quality gap versus dense GELU; this is an early scoped result, not full validation.

## Recommended next action

Stop this run as no-paper useful signal; before scaling, test a bounded stronger compensation mechanism such as normalized ternary activations plus residual scales and require recovery of at least half the dense-vs-ternary loss gap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Normalized Ternary Activations with Residual Scales on a Small Transformer LM
- Success threshold: Mean validation loss of the normalized/scaled ternary residual-scale variant must improve over current ternary_res_scale by at least 0.09 loss points at 800-1200 steps and remain within 0.10 loss points of dense GELU.
- Stop condition: Stop if the normalized/scaled ternary variant improves by less than 0.03 loss points over current ternary_res_scale or shows unstable activation occupancy across three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-activations-with-per-layer-residual-scales-53b07de75015`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
