# Ternary Weights + Per-Channel FP8 Residual

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-weights-per-channel-fp8-residual-a77e41e92365`
Run ID: `ternary-weights-per-channel-fp8-residual-a77e41e92365-20260629T113712047316+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8d925090100d

## What looked useful

Across 180 cases, ternary plus FP8 residual reached mean weight NMSE 0.0001449 and linear-output NMSE 0.0001447 versus 0.0005892 and 0.0005884 for per-channel FP8, about 0.246x FP8 error. It used 10.17 effective bits/weight versus 8.08 for FP8, about 1.258x the bit cost.

## Boundaries and scale limits

Tested only synthetic weights, random linear activations, software FP8 approximation, and simple dense bit accounting. Did not test trained transformer perplexity, training convergence, hardware kernels, packing efficiency, activation quantization, or end-to-end latency.

## Claim scope

In a bounded CPU NumPy proxy over synthetic weight matrices, ternary per-channel weights plus a dense per-channel FP8 E4M3 residual reduces reconstruction and random linear-output NMSE versus direct per-channel FP8, but only by spending more bits per weight.

## Why it stopped

The result is a proxy useful signal, not full validation: it supports the residual-dynamic-range mechanism but does not establish practical compression, trained-model quality, or hardware speed.

## Recommended next action

Run one bounded direct follow-up on a trained small transformer or GPT-2-small-class model, comparing perplexity and packed bandwidth against direct FP8 and INT8/INT10-like baselines; otherwise stop at this no-paper useful signal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct PTQ test of ternary plus FP8 residual on trained transformer layers
- Success threshold: At matched or explicitly justified bandwidth, ternary plus FP8 residual must reduce perplexity degradation or layer-output error by at least 20% versus direct FP8 without exceeding the selected packed storage budget.
- Stop condition: Stop if trained-model perplexity is not better than direct FP8 at comparable packed cost, or if packing/accounting shows the dense residual representation cannot be bandwidth-competitive.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-weights-per-channel-fp8-residual-a77e41e92365`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
