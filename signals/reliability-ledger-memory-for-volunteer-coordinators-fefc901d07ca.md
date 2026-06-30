# Reliability Ledger Memory for Volunteer Coordinators

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `reliability-ledger-memory-for-volunteer-coordinators-fefc901d07ca`
Run ID: `reliability-ledger-memory-for-volunteer-coordinators-fefc901d07ca-20260610T145121821263+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b0deda3113ea

## What looked useful

Reliability memory is useful only when coupled to burden balancing. A naive reliability ledger overuses high-posterior volunteers and underperforms simple recency/fairness baselines; a balanced ledger reduced uncovered shifts by 0.0620 absolute versus random, 0.0239 versus fair rotation, and 0.0155 versus recency in paired synthetic validation.

## Boundaries and scale limits

Synthetic-only evidence; no real volunteer attendance logs, coordinator workflow replay, privacy review, consent process, or prospective field trial. The balanced ledger still increases assignment concentration relative to random, fair rotation, and recency baselines.

## Claim scope

In a deterministic synthetic repeated-shift benchmark with 300 paired trials, 120 days, 70 volunteers, and 8 slots/day, a reliability-ledger scheduler with explicit assignment balancing reduced uncovered shifts versus random, fair-rotation, recency, and naive ledger baselines.

## Why it stopped

The mechanism is supported in a synthetic proxy, but direct real-world evidence is missing and the fairness/burden tradeoff remains unresolved.

## Recommended next action

Stop this run as no-paper useful signal; next evaluate the balanced ledger on consented real or realistic trace replay before making any field or paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace Replay of Balanced Reliability Ledger for Volunteer Shift Coverage
- Success threshold: Balanced ledger beats recency by >= 0.01 absolute uncovered-rate reduction with paired 95% CI excluding zero, while assignment Gini is no more than 0.10 above recency or an agreed operational fairness bound.
- Stop condition: Stop if balanced ledger fails to beat recency on uncovered shifts, or if the coverage gain requires assignment concentration above the fairness bound.

## Evidence references

- Artifact root: `<local-path>/projects/reliability-ledger-memory-for-volunteer-coordinators-fefc901d07ca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
