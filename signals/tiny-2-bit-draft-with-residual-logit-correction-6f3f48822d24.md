# Tiny 2-Bit Draft with Residual Logit Correction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-2-bit-draft-with-residual-logit-correction-6f3f48822d24`
Run ID: `tiny-2-bit-draft-with-residual-logit-correction-6f3f48822d24-20260604T232815214164+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/bc4eb80e5e73

## What looked useful

Across three seeds, residual correction reduced KL vs raw 2-bit by mean 0.3076, improved target top-1 agreement by mean 0.0950, and improved the acceptance proxy by mean 0.1468 while estimated corrected storage stayed at 24.1% of dense draft FP32 storage.

## Boundaries and scale limits

Tiny char-level MLPs only; no transformer LM, GPT-2-small-class baseline, real int2 kernel, real speculative decoding loop, latency measurement, or large-tokenized benchmark was tested.

## Claim scope

In a bounded NumPy Tiny Shakespeare next-character MLP probe, a learned residual logit correction on frozen 2-bit draft features consistently reduced target-distribution KL and improved top-token agreement and an acceptance proxy versus the raw 2-bit draft.

## Why it stopped

Proxy-scale mechanism evidence is positive but insufficient for publication-grade or deployment claims because it used tiny char-level MLPs and dequantized NumPy evaluation rather than realistic transformer kernels and decoding.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use a tiny transformer or GPT-2-small-class draft/target pair with a real speculative decoding acceptance metric.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer Speculative Acceptance for 2-Bit Draft Residual Correction
- Success threshold: Residual correction improves true speculative acceptance by at least 50% of the raw 2-bit drop versus dense draft while corrected draft storage remains below 35% of dense draft storage and throughput is not slower than dense draft.
- Stop condition: Stop if corrected 2-bit acceptance remains within 10% relative of raw 2-bit, if residual compute makes throughput slower than dense draft, or if storage exceeds 35% of dense draft.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-2-bit-draft-with-residual-logit-correction-6f3f48822d24`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
