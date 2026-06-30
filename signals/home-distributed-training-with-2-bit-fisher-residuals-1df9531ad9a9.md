# Home Distributed Training with 2-bit Fisher Residuals

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `home-distributed-training-with-2-bit-fisher-residuals-1df9531ad9a9`
Run ID: `home-distributed-training-with-2-bit-fisher-residuals-1df9531ad9a9-20260604T230233915643+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/56ed13c59bd9

## What looked useful

All 2-bit methods achieved 15.98x lower gradient communication than FP32 dense gradients. Fisher residuals averaged 0.5251 final accuracy versus 0.5231 for plain 2-bit, 0.5268 for 2-bit full error feedback, and 0.5258 for dense; the Fisher variant was not clearly better and had lower gradient cosine than plain 2-bit.

## Boundaries and scale limits

Small MLP, synthetic teacher-student classification, simulated workers on one GPU, 300 steps, no WAN latency, no asynchronous stragglers, no transformer/LLM scale, and no real home-node networking.

## Claim scope

In a 5-seed simulated 4-worker synchronous SGD teacher-student classification probe on GB10, a 2-bit Fisher-weighted residual buffer did not materially improve final accuracy or gradient fidelity over simpler 2-bit gradient communication controls at the same communication budget.

## Why it stopped

Bounded proxy experiment found no measurable advantage for the Fisher-weighted residual mechanism over simpler 2-bit baselines; this is an early falsification, not a full validation of home distributed training.

## Recommended next action

Stop this variant as no-paper early falsification; only revisit if a transformer-scale follow-up can predeclare a stronger Fisher residual rule and beat plain 2-bit plus full error-feedback controls under the same communication budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-scale control test for 2-bit Fisher residuals
- Success threshold: Fisher residuals must improve validation perplexity by at least 3% versus plain 2-bit and full error-feedback controls at the same communication budget without destabilizing training.
- Stop condition: Stop if Fisher residuals fail to beat both 2-bit controls after a calibrated medium run or if the mechanism requires extra communication/memory that removes the home-distributed advantage.

## Evidence references

- Artifact root: `<local-path>/projects/home-distributed-training-with-2-bit-fisher-residuals-1df9531ad9a9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
