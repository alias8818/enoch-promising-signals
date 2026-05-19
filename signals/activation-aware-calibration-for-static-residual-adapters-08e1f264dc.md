# Activation-aware calibration for static residual adapters

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `activation-aware-calibration-for-static-residual-adapters-08e1f264dc`
Run ID: `activation-aware-calibration-for-static-residual-adapters-08e1f264dc-20260519T031023556192+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Activation-aware calibration for static residual adapters: internal_generated:activation-aware-calibration-for-static-residual-adapters-08e1f264dc

## What looked useful

Calibration set adapter residual RMS to the intended 5% block-residual ratio and improved mean target NLL from 2.4238 for random adapters to 2.3790 across seeds 0, 1, and 2; full fine-tuning remained much better at 1.7973 NLL.

## Boundaries and scale limits

Validation used a small character-level transformer and local Python-source target corpus, not GPT-2-small-class pretrained adaptation, subword-tokenized standard benchmarks, larger ranks, or long/full-scale training.

## Claim scope

In a bounded 4-layer character-transformer source-to-Python-code adaptation study, activation-aware RMS calibration of rank-8 static residual adapters consistently improved target validation NLL versus otherwise identical random adapters across three seeds.

## Why it stopped

No-paper closure: bounded direct evidence supports the calibration mechanism, but the experiment is too small and full fine-tuning is too far ahead for publication-grade claims.

## Recommended next action

Run one final depth-4 bounded deepen test on a GPT-2-small-class pretrained model with a standard text/code target corpus and stronger adapter initialization controls; stop if the calibrated-over-control NLL gain does not persist.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small validation of activation-aware residual adapter calibration
- Success threshold: Calibrated adapters improve mean held-out target NLL by at least 0.03 versus the strongest non-activation-aware adapter control across seeds and recover at least 25% of the random-adapter-to-full-finetune NLL gap.
- Stop condition: Stop negative if calibrated adapters fail to beat the strongest non-activation-aware adapter control by 0.03 mean NLL or if calibration gains are seed-fragile.

## Evidence references

- Artifact root: `<local-path>/projects/activation-aware-calibration-for-static-residual-adapters-08e1f264dc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
