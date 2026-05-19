# True fused DynResAct route+scatter kernel for GPT-2-small prefill

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `63`
Project ID: `true-fused-dynresact-route-scatter-kernel-for-gpt-2-small-b490e7dadf`
Run ID: `true-fused-dynresact-route-scatter-kernel-for-gpt-2-small-b490e7dadf-20260517T155633316835+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `63`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: True fused DynResAct route+scatter kernel for GPT-2-small prefill: internal_generated:true-fused-dynresact-route-scatter-kernel-for-gpt-2-small-b490e7dadf

## What looked useful

Fusion removes PyTorch sort/scatter overhead at tiny token counts, but the scalar fused route computation gives up optimized tensor-core matmul and loses the advantage at realistic larger prefill sizes or higher route counts.

## Boundaries and scale limits

Single GB10, synthetic activations and router weights, forward microbenchmark only, no full GPT-2 model integration, no backward pass, no real activation traces, and no tensor-core fused route implementation.

## Claim scope

On GB10 for GPT-2-small hidden=768 FP16 synthetic prefill tensors, a naive one-block-per-token fused learned-linear-router plus row-scatter CUDA kernel only beats PyTorch route+sort/scatter for tiny 1024-token prefills and is break-even or slower at medium and large prefill sizes, especially with 4 or 8 routes.

## Why it stopped

Direct bounded validation on GPT-2-small hidden size falsified the broad speedup threshold: speedup vs PyTorch route+sort/scatter fell below 1.0 for 4-route and 8-route medium/large prefills and was only robustly positive at 1024 tokens.

## Recommended next action

Stop this learned-linear true-fused scalar-router design; only revisit route+scatter fusion if the route is cheap/precomputed or a tensor-core routing primitive can be fused without losing GEMM efficiency.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/true-fused-dynresact-route-scatter-kernel-for-gpt-2-small-b490e7dadf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
