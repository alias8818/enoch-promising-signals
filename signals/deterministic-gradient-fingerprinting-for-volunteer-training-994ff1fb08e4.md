# Deterministic Gradient Fingerprinting for Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `deterministic-gradient-fingerprinting-for-volunteer-training-994ff1fb08e4`
Run ID: `deterministic-gradient-fingerprinting-for-volunteer-training-994ff1fb08e4-20260525T144831172073+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2348c1aa266a

## What looked useful

Weak fingerprints up to alpha=0.2 preserved utility but only reached AUC 0.763; alpha=0.3 preserved utility but reached AUC 0.867; alpha=0.4 reached AUC 0.934 but reduced accuracy by 0.037, exceeding the pre-declared utility-loss threshold.

## Boundaries and scale limits

Synthetic data, logistic regression only, no secure aggregation, no clipping/noise, no adversarial volunteers, no real neural-network or GPT-2-small-class training, and no multi-node volunteer hardware. This is a bounded mechanism probe, not a full validation.

## Claim scope

In a deterministic synthetic volunteer-training logistic-regression simulator with 64 volunteers, 8 participants per round, 512-dimensional gradients, and 240 rounds, per-volunteer Rademacher gradient fingerprints produced monotonically stronger participant-recovery signal as fingerprint strength increased, but no tested strength satisfied both AUC >= 0.90 and accuracy drop <= 0.02 versus the un-fingerprinted baseline.

## Why it stopped

Early bounded synthetic evidence did not meet the combined recovery-plus-utility threshold; this is not a full validation or a universal falsification.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test multi-round accumulated attribution or error-correcting fingerprint codes on a small neural model before attempting scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-round deterministic fingerprint accumulation on a small neural volunteer-training model
- Success threshold: AUC >= 0.90 and TPR at 1% FPR >= 0.50 with final validation metric drop <=0.02 versus baseline across at least three deterministic seeds.
- Stop condition: Stop if no setting reaches AUC >= 0.85 without exceeding a 0.02 validation-metric drop, or if the next meaningful test requires more than the local short-run budget without a stronger small-model signal.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-gradient-fingerprinting-for-volunteer-training-994ff1fb08e4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
