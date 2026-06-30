# Anchor-locked memory on real repeated-agent replay logs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `68`
Project ID: `anchor-locked-memory-on-real-repeated-agent-replay-logs-6af2adf8c5`
Run ID: `anchor-locked-memory-on-real-repeated-agent-replay-logs-6af2adf8c5-20260630T011752112401+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 10, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- weak evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Anchor-Locked Memory for Long-Context CPU Agents: enoch://control-plane/projects/anchor-locked-memory-for-long-context-cpu-agents-3e65e99eeeaa/runs/anchor-locked-memory-for-long-context-cpu-agents-3e65e99eeeaa-20260630T005732002951+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3c3f7d6f11dc

## What looked useful

A deterministic harness over local replay-like logs found that locked anchor chunks recovered mission-critical facts missed by transcript and flat retrieval baselines.

## Boundaries and scale limits

Only one local worker JSONL stream plus prompt/scaffold files was available; no independent multi-session repeated-agent replay corpus or downstream agent-loop success metric was tested.

## Claim scope

Anchor-locked memory improved exact recovery of project invariants on a local sanitized Enoch/Codex worker replay-log proxy: 10/10 vs 6/10 for transcript_search and flat_retrieval.

## Why it stopped

Proxy-only local evidence supports the mechanism but does not directly validate the original real repeated-agent replay-log claim.

## Recommended next action

Stop as no-paper useful signal; the next bounded test should run this harness on a real multi-session repeated-agent replay corpus with noisy/stale metadata controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor-locked memory on multi-session repeated-agent replay corpus
- Success threshold: Anchor-locked memory beats the best non-locked retrieval baseline by >=15 percentage points on exact invariant recovery and shows a positive downstream task-success delta on at least 50 replay sessions.
- Stop condition: Stop if fewer than 20 real replay sessions are available or if anchor-locked recovery fails to beat the tuned flat baseline by at least 5 percentage points in the first 20 sessions.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-locked-memory-on-real-repeated-agent-replay-logs-6af2adf8c5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
