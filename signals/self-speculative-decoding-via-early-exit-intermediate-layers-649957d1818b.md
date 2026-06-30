# Self-Speculative Decoding via Early-Exit Intermediate Layers

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-decoding-via-early-exit-intermediate-layers-649957d1818b`
Run ID: `self-speculative-decoding-via-early-exit-intermediate-layers-649957d1818b-20260529T165703430943+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/35d2c96c8efa

## What looked useful

Intermediate layers 2-10 had only 7.7%-39.0% top-1 agreement with the final layer and modeled speedups below 0.565x. Layer 11 reached 54.4% agreement but cost 92.0% of a full forward and still modeled at only 0.652x, so the naïve tied-head early exit is not practically viable.

## Boundaries and scale limits

Single pretrained GPT-2-small model, 12,192 next-token positions, greedy argmax acceptance proxy, truncated-forward timing on GB10. No trained auxiliary exits, no full KV-cache autoregressive serving benchmark, no larger-model validation.

## Claim scope

On GPT-2-small with WikiText-2 validation text, reusing the pretrained final layer norm and tied LM head at intermediate layers does not provide enough greedy verifier acceptance or compute savings for self-speculative decoding speedup.

## Why it stopped

Moderate proxy/direct evidence early-falsifies the untrained tied-head early-exit variant rather than providing full-scale validation of all early-exit self-speculative methods.

## Recommended next action

Stop this no-paper run; if continuing, run a bounded trained-exit follow-up requiring an actual autoregressive KV-cache speedup above 1.1x before claiming viability.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train a lightweight GPT-2-small early-exit head for self-speculative decoding
- Success threshold: At least 1.1x wall-clock tokens/sec over final-only greedy decoding with identical final accepted outputs, plus held-out mean accepted draft tokens of at least 1.5 for gamma=4 from a layer no deeper than 8.
- Stop condition: Stop if trained exits at layers 6-8 remain below 0.75 top-1 agreement with the final layer or if direct autoregressive speedup remains below 1.0x after optimized KV-cache implementation.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-intermediate-layers-649957d1818b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
