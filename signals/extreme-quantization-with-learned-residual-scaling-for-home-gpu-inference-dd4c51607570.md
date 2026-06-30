# Extreme Quantization with Learned Residual Scaling for Home GPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-quantization-with-learned-residual-scaling-for-home-gpu-inference-dd4c51607570`
Run ID: `extreme-quantization-with-learned-residual-scaling-for-home-gpu-inference-dd4c51607570-20260608T073542353164+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7841a987ac2c

## What looked useful

Learned residual scaling appears useful as an outlier-compensation mechanism at a nominal 3-bit budget, but the benefit is distribution-dependent and does not establish a practical home-GPU inference win.

## Boundaries and scale limits

No real transformer weights, no perplexity/task evaluation, no packed low-bit CUDA kernel, no end-to-end token generation benchmark, and no long-run serving test were performed.

## Claim scope

On synthetic CUDA linear-layer probes up to 8192x8192 on GB10, int2 plus a 1-bit residual sign and learned per-output-channel scalar improves substantially over raw int2 and modestly beats learned-scale int3 only on average due to outlier-heavy cases; it is worse than int3 on Gaussian and low-rank cases and much worse than int4.

## Why it stopped

Moderate synthetic evidence is mixed: LRS helps outlier-heavy weights and beats raw int2, but is not robust across tested distributions, remains far behind int4, and lacks a packed inference-speed demonstration.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should apply the same LRS scheme to real pretrained transformer linear layers and compare perplexity plus a packed-kernel feasibility estimate against int3/int4 baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate LRS on real transformer linear layers with perplexity and packed-kernel feasibility
- Success threshold: On at least one small pretrained transformer, LRS must reduce perplexity or held-out loss versus same-nominal-bit int3 by at least 5% relative without exceeding int4 memory by more than 10%, and must have a credible packed-kernel path with no worse than 10% latency regression versus int3.
- Stop condition: Stop if LRS is not better than int3 on real transformer held-out loss, or if residual sign reconstruction makes the packed-kernel path slower than int3 by more than 10% without a compensating quality gain.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-quantization-with-learned-residual-scaling-for-home-gpu-inference-dd4c51607570`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
