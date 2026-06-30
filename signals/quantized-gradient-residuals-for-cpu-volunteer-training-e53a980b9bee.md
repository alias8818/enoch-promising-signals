# Quantized Gradient Residuals for CPU Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantized-gradient-residuals-for-cpu-volunteer-training-e53a980b9bee`
Run ID: `quantized-gradient-residuals-for-cpu-volunteer-training-e53a980b9bee-20260604T150141000579+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5996c637976a

## What looked useful

Across three seeds, 2-bit quantization without residuals degraded validation loss by +0.0120 +/- 0.0013 versus FP32, while 2-bit residual quantization had -0.00012 +/- 0.00047 loss delta at the same 93.49% byte reduction. Residuals also reduced the 4-bit loss delta from +0.000172 to +0.000012 at 87.24% byte reduction.

## Boundaries and scale limits

Synthetic convex model only; no real volunteer network, no asynchronous or stale updates, no worker churn, no privacy/security overhead, no neural-network or transformer training, and no distributed wall-clock throughput measurement.

## Claim scope

In a synthetic CPU-local 8-worker synchronous logistic-regression proxy with non-IID shards, per-worker residual error feedback lets 2-bit and 4-bit uniform quantized gradients match FP32 validation loss while reducing transmitted gradient bytes by 93.49% and 87.24%, respectively.

## Why it stopped

No-paper closure: the result is a useful synthetic mechanism signal, not direct evidence for real CPU volunteer training or a publication-grade validation.

## Recommended next action

Run a bounded deeper test on a small neural model with simulated volunteer churn/asynchrony and FP32, q4/q2 no-residual, and q4/q2 residual controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual Quantized Gradients Under Simulated Volunteer Churn
- Success threshold: Residual q4 or q2 reaches within 1% relative validation loss of FP32 and improves final validation loss by at least 0.005 over no-residual quantization at the same transmitted-byte budget in at least 3 seeds.
- Stop condition: Stop as negative if residual q4/q2 fails to beat no-residual by 0.005 validation loss or cannot remain within 1% relative validation loss of FP32 under churn/asynchrony.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-gradient-residuals-for-cpu-volunteer-training-e53a980b9bee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
