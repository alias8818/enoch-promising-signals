# Tier-Adaptive Quantization Cascade on GB10 VRAM Budget

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tier-adaptive-quantization-cascade-on-gb10-vram-budget-71d535402e5e`
Run ID: `tier-adaptive-quantization-cascade-on-gb10-vram-budget-71d535402e5e-20260614T050501837279+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/353f49aa9e91

## What looked useful

Across two medium seeds, adaptive tiering reduced MSE versus uniform q4 by 19.96%, 36.30%, 59.47%, and 84.75% at 1.10x, 1.20x, 1.35x, and 1.60x q4 byte budgets, and beat largest-first and random controls at the same estimated budgets.

## Boundaries and scale limits

Synthetic residual MLP only; estimated packed storage only; dequantized execution; no real LLM perplexity, packed CUDA kernel, KV-cache, long-context, or actual VRAM-pressure validation.

## Claim scope

On a deterministic synthetic transformer-like residual MLP run on GB10 CUDA, calibration-driven tier-adaptive 4/8/16-bit weight assignment reduces held-out output MSE versus uniform q4, largest-first, and random controls at equal estimated storage budgets.

## Why it stopped

Proxy useful signal only: the tier-selection mechanism worked in synthetic GB10 CUDA tests, but this is not direct/full validation of an LLM VRAM-budget quantization cascade.

## Recommended next action

Run a bounded real-transformer follow-up using GPT-2-small-class weights or a parameter-matched local transformer, measuring perplexity plus actual packed int4/int8 memory rather than synthetic reconstruction MSE.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transformer packed-memory validation for tier-adaptive quantization
- Success threshold: At 1.2x to 1.6x q4 actual packed-memory budgets, adaptive tiering reduces validation perplexity gap to fp16 by at least 25% versus the best non-adaptive equal-memory control without reducing throughput by more than 10%.
- Stop condition: Stop if adaptive tiering fails to beat the best equal-memory non-adaptive control on validation perplexity at two or more tested budgets, or if packed-memory measurement cannot be obtained.

## Evidence references

- Artifact root: `<local-path>/projects/tier-adaptive-quantization-cascade-on-gb10-vram-budget-71d535402e5e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
