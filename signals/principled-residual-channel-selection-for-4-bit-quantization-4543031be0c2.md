# Principled Residual Channel Selection for 4-bit Quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `principled-residual-channel-selection-for-4-bit-quantization-4543031be0c2`
Run ID: `principled-residual-channel-selection-for-4-bit-quantization-4543031be0c2-20260605T171505133277+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/0bd4b15288b5

## What looked useful

Across two corrected 32-seed medium runs, the loss-diagonal selector was best at all tested residual budgets. In the random-sensitivity setting it reduced output MSE by 68.27%, 76.41%, 89.33%, and 95.20% for 3, 5, 13, and 26 residual channels, versus best non-loss-aware heuristic reductions of 29.71%, 35.94%, 52.64%, and 63.00%. In an inverse-sensitivity setting it reduced MSE by 31.20% to 75.00% while common heuristics were near zero or random-level.

## Boundaries and scale limits

Synthetic linear proxy only; no trained transformer, nonlinear block, real calibration corpus, perplexity/task metric, GPTQ/AWQ/SpQR implementation comparison, or deployment latency/memory validation.

## Claim scope

In controlled two-layer linear NumPy proxies with per-column INT4 quantization of a hidden projection, selecting residual channels by activation-calibrated quantization error times downstream sensitivity outperforms random, weight-norm, raw quantization-error, and activation-only selectors on validation output MSE.

## Why it stopped

This run produced a useful synthetic mechanism signal, but it is proxy-only and not a full validation of 4-bit LLM quantization quality or deployability.

## Recommended next action

Run a bounded transformer-layer follow-up on GPT-2-small-class weights: apply the loss-diagonal residual selector to real MLP/attention projection layers and compare perplexity against AWQ/GPTQ/SpQR-style residual or salient-channel baselines at matched storage budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-layer validation of loss-aware residual channel selection
- Success threshold: At matched residual budget, loss-aware selection improves validation layer-output MSE by at least 20% relative to the best non-loss-aware selector and shows a measurable perplexity or next-token-loss improvement over the same selector without increasing residual storage.
- Stop condition: Stop if the loss-aware selector fails to beat the best non-loss-aware selector on both layer-output MSE and language-model loss in two independent GPT-2-small-class layers or if residual-path overhead eliminates the storage/performance rationale.

## Evidence references

- Artifact root: `<local-path>/projects/principled-residual-channel-selection-for-4-bit-quantization-4543031be0c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
