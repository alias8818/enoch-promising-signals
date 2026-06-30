# Two-Level Agent Memory: Anchors Plus Operator Doctrine

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `two-level-agent-memory-anchors-plus-operator-doctrine-4fb7f3f91592`
Run ID: `two-level-agent-memory-anchors-plus-operator-doctrine-4fb7f3f91592-20260610T065228504416+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/40ad4bcae45f

## What looked useful

Two-level retrieval achieved 0.698 exact rate on 6000 paired confirmation trials versus 0.3725 for the best flat baseline, with positive gains in all 15 budget/noise sweep cells. The failure mechanism was flat top-k crowding out exact anchors while still retrieving doctrine.

## Boundaries and scale limits

Synthetic generated memories only; no real agent traces, no LLM answerer, no production memory writes, no long-horizon deployment, and no validation on tasks that require only one memory level or neither memory level.

## Claim scope

In a deterministic synthetic bounded-context retrieval benchmark where each query requires one operator-doctrine item and one episodic-anchor item, reserving separate retrieval budget for doctrine and anchors improves exact availability of both required items compared with flat top-k retrieval under the same item budget.

## Why it stopped

This run produced a useful synthetic mechanism signal but not direct real-agent evidence, so it is no-paper evidence rather than publication-grade validation.

## Recommended next action

Run a bounded follow-up on a small real agent trace corpus where agent-written doctrine and anchor memories feed an LLM answerer under matched token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-Level Memory on Real Agent Traces
- Success threshold: At least 10 percentage point absolute task-accuracy gain over flat top-k on both-required tasks, no more than 3 percentage point regression on single-level/no-memory tasks, and consistent gains across at least three random seeds or trace splits.
- Stop condition: Stop if the two-level method fails to beat flat top-k by 5 percentage points on both-required tasks or introduces more than 5 percentage points regression on single-level/no-memory tasks.

## Evidence references

- Artifact root: `<local-path>/projects/two-level-agent-memory-anchors-plus-operator-doctrine-4fb7f3f91592`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
