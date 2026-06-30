# EntropyRouter_ModelCascade_CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropyrouter-modelcascade-cpu-6e6eed0e534c`
Run ID: `entropyrouter-modelcascade-cpu-6e6eed0e534c-20260603T212301038253+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7dfe5b51a415

## What looked useful

Entropy routing beat random routing in every tested setting. On UCI Letter with a 12-feature cheap model, 35% routing achieved 0.698 accuracy versus 0.658 random routing and 0.592 small-only accuracy, with an estimated 2.20x speedup versus big-only inference; big-only accuracy was 0.782.

## Boundaries and scale limits

This run did not test LLMs, transformer decoding, production serving overhead, calibration methods beyond raw entropy, or broad multi-dataset robustness. UCI Letter accuracy remained materially below the full big-model baseline at 20-35% route budgets.

## Claim scope

In NumPy CPU two-stage classification cascades on one synthetic mixture task and UCI Letter Recognition, cheap-model normalized entropy ranks examples better than random routing for deciding which inputs receive the stronger model at fixed route budgets.

## Why it stopped

No-paper useful signal: local proxy evidence supports entropy as better-than-random routing, but the real-data quality/speed frontier is not strong enough for a publication-grade CPU model-cascade claim.

## Recommended next action

Run a bounded deepen test on real transformer or compact language-model classification/QA workloads with calibrated entropy, fixed quality floors, and end-to-end CPU latency before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Entropy router on compact transformer CPU cascades
- Success threshold: Entropy cascade reaches at least 95% of big-model task metric with at least 1.5x measured end-to-end CPU speedup on both tasks and beats random routing by at least 2 percentage points at the selected route budget.
- Stop condition: Stop if entropy routing fails to beat random routing by 2 percentage points on either task or cannot meet the 95% quality floor at any route budget with at least 1.5x speedup.

## Evidence references

- Artifact root: `<local-path>/projects/entropyrouter-modelcascade-cpu-6e6eed0e534c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
