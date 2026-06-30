# Spectral Activation Residual: int4 acts + low-rank FP8 spectral component

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `spectral-activation-residual-int4-acts-low-rank-fp8-spectral-component-b3d4a6b55972`
Run ID: `spectral-activation-residual-int4-acts-low-rank-fp8-spectral-component-b3d4a6b55972-20260614T042742002604+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8afe4dd041f4

## What looked useful

Medium sweep over 54 CUDA cases found mean spectral residual improvement of 1.091x over int4 MSE versus 1.014x for a random residual control; rank-32 reached 1.154x at an optimistic 4.375 bits/element. Spectral residual beat int8 MSE in 0/54 cases, and random-linear relative MSE remained 0.249 versus 0.00303 for int8.

## Boundaries and scale limits

No real transformer activations, perplexity, trained model, fused kernel, metadata overhead accounting, or large-scale serving path was tested. The bits-per-element estimate is optimistic and excludes scales/metadata.

## Claim scope

On synthetic activation-like matrices up to 2048 x 2048, an SVD-selected low-rank FP8 residual added to per-feature int4 activations consistently improves reconstruction and random-linear projection error over plain int4 and a random low-rank residual control, but the effect is modest.

## Why it stopped

Proxy/early bounded test found a real but modest mechanism that is not strong enough or direct enough for paper-positive validation.

## Recommended next action

Do not write a paper from this proxy result; run a bounded real-activation follow-up on GPT-2-small-class saved activations with perplexity/logit-error proxies and exact storage overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real transformer activation test for int4 plus FP8 spectral residual
- Success threshold: At least 20% reduction in layer-output or logit relative MSE versus int4, clearly above random low-rank control, while staying below 4.5 effective bits per activation element; stop if improvement is below 10% or not above random control.
- Stop condition: Stop after a GPT-2-small bounded run if spectral residual fails to beat random residual by at least 2x in relative improvement or if exact overhead exceeds 4.5 bits per element for the tested ranks.

## Evidence references

- Artifact root: `<local-path>/projects/spectral-activation-residual-int4-acts-low-rank-fp8-spectral-component-b3d4a6b55972`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
