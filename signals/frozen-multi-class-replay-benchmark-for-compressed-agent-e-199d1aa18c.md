# Frozen multi-class replay benchmark for compressed agent evidence ledgers

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `frozen-multi-class-replay-benchmark-for-compressed-agent-e-199d1aa18c`
Run ID: `frozen-multi-class-replay-benchmark-for-compressed-agent-e-199d1aa18c-20260530T062350960430+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Compressed State Evidence Ledger for CPU Agent Safety: enoch://control-plane/projects/compressed-state-evidence-ledger-for-cpu-agent-safety-cddb89afe499/runs/compressed-state-evidence-ledger-for-cpu-agent-safety-cddb89afe499-20260529T143610646387+0000
- Parent run decision: Real-trace replay evaluation for compressed agent evidence ledgers: enoch://control-plane/projects/real-trace-replay-evaluation-for-compressed-agent-evidence-0b01e4c2a2/runs/real-trace-replay-evaluation-for-compressed-agent-evidence-0b01e4c2a2-20260529T191331016239+0000

## What looked useful

At the 16-event target budget, class_stratified_topk reached macro-F1 0.1498 +/- 0.0070 versus 0.7396 +/- 0.0090 for random_reservoir and 0.2197 +/- 0.0077 for global_topk, despite 6x event compression. Paired fixed-seed deltas were -0.5898 versus random reservoir and -0.0699 versus global top-k. Random reservoir was the best lossy method at every tested budget.

## Boundaries and scale limits

Synthetic ledgers only; no real agent traces, no production replay stack, no learned semantic compressor, and no task/model diversity beyond the local generated benchmark. The result is a medium confirmation negative for the tested mechanism, not a universal impossibility claim for all compressed evidence ledgers.

## Claim scope

In a fixed-seed synthetic 8-class frozen replay benchmark with 96-event scored evidence ledgers and a frozen multinomial replay model, naive class-hint-stratified top-score event compression does not preserve replay decisions better than generic lossy controls at equal event budgets.

## Why it stopped

Tier 2 fixed-seed medium confirmation directly falsified the stated success threshold for the tested class-aware top-score compressed ledger mechanism.

## Recommended next action

Stop this class-stratified top-score compressor line as no-paper evidence; only revisit if a materially different calibration-aware or learned compressor is available and can be tested on real agent traces.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/frozen-multi-class-replay-benchmark-for-compressed-agent-e-199d1aa18c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
