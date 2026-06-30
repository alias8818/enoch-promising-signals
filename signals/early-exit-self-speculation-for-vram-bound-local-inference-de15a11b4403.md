# Early-Exit Self-Speculation for VRAM-Bound Local Inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `early-exit-self-speculation-for-vram-bound-local-inference-de15a11b4403`
Run ID: `early-exit-self-speculation-for-vram-bound-local-inference-de15a11b4403-20260530T080521074349+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6747810389ed

## What looked useful

Intermediate exits are either cheap but rarely agree with the final token, or late enough to agree moderately but too expensive. Best optimistic modeled speedups were 0.834x for Qwen2.5-0.5B and 0.852x for SmolLM2-135M, both below baseline.

## Boundaries and scale limits

This does not evaluate trained auxiliary exits, EAGLE-style speculators, fused serving kernels, 7B+ models, long-context workloads, or production prompt distributions.

## Claim scope

Raw untrained early-exit/logit-lens self-speculation on cached local Qwen2.5-0.5B and SmolLM2-135M models, measured on short prompts on GB10, does not provide enough exact next-token agreement to beat baseline decode under an optimistic memory-bound speed model.

## Why it stopped

Proxy/early falsification: direct agreement measurements plus an optimistic speed model were insufficient for a positive claim, and no full serving validation was attempted.

## Recommended next action

Stop this raw untrained-exit variant; the bounded next useful test is to train lightweight auxiliary exit heads and require measured speculative decode speedup above baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train Calibrated Auxiliary Exits for Local Self-Speculation
- Success threshold: At least 1.15x measured tokens/s versus greedy baseline on held-out prompts with exact greedy output equivalence and no more than 10% additional peak memory.
- Stop condition: Stop if trained exits below 50% depth cannot reach 70% top-1 agreement on held-out prompts or if measured speculative decoding remains below 1.0x baseline.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-self-speculation-for-vram-bound-local-inference-de15a11b4403`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
