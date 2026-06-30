# 4-bit Quantization with Error-Bounded Calibration for Small Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-quantization-with-error-bounded-calibration-for-small-models-adf37d5b9e42`
Run ID: `4-bit-quantization-with-error-bounded-calibration-for-small-models-adf37d5b9e42-20260621T092522207038+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bd2d277891e5

## What looked useful

Both calibrated methods beat minmax on held-out MSE, p95, and p99 in 6/6 aggregate conditions. Error-bounded calibration had macro relative-to-minmax MSE 0.796 and p99 0.881, but MSE-grid was better with MSE 0.770 and p99 0.865. Error-bounded calibration beat MSE-grid in 0/6 conditions for MSE, p95, and p99, and only 2/6 for max error.

## Boundaries and scale limits

CPU-only NumPy proxy: 8 seeds, 192x256 synthetic weight matrices, 128 calibration samples, 512 held-out samples, Gaussian/Laplace/Student-t activations with in-distribution and shifted tests. No real pretrained model weights, no transformer perplexity, no packed int4 inference kernel.

## Claim scope

On synthetic small-model-like linear layers with per-output-row symmetric int4 weight quantization, calibration-set scale search improves held-out output-error metrics versus raw minmax quantization, but the tested p99-plus-max error-bounded objective does not outperform a simpler MSE-calibrated scale grid.

## Why it stopped

Proxy evidence supports calibration over minmax but early-falsifies the added value of the tested error-bounded guard versus a simpler calibrated control; this is not a full validation.

## Recommended next action

Stop this worker run as no-paper useful signal; the next concrete test is a bounded real-small-model layer/perplexity evaluation using identical calibration tokens for minmax, MSE-grid, and the error-bounded objective.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-small-model int4 calibration comparison
- Success threshold: Error-bounded calibration must beat MSE-grid by at least 3% on held-out p99 layer error or perplexity/loss degradation while not worsening max error by more than 1% in a majority of tested layers.
- Stop condition: Stop if error-bounded calibration fails to beat MSE-grid on p99 or loss in the first two representative transformer blocks, or if real-model setup exceeds the local CPU-only worker budget.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-quantization-with-error-bounded-calibration-for-small-models-adf37d5b9e42`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
