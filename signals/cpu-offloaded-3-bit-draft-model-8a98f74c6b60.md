# CPU-Offloaded 3-bit Draft Model

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cpu-offloaded-3-bit-draft-model-8a98f74c6b60`
Run ID: `cpu-offloaded-3-bit-draft-model-8a98f74c6b60-20260603T151825292064+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2995134c597b

## What looked useful

3-bit storage reduces theoretical weight bytes to about 9.5% of dense fp32, but measured per-token dequantization made the CPU draft path 12.6x to 36.1x slower than dense CPU layers. A hidden=1024 stress point modeled only 0.264x speedup even at 95% acceptance.

## Boundaries and scale limits

Synthetic layers only; no trained language model, no real text acceptance distribution, no optimized packed int3 CPU kernel, and no end-to-end target-model speculative decoder.

## Claim scope

On GB10, a synthetic CPU-resident 3-bit draft stack that dequantizes weights each token is not a latency-helpful speculative-decoding draft path beyond a small optimistic proxy shape.

## Why it stopped

Proxy/early falsification: compact CPU 3-bit storage alone did not produce a viable latency mechanism because per-token dequantization dominated measured draft cost.

## Recommended next action

Stop this no-paper run; if continuing, run a bounded deepen follow-up with an optimized packed int3 CPU kernel and measured end-to-end acceptance on a real small language-model pair.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed int3 CPU kernel for end-to-end speculative decoding
- Success threshold: At least 1.25x end-to-end tokens/s over target-only decoding with acceptance measured on real text and no quality regression beyond the target model distribution.
- Stop condition: Stop if the optimized packed int3 draft latency remains above 50% of target token latency or if real acceptance is below 0.70 at the tested draft length.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-3-bit-draft-model-8a98f74c6b60`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
