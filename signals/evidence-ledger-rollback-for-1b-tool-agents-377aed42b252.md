# Evidence-ledger rollback for 1B tool agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-rollback-for-1b-tool-agents-377aed42b252`
Run ID: `evidence-ledger-rollback-for-1b-tool-agents-377aed42b252-20260528T100013431537+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a77778913927

## What looked useful

Ledger rollback raised success by a mean 0.4101 over no rollback across independent-fault points and reached 0.9254 success at 20% faults versus 0.1722 without rollback. Under 80% sticky corrupted re-query behavior, mean lift fell to 0.0499 while tool-call overhead increased, showing rollback needs source diversity or escalation for correlated bad evidence.

## Boundaries and scale limits

No real 1B-parameter model, production agent harness, human-authored task set, real tool APIs, latency stack, or long-horizon traces were tested. Evidence is limited to deterministic synthetic CPU simulations with 5,000 episodes per fault-rate point.

## Claim scope

Synthetic 8-hop arithmetic tool-agent trajectories with injected tool-observation faults show that dependency-aware evidence-ledger rollback improves correctness over no rollback and retry-last baselines when bad observations are independently recoverable, but provides only small gains under correlated/sticky tool faults.

## Why it stopped

No-paper useful signal: synthetic evidence supports the mechanism under independently recoverable faults and identifies a correlated-fault boundary, but it is proxy evidence rather than direct validation for 1B tool agents.

## Recommended next action

Run a bounded direct-evidence follow-up with a small real tool-agent harness or open 1B-class model, injected API faults, and the same baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct tool-agent rollback test with injected API faults
- Success threshold: At 5-10% independently recoverable injected tool faults, ledger rollback improves task success by at least 10 percentage points over the strongest retry baseline with less than 2x mean tool-call cost, while the sticky-fault arm documents whether escalation is required.
- Stop condition: Stop if the real-agent harness shows less than 5 percentage points improvement over retry baselines at 5-10% independent faults or if rollback false positives exceed 5% on zero-fault tasks.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-for-1b-tool-agents-377aed42b252`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
