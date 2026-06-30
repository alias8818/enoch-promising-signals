# Capability Proof-of-Work for Volunteer Training Credit

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `capability-proof-of-work-for-volunteer-training-credit-2ffa441f8b42`
Run ID: `capability-proof-of-work-for-volunteer-training-credit-2ffa441f8b42-20260608T061611646448+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c7fc803dce9c

## What looked useful

Capability proof-of-work reduced worst-case false-credit versus attendance logs in all scenarios and reduced dishonest false-credit versus static quiz in three of four scenarios, but the weak-training-effect scenario showed higher dishonest false-credit for capability proof than static quiz. Proxy solving also left substantial residual false-credit under high proxy attack.

## Boundaries and scale limits

No real volunteer cohorts, no real training tasks, no field adversaries, no accessibility/fairness analysis, no policy validation, and no downstream volunteer performance measurement were tested. The experiment used 30,000 synthetic trials per group across four scenarios.

## Claim scope

Synthetic item-response simulations show that randomized capability proof tasks can reduce false volunteer training credit compared with attendance logs and leakage-prone static quizzes under explicit assumptions about capability separation, task-bank leakage, and proxy solving.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy only and the result is mixed rather than a direct validation of volunteer training credit.

## Recommended next action

Run a bounded field-style pilot with a real volunteer task bank, held-out randomized proof tasks, pre/post training cohorts, and identity/proxy controls before making any paper or deployment claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Field-Style Calibration of Capability Proof Tasks for Volunteer Training Credit
- Success threshold: Capability proof achieves trained accept rate >= 0.70 and dishonest false-credit at least 0.25 absolute below static quiz while not increasing accessibility failures beyond a pre-registered tolerance.
- Stop condition: Stop if trained accept rate is below 0.60, dishonest false-credit is not lower than static quiz by at least 0.10 absolute, or proxy/accessibility failures dominate the measured effect.

## Evidence references

- Artifact root: `<local-path>/projects/capability-proof-of-work-for-volunteer-training-credit-2ffa441f8b42`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
