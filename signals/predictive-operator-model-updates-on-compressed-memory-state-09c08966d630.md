# Predictive Operator-Model Updates on Compressed Memory State

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `predictive-operator-model-updates-on-compressed-memory-state-09c08966d630`
Run ID: `predictive-operator-model-updates-on-compressed-memory-state-09c08966d630-20260629T023902061844+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ed224b707225

## What looked useful

The predictive compressed-delta strategy beat compressed_online in only 1 of 6 main scenario/compression cells and had negative mean regret delta at all tested momentum values. Full uncompressed online learning was substantially better in every cell, indicating compression loss dominates the simple predictive forecast.

## Boundaries and scale limits

No real operator traces, private payloads, LLM calls, learned compression, or end-to-end model training were used. Results are an early proxy falsification of this simple update rule, not a universal rejection of predictive memory updates.

## Claim scope

Synthetic repeated-task routing proxy with 12-dimensional hidden task features compressed to 3 or 6 dimensions, 4 operators, 3 drift regimes, 24 seeds, and online bandit feedback. The tested mechanism is a one-step compressed weight-delta forecast before operator selection.

## Why it stopped

Proxy/early falsification: the tested predictive update failed to robustly improve regret versus the compressed online control across drift regimes and momentum ablations.

## Recommended next action

Stop this simple compressed-delta approach as no-paper evidence; any next attempt should replace the heuristic delta forecast with a learned transition model and test it on the same synthetic harness before using real traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Transition Predictor for Compressed Operator Memory
- Success threshold: Predictive learned transition reduces mean regret versus compressed_online by at least 0.01 in 4 of 6 scenario/compression cells without increasing regret by more than 0.005 in any remaining cell.
- Stop condition: Stop if the learned transition model wins fewer than 3 of 6 cells or if gains vanish under a held-out seed set.

## Evidence references

- Artifact root: `<local-path>/projects/predictive-operator-model-updates-on-compressed-memory-state-09c08966d630`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
