# Verifiable Gradient Audits for Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `verifiable-gradient-audits-for-volunteer-training-f79663a6d834`
Run ID: `verifiable-gradient-audits-for-volunteer-training-f79663a6d834-20260527T105513512134+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/01d3df5daa94

## What looked useful

Exact spot recomputation is a viable low-complexity audit primitive for catching incorrect volunteer gradients when the coordinator can deterministically reconstruct the worker minibatch. Detection probability tracks audit probability; 25% audit detected about 24-26% of malicious submissions across attack modes with about 8% local recomputation wall-time fraction in this toy simulator.

## Boundaries and scale limits

Synthetic data, small convex model, local single-process execution, deterministic minibatches, no network costs, no privacy layer, no robust aggregation baseline, no Sybil resistance, and no adaptive adversary that can predict or infer audit sampling.

## Claim scope

In a deterministic NumPy softmax-regression volunteer-training simulator with 16 workers, 25% malicious workers, 5 seeds, and exact spot recomputation, non-exact gradient submissions are detected at approximately the audit sampling rate. The clearest training benefit was for sign-flip attacks, where 25% audit improved final accuracy from 0.7847 to 0.8312 and full audit reached 0.8848.

## Why it stopped

No-paper useful signal: the mechanism worked in a synthetic simulator, but the evidence is not direct enough for a paper or full volunteer-training validation.

## Recommended next action

Run a bounded real-workload follow-up using PyTorch/FedAvg on MNIST or Fashion-MNIST, comparing exact spot audits against no audit and robust aggregation under the same malicious-worker schedule.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-workload spot recomputation audits for small FedAvg training
- Success threshold: At 10-25% audit rate, malicious detection rate must match the audit rate within 5 percentage points and final accuracy must recover at least 50% of the attack-induced accuracy drop versus no-audit attack baseline, without more than 30% coordinator recomputation wall-time overhead.
- Stop condition: Stop as negative if detection deviates from the configured audit rate by more than 5 percentage points, if accuracy recovery is below 25% of the attack-induced drop, or if overhead exceeds 50% on the bounded workload.

## Evidence references

- Artifact root: `<local-path>/projects/verifiable-gradient-audits-for-volunteer-training-f79663a6d834`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
