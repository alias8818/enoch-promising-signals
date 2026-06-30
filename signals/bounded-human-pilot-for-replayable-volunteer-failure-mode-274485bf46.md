# Bounded human pilot for replayable volunteer failure-mode simulator

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-human-pilot-for-replayable-volunteer-failure-mode-274485bf46`
Run ID: `bounded-human-pilot-for-replayable-volunteer-failure-mode-274485bf46-20260628T225656773898+0000`

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

- Parent run decision: Home-Runnable Volunteer Training Simulator with Realistic Failure Modes: enoch://control-plane/projects/home-runnable-volunteer-training-simulator-with-realistic-failure-modes-e03b97a10d97/runs/home-runnable-volunteer-training-simulator-with-realistic-failure-modes-e03b97a10d97-20260628T222532067472+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fa04f23a4af5

## What looked useful

Replay digests matched exactly. Medium run covered 5 scenarios x 80 seeds x 2 policies with 46 volunteers and 180 tasks per run. Risk-aware dispatch reduced synthetic failure rates by 2.37 percentage points in baseline and 2.43 percentage points in skill-mismatch scenarios, but showed essentially zero advantage in coordination-lag and combined stress scenarios.

## Boundaries and scale limits

No real volunteers, consent flow, coordinator UI, field organization data, or human timing traces were tested. The result supports simulator mechanics and pilot design only, not behavioral validity or publication-grade human evidence.

## Claim scope

A pure-Python synthetic simulator can replay volunteer failure-mode traces exactly and produce scenario-specific dispatch metrics over 80 seeded runs per scenario. In this synthetic setup, risk-aware dispatch reduced failure rates for baseline and skill-mismatch scenarios, was weak under dropout-wave stress, and did not improve coordination-lag or combined overload scenarios.

## Why it stopped

Proxy-only synthetic evidence produced a useful simulator and mixed mechanism signal, but no direct human-pilot validation.

## Recommended next action

Stop paper pursuit from this run; run a bounded consented human/coordinator pilot using the same replayable scenario traces and compare observed decision delays and failure modes against simulator predictions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded human validation of replayable volunteer failure-mode scenarios
- Success threshold: At least 75% of participants reproduce the simulator-predicted policy advantage direction for skill-mismatch and no-advantage direction for coordination-lag/combined scenarios, with replay logs matching assigned event streams.
- Stop condition: Stop if replay logs cannot be made equivalent across participants, if fewer than 6 usable participant traces are collected, or if plausibility ratings indicate the injected failures are not credible.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-human-pilot-for-replayable-volunteer-failure-mode-274485bf46`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
