# Gradient Sketch Verification Lottery for CPU Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-sketch-verification-lottery-for-cpu-volunteer-training-e63c4316b305`
Run ID: `gradient-sketch-verification-lottery-for-cpu-volunteer-training-e63c4316b305-20260628T191822084893+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/68f1afa29ba0

## What looked useful

Coordinate-sketch audits applied to every submission matched full verification under dense sign-flip attacks at 6.25% coordinate recomputation cost, but lottery-only sparse audits detected roughly only the audited fraction and failed to preserve training quality under persistent dense attacks. Sparse attacks can evade sampled coordinates, with sketch_all_k128 detecting about 73% in the stress run.

## Boundaries and scale limits

No real distributed volunteers, no deep-model benchmark, no cryptographic commitment protocol, no adaptive adversary, no network/churn/economic-deterrence effects. Main dense attack used 5 seeds; sparse stress used 3 seeds.

## Claim scope

Synthetic CPU logistic-regression volunteer-training proxy with assigned minibatches, 20% malicious workers, dense sign-flip and sparse-spike gradient corruptions, and verifier-side sampled-coordinate gradient recomputation.

## Why it stopped

Proxy evidence is sufficient to reject sparse lottery auditing as a standalone defense in the tested setting, while supporting only a scoped mechanism signal for sketch-every-submission verification.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded work should test sketch-every-submission plus robust aggregation and hidden audit-coordinate commitments on a small deep-model CPU benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sketch-Every-Submission Verification with Robust Aggregation on a Small Deep Model
- Success threshold: Within 2 percentage points of full-verification validation accuracy while using less than 15% verifier coordinate recomputation cost and detecting or neutralizing at least 90% of malicious impact across dense and sparse attack settings.
- Stop condition: Stop if sketch plus robust aggregation is more than 5 percentage points below full verification on validation accuracy, exceeds 15% coordinate recomputation cost, or sparse/small-norm attacks consistently evade detection and degrade accuracy by more than 5 points.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-sketch-verification-lottery-for-cpu-volunteer-training-e63c4316b305`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
