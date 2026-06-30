# Per-Layer Learned INT4/FP8 Router with Reconstruction-Constrained Gate

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `per-layer-learned-int4-fp8-router-with-reconstruction-constrained-gate-a444c1698978`
Run ID: `per-layer-learned-int4-fp8-router-with-reconstruction-constrained-gate-a444c1698978-20260629T004723742914+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/640fda8882d3

## What looked useful

Best GPT-2 mixed route used 30/48 FP8 layers at 6.806 bits/param and cut logit MSE to 12.34 from all-INT4 116.69; best DistilGPT-2 mixed route used 13/24 FP8 layers at 6.444 bits/param and cut logit MSE to 4.90 from all-INT4 17.01. Both remained worse than all-FP8.

## Boundaries and scale limits

Small local proxy only: tiny text sets, GPT-2-family models, dequantized fp32 evaluation of reconstructed weights, no real packed INT4/FP8 kernels, no large-corpus perplexity, no larger modern model validation.

## Claim scope

On cached GPT-2 and DistilGPT-2 with short calibration/evaluation text, a reconstruction-constrained learned per-layer INT4/FP8 gate found mixed routes that substantially reduced logit MSE versus all-INT4 at less than 8 bits/parameter.

## Why it stopped

Current result is a useful proxy/mechanism signal, not full validation: evaluation is small and dequantized, and all-FP8 remains much closer to the original model.

## Recommended next action

Run a bounded deepen follow-up on a larger held-out corpus with route persistence checks and heuristic baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus-scale route persistence and heuristic baseline check for GPT-2 INT4/FP8 gating
- Success threshold: At <=7.0 bits/parameter, learned gate achieves >=50% reduction in all-INT4 logit MSE and <=0.05 perplexity/loss degradation versus original while beating all same-budget heuristic baselines on median logit MSE.
- Stop condition: Stop if the learned route fails to beat the best same-budget heuristic baseline or if route overlap across calibration subsets is below 50%.

## Evidence references

- Artifact root: `<local-path>/projects/per-layer-learned-int4-fp8-router-with-reconstruction-constrained-gate-a444c1698978`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
