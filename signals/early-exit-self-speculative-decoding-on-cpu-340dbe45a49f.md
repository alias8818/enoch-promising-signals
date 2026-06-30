# Early-Exit Self-Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `early-exit-self-speculative-decoding-on-cpu-340dbe45a49f`
Run ID: `early-exit-self-speculative-decoding-on-cpu-340dbe45a49f-20260525T003259113821+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ef73a7cda2a2

## What looked useful

All benchmark rows preserved exact greedy output, but every early-exit self-speculative configuration was slower than cached greedy baseline. distilgpt2 best measured speedup was 0.435x, with shallow exits accepting about 5-12% of drafts and deeper exits accepting up to 46.5% but costing too much CPU compute.

## Boundaries and scale limits

Tested real pretrained GPT-2-family models only, not 7B+ models, quantized inference engines, sampling workloads, fused kernels, persistent verifier KV-cache truncation, or trained auxiliary exit heads.

## Claim scope

On this CPU worker, off-the-shelf GPT-2-family intermediate-layer logits used as an exact self-speculative drafter did not accelerate cached greedy decoding for sshleifer/tiny-gpt2 smoke or distilgpt2 bounded benchmarks.

## Why it stopped

Direct bounded CPU benchmarks on real pretrained distilgpt2 weights falsified the speedup hypothesis for off-the-shelf intermediate logits; this is not a full-scale validation of all possible early-exit self-speculative systems.

## Recommended next action

Stop this off-the-shelf early-exit CPU path as a no-paper useful negative result; only revisit with trained or calibrated auxiliary exit heads that first demonstrate much higher acceptance at low exit depth.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train calibrated auxiliary exit heads for CPU self-speculative decoding
- Success threshold: At least 1.10x wall-clock speedup over cached greedy decoding with exact greedy output, exit layer at or before half depth, and draft acceptance at least 70% on the benchmark prompts.
- Stop condition: Stop if trained/calibrated exits remain below 50% acceptance at half depth or below 1.0x wall-clock speedup after a bounded distilgpt2-class run.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-self-speculative-decoding-on-cpu-340dbe45a49f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
