# Operator-Doctrine Memory: Distilling Reusable Task Heuristics from Failed Traces

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `operator-doctrine-memory-distilling-reusable-task-heuristics-from-failed-traces-802d6fc5a243`
Run ID: `operator-doctrine-memory-distilling-reusable-task-heuristics-from-failed-traces-802d6fc5a243-20260630T031644502039+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/10b86387d25e

## What looked useful

The tested doctrine-memory mechanism underperformed nearest-trace retrieval by 16.5 percentage points on average and keyword bag-of-words by 8.4 percentage points on average. The run also found and fixed a label-leakage hazard in trace IDs, showing that future operator-memory studies need strict leakage controls and simple baselines.

## Boundaries and scale limits

Synthetic traces only; no real failed-trace corpus, no human doctrine-quality review, no prospective autonomous-task replay, no action-quality scoring beyond classifying the failure mode. CPU-only run completed in 0.055 seconds and does not exercise GB10 scale.

## Claim scope

In a deterministic synthetic proxy with 12 operator failure modes, 48 training traces, and 36 held-out paraphrase traces, a simple token-trigger doctrine-memory distillation did not outperform nearest-trace memory or keyword bag-of-words baselines for failure-mode classification.

## Why it stopped

Corrected synthetic proxy showed doctrine-memory accuracy 0.5278 versus nearest-trace 0.6944 and keyword bag-of-words 0.6111; this is an early proxy falsification, not a full real-world validation.

## Recommended next action

Stop this run as a proxy negative; the concrete next action is a bounded real-trace follow-up that labels at least 50 failed traces and compares doctrine-memory against nearest-trace and keyword baselines on action-quality and recurrence-reduction metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Failed-Trace Doctrine Memory Evaluation
- Success threshold: Doctrine-memory must improve held-out corrective-action F1 by at least 10 percentage points over nearest-trace retrieval with no worse than a 5 percentage point increase in false-positive action recommendations.
- Stop condition: Stop if leakage-controlled doctrine-memory does not beat nearest-trace retrieval on corrective-action F1 or if human reviewers judge more than 25% of extracted doctrine rules non-actionable.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-distilling-reusable-task-heuristics-from-failed-traces-802d6fc5a243`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
