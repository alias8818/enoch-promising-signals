# KV-Cache Linear Extrapolation Drafting

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `kv-cache-linear-extrapolation-drafting-6d505155067e`
Run ID: `kv-cache-linear-extrapolation-drafting-6d505155067e-20260601T084941590323+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f880ef6e3b04

## What looked useful

KV-linear extrapolated keys and values had about 2.8-2.9x the MSE of a persistence baseline against actual next-token KV tensors. KV-derived draft logits achieved 0-2.1% top-1 target accuracy versus 20.8% for the model and 17.7-21.9% for a hidden-state extrapolation control.

## Boundaries and scale limits

Early local probe only: GPT-2 and DistilGPT-2, 96 varied synthetic contexts each, context_len 96. Does not test 7B+ models, long contexts, natural corpus evaluation, fused kernels, learned KV adapters, or end-to-end speculative verification latency.

## Claim scope

For small GPT-2-family frozen causal language models on short synthetic text contexts, naive two-point linear extrapolation of raw KV-cache tensors does not provide a useful next-token drafting signal and is geometrically worse than copying the previous KV tensors.

## Why it stopped

Proxy early falsification: direct KV geometry and heuristic draft logits failed on two GPT-2-family checkpoints, but full production speculative decoding was not tested.

## Recommended next action

Stop pursuing raw KV linear extrapolation as a paper-ready drafting method; branch only if testing hidden-state extrapolation or a learned KV-to-logit adapter in a real draft/verify loop.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Hidden-State Extrapolation Drafting With Verification
- Success threshold: At least 1.15x end-to-end decoding speedup or at least 30% verifier acceptance with no quality regression on a fixed small prompt suite.
- Stop condition: Stop if hidden-state drafting acceptance is below 15% or measured latency is slower than no-draft decoding after implementation overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-linear-extrapolation-drafting-6d505155067e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
