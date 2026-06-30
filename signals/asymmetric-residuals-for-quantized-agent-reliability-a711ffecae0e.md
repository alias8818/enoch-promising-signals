# Asymmetric Residuals for Quantized Agent Reliability

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `asymmetric-residuals-for-quantized-agent-reliability-a711ffecae0e`
Run ID: `asymmetric-residuals-for-quantized-agent-reliability-a711ffecae0e-20260525T104451571446+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7766e9134d7c

## What looked useful

Asymmetric residual correction lowered logit MSE but did not reliably improve action preservation. At int2 it worsened action flip rates in all distributions and all seeds versus symmetric correction; at int3/int4 gains were tiny and inconsistent except for one small rare_spikes/int3 improvement.

## Boundaries and scale limits

Does not test real LLMs, transformer internals, multi-step agents, tool-call benchmarks, activation quantization, or production serving. The result is a proxy mechanism test, not a full validation of quantized agent reliability.

## Claim scope

Bounded synthetic linear agent-action task with per-action low-bit weight quantization, 96-dimensional contexts, 6 actions, three input distributions, 20 seeds, and asymmetric residual correction selected by quantized logit sign.

## Why it stopped

Proxy early falsification: the tested asymmetric residual mechanism improves reconstruction error but not the target action-flip reliability metric, and it materially hurts reliability at int2.

## Recommended next action

Stop as no-paper proxy evidence; revisit only with a real quantized small language model/tool-call benchmark that directly measures task-level agent reliability.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/asymmetric-residuals-for-quantized-agent-reliability-a711ffecae0e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
