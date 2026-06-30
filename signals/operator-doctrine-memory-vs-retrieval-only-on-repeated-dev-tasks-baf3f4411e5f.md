# Operator-Doctrine Memory vs Retrieval-Only on Repeated Dev Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-vs-retrieval-only-on-repeated-dev-tasks-baf3f4411e5f`
Run ID: `operator-doctrine-memory-vs-retrieval-only-on-repeated-dev-tasks-baf3f4411e5f-20260619T112232286451+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cfd9f4a57e07

## What looked useful

Layered doctrine memory reached 0.542 exact match and 1.000 recall across 1100 scored rows per strategy, versus 0.151 exact match and 0.573 recall for flat retrieval. The mean exact-match delta versus flat retrieval was +0.391, with all five seed deltas at least +0.377. Budget sensitivity runs at 45, 90, and 180 approximate tokens preserved positive deltas of +0.440 to +0.517.

## Boundaries and scale limits

Synthetic task generator, symbolic compliance checker, simple lexical retrieval baseline, no live LLM-agent runs, no real operator traces, and no human grading.

## Claim scope

In a deterministic synthetic repeated-dev-task replay with noisy prior transcripts and equal approximate context budgets, compact project/topic-scoped operator-doctrine memory improved exact rule compliance over transcript search and flat retrieval.

## Why it stopped

Synthetic proxy evidence supports the mechanism but is not direct/full validation and is insufficient for a paper-ready positive decision.

## Recommended next action

Stop this run as no-paper useful signal; next run should evaluate a live LLM agent on held-out repeated dev-task replays with a stronger retrieval-only baseline and executable or human grading.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-agent repeated dev-task replay for operator-doctrine memory
- Success threshold: Doctrine memory improves exact compliance by >=10 percentage points over strong retrieval-only baseline while irrelevant-rule false-positive rate increases by <=5 percentage points.
- Stop condition: Stop if doctrine memory fails to beat retrieval-only by 10 percentage points on exact compliance or if false positives increase by more than 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-retrieval-only-on-repeated-dev-tasks-baf3f4411e5f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
