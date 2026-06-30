# Long-context agent memory compression via hierarchical semantic summarization for extended task sessions

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `long-context-agent-memory-compression-via-hierarchical-semantic-summarization-for-extended-task--ff98d17826ef`
Run ID: `long-context-agent-memory-compression-via-hierarchical-semantic-summarization-for-extended-task--ff98d17826ef-20260614T065034312720+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b71a2bd1b483

## What looked useful

At 64 facts, hierarchical_semantic reached old accuracy 0.255 and middle accuracy 0.278 versus flat_recency 0.042/0.069 and flat_salience 0.037/0.074, with similar overall accuracy around 0.24. At 128 facts, hierarchical_semantic reached old/middle 0.447/0.473 versus flat_recency 0.178/0.233, but recent recall dropped to 0.480 versus flat_recency 0.746. This supports hierarchy as a branch-retention mechanism, not a standalone universal memory policy.

## Boundaries and scale limits

Synthetic structured facts only; no real LLM summarization, no human-authored transcripts, no vector retrieval baseline, no model-native long-context baseline, and no downstream agent task-success measurement. Main run used 40 seeds, 8,000 events, 96 task branches, and fact budgets of 64/128/256/512.

## Claim scope

On a deterministic synthetic multi-task agent-session proxy with structured factual updates, hierarchical semantic grouping improves old and middle branch fact recall under tight compressed-memory budgets, but it does not universally improve overall accuracy because it trades away recent recall.

## Why it stopped

Closed as no-paper useful signal because the evidence is a local structured proxy; it supports a mechanism but is not direct/full validation of long-context LLM-agent memory compression.

## Recommended next action

Run a bounded real-transcript follow-up using actual long agent sessions, LLM-generated hierarchical summaries, a recency-plus-working-memory control, and downstream Q&A/task-success scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transcript evaluation of hierarchical agent memory compression
- Success threshold: At matched token budget, hierarchical plus recent-tier memory improves old-fact accuracy by at least 20 percentage points over flat recency while keeping overall accuracy within 5 percentage points of the best flat baseline across at least 3 independent transcript sets.
- Stop condition: Stop if real LLM summaries fail to preserve structured facts above the flat salience baseline, or if old-fact gains require more than a 10 percentage point loss in overall accuracy after adding a recent working-memory tier.

## Evidence references

- Artifact root: `<local-path>/projects/long-context-agent-memory-compression-via-hierarchical-semantic-summarization-for-extended-task-`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
