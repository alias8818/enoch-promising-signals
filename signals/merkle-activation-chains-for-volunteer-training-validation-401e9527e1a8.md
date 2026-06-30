# Merkle Activation Chains for Volunteer Training Validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-activation-chains-for-volunteer-training-validation-401e9527e1a8`
Run ID: `merkle-activation-chains-for-volunteer-training-validation-401e9527e1a8-20260531T120832903935+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9589fd5d43ed

## What looked useful

Merkle activation chains are useful as an audit ledger but are not an independent volunteer-training validator. They catch unrechained post-hoc edits, but a malicious volunteer can re-chain false commitments unless verifier recomputation or an additional challenge protocol is used. Naive every-step activation hashing cut toy GPU throughput from 3149.7 to 451.7 steps/s.

## Boundaries and scale limits

Tested only 300 synthetic training steps on one small MLP with naive CPU SHA-256 hashing of GPU activation copies; not tested on real volunteer infrastructure, large models, hostile kernels, multi-node training, or unpredictable challenge protocols.

## Claim scope

On a small synthetic PyTorch CUDA MLP workload, Merkle-chained activation commitments worked as tamper-evident training trace logs and enabled recomputation-based detection of an injected false activation root, but structural chain verification alone accepted a self-consistent forged chain.

## Why it stopped

Proxy early falsification of the strong validation claim: structural Merkle activation chains alone accepted a self-consistent forged chain, so they do not validate volunteer training without recomputation or an added challenge mechanism.

## Recommended next action

Stop this standalone validation claim; a bounded follow-up should test unpredictable sampled recomputation/challenge protocols that preserve tamper-evidence while reducing overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Unpredictable Challenge Audits for Merkle Activation Chains
- Success threshold: At least 95% detection of injected isolated and burst faults at <=10% recomputation audit rate with <=20% end-to-end throughput overhead on the bounded model.
- Stop condition: Stop if self-consistent forged volunteers still pass challenged verification, or if overhead remains above 50% at audit rates needed for 95% detection.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-activation-chains-for-volunteer-training-validation-401e9527e1a8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
