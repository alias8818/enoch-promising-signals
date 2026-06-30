# 2-bit Draft Model with Residual Distribution Correction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `2-bit-draft-model-with-residual-distribution-correction-1b834e12c5e3`
Run ID: `2-bit-draft-model-with-residual-distribution-correction-1b834e12c5e3-20260523T152604401150+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/94b8eb508186

## What looked useful

Across three medium seeds, residual correction reduced target-to-draft KL by a mean 73.4% and improved the speculative acceptance proxy by a mean +3.42 percentage points versus the plain 2-bit draft, with NLL improving in every seed.

## Boundaries and scale limits

Synthetic data, small GRU architecture, distribution-overlap acceptance proxy only; no real-text transformer target, no end-to-end speculative decoding latency, no KV-cache or memory-bandwidth measurements, and no 7B+ validation.

## Claim scope

On a synthetic HMM sequence task with small GRU language models, a frozen per-channel 2-bit quantized draft plus a small full-precision low-rank residual logit head consistently improved held-out target-distribution match versus the plain 2-bit draft across three medium seeds.

## Why it stopped

No-paper useful signal: the local proxy supports the residual-correction mechanism, but it is not direct/full validation of 2-bit draft speculative decoding.

## Recommended next action

Run a bounded transformer-on-real-text follow-up with real speculative decoding acceptance and latency metrics before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer real-text test of 2-bit residual-corrected draft acceptance
- Success threshold: At least +2 percentage points absolute accepted-token rate or +5% accepted tokens per verification step over the plain 2-bit draft, with no more than 10% draft-side latency overhead and no NLL regression versus the corrected draft objective.
- Stop condition: Stop if residual correction fails to improve accepted-token rate in two real-text transformer seeds or if correction-head overhead erases measured decoding throughput gains.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-draft-model-with-residual-distribution-correction-1b834e12c5e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
