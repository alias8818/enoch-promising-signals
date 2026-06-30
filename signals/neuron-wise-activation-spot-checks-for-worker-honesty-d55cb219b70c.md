# Neuron-Wise Activation Spot-Checks for Worker Honesty

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `neuron-wise-activation-spot-checks-for-worker-honesty-d55cb219b70c`
Run ID: `neuron-wise-activation-spot-checks-for-worker-honesty-d55cb219b70c-20260521T231935074874+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f075905c6213

## What looked useful

Random neuron spot-checks are a cheap detector for broad activation lies, but they should not be treated as a standalone honesty guarantee: 1% corruption with k=8 checks was detected only 4.24%-7.51% of the time, while 20% corruption with k=32 checks was detected 96.76%-99.87% of the time.

## Boundaries and scale limits

Single small MLP, synthetic teacher-generated labels, one hidden layer, CPU-only local run, four simple fabrication strategies, no transformer activations, no adaptive attacker with pre-knowledge of sampled neurons, no cryptographic commitment protocol, and no end-to-end distributed worker setting.

## Claim scope

In a synthetic 4096-example ReLU MLP activation audit, random neuron-wise recomputation checks detected dense activation fabrication reliably but had low power against sparse 1%-5% activation-cell tampering at audit budgets up to 64 neurons per example.

## Why it stopped

The local evidence is a useful mechanism signal but not publication-grade: it supports dense-fabrication detection and exposes sparse-tampering weakness in a toy MLP setting.

## Recommended next action

Run a bounded transformer-layer follow-up comparing random neuron checks against salience-targeted checks under sparse, task-impactful activation tampering.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Targeted versus random transformer activation spot-checks under sparse tampering
- Success threshold: At k<=64 checked neurons per token or example, targeted checks improve detection of sparse task-impactful tampering by at least 2x over random checks while keeping honest false positives below 1%.
- Stop condition: Stop if targeted checks fail to improve sparse-tampering detection by at least 25% relative over random checks or if honest false positives exceed 1% at practical tolerances.

## Evidence references

- Artifact root: `<local-path>/projects/neuron-wise-activation-spot-checks-for-worker-honesty-d55cb219b70c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
