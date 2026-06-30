# Merkle-Grad: Cheating-Resistant CPU Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-grad-cheating-resistant-cpu-volunteer-training-a6dd4ce7f2b7`
Run ID: `merkle-grad-cheating-resistant-cpu-volunteer-training-a6dd4ce7f2b7-20260608T105414136827+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8b444109bef9

## What looked useful

Merkle-sum commitments provide a practical aggregate-binding mechanism and cheap sampled audit verification, but sparse cheating is only weakly detected unless audit coverage is high: with 1% corrupted leaves, auditing 64/256 leaves detected about 59.7%; with 5% corruption, auditing 32/256 leaves detected about 83.3% and auditing 64/256 detected about 97.3%.

## Boundaries and scale limits

Tested only synthetic NumPy logistic-regression gradients on one CPU worker: 4,096 rows, 512 features, 256 leaves, 300 detection trials per setting. Not tested on neural network convergence, heterogeneous volunteer CPUs, networked workers, adversarial economics, Sybil/collusion resistance, or large-scale training.

## Claim scope

On a synthetic CPU logistic-regression workload with 256 gradient leaves, a Merkle-sum tree can bind a submitted aggregate gradient to committed per-leaf gradients, and randomized recomputation audits detect corrupted leaves at the expected sampling probability.

## Why it stopped

The current result is a bounded synthetic mechanism test, not full validation of cheating-resistant volunteer training; sparse corruption remains insufficiently detected at low audit rates.

## Recommended next action

Stop this run as a no-paper useful signal; next, run a bounded multi-process small-model training follow-up that compares audited volunteer shards against a trusted baseline and includes low-magnitude adversarial bias attacks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Audited multi-process small-model training with bias attacks
- Success threshold: Audited training reaches within 2% relative final validation loss or accuracy of the trusted baseline across three seeds, while repeated-round detection reaches at least 95% for 5% corrupted leaves with measured overhead below 2x.
- Stop condition: Stop if audited training diverges from the trusted baseline beyond 5% relative final metric in clean no-attack runs, if deterministic recomputation fails across worker processes, or if overhead exceeds 3x before adversarial tests.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-grad-cheating-resistant-cpu-volunteer-training-a6dd4ce7f2b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
