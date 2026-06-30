# Blockwise 8-bit Adam CPU Trainer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `blockwise-8-bit-adam-cpu-trainer-e211827cc29e`
Run ID: `blockwise-8-bit-adam-cpu-trainer-e211827cc29e-20260603T225943746707+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/71331c498ab7

## What looked useful

Naive independent blockwise linear quantization of Adam moments is unstable because underestimated second moments can explode updates. Adding a v_hat >= m_hat^2 floor stabilizes the method and preserves the intended memory reduction, but the unfused NumPy CPU implementation is materially slower than Adam32.

## Boundaries and scale limits

Synthetic optimizer proxy only; no real neural-network training, no GPT-2-class model, no fused CPU kernel, and no datacenter-scale validation.

## Claim scope

On a deterministic NumPy quadratic optimizer benchmark up to 1,048,576 parameters, stabilized persistent blockwise 8-bit Adam state reduced optimizer-state memory by 74.93% versus float32 Adam while preserving qualitative convergence, but with a 2.94x to 3.62x CPU update slowdown and a small quantization-limited residual loss.

## Why it stopped

Proxy evidence supports a mechanism and exposes the stability requirement, but the current result is not direct or strong enough for a paper and shows significant CPU overhead.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should implement a fused CPU kernel and validate on a real small model against Adam32.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused stabilized blockwise 8-bit Adam on a real CPU training task
- Success threshold: At least 70% optimizer-state memory reduction, final validation loss or accuracy within 5% of Adam32, no divergence across three seeds, and <=1.5x mean step-time slowdown.
- Stop condition: Stop if the fused implementation remains >2x slower than Adam32, diverges at Adam32-useful learning rates, or misses Adam32 validation quality by more than 10%.

## Evidence references

- Artifact root: `<local-path>/projects/blockwise-8-bit-adam-cpu-trainer-e211827cc29e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
