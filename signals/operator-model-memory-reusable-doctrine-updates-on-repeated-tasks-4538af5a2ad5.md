# Operator-Model Memory: Reusable Doctrine Updates on Repeated Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-model-memory-reusable-doctrine-updates-on-repeated-tasks-4538af5a2ad5`
Run ID: `operator-model-memory-reusable-doctrine-updates-on-repeated-tasks-4538af5a2ad5-20260628T064024217392+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/61679df5237a

## What looked useful

Across 200 seeds and 108,000 synthetic task attempts, doctrine memory reached 0.6406 final-quarter success versus 0.3822 for episodic memory and 0.0000 for no memory. Doctrine used 11.995 memory items on average versus 118.71 for episodic memory. A repeat run reproduced all metrics exactly except wall-clock timing.

## Boundaries and scale limits

Synthetic rule-satisfaction proxy only; no real LLM, live operator, human feedback, execution-verified task success, stale-doctrine stress test, or cross-project transfer validation. The benchmark intentionally ran as a short CPU-only local test and does not validate large-model memory behavior.

## Claim scope

In a deterministic synthetic benchmark of repeated operator-task families with stable hidden doctrine requirements and varied surface wording, compressed family-level doctrine updates improved final-quarter task success over no memory and raw episodic recall while using substantially fewer memory items.

## Why it stopped

Stopped at useful synthetic mechanism evidence: the result supports reusable doctrine in a proxy benchmark but is not direct/full validation of an operator model memory system.

## Recommended next action

Run a bounded live-LLM or trace-backed follow-up on real repeated operator tasks with execution-verified labels, comparing no memory, episodic memory, and doctrine updates under a fixed context budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-LLM Doctrine Memory on Repeated Operator Tasks
- Success threshold: Doctrine improves held-out task success by at least 10 percentage points over episodic memory with no increase in severe instruction-compliance failures and at least 50% lower memory-token budget.
- Stop condition: Stop as unsupported if doctrine improves success by less than 5 percentage points over episodic memory or introduces more severe compliance failures than either baseline.

## Evidence references

- Artifact root: `<local-path>/projects/operator-model-memory-reusable-doctrine-updates-on-repeated-tasks-4538af5a2ad5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
