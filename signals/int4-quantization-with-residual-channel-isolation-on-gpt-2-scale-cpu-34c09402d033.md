# INT4 Quantization with Residual Channel Isolation on GPT-2-Scale CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int4-quantization-with-residual-channel-isolation-on-gpt-2-scale-cpu-34c09402d033`
Run ID: `int4-quantization-with-residual-channel-isolation-on-gpt-2-scale-cpu-34c09402d033-20260608T214406112541+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/aed08e2299b1

## What looked useful

Across 20 bounded CPU runs, residual-ranked full-precision isolation reduced weighted output MSE by 8.66%, 15.28%, 23.87%, and 30.47% at 0.25%, 0.5%, 1%, and 2% isolated channels respectively; random isolation reduced only 0.32%, 0.37%, 0.89%, and 1.78%. Residual ranking beat random in every seed/fraction condition.

## Boundaries and scale limits

No pretrained GPT-2 weights, real text activations, perplexity evaluation, downstream task evaluation, or packed INT4 CPU kernel were tested. Timing uses dequantized dense fp32 NumPy matmuls and must not be interpreted as INT4 serving throughput.

## Claim scope

On GPT-2-small projection matrix dimensions with synthetic heavy-tailed weights and activations, ranking output channels by calibration residual identifies a small full-precision channel subset that reduces held-out INT4 output reconstruction MSE far more than random channel isolation at the same storage budget.

## Why it stopped

Synthetic GPT-2-shaped reconstruction evidence supports the mechanism but is proxy-only and does not validate pretrained GPT-2 quality or packed CPU INT4 performance.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same residual-channel selection on actual GPT-2-small weights and real calibration text, with held-out perplexity versus plain INT4 and an outlier-channel baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate residual channel isolation on real GPT-2-small perplexity
- Success threshold: At 1% isolated channels, residual-ranked isolation recovers at least 50% of the perplexity degradation from plain INT4 and beats both random and magnitude-ranked controls by at least 20% relative error recovery without reducing estimated compression below 6.5x versus fp32.
- Stop condition: Stop if residual-ranked isolation fails to beat magnitude-ranked or random controls on held-out perplexity at 0.5%, 1%, and 2% isolated channels, or if the mixed path removes the expected CPU memory/compression advantage.

## Evidence references

- Artifact root: `<local-path>/projects/int4-quantization-with-residual-channel-isolation-on-gpt-2-scale-cpu-34c09402d033`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
