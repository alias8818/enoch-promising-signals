# Random Probe Verification of Volunteer Training Steps

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `random-probe-verification-of-volunteer-training-steps-655dfceaf4b0`
Run ID: `random-probe-verification-of-volunteer-training-steps-655dfceaf4b0-20260526T051140905998+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a7ef6cb17638

## What looked useful

Random probes are useful as a population-level tripwire when deficiencies are clustered, but sparse one-step omissions require hundreds of checks and still do not certify every deficient volunteer. Rare single-step failures required 621/2400 uniform checks or 800/2400 stratified checks to reach 0.95 probability of detecting any problem; detecting all deficient volunteers remained near zero under sparse failures even at half-checklist sampling.

## Boundaries and scale limits

No real volunteer training logs, no human behavior model, no adversarial behavior, no operational cost data, and no deployed-system validation. The result supports only a proxy population-audit claim, not full verification of individual completion.

## Claim scope

Synthetic audit model with 200 volunteers, 12 training steps, four injected failure regimes, and random probe designs evaluated by exact detection probabilities plus 5000-trial Monte Carlo checks.

## Why it stopped

Synthetic/proxy evidence is sufficient to show the limitation of random probes for sparse failures, but it is not direct validation of real volunteer training verification.

## Recommended next action

Stop this as a no-paper useful signal; a bounded follow-up should replay the same audit designs on deidentified or realistic training-step traces with injected omissions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Calibrated Random Probe Verification for Volunteer Training Logs
- Success threshold: >=0.95 probability of detecting injected problem batches at <=25% full-audit cost, with explicit reporting if all-deficient-volunteer detection remains below 0.90.
- Stop condition: Stop if trace-calibrated sparse omissions need more than 50% full-audit cost to reach 0.95 any-defect detection or if all-deficient-volunteer detection remains below 0.50 at 50% full-audit cost.

## Evidence references

- Artifact root: `<local-path>/projects/random-probe-verification-of-volunteer-training-steps-655dfceaf4b0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
