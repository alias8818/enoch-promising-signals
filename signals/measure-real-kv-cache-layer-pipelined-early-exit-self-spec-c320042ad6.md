# Measure real KV-cache layer-pipelined early-exit self-speculation

Status: `useful_signal`
Project ID: `measure-real-kv-cache-layer-pipelined-early-exit-self-spec-c320042ad6`
Run ID: `measure-real-kv-cache-layer-pipelined-early-exit-self-spec-c320042ad6-20260518T102707249791+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6dcd20e5834b

## What looked useful

Best <= half-depth exit was layer 6 with 13.28% agreement with final argmax and a 1.072x optimistic pipeline-overlap upper-bound speedup, below the run threshold of >=25% agreement and >=1.15x speedup.

## Boundaries and scale limits

One pretrained 12-layer GPT-2-small model, 16 Wikitext validation contexts, 670 cached decode positions, single-token drafting metric, no implemented parallel scheduler, no trained auxiliary exits, no confidence gating, no larger-model validation.

## Claim scope

On GPT-2-small float16 inference on GB10, raw untrained intermediate exits through half depth, projected through the final layer norm and tied LM head during real KV-cache decode, do not agree with the final model often enough to support layer-pipelined early-exit self-speculation under the Tier 1 threshold.

## Why it stopped

Controlled small direct test with real KV caches found that raw half-depth exits miss both agreement and speedup thresholds; this is an early falsification, not a full validation of all trained or larger-scale variants.

## Recommended next action

Stop this raw-mechanism branch as an early direct falsification; only reopen with a trained/calibrated half-depth exit or a real pipelined scheduler that can meet the same acceptance and wall-clock thresholds.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/measure-real-kv-cache-layer-pipelined-early-exit-self-spec-c320042ad6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
