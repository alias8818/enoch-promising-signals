# Cheating-Resistant Volunteer Training: Local Toy Validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cheating-resistant-volunteer-training-local-toy-validation-94e2b14b7e30`
Run ID: `cheating-resistant-volunteer-training-local-toy-validation-94e2b14b7e30-20260613T060557763397+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/62aab312ff43

## What looked useful

Audit probes appear useful for certifying that assigned computation was performed, but they do not certify that non-audit training gradients are benign. Severe lazy/replay auditing recovered mean accuracy from 0.8509 to 0.8644 versus a 0.8657 clean baseline, while 50% adaptive poisoning passed the audit and reduced mean accuracy to 0.4738.

## Boundaries and scale limits

Toy synthetic data only; no real volunteer network, no heterogeneous hardware, no privacy protocol, no large model, no collusion, and no defense against adaptive poisoners that compute audits honestly while corrupting training gradients.

## Claim scope

In a local synthetic logistic-regression volunteer-training simulation, hidden projected audit gradients rejected lazy random and stale replay submissions with zero honest false rejects across the tested seeds, and preserved near-clean accuracy under up to 80% lazy/replay cheaters.

## Why it stopped

Local toy validation produced a useful mixed result but not direct publication-grade evidence; the tested audit is effective against lazy/replay cheating and ineffective against adaptive poisoning.

## Recommended next action

Run a bounded follow-up combining hidden audit probes with robust aggregation against adaptive poisoning, using the same toy setup plus trimmed mean or coordinate median baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Audit Probes Plus Robust Aggregation Against Adaptive Volunteer Poisoning
- Success threshold: Audit-plus-robust keeps lazy/replay detection at or above 0.99 with honest false rejection at or below 0.01 and improves 50% adaptive-poison mean accuracy by at least 0.20 over audit-only.
- Stop condition: Stop as a negative result if robust aggregation does not improve 50% adaptive-poison mean accuracy by at least 0.10 over audit-only or if it introduces more than 0.05 honest-update false rejection/effective loss.

## Evidence references

- Artifact root: `<local-path>/projects/cheating-resistant-volunteer-training-local-toy-validation-94e2b14b7e30`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
