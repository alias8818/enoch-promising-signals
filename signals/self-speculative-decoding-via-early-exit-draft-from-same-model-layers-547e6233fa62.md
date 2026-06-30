# Self-Speculative Decoding via Early-Exit Draft from Same Model Layers

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-decoding-via-early-exit-draft-from-same-model-layers-547e6233fa62`
Run ID: `self-speculative-decoding-via-early-exit-draft-from-same-model-layers-547e6233fa62-20260525T042901080307+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6964266ffb6c

## What looked useful

Mean one-token acceptance overlap remained low: distilgpt2 reached 0.349 at layer 4/6 and gpt2 reached 0.382 at layer 8/12, with top-1 agreement only 0.231 and 0.254 respectively. These values imply most early-exit draft tokens would be rejected, making the no-training tied-head mechanism a poor candidate for self-speculative decoding.

## Boundaries and scale limits

Only 20 fixed prompts and 130 next-token positions were evaluated; no trained early-exit heads, no larger models, no long-context workloads, and no production speculative decoding kernel were tested.

## Claim scope

On pretrained GPT-2-family models tested locally (distilgpt2 and gpt2), using intermediate hidden states with the existing final layer norm and tied LM head as an untrained same-model draft distribution gives low speculative acceptance and is not practically viable for speedup.

## Why it stopped

Early direct probes on distilgpt2 and gpt2 found acceptance overlap too low for speculative speedup; this is a proxy/early falsification of the simple no-training mechanism, not a full validation of all trained early-exit speculative decoding variants.

## Recommended next action

Stop this no-training tied-head variant; a bounded follow-up should train or self-distill lightweight early-exit heads on a frozen GPT-2-small backbone and require mean acceptance above 0.75 plus measured wall-clock decoding speedup before escalating.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train calibrated early-exit heads for same-model speculative decoding
- Success threshold: At least one exit layer must reach mean acceptance overlap >= 0.75, P10 overlap >= 0.50, and >= 1.15x measured wall-clock tokens/sec on held-out prompts.
- Stop condition: Stop if trained exits remain below 0.60 mean acceptance overlap or fail to beat normal cached decoding wall-clock throughput.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-draft-from-same-model-layers-547e6233fa62`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
