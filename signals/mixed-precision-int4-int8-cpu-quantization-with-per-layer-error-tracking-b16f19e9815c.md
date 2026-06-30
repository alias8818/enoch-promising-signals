# Mixed-Precision INT4-INT8 CPU Quantization with Per-Layer Error Tracking

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `mixed-precision-int4-int8-cpu-quantization-with-per-layer-error-tracking-b16f19e9815c`
Run ID: `mixed-precision-int4-int8-cpu-quantization-with-per-layer-error-tracking-b16f19e9815c-20260629T055002361685+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/084f73bed7c6

## What looked useful

Per-layer error tracking was a reliable allocation heuristic in this bounded proxy: 5/5 exhaustive-best selections, 57.17% mean logit-MSE reduction versus all-INT4, and 44.99% reduction versus mean non-selected budget-matched policies. Accuracy was saturated, so the evidence is about output-error preservation rather than task accuracy gains.

## Boundaries and scale limits

Synthetic 2-96-64-48-3 MLP only; weight-only symmetric per-output-channel quantization; dequantized NumPy CPU matmuls; no packed INT4/INT8 kernels, activation quantization, real pretrained models, or production latency measurements.

## Claim scope

On a five-seed synthetic 3-class spiral MLP CPU proxy, calibration-time per-layer INT4 error tracking selected the exhaustive best one-INT8-layer mixed precision allocation and reduced held-out logit MSE versus all-INT4 and average budget-matched alternatives.

## Why it stopped

Closed as no-paper useful signal: the local proxy supports the mechanism but is synthetic and does not validate real CPU kernel performance or real-model behavior.

## Recommended next action

Run a bounded deepen study on real small pretrained models using packed CPU INT4/INT8 kernels, with latency, memory, and task-loss comparisons against established sensitivity baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model packed CPU validation for per-layer INT4/INT8 error tracking
- Success threshold: Across tested models, tracked mixed precision should reduce task loss or output divergence by at least 25% versus all-INT4 and beat the mean budget-matched baseline while preserving a measurable storage or latency advantage over all-INT8.
- Stop condition: Stop if tracked allocation fails to beat budget-matched baselines on two real models or if packed CPU kernels erase the expected storage/latency tradeoff.

## Evidence references

- Artifact root: `<local-path>/projects/mixed-precision-int4-int8-cpu-quantization-with-per-layer-error-tracking-b16f19e9815c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
