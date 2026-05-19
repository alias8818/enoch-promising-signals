# Controlled ResidualFP channel ablations in a longer tiny LM run

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `controlled-residualfp-channel-ablations-in-a-longer-tiny-l-d79bfcfb7c`
Run ID: `controlled-residualfp-channel-ablations-in-a-longer-tiny-l-d79bfcfb7c-20260517T145933309463+0000`

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

- Internal Enoch project: Controlled ResidualFP channel ablations in a longer tiny LM run: internal_generated:controlled-residualfp-channel-ablations-in-a-longer-tiny-l-d79bfcfb7c

## What looked useful

ResidualFP channel masking produced a consistent mechanism signal: full masking increased mean validation loss by +0.05837, and 50% training-time channel ablation reduced learned FP gain and the full-mask damage. However, unablated ResidualFP was slightly worse than dense by +0.00090 mean validation loss, so the practical performance hypothesis was not supported.

## Boundaries and scale limits

Results are limited to a tiny character-level LM, Tiny Shakespeare, one ResidualFP operationalization, 3 seeds, and 5,000 training steps. This is not evidence about GPT-2-small-class or larger subword LMs.

## Claim scope

In a 466k-parameter character-level GPT-style Tiny Shakespeare LM trained for 5,000 steps across seeds 11, 17, and 23, the tested ResidualFP implementation learns load-bearing reserved MLP residual fast-path channels, but does not improve validation loss over a dense baseline.

## Why it stopped

Tier-2 local evidence directly tested the target metric with fixed seeds, a dense baseline, and ablation controls; the mechanism exists but did not beat the baseline.

## Recommended next action

Stop this branch as no-paper evidence; only pursue a new bounded follow-up if testing a parameter-matched or regularized ResidualFP variant with the same fixed-batch ablation diagnostics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-matched and regularized ResidualFP fast-path test
- Success threshold: Mean validation loss improves over dense by >= 0.005 across 3 seeds and full channel ablation increases validation loss by >= 0.03 without relying on different validation batches.
- Stop condition: Stop if the parameter-matched or regularized variant fails to beat dense by 0.005 mean validation loss or loses the monotonic channel-ablation mechanism signal.

## Evidence references

- Artifact root: `<local-path>/projects/controlled-residualfp-channel-ablations-in-a-longer-tiny-l-d79bfcfb7c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
