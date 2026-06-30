# Classifier-Based Safe Agent Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `classifier-based-safe-agent-pretraining-8fd9fe301c67`
Run ID: `classifier-based-safe-agent-pretraining-8fd9fe301c67-20260525T175120989687+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9dc65dc46b70

## What looked useful

Matched classifier pretraining reduced early violation rate from 0.1369 to 0.0398 versus no pretraining across 64 seeds, but shifted classifier pretraining increased early violation rate from 0.0606 to 0.2405 and reduced final return. Safety-classifier pretraining needs held-out unsafe-pattern validation and calibration gates before scaling.

## Boundaries and scale limits

Toy tabular control only; no language-agent training, no neural policy, no real tool-use benchmark, and no large-scale pretraining. Classifier labels are synthetic and the shifted suite is a proxy for realistic distribution shift.

## Claim scope

In a 12-state synthetic tabular safety environment, classifier-based Q-value pretraining reduced early unsafe exploration when the safety classifier matched the deployment hazard distribution, but failed under a held-out hazard shift.

## Why it stopped

Proxy toy result provides useful mixed evidence but is not a full validation; broad robustness is early-falsified by the shifted classifier suite.

## Recommended next action

Run a bounded neural follow-up with held-out unsafe patterns and classifier calibration/abstention; stop treating matched-distribution toy gains as sufficient evidence for safe agent pretraining.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated classifier pretraining under held-out unsafe patterns
- Success threshold: Calibration/abstention classifier pretraining must reduce matched early violation rate by at least 30% versus no pretraining and must not increase shifted early violation rate by more than 5 percentage points versus no pretraining.
- Stop condition: Stop if unsafe recall or calibration cannot be measured on held-out hazards, or if shifted early violations exceed the no-pretraining baseline by more than 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/classifier-based-safe-agent-pretraining-8fd9fe301c67`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
