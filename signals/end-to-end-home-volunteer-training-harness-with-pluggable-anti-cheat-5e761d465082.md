# End-to-end home volunteer training harness with pluggable anti-cheat

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `end-to-end-home-volunteer-training-harness-with-pluggable-anti-cheat-5e761d465082`
Run ID: `end-to-end-home-volunteer-training-harness-with-pluggable-anti-cheat-5e761d465082-20260621T213300762054+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b48e51090c9f

## What looked useful

On 5,000 deterministic synthetic sessions, the harness detected 1,000/1,000 speedrun cheats, 1,000/1,000 identity-swap cheats, and 1,000/1,000 answer-flood cheats with 0/1,000 honest false positives and 0.0217 ms/session mean evaluation latency, but missed 1,000/1,000 stealth-assist cheats.

## Boundaries and scale limits

Synthetic generator only; no real volunteers, browser instrumentation, LMS integration, privacy-preserving liveness checks, accessibility cohort, or field deployment were tested. The benchmark is CPU-only and not a full validation of at-home training integrity.

## Claim scope

A local Python prototype demonstrates that a small pluggable anti-cheat API can detect synthetic trace-visible volunteer-training cheating modes with negligible evaluation latency, while also showing that local traces alone miss stealth helper-assisted completion.

## Why it stopped

Synthetic local evidence is mixed: trace-visible cheating is detected, but stealth off-device assistance is an early falsification for local-trace-only anti-cheat claims rather than a full field validation.

## Recommended next action

Stop this run as a no-paper useful signal; next run should add a consented browser challenge-response/liveness plugin and test whether it detects helper-assisted completion without raising honest false positives.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Consent-based liveness challenge plugin for helper-assisted at-home training
- Success threshold: Detect at least 80% of controlled helper-assisted sessions with less than 5% false positives on honest controlled sessions and less than 250 ms added median client-side latency per challenge.
- Stop condition: Stop if liveness challenges do not exceed 60% helper-assist recall at 5% honest false-positive rate, or if the intervention requires privacy-sensitive data beyond explicit consent and local processing.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-home-volunteer-training-harness-with-pluggable-anti-cheat-5e761d465082`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
