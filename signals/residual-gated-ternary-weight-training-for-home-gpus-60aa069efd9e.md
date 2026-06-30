# Residual-Gated Ternary Weight Training for Home GPUs

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `residual-gated-ternary-weight-training-for-home-gpus-60aa069efd9e`
Run ID: `residual-gated-ternary-weight-training-for-home-gpus-60aa069efd9e-20260529T190913483269+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/9f4ef5372376

## What looked useful

Residual-gated ternary averaged 0.5793 eval accuracy versus 0.5767 for plain ternary and 0.5917 for dense; it ran slower than ternary (523,869 vs 664,398 samples/sec) and doubled estimated training state (18.60 vs 9.30 MiB). Removing the gate penalty did not improve the result.

## Boundaries and scale limits

This run did not test GPT-2-small-class language modeling, long-run convergence, custom fused low-bit kernels, low-bit optimizer state, sparse residual deployment, or datacenter-scale models.

## Claim scope

On a deterministic CUDA teacher-student MLP proxy with 3 seeds and 1000 steps, residual-gated ternary weights did not provide a meaningful trainability or accuracy advantage over straight-through ternary weights and imposed higher training-state and throughput costs.

## Why it stopped

Proxy early falsification: the residual-gated mechanism failed to show a meaningful advantage over plain ternary while adding training-state and throughput cost.

## Recommended next action

Stop this no-paper line unless a direct transformer experiment with fused kernels and low-bit optimizer state is explicitly funded; the current result is a proxy early falsification rather than full validation.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/residual-gated-ternary-weight-training-for-home-gpus-60aa069efd9e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
