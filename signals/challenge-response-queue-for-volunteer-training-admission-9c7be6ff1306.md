# Challenge-response queue for volunteer training admission

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `challenge-response-queue-for-volunteer-training-admission-9c7be6ff1306`
Run ID: `challenge-response-queue-for-volunteer-training-admission-9c7be6ff1306-20260630T144324931323+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5c910545da46

## What looked useful

Challenge-response queues are promising as overload filters but not as standalone admission gates. A grace/manual fallback lane materially reduced modeled disparity while preserving most quality gains.

## Boundaries and scale limits

Synthetic assumptions only; no real applicant data, no real challenge content, no measured retention, no field pilot, and no publication-grade external validation.

## Claim scope

In a synthetic 180-day volunteer-training queue simulation with weekly cohorts, challenge-response admission increased committed-attendee share versus FIFO, especially under overload, but challenge-only admission produced substantial access disparity when response probability differed by applicant segment.

## Why it stopped

The evidence is synthetic and mechanism-level: useful for policy design, but insufficient for deployment or paper-positive claims.

## Recommended next action

Stop short of paper claims; run a bounded sensitivity sweep over challenge difficulty, fallback capacity, and admission-disparity thresholds before any field pilot.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Policy frontier for challenge-response volunteer admission
- Success threshold: Find at least one policy region with >=0.20 committed-attendee share gain versus FIFO, >=0.75 seat utilization under overload, <0.10 committed false rejection, and <0.07 mainstream-minus-underserved committed-admission gap.
- Stop condition: Stop if no tested policy setting meets all thresholds across both low-gap and high-gap scenarios, or if gains only occur by exceeding the disparity or false-rejection thresholds.

## Evidence references

- Artifact root: `<local-path>/projects/challenge-response-queue-for-volunteer-training-admission-9c7be6ff1306`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
