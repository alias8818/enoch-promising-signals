# Merkle activation attestation for spoofed update detection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-activation-attestation-for-spoofed-update-detection-bd2abf518a78`
Run ID: `merkle-activation-attestation-for-spoofed-update-detection-bd2abf518a78-20260527T161013189431+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/05d9de47723a

## What looked useful

Broad and sparse weight spoofs were detected in 400/400 trials at every challenge count with 0/2800 honest-control false detections, but a dormant trigger was detected only 117/400 times at 64 random challenges and 400/400 times with trigger-aware challenges.

## Boundaries and scale limits

Toy CPU-only MLP benchmark; no transformer-scale serving, real supply-chain integration, remote attestation, hardware nondeterminism, adaptive adversary, or secret challenge protocol was tested.

## Claim scope

In a synthetic 64-128-96-32 ReLU MLP, Merkle roots over quantized internal activations detect spoofed model updates when private challenges induce activation differences.

## Why it stopped

Synthetic proxy evidence supports the mechanism for activation-visible spoofing but also shows random challenges can miss dormant input-conditional spoofing; this is useful no-paper evidence, not full validation.

## Recommended next action

Stop paper work for this run; run a bounded deepen test on a small real model update with runtime nondeterminism and challenge sets designed to cover rare spoofed behavior.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model activation attestation under nondeterminism and rare-trigger challenge coverage
- Success threshold: At least 99% detection of activation-visible unauthorized edits with no more than 0.1% honest false positives, plus quantified detection improvement for rare triggers when using targeted challenges versus random challenges.
- Stop condition: Stop if benign nondeterminism causes more than 1% false positives after reasonable quantization/tolerance tuning, or if unauthorized activation-visible edits are detected in less than 95% of trials at 64 challenges.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-activation-attestation-for-spoofed-update-detection-bd2abf518a78`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
