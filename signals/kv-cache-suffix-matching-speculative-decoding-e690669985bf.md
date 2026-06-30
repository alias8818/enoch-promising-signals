# KV-Cache Suffix-Matching Speculative Decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `kv-cache-suffix-matching-speculative-decoding-e690669985bf`
Run ID: `kv-cache-suffix-matching-speculative-decoding-e690669985bf-20260528T113503429998+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/636baa95d018

## What looked useful

Same-prefix controls recovered exact KV/logit equality, while different-prefix same-suffix cases had median suffix value cosine about 0.924 on synthetic tokens and 0.919 on natural-text prefixes, with minimum value cosine as low as 0.1567. This falsifies suffix-only exact KV reuse as a standalone mechanism under the tested conditions.

## Boundaries and scale limits

Mechanism probes only: 32 synthetic-token prefix pairs and 24 natural-text prefix pairs on Qwen3-0.6B, plus a tiny-model smoke test. No end-to-end speculative decoding speed benchmark, no approximate repair method, no serving trace, and no 7B+ validation.

## Claim scope

On a cached Qwen3-0.6B causal transformer, identical suffix token sequences at identical absolute positions do not produce reusable exact KV-cache states when the preceding prefix differs; suffix-token equality alone is therefore not a sound exact cache key for speculative decoding.

## Why it stopped

Proxy/mechanism early falsification rather than full-scale validation: KV states diverged materially for identical suffixes under different prefixes in the local Qwen3-0.6B probes.

## Recommended next action

Stop this suffix-only exact-reuse line as a paper claim; the bounded next test is a similarity-gated or context-fingerprinted variant that never reuses KV based on suffix tokens alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Similarity-Gated KV Suffix Reuse for Speculative Decoding
- Success threshold: Zero incorrect target-token acceptances in the tested prompt set, at least 5% net decode latency reduction versus standard speculative decoding, and a measured gate false-accept rate of 0 under deterministic replay.
- Stop condition: Stop if the gate accepts fewer than 1% of candidate suffix matches or if any incorrect target KV reuse survives verification.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-suffix-matching-speculative-decoding-e690669985bf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
