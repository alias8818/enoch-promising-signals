# Adaptive-source and fairness stress test for evidence-ledger queue admission

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adaptive-source-and-fairness-stress-test-for-evidence-ledg-f29831c3bc`
Run ID: `adaptive-source-and-fairness-stress-test-for-evidence-ledg-f29831c3bc-20260620T201201440855+0000`

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

- Parent run decision: Evidence-Ledger-Gated Queue Admission Simulation: enoch://control-plane/projects/evidence-ledger-gated-queue-admission-simulation-295b8c09eba4/runs/evidence-ledger-gated-queue-admission-simulation-295b8c09eba4-20260620T092704033765+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/65f84ab55b3d

## What looked useful

Adaptive source reputation suppressed adversarial flooding, but source adaptation alone starved minority sources; adding a per-source cap and minority floor preserved adversarial suppression while restoring minority admission share.

## Boundaries and scale limits

The evidence is limited to a small controlled simulator. It does not validate real evidence corpora, deployed ledger traces, delayed or noisy adjudication, adaptive adversaries, non-stationary source reliability, or production queue dynamics.

## Claim scope

In a deterministic, synthetic, admission-level stress test with 60 seeds, 120 batches per seed, fixed capacity 20, source identity, latent validity, adversarial flooding, and minority-source underrepresentation, adaptive source reputation plus explicit fairness constraints reduced adversarial admissions by 99.15% versus the best non-adaptive baseline while preserving precision and raising minority-source retention above the candidate-stream share.

## Why it stopped

Tier 1 controlled direct test completed and met the stated mechanism threshold, but the evidence is synthetic and small-scale, so it is no-paper useful signal rather than publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up with delayed/noisy audit feedback and an adaptive adversary to test whether adaptive-fair admission remains stable when source reputation is learned from imperfect lagged labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Delayed-audit adaptive adversary stress test for adaptive-fair ledger admission
- Success threshold: Adaptive-fair adversarial admission share is at least 50% lower than the best non-adaptive baseline, valid precision is no more than 5 percentage points below the best non-adaptive baseline, and minority retention is at least 0.80 across 60 seeds under delayed/noisy feedback.
- Stop condition: Stop if adaptive-fair fails any threshold in the delayed/noisy adaptive-adversary setting or if performance depends on a single narrow fairness hyperparameter setting.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-source-and-fairness-stress-test-for-evidence-ledg-f29831c3bc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
