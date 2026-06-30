# Attention-Sink Residual KV-Cache Quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `attention-sink-residual-kv-cache-quantization-af7f78d91eaf`
Run ID: `attention-sink-residual-kv-cache-quantization-af7f78d91eaf-20260621T030942352798+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c4961ff9efce

## What looked useful

Sink preservation is a meaningful complement to residual-window KV quantization when sinks have high attention mass, but preserve-first-N is brittle for late sinks. The no-sink control showed negligible benefit from preserving four arbitrary extra tokens.

## Boundaries and scale limits

Synthetic single-layer NumPy attention only; no real LLM KV activations, RoPE, multi-layer/head interactions, perplexity, generation quality, serving kernels, or throughput measurements.

## Claim scope

In deterministic synthetic attention traces with planted initial or late sink tokens carrying about 25% mean attention mass, preserving detected sink tokens plus a recent residual KV window substantially reduced quantization-induced attention-output RMSE compared with residual-window-only preservation at 2-bit and 4-bit KV quantization.

## Why it stopped

Closed as no-paper useful-signal evidence because this was a synthetic proxy mechanism test, not direct LLM-quality or serving validation.

## Recommended next action

Run the same residual-window plus detected-sink policy on real GPT-2-small-class KV traces and measure next-token KL or perplexity against FP32 cache.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model validation of detected-sink residual KV-cache quantization
- Success threshold: Detected-sink-plus-residual reduces mean next-token KL or perplexity degradation by at least 25% versus residual-only and outperforms random-extra preservation at the same budget in sink-heavy traces.
- Stop condition: Stop if detected sink preservation fails to beat random-extra preservation by at least 10% relative error reduction or if the environment cannot run a small real-model trace within the CPU/GPU budget.

## Evidence references

- Artifact root: `<local-path>/projects/attention-sink-residual-kv-cache-quantization-af7f78d91eaf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
