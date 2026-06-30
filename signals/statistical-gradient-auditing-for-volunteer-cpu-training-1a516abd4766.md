# Statistical gradient auditing for volunteer CPU training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `statistical-gradient-auditing-for-volunteer-cpu-training-1a516abd4766`
Run ID: `statistical-gradient-auditing-for-volunteer-cpu-training-1a516abd4766-20260608T203810967333+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0ff866bd4fb9

## What looked useful

Projection audits were robust against sparse and sign-flip attacks that norm-only checks missed; sensitivity runs show a practical detection boundary where 1% progress cancellation remains weak but 2% cancellation is caught by 64-coordinate or 64-projection audits at roughly 96-98% TPR under the synthetic assumptions.

## Boundaries and scale limits

No real volunteer CPU deployment, no neural-network training loop, no network or scheduling overhead, no non-IID worker data, no collusion, and no adaptive adversary that sees audit probes before committing a gradient were tested.

## Claim scope

In a synthetic logistic-regression gradient-report simulation, hidden coordinate and random-projection audits calibrated at 1% false-positive rate detect broad, sign-flip, sparse 1%, and progress-canceling gradient corruption with small audit budgets when corruption is at least about 2% of the gradient scale; norm-only checks fail on direction-preserving-norm attacks.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic and mechanism-level, not direct validation of volunteer CPU training.

## Recommended next action

Build a bounded volunteer-style prototype with hidden post-commit audit probes on a small neural model and measure TPR, FPR, convergence impact, and audit overhead under non-IID worker shards.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Post-commit gradient audits in a real volunteer-style CPU training prototype
- Success threshold: At least 90% TPR at 1% FPR for 2% progress cancellation and sparse 1% sabotage, with less than 10% audit overhead and no material honest convergence degradation in the bounded prototype.
- Stop condition: Stop if hidden audits cannot exceed 50% TPR at 1% FPR for 2% progress cancellation under the prototype, or if audit overhead exceeds 25% at the smallest budget that reaches 90% TPR.

## Evidence references

- Artifact root: `<local-path>/projects/statistical-gradient-auditing-for-volunteer-cpu-training-1a516abd4766`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
