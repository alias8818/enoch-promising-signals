# Held-out noisy replay validation for layered home-task memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `held-out-noisy-replay-validation-for-layered-home-task-mem-c896cad12a`
Run ID: `held-out-noisy-replay-validation-for-layered-home-task-mem-c896cad12a-20260629T225548551544+0000`

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

- Parent run decision: Medium realistic replay for layered home-task memory: enoch://control-plane/projects/medium-realistic-replay-for-layered-home-task-memory-dc639fff99/runs/medium-realistic-replay-for-layered-home-task-memory-dc639fff99-20260629T212413216073+0000
- Parent run decision: Human-authored replay validation for layered home-task memory: enoch://control-plane/projects/human-authored-replay-validation-for-layered-home-task-mem-9deab5203b/runs/human-authored-replay-validation-for-layered-home-task-mem-9deab5203b-20260629T214134815942+0000

## What looked useful

Layered doctrine memory reached 1.000 mean exact-match accuracy across tested noise levels; transcript search reached 0.967 and flat retrieval 0.928, so the layered strategy provided a modest +0.0328125 mean accuracy lift over the best non-layered baseline.

## Boundaries and scale limits

Synthetic only: 64 households, 16 held-out households per noise level, 128 held-out queries per noise level, five noise levels, no real operator logs, no LLM extraction, no embedding retrieval, no long-horizon production agent sessions.

## Claim scope

On a deterministic synthetic held-out home-task replay benchmark with controlled noisy and contradictory memory records, explicit layered slot memory improved exact fact recall over no-memory, flat retrieval, and transcript-search baselines.

## Why it stopped

Closed as no-paper useful signal because the result is synthetic/proxy evidence with a modest baseline gap, not a direct real-agent or real-user validation.

## Recommended next action

Run a bounded direct-evidence follow-up using LLM-extracted memory summaries and an embedding retrieval baseline on realistic repeated home-task replay transcripts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LLM-extracted noisy home-task replay validation
- Success threshold: Layered memory improves exact recall by at least 0.05 over the best non-layered practical baseline at 0.30 and 0.60 noise with no worse than comparable abstention or contradiction rate.
- Stop condition: Stop if layered memory fails to beat the best non-layered baseline by 0.02 at 0.30 noise or if LLM extraction noise makes the benchmark labels non-adjudicable.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-noisy-replay-validation-for-layered-home-task-mem-c896cad12a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
