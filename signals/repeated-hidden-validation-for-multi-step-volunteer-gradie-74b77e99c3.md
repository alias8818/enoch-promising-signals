# Repeated Hidden Validation for Multi-Step Volunteer Gradient Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `repeated-hidden-validation-for-multi-step-volunteer-gradie-74b77e99c3`
Run ID: `repeated-hidden-validation-for-multi-step-volunteer-gradie-74b77e99c3-20260518T050253557061+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/cc45d3b9e238

## What looked useful

Repeated hidden validation is a useful harmful-gradient filter versus no validation, improving mean test accuracy by 18.4 points and reducing malicious acceptance by 97.3 points, but it did not materially beat one-shot hidden validation on held-out accuracy.

## Boundaries and scale limits

Small synthetic 2D classification only; no LLM-scale training, real volunteer network, real corpus, adaptive adversary, collusion, Sybil attack, privacy mechanism, or long-horizon hidden-validator overfitting test.

## Claim scope

In a 10-seed synthetic neural classification simulation with 12 volunteer gradient providers, 50% label-flip malicious volunteers, and 80 multi-step training rounds, repeated hidden validation reduced malicious update acceptance from 100% to 2.7% and recovered held-out accuracy near the honest-only oracle.

## Why it stopped

No-paper useful signal: the controlled direct test supports hidden validation as a harmful-gradient filter but does not show that repeated validation materially improves the main held-out metric over the simpler one-shot hidden-validation baseline.

## Recommended next action

Run a medium direct comparison on a GPT-2-small-class or other real sequence task where repeated validation must beat one-shot hidden validation by at least 2% relative validation loss or 1 absolute accuracy point under adaptive or heterogeneous volunteer attacks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Real-Task Repeated vs One-Shot Hidden Volunteer Gradient Validation
- Success threshold: Repeated hidden validation must beat one-shot hidden validation by at least 2% relative validation loss or 1 absolute accuracy point while keeping malicious acceptance below 10% and not underperforming honest-only oracle by more than 3%.
- Stop condition: Stop as no-paper if repeated validation fails to materially beat one-shot hidden validation on the primary held-out metric or if hidden-set overfitting/adaptive attacks erase the malicious-acceptance advantage.

## Evidence references

- Artifact root: `<local-path>/projects/repeated-hidden-validation-for-multi-step-volunteer-gradie-74b77e99c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
