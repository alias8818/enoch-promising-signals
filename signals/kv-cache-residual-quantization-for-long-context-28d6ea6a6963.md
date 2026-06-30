# KV-Cache Residual Quantization for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-residual-quantization-for-long-context-28d6ea6a6963`
Run ID: `kv-cache-residual-quantization-for-long-context-28d6ea6a6963-20260603T230414920239+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/fd1189fd69cb

## What looked useful

Residual correction recovered information from int4, but rq4_2 used 6.50 bits/value and had 2.14x the mean output relative L2 of int6 at 6.25 bits/value; rq4_4 used 8.50 bits/value and had 1.28x the mean output relative L2 of int8 at 8.25 bits/value.

## Boundaries and scale limits

No trained-model KV traces, no perplexity or generation-quality evaluation, no packed-cache fused attention kernel, and no datacenter-scale serving benchmark were run.

## Claim scope

On synthetic long-context K/V tensors up to length 8192, naive residual quantization stages improve over plain int4 but do not beat uniform bit-width quantization at comparable effective storage for attention-output reconstruction.

## Why it stopped

Proxy attention-level evidence falsified the storage-matched advantage of naive residual quantization over uniform int6/int8, but it is not a full model-quality validation.

## Recommended next action

Stop this naive residual-quantization variant as no-paper evidence; the next bounded test should use real trained-model KV traces and adaptive residual allocation under an exactly fixed bit budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Storage-matched adaptive residual KV quantization on real model traces
- Success threshold: At the same effective bits/value as int6, adaptive residual quantization reduces attention-output relative L2 by at least 20% and does not worsen next-token loss by more than the uniform baseline on real model traces.
- Stop condition: Stop if adaptive residual allocation fails to beat uniform int6 on attention-output error at matched bits/value across at least two real prompt sets.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-residual-quantization-for-long-context-28d6ea6a6963`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
