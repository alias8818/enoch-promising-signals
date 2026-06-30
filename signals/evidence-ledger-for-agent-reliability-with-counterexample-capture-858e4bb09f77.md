# Evidence ledger for agent reliability with counterexample capture

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-for-agent-reliability-with-counterexample-capture-858e4bb09f77`
Run ID: `evidence-ledger-for-agent-reliability-with-counterexample-capture-858e4bb09f77-20260609T025205329119+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/c722187ae2f8

## What looked useful

Counterexample ledger discovered a mean 0.8958 of planted hidden failure modes, improved stress Brier by 0.0736 and stress failure AUC by 0.2305, and reduced stress brittle-slice MAE by 0.2307, but worsened in-distribution Brier by 0.0017 and ECE by 0.0474.

## Boundaries and scale limits

128 deterministic synthetic seeds only; no real agent traces, no human labels, no production drift, and only a simple per-family baseline. Results support mechanism exploration, not deployment or paper-grade reliability claims.

## Claim scope

Synthetic feature-pattern agent traces show that counterexample capture improves shifted stress-set reliability estimates and brittle-slice failure triage, while worsening average in-distribution calibration versus a naive per-family success-rate ledger.

## Why it stopped

No-paper useful signal: the evidence is synthetic and mixed, with stress and brittle-slice gains but in-distribution calibration regression.

## Recommended next action

Run a bounded real-trace or high-fidelity agent-trace follow-up comparing counterexample capture against calibrated feature/logistic and hierarchical reliability baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace counterexample ledger calibration study
- Success threshold: Counterexample ledger or calibrated variant improves shifted/stress Brier by at least 0.03 and failure AUC by at least 0.08 over the strongest calibrated baseline, while in-distribution ECE degrades by no more than 0.01.
- Stop condition: Stop if real-trace evaluation cannot beat the strongest calibrated baseline on stress Brier or failure AUC, or if in-distribution ECE degradation exceeds 0.03 after shrinkage/calibration tuning.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-agent-reliability-with-counterexample-capture-858e4bb09f77`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
