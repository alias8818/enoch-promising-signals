# Evidence-Ledger Agent Memory on Repeated Local Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-memory-on-repeated-local-tasks-52f9818bcc74`
Run ID: `evidence-ledger-agent-memory-on-repeated-local-tasks-52f9818bcc74-20260613T045442025019+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3b47ae733d08

## What looked useful

Evidence-ledger memory matched stateless correctness with 0 wrong answers, avoided the 60 stale answers produced by naive memory, and reduced total commands by 50.60% versus stateless rediscovery.

## Boundaries and scale limits

Synthetic repositories only; no LLM coding agent, no real-world repositories, no token metrics, and no long-horizon task completion measurement.

## Claim scope

In a deterministic synthetic repeated-local-task benchmark, an evidence-ledger cache using evidence paths and SHA-256 validation reduced repeated discovery commands while preserving correctness after local file mutations.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a synthetic deterministic proxy rather than direct evidence from an LLM coding agent on real repositories.

## Recommended next action

Run a bounded real-agent follow-up on real local repositories with stateless, naive-memory, and evidence-ledger variants, measuring correctness, commands, tokens, wall-clock, and stale-memory failures.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Evidence-Ledger Memory on Repeated Local Repository Tasks
- Success threshold: Evidence-ledger variant achieves at least 25% lower command and token counts than stateless with no statistically meaningful correctness loss and fewer stale failures than naive memory.
- Stop condition: Stop if evidence-ledger correctness drops below stateless by more than 2 percentage points, stale failures match naive memory, or overhead removes command/token savings.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-memory-on-repeated-local-tasks-52f9818bcc74`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
