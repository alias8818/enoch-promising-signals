# Home-Runnable Volunteer Training Simulator with Realistic Failure Modes

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `home-runnable-volunteer-training-simulator-with-realistic-failure-modes-e03b97a10d97`
Run ID: `home-runnable-volunteer-training-simulator-with-realistic-failure-modes-e03b97a10d97-20260628T222532067472+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fa04f23a4af5

## What looked useful

The prototype generated 2,400 scenarios in 0.053020823979750276 seconds at 17,812 kB max RSS, covered all 6 defined failure modes globally, produced 1,967 unique scenario signatures, and had 0 replay mismatches. Standard-library tests passed.

## Boundaries and scale limits

This run used authored failure modes and scripted learner behavior only. It did not use field incident logs, real volunteers, delayed retention tests, live operations, or a controlled comparison against static training materials.

## Claim scope

A dependency-light Python prototype can run on a home-class machine and generate replayable volunteer-coordination scenarios with injected failure modes, full defined-mode coverage over a 2,400-scenario local evaluation, zero deterministic replay mismatches, and low measured resource use.

## Why it stopped

Local proxy evidence supports technical feasibility but does not directly validate realistic field failure modes or human training efficacy.

## Recommended next action

Stop this run as no-paper useful signal; next run should conduct a bounded human pilot with a field-derived incident taxonomy and static-training control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded human pilot for replayable volunteer failure-mode simulator
- Success threshold: Simulator group improves matched post-test decision accuracy by at least 15 percentage points over static training while median setup time remains under 10 minutes.
- Stop condition: Stop if recruitment cannot obtain a small volunteer sample, if field-derived incidents do not map cleanly to simulator failure modes, or if setup burden exceeds 10 minutes median.

## Evidence references

- Artifact root: `<local-path>/projects/home-runnable-volunteer-training-simulator-with-realistic-failure-modes-e03b97a10d97`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
