# Long-Context Anchor Memory for Agent Task Handoffs

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `long-context-anchor-memory-for-agent-task-handoffs-2a2ffe6cdf1b`
Run ID: `long-context-anchor-memory-for-agent-task-handoffs-2a2ffe6cdf1b-20260612T021728068048+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f0e02bdbdc90

## What looked useful

Anchor memory recovered all six gold facts in 100% of 200 cases at 120 tokens, while tail recovered 0%, keyword recovered 17.67% mean fact accuracy with 0% all-facts recovery, and rolling summary recovered 8.67% mean fact accuracy with 0% all-facts recovery. Keyword retrieval reached 100% only at 360 tokens, roughly 3.2x the anchor packet size.

## Boundaries and scale limits

Synthetic exact-match recovery only; no real agent traces, no model-in-the-loop resume attempts, no human anchor-authoring burden measurement, and no robustness testing for stale or conflicting anchors.

## Claim scope

In a deterministic synthetic benchmark of long agent transcripts with six early resume-critical facts and later distractors, explicit key/value anchor memory preserved all required facts under 120-360 token handoff budgets, outperforming tail-only, recency-biased keyword retrieval, and lossy rolling-summary baselines at tight budgets.

## Why it stopped

The evidence supports the mechanism only in a synthetic exact-match proxy, not a full validation of real long-context agent task handoffs.

## Recommended next action

Stop this run as a no-paper useful signal; next, run a bounded real-trace replay where a model resumes from equal-budget anchor versus non-anchor handoff packets and must execute the correct next command or edit.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace model-in-the-loop anchor handoff replay
- Success threshold: Anchor packets improve next-action correctness by at least 20 percentage points over the strongest non-anchor baseline at the same token budget, with no more than 5 percentage points increase in stale or misleading resume actions.
- Stop condition: Stop if anchor packets fail to beat the strongest non-anchor baseline by at least 10 percentage points on next-action correctness after 30 traces, or if stale/conflicting anchors cause more than 10% misleading resumes.

## Evidence references

- Artifact root: `<local-path>/projects/long-context-anchor-memory-for-agent-task-handoffs-2a2ffe6cdf1b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
