# Counter-Example Ledger: Negative-Memory Layer Reduces Repeated Failures

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `counter-example-ledger-negative-memory-layer-reduces-repeated-failures-48876d31d9e2`
Run ID: `counter-example-ledger-negative-memory-layer-reduces-repeated-failures-48876d31d9e2-20260611T184359910258+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bfc61bad5e15

## What looked useful

Across 300 seeds and 1,200 episodes per seed, negative ledger repeat failures per episode were 0.0566 stationary, 0.1595 mild_drift, and 0.3892 reversal, lower than positive-only at 0.1650, 0.2819, and 0.5410. Paired bootstrap 95% CIs for negative-ledger minus positive-only repeat failures per episode were strictly below zero in all regimes.

## Boundaries and scale limits

Evidence is synthetic and symbolic, not a real LLM-agent, production workflow, or model-training result. It does not test semantic retrieval, memory pruning, tool-use recovery, user-visible quality, or production memory overhead.

## Claim scope

In a synthetic repeated-task decision benchmark with 32 task families and 8 actions, a negative-memory counter-example ledger reduced repeated failures versus no-memory and positive-only-memory baselines across stationary, mild-drift, and full-reversal regimes.

## Why it stopped

Closed as no-paper useful signal because the evidence supports the mechanism only in a synthetic proxy benchmark, not in a direct LLM-agent or production workflow setting.

## Recommended next action

Run a bounded real LLM-agent deepen test on repeated tool-use or coding failures with matched no-memory and positive-only-memory baselines before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent counter-example ledger on repeated tool-use failures
- Success threshold: Negative ledger reduces same-error recurrence by at least 25% versus positive-only memory with a bootstrap 95% CI below zero and no more than 2 percentage point task-success regression.
- Stop condition: Stop if same-error recurrence reduction versus positive-only memory is below 10%, the confidence interval crosses zero after the planned task budget, or success rate regresses by more than 2 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/counter-example-ledger-negative-memory-layer-reduces-repeated-failures-48876d31d9e2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
