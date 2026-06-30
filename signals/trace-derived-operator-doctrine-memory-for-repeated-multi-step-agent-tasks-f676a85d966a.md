# Trace-Derived Operator-Doctrine Memory for Repeated Multi-Step Agent Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trace-derived-operator-doctrine-memory-for-repeated-multi-step-agent-tasks-f676a85d966a`
Run ID: `trace-derived-operator-doctrine-memory-for-repeated-multi-step-agent-tasks-f676a85d966a-20260613T234312112955+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d4d69433c599

## What looked useful

Across 30 seeds with 240 prior traces and 160 held-out tasks per seed, doctrine memory reached 0.9698 mean success versus 0.1508 for no memory and 0.9392 for raw trace retrieval. Mean violations were 0.4048 versus 2.4892 and 0.6835 respectively. A train-size sweep from 20 to 240 prior traces showed doctrine memory consistently above raw retrieval by 0.0117 to 0.0637 success rate.

## Boundaries and scale limits

Synthetic deterministic task generator only; no real LLM agent traces, no human operator labels, no live A/B test, no long-horizon project memory, and no validation on natural code/research workflows.

## Claim scope

In a controlled synthetic repeated-task benchmark, compact doctrine rules extracted contrastively from prior successful traces improved held-out multi-step task success and reduced doctrine violations versus no memory, with a smaller but consistent improvement over raw successful-trace retrieval.

## Why it stopped

No-paper useful signal: the local result is a synthetic mechanism test, not direct validation on real repeated multi-step agent tasks.

## Recommended next action

Run a bounded real-trace replay study using anonymized prior agent traces with operator-correctness labels, comparing extracted doctrine memory against raw trace retrieval and handwritten memory on the same repeated task families.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Replay of Operator-Doctrine Memory
- Success threshold: Doctrine memory improves held-out task success by at least 5 percentage points over raw trace retrieval or reduces operator-doctrine violations by at least 25% without lowering success.
- Stop condition: Stop if fewer than 100 labeled real traces are available, if doctrine extraction fails to recover stable rules across folds, or if doctrine memory does not beat raw trace retrieval on either success or violation reduction.

## Evidence references

- Artifact root: `<local-path>/projects/trace-derived-operator-doctrine-memory-for-repeated-multi-step-agent-tasks-f676a85d966a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
