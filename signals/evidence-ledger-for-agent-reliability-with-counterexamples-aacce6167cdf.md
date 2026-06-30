# Evidence Ledger for Agent Reliability with Counterexamples

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-for-agent-reliability-with-counterexamples-aacce6167cdf`
Run ID: `evidence-ledger-for-agent-reliability-with-counterexamples-aacce6167cdf-20260608T120452783532+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/715307f7e303

## What looked useful

The ledger is useful as a conservative release gate for detecting rare failure pockets, not as a calibrated reliability estimator. Main run false certifications: naive 598/796 certified, stratified mean 16/53, counterexample ledger 0/3; ledger MAE was worse at 0.146 versus 0.039 for naive.

## Boundaries and scale limits

Synthetic-only CPU Monte Carlo: 5,000-agent main run plus 2,000-agent ablations. No real agent traces, no live counterexample generation, no human task taxonomy validation, and no full deployment reliability study.

## Claim scope

On synthetic pass/fail agent-evaluation traces with hidden risky strata and mismatched test/deployment distributions, a conservative counterexample-aware evidence ledger reduced false high-reliability certification versus naive aggregate estimation, but at the cost of severe underestimation and poor calibration.

## Why it stopped

Proxy-only useful signal: synthetic evidence supports a conservative gating mechanism but does not directly validate real agent reliability or counterexample discovery.

## Recommended next action

Run a bounded deepen follow-up on real or semi-real agent traces with pre-registered strata and held-out deployment weights; do not write a paper from this synthetic proxy alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Counterexample Ledger on Real Agent Evaluation Traces
- Success threshold: At least 50% lower false-certification rate than the best non-ledger baseline at the same 0.90 reliability threshold, with no more than 2x reduction in true certification rate and calibration error reported.
- Stop condition: Stop if the ledger fails to reduce false certification versus stratified/risk-control baselines or if the certification rate collapses enough to make the gate operationally unusable.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-agent-reliability-with-counterexamples-aacce6167cdf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
