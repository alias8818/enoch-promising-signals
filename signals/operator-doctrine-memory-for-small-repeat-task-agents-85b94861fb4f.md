# Operator-Doctrine Memory for Small Repeat-Task Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-for-small-repeat-task-agents-85b94861fb4f`
Run ID: `operator-doctrine-memory-for-small-repeat-task-agents-85b94861fb4f-20260620T081822257510+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bf455e7e63d3

## What looked useful

Layered doctrine memory achieved 1.0000 exact accuracy and 0.0000 violation rate across 34,560 strategy-evaluation episodes; flat retrieval reached 0.2602 exact accuracy with 0.6797 violation rate, transcript search 0.0003 exact accuracy, and no memory 0.0000 exact accuracy.

## Boundaries and scale limits

Synthetic symbolic tasks only; no real operator traces, no LLM extraction/adherence errors, no production latency or long-horizon deployment data.

## Claim scope

On a deterministic synthetic repeated-task replay benchmark, explicit layered operator-doctrine memory with precedence rules preserved current operator/project/task preferences and avoided stale conflicting constraints better than no memory, raw transcript search, and flat retrieval.

## Why it stopped

Closed as no-paper useful signal because the positive mechanism evidence is synthetic/proxy-only rather than direct real-agent validation.

## Recommended next action

Run a bounded direct-evidence follow-up on human-authored or sanitized real repeated-task traces with LLM doctrine extraction noise and blinded scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layered doctrine memory on human-authored repeated-task traces
- Success threshold: Layered doctrine memory improves exact accuracy by at least 20 percentage points over the best baseline and reduces stale-conflict violation rate by at least 50% with no increase in missing required preferences.
- Stop condition: Stop if layered memory fails to beat the best baseline on exact accuracy or if its stale-conflict violation rate is within 10% relative of flat retrieval.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-for-small-repeat-task-agents-85b94861fb4f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
