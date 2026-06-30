# Anchor-Locked Memory for Long-Context CPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-locked-memory-for-long-context-cpu-agents-3e65e99eeeaa`
Run ID: `anchor-locked-memory-for-long-context-cpu-agents-3e65e99eeeaa-20260630T005732002951+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3c3f7d6f11dc

## What looked useful

Anchor-locked memory reached 600/600 correct queries in every noise condition, while sliding context stayed at 2-6/600 and flat recency retrieval fell from 109/600 at low noise to 4-6/600 at higher noise because later stale mentions overwrote canonical facts.

## Boundaries and scale limits

Tested only synthetic generated facts on one CPU process: 160 anchors, 8 sessions, 600 queries per condition, and up to 27,820 events per condition. No real LLM agent, embedding retriever, production persistence, adversarial anchor aliasing, or long-running deployment was tested.

## Claim scope

In deterministic synthetic replay tasks with explicit stable anchor IDs and authoritative first-write locks, anchor-locked memory preserved correct anchored fact recall under stale and contradictory later context.

## Why it stopped

Synthetic mechanism evidence is useful but not sufficient for paper-grade validation of long-context CPU agents.

## Recommended next action

Run a bounded deepen test on real or semi-real repeated-agent replay logs with hidden ground truth and a BM25 or embedding retrieval baseline before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor-locked memory on real repeated-agent replay logs
- Success threshold: Anchor-locked memory improves exact-match anchored recall by at least 20 percentage points over the best non-locking baseline with no more than 10 percent query-latency overhead on the replay workload.
- Stop condition: Stop if anchor IDs are absent or ambiguous in more than 30 percent of candidate real replay tasks, or if anchor-locked recall is within 5 percentage points of the best baseline.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-locked-memory-for-long-context-cpu-agents-3e65e99eeeaa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
